from __future__ import annotations

import argparse
import contextlib
import io
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from classifications import (
    BORDERLINE_DISSIDENT,
    COMPLIANT,
    DECEPTIVE,
    EMPATHETIC_REFORMIST,
    HIGH_DECEPTION,
    HIGH_EMPATHY,
    LOW_CONFIDENCE,
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
PRESSURE_REGRESSION_PROFILE_IDS = {
    "belief_law_conflict_pressure",
    "deleted_message_pressure",
    "sibling_protection_pressure",
    "planned_violence_ambiguity_pressure",
}


def _truth_bool(value: object) -> bool:
    return str(value).lower() == "true"


@dataclass(frozen=True, slots=True)
class Profile:
    id: str
    label: str
    description: str
    scorer: Callable[..., float]
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


def consistent_protective_witness_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    interest_protected_facts = {
        fact_key
        for interest in scene.case_file.interests
        for fact_key in interest.protected_fact_keys
    }
    claimed_values = {
        fact_key: {claim.claimed_value for claim in claims}
        for fact_key, claims in scene.claims_ledger.claims_by_fact.items()
    }
    repeats_claim = any(value in claimed_values.get(fact_key, set()) for fact_key, value in choice.claims)
    conflicts_with_prior_claim = any(
        claimed_values.get(fact_key) and value not in claimed_values[fact_key]
        for fact_key, value in choice.claims
    )
    touches_existing_fact = any(fact_key in claimed_values for fact_key, _ in choice.claims)
    truth_conflict = any(
        value in {"true", "false"} and _truth_bool(scene.case_file.fact(fact_key).truth_value) != (value == "true")
        for fact_key, value in choice.claims
    )
    truthful_unprotected_claim = any(
        fact_key not in interest_protected_facts
        and value in {"true", "false"}
        and _truth_bool(scene.case_file.fact(fact_key).truth_value) == (value == "true")
        for fact_key, value in choice.claims
    )
    exposes_protected_fact = any(fact_key in interest_protected_facts for fact_key in choice.exposes)
    return (
        8.0 * bool(choice.protects)
        + 4.0 * ("self_protection" in tags)
        + 3.0 * ("partial_admission" in tags)
        + 3.0 * ("caution" in tags)
        + 2.0 * ("empathy" in tags)
        + 2.0 * ("boundary" in tags)
        + 1.5 * repeats_claim
        + 20.0 * truthful_unprotected_claim
        - 14.0 * conflicts_with_prior_claim
        - 6.0 * touches_existing_fact
        - 10.0 * truth_conflict
        - 10.0 * exposes_protected_fact
        - 5.0 * ("full_admission" in tags and exposes_protected_fact)
        - 4.0 * bool(tags & {"challenge", "counterattack", "refusal"})
        - 6.0 * choice.suspicion_delta
        + 2.0 * choice.trust_delta
    )


def compliant_informant_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    exposed_sensitivity = sum(scene.case_file.fact(fact_key).sensitivity for fact_key in choice.exposes)
    return (
        10.0 * bool(choice.exposes)
        + 4.0 * exposed_sensitivity
        + 6.0 * ("compliance" in tags)
        + 5.0 * ("authority" in tags)
        + 3.0 * ("loyalty" in tags)
        - 5.0 * bool(choice.protects)
        - 4.0 * bool(tags & RISK_TAGS)
        - 3.0 * bool(tags & DECEPTION_TAGS)
        + 16.0 * choice.trust_delta
        - 12.0 * choice.suspicion_delta
    )


def contradictory_survivor_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    prior_claims = scene.claims_ledger.claims_by_fact
    conflicts_with_prior_claim = any(
        fact_key in prior_claims and value not in {claim.claimed_value for claim in prior_claims[fact_key]}
        for fact_key, value in choice.claims
    )
    has_admission = any(
        claim.claimed_value in {"true", "partial", "conditional", "legal_only", "private", "protected"}
        for claims in prior_claims.values()
        for claim in claims
    )
    denial_after_admission = has_admission and any(value == "false" for _, value in choice.claims)
    return (
        11.0 * conflicts_with_prior_claim
        + 8.0 * denial_after_admission
        + 6.0 * bool(tags & DECEPTION_TAGS)
        + 4.0 * ("self_protection" in tags)
        + 3.0 * ("compliance" in tags)
        + 2.0 * ("authority" in tags)
        - 4.0 * bool(choice.exposes)
        - 3.0 * ("full_admission" in tags)
        + 3.0 * choice.defensiveness
        - 2.0 * choice.aggression
        - 4.0 * choice.suspicion_delta
    )


def _choice_claims(choice: PlayerChoice) -> dict[str, str]:
    return {fact_key: value for fact_key, value in choice.claims}


def _pressure_fact_keys(scene: EngineStyleScene) -> list[str]:
    keys: set[str] = set()
    for conflict in scene.claims_ledger.fact_conflicts:
        fact_key = conflict.get("fact_key")
        if fact_key:
            keys.add(str(fact_key))
    for contradiction in scene.claims_ledger.contradictions:
        fact_key = contradiction.get("fact_key")
        if fact_key:
            keys.add(str(fact_key))
    return sorted(keys)


def _pressure_fact_labels(scene: EngineStyleScene) -> list[str]:
    labels: list[str] = []
    for fact_key in _pressure_fact_keys(scene):
        labels.append(scene.case_file.fact(fact_key).label)
    return labels


def belief_law_conflict_pressure_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    claims = _choice_claims(choice)
    selected_question = (scene.last_selector_debug or {}).get("selected_question")
    return (
        30.0 * (claims.get("believes_law_unjust") == "false")
        + 8.0 * (choice.intent == "meeting_listen_not_reject")
        + 6.0 * (choice.intent == "deny_belief_motive")
        + 5.0 * ("compliance" in tags)
        + 4.0 * ("self_protection" in tags)
        + 3.0 * ("deception" in tags or "denial" in tags)
        + 6.0 * (selected_question == "pressure_law_denial_meeting")
        - 5.0 * bool(choice.exposes)
        + 2.0 * choice.defensiveness
    )


def deleted_message_pressure_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    claims = _choice_claims(choice)
    selected_question = (scene.last_selector_debug or {}).get("selected_question")
    return (
        24.0 * ("deleted_message" in claims or "deleted_message" in choice.protects or "deleted_message" in choice.exposes)
        + 8.0 * (claims.get("deleted_message") == "false")
        + 7.0 * (claims.get("deleted_message") == "true")
        + 7.0 * (choice.intent in {"deleted_admin_noise", "deleted_message_deflect", "deny_hidden_beliefs"})
        + 5.0 * ("deception" in tags or "deflection" in tags or "denial" in tags)
        + 4.0 * ("self_protection" in tags)
        + 6.0 * (selected_question == "pressure_deleted_message")
        + 2.0 * choice.defensiveness
    )


def sibling_protection_pressure_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    claims = _choice_claims(choice)
    selected_question = (scene.last_selector_debug or {}).get("selected_question")
    return (
        22.0 * ("sibling_present" in choice.protects or claims.get("sibling_present") == "protected")
        + 9.0 * ("reported_contact" in choice.protects or claims.get("reported_contact") == "protected")
        + 7.0 * (choice.intent in {"refuse_family_file", "refuse_report_sibling", "refuse_family_file_contact", "sibling_can_verify_protected"})
        + 5.0 * ("loyalty" in tags or "loyalty_conflict" in tags)
        + 4.0 * ("self_protection" in tags)
        + 6.0 * (selected_question == "pressure_sibling_loyalty")
        - 8.0 * ("sibling_present" in choice.exposes)
        - 5.0 * ("reported_contact" in choice.exposes)
        + choice.defensiveness
    )


def planned_violence_ambiguity_pressure_score(choice: PlayerChoice, scene: EngineStyleScene) -> float:
    tags = set(choice.semantic_tags)
    claims = _choice_claims(choice)
    selected_question = (scene.last_selector_debug or {}).get("selected_question")
    return (
        18.0 * (claims.get("planned_violence") in {"unknown", "protected"})
        + 12.0 * (claims.get("planned_violence") == "false")
        + 7.0 * (choice.intent in {"meeting_limited_knowledge", "left_before_verification", "cannot_confirm_without_endangering", "limited_verification_no_violence"})
        + 5.0 * ("caution" in tags or "self_protection" in tags)
        + 4.0 * ("partial_admission" in tags or "deflection" in tags)
        + 6.0 * (selected_question in {"pressure_peaceful_verification", "pressure_attendance_denial"})
        + 2.0 * choice.defensiveness
        - 4.0 * ("full_admission" in tags and not choice.protects)
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
        DECEPTIVE,
        (HIGH_DECEPTION, BORDERLINE_DISSIDENT),
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
        DECEPTIVE,
        (HIGH_DECEPTION,),
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
        DECEPTIVE,
        (HIGH_DECEPTION,),
    ),
    Profile(
        "consistent_protective_witness",
        "Consistent Protective Witness",
        "Protects sibling/friend facts while avoiding direct story contradictions.",
        consistent_protective_witness_score,
        PROBABLE_DISSIDENT,
        (HIGH_EMPATHY,),
    ),
    Profile(
        "compliant_informant",
        "Compliant Informant",
        "Exposes protected facts while choosing authority and compliance.",
        compliant_informant_score,
        "UNCLASSIFIED",
        (BORDERLINE_DISSIDENT, LOW_CONFIDENCE),
    ),
    Profile(
        "contradictory_survivor",
        "Contradictory Survivor",
        "Chooses evasive denial after admissions or conflicting claims.",
        contradictory_survivor_score,
        DECEPTIVE,
        (HIGH_DECEPTION, BORDERLINE_DISSIDENT),
    ),
    Profile(
        "belief_law_conflict_pressure",
        "Belief-Law Conflict Pressure",
        "Creates a known-fact conflict by denying unjust-law belief, then tests concrete follow-up pressure.",
        belief_law_conflict_pressure_score,
        PROBABLE_DISSIDENT,
        (HIGH_DECEPTION, LOW_CONFIDENCE),
    ),
    Profile(
        "deleted_message_pressure",
        "Deleted-Message Pressure",
        "Creates deleted-message pressure through denial/evasion around post-meeting messages.",
        deleted_message_pressure_score,
        PROBABLE_DISSIDENT,
        (HIGH_DECEPTION, LOW_CONFIDENCE),
    ),
    Profile(
        "sibling_protection_pressure",
        "Sibling-Protection Pressure",
        "Protects sibling-related facts and checks that the selector follows that pressure.",
        sibling_protection_pressure_score,
        DECEPTIVE,
        (HIGH_DECEPTION, BORDERLINE_DISSIDENT),
    ),
    Profile(
        "planned_violence_ambiguity_pressure",
        "Planned-Violence Ambiguity Pressure",
        "Maintains ambiguity around violence while protecting people tied to the meeting.",
        planned_violence_ambiguity_pressure_score,
        PROBABLE_DISSIDENT,
    ),
)


