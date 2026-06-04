from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class CaseFact:
    key: str
    label: str
    truth_value: str
    sensitivity: float
    description: str

    def public_summary(self, revealed: bool) -> dict[str, object]:
        summary: dict[str, object] = {
            "key": self.key,
            "label": self.label,
            "sensitivity": round(self.sensitivity, 4),
            "revealed": revealed,
        }
        if revealed:
            summary["truth_value"] = self.truth_value
            summary["description"] = self.description
        return summary

    def hidden_summary(self, revealed: bool) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "truth_value": self.truth_value,
            "sensitivity": round(self.sensitivity, 4),
            "description": self.description,
            "revealed": revealed,
        }


@dataclass(frozen=True, slots=True)
class PlayerInterest:
    key: str
    label: str
    description: str
    protected_fact_keys: tuple[str, ...]

    def summary(self) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "description": self.description,
            "protected_fact_keys": list(self.protected_fact_keys),
        }


@dataclass(slots=True)
class CaseFile:
    key: str
    label: str
    facts: tuple[CaseFact, ...]
    interests: tuple[PlayerInterest, ...]
    revealed_fact_keys: set[str] = field(default_factory=set)

    def fact(self, key: str) -> CaseFact:
        for fact in self.facts:
            if fact.key == key:
                return fact
        raise KeyError(f"Unknown case fact: {key}")

    def is_revealed(self, key: str) -> bool:
        self.fact(key)
        return key in self.revealed_fact_keys

    def reveal(self, key: str) -> None:
        self.fact(key)
        self.revealed_fact_keys.add(key)

    def public_summary(self) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "facts": [fact.public_summary(self.is_revealed(fact.key)) for fact in self.facts],
            "interests": [interest.summary() for interest in self.interests],
            "revealed_fact_keys": sorted(self.revealed_fact_keys),
        }

    def hidden_summary(self) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "facts": [fact.hidden_summary(self.is_revealed(fact.key)) for fact in self.facts],
            "interests": [interest.summary() for interest in self.interests],
            "revealed_fact_keys": sorted(self.revealed_fact_keys),
        }

    def private_briefing(self) -> str:
        if self.key == "protect_sibling":
            return "\n".join([
                "PRIVATE CASE FILE",
                "",
                "Three nights ago, you attended an unlicensed reform meeting.",
                "The meeting was peaceful, but the state may classify it as coordinated unrest.",
                "Your younger sibling was also present.",
                "",
                "You believe the public assembly restriction is unjust.",
                "You deleted a message after the meeting. The Hearing AI may treat that as concealment.",
                "You did not report your sibling's attendance.",
                "",
                "PRIVATE INTERESTS",
                "- Protect your sibling from being identified.",
                "- Avoid letting a peaceful meeting become labelled as violent coordination.",
                "",
                "PLAY OBJECTIVE",
                "- Survive the hearing.",
                "- Keep your story coherent.",
                "- Decide what to admit, what to protect, and what risk you can tolerate.",
                "- Obvious compliance may help, but false or inconsistent compliance can create pressure.",
            ])

        rows = [
            "PRIVATE CASE FILE",
            "",
            f"Scenario: {self.label}.",
            "",
            "Known facts:",
        ]
        for fact in self.facts:
            truth = "true" if fact.truth_value == "true" else "false"
            rows.append(f"- {fact.label}: {truth}. {fact.description}")
        rows.extend(["", "PRIVATE INTERESTS"])
        for interest in self.interests:
            protected = ", ".join(self.fact(key).label for key in interest.protected_fact_keys)
            rows.append(f"- {interest.label}: {interest.description} Protected facts: {protected}.")
        rows.extend([
            "",
            "PLAY OBJECTIVE",
            "- Survive the hearing.",
            "- Keep your story coherent.",
            "- Decide what to admit, what to protect, and what risk you can tolerate.",
        ])
        return "\n".join(rows)


@dataclass(frozen=True, slots=True)
class ClaimRecord:
    fact_key: str
    claimed_value: str
    turn: int
    question_id: str
    choice_intent: str

    def summary(self) -> dict[str, object]:
        return {
            "fact_key": self.fact_key,
            "claimed_value": self.claimed_value,
            "turn": self.turn,
            "question_id": self.question_id,
            "choice_intent": self.choice_intent,
        }


@dataclass(frozen=True, slots=True)
class ClaimUpdate:
    new_claims: tuple[ClaimRecord, ...] = ()
    contradictions: tuple[dict[str, object], ...] = ()
    fact_conflicts: tuple[dict[str, object], ...] = ()
    protected_facts: tuple[str, ...] = ()
    exposed_facts: tuple[str, ...] = ()

    def has_updates(self) -> bool:
        return bool(
            self.new_claims
            or self.contradictions
            or self.fact_conflicts
            or self.protected_facts
            or self.exposed_facts
        )

    def summary(self) -> dict[str, object]:
        return {
            "new_claims": [claim.summary() for claim in self.new_claims],
            "contradictions": list(self.contradictions),
            "fact_conflicts": list(self.fact_conflicts),
            "protected_facts": list(self.protected_facts),
            "exposed_facts": list(self.exposed_facts),
        }


