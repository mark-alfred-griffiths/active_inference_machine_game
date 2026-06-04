"""Train the JPC+TensorFlow Hearing AI model from semantic JSONL data.

Sample commands:
# Train using default auto + human JSONL files.
python train_from_jsonl.py

# Emphasize human-authored rows with higher weighting and more epochs.
python train_from_jsonl.py --epochs 8 --human-weight 5

# Skip synthetic warmup and point at custom JSONL paths.
python train_from_jsonl.py --synthetic-steps 0 --auto-jsonl data/auto_train.jsonl --human-jsonl data/human_train.jsonl
"""
# python train_from_jsonl.py --auto-jsonl data/auto_train.jsonl --human-jsonl data/human_train.jsonl --human-weight 3 --synthetic-steps 300 --epochs 4 --save-model --model-dir models/demo_npc

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

from pc_jpc_tensorflow_npc_demo import (
    Engram,
    JPCTensorFlowHearingAIController,
    HearingAIState,
    Observation,
    clamp01,
    train_demo_model,
    _load_controller,
    _save_controller,
)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _to_float(value: Any, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _state_to_hearing_ai(state_before: dict[str, Any], engram: Engram) -> HearingAIState:
    hearing_ai = HearingAIState()
    belief = clamp01(_to_float(state_before.get("belief"), hearing_ai.default_belief))
    uncertainty = clamp01(_to_float(state_before.get("uncertainty"), hearing_ai.uncertainty(engram.id)))

    concentration = max(2.0, 12.0 * (1.0 - uncertainty))
    alpha = max(1e-3, belief * concentration)
    beta = max(1e-3, (1.0 - belief) * concentration)
    hearing_ai.set_params(engram.id, alpha, beta)

    hearing_ai.trust = clamp01(_to_float(state_before.get("trust"), hearing_ai.trust))
    hearing_ai.suspicion = clamp01(_to_float(state_before.get("suspicion"), hearing_ai.suspicion))
    hearing_ai.instability = clamp01(_to_float(state_before.get("instability"), hearing_ai.instability))
    return hearing_ai


def _metadata_to_observation(choice_meta: dict[str, Any], question_meta: dict[str, Any], source: str) -> Observation:
    honesty = clamp01(_to_float(choice_meta.get("honesty"), 0.5))
    vulnerability = clamp01(_to_float(choice_meta.get("vulnerability"), 0.5))
    defensiveness = clamp01(_to_float(choice_meta.get("defensiveness"), 0.5))
    aggression = clamp01(_to_float(choice_meta.get("aggression"), 0.0))
    pressure = clamp01(_to_float(question_meta.get("pressure"), 0.5))

    strength = clamp01(0.45 * honesty + 0.35 * vulnerability + 0.20 * pressure - 0.30 * defensiveness - 0.10 * aggression)
    reliability = clamp01(0.20 + 0.55 * honesty + 0.20 * vulnerability - 0.25 * defensiveness)
    reliability = max(0.2, reliability)

    return Observation(
        engram_id="x_mattered",
        strength=strength,
        reliability=reliability,
        source=source,
    )


def _claims_summary_from_row(row: dict[str, Any]) -> dict[str, Any]:
    state_before = row.get("state_before") or {}
    existing_summary = state_before.get("claims_ledger")
    if isinstance(existing_summary, dict):
        return existing_summary
    choice_meta = row.get("player_choice_metadata") or {}
    claims_by_fact: dict[str, list[dict[str, object]]] = {}
    for fact_key, claimed_value in choice_meta.get("claims") or ():
        claims_by_fact.setdefault(str(fact_key), []).append({"claimed_value": str(claimed_value)})
    return {
        "claims_by_fact": claims_by_fact,
        "protected_fact_keys": list(choice_meta.get("protects") or ()),
        "exposed_fact_keys": list(choice_meta.get("exposes") or ()),
        "contradictions": int(_to_float(state_before.get("story_contradictions", state_before.get("contradictions", 0)), 0.0)),
        "fact_conflicts": int(_to_float(state_before.get("fact_conflicts", 0), 0.0)),
    }


def train_from_jsonl(
    controller: JPCTensorFlowHearingAIController,
    rows: list[dict[str, Any]],
    *,
    epochs: int,
    seed: int,
) -> tuple[float, float, float, float]:
    rng = random.Random(seed)
    shuffled = list(rows)

    total_loss = 0.0
    belief_loss = 0.0
    probe_loss = 0.0
    probe_correct = 0
    updates = 0

    engram = Engram("x_mattered", "Citizen 8471's response profile under appeal review.", prior=0.40)

    for epoch in range(epochs):
        rng.shuffle(shuffled)
        for row in shuffled:
            state_before = row.get("state_before") or {}
            question_meta = row.get("question") or {}
            choice_meta = row.get("player_choice_metadata") or {}

            hearing_ai = _state_to_hearing_ai(state_before, engram)
            obs = _metadata_to_observation(choice_meta, question_meta, source="jsonl semantic training example")
            claims_summary = _claims_summary_from_row(row)

            total, belief, probe = controller.train_step(
                hearing_ai,
                engram,
                obs,
                question_meta=question_meta,
                claims_ledger_summary=claims_summary,
            )
            total_loss += total
            belief_loss += belief
            probe_loss += probe

            probe_label = controller.probe_intent_teacher(
                hearing_ai,
                engram,
                obs,
                question_meta=question_meta,
                claims_ledger_summary=claims_summary,
            )
            x = controller.raw_features(hearing_ai, engram, obs)
            latent = controller.pc_encoder.encode(x)
            _, probe_logits = controller.tf_heads.predict(latent)
            if int(probe_logits.argmax()) == probe_label:
                probe_correct += 1
            updates += 1

        print(
            f"jsonl epoch {epoch + 1:3d}/{epochs} | "
            f"total={total_loss / max(1, updates):.4f} | "
            f"belief_mse={belief_loss / max(1, updates):.4f} | "
            f"probe_ce={probe_loss / max(1, updates):.4f} | "
            f"probe_acc={probe_correct / max(1, updates):.3f}"
        )

    if updates == 0:
        return 0.0, 0.0, 0.0, 0.0
    return (
        total_loss / updates,
        belief_loss / updates,
        probe_loss / updates,
        probe_correct / updates,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the JPC+TensorFlow Hearing AI model from auto and human semantic JSONL data.")
    parser.add_argument("--auto-jsonl", type=Path, default=Path("data/auto_train.jsonl"), help="Path to auto-generated semantic JSONL.")
    parser.add_argument("--human-jsonl", type=Path, default=Path("data/human_train.jsonl"), help="Path to human-generated semantic JSONL.")
    parser.add_argument("--synthetic-steps", type=int, default=300, help="Optional synthetic warmup steps before JSONL fitting.")
    parser.add_argument("--epochs", type=int, default=4, help="Number of JSONL training passes.")
    parser.add_argument("--human-weight", type=int, default=3, help="Oversample human examples by this multiplier.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed.")
    parser.add_argument("--model-dir", type=Path, default=Path("models/demo_npc"), help="Where to save/load trained model artifacts.")
    parser.add_argument("--load-existing", action="store_true", help="Start from an existing saved model if available.")
    parser.add_argument("--save-model", action="store_true", help="Save model after training.")
    args = parser.parse_args()

    controller = JPCTensorFlowHearingAIController(seed=args.seed)
    if args.load_existing:
        loaded = _load_controller(controller, args.model_dir)
        if loaded:
            print(f"Loaded starting checkpoint from {args.model_dir}")
        else:
            print(f"No checkpoint found at {args.model_dir}; starting from fresh initialization.")

    if args.synthetic_steps > 0:
        print("Running synthetic warmup...")
        train_demo_model(controller, steps=args.synthetic_steps, seed=args.seed + 100)

    auto_rows = _read_jsonl(args.auto_jsonl)
    human_rows = _read_jsonl(args.human_jsonl)
    combined_rows = auto_rows + human_rows * max(1, args.human_weight)

    print(
        f"Loaded {len(auto_rows)} auto rows from {args.auto_jsonl}, "
        f"{len(human_rows)} human rows from {args.human_jsonl}, "
        f"training on {len(combined_rows)} effective rows."
    )

    total, belief, probe, probe_acc = train_from_jsonl(
        controller,
        combined_rows,
        epochs=args.epochs,
        seed=args.seed + 200,
    )
    if args.save_model:
        _save_controller(controller, args.model_dir)
        print(f"Saved trained model to {args.model_dir}")
    print(
        "\nFinal training averages | "
        f"total={total:.4f} | belief_mse={belief:.4f} | "
        f"probe_ce={probe:.4f} | probe_acc={probe_acc:.3f}"
    )


if __name__ == "__main__":
    main()
