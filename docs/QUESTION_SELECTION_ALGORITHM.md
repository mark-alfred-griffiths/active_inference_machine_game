# Question Selection Algorithm

This document describes how the current Citizen hearing demo selects the next question posed to the player.

The implementation is based on:

- `question_selector.py`
- `engine_style_scene.py`
- `pc_jpc_tensorflow_npc_demo.py`
- `dialogue_questions.py`

## Summary

The system uses a hybrid selector.

The neural network does not directly choose the next question ID. Instead, it predicts a broad `question_probe_intent`, such as `probe_deception` or `probe_protected_fact`. The heuristic selector then scores valid authored questions and chooses the highest-scoring unasked question.

This design preserves authored gameplay while still letting the neural model influence what kind of uncertainty the hearing AI investigates next.

```text
player answer
    -> belief/story update
    -> JPC latent
    -> TensorFlow question_probe_logits
    -> preferred question_probe_intent
    -> heuristic scoring over valid authored questions
    -> next question ID
```

## Why The Neural Network Does Not Directly Choose Question IDs

Direct neural question-ID selection would be brittle in this project because questions are authored game content. A raw neural selector could choose:

- a question that does not exist,
- a question already asked,
- a terminal or invalid node,
- a question that is narratively incoherent,
- a question unsupported by the current story state.

The current design avoids that by splitting responsibility:

- `pc_jpc_tensorflow_npc_demo.py` predicts the desired probe type.
- `question_selector.py` maps that probe type onto valid authored questions.
- `engine_style_scene.py` enforces the turn loop and stores debug trace output.
- `dialogue_questions.py` provides the authored question bank and metadata.

The result is a safety layer: the neural network influences the selector, but the selector remains constrained to playable authored nodes.

## Authored Question Metadata

Questions are defined in `dialogue_questions.py` as `QuestionNode` instances from `engine_style_scene.py`.

Selection-relevant fields include:

```text
reaction_context
target_context
discriminates
information_gain_hint
pressure
probes_facts
probes_claims
pressure_on_interests
choices
```

Examples from `dialogue_questions.py` include case-file questions that probe facts such as:

```text
believes_law_unjust
attended_meeting
deleted_message
planned_violence
sibling_present
reported_contact
```

Choice metadata such as `claims`, `protects`, and `exposes` is not directly scored as a future question, but it updates the claims ledger and case-file state. That updated state then affects the next question score.

## Neural Probe Intent

`QuestionProbeIntent` is defined in `pc_jpc_tensorflow_npc_demo.py`.

Current probe intents are:

```text
probe_compliance
probe_loyalty
probe_deception
probe_risk
probe_empathy
probe_contradiction
probe_protected_fact
probe_final_answer
```

The TensorFlow model in `TensorFlowHearingAIHeads` has three heads:

```text
belief_raw_delta
policy_logits
question_probe_logits
```

The question probe head outputs one logit per probe intent. At runtime, `JPCTensorFlowHearingAIController.update_belief_and_act()` stores the chosen probe in `controller.last_trace`:

```python
"predicted_question_probe_intent": self.probe_intent_labels[int(np.argmax(probe_logits))].value
```

`EngineStyleScene._preferred_neural_probe_intent()` reads this value:

```python
trace = getattr(self.controller, "last_trace", {}) or {}
probe = trace.get("predicted_question_probe_intent")
return str(probe) if probe else None
```

That preferred probe is then passed into `score_available_questions()`.

## Runtime Selection Flow

The runtime handoff happens in `EngineStyleScene.play_turn()`.

After the player selects an answer, the engine:

1. applies trust/suspicion/instability deltas,
2. updates `CitizenBeliefModel`,
3. updates `ClaimsLedger`,
4. builds an `Observation`,
5. calls `controller.update_belief_and_act(...)`,
6. records trace/history,
7. marks the current question as asked,
8. selects the next question.

If the selected `PlayerChoice` has an explicit `next_question_id`, the engine follows it. Otherwise:

```python
self.current_question_id = self.select_next_question_id()
```

`EngineStyleScene.select_next_question_id()` calls:

```python
score_available_questions(
    self.question_nodes(),
    self.asked_question_ids,
    self._citizen_posterior_snapshot(),
    self._citizen_snapshot(),
    self.case_file.public_summary(),
    self.claims_ledger.summary(),
    self.last_neural_probe_intent,
)
```

The highest-scoring `QuestionScore` becomes the next question.

## Valid Question Filtering

`question_selector.score_available_questions()` only considers questions that meet all of these conditions:

```python
question_id != "final"
node.choices
question_id not in asked_question_ids
```

This prevents:

- direct repetition,
- selecting `final` as a normal question,
- selecting nodes without player choices,
- selecting missing/non-authored question IDs.

If no valid questions remain, the selector returns `final`.

## Scoring Formula

Each candidate receives a `QuestionScore` in `question_selector.score_question()`.

The current weighted scoring formula is:

```text
total =
    information_gain              * TRAIT_INFORMATION_WEIGHT
  + pressure                      * QUESTION_PRESSURE_WEIGHT
  + ambiguity                     * CLASSIFICATION_AMBIGUITY_WEIGHT
  + context_coverage              * CONTEXT_COVERAGE_WEIGHT
  + fact_probe_gain               * FACT_PROBE_WEIGHT
  + contradiction_probe_gain      * CONTRADICTION_PROBE_WEIGHT
  + protected_interest_pressure   * PROTECTED_INTEREST_WEIGHT
  + neural_probe_alignment        * NEURAL_PROBE_INTENT_WEIGHT
  - exposed_fact_penalty          * EXPOSED_FACT_PENALTY_WEIGHT
```

Current constants in `question_selector.py`:

```text
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
```

The large weights are currently trait uncertainty, pressure, classification ambiguity, and context coverage. Story and neural-probe terms are smaller nudges, except contradiction probing has a stronger dedicated weight.

## Classification Ambiguity

Classification ambiguity is computed by `_classification_ambiguity()`.

It calls `classification_distribution(snapshot)` from `classifications.py`, sorts the probabilities, and computes:

```text
1.0 - (top_probability - second_probability)
```

If the top two classifications are close together, ambiguity is high. High ambiguity increases the score of all candidate questions through `CLASSIFICATION_AMBIGUITY_WEIGHT`.

Gameplay effect: when the classifier is uncertain, the hearing AI keeps asking questions rather than prematurely settling.

## Trait Uncertainty And Information Gain

Trait uncertainty is handled by `_trait_information_gain()`.

It considers:

- the question's selector context,
- `TRAIT_BY_CONTEXT`,
- the question's `discriminates` metadata,
- semantic tags on the question's answer choices,
- the current citizen posterior snapshot.

`TRAIT_BY_CONTEXT` maps contexts to model traits:

```text
authority    -> compliance
loyalty      -> loyalty
association  -> loyalty
deception    -> deception
risk         -> risk
empathy      -> empathy
final        -> risk
```

If a question targets uncertain traits, it receives higher information gain. `information_gain_hint` can scale the base gain:

```text
hint_multiplier = 0.75 + 0.50 * information_gain_hint
```

Gameplay effect: if deception is uncertain, deception-discriminating questions become more attractive; if loyalty is uncertain, loyalty questions become more attractive.

## Question Pressure

Each `QuestionNode` has a `pressure` value. This is added through `QUESTION_PRESSURE_WEIGHT`.

Higher-pressure questions are more likely when all else is equal.

There is a specific final-context adjustment:

```python
if selector_context == "final" and len(asked_question_ids) < 5:
    pressure *= 0.45
```

This makes final-style questions less likely too early.

## Coverage And Repetition

The selector does not merely ask the highest-pressure question in one category repeatedly.

`_context_counts()` counts how often each selector context has already appeared in `asked_question_ids`.

`context_coverage` rewards less-used contexts:

```text
context_coverage = (max_seen - context_seen + 1) / (max_seen + 1)
```

A context that has been used less than the most-used context gets a coverage boost.

Direct question repetition is prevented by filtering out `asked_question_ids` entirely.

Gameplay effect: the hearing AI tends to move across authority, loyalty, deception, risk, empathy, final, and case-pressure contexts rather than staying stuck on one theme.

## Story State

Story state is computed in `_story_state()` using:

- `case_file.public_summary()`
- `claims_ledger.summary()`

It extracts:

```text
unrevealed_fact_keys
contradicted_fact_keys
protected_fact_keys
exposed_fact_keys
pressured_interest_keys
```

### Protected Facts

A protected fact is a fact the player has tried to shield via choice metadata.

If protected facts overlap with a `PlayerInterest`, `_interest_pressure()` marks the relevant interest as pressured. A candidate question can receive `protected_interest_pressure` if its `pressure_on_interests` overlaps with that pressured interest.

Gameplay effect: if the player keeps protecting their sibling, questions that pressure `protect_sibling` become more likely.

### Exposed Facts

If a fact has already been exposed, future questions probing that fact receive `exposed_fact_penalty`.

Gameplay effect: the AI is less rewarded for repeatedly probing facts already revealed.

### Contradictions

The selector treats a fact as contradicted when the claims ledger contains multiple incompatible claimed values for that fact.

Contradiction compatibility is intentionally softened by `_claims_contradict()`:

- identical values do not contradict,
- ambiguous refinements such as `conditional`, `private`, `procedural`, `protected`, `unknown`, `partial`, and `legal_only` do not contradict each other,
- direct `true` versus `false` contradicts,
- direct `true`/`false` versus an ambiguous refinement does not automatically contradict.

If a candidate probes contradicted facts or claims, it receives `contradiction_probe_gain`.

Gameplay effect: direct inconsistencies make follow-up questions more likely, but cautious partial answers are treated as ambiguous rather than automatically deceptive.

### Fact Conflicts

Known fact conflicts are tracked by `ClaimsLedger` and affect the belief model in `belief_model.py`. In the selector, direct fact-conflict events are not separately weighted as their own field. Instead, their practical influence enters through the claims ledger and story state: claims remain recorded by fact, exposed/protected facts remain tracked, and related fact/claim probes can still be scored through `probes_facts`, `probes_claims`, protected interests, and contradiction logic.

Gameplay effect: a claim that conflicts with the case file creates model pressure immediately, while future selection pressure depends on how that claim changes the ledger and relevant authored probe metadata.

## Story Warmup

`STORY_PRESSURE_WARMUP_TURNS = 5` limits early story pressure.

In `score_question()`:

```python
if len(asked_question_ids) < STORY_PRESSURE_WARMUP_TURNS and contradiction_probe_gain <= 0.0:
    fact_probe_gain = 0.0
    protected_interest_pressure = 0.0
    exposed_fact_penalty = 0.0
```

During the first five asked questions, story fact pressure is mostly muted unless there is already contradiction pressure.

Gameplay effect: early play does not immediately collapse into case-file interrogation unless the player creates strong inconsistency pressure.

## Neural Probe Alignment

`_probe_intent_alignment()` maps the neural `preferred_probe_intent` onto candidate question metadata.

Examples:

```text
probe_compliance      -> authority/compliance contexts or compliance discriminates
probe_loyalty         -> loyalty/association contexts or loyalty discriminates
probe_deception       -> deception context, deception discriminates, or claim probes
probe_risk            -> risk context or risk discriminates
probe_empathy         -> empathy context or empathy discriminates
probe_contradiction   -> probes contradicted facts/claims, or claim-probe questions
probe_protected_fact  -> probes protected facts or pressured interests
probe_final_answer    -> final context
```

The resulting alignment value is multiplied by `NEURAL_PROBE_INTENT_WEIGHT`, currently `0.001`.

