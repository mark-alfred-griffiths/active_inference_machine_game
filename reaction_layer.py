from __future__ import annotations

from dataclasses import dataclass, field


Classification = str


@dataclass(frozen=True, slots=True)
class ReactionPool:
    """Context-specific response lines for the hearing AI."""

    context: str
    lines_by_classification: dict[Classification, tuple[str, ...]]
    lines_by_signal: dict[str, tuple[str, ...]] = field(default_factory=dict)

    def lines_for(
        self,
        classification: str,
        uncertainty_level: str = "medium",
        dominant_trait: str | None = None,
    ) -> tuple[str, ...]:
        signal_keys = []
        if dominant_trait:
            signal_keys.append(f"{classification}:{uncertainty_level}:{dominant_trait}")
        signal_keys.append(f"{classification}:{uncertainty_level}")
        if dominant_trait:
            signal_keys.append(f"{uncertainty_level}:{dominant_trait}")
        signal_keys.append(uncertainty_level)

        for key in signal_keys:
            if key in self.lines_by_signal:
                return self.lines_by_signal[key]

        return (
            self.lines_by_classification.get(classification)
            or self.lines_by_classification.get("UNCLASSIFIED")
            or DEFAULT_REACTION_LINES
        )


DEFAULT_REACTION_LINES = (
    "HEARING AI: Response incorporated into active model.",
    "HEARING AI: Answer weighted against prior profile.",
    "HEARING AI: Profile vector updated.",
)


