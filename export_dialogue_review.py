from pathlib import Path

from engine_style_scene import EngineStyleScene


class _DummyController:
    action_labels = ("press", "comfort", "escalate")


class _DummyHearingAI:
    pass


class _DummyEngram:
    id = "x_mattered"


def main() -> None:
    scene = EngineStyleScene(
        _DummyController(),
        _DummyHearingAI(),
        _DummyEngram(),
        lambda x: x,
    )

    nodes = scene.question_nodes()

    output_lines: list[str] = []

    output_lines.append("# Hearing AI Dialogue Review Document")
    output_lines.append("")
    output_lines.append(
        "Generated from engine_style_scene.py for narrative re-authoring."
    )
    output_lines.append("")

    for node in nodes.values():

        output_lines.append("=" * 80)
        output_lines.append(f"NODE: {node.id}")
        output_lines.append("=" * 80)
        output_lines.append("")

        output_lines.append("ALICE QUESTION")
        output_lines.append("--------------")
        output_lines.append(node.ai_line)
        output_lines.append("")

        output_lines.append("PLAYER CHOICES")
        output_lines.append("--------------")

        for idx, choice in enumerate(node.choices, start=1):
            output_lines.append(f"{idx}. {choice.text}")

        output_lines.append("")
        output_lines.append("")

    out_path = Path("dialogue_revision_document.txt")
    out_path.write_text("\n".join(output_lines), encoding="utf-8")

    print(f"Wrote review document to: {out_path}")


if __name__ == "__main__":
    main()