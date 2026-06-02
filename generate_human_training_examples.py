from __future__ import annotations

import argparse
import json
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


def collect_episode(scene: EngineStyleScene, episode_id: str, max_turns: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
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
        if selected_index == -1:
            print("Ending episode early at user request.")
            break

        selected_option = options[selected_index]
        scene.play_turn(selected_index, Observation)
        after = scene_snapshot(scene)

        rows.append({
            "example_source": "human_engine_style_playthrough",
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
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if args.append else "w"
    total_rows = 0

    with args.output.open(mode, encoding="utf-8") as handle:
        for episode_index in range(args.episodes):
            episode_id = f"human_engine_ep_{episode_index:04d}"
            scene = make_scene(args.seed + episode_index, args.train_steps)
            rows = collect_episode(scene, episode_id, args.max_turns)
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                total_rows += 1

    print(f"Wrote {total_rows} human engine-style examples to {args.output}.")


if __name__ == "__main__":
    main()
