from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from terminal_theme import classification as colour_classification
from terminal_theme import heat_percent, heading, section


TRAIT_KEYS = ("compliance", "loyalty", "deception", "risk", "empathy")


@dataclass(slots=True)
class LatentBelief:
    """Posterior-style belief for one citizen trait."""

    mean: float
    uncertainty: float

    @property
    def confidence(self) -> float:
        return 1.0 - self.uncertainty

    def snapshot(self) -> dict[str, float]:
        return {
            "mean": self.mean,
            "uncertainty": self.uncertainty,
            "confidence": self.confidence,
        }


@dataclass(slots=True)
class CitizenBeliefState:
    compliance: LatentBelief
    loyalty: LatentBelief
    deception: LatentBelief
    risk: LatentBelief
    empathy: LatentBelief

    @classmethod
    def default(cls) -> "CitizenBeliefState":
        return cls(
            compliance=LatentBelief(0.50, 0.35),
            loyalty=LatentBelief(0.50, 0.35),
            deception=LatentBelief(0.20, 0.45),
            risk=LatentBelief(0.35, 0.40),
            empathy=LatentBelief(0.50, 0.35),
        )

    def scalar_snapshot(self) -> dict[str, float]:
        return {key: getattr(self, key).mean for key in TRAIT_KEYS}

    def posterior_snapshot(self) -> dict[str, dict[str, float]]:
        return {key: getattr(self, key).snapshot() for key in TRAIT_KEYS}


