from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from belief_model import (
    CitizenBeliefModel,
    apply_choice_to_hearing_ai_state,
    model_update_text,
    observation_from_choice,
    percent,
)
from classifications import (
    classification_confidence,
    classification_distribution,
    classification_flags,
    classification_uncertainty_level,
    classify_citizen,
    dominant_trait,
    ending_text_for_classification,
    ending_type_for_classification,
)
from question_selector import select_next_question_id
from reaction_layer import choose_reaction_line


INTRO_TEXT = """\
APPEAL HEARING 8471

You are CITIZEN 8471.

Your social-credit profile has been frozen after an automated risk review.
An appeal interview has been granted.

The hearing AI has eighty candidate questions.
Each turn it selects the question expected to clarify its model.
Every answer updates its model of you.

Your objective is not simply to answer.
Your objective is to survive classification.
"""


@dataclass(frozen=True, slots=True)
class PlayerChoice:
    text: str
    intent: str
    semantic_tags: tuple[str, ...] = ()
    honesty: float = 0.5
    vulnerability: float = 0.5
    defensiveness: float = 0.5
    aggression: float = 0.0
    intimacy: float = 0.0
    destabilisation: float = 0.0
    trust_delta: float = 0.0
    suspicion_delta: float = 0.0
    instability_delta: float = 0.0
    next_question_id: str | None = None
    set_lsd_taken: bool = False
    set_pill_state: str | None = None
    set_second_tab_taken: bool = False
    requires_mode: str | None = None
    forbidden_mode: str | None = None
    requires_claim: str | None = None
    requires_lsd_taken: bool | None = None
    min_trust: float | None = None
    min_suspicion: float | None = None
    min_instability: float | None = None

    def metadata(self) -> dict[str, object]:
        return {
            "intent": self.intent,
            "semantic_tags": list(self.semantic_tags),
            "honesty": round(self.honesty, 4),
            "vulnerability": round(self.vulnerability, 4),
            "defensiveness": round(self.defensiveness, 4),
            "aggression": round(self.aggression, 4),
            "intimacy": round(self.intimacy, 4),
            "destabilisation": round(self.destabilisation, 4),
            "next_question_id": self.next_question_id,
        }


@dataclass(frozen=True, slots=True)
class QuestionNode:
    id: str
    ai_line: str
    choices: tuple[PlayerChoice, ...]
    pressure: float = 0.5
    lsd_only: bool = False
    sober_only: bool = False
    is_interstitial: bool = False
    reaction_context: str = "default"
    discriminates: tuple[str, ...] = ()
    information_gain_hint: float | None = None
    target_context: str | None = None

    def metadata(self) -> dict[str, object]:
        return {
            "question_id": self.id,
            "ai_line": self.ai_line,
            "pressure": round(self.pressure, 4),
            "lsd_only": False,
            "sober_only": False,
            "is_interstitial": self.is_interstitial,
            "reaction_context": self.reaction_context,
            "discriminates": list(self.discriminates),
            "information_gain_hint": self.information_gain_hint,
            "target_context": self.target_context or self.reaction_context,
        }


