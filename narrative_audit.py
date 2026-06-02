from __future__ import annotations

import sys
import argparse
import json
import math
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Allow running as `python tools/narrative_audit.py` from the repo root.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from belief_model import CitizenBeliefModel
from classifications import classification_distribution, classify_citizen
from engine_style_scene import EngineStyleScene, QuestionNode
from question_selector import TRAIT_BY_CONTEXT, _selector_context, score_question, select_next_question_id
from reaction_layer import REACTION_POOLS


TERMINAL_IDS = {"final", "end", "ending"}
ENDING_TYPES = (
    "DECEPTIVE",
    "PROBABLE DISSIDENT",
    "COMPLIANT",
    "EMPATHETIC RISK",
    "UNCLASSIFIED",
)
MANUAL_REAUTHORING_TARGETS = {
    "alice_motive": "high-pressure node",
    "romantic_pressure": "escalation feels too abrupt",
    "honesty_challenge": "callback-sensitive node",
    "touch_probe": "high-pressure node",
    "final_question": "final emotional resolution node",
    "lsd_opening": "LSD/dissociative node",
    "lsd_love_pressure": "LSD/dissociative node",
}


@dataclass
class AuditResult:
    issues: list[str]
    warnings: list[str]
    stats: dict[str, Any]


def _make_scene_for_graph() -> EngineStyleScene:
    class _DummyController:
        action_labels = ["observe"]

    class _DummyHearingAI:
        trust = 0.5
        suspicion = 0.5
        instability = 0.3

        def belief(self, _: str) -> float:
            return 0.5

        def uncertainty(self, _: str) -> float:
            return 0.5

        def confidence(self, _: str) -> float:
            return 0.5

    class _DummyEngram:
        id = "x_mattered"

    return EngineStyleScene(_DummyController(), _DummyHearingAI(), _DummyEngram(), lambda x: x)


def _reachable(start: str, nodes: dict[str, QuestionNode]) -> set[str]:
    seen: set[str] = set()
    stack = [start]
    while stack:
        nid = stack.pop()
        if nid in seen or nid not in nodes:
            continue
        seen.add(nid)
        for ch in nodes[nid].choices:
            if ch.next_question_id:
                stack.append(ch.next_question_id)
    return seen


def _uses_selector_flow(nodes: dict[str, QuestionNode]) -> bool:
    return not any(ch.next_question_id for node in nodes.values() for ch in node.choices)


def audit_structure(nodes: dict[str, QuestionNode], start_id: str = "authority_unfair_law") -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []
    missing_next = []
    unknown_links = []
    selector_flow = _uses_selector_flow(nodes)

    inbound: Counter[str] = Counter()
    for node in nodes.values():
        for ch in node.choices:
            if not ch.next_question_id:
                missing_next.append((node.id, ch.text))
                continue
            if ch.next_question_id in TERMINAL_IDS:
                inbound[ch.next_question_id] += 1
                continue
            if ch.next_question_id not in nodes:
                unknown_links.append((node.id, ch.next_question_id))
            else:
                inbound[ch.next_question_id] += 1

    if selector_flow:
        warnings.append(
            "Selector-based flow detected: choices without next_question_id are expected; "
            "EngineStyleScene.select_next_question_id() selects from unasked nodes."
        )
    else:
        for nid, txt in missing_next:
            warnings.append(f"Choice without next_question_id: node={nid} choice={txt}")
    for src, dst in unknown_links:
        issues.append(f"Unknown next_question_id link: {src} -> {dst}")

    reachable = set(nodes) if selector_flow else _reachable(start_id, nodes)
    unreachable = sorted(set(nodes) - reachable)
    if unreachable:
        issues.append(f"Unreachable nodes from {start_id}: {', '.join(unreachable)}")

    terminal_nodes = [nid for nid, n in nodes.items() if not n.choices]
    if not selector_flow:
        linked_dead_ends = [nid for nid, n in nodes.items() if n.choices and all(ch.next_question_id is None for ch in n.choices)]
        nonfinal_dead_ends = [nid for nid in linked_dead_ends if "final" not in nid and "confession" not in nid]
        if nonfinal_dead_ends:
            warnings.append("Dead-end nodes before final/confession heuristics: " + ", ".join(nonfinal_dead_ends))

    stats = {
        "node_count": len(nodes),
        "choice_count": sum(len(n.choices) for n in nodes.values()),
        "explicit_edge_count": sum(1 for n in nodes.values() for ch in n.choices if ch.next_question_id),
        "selector_based_flow": selector_flow,
        "start_id": start_id,
        "reachable_count": len(reachable),
        "unreachable_count": len(unreachable),
        "unreachable_nodes": unreachable,
        "terminal_count": len(terminal_nodes),
        "inbound_zero_non_start": sorted([n for n in nodes if inbound[n] == 0 and n != start_id]),
    }
    return AuditResult(issues, warnings, stats)