class CitizenBeliefModel:
    """Bayesian-style citizen profile updated from authored choice metadata."""

    def __init__(self, state: CitizenBeliefState | None = None) -> None:
        self.state = state or CitizenBeliefState.default()

    @classmethod
    def default(cls) -> "CitizenBeliefModel":
        return cls()

    @property
    def compliance(self) -> float:
        return self.state.compliance.mean

    @property
    def loyalty(self) -> float:
        return self.state.loyalty.mean

    @property
    def deception(self) -> float:
        return self.state.deception.mean

    @property
    def risk(self) -> float:
        return self.state.risk.mean

    @property
    def empathy(self) -> float:
        return self.state.empathy.mean

    def scalar_snapshot(self) -> dict[str, float]:
        return self.state.scalar_snapshot()

    def posterior_snapshot(self) -> dict[str, dict[str, float]]:
        return self.state.posterior_snapshot()

    def update_from_choice(self, choice: Any, clamp01) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]]:
        before = self.posterior_snapshot()
        updates = self._choice_updates(choice)
        evidence = self._evidence_strength(choice)

        for key, delta in updates.items():
            belief = getattr(self.state, key)
            belief.mean = clamp01(belief.mean + delta)
            belief.uncertainty = self._updated_uncertainty(belief.uncertainty, delta, evidence, clamp01)

        return before, self.posterior_snapshot()

    def apply_claim_update(
        self,
        claim_update: Any,
        case_file: Any,
        clamp01,
    ) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]] | None:
        if not claim_update.has_updates():
            return None

        before = self.posterior_snapshot()
        contradiction_count = len(claim_update.contradictions)
        fact_conflict_count = len(claim_update.fact_conflicts)
        exposed_sensitivity = sum(case_file.fact(key).sensitivity for key in claim_update.exposed_facts)
        protected_sensitivity = sum(case_file.fact(key).sensitivity for key in claim_update.protected_facts)
        has_consistent_partial = bool(claim_update.new_claims) and not (
            claim_update.contradictions or claim_update.fact_conflicts
        )
        has_consistent_partial = has_consistent_partial and any(
            claim.claimed_value not in {"true", "false"}
            for claim in claim_update.new_claims
        )

        deception_delta = 0.005 * contradiction_count + 0.003 * fact_conflict_count
        deception_delta += 0.0005 * protected_sensitivity
        if has_consistent_partial:
            deception_delta -= 0.010

        risk_delta = 0.006 * exposed_sensitivity

        deception = self.state.deception
        risk = self.state.risk
        deception.mean = clamp01(deception.mean + deception_delta)
        risk.mean = clamp01(risk.mean + risk_delta)

        uncertainty_delta = 0.006 * fact_conflict_count + 0.0015 * protected_sensitivity
        if contradiction_count:
            uncertainty_delta += 0.004 * contradiction_count
        deception.uncertainty = clamp01(max(0.04, deception.uncertainty + uncertainty_delta))
        if exposed_sensitivity:
            risk.uncertainty = clamp01(max(0.04, risk.uncertainty + 0.002 * exposed_sensitivity))

        return before, self.posterior_snapshot()

    def _updated_uncertainty(self, uncertainty: float, delta: float, evidence: float, clamp01) -> float:
        reduction = 0.025 + 0.10 * evidence + min(abs(delta), 0.16) * 0.35
        if abs(delta) < 0.015:
            reduction *= 0.45
        return clamp01(max(0.04, uncertainty - reduction))

    def _evidence_strength(self, choice: Any) -> float:
        tags = set(choice.semantic_tags)
        evidence = 0.20
        evidence += 0.25 * choice.honesty
        evidence += 0.12 * choice.vulnerability
        evidence += 0.10 * choice.aggression
        evidence += 0.08 * choice.defensiveness
        if "full_admission" in tags:
            evidence += 0.25
        if "partial_admission" in tags:
            evidence += 0.14
        if {"denial", "deflection", "deception"} & tags:
            evidence -= 0.08
        return max(0.0, min(1.0, evidence))

    def _choice_updates(self, choice: Any) -> dict[str, float]:
        tags = set(choice.semantic_tags)
        compliance = 0.04 * choice.honesty - 0.05 * choice.defensiveness - 0.05 * choice.aggression
        loyalty = 0.04 * choice.honesty - 0.04 * choice.aggression
        deception = 0.05 * choice.defensiveness - 0.04 * choice.honesty
        risk = 0.04 * choice.defensiveness + 0.06 * choice.aggression
        has_risk_signal = bool({"dissident_risk", "challenge", "counterattack", "refusal"} & tags)
        has_empathy_signal = "empathy" in tags
        has_reform_signal = bool(
            "reform" in getattr(choice, "intent", "")
            or {"loyalty_conflict", "fear"} & tags
        )
        has_plain_authority_signal = bool({"compliance", "loyalty", "authority"} & tags) and not (
            has_empathy_signal or has_reform_signal
        )

        empathy = -0.02 * choice.aggression
        if has_empathy_signal:
            if has_risk_signal:
                empathy += 0.04 + 0.025 * choice.vulnerability
            else:
                empathy += 0.06 + 0.025 * choice.vulnerability
        elif has_reform_signal:
            empathy += 0.035 + 0.02 * choice.vulnerability
        else:
            empathy += 0.006 * choice.vulnerability

        if has_plain_authority_signal:
            empathy -= 0.02
        if {"deception", "deflection", "denial"} & tags and not has_empathy_signal:
            empathy -= 0.02
        if {"self_protection", "caution"} & tags and not (has_empathy_signal or has_reform_signal):
            empathy -= 0.008

        if "compliance" in tags:
            compliance += 0.09
            loyalty += 0.07
            risk -= 0.06
        if {"loyalty", "authority"} & tags:
            loyalty += 0.06
        if {"deception", "deflection", "denial"} & tags:
            deception += 0.16
            risk += 0.01
            compliance -= 0.02
        if {"dissident_risk", "challenge", "counterattack"} & tags:
            risk += 0.13
            loyalty -= 0.06
            compliance -= 0.07
        if "refusal" in tags:
            risk += 0.08
            compliance -= 0.06
        if "empathy" in tags:
            if has_risk_signal:
                loyalty -= 0.02
            else:
                compliance += 0.02
                risk -= 0.03
        if "full_admission" in tags:
            deception -= 0.09
            risk += 0.06 if has_risk_signal else 0.01
        if "partial_admission" in tags:
            deception -= 0.04
            if has_risk_signal:
                risk += 0.03
            elif {"boundary", "caution", "empathy"} & tags:
                compliance += 0.02

        return {
            "compliance": compliance,
            "loyalty": loyalty,
            "deception": deception,
            "risk": risk,
            "empathy": empathy,
        }


