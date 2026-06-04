from __future__ import annotations

import argparse
import json
from pathlib import Path

DEFAULT_PROFILES = (
    "compliant_loyalist",
    "cautious_survivor",
    "honest_dissident",
    "deceptive_appeaser",
    "empathetic_reformer",
)


def strip_deprecated_policy_fields(row: dict[str, object]) -> None:
    """Remove fields left by the removed hearing-action policy head."""
    row.pop("hearing_ai_action", None)
    model_trace = row.get("model_trace")
    if isinstance(model_trace, dict):
        model_trace.pop("policy_logits", None)
        model_trace.pop("chosen_action", None)


def collate(input_root: Path, output: Path, profiles: tuple[str, ...]) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    rows_written = 0
    with output.open("w", encoding="utf-8") as out:
        for profile_label in profiles:
            path = input_root / profile_label / "human_train.jsonl"
            if not path.exists():
                raise FileNotFoundError(f"Missing archetype file: {path}")
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                strip_deprecated_policy_fields(row)
                original_episode_id = row.get("episode_id", "episode")
                row["profile_label"] = profile_label
                row["source_episode_id"] = original_episode_id
                row["episode_id"] = f"{profile_label}_{original_episode_id}"
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
                rows_written += 1
    return rows_written


def main() -> None:
    parser = argparse.ArgumentParser(description="Collate human archetype JSONL files with profile labels and unique episode IDs.")
    parser.add_argument("--input-root", type=Path, default=Path("data/human_playthroughs"))
    parser.add_argument("--output", type=Path, default=Path("data/training/human_train_all_archetypes.jsonl"))
    parser.add_argument(
        "--profiles",
        nargs="+",
        default=DEFAULT_PROFILES,
        help="Profile subfolders to collate, in output order.",
    )
    args = parser.parse_args()

    rows_written = collate(args.input_root, args.output, tuple(args.profiles))
    print(f"Wrote {rows_written} rows to {args.output}")


if __name__ == "__main__":
    main()