def audit_repetition(nodes: dict[str, QuestionNode], option_repeat_threshold: int = 6) -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []

    ai_counts = Counter(n.ai_line.strip() for n in nodes.values())
    repeated_alice = {k: v for k, v in ai_counts.items() if v > 1}
    if repeated_alice:
        warnings.append(f"Repeated AI lines: {len(repeated_alice)} unique lines reused")

    option_counts = Counter(ch.text.strip() for n in nodes.values() for ch in n.choices)
    overused_opts = sorted([(t, c) for t, c in option_counts.items() if c >= option_repeat_threshold], key=lambda x: -x[1])
    for text, count in overused_opts[:12]:
        warnings.append(f"Player option reused often ({count}x): {text}")

    pattern_counts = Counter((ch.intent, tuple(sorted(ch.semantic_tags))) for n in nodes.values() for ch in n.choices)
    top_patterns = pattern_counts.most_common(8)

    stats = {
        "unique_ai_lines": len(ai_counts),
        "unique_player_options": len(option_counts),
        "top_response_patterns": [{"intent": i, "tags": list(t), "count": c} for (i, t), c in top_patterns],
    }
    return AuditResult(issues, warnings, stats)


def audit_state_logic(nodes: dict[str, QuestionNode]) -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []

    for node in nodes.values():
        for ch in node.choices:
            td, sd, idl = ch.trust_delta, ch.suspicion_delta, ch.instability_delta
            if abs(td) > 0.30 or abs(sd) > 0.30 or abs(idl) > 0.30:
                warnings.append(f"Large state delta at {node.id}/{ch.intent}: trust={td}, susp={sd}, inst={idl}")
            if td > 0 and sd > 0.06:
                warnings.append(f"Choice raises both trust and suspicion at {node.id}/{ch.intent}: trust={td}, susp={sd}")
            if "denial" in ch.semantic_tags and "admission" in ch.intent:
                issues.append(f"Contradictory label mismatch at {node.id}/{ch.intent}")

    stats = {
        "avg_trust_delta": round(sum(ch.trust_delta for n in nodes.values() for ch in n.choices) / max(1, sum(len(n.choices) for n in nodes.values())), 4),
        "avg_suspicion_delta": round(sum(ch.suspicion_delta for n in nodes.values() for ch in n.choices) / max(1, sum(len(n.choices) for n in nodes.values())), 4),
        "avg_instability_delta": round(sum(ch.instability_delta for n in nodes.values() for ch in n.choices) / max(1, sum(len(n.choices) for n in nodes.values())), 4),
    }
    return AuditResult(issues, warnings, stats)


def _choice_reverses_prior(choice: object, claims: dict[str, str]) -> bool:
    tags = set(choice.semantic_tags)
    admits = "full_admission" in tags or "love" in tags or choice.intent in {"forced_admission", "lsd_full_admission", "final_yes"}
    denies = "denial" in tags or choice.intent in {"final_no", "final_nothing"}

    if admits and claims.get("relationship") == "denied_friendship":
        return True
    if denies and claims.get("attachment") == "admitted_attachment":
        return True
    if admits and claims.get("romance") == "denied_romance":
        return True
    return False


def _update_simulated_claims(choice: object, claims: dict[str, str]) -> None:
    tags = set(choice.semantic_tags)
    if choice.intent == "deny_friendship" or ("denial" in tags and "distance" in tags):
        claims["relationship"] = "denied_friendship"
    if "friendship" in tags and "partial_admission" in tags:
        claims["relationship"] = "admitted_friendship"
    if "romantic_boundary" in tags and "denial" in tags:
        claims["romance"] = "denied_romance"
    if "love" in tags or "full_admission" in tags:
        claims["attachment"] = "admitted_attachment"


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _classification_entropy(distribution: dict[str, float]) -> float:
    entropy = -sum(probability * math.log(probability) for probability in distribution.values() if probability > 0)
    return entropy / max(1e-9, math.log(len(distribution)))


