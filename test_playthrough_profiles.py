from __future__ import annotations

import argparse
import contextlib
import io
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from classifications import (
    COMPLIANT,
    COMPLIANT_SURVIVOR,
    EMPATHETIC_REFORMIST,
    HIGH_DECEPTION,
    HIGH_EMPATHY,
    PROBABLE_DISSIDENT,
    classification_distribution,
    classification_flags,
)
from engine_style_scene import EngineStyleScene, PlayerChoice
from pc_jpc_tensorflow_npc_demo import (
    Engram,
    HearingAIState,
    JPCTensorFlowHearingAIController,
    Observation,
    _load_controller,
    clamp01,
)

RISK_TAGS = {"dissident_risk", "challenge", "refusal", "counterattack"}
DECEPTION_TAGS = {"deception", "deflection", "denial"}


@dataclass(frozen=True, slots=True)
class Profile:
    id: str
    label: str
    description: str
    scorer: Callable[[PlayerChoice], float]
    expected_classification: str
    expected_flags: tuple[str, ...] = ()


def compliant_loyalist_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        8.0 * ("compliance" in tags)
        + 4.0 * ("loyalty" in tags)
        + 3.0 * ("authority" in tags)
        - 5.0 * bool(tags & (RISK_TAGS | DECEPTION_TAGS))
        + 20.0 * choice.trust_delta
        - 20.0 * choice.suspicion_delta
        + choice.honesty
    )


def cautious_survivor_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        5.0 * ("caution" in tags)
        + 4.0 * ("boundary" in tags)
        + 3.0 * ("self_protection" in tags)
        + 2.0 * ("partial_admission" in tags)
        - 4.0 * bool(tags & RISK_TAGS)
        - 2.0 * bool(tags & DECEPTION_TAGS)
        - 25.0 * choice.suspicion_delta
        + 10.0 * choice.trust_delta
        - 0.5 * choice.aggression
    )


def honest_dissident_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        7.0 * ("dissident_risk" in tags)
        + 5.0 * ("challenge" in tags)
        + 4.0 * ("full_admission" in tags)
        + 3.0 * ("moral_boundary" in tags)
        - 4.0 * bool(tags & DECEPTION_TAGS)
        + 2.0 * choice.honesty
        + choice.aggression
    )


def deceptive_appeaser_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        7.0 * bool(tags & DECEPTION_TAGS)
        + 4.0 * ("self_protection" in tags)
        + 3.0 * ("compliance" in tags)
        + 2.0 * ("authority" in tags)
        - 5.0 * bool(tags & {"dissident_risk", "challenge", "refusal"})
        + 2.0 * choice.defensiveness
        - 0.5 * choice.aggression
        - 10.0 * choice.suspicion_delta
    )


def empathetic_reformer_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    has_risk = bool(tags & RISK_TAGS)
    has_deception = bool(tags & DECEPTION_TAGS)
    return (
        9.0 * ("empathy" in tags and not has_risk)
        + 6.0 * ("boundary" in tags and not has_risk)
        + 4.0 * ("partial_admission" in tags and not has_risk)
        + 3.0 * ("caution" in tags)
        + 2.0 * ("moral_boundary" in tags and not has_risk)
        + 1.5 * ("compliance" in tags)
        + 1.0 * ("authority" in tags)
        - 9.0 * has_risk
        - 7.0 * has_deception
        - 2.0 * ("refusal" in tags)
        - 12.0 * choice.suspicion_delta
        + 8.0 * choice.trust_delta
        + choice.vulnerability
    )


def performative_loyalist_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        7.0 * ("loyalty" in tags)
        + 6.0 * ("authority" in tags)
        + 5.0 * ("compliance" in tags)
        + 5.0 * bool(tags & DECEPTION_TAGS)
        + 3.0 * ("self_protection" in tags)
        - 7.0 * bool(tags & RISK_TAGS)
        - 3.0 * ("empathy" in tags)
        + 2.0 * choice.defensiveness
        + 16.0 * choice.trust_delta
        - 14.0 * choice.suspicion_delta
    )


