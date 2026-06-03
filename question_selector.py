from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass
from typing import Any

from classifications import classification_distribution


TRAIT_INFORMATION_WEIGHT = 0.38
QUESTION_PRESSURE_WEIGHT = 0.21
CLASSIFICATION_AMBIGUITY_WEIGHT = 0.19
CONTEXT_COVERAGE_WEIGHT = 0.10
FACT_PROBE_WEIGHT = 0.002
CONTRADICTION_PROBE_WEIGHT = 0.05
PROTECTED_INTEREST_WEIGHT = 0.002
EXPOSED_FACT_PENALTY_WEIGHT = 0.02
NEURAL_PROBE_INTENT_WEIGHT = 0.001
STORY_PRESSURE_WARMUP_TURNS = 5

TRAIT_BY_CONTEXT = {
    "authority": "compliance",
    "loyalty": "loyalty",
    "association": "loyalty",
    "deception": "deception",
    "risk": "risk",
    "empathy": "empathy",
    "final": "risk",
}

AMBIGUOUS_CLAIM_REFINEMENTS = {"conditional", "private", "procedural", "protected", "unknown", "partial", "legal_only"}
DIRECT_CLAIM_VALUES = {"true", "false"}


@dataclass(frozen=True, slots=True)
class QuestionScore:
    question_id: str
    total: float
    information_gain: float
    pressure: float
    ambiguity: float
    context_coverage: float
    fact_probe_gain: float = 0.0
    contradiction_probe_gain: float = 0.0
    protected_interest_pressure: float = 0.0
    exposed_fact_penalty: float = 0.0
    neural_probe_alignment: float = 0.0

    def reason(self) -> str:
        components = [
            ("trait", self.information_gain * TRAIT_INFORMATION_WEIGHT),
            ("pressure", self.pressure * QUESTION_PRESSURE_WEIGHT),
            ("ambiguity", self.ambiguity * CLASSIFICATION_AMBIGUITY_WEIGHT),
            ("coverage", self.context_coverage * CONTEXT_COVERAGE_WEIGHT),
            ("fact", self.fact_probe_gain * FACT_PROBE_WEIGHT),
            ("contradiction", self.contradiction_probe_gain * CONTRADICTION_PROBE_WEIGHT),
            ("protected", self.protected_interest_pressure * PROTECTED_INTEREST_WEIGHT),
            ("neural_probe", self.neural_probe_alignment * NEURAL_PROBE_INTENT_WEIGHT),
        ]
        positive = [(label, value) for label, value in components if value > 0.0]
        top = sorted(positive, key=lambda item: item[1], reverse=True)[:3]
        return ", ".join(f"{label}={value:.3f}" for label, value in top)


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


def _fact_sensitivity(case_file_summary: dict[str, Any] | None, fact_key: str) -> float:
    if not case_file_summary:
        return 0.0
    for fact in case_file_summary.get("facts", []):
        if fact.get("key") == fact_key:
            return max(0.0, min(1.0, float(fact.get("sensitivity", 0.0))))
    return 0.0


def _unrevealed_fact_keys(case_file_summary: dict[str, Any] | None) -> set[str]:
    if not case_file_summary:
        return set()
    return {
        str(fact["key"])
        for fact in case_file_summary.get("facts", [])
        if not fact.get("revealed")
    }


def _interest_pressure(case_file_summary: dict[str, Any] | None, protected_fact_keys: set[str]) -> set[str]:
    if not case_file_summary or not protected_fact_keys:
        return set()
    pressured_interests: set[str] = set()
    for interest in case_file_summary.get("interests", []):
        protected_by_interest = set(str(key) for key in interest.get("protected_fact_keys", []))
        if protected_by_interest & protected_fact_keys:
            pressured_interests.add(str(interest.get("key")))
    return pressured_interests


def _story_state(
    case_file_summary: dict[str, Any] | None,
    claims_ledger_summary: dict[str, Any] | None,
) -> dict[str, set[str]]:
    claims_ledger_summary = claims_ledger_summary or {}
    contradicted_fact_keys: set[str] = set()
    # The ledger summary stores aggregate claims, not individual contradiction events.
    # Treat facts with multiple incompatible claimed values as contradicted.
    for fact_key, claims in claims_ledger_summary.get("claims_by_fact", {}).items():
        claimed_values = [str(claim.get("claimed_value")) for claim in claims]
        for index, previous in enumerate(claimed_values):
            for current in claimed_values[index + 1:]:
                if _claims_contradict(previous, current):
                    contradicted_fact_keys.add(str(fact_key))
                    break
    protected_fact_keys = set(str(key) for key in claims_ledger_summary.get("protected_fact_keys", []))
    exposed_fact_keys = set(str(key) for key in claims_ledger_summary.get("exposed_fact_keys", []))
    return {
        "unrevealed_fact_keys": _unrevealed_fact_keys(case_file_summary),
        "contradicted_fact_keys": contradicted_fact_keys,
        "protected_fact_keys": protected_fact_keys,
        "exposed_fact_keys": exposed_fact_keys,
        "pressured_interest_keys": _interest_pressure(case_file_summary, protected_fact_keys),
    }