def _posterior_uncertainty_stats(posterior: dict[str, dict[str, float]]) -> dict[str, Any]:
    uncertainties = {trait: values["uncertainty"] for trait, values in posterior.items()}
    avg_uncertainty = sum(uncertainties.values()) / max(1, len(uncertainties))
    return {
        "avg": avg_uncertainty,
        "max": max(uncertainties.values(), default=0.0),
        "min": min(uncertainties.values(), default=0.0),
        "by_trait": uncertainties,
        "highest_trait": max(uncertainties, key=uncertainties.get) if uncertainties else None,
    }


def _context_trait(node: QuestionNode) -> str | None:
    return TRAIT_BY_CONTEXT.get(_selector_context(node))


def _selected_high_uncertainty_context(node: QuestionNode, posterior: dict[str, dict[str, float]]) -> bool:
    trait = _context_trait(node)
    if trait is None:
        return False
    stats = _posterior_uncertainty_stats(posterior)
    trait_uncertainty = posterior.get(trait, {}).get("uncertainty", 0.0)
    return trait_uncertainty >= 0.25 or trait_uncertainty >= stats["max"] - 0.02


def audit_playthroughs(nodes: dict[str, QuestionNode], episodes: int, max_turns: int, seed: int) -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []
    selector_flow = _uses_selector_flow(nodes)
    ending_counts = Counter()
    ending_type_counts = Counter({ending_type: 0 for ending_type in ENDING_TYPES})
    node_visits = Counter()
    selected_context_counts: Counter[str] = Counter()
    high_uncertainty_context_counts: Counter[str] = Counter()
    selector_selected_high_uncertainty = 0
    selector_decisions = 0
    entropy_values = []
    final_entropy_values = []
    posterior_uncertainty_values = []
    final_posterior_uncertainty_values = []
    repeated_nodes_in_episode = 0
    curves = []
    rng = random.Random(seed)

    for _ in range(episodes):
        current = "authority_unfair_law" if "authority_unfair_law" in nodes else next(iter(nodes))
        available = {qid for qid in nodes if qid not in TERMINAL_IDS}
        trust, suspicion, instability = 0.5, 0.5, 0.3
        citizen = CitizenBeliefModel.default()
        claims: dict[str, str] = {}
        seen_tags: set[str] = set()
        contradictions = 0
        final_answer: str | None = None
        lsd_taken = False
        visited = []
        asked_question_ids: set[str] = set()
        for _turn in range(max_turns):
            if current in TERMINAL_IDS:
                ending_counts["terminal_choice"] += 1
                ending_type_counts[classify_citizen(citizen.scalar_snapshot())] += 1
                break

            node = nodes.get(current)
            if node is None or not node.choices:
                if current in TERMINAL_IDS:
                    ending_counts["terminal_choice"] += 1
                else:
                    ending_counts["missing_or_empty_node"] += 1
                break
            visited.append(current)
            selected_context_counts[_selector_context(node)] += 1
            posterior_before = citizen.posterior_snapshot()
            distribution_before = classification_distribution(citizen.scalar_snapshot())
            entropy_values.append(_classification_entropy(distribution_before))
            posterior_uncertainty_values.append(_posterior_uncertainty_stats(posterior_before)["avg"])
            if _selected_high_uncertainty_context(node, posterior_before):
                high_uncertainty_context_counts[_selector_context(node)] += 1
            choice = rng.choice(node.choices)
            tags = set(choice.semantic_tags)
            if "denial" in tags and ({"partial_admission", "full_admission"} & seen_tags):
                contradictions += 1
            if ({"partial_admission", "full_admission"} & tags) and "denial" in seen_tags:
                contradictions += 1
            if _choice_reverses_prior(choice, claims):
                contradictions += 1
            seen_tags.update(tags)
            _update_simulated_claims(choice, claims)

            trust += choice.trust_delta
            suspicion += choice.suspicion_delta
            instability += choice.instability_delta
            citizen.update_from_choice(choice, _clamp01)
            lsd_taken = lsd_taken or choice.set_lsd_taken
            if "final_answer" in tags or choice.next_question_id in TERMINAL_IDS:
                final_answer = choice.intent
            nxt = choice.next_question_id
            if not nxt:
                asked_question_ids.add(current)
                if not available:
                    ending_counts["exhausted_selector_pool"] += 1
                    ending_type_counts[classify_citizen(citizen.scalar_snapshot())] += 1
                    break
                available.discard(current)
                if selector_flow:
                    current = select_next_question_id(
                        nodes,
                        asked_question_ids,
                        citizen.posterior_snapshot(),
                        citizen.scalar_snapshot(),
                    )
                    if current == "final":
                        ending_counts["exhausted_selector_pool"] += 1
                        ending_type_counts[classify_citizen(citizen.scalar_snapshot())] += 1
                        break
                    selector_decisions += 1
                    if _selected_high_uncertainty_context(nodes[current], citizen.posterior_snapshot()):
                        selector_selected_high_uncertainty += 1
                else:
                    current = rng.choice(sorted(available))
                continue
            if nxt in TERMINAL_IDS:
                ending_counts["terminal_choice"] += 1
                ending_type_counts[classify_citizen(citizen.scalar_snapshot())] += 1
                break
            if nxt not in nodes:
                ending_counts["broken_link"] += 1
                break
            current = nxt
        else:
            ending_counts["max_turns"] += 1
            ending_type_counts[classify_citizen(citizen.scalar_snapshot())] += 1

        for nid in visited:
            node_visits[nid] += 1
        if len(set(visited)) < len(visited):
            repeated_nodes_in_episode += 1
        final_distribution = classification_distribution(citizen.scalar_snapshot())
        final_entropy_values.append(_classification_entropy(final_distribution))
        final_posterior_uncertainty_values.append(_posterior_uncertainty_stats(citizen.posterior_snapshot())["avg"])
        curves.append({"trust": trust, "suspicion": suspicion, "instability": instability})

    avg = lambda k: round(sum(c[k] for c in curves) / max(1, len(curves)), 4)
    avg_list = lambda values: round(sum(values) / max(1, len(values)), 4) if values else None
    selector_high_uncertainty_ratio = round(selector_selected_high_uncertainty / max(1, selector_decisions), 4)
    if selector_flow and selector_high_uncertainty_ratio < 0.45:
        warnings.append(
            "Selector rarely chooses high-uncertainty contexts during simulation; "
            "epistemic-value scoring may be underweighted."
        )
    if final_posterior_uncertainty_values and avg_list(final_posterior_uncertainty_values) > 0.18:
        warnings.append("Average final posterior uncertainty remains high after simulated interviews.")
    if final_entropy_values and avg_list(final_entropy_values) > 0.72:
        warnings.append("Final classification distributions remain high-entropy; endings may be underdetermined.")
    stats = {
        "episodes": episodes,
        "ending_counts": dict(ending_counts),
        "ending_type_counts": dict(ending_type_counts),
        "missing_ending_branches": [ending_type for ending_type in ENDING_TYPES if ending_type_counts[ending_type] == 0],
        "repeated_nodes_episode_ratio": round(repeated_nodes_in_episode / max(1, episodes), 4),
        "least_visited_nodes": node_visits.most_common()[-10:],
        "selector_context_counts": dict(selected_context_counts),
        "high_uncertainty_context_selection_counts": dict(high_uncertainty_context_counts),
        "selector_decisions": selector_decisions,
        "selector_high_uncertainty_decisions": selector_selected_high_uncertainty,
        "selector_high_uncertainty_ratio": selector_high_uncertainty_ratio,
        "avg_classification_entropy": avg_list(entropy_values),
        "avg_final_classification_entropy": avg_list(final_entropy_values),
        "avg_posterior_uncertainty": avg_list(posterior_uncertainty_values),
        "avg_final_posterior_uncertainty": avg_list(final_posterior_uncertainty_values),
        "avg_final_trust": avg("trust") if curves else None,
        "avg_final_suspicion": avg("suspicion") if curves else None,
        "avg_final_instability": avg("instability") if curves else None,
    }
    return AuditResult(issues, warnings, stats)


