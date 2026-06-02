from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from engine_style_scene import EngineStyleScene
from dialogue_questions import question_pool_by_context


class DummyController:
    action_labels = ["dismiss", "probe", "reveal", "confront"]
    last_trace = {}


class DummyHearingAI:
    trust = 0.5
    suspicion = 0.5
    instability = 0.3

    def belief(self, _): return 0.5
    def uncertainty(self, _): return 0.5
    def confidence(self, _): return 0.5


class DummyEngram:
    id = "x_mattered"


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def clean(text: str, limit: int | None = None) -> str:
    text = " ".join(text.replace("\n", " ").split()).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def flags(node) -> str:
    bits = []
    if node.is_interstitial: bits.append("pause")
    if node.lsd_only: bits.append("LSD")
    if node.sober_only: bits.append("sober")
    if not node.choices: bits.append("terminal")
    return f" [{' / '.join(bits)}]" if bits else ""


def delta(choice) -> str:
    parts = []
    if choice.trust_delta: parts.append(f"trust {choice.trust_delta:+.2f}")
    if choice.suspicion_delta: parts.append(f"susp {choice.suspicion_delta:+.2f}")
    if choice.instability_delta: parts.append(f"inst {choice.instability_delta:+.2f}")
    if choice.set_lsd_taken: parts.append("TAKE_LSD")
    if choice.set_pill_state: parts.append(f"pill={choice.set_pill_state}")
    return "; ".join(parts) if parts else "state: —"


def route_overview(nodes) -> list[str]:
    lines = []
    lines.append("TEXT DIALOGUE GRAPH / ROUTE OVERVIEW")
    lines.append("=" * 80)
    lines.append("Plain text only. No Mermaid. No Graphviz.")
    lines.append("")
    lines.append("ROUTING MODEL")
    lines.append("- Start node: authority_unfair_law")
    lines.append("- Choices do not carry fixed next_question_id links.")
    lines.append("- After each answer, EngineStyleScene.select_next_question_id() selects")
    lines.append("  the highest-scoring unasked question from the remaining pool.")
    lines.append("- When no unasked questions remain, the scene moves to final.")
    lines.append("")
    grouped = question_pool_by_context()
    for context, node_ids in sorted(grouped.items()):
        lines.append("=" * 80)
        lines.append(f"CONTEXT: {context.upper()} ({len(node_ids)} questions)")
        lines.append("=" * 80)
        lines.append("")
        for node_id in node_ids:
            node = nodes[node_id]
            lines.append(f"[{node_id}]{flags(node)}")
            lines.append(f"  AI: {clean(node.ai_line, 120)}")
            if not node.choices:
                lines.append("  └─ TERMINAL")
            for i, choice in enumerate(node.choices, 1):
                branch = "└─" if i == len(node.choices) else "├─"
                target = choice.next_question_id or "SELECTOR -> next unasked question"
                lines.append(f"  {branch} {clean(choice.text, 70)}")
                lines.append(f"     -> {target}  ({choice.intent}; {delta(choice)})")
            lines.append("")
    lines.append("=" * 80)
    lines.append("SELECTOR SUMMARY")
    lines.append("=" * 80)
    lines.append("")
    lines.append("[ANY ANSWERED QUESTION]")
    lines.append("  └─ answer chosen")
    lines.append("     -> SELECTOR")
    lines.append("")
    lines.append("[SELECTOR]")
    lines.append("  ├─ if unasked questions remain: choose highest scoring unasked node")
    lines.append("  └─ if pool exhausted: final")
    return lines


def authoring_cards(nodes) -> list[str]:
    inbound = Counter()
    for node in nodes.values():
        for choice in node.choices:
            if choice.next_question_id:
                inbound[choice.next_question_id] += 1

    lines = []
    lines.append("\n" + "=" * 80)
    lines.append("AUTHORING CARDS")
    lines.append("=" * 80)
    lines.append("Use these to mark specific broken transitions.")
    lines.append("")

    for node_id, node in nodes.items():
        lines.append("-" * 80)
        lines.append(f"NODE: {node_id}{flags(node)}")
        lines.append(f"PRESSURE: {node.pressure:.2f} | INBOUND: {inbound[node_id]}")
        lines.append(f"AI: {clean(node.ai_line)}")
        lines.append("")
        lines.append("PURPOSE / AUTHORING NOTE:")
        if any(k in node_id for k in ["drug", "supply", "josh", "father", "network"]):
            lines.append("  Drug/supply branch: answer the player's concrete question first, then widen the threat.")
        elif any(k in node_id for k in ["love", "romantic", "touch"]):
            lines.append("  Intimacy branch: avoid repeating denial/love pressure without a new fact or emotional shift.")
        elif "pause" in node_id:
            lines.append("  Pause branch: should change pace, not simply delay the next question.")
        elif "final" in node_id:
            lines.append("  Final branch: ending should match the accumulated emotional trajectory.")
        else:
            lines.append("  Check whether this beat changes topic, power, intimacy, certainty, or threat.")
        lines.append("")
        lines.append("ROUTES:")
        if not node.choices:
            lines.append("  END")
        for i, choice in enumerate(node.choices, 1):
            tags = ", ".join(choice.semantic_tags) if choice.semantic_tags else "none"
            lines.append(f"  {i}) PLAYER: {clean(choice.text)}")
            lines.append(f"     INTENT: {choice.intent}")
            lines.append(f"     TAGS: {tags}")
            lines.append(f"     STATE: {delta(choice)}")
            lines.append(f"     NEXT: {choice.next_question_id or 'SELECTOR -> next unasked question'}")
            lines.append("     REAUTHOR TODO: [ ]")
            lines.append("")
        lines.append("CHECKLIST:")
        lines.append("  [ ] Does the AI response fit the actual player answer?")
        lines.append("  [ ] Does this transition feel psychologically earned?")
        lines.append("  [ ] Does the next node follow logically from this answer?")
        lines.append("  [ ] Should this be split into a finer-grained response node?")
        lines.append("")
    return lines


def main():
    scene = EngineStyleScene(DummyController(), DummyHearingAI(), DummyEngram(), clamp01)
    nodes = scene.question_nodes()
    lines = route_overview(nodes) + authoring_cards(nodes)
    txt = "\n".join(lines)
    (ROOT / "text_dialogue_graph.txt").write_text(txt, encoding="utf-8")
    (ROOT / "text_dialogue_graph.md").write_text("```text\n" + txt + "\n```\n", encoding="utf-8")
    print("Wrote text_dialogue_graph.txt and text_dialogue_graph.md")


if __name__ == "__main__":
    main()