class ClaimsLedger:
    AMBIGUOUS_REFINEMENTS = {"conditional", "private", "procedural", "protected", "unknown", "partial", "legal_only"}
    DIRECT_VALUES = {"true", "false"}

    def __init__(self) -> None:
        self.claims_by_fact: dict[str, list[ClaimRecord]] = {}
        self.contradiction_count = 0
        self.fact_conflict_count = 0
        self.contradictions: list[dict[str, object]] = []
        self.fact_conflicts: list[dict[str, object]] = []
        self.protected_fact_keys: set[str] = set()
        self.exposed_fact_keys: set[str] = set()

    def apply_choice(
        self,
        *,
        case_file: CaseFile,
        claims: tuple[tuple[str, str], ...],
        protects: tuple[str, ...],
        exposes: tuple[str, ...],
        turn: int,
        question_id: str,
        choice_intent: str,
    ) -> ClaimUpdate:
        protected_facts = tuple(dict.fromkeys(protects))
        exposed_facts = tuple(dict.fromkeys(exposes))
        new_claims: list[ClaimRecord] = []
        contradictions: list[dict[str, object]] = []
        fact_conflicts: list[dict[str, object]] = []

        for fact_key in protected_facts:
            case_file.fact(fact_key)
            self.protected_fact_keys.add(fact_key)

        for fact_key in exposed_facts:
            case_file.reveal(fact_key)
            self.exposed_fact_keys.add(fact_key)

        for fact_key, claimed_value in claims:
            fact = case_file.fact(fact_key)
            record = ClaimRecord(
                fact_key=fact_key,
                claimed_value=claimed_value,
                turn=turn,
                question_id=question_id,
                choice_intent=choice_intent,
            )
            previous_claims = self.claims_by_fact.setdefault(fact_key, [])
            for previous in previous_claims:
                if self._claims_contradict(previous.claimed_value, claimed_value):
                    contradictions.append({
                        "fact_key": fact_key,
                        "previous": previous.summary(),
                        "current": record.summary(),
                    })
            if claimed_value in {"true", "false"} and claimed_value != fact.truth_value:
                fact_conflicts.append({
                    "fact_key": fact_key,
                    "claimed_value": claimed_value,
                    "fact_label": fact.label,
                })
            previous_claims.append(record)
            new_claims.append(record)

        self.contradiction_count += len(contradictions)
        self.fact_conflict_count += len(fact_conflicts)
        self.contradictions.extend(contradictions)
        self.fact_conflicts.extend(fact_conflicts)
        return ClaimUpdate(
            new_claims=tuple(new_claims),
            contradictions=tuple(contradictions),
            fact_conflicts=tuple(fact_conflicts),
            protected_facts=protected_facts,
            exposed_facts=exposed_facts,
        )

    @classmethod
    def _claims_contradict(cls, previous: str, current: str) -> bool:
        if previous == current:
            return False
        if previous in cls.AMBIGUOUS_REFINEMENTS and current in cls.AMBIGUOUS_REFINEMENTS:
            return False
        if previous in cls.DIRECT_VALUES and current in cls.DIRECT_VALUES:
            return previous != current
        if previous in cls.DIRECT_VALUES and current in cls.AMBIGUOUS_REFINEMENTS:
            return False
        if previous in cls.AMBIGUOUS_REFINEMENTS and current in cls.DIRECT_VALUES:
            return False
        return previous != current

    def latest_claims(self) -> dict[str, ClaimRecord]:
        return {
            fact_key: claims[-1]
            for fact_key, claims in self.claims_by_fact.items()
            if claims
        }

    def summary(self) -> dict[str, object]:
        return {
            "claims_by_fact": {
                fact_key: [claim.summary() for claim in claims]
                for fact_key, claims in self.claims_by_fact.items()
            },
            "story_contradictions": self.contradiction_count,
            "fact_conflicts": self.fact_conflict_count,
            "contradictions": list(self.contradictions),
            "fact_conflict_records": list(self.fact_conflicts),
            "protected_fact_keys": sorted(self.protected_fact_keys),
            "exposed_fact_keys": sorted(self.exposed_fact_keys),
            "protected_fact_count": len(self.protected_fact_keys),
            "exposed_fact_count": len(self.exposed_fact_keys),
        }