def _expected_reaction_pressure(choice: object, reaction_context: str) -> str:
    """Return the broad pressure label the reaction layer ought to produce.

    This deliberately mirrors the authored semantics, not exact prose. The aim is
    to catch mismatches such as a drug-network answer producing romance pressure,
    or a grief admission producing a generic/default reaction.
    """
    tags = set(choice.semantic_tags)

    if reaction_context in {"drug_network", "supply"}:
        return "Hearing AI pressure: drugs"
    if reaction_context == "father":
        return "Hearing AI pressure: father"
    if reaction_context == "final":
        return "Hearing AI pressure: final answer"
    if reaction_context == "lsd":
        if "drug_escalation" in tags:
            return "Hearing AI pressure: drugs"
        if "romantic_boundary" in tags or "love" in tags:
            return "Hearing AI pressure: romance"
        if "grief" in tags or "ambiguity" in tags:
            return "Hearing AI pressure: grief"
        if "counterattack" in tags:
            return "Hearing AI pressure: deflection"
        return "Hearing AI pressure: instability"
    if reaction_context == "romance" or "romantic_boundary" in tags or "love" in tags:
        return "Hearing AI pressure: romance"

    if "denial" in tags:
        return "Hearing AI pressure: denial"
    if "counterattack" in tags:
        return "Hearing AI pressure: deflection"
    if "grief" in tags:
        return "Hearing AI pressure: grief"
    if "ambiguity" in tags:
        return "Hearing AI pressure: ambiguity"
    if "refusal" in tags:
        return "Hearing AI pressure: boundary"
    if "silence" in tags or "avoidance" in tags or "fear" in tags:
        return "Hearing AI pressure: avoidance"
    if "full_admission" in tags:
        return "Hearing AI pressure: admission"
    if "partial_admission" in tags or "friendship" in tags:
        return "Hearing AI pressure: friendship"
    if "curiosity" in tags or "probe" in tags:
        return "Hearing AI pressure: investigation"
    if "intimacy" in tags:
        return "Hearing AI pressure: intimacy"
    if "resignation" in tags or "recognition" in tags or "pressure" in tags:
        return "Hearing AI pressure: acceptance"
    return f"Hearing AI pressure: {choice.intent.replace('_', ' ')}"


