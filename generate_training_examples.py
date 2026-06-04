from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

from engine_style_scene import EngineStyleScene
from pc_jpc_tensorflow_npc_demo import (
    Engram,
    JPCTensorFlowHearingAIController,
    HearingAIState,
    Observation,
    clamp01,
    train_demo_model,
)
#python generate_human_training_examples.py \
#  --episodes 10 \
#  --max-turns 30 \
#  --train-steps 100 \
#  --append \
#  --output data/human_train.jsonl

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
        "second_tab_taken": scene.second_tab_taken,
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
        "history_length": len(scene.history),
        "theory_model": scene.theory_snapshot() if hasattr(scene, "theory_snapshot") else None,
    }


def option_metadata(option: object) -> dict[str, Any]:
    return option.metadata() if hasattr(option, "metadata") and callable(option.metadata) else {}


def human_like_option_score(option: object, rng: random.Random) -> float:
    meta = option_metadata(option)
    tags = set(meta.get("semantic_tags") or ())
    claims = meta.get("claims") or ()
    protects = meta.get("protects") or ()
    exposes = meta.get("exposes") or ()
    return (
        2.5 * ("partial_admission" in tags)
        + 2.0 * ("boundary" in tags)
        + 1.8 * ("caution" in tags)
        + 1.6 * ("empathy" in tags)
        + 1.0 * ("compliance" in tags)
        + 0.8 * bool(protects)
        + 0.5 * bool(claims)
        - 1.6 * ("counterattack" in tags)
        - 1.2 * ("refusal" in tags)
        - 0.8 * ("full_admission" in tags and bool(exposes))
        - 0.6 * ("denial" in tags)
        + rng.uniform(-0.35, 0.35)
    )


def choose_human_like_option(options: list[object], rng: random.Random) -> int:
    ranked = sorted(
        ((human_like_option_score(option, rng), -index, index) for index, option in enumerate(options)),
        reverse=True,
    )
    return ranked[0][2]


def generate_episode(episode_id: str, seed: int, max_turns: int, train_steps: int) -> list[dict[str, Any]]:
    scene = make_scene(seed, train_steps)
    rng = random.Random(seed)
    rows: list[dict[str, Any]] = []

    for turn_index in range(max_turns):
        if scene.is_complete():
            break

        question = scene.current_question()
        options = scene.choices(Observation)
        if not options:
            break

        before = scene_snapshot(scene)
        choice_index = choose_human_like_option(options, rng)
        selected_option = options[choice_index]
        scene.play_turn(choice_index, Observation)
        after = scene_snapshot(scene)

        rows.append({
            "example_source": "auto_generated_engine_style_sweep",
            "is_auto_generated": True,
            "episode_id": episode_id,
            "turn_index": turn_index,
            "scene_id": "citizen_appeal_hearing",
            "hearing_ai_id": "hearing_ai",
            "question": question.metadata(),
            "state_before": before,
            "player_options": [
                {"text": opt.text, "metadata": option_metadata(opt)}
                for opt in options
            ],
            "player_choice": selected_option.text,
            "player_choice_metadata": option_metadata(selected_option),
            "model_trace": scene.controller.last_trace,
            "theory_revision": scene.last_theory_revision if hasattr(scene, "last_theory_revision") else None,
            "theory_before": scene.last_theory_before if hasattr(scene, "last_theory_before") else None,
            "theory_after": scene.last_theory_after if hasattr(scene, "last_theory_after") else None,
            "state_after": after,
            "ending_reason": scene.ending_reason,
        })

    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate semantic JSONL from the engine-style authored scene.")
    parser.add_argument("--episodes", type=int, default=10, help="Number of random episodes to generate.")
    parser.add_argument("--max-turns", type=int, default=14, help="Max turns per episode.")
    parser.add_argument("--train-steps", type=int, default=700, help="Synthetic model training steps per episode controller. Use 0 to skip.")
    parser.add_argument("--output", type=Path, default=Path("data/auto_train.jsonl"), help="Output JSONL file.")
    parser.add_argument("--seed", type=int, default=7, help="Base random seed.")
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with args.output.open("w", encoding="utf-8") as handle:
        for episode_index in range(args.episodes):
            episode_id = f"auto_engine_ep_{episode_index:04d}"
            rows = generate_episode(episode_id, args.seed + episode_index, args.max_turns, args.train_steps)
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                written += 1

    print(f"Wrote {written} engine-style semantic training examples to {args.output}.")


if __name__ == "__main__":
    main()
