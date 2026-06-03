from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Any

# python generate_human_training_examples.py --episodes 10 --max-turns 30 --train-steps 100 --append --output data/human_train_reauthoring.jsonl

from engine_style_scene import EngineStyleScene
from pc_jpc_tensorflow_npc_demo import (
    Engram,
    JPCTensorFlowHearingAIController,
    HearingAIState,
    Observation,
    clamp01,
    train_demo_model,
)

# python generate_human_training_examples.py \ --episodes 10 \ --max-turns 30 \ --train-steps 100 \ --append \ --output data/human_train.jsonl

def make_scene(seed: int, train_steps: int) -> EngineStyleScene:
    controller = JPCTensorFlowHearingAIController(seed=seed)
    if train_steps > 0:
        train_demo_model(controller, steps=train_steps, seed=seed + 100)
    return EngineStyleScene(
        controller,
        HearingAIState(),
        Engram("x_mattered", "Citizen 8471's response profile under appeal review.", prior=0.40),
        clamp01,
    )


def scene_snapshot(scene: EngineStyleScene) -> dict[str, Any]:
    question = scene.current_question() if not scene.is_complete() else None
    return {
        "turn": scene.turn,
        "question_id": question.id if question else None,
        "ai_line": question.ai_line if question else None,
        "lsd_taken": scene.lsd_taken,
        "pill_state": scene.pill_state,
        "trust": round(float(scene.hearing_ai.trust), 4),
        "suspicion": round(float(scene.hearing_ai.suspicion), 4),
        "instability": round(float(scene.hearing_ai.instability), 4),
        "belief": round(float(scene.hearing_ai.belief(scene.engram.id)), 4),
        "uncertainty": round(float(scene.hearing_ai.uncertainty(scene.engram.id)), 4),
        "confidence": round(float(scene.hearing_ai.confidence(scene.engram.id)), 4),
        "contradictions": scene.contradictions,
        "story_contradictions": scene.claims_ledger.contradiction_count,
        "fact_conflicts": scene.claims_ledger.fact_conflict_count,
        "protected_fact_count": len(scene.claims_ledger.protected_fact_keys),
        "exposed_fact_count": len(scene.claims_ledger.exposed_fact_keys),
        "case_file": scene.case_file.public_summary(),
        "claims_ledger": scene.claims_ledger.summary(),
        "preferred_neural_probe": scene.last_neural_probe_intent,
        "selector_debug": scene.last_selector_debug,
        "theory_model": scene.theory_snapshot() if hasattr(scene, "theory_snapshot") else None,
    }


def choose_human_option(options: list[object]) -> int:
    while True:
        raw = input("Select option number, or q to quit episode: ").strip().lower()
        if raw == "q":
            return -1
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return idx
        print("Invalid selection. Please enter one of the visible option numbers.")


def choose_profile_option(
    profile_id: str,
    options: list[object],
    scene: EngineStyleScene,
    rng: random.Random | None = None,
    *,
    stochastic: bool = True,
    temperature: float = 1.5,
    top_margin: float = 5.0,
) -> tuple[int, dict[str, Any]]:
    from test_playthrough_profiles import PROFILES, score_choice

    profile = next((candidate for candidate in PROFILES if candidate.id == profile_id), None)
    if profile is None:
        valid = ", ".join(profile.id for profile in PROFILES)
        raise ValueError(f"Unknown profile {profile_id!r}. Valid profiles: {valid}")

    ranked = [
        (float(score_choice(profile, option, scene)), index)
        for index, option in enumerate(options)
    ]
    ranked.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    best_score = ranked[0][0]
    candidates = [
        (score, index)
        for score, index in ranked
        if best_score - score <= top_margin
    ]

    metadata: dict[str, Any] = {
        "mode": "stochastic" if stochastic else "deterministic",
        "temperature": temperature,
        "top_margin": top_margin,
        "best_score": round(best_score, 4),
        "candidate_count": len(candidates),
        "ranked_options": [
            {"option_index": index, "score": round(score, 4)}
            for score, index in ranked
        ],
    }

    if not stochastic or len(candidates) == 1:
        selected_index = ranked[0][1]
        metadata["selected_score"] = round(ranked[0][0], 4)
        return selected_index, metadata

    if temperature <= 0:
        raise ValueError("--profile-temperature must be greater than 0 when stochastic profile choice is enabled.")

    local_rng = rng if rng is not None else random.Random()
    weights = [math.exp((score - best_score) / temperature) for score, _index in candidates]
    selected_score, selected_index = local_rng.choices(candidates, weights=weights, k=1)[0]
    metadata["selected_score"] = round(selected_score, 4)
    metadata["candidate_options"] = [
        {
            "option_index": index,
            "score": round(score, 4),
            "weight": round(weight, 6),
        }
        for (score, index), weight in zip(candidates, weights)
    ]
    return selected_index, metadata