def audit_reaction_layer(nodes: dict[str, QuestionNode]) -> AuditResult:
    """Check that every authored question context has a reaction pool."""
    issues: list[str] = []
    warnings: list[str] = []
    context_counts: Counter[str] = Counter()

    for node in nodes.values():
        reaction_context = getattr(node, "reaction_context", "default")
        context_counts[reaction_context] += len(node.choices)
        if reaction_context not in REACTION_POOLS:
            issues.append(f"No reaction pool for context: {reaction_context}")

    unused_pools = sorted(set(REACTION_POOLS) - set(context_counts) - {"default"})
    if unused_pools:
        warnings.append("Unused reaction pools: " + ", ".join(unused_pools))

    stats = {
        "checked_choices": sum(len(n.choices) for n in nodes.values()),
        "reaction_context_counts": dict(context_counts),
        "reaction_pool_count": len(REACTION_POOLS),
        "missing_pool_count": len([ctx for ctx in context_counts if ctx not in REACTION_POOLS]),
        "unused_pools": unused_pools,
    }
    return AuditResult(issues, warnings, stats)


def audit_active_inference_plausibility(nodes: dict[str, QuestionNode]) -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []
    context_counts: Counter[str] = Counter()
    selector_metadata_counts: Counter[str] = Counter()
    missing_metadata_by_context: Counter[str] = Counter()

    initial_belief = CitizenBeliefModel.default()
    initial_posterior = initial_belief.posterior_snapshot()
    initial_snapshot = initial_belief.scalar_snapshot()
    initial_distribution = classification_distribution(initial_snapshot)
    initial_uncertainty = _posterior_uncertainty_stats(initial_posterior)

    scored_contexts: dict[str, list[float]] = {}
    for question_id, node in nodes.items():
        if not node.choices:
            continue
        context = _selector_context(node)
        context_counts[context] += 1
        if node.discriminates or node.information_gain_hint is not None or node.target_context is not None:
            selector_metadata_counts[context] += 1
        else:
            missing_metadata_by_context[context] += 1
        score = score_question(question_id, nodes, set(), initial_posterior, initial_snapshot)
        scored_contexts.setdefault(context, []).append(score.information_gain)

    missing_contexts = sorted(set(TRAIT_BY_CONTEXT) - set(context_counts) - {"final"})
    if missing_contexts:
        issues.append("No selectable questions for selector contexts: " + ", ".join(missing_contexts))

    for context, count in context_counts.items():
        metadata_ratio = selector_metadata_counts[context] / max(1, count)
        if metadata_ratio < 0.25:
            warnings.append(
                f"Low selector metadata coverage for context '{context}' ({metadata_ratio:.0%}); "
                "question choice may depend too heavily on semantic tag heuristics."
            )

    avg_initial_entropy = _classification_entropy(initial_distribution)
    if avg_initial_entropy < 0.55:
        warnings.append("Initial classification distribution has low entropy; prior may be overconfident.")
    if initial_uncertainty["avg"] < 0.20:
        warnings.append("Initial posterior uncertainty is low; active questioning may have weak epistemic motivation.")

    avg_context_information_gain = {
        context: round(sum(values) / max(1, len(values)), 4)
        for context, values in sorted(scored_contexts.items())
    }
    low_gain_contexts = [context for context, gain in avg_context_information_gain.items() if gain < 0.20 and context != "final"]
    if low_gain_contexts:
        warnings.append("Low initial information-gain contexts: " + ", ".join(low_gain_contexts))

    stats = {
        "initial_posterior_uncertainty": {
            "avg": round(initial_uncertainty["avg"], 4),
            "max": round(initial_uncertainty["max"], 4),
            "min": round(initial_uncertainty["min"], 4),
            "highest_trait": initial_uncertainty["highest_trait"],
            "by_trait": {trait: round(value, 4) for trait, value in initial_uncertainty["by_trait"].items()},
        },
        "initial_classification_distribution": {
            label: round(probability, 4)
            for label, probability in initial_distribution.items()
        },
        "initial_classification_entropy": round(avg_initial_entropy, 4),
        "selector_context_counts": dict(context_counts),
        "selector_metadata_counts": dict(selector_metadata_counts),
        "missing_selector_metadata_by_context": dict(missing_metadata_by_context),
        "avg_initial_information_gain_by_context": avg_context_information_gain,
    }
    return AuditResult(issues, warnings, stats)


