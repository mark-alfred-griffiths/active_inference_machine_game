from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from engine_style_scene import EngineStyleScene, INTRO_TEXT  # noqa: E402


SCENE_ID = "citizen_appeal_hearing"
OUTPUT_PATH = PROJECT_ROOT / "data" / "scenes" / f"{SCENE_ID}.yaml"


class _DummyController:
    action_labels = ("press", "comfort", "escalate")


class _DummyHearingAI:
    pass


class _DummyEngram:
    pass


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _yaml_scalar(value: Any) -> str:
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def _yaml_list(items: Iterable[Any]) -> str:
    values = tuple(items)
    if not values:
        return "[]"
    return "[" + ", ".join(_yaml_scalar(item) for item in values) + "]"


def _append_pair_list(lines: list[str], indent: str, key: str, pairs: Iterable[tuple[str, str]]) -> None:
    values = tuple(pairs)
    if not values:
        lines.append(f"{indent}{key}: []")
        return
    lines.append(f"{indent}{key}:")
    for fact_key, claimed_value in values:
        lines.append(f"{indent}  - fact_key: {_yaml_scalar(fact_key)}")
        lines.append(f"{indent}    claimed_value: {_yaml_scalar(claimed_value)}")


def export_scene_yaml() -> str:
    scene = EngineStyleScene(_DummyController(), _DummyHearingAI(), _DummyEngram(), _clamp01)
    nodes = scene.question_nodes()

    lines: list[str] = [
        "schema_version: 1",
        f"scene_id: {SCENE_ID}",
        "title: \"Citizen 8471 Appeal Hearing\"",
        "source: \"engine_style_scene.py + dialogue_questions.py\"",
        f"initial_question_id: {_yaml_scalar(scene.current_question_id)}",
        f"max_turns: {scene.max_turns}",
        f"node_count: {len(nodes)}",
        "intro_text: |",
    ]

    for intro_line in INTRO_TEXT.rstrip().splitlines():
        lines.append(f"  {intro_line}" if intro_line else "")

    lines.append("nodes:")

    for node in nodes.values():
        lines.extend(
            [
                f"  - id: {_yaml_scalar(node.id)}",
                f"    ai_line: {_yaml_scalar(node.ai_line)}",
                f"    pressure: {node.pressure:.2f}",
                f"    is_interstitial: {_yaml_scalar(node.is_interstitial)}",
                f"    reaction_context: {_yaml_scalar(node.reaction_context)}",
                f"    target_context: {_yaml_scalar(node.target_context)}",
                f"    discriminates: {_yaml_list(node.discriminates)}",
                f"    information_gain_hint: {_yaml_scalar(node.information_gain_hint)}",
                f"    probes_facts: {_yaml_list(node.probes_facts)}",
                f"    probes_claims: {_yaml_list(node.probes_claims)}",
                f"    pressure_on_interests: {_yaml_list(node.pressure_on_interests)}",
                "    choices:" if node.choices else "    choices: []",
            ]
        )

        for choice in node.choices:
            lines.extend(
                [
                    f"      - text: {_yaml_scalar(choice.text)}",
                    f"        intent: {_yaml_scalar(choice.intent)}",
                    f"        semantic_tags: {_yaml_list(choice.semantic_tags)}",
                    f"        honesty: {choice.honesty:.2f}",
                    f"        vulnerability: {choice.vulnerability:.2f}",
                    f"        defensiveness: {choice.defensiveness:.2f}",
                    f"        aggression: {choice.aggression:.2f}",
                    f"        intimacy: {choice.intimacy:.2f}",
                    f"        destabilisation: {choice.destabilisation:.2f}",
                    f"        trust_delta: {choice.trust_delta:.2f}",
                    f"        suspicion_delta: {choice.suspicion_delta:.2f}",
                    f"        instability_delta: {choice.instability_delta:.2f}",
                    f"        protects: {_yaml_list(choice.protects)}",
                    f"        exposes: {_yaml_list(choice.exposes)}",
                    f"        next_question_id: {_yaml_scalar(choice.next_question_id)}",
                ]
            )
            _append_pair_list(lines, "        ", "claims", choice.claims)

    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(export_scene_yaml(), encoding="utf-8")
    print(f"Wrote scene YAML to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