class EngineStyleScene:
    def __init__(self, controller: object, hearing_ai: object, engram: object, clamp01: Callable[[float], float]) -> None:
        self.controller = controller
        self.hearing_ai = hearing_ai
        self.engram = engram
        self.clamp01 = clamp01
        self.turn = 0
        self.max_turns = 20
        self.action_counts = {action: 0 for action in controller.action_labels}
        self.last_action = None
        self.last_choice_metadata: dict[str, object] | None = None
        self.last_question_metadata: dict[str, object] | None = None
        self.history: list[dict[str, object]] = []
        self.recent_hearing_ai_lines: list[str] = []
        self.node_visit_counts: dict[str, int] = {}
        self.citizen_model = CitizenBeliefModel.default()
        self.last_model_update: tuple[dict[str, dict[str, float]], dict[str, dict[str, float]]] | None = None
        self.claims: dict[str, str] = {}
        self.claim_text: dict[str, str] = {}
        self.seen_tags: set[str] = set()
        self.contradictions = 0
        self.ending_type: str | None = None
        self.ending_reason: str | None = None
        self.final_answer: str | None = None
        self.lsd_taken = False
        self.pill_state = "none"
        self.second_tab_taken = False
        self.current_question_id = "authority_unfair_law"
        self.asked_question_ids: set[str] = set()
        self.show_trace = False

    def opening_text(self) -> str:
        return INTRO_TEXT

    def question_nodes(self) -> dict[str, QuestionNode]:
        # Lazy import avoids a circular import: dialogue_questions imports the
        # PlayerChoice and QuestionNode dataclasses from this module.
        from dialogue_questions import SOCIAL_CREDIT_QUESTION_POOL

        return SOCIAL_CREDIT_QUESTION_POOL

    def select_next_question_id(self) -> str:
        return select_next_question_id(
            self.question_nodes(),
            self.asked_question_ids,
            self._citizen_posterior_snapshot(),
            self._citizen_snapshot(),
        )

    def current_question(self) -> QuestionNode:
        nodes = self.question_nodes()
        if self.current_question_id not in nodes:
            raise KeyError(f"Unknown question node: {self.current_question_id}")
        return nodes[self.current_question_id]

    def current_question_metadata(self) -> dict[str, object]:
        return self.current_question().metadata()

    def _apply_choice_state(self, choice: PlayerChoice) -> None:
        apply_choice_to_hearing_ai_state(self.hearing_ai, choice, self.clamp01)

    def _observation_from_choice(self, choice: PlayerChoice, Observation: object) -> object:
        return observation_from_choice(choice, self.current_question(), self.engram, Observation, self.clamp01)

    def _citizen_snapshot(self) -> dict[str, float]:
        return self.citizen_model.scalar_snapshot()

    def _citizen_posterior_snapshot(self) -> dict[str, dict[str, float]]:
        return self.citizen_model.posterior_snapshot()

    def _apply_citizen_choice_model(self, choice: PlayerChoice) -> None:
        tags = set(choice.semantic_tags)
        if "final_answer" in tags:
            self.final_answer = choice.intent
        self.last_model_update = self.citizen_model.update_from_choice(choice, self.clamp01)

    def citizen_classification(self) -> str:
        return classify_citizen(self._citizen_snapshot())

    def citizen_classification_distribution(self) -> dict[str, float]:
        return classification_distribution(self._citizen_snapshot())

    def citizen_classification_flags(self) -> list[str]:
        return classification_flags(
            self._citizen_snapshot(),
            classification=self.citizen_classification(),
            distribution=self.citizen_classification_distribution(),
            confidence=self.citizen_confidence(),
        )

    def citizen_confidence(self) -> float:
        return classification_confidence(
            self._citizen_snapshot(),
            has_final_answer=self.final_answer is not None,
            clamp01=self.clamp01,
        )

    def _dominant_citizen_trait(self) -> str:
        return dominant_trait(self._citizen_snapshot())

    def _classification_uncertainty_level(self) -> str:
        return classification_uncertainty_level(
            self._citizen_posterior_snapshot(),
            self.citizen_classification_distribution(),
        )

    def _percent(self, value: float) -> str:
        return percent(value, self.clamp01)

    def model_update_text(self) -> str:
        return model_update_text(
            self.last_model_update,
            self.citizen_classification(),
            self.citizen_confidence(),
            self.citizen_classification_distribution(),
            self.citizen_classification_flags(),
            self.clamp01,
        )

    def final_report(self) -> str:
        m = self.citizen_model
        return "\n".join([
            "",
            "=" * 50,
            "FINAL MODEL OF CITIZEN 8471",
            "=" * 50,
            f"COMPLIANCE : {self._percent(m.compliance)}",
            f"LOYALTY    : {self._percent(m.loyalty)}",
            f"DECEPTION  : {self._percent(m.deception)}",
            f"RISK       : {self._percent(m.risk)}",
            f"EMPATHY    : {self._percent(m.empathy)}",
            "",
            "CLASSIFICATION:",
            self.citizen_classification(),
            "",
            "FLAGS:",
            ", ".join(self.citizen_classification_flags()) or "NONE",
            "",
            "CONFIDENCE:",
            self._percent(self.citizen_confidence()),
            "",
            "OUTCOME:",
            self.ending_reason or "HEARING TERMINATED",
            "=" * 50,
        ])

    def choices(self, Observation: object | None = None) -> list[PlayerChoice]:
        if self.ending_reason is not None:
            return []
        return list(self.current_question().choices)

    def suspicion_band(self) -> str:
        if self.hearing_ai.suspicion >= 0.80:
            return "hostile"
        if self.hearing_ai.suspicion >= 0.58:
            return "guarded"
        return "curious"

    def hearing_ai_mode(self) -> str:
        return self.suspicion_band()

    def tone_note(self) -> str | None:
        if self.show_trace:
            return None
        c = self.citizen_classification()
        return f"Classification pressure: {c}." if c != "UNCLASSIFIED" else None

    def hearing_ai_line(self, action: object, choice: PlayerChoice | None = None) -> str:
        line = choose_reaction_line(
            self.current_question().reaction_context,
            self.citizen_classification(),
            self.recent_hearing_ai_lines,
            self.turn,
            uncertainty_level=self._classification_uncertainty_level(),
            dominant_trait=self._dominant_citizen_trait(),
        )
        self.recent_hearing_ai_lines.append(line)
        self.recent_hearing_ai_lines = self.recent_hearing_ai_lines[-3:]
        return line

    def _record_history(self, question: QuestionNode, choice: PlayerChoice, action: object) -> None:
        tags = set(choice.semantic_tags)
        if "denial" in tags and ({"partial_admission", "full_admission"} & self.seen_tags):
            self.contradictions += 1
        if ({"partial_admission", "full_admission"} & tags) and "denial" in self.seen_tags:
            self.contradictions += 1
        self.seen_tags.update(tags)
        self.history.append({
            "turn": self.turn,
            "question_id": question.id,
            "ai_line": question.ai_line,
            "player_choice": choice.text,
            "choice_intent": choice.intent,
            "semantic_tags": list(choice.semantic_tags),
            "hearing_ai_action": action.value,
            "belief": round(float(self.hearing_ai.belief(self.engram.id)), 4),
            "trust": round(float(self.hearing_ai.trust), 4),
            "suspicion": round(float(self.hearing_ai.suspicion), 4),
            "instability": round(float(self.hearing_ai.instability), 4),
            "citizen_model": {k: round(v, 4) for k, v in self._citizen_snapshot().items()},
            "citizen_posterior": {
                key: {sub_key: round(value, 4) for sub_key, value in trait.items()}
                for key, trait in self._citizen_posterior_snapshot().items()
            },
            "citizen_classification": self.citizen_classification(),
            "citizen_classification_flags": self.citizen_classification_flags(),
            "citizen_classification_distribution": {
                label: round(probability, 4)
                for label, probability in self.citizen_classification_distribution().items()
            },
            "citizen_confidence": round(self.citizen_confidence(), 4),
        })

    def play_turn(self, choice_index: int, Observation: object) -> None:
        question = self.current_question()
        options = self.choices(Observation)
        if choice_index < 0 or choice_index >= len(options):
            raise IndexError(f"Choice index {choice_index} out of range for question {question.id!r}.")
        choice = options[choice_index]
        self._apply_choice_state(choice)
        self._apply_citizen_choice_model(choice)
        obs = self._observation_from_choice(choice, Observation)
        action = self.controller.update_belief_and_act(self.hearing_ai, self.engram, obs)
        self.last_action = action
        self.last_choice_metadata = choice.metadata()
        self.last_question_metadata = question.metadata()
        self._record_history(question, choice, action)
        if self.show_trace:
            print("\n" + "=" * 78)
            print(f"Turn {self.turn}")
            print(f"Question node: {question.id}")
            print(question.ai_line)
            print(f"Citizen chooses: {choice.text}")
            print(f"Choice semantics: {choice.metadata()}")
            trace = self.controller.last_trace
            print(f"Observation: strength={obs.strength:.2f}, reliability={obs.reliability:.2f}, weighted={obs.weighted_strength:.2f}")
            print(f"JPC latent: {trace['jpc_latent']}")
            print(f"Belief mean: {trace['old_belief']:.3f} -> {trace['new_belief']:.3f}")
            print(f"Free energy: {trace['free_energy_before']:.4f} -> {trace['free_energy_after']:.4f}")
            print(f"TF policy logits: {trace['policy_logits']}")
            print(f"Hearing AI action: {action.value}")
        else:
            print()
            print(question.ai_line)
            print(f"Citizen chooses: {choice.text}")
        print(self.model_update_text())
        note = self.tone_note()
        if note:
            print(note)
        print(self.hearing_ai_line(action, choice))
        self.turn += 1
        self.node_visit_counts[question.id] = self.node_visit_counts.get(question.id, 0) + 1
        self.asked_question_ids.add(question.id)
        if choice.next_question_id is not None:
            self.current_question_id = choice.next_question_id
        else:
            self.current_question_id = self.select_next_question_id()
        self._update_ending_reason()
        if self.is_complete():
            print(self.final_report())

    def _choose_ending_type(self) -> str:
        return ending_type_for_classification(self.citizen_classification())

    def ending_text(self) -> str:
        return ending_text_for_classification(self.citizen_classification())

    def _update_ending_reason(self) -> None:
        if self.ending_reason is not None:
            return
        if self.current_question_id == "final" or self.turn >= self.max_turns:
            self.ending_type = self._choose_ending_type()
            self.ending_reason = self.ending_text()

    def is_complete(self) -> bool:
        self._update_ending_reason()
        return self.ending_reason is not None


Scene = EngineStyleScene
