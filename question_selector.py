from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass
from typing import Any

from classifications import classification_distribution


TRAIT_BY_CONTEXT = {
    "authority": "compliance",
    "loyalty": "loyalty",
    "association": "loyalty",
    "deception": "deception",
    "risk": "risk",
    "empathy": "empathy",
    "final": "risk",
}


@dataclass(frozen=True, slots=True)
class QuestionScore:
    question_id: str
    total: float
    information_gain: float
    pressure: float
    ambiguity: float
    context_coverage: float


def _classification_ambiguity(snapshot: dict[str, float]) -> float:
    distribution = classification_distribution(snapshot)
    top_two = sorted(distribution.values(), reverse=True)[:2]
    if len(top_two) < 2:
        return 0.0
    return max(0.0, min(1.0, 1.0 - (top_two[0] - top_two[1])))


def _selector_context(node: Any) -> str:
    return getattr(node, "target_context", None) or node.reaction_context


def _context_counts(nodes: dict[str, Any], asked_question_ids: set[str]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for question_id in asked_question_ids:
        node = nodes.get(question_id)
        if node is not None:
            counts[_selector_context(node)] += 1
    return counts


def _trait_information_gain(node: Any, posterior: dict[str, dict[str, float]]) -> float:
    context_trait = TRAIT_BY_CONTEXT.get(_selector_context(node))
    trait_uncertainties = []

    if context_trait is not None:
        trait_uncertainties.append(posterior.get(context_trait, {}).get("uncertainty", 0.0))

    discriminates = getattr(node, "discriminates", ())
    for trait in discriminates:
        if trait in posterior:
            trait_uncertainties.append(posterior[trait].get("uncertainty", 0.0))

    tag_traits = []
    for choice in node.choices:
        tags = set(choice.semantic_tags)
        if {"compliance", "authority"} & tags:
            tag_traits.append("compliance")
        if "loyalty" in tags:
            tag_traits.append("loyalty")
        if {"deception", "deflection", "denial"} & tags:
            tag_traits.append("deception")
        if {"dissident_risk", "challenge", "counterattack", "refusal"} & tags:
            tag_traits.append("risk")
        if "empathy" in tags:
            tag_traits.append("empathy")

    if tag_traits:
        tag_uncertainty = sum(posterior.get(trait, {}).get("uncertainty", 0.0) for trait in tag_traits) / len(tag_traits)
        trait_uncertainties.append(tag_uncertainty)

    if not trait_uncertainties:
        return 0.0

    base_gain = max(trait_uncertainties)
    hint = getattr(node, "information_gain_hint", None)
    if hint is None:
        return base_gain
    hint_multiplier = 0.75 + 0.50 * max(0.0, min(1.0, hint))
    return max(0.0, min(1.0, base_gain * hint_multiplier))


def score_question(
    question_id: str,
    nodes: dict[str, Any],
    asked_question_ids: set[str],
    citizen_posterior: dict[str, dict[str, float]],
    citizen_snapshot: dict[str, float],
) -> QuestionScore:
    node = nodes[question_id]
    context_counts = _context_counts(nodes, asked_question_ids)
    max_seen = max(context_counts.values(), default=0)

    information_gain = _trait_information_gain(node, citizen_posterior)
    pressure = node.pressure
    ambiguity = _classification_ambiguity(citizen_snapshot)
    selector_context = _selector_context(node)
    context_seen = context_counts[selector_context]
    context_coverage = (max_seen - context_seen + 1) / (max_seen + 1) if max_seen else 1.0

    if selector_context == "final" and len(asked_question_ids) < 5:
        pressure *= 0.45

    total = (
        information_gain * 0.42
        + pressure * 0.24
        + ambiguity * 0.22
        + context_coverage * 0.12
    )
    return QuestionScore(
        question_id=question_id,
        total=total,
        information_gain=information_gain,
        pressure=pressure,
        ambiguity=ambiguity,
        context_coverage=context_coverage,
    )


def select_next_question_id(
    nodes: dict[str, Any],
    asked_question_ids: set[str],
    citizen_posterior: dict[str, dict[str, float]],
    citizen_snapshot: dict[str, float],
    seed: int | None = None,
) -> str:
    available = [
        question_id
        for question_id, node in nodes.items()
        if question_id != "final" and node.choices and question_id not in asked_question_ids
    ]
    if not available:
        return "final"

    scores = [
        score_question(question_id, nodes, asked_question_ids, citizen_posterior, citizen_snapshot)
        for question_id in available
    ]

    if seed is None:
        return max(scores, key=lambda score: (score.total, score.information_gain, score.pressure, score.question_id)).question_id

    top_score = max(score.total for score in scores)
    candidates = [score for score in scores if top_score - score.total <= 0.03]
    rng = random.Random(seed + len(asked_question_ids))
    return rng.choice(sorted(candidates, key=lambda score: score.question_id)).question_id
