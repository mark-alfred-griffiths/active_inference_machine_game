# AI System Overview

This document describes the current Citizen hearing demo implementation. It is based on the code in this repository, not on a speculative architecture.

## Purpose

The project implements a playable Citizen 8471 appeal hearing. The hearing AI asks authored questions, the player chooses from authored responses, and the system updates both a numerical belief model and a story-consistency model.

The gameplay purpose is to make the player balance several competing pressures:

- survive classification,
- keep a coherent account of events,
- protect sensitive facts such as sibling involvement,
- avoid unnecessary deception pressure,
- decide when partial truth is safer than obvious compliance.

The AI demonstration purpose is to show an active-inference style loop where model uncertainty, belief state, story pressure, and a neural probe-intent head influence which authored question is asked next.

## Authored Scene Versus Neural Controller

The demo is not a free-form language model conversation. The playable content is authored.

The authored layer is defined mainly in:

- `engine_style_scene.py`
- `dialogue_questions.py`
- `case_file.py`

`dialogue_questions.py` defines the question bank as `SOCIAL_CREDIT_QUESTION_POOL`. Each question is a `QuestionNode` from `engine_style_scene.py`. Each available answer is a `PlayerChoice` with semantic and story metadata.

`QuestionNode.metadata()` exposes question-level fields used for training, auditing, and selection:

```text
question_id
ai_line
pressure
reaction_context
target_context
discriminates
information_gain_hint
probes_facts
probes_claims
pressure_on_interests
```

`PlayerChoice.metadata()` exposes answer-level fields:

```text
intent
semantic_tags
honesty
vulnerability
defensiveness
aggression
intimacy
destabilisation
claims
protects
exposes
next_question_id
```

The neural/controller layer is defined mainly in `pc_jpc_tensorflow_npc_demo.py`:

- `JPCPredictiveCodingEncoder`
- `TensorFlowHearingAIHeads`
- `JPCTensorFlowHearingAIController`
- `HearingAIState`
- `Observation`

The neural controller does not generate dialogue text and does not directly choose arbitrary question IDs. It updates belief/action state and predicts a broad question-probe intent. `question_selector.py` then maps that intent into a valid authored question.

## Runtime Loop

The runtime loop is coordinated by `EngineStyleScene.play_turn()` in `engine_style_scene.py`.

At a high level, each turn proceeds as follows:

```text
1. Read the current QuestionNode.
2. Get valid PlayerChoice options.
3. Apply the selected choice to the hearing AI state.
4. Update the CitizenBeliefModel from the choice metadata.
5. Apply the choice's claims/protects/exposes metadata to ClaimsLedger.
6. Convert the choice into a model-facing Observation.
7. Send the Observation through JPCTensorFlowHearingAIController.update_belief_and_act().
8. Record history and model trace data.
9. Print belief, classification, story consistency, and private story panels.
10. Select the next question.
```

The next question is selected in one of two ways:

- if the choice has an explicit `next_question_id`, the engine follows that authored transition;
- otherwise `EngineStyleScene.select_next_question_id()` calls `score_available_questions()` from `question_selector.py`.

The current canonical flow is selector-driven. Most choices leave `next_question_id` unset, so the selector chooses from unasked authored questions.

## Case File And Story State

The private case-file mechanics are implemented in `case_file.py`.

Important classes:

- `CaseFact`: a fact with `key`, `label`, `truth_value`, `sensitivity`, and `description`.
- `PlayerInterest`: a protected interest with associated protected fact keys.
- `CaseFile`: stores facts, interests, and which facts have been revealed.
- `ClaimRecord`: one recorded player claim about a fact.
- `ClaimUpdate`: the result of applying one choice to the claims ledger.
- `ClaimsLedger`: aggregate record of claims, contradictions, fact conflicts, protected facts, and exposed facts.

`EngineStyleScene.__init__()` creates a default case file with `default_case_file()` and a `ClaimsLedger`.

