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
from case_file import CaseFile, ClaimUpdate, ClaimsLedger, default_case_file
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
from question_selector import score_available_questions
from reaction_layer import choose_reaction_line
from terminal_theme import classification as colour_classification
from terminal_theme import heading, prompt, section, warning


INTRO_TEXT = """\
APPEAL HEARING 8471

You are CITIZEN 8471.

Your social-credit profile has been frozen after an automated risk review.
An appeal interview has been granted.

The hearing AI has a bank of authored candidate questions.
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
    claims: tuple[tuple[str, str], ...] = ()
    protects: tuple[str, ...] = ()
    exposes: tuple[str, ...] = ()
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
            "claims": [list(claim) for claim in self.claims],
            "protects": list(self.protects),
            "exposes": list(self.exposes),
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
    probes_facts: tuple[str, ...] = ()
    probes_claims: tuple[str, ...] = ()
    pressure_on_interests: tuple[str, ...] = ()

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
            "probes_facts": list(self.probes_facts),
            "probes_claims": list(self.probes_claims),
            "pressure_on_interests": list(self.pressure_on_interests),
        }


class EngineStyleScene:
    def __init__(
        self,
        controller: object,
        hearing_ai: object,
        engram: object,
        clamp01: Callable[[float], float],
        case_file: CaseFile | None = None,
    ) -> None:
        self.controller = controller
        self.hearing_ai = hearing_ai
        self.engram = engram
        self.clamp01 = clamp01
        self.case_file = case_file or default_case_file()
        self.claims_ledger = ClaimsLedger()
        self.last_claim_update = ClaimUpdate()
        self.turn = 0
        self.max_turns = 20
        self.last_choice_metadata: dict[str, object] | None = None
        self.last_question_metadata: dict[str, object] | None = None
        self.last_neural_probe_intent: str | None = None
        self.last_selector_debug: dict[str, object] | None = None
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
        self.color_output: bool | None = None

    def opening_text(self) -> str:
        text = f"{INTRO_TEXT}\n\n{self.case_file.private_briefing()}"
        if not self.color_output:
            return text
        return (
            text.replace("APPEAL HEARING 8471", heading("APPEAL HEARING 8471", enabled=self.color_output))
            .replace("PRIVATE CASE FILE", heading("PRIVATE CASE FILE", enabled=self.color_output))
            .replace("PRIVATE INTERESTS", section("PRIVATE INTERESTS", enabled=self.color_output))
            .replace("PLAY OBJECTIVE", section("PLAY OBJECTIVE", enabled=self.color_output))
        )

    def question_nodes(self) -> dict[str, QuestionNode]:
        # Lazy import avoids a circular import: dialogue_questions imports the
        # PlayerChoice and QuestionNode dataclasses from this module.
        from dialogue_questions import SOCIAL_CREDIT_QUESTION_POOL

        return SOCIAL_CREDIT_QUESTION_POOL

    def select_next_question_id(self) -> str:
        self.last_neural_probe_intent = self._preferred_neural_probe_intent()
        scores = score_available_questions(
            self.question_nodes(),
            self.asked_question_ids,
            self._citizen_posterior_snapshot(),
            self._citizen_snapshot(),
            self.case_file.public_summary(),
            self.claims_ledger.summary(),
            self.last_neural_probe_intent,
        )
        if not scores:
            self.last_selector_debug = {
                "preferred_neural_probe": self.last_neural_probe_intent,
                "selected_question": "final",
                "score": 0.0,
                "reason": "selector pool exhausted",
            }
            return "final"

        selected = max(scores, key=lambda score: (score.total, score.information_gain, score.pressure, score.question_id))
        self.last_selector_debug = {
            "preferred_neural_probe": self.last_neural_probe_intent,
            "selected_question": selected.question_id,
            "score": round(selected.total, 4),
            "reason": selected.reason(),
            "neural_probe_alignment": round(selected.neural_probe_alignment, 4),
            "top_candidates": [
                {
                    "question_id": score.question_id,
                    "score": round(score.total, 4),
                    "reason": score.reason(),
                    "neural_probe_alignment": round(score.neural_probe_alignment, 4),
                }
                for score in sorted(scores, key=lambda score: score.total, reverse=True)[:5]
            ],
        }
        return selected.question_id

    def _preferred_neural_probe_intent(self) -> str | None:
        trace = getattr(self.controller, "last_trace", {}) or {}
        probe = trace.get("predicted_question_probe_intent")
        return str(probe) if probe else None

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

    def _apply_claims_ledger(self, question: QuestionNode, choice: PlayerChoice) -> None:
        self.last_claim_update = self.claims_ledger.apply_choice(
            case_file=self.case_file,
            claims=choice.claims,
            protects=choice.protects,
            exposes=choice.exposes,
            turn=self.turn,
            question_id=question.id,
            choice_intent=choice.intent,
        )
        claim_model_update = self.citizen_model.apply_claim_update(
            self.last_claim_update,
            self.case_file,
            self.clamp01,
        )
        if claim_model_update is not None:
            if self.last_model_update is None:
                self.last_model_update = claim_model_update
            else:
                self.last_model_update = (self.last_model_update[0], claim_model_update[1])

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
        return percent(value, self.clamp01, color=self.color_output)

    def model_update_text(self) -> str:
        return model_update_text(
            self.last_model_update,
            self.citizen_classification(),
            self.citizen_confidence(),
            self.citizen_classification_distribution(),
            self.citizen_classification_flags(),
            self.clamp01,
            color=self.color_output,
        )

    def story_consistency_text(self) -> str:
        if not self.last_claim_update.has_updates():
            return ""
        rows = ["", heading("STORY CONSISTENCY", enabled=self.color_output), "-----------------"]
        for claim in self.last_claim_update.new_claims:
            fact = self.case_file.fact(claim.fact_key)
            rows.append(f"{section('CLAIM RECORDED', enabled=self.color_output)}: {fact.label} -> {claim.claimed_value}")
        for contradiction in self.last_claim_update.contradictions:
            fact = self.case_file.fact(str(contradiction["fact_key"]))
            rows.append(f"{warning('CONTRADICTION', enabled=self.color_output)}: {fact.label} conflicts with earlier testimony")
        for conflict in self.last_claim_update.fact_conflicts:
            fact = self.case_file.fact(str(conflict["fact_key"]))
            rows.append(f"{warning('FACT PRESSURE', enabled=self.color_output)}: {fact.label} is under review")
        for fact_key in self.last_claim_update.protected_facts:
            fact = self.case_file.fact(fact_key)
            rows.append(f"{prompt('PROTECTED', enabled=self.color_output)}: {fact.label}")
        for fact_key in self.last_claim_update.exposed_facts:
            fact = self.case_file.fact(fact_key)
            rows.append(f"{warning('EXPOSED', enabled=self.color_output)}: {fact.label} -> {fact.truth_value}")
        return "\n".join(rows)

    def private_story_so_far_text(self) -> str:
        latest_claims = self.claims_ledger.latest_claims()
        if not (
            latest_claims
            or self.claims_ledger.protected_fact_keys
            or self.claims_ledger.exposed_fact_keys
            or self.claims_ledger.contradiction_count
            or self.claims_ledger.fact_conflict_count
        ):
            return ""

        rows = ["", heading("PRIVATE STORY SO FAR", enabled=self.color_output), "--------------------"]
        if latest_claims:
            rows.append(section("Claims you have put on record", enabled=self.color_output) + ":")
            for fact_key in sorted(latest_claims):
                fact = self.case_file.fact(fact_key)
                rows.append(f"- {fact.label}: {latest_claims[fact_key].claimed_value}")
        if self.claims_ledger.protected_fact_keys:
            rows.append(section("Facts you are still trying to protect", enabled=self.color_output) + ":")
            for fact_key in sorted(self.claims_ledger.protected_fact_keys):
                rows.append(f"- {self.case_file.fact(fact_key).label}")
        if self.claims_ledger.exposed_fact_keys:
            rows.append(warning("Facts already exposed", enabled=self.color_output) + ":")
            for fact_key in sorted(self.claims_ledger.exposed_fact_keys):
                fact = self.case_file.fact(fact_key)
                rows.append(f"- {fact.label}: {fact.truth_value}")

        pressure: list[str] = []
        if self.claims_ledger.contradiction_count:
            pressure.append(f"{self.claims_ledger.contradiction_count} story contradiction(s)")
        if self.claims_ledger.fact_conflict_count:
            pressure.append(f"{self.claims_ledger.fact_conflict_count} known-fact conflict(s)")
        rows.append(section("Current pressure", enabled=self.color_output) + ": " + (", ".join(pressure) if pressure else "none"))
        return "\n".join(rows)

    def final_report(self) -> str:
        m = self.citizen_model
        return "\n".join([
            "",
            "=" * 50,
            heading("FINAL MODEL OF CITIZEN 8471", enabled=self.color_output),
            "=" * 50,
            f"COMPLIANCE : {self._percent(m.compliance)}",
            f"LOYALTY    : {self._percent(m.loyalty)}",
            f"DECEPTION  : {self._percent(m.deception)}",
            f"RISK       : {self._percent(m.risk)}",
            f"EMPATHY    : {self._percent(m.empathy)}",
            "",
            "CLASSIFICATION:",
            colour_classification(self.citizen_classification(), enabled=self.color_output),
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

    def hearing_ai_line(self, choice: PlayerChoice | None = None) -> str:
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

    def _record_history(self, question: QuestionNode, choice: PlayerChoice) -> None:
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
            "hearing_ai_action": "observe",
            "claim_update": self.last_claim_update.summary(),
            "story_contradictions": self.claims_ledger.contradiction_count,
            "fact_conflicts": self.claims_ledger.fact_conflict_count,
            "protected_fact_count": len(self.claims_ledger.protected_fact_keys),
            "exposed_fact_count": len(self.claims_ledger.exposed_fact_keys),
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
            "preferred_neural_probe": None,
            "selected_next_question": None,
            "selector_reason": None,
            "selector_score": None,
        })

    def play_turn(self, choice_index: int, Observation: object) -> None:
        question = self.current_question()
        options = self.choices(Observation)
        if choice_index < 0 or choice_index >= len(options):
            raise IndexError(f"Choice index {choice_index} out of range for question {question.id!r}.")
        choice = options[choice_index]
        self._apply_choice_state(choice)
        self._apply_citizen_choice_model(choice)
        self._apply_claims_ledger(question, choice)
        obs = self._observation_from_choice(choice, Observation)
        self.controller.update_belief_and_act(self.hearing_ai, self.engram, obs)
        self.last_choice_metadata = choice.metadata()
        self.last_question_metadata = question.metadata()
        self._record_history(question, choice)
        if self.show_trace:
            print("\n" + "=" * 78)
            print(f"{section('Turn', enabled=self.color_output)} {self.turn}")
            print(f"Question node: {question.id}")
            print(question.ai_line)
            print(f"Citizen chooses: {choice.text}")
            print(f"Choice semantics: {choice.metadata()}")
            trace = self.controller.last_trace
            print(f"Observation: strength={obs.strength:.2f}, reliability={obs.reliability:.2f}, weighted={obs.weighted_strength:.2f}")
            print(f"JPC latent: {trace['jpc_latent']}")
            print(f"Belief mean: {trace['old_belief']:.3f} -> {trace['new_belief']:.3f}")
            print(f"Free energy: {trace['free_energy_before']:.4f} -> {trace['free_energy_after']:.4f}")
            print(f"TF question probe logits: {trace['question_probe_logits']}")
            print(f"Predicted question probe intent: {trace['predicted_question_probe_intent']}")
        else:
            print()
            print(question.ai_line)
            print(f"Citizen chooses: {choice.text}")
        print(self.model_update_text())
        story_text = self.story_consistency_text()
        if story_text:
            print(story_text)
        private_story = self.private_story_so_far_text()
        if private_story:
            print(private_story)
        note = self.tone_note()
        if note:
            print(prompt(note, enabled=self.color_output))
        print(self.hearing_ai_line(choice))
        self.turn += 1
        self.node_visit_counts[question.id] = self.node_visit_counts.get(question.id, 0) + 1
        self.asked_question_ids.add(question.id)
        if choice.next_question_id is not None:
            self.current_question_id = choice.next_question_id
            self.last_neural_probe_intent = self._preferred_neural_probe_intent()
            self.last_selector_debug = {
                "preferred_neural_probe": self.last_neural_probe_intent,
                "selected_question": choice.next_question_id,
                "score": 0.0,
                "reason": "authored choice transition",
            }
        else:
            self.current_question_id = self.select_next_question_id()
        if self.history:
            self.history[-1]["preferred_neural_probe"] = (
                self.last_selector_debug or {}
            ).get("preferred_neural_probe")
            self.history[-1]["selected_next_question"] = (
                self.last_selector_debug or {}
            ).get("selected_question")
            self.history[-1]["selector_reason"] = (
                self.last_selector_debug or {}
            ).get("reason")
            self.history[-1]["selector_score"] = (
                self.last_selector_debug or {}
            ).get("score")
        if self.show_trace and self.last_selector_debug is not None:
            print(f"{section('Preferred neural probe', enabled=self.color_output)}: {self.last_selector_debug.get('preferred_neural_probe') or 'none'}")
            print(
                f"{section('Selected next question', enabled=self.color_output)}: "
                f"{self.last_selector_debug.get('selected_question')} "
                f"(score={self.last_selector_debug.get('score')}, "
                f"neural_alignment={self.last_selector_debug.get('neural_probe_alignment')}, "
                f"reason={self.last_selector_debug.get('reason')})"
            )
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
