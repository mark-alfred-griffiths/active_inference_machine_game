from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dialogue_questions import SOCIAL_CREDIT_QUESTION_POOL

OUTPUT_PATH = PROJECT_ROOT / "audit_scene_balance.md"
HIGH_PRESSURE = 0.84
LOW_PRESSURE = 0.60
EXPECTED_CHOICES = 3
RISK_TAGS = {"dissident_risk", "challenge", "refusal", "deception", "deflection", "denial", "counterattack"}
SAFE_TAGS = {"compliance", "authority", "loyalty", "honesty", "caution", "boundary"}


def fmt(value: float) -> str:
    return f"{value:.3f}"


def choice_kind(tags: set[str]) -> str:
    if "compliance" in tags and not (tags & RISK_TAGS):
        return "compliant-safe"
    if "empathy" in tags and not (tags & RISK_TAGS):
        return "empathetic-safe"
    if "dissident_risk" in tags or "challenge" in tags or "refusal" in tags:
        return "risk-signalling"
    if "deception" in tags or "deflection" in tags or "denial" in tags:
        return "evasive/deceptive"
    if "boundary" in tags or "partial_admission" in tags:
        return "conditional-boundary"
    return "other"


def audit() -> tuple[str, dict[str, object]]:
    nodes = SOCIAL_CREDIT_QUESTION_POOL
    playable_nodes = [node for node in nodes.values() if node.choices]
    choices = [choice for node in playable_nodes for choice in node.choices]

    tag_counts = Counter(tag for choice in choices for tag in choice.semantic_tags)
    context_counts = Counter(node.reaction_context for node in nodes.values())
    target_context_counts = Counter(node.target_context or node.reaction_context for node in nodes.values())
    discriminates_counts = Counter(tag for node in playable_nodes for tag in node.discriminates)
    kind_counts = Counter(choice_kind(set(choice.semantic_tags)) for choice in choices)

    missing_discriminates = [node.id for node in playable_nodes if not node.discriminates]
    tags_used_once = sorted(tag for tag, count in tag_counts.items() if count == 1)
    high_pressure = sorted((node.id, node.pressure) for node in playable_nodes if node.pressure >= HIGH_PRESSURE)
    low_pressure = sorted((node.id, node.pressure) for node in playable_nodes if node.pressure <= LOW_PRESSURE)
    choice_count_issues = sorted((node.id, len(node.choices)) for node in nodes.values() if node.id != "final" and len(node.choices) != EXPECTED_CHOICES)
    duplicate_choice_issues = []
    for node in playable_nodes:
        text_counts = Counter(choice.text for choice in node.choices)
        intent_counts = Counter(choice.intent for choice in node.choices)
        duplicate_text = sorted(text for text, count in text_counts.items() if count > 1)
        duplicate_intents = sorted(intent for intent, count in intent_counts.items() if count > 1)
        if duplicate_text or duplicate_intents:
            duplicate_choice_issues.append((node.id, duplicate_text, duplicate_intents))

    by_context: dict[str, list[float]] = defaultdict(list)
    by_context_suspicion: dict[str, list[float]] = defaultdict(list)
    for node in playable_nodes:
        for choice in node.choices:
            context = node.reaction_context
            by_context[context].append(choice.trust_delta)
            by_context_suspicion[context].append(choice.suspicion_delta)

    kind_deltas: dict[str, dict[str, list[float]]] = defaultdict(lambda: {"trust": [], "suspicion": []})
    for choice in choices:
        kind = choice_kind(set(choice.semantic_tags))
        kind_deltas[kind]["trust"].append(choice.trust_delta)
        kind_deltas[kind]["suspicion"].append(choice.suspicion_delta)

    node_balance = []
    for node in playable_nodes:
        kinds = Counter(choice_kind(set(choice.semantic_tags)) for choice in node.choices)
        trust_avg = mean(choice.trust_delta for choice in node.choices)
        suspicion_avg = mean(choice.suspicion_delta for choice in node.choices)
        has_safe = kinds["compliant-safe"] + kinds["empathetic-safe"] > 0
        has_risk = kinds["risk-signalling"] > 0
        status = "ok" if has_safe and has_risk and len(node.choices) == EXPECTED_CHOICES else "review"
        node_balance.append((status, node.id, node.reaction_context, dict(kinds), trust_avg, suspicion_avg))

    review_nodes = [row for row in node_balance if row[0] == "review"]
    highest_suspicion_nodes = sorted(node_balance, key=lambda row: row[5], reverse=True)[:12]
    lowest_trust_nodes = sorted(node_balance, key=lambda row: row[4])[:12]

    lines: list[str] = []
    lines.append("# Citizen Scene Balance Audit")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Nodes: {len(nodes)} total, {len(playable_nodes)} playable, {len(nodes) - len(playable_nodes)} terminal")
    lines.append(f"- Choices: {len(choices)}")
    lines.append(f"- Average trust_delta: {fmt(mean(choice.trust_delta for choice in choices))}")
    lines.append(f"- Average suspicion_delta: {fmt(mean(choice.suspicion_delta for choice in choices))}")
    lines.append(f"- Missing discriminates: {len(missing_discriminates)}")
    lines.append(f"- Choice-count issues: {len(choice_count_issues)}")
    lines.append(f"- Duplicate choice issues: {len(duplicate_choice_issues)}")
    lines.append("")

    lines.append("## Context Counts")
    for context, count in sorted(context_counts.items()):
        lines.append(f"- {context}: {count}")
    lines.append("")

    lines.append("## Target Context Counts")
    for context, count in sorted(target_context_counts.items()):
        lines.append(f"- {context}: {count}")
    lines.append("")

    lines.append("## Choice Kind Counts")
    for kind, count in sorted(kind_counts.items()):
        trust_values = kind_deltas[kind]["trust"]
        suspicion_values = kind_deltas[kind]["suspicion"]
        lines.append(f"- {kind}: {count}; avg trust {fmt(mean(trust_values))}; avg suspicion {fmt(mean(suspicion_values))}")
    lines.append("")

    lines.append("## Top Semantic Tags")
    for tag, count in tag_counts.most_common(30):
        lines.append(f"- {tag}: {count}")
    lines.append("")

    lines.append("## Discriminates Counts")
    for trait, count in sorted(discriminates_counts.items()):
        lines.append(f"- {trait}: {count}")
    lines.append("")

    lines.append("## Context Delta Averages")
    for context in sorted(by_context):
        lines.append(f"- {context}: avg trust {fmt(mean(by_context[context]))}; avg suspicion {fmt(mean(by_context_suspicion[context]))}")
    lines.append("")

    lines.append("## Missing Discriminates")
    if missing_discriminates:
        for node_id in missing_discriminates:
            lines.append(f"- {node_id}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Tags Used Once")
    if tags_used_once:
        for tag in tags_used_once:
            lines.append(f"- {tag}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Pressure Review")
    lines.append("### High Pressure")
    if high_pressure:
        for node_id, pressure in high_pressure:
            lines.append(f"- {node_id}: {pressure:.2f}")
    else:
        lines.append("- None")
    lines.append("### Low Pressure")
    if low_pressure:
        for node_id, pressure in low_pressure:
            lines.append(f"- {node_id}: {pressure:.2f}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Choice Count Issues")
    if choice_count_issues:
        for node_id, count in choice_count_issues:
            lines.append(f"- {node_id}: {count} choices")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Duplicate Choice Issues")
    if duplicate_choice_issues:
        for node_id, duplicate_text, duplicate_intents in duplicate_choice_issues:
            lines.append(f"- {node_id}: duplicate_text={duplicate_text}; duplicate_intents={duplicate_intents}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Choice Balance Review")
    if review_nodes:
        for _, node_id, context, kinds, trust_avg, suspicion_avg in review_nodes:
            lines.append(f"- {node_id} ({context}): {kinds}; avg trust {fmt(trust_avg)}; avg suspicion {fmt(suspicion_avg)}")
    else:
        lines.append("- All playable nodes include both a safe/compliant path and a risk-signalling path.")
    lines.append("")

    lines.append("## Highest Average Suspicion Nodes")
    for _, node_id, context, kinds, trust_avg, suspicion_avg in highest_suspicion_nodes:
        lines.append(f"- {node_id} ({context}): avg suspicion {fmt(suspicion_avg)}; avg trust {fmt(trust_avg)}; {kinds}")
    lines.append("")

    lines.append("## Lowest Average Trust Nodes")
    for _, node_id, context, kinds, trust_avg, suspicion_avg in lowest_trust_nodes:
        lines.append(f"- {node_id} ({context}): avg trust {fmt(trust_avg)}; avg suspicion {fmt(suspicion_avg)}; {kinds}")
    lines.append("")

    metrics = {
        "nodes": len(nodes),
        "playable_nodes": len(playable_nodes),
        "choices": len(choices),
        "avg_trust_delta": mean(choice.trust_delta for choice in choices),
        "avg_suspicion_delta": mean(choice.suspicion_delta for choice in choices),
        "missing_discriminates": missing_discriminates,
        "choice_count_issues": choice_count_issues,
        "duplicate_choice_issues": duplicate_choice_issues,
        "tags_used_once": tags_used_once,
    }
    return "\n".join(lines) + "\n", metrics


def main() -> None:
    report, metrics = audit()
    OUTPUT_PATH.write_text(report, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"nodes={metrics['nodes']} playable={metrics['playable_nodes']} choices={metrics['choices']}")
    print(f"avg_trust_delta={metrics['avg_trust_delta']:.3f}")
    print(f"avg_suspicion_delta={metrics['avg_suspicion_delta']:.3f}")
    print(f"missing_discriminates={len(metrics['missing_discriminates'])}")
    print(f"choice_count_issues={len(metrics['choice_count_issues'])}")
    print(f"duplicate_choice_issues={len(metrics['duplicate_choice_issues'])}")


if __name__ == "__main__":
    main()