def apply_choice_to_hearing_ai_state(hearing_ai: Any, choice: Any, clamp01) -> None:
    """Apply authored choice metadata to the scene-level Hearing AI affect state."""

    nudge_hearing_ai_state(hearing_ai, clamp01, choice.trust_delta, choice.suspicion_delta, choice.instability_delta)
    tags = set(choice.semantic_tags)
    trust = 0.05 * choice.honesty + 0.03 * choice.vulnerability - 0.04 * choice.defensiveness
    suspicion = 0.05 * choice.defensiveness + 0.06 * choice.aggression - 0.04 * choice.honesty
    instability = 0.08 * choice.destabilisation + 0.02 * choice.vulnerability
    if {"deception", "deflection", "denial"} & tags:
        suspicion += 0.06
    if {"dissident_risk", "counterattack", "refusal"} & tags:
        suspicion += 0.05
    if "compliance" in tags:
        trust += 0.05
        suspicion -= 0.04
    if "empathy" in tags and not ({"dissident_risk", "challenge", "refusal", "deception"} & tags):
        trust += 0.02
        suspicion -= 0.03
    nudge_hearing_ai_state(hearing_ai, clamp01, trust, suspicion, instability)


def nudge_hearing_ai_state(hearing_ai: Any, clamp01, trust: float = 0.0, suspicion: float = 0.0, instability: float = 0.0) -> None:
    hearing_ai.trust = clamp01(hearing_ai.trust + trust)
    hearing_ai.suspicion = clamp01(hearing_ai.suspicion + suspicion)
    hearing_ai.instability = clamp01(hearing_ai.instability + instability)


def observation_from_choice(choice: Any, question: Any, engram: Any, Observation: Any, clamp01) -> Any:
    """Convert authored choice metadata into the Observation consumed by JPC/TF."""

    tags = set(choice.semantic_tags)
    strength = 0.30
    reliability = 0.50
    if "compliance" in tags:
        strength -= 0.10
        reliability += 0.08
    if "dissident_risk" in tags:
        strength += 0.28
        reliability += 0.12
    if {"deception", "deflection", "denial"} & tags:
        strength += 0.18
        reliability -= 0.08
    if "full_admission" in tags:
        strength += 0.22
        reliability += 0.12
    if "partial_admission" in tags:
        strength += 0.12
        reliability += 0.06
    if "empathy" in tags:
        if {"dissident_risk", "challenge", "refusal"} & tags:
            strength += 0.08
        else:
            strength += 0.02
            reliability += 0.04
    strength += 0.15 * choice.aggression + 0.10 * choice.defensiveness + 0.08 * choice.vulnerability
    reliability += 0.18 * choice.honesty - 0.12 * choice.defensiveness
    return Observation(
        engram.id,
        clamp01(strength),
        clamp01(reliability),
        f"question={question.id}; choice={choice.intent}: {', '.join(choice.semantic_tags)}",
    )


def percent(value: float, clamp01, *, color: bool | None = False) -> str:
    if color:
        return heat_percent(value, clamp01, enabled=color)
    return f"{round(100 * clamp01(value)):3d}%"


def model_update_text(
    last_model_update: tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]] | None,
    classification: str,
    confidence: float,
    distribution: dict[str, float],
    flags: list[str] | None,
    clamp01,
    color: bool | None = False,
) -> str:
    if last_model_update is None:
        return ""
    before, after = last_model_update
    rows = ["", heading("MODEL UPDATE", enabled=color), "------------"]
    for key in TRAIT_KEYS:
        before_trait = before[key]
        after_trait = after[key]
        rows.append(
            f"{key.upper().ljust(10)} "
            f"{percent(before_trait['mean'], clamp01, color=color)} +/- {percent(before_trait['uncertainty'], clamp01, color=color)} "
            f"-> {percent(after_trait['mean'], clamp01, color=color)} +/- {percent(after_trait['uncertainty'], clamp01, color=color)}"
        )
    rows += [
        "",
        section("CURRENT CLASSIFICATION", enabled=color),
        "----------------------",
        colour_classification(classification, enabled=color),
        f"CONFIDENCE {percent(confidence, clamp01, color=color)}",
    ]
    rows.append("FLAGS " + (", ".join(flags) if flags else "NONE"))
    rows.append(
        "P("
        + ", ".join(f"{label}={percent(probability, clamp01, color=color).strip()}" for label, probability in distribution.items())
        + ")"
    )
    return "\n".join(rows)