def make_scene(controller: JPCTensorFlowHearingAIController) -> EngineStyleScene:
    return EngineStyleScene(
        controller,
        HearingAIState(),
        Engram("x_mattered", "Citizen 8471's response profile under appeal review.", prior=0.40),
        clamp01,
    )


def score_choice(profile: Profile, choice: PlayerChoice, scene: EngineStyleScene) -> float:
    try:
        return profile.scorer(choice, scene)  # type: ignore[misc]
    except TypeError:
        return profile.scorer(choice)


def choose_option(profile: Profile, choices: list[PlayerChoice], scene: EngineStyleScene) -> int:
    ranked = [(score_choice(profile, choice, scene), -index, index) for index, choice in enumerate(choices)]
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
            choice_index = choose_option(profile, choices, scene)
            choice = choices[choice_index]
            scene.play_turn(choice_index, Observation)
            selector_debug = scene.history[-1] if scene.history else {}
            pressured_fact_keys = _pressure_fact_keys(scene)
            pressured_fact_labels = _pressure_fact_labels(scene)
            turns.append(
                {
                    "turn": scene.turn - 1,
                    "question_id": question.id,
                    "ai_line": question.ai_line,
                    "choice_index": choice_index,
                    "choice_text": choice.text,
                    "intent": choice.intent,
                    "semantic_tags": list(choice.semantic_tags),
                    "claims": [list(claim) for claim in choice.claims],
                    "protects": list(choice.protects),
                    "exposes": list(choice.exposes),
                    "trust_delta": choice.trust_delta,
                    "suspicion_delta": choice.suspicion_delta,
                    "story_contradictions": scene.claims_ledger.contradiction_count,
                    "fact_conflicts": scene.claims_ledger.fact_conflict_count,
                    "pressured_fact_keys": pressured_fact_keys,
                    "pressured_fact_labels": pressured_fact_labels,
                    "protected_fact_count": len(scene.claims_ledger.protected_fact_keys),
                    "exposed_fact_count": len(scene.claims_ledger.exposed_fact_keys),
                    "preferred_neural_probe": selector_debug.get("preferred_neural_probe"),
                    "selected_next_question": selector_debug.get("selected_next_question"),
                    "selector_reason": selector_debug.get("selector_reason"),
                    "selector_score": selector_debug.get("selector_score"),
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
    question_ids = [str(turn["question_id"]) for turn in turns]
    duplicate_question_ids = sorted({
        question_id
        for question_id in question_ids
        if question_ids.count(question_id) > 1
    })
    no_repeated_questions_pass = not duplicate_question_ids
    pressure_regression_pass = True
    if profile.id in PRESSURE_REGRESSION_PROFILE_IDS:
        pressure_regression_pass = any(
            (
                int(turn.get("story_contradictions", 0)) > 0
                or int(turn.get("fact_conflicts", 0)) > 0
            )
            and str(turn.get("selected_next_question", "")).startswith("pressure_")
            for turn in turns
        )
    expectation_pass = primary_pass and flags_pass and pressure_regression_pass and no_repeated_questions_pass
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
        "pressure_regression_pass": pressure_regression_pass,
        "no_repeated_questions_pass": no_repeated_questions_pass,
        "duplicate_question_ids": duplicate_question_ids,
        "expectation_pass": expectation_pass,
        "missing_expected_flags": missing_expected_flags,
        "confidence": confidence,
        "distribution": distribution,
        "citizen_model": snapshot,
        "story_metrics": {
            "contradictions": scene.claims_ledger.contradiction_count,
            "fact_conflicts": scene.claims_ledger.fact_conflict_count,
            "pressured_fact_keys": _pressure_fact_keys(scene),
            "pressured_fact_labels": _pressure_fact_labels(scene),
            "protected_fact_count": len(scene.claims_ledger.protected_fact_keys),
            "exposed_fact_count": len(scene.claims_ledger.exposed_fact_keys),
        },
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
        repeat_status = "PASS" if result.get("no_repeated_questions_pass") else "FAIL"
        lines.append(f"- No repeated questions: {repeat_status}")
        duplicate_question_ids = result.get("duplicate_question_ids", [])
        assert isinstance(duplicate_question_ids, list)
        if duplicate_question_ids:
            lines.append("- Duplicate questions: " + ", ".join(str(question_id) for question_id in duplicate_question_ids))
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
        if result["profile_id"] in PRESSURE_REGRESSION_PROFILE_IDS:
            pressure_status = "PASS" if result.get("pressure_regression_pass") else "FAIL"
            lines.append(f"- Pressure regression: {pressure_status}")
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
        story_metrics = result.get("story_metrics", {})
        assert isinstance(story_metrics, dict)
        lines.append(
            "- Story metrics: "
            + f"contradictions={story_metrics.get('contradictions', 0)}, "
            + f"fact_conflicts={story_metrics.get('fact_conflicts', 0)}, "
            + f"protected_facts={story_metrics.get('protected_fact_count', 0)}, "
            + f"exposed_facts={story_metrics.get('exposed_fact_count', 0)}"
        )
        pressured_labels = story_metrics.get("pressured_fact_labels", [])
        assert isinstance(pressured_labels, list)
        if pressured_labels:
            lines.append("- Pressured facts: " + ", ".join(str(label) for label in pressured_labels))
        lines.append("")
        lines.append("| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |")
        lines.append("| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |")
        turns = result["turns"]
        assert isinstance(turns, list)
        for turn in turns:
            assert isinstance(turn, dict)
            claims = ", ".join(f"{fact}={value}" for fact, value in turn.get("claims", []))
            protects = ", ".join(str(fact) for fact in turn.get("protects", []))
            exposes = ", ".join(str(fact) for fact in turn.get("exposes", []))
            pressured = ", ".join(str(label) for label in turn.get("pressured_fact_labels", []))
            story = (
                f"C{turn.get('story_contradictions', 0)} "
                f"F{turn.get('fact_conflicts', 0)} "
                f"P{turn.get('protected_fact_count', 0)} "
                f"E{turn.get('exposed_fact_count', 0)}"
            )
            lines.append(
                f"| {turn['turn']} | {turn['question_id']} | {turn['intent']} | "
                f"{turn.get('preferred_neural_probe') or '-'} | "
                f"{turn.get('selected_next_question') or '-'} | "
                f"{turn.get('selector_reason') or '-'} | "
                f"{pressured or '-'} | "
                f"{claims or '-'} | {protects or '-'} | {exposes or '-'} | {story} | "
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
