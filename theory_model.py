from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


@dataclass(slots=True)
class Theory:
    """A visible competing hypothesis the machine can build about the player."""

    key: str
    label: str
    probability: float
    focus: str


@dataclass(slots=True)
class TheoryModel:
    """
    Player-facing model layer.

    This does not replace the JPC/TensorFlow controller. It translates authored
    choice semantics into visible competing theories so the player can form a
    strategy against the machine instead of guessing at hidden variables.
    """

    theories: dict[str, Theory] = field(default_factory=dict)
    convergence_threshold: float = 0.82
    last_focus: str = "Attachment"

    @classmethod
    def default(cls) -> "TheoryModel":
        return cls(
            theories={
                "loved_x": Theory("loved_x", "You loved X", 0.20, "Attachment"),
                "pitied_x": Theory("pitied_x", "You pitied X", 0.35, "Responsibility"),
                "feared_x": Theory("feared_x", "You feared X", 0.15, "Fear"),
                "betrayed_x": Theory("betrayed_x", "You betrayed X", 0.10, "Betrayal"),
                "barely_knew_x": Theory("barely_knew_x", "You barely knew X", 0.20, "Contradictions"),
            },
            last_focus="Attachment",
        )

    def snapshot(self) -> dict[str, float]:
        return {key: theory.probability for key, theory in self.theories.items()}

    def leading_theory(self) -> Theory:
        return max(self.theories.values(), key=lambda theory: theory.probability)

    def confidence_band(self, key: str | None = None) -> str:
        value = self.theories[key].probability if key else self.leading_theory().probability
        if value >= 0.72:
            return "High"
        if value >= 0.50:
            return "Moderate"
        return "Low"

    def uncertainty(self, key: str) -> float:
        """Uncertainty is highest near 50%, lowest near 0% or 100%."""
        p = self.theories[key].probability
        return 1.0 - min(1.0, abs(p - 0.5) * 2.0)

    def highest_uncertainty_theory(self) -> Theory:
        return max(self.theories.values(), key=lambda theory: self.uncertainty(theory.key))

    def investigation_focus(self) -> str:
        self.last_focus = self.highest_uncertainty_theory().focus
        return self.last_focus

    def has_converged(self) -> bool:
        return self.leading_theory().probability >= self.convergence_threshold

    def _deltas_from_choice(
        self,
        *,
        intent: str,
        tags: set[str],
        honesty: float,
        vulnerability: float,
        defensiveness: float,
        aggression: float,
        intimacy: float,
        destabilisation: float,
    ) -> dict[str, float]:
        deltas = {key: 0.0 for key in self.theories}

        # Attachment / love / care.
        if "love" in tags or intent in {"final_yes", "lsd_maybe_love"}:
            deltas["loved_x"] += 0.26
            deltas["barely_knew_x"] -= 0.18
        if "full_admission" in tags:
            deltas["loved_x"] += 0.18
            deltas["pitied_x"] += 0.08
            deltas["barely_knew_x"] -= 0.16
        if "partial_admission" in tags or "friendship" in tags or "grief" in tags:
            deltas["pitied_x"] += 0.10
            deltas["loved_x"] += 0.06
            deltas["barely_knew_x"] -= 0.08
        if "pity" in tags or "empathy" in tags or "moral_pressure" in tags:
            deltas["pitied_x"] += 0.16
            deltas["loved_x"] -= 0.04

        # Denial and distance.
        if "denial" in tags or intent in {"final_no", "final_nothing"}:
            deltas["barely_knew_x"] += 0.14
            deltas["loved_x"] -= 0.10
            deltas["pitied_x"] -= 0.05
        if "distance" in tags or "coldness" in tags:
            deltas["barely_knew_x"] += 0.12
            deltas["pitied_x"] -= 0.07
        if "romantic_boundary" in tags:
            deltas["loved_x"] -= 0.08
            deltas["pitied_x"] += 0.04

        # Fear / betrayal / danger.
        if "fear" in tags or "avoidance" in tags or "paranoia" in tags:
            deltas["feared_x"] += 0.12
        if "guilt" in tags or "responsibility" in tags:
            deltas["betrayed_x"] += 0.14
            deltas["pitied_x"] += 0.06
        if "danger" in tags or "authority" in tags or "shared_secret" in tags:
            deltas["betrayed_x"] += 0.08
            deltas["feared_x"] += 0.06
        if "counterattack" in tags or "deflection" in tags or "refusal" in tags:
            deltas["feared_x"] += 0.06
            deltas["betrayed_x"] += 0.05

        # Continuous authored features also matter.
        deltas["loved_x"] += 0.10 * intimacy + 0.08 * vulnerability - 0.08 * defensiveness
        deltas["pitied_x"] += 0.08 * vulnerability + 0.06 * honesty - 0.04 * aggression
        deltas["feared_x"] += 0.07 * defensiveness + 0.06 * destabilisation
        deltas["betrayed_x"] += 0.05 * aggression + 0.05 * defensiveness - 0.04 * honesty
        deltas["barely_knew_x"] += 0.06 * defensiveness - 0.08 * vulnerability - 0.04 * honesty

        # Drug escalation should destabilise the model, not act as proof of
        # love or pity. The player taking acid/pills is evidence that the
        # interview conditions are becoming unreliable, so it should mostly
        # raise fear/danger while cancelling the automatic attachment gain
        # created by intimacy/vulnerability metadata.
        if "drug_escalation" in tags:
            deltas["loved_x"] -= 0.16
            deltas["pitied_x"] -= 0.10
            deltas["feared_x"] += 0.08
            deltas["betrayed_x"] += 0.03
            deltas["barely_knew_x"] += 0.02

        return deltas

    def update_from_choice(self, choice: object) -> tuple[dict[str, float], dict[str, float]]:
        before = self.snapshot()
        tags = set(getattr(choice, "semantic_tags", ()) or ())
        intent = str(getattr(choice, "intent", ""))
        deltas = self._deltas_from_choice(
            intent=intent,
            tags=tags,
            honesty=float(getattr(choice, "honesty", 0.5)),
            vulnerability=float(getattr(choice, "vulnerability", 0.5)),
            defensiveness=float(getattr(choice, "defensiveness", 0.5)),
            aggression=float(getattr(choice, "aggression", 0.0)),
            intimacy=float(getattr(choice, "intimacy", 0.0)),
            destabilisation=float(getattr(choice, "destabilisation", 0.0)),
        )
        for key, delta in deltas.items():
            self.theories[key].probability = _clamp01(self.theories[key].probability + delta)

        if "drug_escalation" in tags:
            self._destabilise_probabilities(amount=0.12)

        self.investigation_focus()
        return before, self.snapshot()

    def _destabilise_probabilities(self, *, amount: float) -> None:
        """Move theories toward uncertainty after drug escalation.

        This makes LSD/pill choices feel like corrupted evidence rather than
        a shortcut to an attachment conclusion. A high theory becomes less
        certain, a very low theory becomes newly possible, and the player gets
        more room to redirect the machine.
        """
        amount = _clamp01(amount)
        for theory in self.theories.values():
            theory.probability = _clamp01(theory.probability + (0.5 - theory.probability) * amount)

    def model_revision_text(self, before: Mapping[str, float], after: Mapping[str, float]) -> str:
        changes = []
        for key, new_value in after.items():
            old_value = before.get(key, new_value)
            diff = new_value - old_value
            if abs(diff) >= 0.045:
                direction = "strengthened" if diff > 0 else "weakened"
                changes.append((abs(diff), f"{self.theories[key].label} hypothesis {direction}."))
        changes.sort(reverse=True, key=lambda item: item[0])

        if not changes:
            body = "No major theory changed."
        else:
            body = "\n".join(text for _, text in changes[:3])

        previous_leader = max(before, key=lambda key: before[key]) if before else self.leading_theory().key
        current_leader = self.leading_theory().key
        if previous_leader != current_leader:
            body += f"\nPrevious leading theory discarded: now {self.theories[current_leader].label.lower()}."

        return "MODEL REVISION\n\n" + body

    def current_model_text(self) -> str:
        leader = self.leading_theory()
        focus = self.investigation_focus()
        return (
            "CURRENT MODEL\n\n"
            f"Leading Theory:\n{leader.label}.\n\n"
            f"Confidence:\n{self.confidence_band(leader.key)}\n\n"
            f"Investigation Focus:\n{focus}"
        )

    def machine_reasoning_text(self) -> str:
        theory = self.highest_uncertainty_theory()
        return (
            "Machine reasoning:\n\n"
            f"Uncertainty remains around {theory.focus.lower()}.\n"
            f"Selecting evidence from {theory.focus.lower()} cluster."
        )

    def final_model_text(self, *, objective_key: str | None = None) -> str:
        lines = ["FINAL MODEL", ""]
        for theory in sorted(self.theories.values(), key=lambda item: item.probability, reverse=True):
            lines.append(f"{theory.label}: {round(theory.probability * 100):d}%")
        leader = self.leading_theory()
        lines.extend(["", "Conclusion:", self._conclusion_for(leader.key)])
        if objective_key:
            victory = self._objective_result(objective_key)
            lines.extend(["", "Objective Result:", victory])
        return "\n".join(lines)

    def _conclusion_for(self, key: str) -> str:
        conclusions = {
            "loved_x": "You cared about X more than you admitted.",
            "pitied_x": "You kept X close through pity, then tried to call it distance.",
            "feared_x": "Fear shaped your relationship with X more than affection did.",
            "betrayed_x": "You knew more about X's collapse than you wanted the hearing AI to see.",
            "barely_knew_x": "The machine cannot prove closeness; your distance held.",
        }
        return conclusions.get(key, "The machine has an incomplete profile.")

    def _objective_result(self, objective_key: str) -> str:
        leader = self.leading_theory().key
        target = self.theories.get(objective_key)
        if objective_key == "avoid_loved_x":
            return "Player victory — the machine did not converge on love." if leader != "loved_x" else "Machine victory — it converged on love."
        if objective_key == "convince_feared_x":
            return "False-conviction victory — the machine converged on fear." if leader == "feared_x" else "Objective failed — fear was not the leading theory."
        if objective_key == "hide_betrayal":
            betrayed = self.theories["betrayed_x"].probability
            return "Player victory — betrayal remained below convergence." if betrayed < self.convergence_threshold else "Machine victory — betrayal converged."
        if target and leader == objective_key:
            return "Objective achieved."
        return "Objective unresolved."