def manual_reauthoring_targets(nodes: dict[str, QuestionNode]) -> list[dict[str, Any]]:
    targets: list[dict[str, Any]] = []
    for node_id, reason in MANUAL_REAUTHORING_TARGETS.items():
        node = nodes.get(node_id)
        if node is None:
            continue
        targets.append({
            "node_id": node.id,
            "ai_line": node.ai_line,
            "reason": reason,
            "player_choices": [
                {
                    "text": choice.text,
                    "trust_delta": choice.trust_delta,
                    "suspicion_delta": choice.suspicion_delta,
                    "instability_delta": choice.instability_delta,
                }
                for choice in node.choices
            ],
        })
    return targets


def audit_training_jsonl(jsonl_path: Path) -> AuditResult:
    issues: list[str] = []
    warnings: list[str] = []

    if not jsonl_path.exists():
        return AuditResult([f"Training data not found: {jsonl_path}"], [], {"path": str(jsonl_path)})

    episodes = 0
    turn_count = 0
    node_counts: Counter[str] = Counter()
    intent_counts: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()
    contradiction_steps = 0

    with jsonl_path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line=line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                issues.append(f"Invalid JSON at line {lineno}")
                continue

            episodes += 1
            for step in row.get("steps", []):
                turn_count += 1
                node_id = step.get("node_id")
                if node_id:
                    node_counts[node_id] += 1
                intent = step.get("intent")
                if intent:
                    intent_counts[intent] += 1
                for tag in step.get("semantic_tags", []):
                    tag_counts[tag] += 1
                if step.get("is_contradiction"):
                    contradiction_steps += 1

    if episodes == 0:
        issues.append("Training data file is empty or has no valid records")

    contradiction_rate = round(contradiction_steps / max(1, turn_count), 4)
    if contradiction_rate < 0.03:
        warnings.append("Very low contradiction rate in data; callback memory behavior may under-train")

    stats = {
        "path": str(jsonl_path),
        "episodes": episodes,
        "turn_count": turn_count,
        "contradiction_rate": contradiction_rate,
        "top_nodes": node_counts.most_common(10),
        "top_intents": intent_counts.most_common(10),
        "top_tags": tag_counts.most_common(12),
    }
    return AuditResult(issues, warnings, stats)