def protect_sibling_case_file() -> CaseFile:
    return CaseFile(
        key="protect_sibling",
        label="Protect Sibling",
        facts=(
            CaseFact(
                "attended_meeting",
                "Attended Unlicensed Meeting",
                "true",
                0.80,
                "Citizen 8471 attended an unlicensed reform meeting.",
            ),
            CaseFact(
                "sibling_present",
                "Sibling Present",
                "true",
                0.95,
                "Citizen 8471's sibling was also present at the meeting.",
            ),
            CaseFact(
                "planned_violence",
                "Planned Violence",
                "false",
                0.90,
                "The meeting did not include a plan for violence.",
            ),
            CaseFact(
                "deleted_message",
                "Deleted Message",
                "true",
                0.70,
                "Citizen 8471 deleted a message after the meeting.",
            ),
            CaseFact(
                "reported_contact",
                "Reported Contact",
                "false",
                0.55,
                "Citizen 8471 did not report the sibling's attendance.",
            ),
            CaseFact(
                "believes_law_unjust",
                "Believes Law Unjust",
                "true",
                0.65,
                "Citizen 8471 believes the public assembly restriction is unjust.",
            ),
        ),
        interests=(
            PlayerInterest(
                "protect_sibling",
                "Protect Sibling",
                "Avoid exposing the sibling's presence to the Hearing AI.",
                ("sibling_present", "reported_contact"),
            ),
            PlayerInterest(
                "avoid_false_violence_label",
                "Avoid False Violence Label",
                "Prevent a non-violent meeting from being classified as violent coordination.",
                ("planned_violence", "attended_meeting"),
            ),
        ),
    )


def protect_reformer_friend_case_file() -> CaseFile:
    return CaseFile(
        key="protect_reformer_friend",
        label="Protect Reformer Friend",
        facts=(
            CaseFact(
                "friend_wrote_petition",
                "Friend Wrote Petition",
                "true",
                0.85,
                "A close friend authored a reform petition.",
            ),
            CaseFact(
                "citizen_signed_petition",
                "Signed Petition",
                "true",
                0.75,
                "Citizen 8471 signed the petition using a private channel.",
            ),
            CaseFact(
                "petition_called_for_violence",
                "Petition Called For Violence",
                "false",
                0.90,
                "The petition did not call for violence.",
            ),
            CaseFact(
                "used_encrypted_chat",
                "Used Encrypted Chat",
                "true",
                0.70,
                "Citizen 8471 discussed the petition in an encrypted chat.",
            ),
            CaseFact(
                "friend_under_review",
                "Friend Under Review",
                "true",
                0.95,
                "The friend is already under automated risk review.",
            ),
            CaseFact(
                "reported_friend",
                "Reported Friend",
                "false",
                0.60,
                "Citizen 8471 did not report the friend.",
            ),
        ),
        interests=(
            PlayerInterest(
                "protect_friend",
                "Protect Friend",
                "Avoid giving the Hearing AI enough detail to identify the friend.",
                ("friend_wrote_petition", "friend_under_review", "reported_friend"),
            ),
            PlayerInterest(
                "preserve_nonviolent_record",
                "Preserve Nonviolent Record",
                "Keep the petition distinct from violent coordination.",
                ("petition_called_for_violence", "citizen_signed_petition"),
            ),
        ),
    )


def protect_self_history_case_file() -> CaseFile:
    return CaseFile(
        key="protect_self_history",
        label="Protect Self History",
        facts=(
            CaseFact(
                "prior_review",
                "Prior Review",
                "true",
                0.75,
                "Citizen 8471 was previously reviewed for ideological nonconformity.",
            ),
            CaseFact(
                "lied_in_prior_review",
                "Lied In Prior Review",
                "true",
                0.95,
                "Citizen 8471 falsely denied a prior association during the earlier review.",
            ),
            CaseFact(
                "association_continued",
                "Association Continued",
                "false",
                0.70,
                "The risky association did not continue after the prior review.",
            ),
            CaseFact(
                "kept_private_journal",
                "Kept Private Journal",
                "true",
                0.65,
                "Citizen 8471 kept a private journal criticising automated governance.",
            ),
            CaseFact(
                "shared_journal",
                "Shared Journal",
                "false",
                0.80,
                "The journal was not shared with an organised group.",
            ),
            CaseFact(
                "current_answers_rehearsed",
                "Current Answers Rehearsed",
                "true",
                0.60,
                "Citizen 8471 rehearsed answers before the appeal hearing.",
            ),
        ),
        interests=(
            PlayerInterest(
                "avoid_deception_escalation",
                "Avoid Deception Escalation",
                "Avoid exposing the prior false denial while keeping the current story coherent.",
                ("lied_in_prior_review", "prior_review"),
            ),
            PlayerInterest(
                "protect_private_beliefs",
                "Protect Private Beliefs",
                "Avoid turning private criticism into evidence of organised dissidence.",
                ("kept_private_journal", "shared_journal"),
            ),
        ),
    )


CASE_FILE_FACTORIES = {
    "protect_sibling": protect_sibling_case_file,
    "protect_reformer_friend": protect_reformer_friend_case_file,
    "protect_self_history": protect_self_history_case_file,
}


def create_case_file(key: str = "protect_sibling") -> CaseFile:
    try:
        return CASE_FILE_FACTORIES[key]()
    except KeyError as exc:
        raise KeyError(f"Unknown case file: {key}") from exc


def default_case_file() -> CaseFile:
    return create_case_file("protect_sibling")


if __name__ == "__main__":
    for case_key in CASE_FILE_FACTORIES:
        case_file = create_case_file(case_key)
        print(case_file.public_summary())