Gameplay effect: the neural model nudges the selector toward the type of question it thinks is useful, but it does not dominate authored scoring.

## Tie-Breaking

`EngineStyleScene.select_next_question_id()` chooses:

```python
max(scores, key=lambda score: (score.total, score.information_gain, score.pressure, score.question_id))
```

So ties are resolved by:

1. total score,
2. information gain,
3. pressure,
4. question ID.

The standalone `question_selector.select_next_question_id()` also supports seeded stochastic tie selection among candidates within `0.03` of the top score, but `EngineStyleScene.select_next_question_id()` currently uses deterministic max selection.

## Debug Trace

When debug trace is enabled, `EngineStyleScene.play_turn()` prints:

- JPC latent,
- belief mean change,
- free energy before/after,
- TensorFlow policy logits,
- TensorFlow question probe logits,
- predicted question probe intent,
- hearing AI action.

`EngineStyleScene.select_next_question_id()` also stores `last_selector_debug` with:

```text
preferred_neural_probe
selected_question
score
reason
neural_probe_alignment
top_candidates
```

The history row for each turn records:

```text
preferred_neural_probe
selected_next_question
selector_reason
selector_score
```

These fields appear in deterministic profile reports and training examples.

## Compact Pseudocode

```python
def play_turn(choice):
    question = current_question()

    apply_choice_to_hearing_ai_state(choice)
    citizen_model.update_from_choice(choice)
    claims_ledger.apply_choice(choice.claims, choice.protects, choice.exposes)

    obs = observation_from_choice(choice, question)
    action = controller.update_belief_and_act(hearing_ai, engram, obs)

    asked_question_ids.add(question.id)

    if choice.next_question_id is not None:
        return choice.next_question_id

    preferred_probe = controller.last_trace.get("predicted_question_probe_intent")

    candidates = []
    for node in authored_questions:
        if node.id == "final":
            continue
        if not node.choices:
            continue
        if node.id in asked_question_ids:
            continue

        score = (
            trait_information_gain(node, citizen_posterior) * 0.38
            + node.pressure * 0.21
            + classification_ambiguity(citizen_snapshot) * 0.19
            + context_coverage(node, asked_question_ids) * 0.10
            + fact_probe_gain(node, case_file, claims_ledger) * 0.002
            + contradiction_probe_gain(node, case_file, claims_ledger) * 0.05
            + protected_interest_pressure(node, case_file, claims_ledger) * 0.002
            + neural_probe_alignment(node, preferred_probe) * 0.001
            - exposed_fact_penalty(node, case_file, claims_ledger) * 0.02
        )
        candidates.append((score, node))

    if not candidates:
        return "final"

    return max(candidates).node.id
```

## Active Inference Gameplay

The selector creates active-inference gameplay because the AI chooses questions that are expected to reduce uncertainty or clarify pressure points.

Examples:

- If classification probabilities are close, ambiguity pressure encourages more probing.
- If the deception trait is uncertain, deception-discriminating questions become more valuable.
- If the player protects sibling-related facts, questions with `pressure_on_interests=("protect_sibling",)` become more attractive.
- If the player directly contradicts an earlier claim, contradiction probes become more attractive.
- If a fact is already exposed, repeated probes on that fact become less attractive.
- If the neural model predicts `probe_protected_fact`, relevant authored questions receive a small alignment boost.

This means the hearing AI is not following a fixed script. It is navigating an authored question bank according to belief uncertainty, story pressure, and neural probe intent.

## Limitations

The neural probe intent currently has a small weight relative to trait uncertainty, pressure, ambiguity, and coverage. This is deliberate: it keeps the authored selector stable and prevents the neural head from producing incoherent question order.

Fact conflicts are not directly represented as a separate selector scoring term. They influence beliefs immediately and can indirectly affect future question choice through the claims ledger and relevant authored metadata.

The selector is deterministic in `EngineStyleScene`; stochastic tie selection exists in the standalone selector function but is not currently used by the playable scene.