def collect_episode(
    scene: EngineStyleScene,
    episode_id: str,
    max_turns: int,
    profile_id: str | None = None,
    rng: random.Random | None = None,
    *,
    stochastic_profile: bool = True,
    profile_temperature: float = 1.5,
    profile_top_margin: float = 5.0,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if profile_id is None:
        print("\n--- Scene setting ---")
        print(scene.opening_text())
        if hasattr(scene, "opening_model_report"):
            print()
            print(scene.opening_model_report())

    for turn_index in range(max_turns):
        if scene.is_complete():
            break

        question = scene.current_question()
        options = scene.choices(Observation)
        if not options:
            break

        before = scene_snapshot(scene)
        if profile_id is None:
            print("\n" + "=" * 80)
            print(f"Episode {episode_id} | Turn {turn_index}")
            print("\nHearing AI asks:")
            print(question.ai_line)
            print("\nPlayer options:")
            for idx, opt in enumerate(options, start=1):
                meta = opt.metadata()
                tags = ", ".join(meta.get("semantic_tags") or [])
                print(f"  {idx}. {opt.text} [{meta.get('intent')}: {tags}]")
            selected_index = choose_human_option(options)
            selection_metadata = None
        else:
            selected_index, selection_metadata = choose_profile_option(
                profile_id,
                options,
                scene,
                rng,
                stochastic=stochastic_profile,
                temperature=profile_temperature,
                top_margin=profile_top_margin,
            )
        if selected_index == -1:
            print("Ending episode early at user request.")
            break

        selected_option = options[selected_index]
        scene.play_turn(selected_index, Observation)
        after = scene_snapshot(scene)

        rows.append({
            "example_source": "human_engine_style_playthrough",
            "profile_label": profile_id,
            "is_auto_generated": False,
            "episode_id": episode_id,
            "turn_index": turn_index,
            "scene_id": "citizen_appeal_hearing",
            "hearing_ai_id": "hearing_ai",
            "question": question.metadata(),
            "state_before": before,
            "player_options": [{"text": opt.text, "metadata": opt.metadata()} for opt in options],
            "player_choice": selected_option.text,
            "player_choice_metadata": selected_option.metadata(),
            "profile_selection": selection_metadata,
            "hearing_ai_action": scene.last_action.value if scene.last_action is not None else None,
            "model_trace": scene.controller.last_trace,
            "theory_revision": scene.last_theory_revision if hasattr(scene, "last_theory_revision") else None,
            "theory_before": scene.last_theory_before if hasattr(scene, "last_theory_before") else None,
            "theory_after": scene.last_theory_after if hasattr(scene, "last_theory_after") else None,
            "state_after": after,
            "ending_reason": scene.ending_reason,
        })

    if scene.is_complete() and hasattr(scene, "_print_final_model_once"):
        scene._print_final_model_once()
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect human JSONL from the engine-style authored scene.")
    parser.add_argument("--episodes", type=int, default=1, help="Number of episodes to collect.")
    parser.add_argument("--max-turns", type=int, default=14, help="Maximum turns per episode.")
    parser.add_argument("--train-steps", type=int, default=700, help="Synthetic model training steps per episode controller. Use 0 to skip.")
    parser.add_argument("--output", type=Path, default=Path("data/human_train.jsonl"), help="Output JSONL file.")
    parser.add_argument("--append", action="store_true", help="Append to existing output instead of overwriting.")
    parser.add_argument("--seed", type=int, default=7, help="Base random seed.")
    parser.add_argument("--profile", default=None, help="Optional human-style profile id for noninteractive generation.")
    parser.add_argument(
        "--deterministic-profile",
        action="store_true",
        help="Always choose the highest-scoring profile option. Useful for regression baselines.",
    )
    parser.add_argument(
        "--profile-temperature",
        type=float,
        default=1.5,
        help="Softmax temperature for stochastic profile option selection. Lower values stay closer to the best option.",
    )
    parser.add_argument(
        "--profile-top-margin",
        type=float,
        default=5.0,
        help="Only sample options whose profile score is within this margin of the best option.",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if args.append else "w"
    total_rows = 0

    with args.output.open(mode, encoding="utf-8") as handle:
        for episode_index in range(args.episodes):
            episode_id = f"human_engine_ep_{episode_index:04d}"
            scene = make_scene(args.seed + episode_index, args.train_steps)
            episode_rng = random.Random(args.seed * 100_000 + episode_index)
            rows = collect_episode(
                scene,
                episode_id,
                args.max_turns,
                args.profile,
                episode_rng,
                stochastic_profile=not args.deterministic_profile,
                profile_temperature=args.profile_temperature,
                profile_top_margin=args.profile_top_margin,
            )
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                total_rows += 1

    print(f"Wrote {total_rows} human engine-style examples to {args.output}.")


if __name__ == "__main__":
    main()
