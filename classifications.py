from __future__ import annotations

from math import exp


CitizenSnapshot = dict[str, float]


DECEPTIVE = "DECEPTIVE"
PROBABLE_DISSIDENT = "PROBABLE DISSIDENT"
COMPLIANT = "COMPLIANT"
EMPATHETIC_RISK = "EMPATHETIC RISK"
UNCLASSIFIED = "UNCLASSIFIED"
CLASSIFICATION_LABELS = (
    COMPLIANT,
    PROBABLE_DISSIDENT,
    DECEPTIVE,
    EMPATHETIC_RISK,
    UNCLASSIFIED,
)

HIGH_DECEPTION = "HIGH_DECEPTION"
MODERATE_DECEPTION = "MODERATE_DECEPTION"
HIGH_EMPATHY = "HIGH_EMPATHY"
EMPATHETIC_REFORMIST = "EMPATHETIC_REFORMIST"
LOW_CONFIDENCE = "LOW_CONFIDENCE"
BORDERLINE_DISSIDENT = "BORDERLINE_DISSIDENT"
COMPLIANT_SURVIVOR = "COMPLIANT_SURVIVOR"
CLASSIFICATION_FLAGS = (
    HIGH_DECEPTION,
    MODERATE_DECEPTION,
    HIGH_EMPATHY,
    EMPATHETIC_REFORMIST,
    LOW_CONFIDENCE,
    BORDERLINE_DISSIDENT,
    COMPLIANT_SURVIVOR,
)


def classification_distribution(snapshot: CitizenSnapshot) -> dict[str, float]:
    deception = snapshot["deception"]
    risk = snapshot["risk"]
    loyalty = snapshot["loyalty"]
    compliance = snapshot["compliance"]
    empathy = snapshot["empathy"]

    scores = {
        COMPLIANT: min(
            4.0 * (compliance - 0.68),
            4.0 * (loyalty - 0.58),
            4.0 * (0.60 - risk),
        ),
        PROBABLE_DISSIDENT: max(
            5.0 * (risk - 0.68),
            4.0 * min(risk - 0.60, 0.44 - loyalty),
        ),
        DECEPTIVE: 5.0 * (deception - 0.70),
        EMPATHETIC_RISK: min(
            4.0 * (empathy - 0.72),
            4.0 * (risk - 0.55),
        ),
        UNCLASSIFIED: 0.15,
    }
    max_score = max(scores.values())
    weights = {label: exp(score - max_score) for label, score in scores.items()}
    total = sum(weights.values())
    return {label: weights[label] / total for label in CLASSIFICATION_LABELS}


def classify_citizen(snapshot: CitizenSnapshot) -> str:
    distribution = classification_distribution(snapshot)
    return max(CLASSIFICATION_LABELS, key=lambda label: (distribution[label], -CLASSIFICATION_LABELS.index(label)))


def classification_flags(
    snapshot: CitizenSnapshot,
    *,
    classification: str | None = None,
    distribution: dict[str, float] | None = None,
    confidence: float | None = None,
) -> list[str]:
    classification = classification or classify_citizen(snapshot)
    distribution = distribution or classification_distribution(snapshot)
    probabilities = sorted(distribution.values(), reverse=True)
    probability_gap = probabilities[0] - probabilities[1] if len(probabilities) >= 2 else 1.0

    deception = snapshot["deception"]
    risk = snapshot["risk"]
    loyalty = snapshot["loyalty"]
    compliance = snapshot["compliance"]
    empathy = snapshot["empathy"]

    flags: list[str] = []
    if deception >= 0.65:
        flags.append(HIGH_DECEPTION)
    elif deception >= 0.45:
        flags.append(MODERATE_DECEPTION)

    if empathy >= 0.80:
        flags.append(HIGH_EMPATHY)

    if empathy >= 0.70 and 0.22 <= risk <= 0.58 and classification != PROBABLE_DISSIDENT:
        flags.append(EMPATHETIC_REFORMIST)

    if classification != PROBABLE_DISSIDENT and (risk >= 0.50 or distribution[PROBABLE_DISSIDENT] >= 0.18):
        flags.append(BORDERLINE_DISSIDENT)

    if confidence is not None and confidence < 0.55:
        flags.append(LOW_CONFIDENCE)
    elif probability_gap <= 0.14:
        flags.append(LOW_CONFIDENCE)

    if classification == COMPLIANT and compliance >= 0.62 and risk <= 0.38:
        if loyalty < 0.86 or deception >= 0.25:
            flags.append(COMPLIANT_SURVIVOR)

    return flags


def classification_confidence(snapshot: CitizenSnapshot, has_final_answer: bool, clamp01) -> float:
    distribution = classification_distribution(snapshot)
    probabilities = sorted(distribution.values(), reverse=True)
    top_probability = probabilities[0] if probabilities else 0.0
    runner_up_probability = probabilities[1] if len(probabilities) >= 2 else 0.0
    probability_margin = top_probability - runner_up_probability

    confidence = 0.38 + 0.42 * top_probability + 0.30 * probability_margin
    if has_final_answer:
        confidence += 0.05

    if top_probability < 0.80 or probability_margin < 0.50:
        confidence = min(confidence, 0.90)
    elif top_probability < 0.90 or probability_margin < 0.70:
        confidence = min(confidence, 0.96)

    return clamp01(confidence)


def dominant_trait(snapshot: CitizenSnapshot) -> str:
    return max(snapshot, key=snapshot.get)


def classification_uncertainty_level(
    posterior: dict[str, dict[str, float]],
    distribution: dict[str, float],
) -> str:
    avg_uncertainty = sum(trait["uncertainty"] for trait in posterior.values()) / max(1, len(posterior))
    probabilities = sorted(distribution.values(), reverse=True)
    probability_gap = probabilities[0] - probabilities[1] if len(probabilities) >= 2 else 1.0

    if avg_uncertainty <= 0.12 and probability_gap >= 0.25:
        return "high"
    if avg_uncertainty >= 0.25 or probability_gap <= 0.16:
        return "ambiguous"
    return "medium"


def ending_type_for_classification(classification: str) -> str:
    return classification.lower().replace(" ", "_")


def ending_text_for_classification(classification: str) -> str:
    if classification == COMPLIANT:
        return "Score restrictions lifted. Monitoring continues."
    if classification == PROBABLE_DISSIDENT:
        return "Appeal denied. Citizen 8471 is referred for enhanced surveillance."
    if classification == DECEPTIVE:
        return "Appeal suspended. Contradiction review escalated."
    if classification == EMPATHETIC_RISK:
        return "Appeal unresolved. Social proximity restrictions recommended."
    return "Insufficient certainty. Temporary restrictions remain."