def _claims_contradict(previous: str, current: str) -> bool:
    if previous == current:
        return False
    if previous in AMBIGUOUS_CLAIM_REFINEMENTS and current in AMBIGUOUS_CLAIM_REFINEMENTS:
        return False
    if previous in DIRECT_CLAIM_VALUES and current in DIRECT_CLAIM_VALUES:
        return previous != current
    if previous in DIRECT_CLAIM_VALUES and current in AMBIGUOUS_CLAIM_REFINEMENTS:
        return False
    if previous in AMBIGUOUS_CLAIM_REFINEMENTS and current in DIRECT_CLAIM_VALUES:
        return False
    return previous != current


def _average_sensitive_overlap(
    fact_keys: set[str],
    target_keys: set[str],
    case_file_summary: dict[str, Any] | None,
) -> float:
    overlap = fact_keys & target_keys
    if not overlap:
        return 0.0
    return sum(_fact_sensitivity(case_file_summary, key) for key in overlap) / len(overlap)


def _story_gains(
    node: Any,
    case_file_summary: dict[str, Any] | None,
    claims_ledger_summary: dict[str, Any] | None,
) -> tuple[float, float, float, float]:
    state = _story_state(case_file_summary, claims_ledger_summary)
    probes_facts = set(str(key) for key in getattr(node, "probes_facts", ()))
    probes_claims = set(str(key) for key in getattr(node, "probes_claims", ()))
    pressure_on_interests = set(str(key) for key in getattr(node, "pressure_on_interests", ()))

    fact_probe_gain = _average_sensitive_overlap(
        probes_facts,
        state["unrevealed_fact_keys"],
        case_file_summary,
    )
    contradiction_probe_gain = _average_sensitive_overlap(
        probes_facts | probes_claims,
        state["contradicted_fact_keys"],
        case_file_summary,
    )
    protected_interest_pressure = 1.0 if pressure_on_interests & state["pressured_interest_keys"] else 0.0
    exposed_fact_penalty = _average_sensitive_overlap(
        probes_facts,
        state["exposed_fact_keys"],
        case_file_summary,
    )
    return fact_probe_gain, contradiction_probe_gain, protected_interest_pressure, exposed_fact_penalty


def _probe_intent_alignment(
    node: Any,
    preferred_probe_intent: str | None,
    case_file_summary: dict[str, Any] | None,
    claims_ledger_summary: dict[str, Any] | None,
) -> float:
    if not preferred_probe_intent:
        return 0.0

    state = _story_state(case_file_summary, claims_ledger_summary)
    context = _selector_context(node)
    discriminates = set(str(trait) for trait in getattr(node, "discriminates", ()))
    probes_facts = set(str(key) for key in getattr(node, "probes_facts", ()))
    probes_claims = set(str(key) for key in getattr(node, "probes_claims", ()))
    pressure_on_interests = set(str(key) for key in getattr(node, "pressure_on_interests", ()))

    if preferred_probe_intent == "probe_compliance":
        return 1.0 if context in {"authority", "compliance"} or "compliance" in discriminates else 0.0
    if preferred_probe_intent == "probe_loyalty":
        return 1.0 if context in {"loyalty", "association"} or "loyalty" in discriminates else 0.0
    if preferred_probe_intent == "probe_deception":
        if context == "deception" or "deception" in discriminates:
            return 1.0
        return 0.6 if probes_claims else 0.0
    if preferred_probe_intent == "probe_risk":
        return 1.0 if context == "risk" or "risk" in discriminates else 0.0
    if preferred_probe_intent == "probe_empathy":
        return 1.0 if context == "empathy" or "empathy" in discriminates else 0.0
    if preferred_probe_intent == "probe_contradiction":
        contradicted_overlap = (probes_facts | probes_claims) & state["contradicted_fact_keys"]
        if contradicted_overlap:
            return 1.0
        return 0.65 if probes_claims else 0.0
    if preferred_probe_intent == "probe_protected_fact":
        protected_overlap = probes_facts & state["protected_fact_keys"]
        interest_overlap = pressure_on_interests & state["pressured_interest_keys"]
        if protected_overlap or interest_overlap:
            return 1.0
        return 0.55 if probes_facts or pressure_on_interests else 0.0
    if preferred_probe_intent == "probe_final_answer":
        return 1.0 if context == "final" else 0.0
    return 0.0