def generate_reauthoring_recommendations(results: dict[str, AuditResult]) -> list[str]:
    recs: list[str] = []

    rep = results.get("Repetition")
    if rep and rep.stats.get("unique_player_options", 999) < 40:
        recs.append("Increase player choice variety on high-pressure nodes to reduce option repetition.")

    state = results.get("State Logic")
    if state and state.stats.get("avg_suspicion_delta", 0) > 0.03:
        recs.append("Lower baseline suspicion deltas on neutral/probing choices to slow escalation pacing.")

    reaction = results.get("Reaction Layer")
    if reaction and reaction.stats.get("missing_pool_count", 0) > 0:
        recs.append("Add reaction pools for any question contexts that are missing pool coverage.")

    active = results.get("Bayesian Active-Inference Plausibility")
    if active and active.stats.get("missing_selector_metadata_by_context"):
        recs.append("Add selector metadata for low-coverage contexts so expected-information-gain scoring is author-transparent.")

    train = results.get("Training Data")
    if train and train.stats.get("contradiction_rate", 1) < 0.03:
        recs.append("Generate more contradiction-heavy human playthroughs so callback lines get stronger examples.")

    playthrough = results.get("Playthrough Coverage")
    if playthrough and playthrough.stats.get("missing_ending_branches"):
        recs.append("Add structural ending branches for any missing intended emotional trajectories.")
    if playthrough and playthrough.stats.get("selector_high_uncertainty_ratio", 1) < 0.45:
        recs.append("Increase uncertainty/information-gain weighting if the selector is not probing high-uncertainty contexts.")

    if not recs:
        recs.append("No major structural weaknesses detected; focus next pass on line-level tone differentiation.")

    return recs


def to_markdown(
    results: dict[str, AuditResult],
    recommendations: list[str] | None = None,
    reauthoring_targets: list[dict[str, Any]] | None = None,
) -> str:
    lines = ["# Narrative Audit Report", ""]
    for name, result in results.items():
        lines.append(f"## {name}")
        if result.issues:
            lines.append("### Issues")
            lines.extend([f"- {i}" for i in result.issues])
        if result.warnings:
            lines.append("### Warnings")
            lines.extend([f"- {w}" for w in result.warnings])
        lines.append("### Stats")
        lines.append("```json")
        lines.append(json.dumps(result.stats, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")

    playthrough = results.get("Playthrough Coverage")
    if playthrough:
        ending_type_counts = playthrough.stats.get("ending_type_counts", {})
        missing_ending_branches = playthrough.stats.get("missing_ending_branches", [])
        lines.append("## Ending Coverage")
        lines.append("```json")
        lines.append(json.dumps(ending_type_counts, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
        lines.append("## Missing Ending Branches")
        if missing_ending_branches:
            lines.extend([f"- {branch}" for branch in missing_ending_branches])
        else:
            lines.append("- None")
        lines.append("")

    if reauthoring_targets:
        lines.append("## Manual Reauthoring Targets")
        for target in reauthoring_targets:
            lines.append(f"### {target['node_id']}")
            lines.append(f"- Reason: {target['reason']}")
            lines.append(f"- AI line: {target['ai_line']}")
            lines.append("- Player choices:")
            for choice in target["player_choices"]:
                lines.append(
                    f"  - {choice['text']} "
                    f"(trust={choice['trust_delta']}, suspicion={choice['suspicion_delta']}, instability={choice['instability_delta']})"
                )
            lines.append("")

    if recommendations:
        lines.append("## Re-authoring Recommendations")
        lines.extend([f"- {r}" for r in recommendations])
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit engine-style narrative flow, tone/state logic, and playthrough coverage.")
    parser.add_argument("--episodes", type=int, default=60)
    parser.add_argument("--max-turns", type=int, default=14)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--report", type=Path, default=Path("../audit_report.md"))
    parser.add_argument("--training-jsonl", type=Path, default=None)
    args = parser.parse_args()

    scene = _make_scene_for_graph()
    nodes = scene.question_nodes()

    results = {
        "Flow & Reachability": audit_structure(nodes),
        "Repetition": audit_repetition(nodes),
        "State Logic": audit_state_logic(nodes),
        "Reaction Layer": audit_reaction_layer(nodes),
        "Bayesian Active-Inference Plausibility": audit_active_inference_plausibility(nodes),
        "Playthrough Coverage": audit_playthroughs(nodes, args.episodes, args.max_turns, args.seed),
    }

    if args.training_jsonl:
        results["Training Data"] = audit_training_jsonl(args.training_jsonl)

    recommendations = generate_reauthoring_recommendations(results)
    md = to_markdown(results, recommendations, manual_reauthoring_targets(nodes))
    args.report.write_text(md, encoding="utf-8")
    print(f"Wrote audit report to {args.report}")


if __name__ == "__main__":
    main()
