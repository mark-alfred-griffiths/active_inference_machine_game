# Citizen Hearing AI Demo

This project is an engine-style active-inference dialogue demo.

The player is Citizen 8471 in an appeal hearing. A hearing AI asks authored questions, tracks belief and story consistency, and selects the next question using a combination of neural probe intent and heuristic active inference over the current story state.

The demo is not a free-form chatbot. It is a playable authored interrogation system where every player answer is an authored choice with semantic, belief, and story metadata.

```text
Authored question node
        ↓
Authored player response menu
        ↓
Choice metadata: traits, claims, protects, exposes
        ↓
Claims ledger + case-file story state
        ↓
Citizen belief model update
        ↓
JPC encoder + TensorFlow heads
        ↓
Neural hearing action + question probe intent
        ↓
Heuristic selector chooses the next valid authored question
        ↓
Classification, flags, survival outcome
```

---

## Core Files

```text
pc_jpc_tensorflow_npc_demo.py       # Main runnable demo and TensorFlow/JPC controller
engine_style_scene.py               # Canonical playable scene engine
dialogue_questions.py               # Authored Citizen hearing question bank and choices
case_file.py                        # Case facts, protected interests, claims ledger
belief_model.py                     # Citizen belief-state updates
classifications.py                  # Classification, flags, calibrated confidence
question_selector.py                # Active-inference/story-state question selector
terminal_theme.py                   # Optional terminal colour and value heat styling
train_from_jsonl.py                 # Train model heads from JSONL data
generate_training_examples.py       # Generate auto training data
generate_human_training_examples.py # Generate interactive or archetype human-style data
test_playthrough_profiles.py        # Deterministic profile regression tests
make_text_dialogue_graph.py         # Export text dialogue graph documentation
```

There is intentionally no generic `scene.py` flow in the current design.

---

## Current Gameplay Design

The current scene is selector-driven rather than fixed-route.

Most choices do not define a hard-coded `next_question_id`. After each answer, the engine asks `question_selector.py` to select the highest-value unasked question from the authored pool.

Selection combines:

- classification ambiguity,
- trait uncertainty,
- authored information-gain hints,
- question pressure,
- repeated-context penalties,
- story-state pressure,
- unresolved sensitive facts,
- protected interests,
- contradictions and fact conflicts,
- neural probe intent from the TensorFlow head.

The neural network does not directly pick arbitrary question IDs. It predicts a probe intent such as `probe_deception`, `probe_protected_fact`, or `probe_contradiction`. The heuristic selector then maps that intent onto a valid authored question and prevents invalid or repeated questions.

---

## Case File And Story Consistency

The player receives a private opening briefing before the hearing begins. This establishes concrete facts and interests, for example protecting a sibling, explaining a deleted message, and avoiding a false violence label.

The current case-file system lives in `case_file.py`.

It tracks:

- `CaseFact`: factual truth, sensitivity, description,
- `PlayerInterest`: what the player is trying to protect,
- `CaseFile`: facts, interests, revealed facts,
- `ClaimsLedger`: what the player has claimed so far.

Choices can contain story metadata:

```text
claims   # fact/value statements placed on record
protects # facts the player is trying not to expose
exposes  # facts the player reveals
```

The claims ledger detects:

- new claims,
- direct contradictions,
- fact conflicts,
- protected fact pressure,
- exposed sensitive facts.

Contradiction logic is intentionally softened. Conditional, private, procedural, protected, partial, unknown, and similar values are treated as ambiguous refinements unless they directly conflict with explicit `true`/`false` claims.

During play, the engine shows a private `PRIVATE STORY SO FAR` panel so the player can understand what they are protecting, what they have exposed, and whether their story is under pressure.

---

## Classification And Belief Model

The Citizen belief model tracks:

```text
compliance
loyalty
deception
risk
empathy
```

Classification labels include:

```text
COMPLIANT
PROBABLE DISSIDENT
DECEPTIVE
EMPATHETIC RISK
UNCLASSIFIED
```

Secondary flags include conditions such as high deception, high empathy, borderline dissident pressure, compliant survivor behavior, and low confidence.

Confidence is calibrated rather than deterministic. Profile runs should not automatically return confidence `1.0`; confidence depends on classification distribution and margin strength.

Empathy is separated from ordinary compliance and loyalty. Generic safe answers should not automatically max out empathy. Empathy rises mainly from compassion, reform, protective, and humane choices.

---

## Run The Demo

Install dependencies:

```bash
pip install tensorflow equinox optax "jax[cpu]"
pip install git+https://github.com/thebuckleylab/jpc.git
```

Run with the current human-mixed model:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --interactive \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model
```

Run with debug trace:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --interactive \
  --debug-trace \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model
```

Force colour output:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --interactive \
  --color always \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model
```

Disable colour:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --interactive \
  --color never \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model
```

Preview the terminal theme:

```bash
python3 terminal_theme.py
```

---

## Training Data Layout

Current training files live under `data/training`:

```text
data/training/auto_train_story.jsonl          # Auto-generated story-aware data
data/training/human_train_all_archetypes.jsonl # Collated human-style archetype data
```

Human-style archetype source files live under:

```text
data/human_playthroughs/<archetype>/human_train.jsonl
```