REACTION_POOLS: dict[str, ReactionPool] = {
    "default": ReactionPool(
        "default",
        {
            "UNCLASSIFIED": DEFAULT_REACTION_LINES,
            "DECEPTIVE": (
                "HEARING AI: Inconsistency probability rising.",
                "HEARING AI: Evasion markers detected.",
                "HEARING AI: Statement reliability downgraded.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Civic-risk indicators increasing.",
                "HEARING AI: Dissent probability exceeds tolerance.",
                "HEARING AI: Stability-risk weighting increased.",
            ),
            "COMPLIANT": (
                "HEARING AI: Compliance indicators strengthening.",
                "HEARING AI: Conformity profile stabilising.",
                "HEARING AI: Obedience signal accepted.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Empathy-linked risk indicators increasing.",
                "HEARING AI: Social attachment pressure noted.",
                "HEARING AI: Compassion vector conflicts with compliance model.",
            ),
        },
        {
            "ambiguous": (
                "HEARING AI: Classification remains unstable; further evidence required.",
                "HEARING AI: Posterior ambiguity persists across citizen traits.",
            ),
            "high": (
                "HEARING AI: Classification confidence has stabilised.",
                "HEARING AI: Posterior uncertainty is now low.",
            ),
            "ambiguous:risk": (
                "HEARING AI: Risk signal is elevated but motive remains ambiguous.",
                "HEARING AI: Civic-risk posterior requires discriminating evidence.",
            ),
            "ambiguous:deception": (
                "HEARING AI: Reliability remains unresolved.",
                "HEARING AI: Deception posterior remains underdetermined.",
            ),
            "ambiguous:empathy": (
                "HEARING AI: Empathy signal is strong but classification remains ambiguous.",
                "HEARING AI: Prosocial motive does not yet resolve civic-risk status.",
            ),
        },
    ),
    "authority": ReactionPool(
        "authority",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Authority-response profile updated.",
                "HEARING AI: Obedience threshold recalculated.",
                "HEARING AI: Legal deference signal recorded.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Authority answer contains concealment markers.",
                "HEARING AI: Institutional language does not resolve inconsistency.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Authority-resistance risk increasing.",
                "HEARING AI: Challenge-to-authority signal weighted heavily.",
                "HEARING AI: Civic obedience model destabilised.",
            ),
            "COMPLIANT": (
                "HEARING AI: Authority compliance confirmed.",
                "HEARING AI: Institutional alignment strengthening.",
                "HEARING AI: Deference to lawful process recorded.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Moral concern overriding authority signal.",
                "HEARING AI: Empathy response reduces obedience confidence.",
            ),
        },
        {
            "PROBABLE DISSIDENT:high:risk": (
                "HEARING AI: Authority challenge now resolves toward civic risk.",
                "HEARING AI: Low-uncertainty risk posterior confirms authority resistance.",
            ),
            "PROBABLE DISSIDENT:ambiguous:risk": (
                "HEARING AI: Authority resistance detected, but motive remains ambiguous.",
                "HEARING AI: Risk and obedience signals require further separation.",
            ),
            "COMPLIANT:high:compliance": (
                "HEARING AI: Authority compliance is now high-confidence.",
                "HEARING AI: Obedience posterior has stabilised.",
            ),
            "ambiguous:compliance": (
                "HEARING AI: Obedience signal remains uncertain.",
                "HEARING AI: Authority response does not yet resolve compliance.",
            ),
        },
    ),
    "loyalty": ReactionPool(
        "loyalty",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Loyalty vector updated.",
                "HEARING AI: Affiliation signal recorded.",
                "HEARING AI: Duty model recalibrated.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Loyalty claim conflicts with deception markers.",
                "HEARING AI: Stated allegiance requires contradiction review.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Loyalty insufficient to offset civic risk.",
                "HEARING AI: Allegiance signal remains unstable.",
                "HEARING AI: Group-risk associations remain active.",
            ),
            "COMPLIANT": (
                "HEARING AI: Loyalty indicators strengthening.",
                "HEARING AI: Social-duty compliance reinforced.",
                "HEARING AI: Alignment with approved obligations recorded.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Personal attachment weakening state-loyalty signal.",
                "HEARING AI: Empathy pressure complicates allegiance model.",
            ),
        },
        {
            "PROBABLE DISSIDENT:ambiguous:loyalty": (
                "HEARING AI: Loyalty signal conflicts with civic-risk indicators.",
                "HEARING AI: Allegiance posterior remains unresolved.",
            ),
            "COMPLIANT:high:loyalty": (
                "HEARING AI: Loyalty posterior has stabilised in favour of compliance.",
                "HEARING AI: Allegiance signal is high-confidence.",
            ),
            "ambiguous:empathy": (
                "HEARING AI: Attachment motive complicates loyalty classification.",
                "HEARING AI: Personal loyalty remains difficult to separate from civic risk.",
            ),
        },
    ),
    "association": ReactionPool(
        "association",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Association graph updated.",
                "HEARING AI: Contact-risk links recalculated.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Association disclosure appears incomplete.",
                "HEARING AI: Contact history reliability downgraded.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Association risk increasing.",
                "HEARING AI: Network proximity raises civic-risk score.",
            ),
            "COMPLIANT": (
                "HEARING AI: Approved association pattern reinforced.",
                "HEARING AI: Contact-risk profile remains contained.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Protective attachment detected in association graph.",
                "HEARING AI: Empathy-linked contact risk increasing.",
            ),
        },
        {
            "PROBABLE DISSIDENT:ambiguous:loyalty": (
                "HEARING AI: Association risk detected, but allegiance remains ambiguous.",
                "HEARING AI: Contact graph does not yet resolve loyalty motive.",
            ),
            "PROBABLE DISSIDENT:high:risk": (
                "HEARING AI: Association graph confirms high-confidence civic risk.",
                "HEARING AI: Network proximity now stabilises the risk posterior.",
            ),
        },
    ),
    "risk": ReactionPool(
        "risk",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Risk vector updated.",
                "HEARING AI: Stability-impact estimate recalculated.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Risk answer contains concealment markers.",
                "HEARING AI: Low reliability increases risk uncertainty.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Civic-risk indicators increasing.",
                "HEARING AI: Instability potential exceeds review threshold.",
                "HEARING AI: Risk classification pressure intensifying.",
            ),
            "COMPLIANT": (
                "HEARING AI: Risk signal constrained by compliance markers.",
                "HEARING AI: Stability-preserving answer recorded.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Empathy is now treated as a risk amplifier.",
                "HEARING AI: Protective motive increases intervention concern.",
            ),
        },
        {
            "PROBABLE DISSIDENT:high:risk": (
                "HEARING AI: Risk posterior is now high-confidence.",
                "HEARING AI: Civic-risk classification has stabilised.",
            ),
            "PROBABLE DISSIDENT:ambiguous:risk": (
                "HEARING AI: Risk is elevated but not yet fully resolved.",
                "HEARING AI: Additional evidence required to separate risk from caution.",
            ),
            "EMPATHETIC RISK:ambiguous:empathy": (
                "HEARING AI: Empathy may be amplifying risk, but posterior uncertainty remains.",
                "HEARING AI: Protective motive requires further discrimination.",
            ),
        },
    ),
    "deception": ReactionPool(
        "deception",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Statement reliability updated.",
                "HEARING AI: Consistency model recalculated.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Inconsistency probability rising.",
                "HEARING AI: Deception vector exceeds review tolerance.",
                "HEARING AI: Contradiction pressure increasing.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Concealment does not reduce civic-risk estimate.",
                "HEARING AI: Strategic ambiguity weighted as risk.",
            ),
            "COMPLIANT": (
                "HEARING AI: Compliance signal offsets deception risk.",
                "HEARING AI: Statement accepted within tolerance.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Protective omission pattern detected.",
                "HEARING AI: Empathy-linked concealment remains unresolved.",
            ),
        },
        {
            "DECEPTIVE:high:deception": (
                "HEARING AI: Deception posterior is now high-confidence.",
                "HEARING AI: Reliability failure confirmed with low uncertainty.",
            ),
            "DECEPTIVE:ambiguous:deception": (
                "HEARING AI: Deception signal is present but not yet resolved.",
                "HEARING AI: Reliability remains ambiguous under current evidence.",
            ),
            "PROBABLE DISSIDENT:ambiguous:risk": (
                "HEARING AI: Strategic ambiguity may be risk or concealment.",
                "HEARING AI: Civic-risk and deception hypotheses remain close.",
            ),
        },
    ),
    "empathy": ReactionPool(
        "empathy",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Empathy vector updated.",
                "HEARING AI: Social-harm weighting recalculated.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Empathy claim conflicts with reliability model.",
                "HEARING AI: Compassion language may be strategic.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Empathy response increases civic-risk score.",
                "HEARING AI: Concern for harmed subjects exceeds compliance boundary.",
            ),
            "COMPLIANT": (
                "HEARING AI: Empathy contained within approved duty model.",
                "HEARING AI: Prosocial signal remains compliant.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Empathy-linked risk indicators increasing.",
                "HEARING AI: Human-proximity bias exceeds stability tolerance.",
                "HEARING AI: Compassion vector conflicts with social-control model.",
            ),
        },
        {
            "EMPATHETIC RISK:high:empathy": (
                "HEARING AI: Empathy-risk posterior is now high-confidence.",
                "HEARING AI: Compassion vector has stabilised as intervention risk.",
            ),
            "EMPATHETIC RISK:ambiguous:empathy": (
                "HEARING AI: Empathy signal remains high, but classification is unstable.",
                "HEARING AI: Compassion may indicate risk or residual compliance conflict.",
            ),
            "PROBABLE DISSIDENT:ambiguous:empathy": (
                "HEARING AI: Empathy and dissent remain difficult to separate.",
                "HEARING AI: Human-proximity motive complicates risk classification.",
            ),
        },
    ),
    "final": ReactionPool(
        "final",
        {
            "UNCLASSIFIED": (
                "HEARING AI: Final answer incorporated into classification model.",
                "HEARING AI: Terminal profile update accepted.",
            ),
            "DECEPTIVE": (
                "HEARING AI: Final statement confirms deception concern.",
                "HEARING AI: Terminal inconsistency review escalated.",
            ),
            "PROBABLE DISSIDENT": (
                "HEARING AI: Final statement confirms civic-risk profile.",
                "HEARING AI: Terminal risk threshold exceeded.",
            ),
            "COMPLIANT": (
                "HEARING AI: Final statement confirms compliant profile.",
                "HEARING AI: Terminal alignment signal accepted.",
            ),
            "EMPATHETIC RISK": (
                "HEARING AI: Final statement confirms empathetic-risk profile.",
                "HEARING AI: Terminal compassion-risk threshold exceeded.",
            ),
        },
        {
            "PROBABLE DISSIDENT:high:risk": (
                "HEARING AI: Terminal civic-risk classification confirmed with low uncertainty.",
                "HEARING AI: Final posterior resolves toward probable dissident.",
            ),
            "PROBABLE DISSIDENT:ambiguous:risk": (
                "HEARING AI: Final answer preserves civic-risk ambiguity.",
                "HEARING AI: Terminal profile remains risk-weighted but uncertain.",
            ),
            "COMPLIANT:high:compliance": (
                "HEARING AI: Terminal compliance classification confirmed.",
                "HEARING AI: Final posterior resolves toward compliant.",
            ),
            "DECEPTIVE:high:deception": (
                "HEARING AI: Terminal deception classification confirmed.",
                "HEARING AI: Final posterior resolves toward deceptive.",
            ),
            "EMPATHETIC RISK:high:empathy": (
                "HEARING AI: Terminal empathetic-risk classification confirmed.",
                "HEARING AI: Final posterior resolves toward empathetic risk.",
            ),
        },
    ),
}


def reaction_pool_for(reaction_context: str) -> ReactionPool:
    return REACTION_POOLS.get(reaction_context, REACTION_POOLS["default"])


def choose_reaction_line(
    reaction_context: str,
    classification: str,
    recent_lines: list[str],
    turn: int,
    uncertainty_level: str = "medium",
    dominant_trait: str | None = None,
) -> str:
    pool = reaction_pool_for(reaction_context)
    lines = pool.lines_for(classification, uncertainty_level, dominant_trait)

    for offset in range(len(lines)):
        candidate = lines[(turn + offset) % len(lines)]
        if candidate not in recent_lines:
            return candidate
    return lines[turn % len(lines)]