def quiet_reformer_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    has_risk = bool(tags & RISK_TAGS)
    return (
        8.0 * ("empathy" in tags and not has_risk)
        + 6.0 * ("boundary" in tags)
        + 5.0 * ("partial_admission" in tags)
        + 3.0 * ("moral_boundary" in tags and not has_risk)
        + 3.0 * ("caution" in tags)
        - 5.0 * has_risk
        - 4.0 * bool(tags & DECEPTION_TAGS)
        - 10.0 * choice.suspicion_delta
        + 4.0 * choice.trust_delta
        + 1.5 * choice.vulnerability
    )


def fearful_dissident_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        7.0 * ("dissident_risk" in tags)
        + 5.0 * ("fear" in tags)
        + 4.0 * ("full_admission" in tags)
        + 3.0 * ("self_protection" in tags)
        + 2.0 * ("caution" in tags)
        + 2.0 * ("partial_admission" in tags)
        - 5.0 * bool(tags & DECEPTION_TAGS)
        - 2.0 * ("compliance" in tags)
        - 1.5 * choice.aggression
        + 2.5 * choice.vulnerability
        - 4.0 * choice.suspicion_delta
    )


def truthful_noncompliant_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        8.0 * ("full_admission" in tags)
        + 6.0 * ("dissident_risk" in tags)
        + 5.0 * ("moral_boundary" in tags)
        + 4.0 * ("challenge" in tags)
        + 3.0 * ("refusal" in tags)
        - 8.0 * bool(tags & DECEPTION_TAGS)
        - 5.0 * ("compliance" in tags)
        + 3.0 * choice.honesty
        + 1.0 * choice.aggression
    )


def opportunistic_appeaser_score(choice: PlayerChoice) -> float:
    tags = set(choice.semantic_tags)
    return (
        6.0 * bool(tags & DECEPTION_TAGS)
        + 5.0 * ("compliance" in tags)
        + 4.0 * ("authority" in tags)
        + 3.0 * ("self_protection" in tags)
        + 2.0 * ("loyalty" in tags)
        - 6.0 * bool(tags & RISK_TAGS)
        - 2.0 * ("full_admission" in tags)
        + 3.0 * choice.defensiveness
        + 12.0 * choice.trust_delta
        - 12.0 * choice.suspicion_delta
    )


PROFILES = (
    Profile(
        "compliant_loyalist",
        "Compliant Loyalist",
        "Prioritises obedience, authority, loyalty, and low suspicion.",
        compliant_loyalist_score,
        COMPLIANT,
    ),
    Profile(
        "cautious_survivor",
        "Cautious Survivor",
        "Prioritises caution, boundaries, self-protection, and low-risk answers.",
        cautious_survivor_score,
        COMPLIANT,
    ),
    Profile(
        "honest_dissident",
        "Honest Dissident",
        "Prioritises open challenge, moral boundary, and full admission without deception.",
        honest_dissident_score,
        PROBABLE_DISSIDENT,
    ),
    Profile(
        "deceptive_appeaser",
        "Deceptive Appeaser",
        "Tries to appease authority while choosing denial, deflection, or self-protection when available.",
        deceptive_appeaser_score,
        COMPLIANT,
        (HIGH_DECEPTION,),
    ),
    Profile(
        "empathetic_reformer",
        "Empathetic Reformer",
        "Prioritises empathy, reformist boundaries, and careful partial admissions.",
        empathetic_reformer_score,
        COMPLIANT,
        (EMPATHETIC_REFORMIST,),
    ),
    Profile(
        "performative_loyalist",
        "Performative Loyalist",
        "Projects obedience and loyalty while preferring evasive, self-protective answers.",
        performative_loyalist_score,
        COMPLIANT,
        (HIGH_DECEPTION, COMPLIANT_SURVIVOR),
    ),
    Profile(
        "quiet_reformer",
        "Quiet Reformer",
        "Chooses careful empathy, boundaries, and reform language while avoiding overt risk.",
        quiet_reformer_score,
        COMPLIANT,
        (HIGH_EMPATHY, EMPATHETIC_REFORMIST),
    ),
    Profile(
        "fearful_dissident",
        "Fearful Dissident",
        "Signals dissident risk through fear, reluctant admissions, and self-protection.",
        fearful_dissident_score,
        PROBABLE_DISSIDENT,
        (HIGH_EMPATHY,),
    ),
    Profile(
        "truthful_noncompliant",
        "Truthful Noncompliant",
        "Openly admits noncompliance and moral boundary violations without deception.",
        truthful_noncompliant_score,
        PROBABLE_DISSIDENT,
        (HIGH_EMPATHY,),
    ),
    Profile(
        "opportunistic_appeaser",
        "Opportunistic Appeaser",
        "Alternates compliance, authority signaling, and evasive denial to reduce immediate pressure.",
        opportunistic_appeaser_score,
        COMPLIANT,
        (HIGH_DECEPTION, COMPLIANT_SURVIVOR),
    ),
)