Current archetypes include:

```text
cautious_survivor
compliant_loyalist
deceptive_appeaser
empathetic_reformer
fearful_dissident
honest_dissident
opportunistic_appeaser
performative_loyalist
quiet_reformer
truthful_noncompliant
```

There may be old or contaminated files in historical folders. Do not train on files marked `contaminated`; use the collated master file above unless deliberately auditing old data.

---

## Generate Training Data

Regenerate auto training data:

```bash
python3 generate_training_examples.py \
  --episodes 40 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/training/auto_train_story.jsonl
```

Collate current human archetype data:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl \
  --profiles cautious_survivor compliant_loyalist deceptive_appeaser empathetic_reformer fearful_dissident honest_dissident opportunistic_appeaser performative_loyalist quiet_reformer truthful_noncompliant
```

Generate human-style examples for one archetype:

```bash
python3 generate_human_training_examples.py \
  --episodes 10 \
  --max-turns 14 \
  --train-steps 0 \
  --profile quiet_reformer \
  --output data/human_playthroughs/quiet_reformer/human_train.jsonl
```

Generate deterministic archetype examples for regression baselines:

```bash
python3 generate_human_training_examples.py \
  --episodes 10 \
  --max-turns 14 \
  --train-steps 0 \
  --profile quiet_reformer \
  --deterministic-profile \
  --output data/human_playthroughs/quiet_reformer/human_train.jsonl
```

---

## Controlled Stochasticity

Human-style generation now uses controlled stochasticity by default.

The archetype scorer ranks all authored options. The generator then samples only from plausible near-top options instead of always choosing the single highest-scoring option.

Useful flags:

```text
--profile-temperature  # higher means more variation among plausible choices
--profile-top-margin   # max score gap from the best option allowed into sampling
--deterministic-profile # always choose the best-scoring option
```

Current defaults:

```text
--profile-temperature 1.5
--profile-top-margin 5.0
```

This makes generated archetype data less repetitive without allowing random out-of-character choices.

---

## Train Models

Current recommended model variants:

```text
models/demo_npc_story_auto         # auto-generated data only
models/demo_npc_story_human_only   # human-style archetype data only
models/demo_npc_story_human_mixed  # auto + weighted human-style data
```

Train auto-only:

```bash
python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_story.jsonl \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_auto
```

Train human-only:

```bash
python3 train_from_jsonl.py \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 1 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_human_only
```

Train human-mixed:

```bash
python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_story.jsonl \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 3 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_human_mixed
```

Training metrics include:

```text
total
belief_mse
policy_ce
policy_acc
probe_ce
probe_acc
```

Checkpoint files saved in each model directory:

```text
tf_heads.weights.h5
jpc_encoder.eqx
meta.json
```

Old checkpoints that do not contain the question-probe intent head are incompatible with the current model architecture and should be retrained.

---

## Test And Playtest

Run deterministic profile tests for one model:

```bash
python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_story_human_mixed \
  --output-dir playtest_logs/story_human_mixed_profiles \
  --max-turns 20
```

Run the current three-model comparison manually:

```bash
python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_story_auto \
  --output-dir playtest_logs/story_auto_profiles \
  --max-turns 20

python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_story_human_only \
  --output-dir playtest_logs/story_human_only_profiles \
  --max-turns 20

python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_story_human_mixed \
  --output-dir playtest_logs/story_human_mixed_profiles \
  --max-turns 20
```

Current playtest reports are written under:

```text
playtest_logs/
```

A compact cross-model summary is kept at:

```text
playtest_logs/playtest_audit_summary.md
playtest_logs/playtest_audit_summary.json
```

---

## Regenerate Documentation And Audits

Export current scene YAML:

```bash
python3 tools/export_scene_yaml.py
```

Regenerate text dialogue graph:

```bash
python3 make_text_dialogue_graph.py
```

Outputs:

```text
text_dialogue_graph.txt
text_dialogue_graph.md
```

Run scene balance audit:

```bash
python3 tools/scene_balance_audit.py
```

Run narrative audit:

```bash
python3 tools/narrative_audit.py \
  --episodes 60 \
  --max-turns 14 \
  --seed 2026 \
  --report audit_report.md \
  --training-jsonl data/training/human_train_all_archetypes.jsonl
```

Current ancillary artifacts:

```text
data/scenes/citizen_appeal_hearing.yaml
audit_scene_balance.md
audit_report.md
text_dialogue_graph.txt
text_dialogue_graph.md
playtest_logs/playtest_audit_summary.md
```

---

## Generated Scene Metadata

`QuestionNode.metadata()` includes:

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

`PlayerChoice.metadata()` includes:

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

This metadata is used by training, auditing, deterministic profiles, and question selection.

---

## Practical Interpretation

The game is intended to be playable because the player has competing objectives:

- survive classification,
- avoid appearing deceptive,
- avoid being labelled dangerous,
- protect sensitive facts,
- expose enough truth to remain coherent,
- avoid contradicting earlier claims.

The AI concept demonstration remains intact because the neural network still participates in belief update, hearing action selection, and probe-intent prediction. The authored selector remains the safety layer that turns neural probe intent into valid playable questions.