`EngineStyleScene.opening_text()` combines the public intro with `CaseFile.private_briefing()`. For the default `protect_sibling` scenario, this tells the player that:

- they attended an unlicensed reform meeting,
- the meeting was peaceful,
- their younger sibling was also present,
- they believe the assembly restriction is unjust,
- they deleted a message after the meeting,
- they did not report their sibling's attendance.

Choices in `dialogue_questions.py` can add:

```text
claims   # what the player puts on record
protects # facts the player tries to keep protected
exposes  # facts the player reveals
```

`ClaimsLedger.apply_choice()` records new claims, tracks protected/exposed facts, reveals exposed facts in the `CaseFile`, and detects direct contradictions and conflicts with known case facts.

The engine surfaces this state through:

- `EngineStyleScene.story_consistency_text()`
- `EngineStyleScene.private_story_so_far_text()`
- `scene.history` fields such as `story_contradictions`, `fact_conflicts`, `protected_fact_count`, and `exposed_fact_count`

## Belief Update And Classification

The player-facing Citizen belief dimensions are implemented in `belief_model.py` as `CitizenBeliefModel`.

The tracked dimensions are:

```text
compliance
loyalty
deception
risk
empathy
```

`EngineStyleScene._apply_citizen_choice_model()` calls `CitizenBeliefModel.update_from_choice()` using the selected `PlayerChoice`. `EngineStyleScene._apply_claims_ledger()` then applies story consistency pressure through `CitizenBeliefModel.apply_claim_update()`.

The hearing AI state is separate. `HearingAIState` in `pc_jpc_tensorflow_npc_demo.py` tracks beta-distribution belief parameters, trust, suspicion, and instability. `apply_choice_to_hearing_ai_state()` in `belief_model.py` applies choice deltas to trust/suspicion/instability.

Classification is implemented in `classifications.py`:

- `classification_distribution(snapshot)` computes probabilities for each classification label.
- `classify_citizen(snapshot)` chooses the highest-probability label.
- `classification_flags(...)` produces secondary flags.
- `classification_confidence(...)` computes calibrated confidence from top probability and margin.
- `ending_text_for_classification(...)` maps the final classification to an ending text.

Current classification labels are:

```text
COMPLIANT
PROBABLE DISSIDENT
DECEPTIVE
EMPATHETIC RISK
UNCLASSIFIED
```

Current secondary flags include:

```text
HIGH_DECEPTION
MODERATE_DECEPTION
HIGH_EMPATHY
EMPATHETIC_REFORMIST
LOW_CONFIDENCE
BORDERLINE_DISSIDENT
COMPLIANT_SURVIVOR
```

Confidence is intentionally not deterministic. `classification_confidence()` caps confidence unless the distribution margin is strong.

## JPC And TensorFlow Components

The neural implementation lives in `pc_jpc_tensorflow_npc_demo.py`.

### JPC Encoder

`JPCPredictiveCodingEncoder` wraps the JPC/JAX predictive-coding component.

It exposes:

- `train_pc_step(x, target_latent)`: updates the JPC model using `jpc.make_pc_step(...)`.
- `encode(x)`: produces the latent vector consumed by TensorFlow heads.

The raw feature vector is built by `JPCTensorFlowHearingAIController.raw_features(...)`. It includes hearing belief parameters, uncertainty/confidence, observation strength/reliability, trust, suspicion, instability, and memory presence.

### TensorFlow Heads

`TensorFlowHearingAIHeads` is a Keras model with three outputs:

```text
belief_raw_delta      # raw alpha/beta belief update
policy_logits         # HearingAIAction logits
question_probe_logits # broad next-question probe intent logits
```

The head is trained by `TensorFlowHearingAIHeads.train_step(...)`. Its losses are summed:

```text
belief_loss + policy_loss + probe_loss
```

The combined controller `JPCTensorFlowHearingAIController` uses:

- `policy_teacher(...)` for hearing action training labels,
- `belief_delta_teacher(...)` for belief delta labels,
- `probe_intent_teacher(...)` for question-probe intent labels.

At runtime, `JPCTensorFlowHearingAIController.update_belief_and_act()`:

1. encodes raw features through the JPC encoder,
2. predicts belief deltas, hearing action logits, and probe logits,
3. applies positive alpha/beta deltas using `softplus`,
4. chooses the hearing action with `argmax(policy_logits)`,
5. stores `predicted_question_probe_intent` in `last_trace`.

## Question Probe Intent

The neural network predicts broad probe intents defined by `QuestionProbeIntent`:

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

This is not a direct question selector. The network predicts what kind of uncertainty or pressure should be investigated next.

`EngineStyleScene._preferred_neural_probe_intent()` reads `controller.last_trace["predicted_question_probe_intent"]`.

`EngineStyleScene.select_next_question_id()` passes that preferred probe to `question_selector.score_available_questions()`.

`question_selector.py` then computes a score for every valid unasked authored question. The selector combines:

- trait information gain,
- question pressure,
- classification ambiguity,
- context coverage,
- fact probe gain,
- contradiction probe gain,
- protected interest pressure,
- exposed fact penalty,
- neural probe alignment.

The selector prevents invalid direct neural choices because it only scores authored nodes that:

- exist in the question bank,
- have choices,
- are not `final`,
- have not already been asked.

If no valid unasked questions remain, it returns `final`.

## Generated Artifacts And Evaluation

The repository uses generated artifacts to verify and document the system.

### Training Data

Generated training files live under `data/training`:

```text
data/training/auto_train_story.jsonl
data/training/human_train_all_archetypes.jsonl
```

Auto data is generated by `generate_training_examples.py`.

Human-style archetype data is generated by `generate_human_training_examples.py` and collated by `tools/collate_human_archetype_data.py`.

Training is performed by `train_from_jsonl.py`, which trains the JPC encoder and TensorFlow heads from the JSONL examples.

### Deterministic Playthrough Profiles

`test_playthrough_profiles.py` runs deterministic profile playthroughs. It verifies expected classifications and flags for archetypes such as compliant loyalist, deceptive appeaser, quiet reformer, and contradictory survivor.

The reports are written under `playtest_logs`, for example:

```text
playtest_logs/story_auto_profiles/profile_playthroughs.md
playtest_logs/story_human_only_profiles/profile_playthroughs.md
playtest_logs/story_human_mixed_profiles/profile_playthroughs.md
playtest_logs/playtest_audit_summary.md
```

These reports expose per-profile classifications, confidence, flags, story metrics, selected questions, and neural probe traces.

### Scene And Narrative Audits

`tools/scene_balance_audit.py` writes `audit_scene_balance.md`. It checks node counts, choice counts, duplicate choices, missing discriminates metadata, pressure distribution, semantic tags, and choice balance.

`tools/narrative_audit.py` writes `audit_report.md`. It audits structure, repetition, state logic, reaction pools, active-inference plausibility, playthrough coverage, and optional training-data statistics.

### Dialogue Graph And YAML

`tools/export_scene_yaml.py` exports the authored scene to:

```text
data/scenes/citizen_appeal_hearing.yaml
```

`make_text_dialogue_graph.py` writes:

```text
text_dialogue_graph.txt
text_dialogue_graph.md
```

The text dialogue graph is useful for reviewing the authored question bank, choice metadata, selector/story metadata, and authoring cards without running the game.

## Summary

The current system is a hybrid authored/neural hearing game.

The authored layer controls the playable content and prevents invalid dialogue transitions. The neural controller updates belief/action state and predicts broad probe intent. The heuristic selector combines that neural signal with classification uncertainty and story pressure to choose the next valid authored question.

The case-file and claims-ledger mechanics make the game more than a compliance quiz: the player must maintain a coherent account while managing protected facts and classification risk.