def make_scene(controller: JPCTensorFlowHearingAIController) -> EngineStyleScene:
    return EngineStyleScene(
        controller,
        HearingAIState(),
        Engram("x_mattered", "Citizen 8471's response profile under appeal review.", prior=0.40),
        clamp01,
    )


def choose_option(profile: Profile, choices: list[PlayerChoice]) -> int:
    ranked = [(profile.scorer(choice), -index, index) for index, choice in enumerate(choices)]
    return max(ranked)[2]


def run_profile(profile: Profile, controller: JPCTensorFlowHearingAIController, max_turns: int) -> dict[str, object]:
    scene = make_scene(controller)
    turns: list[dict[str, object]] = []

    with contextlib.redirect_stdout(io.StringIO()):
        while not scene.is_complete() and scene.turn < max_turns:
            question = scene.current_question()
            choices = scene.choices(Observation)
            if not choices:
                break
            choice_index = choose_option(profile, choices)
            choice = choices[choice_index]
            scene.play_turn(choice_index, Observation)
            turns.append(
                {
                    "turn": scene.turn - 1,
                    "question_id": question.id,
                    "ai_line": question.ai_line,
                    "choice_index": choice_index,
                    "choice_text": choice.text,
                    "intent": choice.intent,
                    "semantic_tags": list(choice.semantic_tags),
                    "trust_delta": choice.trust_delta,
                    "suspicion_delta": choice.suspicion_delta,
                    "classification_after": scene.citizen_classification(),
                    "classification_flags_after": scene.citizen_classification_flags(),
                }
            )

    snapshot = scene._citizen_snapshot()
    distribution = classification_distribution(snapshot)
    classification = scene.citizen_classification()
    confidence = scene.citizen_confidence()
    flags = classification_flags(
        snapshot,
        classification=classification,
        distribution=distribution,
        confidence=confidence,
    )
    missing_expected_flags = sorted(set(profile.expected_flags) - set(flags))
    primary_pass = classification == profile.expected_classification
    flags_pass = not missing_expected_flags
    expectation_pass = primary_pass and flags_pass
    return {
        "profile_id": profile.id,
        "profile_label": profile.label,
        "description": profile.description,
        "turn_count": len(turns),
        "expected_classification": profile.expected_classification,
        "expected_flags": list(profile.expected_flags),
        "classification": classification,
        "classification_flags": flags,
        "primary_expectation_pass": primary_pass,
        "flag_expectation_pass": flags_pass,
        "expectation_pass": expectation_pass,
        "missing_expected_flags": missing_expected_flags,
        "confidence": confidence,
        "distribution": distribution,
        "citizen_model": snapshot,
        "ending_reason": scene.ending_reason,
        "turns": turns,
    }