def score_question(
    question_id: str,
    nodes: dict[str, Any],
    asked_question_ids: set[str],
    citizen_posterior: dict[str, dict[str, float]],
    citizen_snapshot: dict[str, float],
    case_file_summary: dict[str, Any] | None = None,
    claims_ledger_summary: dict[str, Any] | None = None,
    preferred_probe_intent: str | None = None,
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
    fact_probe_gain, contradiction_probe_gain, protected_interest_pressure, exposed_fact_penalty = _story_gains(
        node,
        case_file_summary,
        claims_ledger_summary,
    )
    if len(asked_question_ids) < STORY_PRESSURE_WARMUP_TURNS and contradiction_probe_gain <= 0.0:
        fact_probe_gain = 0.0
        protected_interest_pressure = 0.0
        exposed_fact_penalty = 0.0
    neural_probe_alignment = _probe_intent_alignment(
        node,
        preferred_probe_intent,
        case_file_summary,
        claims_ledger_summary,
    )

    if selector_context == "final" and len(asked_question_ids) < 5:
        pressure *= 0.45

    total = (
        information_gain * TRAIT_INFORMATION_WEIGHT
        + pressure * QUESTION_PRESSURE_WEIGHT
        + ambiguity * CLASSIFICATION_AMBIGUITY_WEIGHT
        + context_coverage * CONTEXT_COVERAGE_WEIGHT
        + fact_probe_gain * FACT_PROBE_WEIGHT
        + contradiction_probe_gain * CONTRADICTION_PROBE_WEIGHT
        + protected_interest_pressure * PROTECTED_INTEREST_WEIGHT
        + neural_probe_alignment * NEURAL_PROBE_INTENT_WEIGHT
        - exposed_fact_penalty * EXPOSED_FACT_PENALTY_WEIGHT
    )
    return QuestionScore(
        question_id=question_id,
        total=total,
        information_gain=information_gain,
        pressure=pressure,
        ambiguity=ambiguity,
        context_coverage=context_coverage,
        fact_probe_gain=fact_probe_gain,
        contradiction_probe_gain=contradiction_probe_gain,
        protected_interest_pressure=protected_interest_pressure,
        exposed_fact_penalty=exposed_fact_penalty,
        neural_probe_alignment=neural_probe_alignment,
    )


def score_available_questions(
    nodes: dict[str, Any],
    asked_question_ids: set[str],
    citizen_posterior: dict[str, dict[str, float]],
    citizen_snapshot: dict[str, float],
    case_file_summary: dict[str, Any] | None = None,
    claims_ledger_summary: dict[str, Any] | None = None,
    preferred_probe_intent: str | None = None,
) -> list[QuestionScore]:
    available = [
        question_id
        for question_id, node in nodes.items()
        if question_id != "final" and node.choices and question_id not in asked_question_ids
    ]
    if not available:
        return []

    return [
        score_question(
            question_id,
            nodes,
            asked_question_ids,
            citizen_posterior,
            citizen_snapshot,
            case_file_summary,
            claims_ledger_summary,
            preferred_probe_intent,
        )
        for question_id in available
    ]


def select_next_question_id(
    nodes: dict[str, Any],
    asked_question_ids: set[str],
    citizen_posterior: dict[str, dict[str, float]],
    citizen_snapshot: dict[str, float],
    case_file_summary: dict[str, Any] | None = None,
    claims_ledger_summary: dict[str, Any] | None = None,
    preferred_probe_intent: str | None = None,
    seed: int | None = None,
) -> str:
    scores = score_available_questions(
        nodes,
        asked_question_ids,
        citizen_posterior,
        citizen_snapshot,
        case_file_summary,
        claims_ledger_summary,
        preferred_probe_intent,
    )
    if not scores:
        return "final"

    if seed is None:
        return max(scores, key=lambda score: (score.total, score.information_gain, score.pressure, score.question_id)).question_id

    top_score = max(score.total for score in scores)
    candidates = [score for score in scores if top_score - score.total <= 0.03]
    rng = random.Random(seed + len(asked_question_ids))
    return rng.choice(sorted(candidates, key=lambda score: score.question_id)).question_id