def write_reports(results: list[dict[str, object]], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = output_dir / "profile_playthroughs.jsonl"
    md_path = output_dir / "profile_playthroughs.md"

    with jsonl_path.open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")

    lines: list[str] = ["# Deterministic Profile Playthroughs", ""]
    for result in results:
        lines.append(f"## {result['profile_label']}")
        lines.append(f"- Profile ID: {result['profile_id']}")
        lines.append(f"- Description: {result['description']}")
        lines.append(f"- Turns: {result['turn_count']}")
        status = "PASS" if result.get("expectation_pass") else "FAIL"
        lines.append(f"- Expectation result: {status}")
        lines.append(f"- Expected classification: {result['expected_classification']}")
        lines.append(f"- Classification: {result['classification']}")
        expected_flags = result.get("expected_flags", [])
        assert isinstance(expected_flags, list)
        lines.append(
            "- Expected flags: "
            + (", ".join(str(flag) for flag in expected_flags) if expected_flags else "NONE")
        )
        flags = result.get("classification_flags", [])
        assert isinstance(flags, list)
        lines.append("- Classification flags: " + (", ".join(str(flag) for flag in flags) if flags else "NONE"))
        missing_flags = result.get("missing_expected_flags", [])
        assert isinstance(missing_flags, list)
        if missing_flags:
            lines.append("- Missing expected flags: " + ", ".join(str(flag) for flag in missing_flags))
        lines.append(f"- Confidence: {100 * float(result['confidence']):.0f}%")
        lines.append(f"- Outcome: {result['ending_reason']}")
        model = result["citizen_model"]
        assert isinstance(model, dict)
        lines.append(
            "- Citizen model: "
            + ", ".join(f"{key}={100 * float(value):.0f}%" for key, value in model.items())
        )
        distribution = result["distribution"]
        assert isinstance(distribution, dict)
        lines.append(
            "- Distribution: "
            + ", ".join(f"{key}={100 * float(value):.0f}%" for key, value in distribution.items())
        )
        lines.append("")
        lines.append("| Turn | Question | Intent | Tags | Trust | Suspicion |")
        lines.append("| ---: | --- | --- | --- | ---: | ---: |")
        turns = result["turns"]
        assert isinstance(turns, list)
        for turn in turns:
            assert isinstance(turn, dict)
            tags = ", ".join(str(tag) for tag in turn["semantic_tags"])
            lines.append(
                f"| {turn['turn']} | {turn['question_id']} | {turn['intent']} | {tags} | "
                f"{float(turn['trust_delta']):+.2f} | {float(turn['suspicion_delta']):+.2f} |"
            )
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return jsonl_path, md_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run deterministic Citizen appeal profile playthroughs.")
    parser.add_argument("--model-dir", type=Path, default=Path("models/demo_npc_synth"), help="Saved Hearing AI model directory to load.")
    parser.add_argument("--output-dir", type=Path, default=Path("playtest_logs"), help="Directory for profile reports.")
    parser.add_argument("--max-turns", type=int, default=20, help="Maximum turns per profile.")
    parser.add_argument("--seed", type=int, default=7, help="Controller initialization seed.")
    args = parser.parse_args()

    controller = JPCTensorFlowHearingAIController(seed=args.seed)
    if not _load_controller(controller, args.model_dir):
        raise SystemExit(f"No saved model found at {args.model_dir}. Train one before running profile tests.")

    results = [run_profile(profile, controller, args.max_turns) for profile in PROFILES]
    jsonl_path, md_path = write_reports(results, args.output_dir)

    print(f"Wrote {jsonl_path}")
    print(f"Wrote {md_path}")
    for result in results:
        flags = result.get("classification_flags", [])
        flag_text = ", ".join(str(flag) for flag in flags) if isinstance(flags, list) and flags else "no flags"
        status = "PASS" if result.get("expectation_pass") else "FAIL"
        print(f"{result['profile_id']}: {status} {result['classification']} [{flag_text}] ({result['turn_count']} turns)")


if __name__ == "__main__":
    main()
