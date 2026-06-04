# Training And Evaluation Workflow

This document describes the current data-generation, model-training, and evaluation workflow for the Citizen hearing demo.

The implementation is based on:

- `generate_training_examples.py`
- `generate_human_training_examples.py`
- `tools/collate_human_archetype_data.py`
- `train_from_jsonl.py`
- `pc_jpc_tensorflow_npc_demo.py`
- `test_playthrough_profiles.py`
- `tools/scene_balance_audit.py`
- `tools/narrative_audit.py`
- `make_text_dialogue_graph.py`

## Data Types

The training pipeline uses semantic JSONL rows generated from the authored scene. These rows do not contain free-form hidden reasoning. They contain the authored question, authored player options, selected choice, metadata, story state, and model trace.

Current canonical training files are:

```text
data/training/auto_train_story.jsonl
data/training/human_train_all_archetypes.jsonl
```

The model is trained from these JSONL files by `train_from_jsonl.py`.

## Generated Auto JSONL Data

`generate_training_examples.py` produces auto-generated story-aware playthrough rows.

Important functions:

- `generate_episode(...)`: runs one authored scene episode and collects turn rows.
- `main()`: parses CLI arguments and writes JSONL.

Typical command:

```bash
python3 generate_training_examples.py \
  --episodes 40 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/training/auto_train_story.jsonl
```

Relevant options:

```text
--episodes     number of generated episodes
--max-turns    maximum turns per episode
--train-steps  synthetic model warmup steps per episode controller; use 0 to skip
--output       output JSONL path
--seed         base random seed
```

Rows include fields such as:

```text
question
state_before
player_options
player_choice
player_choice_metadata
model_trace
state_after
ending_reason
```

`model_trace` should contain the current two-head trace fields, including:

```text
raw_features
jpc_latent
raw_delta_alpha
raw_delta_beta
delta_alpha
delta_beta
question_probe_logits
predicted_question_probe_intent
```

## Human-Style Archetype JSONL Data

`generate_human_training_examples.py` can be used interactively or non-interactively.

Interactive collection writes choices made by a human player:

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/human_playthroughs/custom/human_train.jsonl
```

Archetype generation uses the `--profile` option and controlled stochasticity:

```bash
python3 generate_human_training_examples.py \
  --episodes 10 \
  --max-turns 14 \
  --train-steps 0 \
  --profile quiet_reformer \
  --profile-temperature 1.5 \
  --profile-top-margin 5.0 \
  --output data/human_playthroughs/quiet_reformer/human_train.jsonl
```

Relevant options:

```text
--profile                 optional archetype profile id
--deterministic-profile   always choose the highest-scoring profile option
--profile-temperature     softmax temperature for stochastic option selection
--profile-top-margin      only sample options near the best archetype score
--append                  append to existing output
```

Human-style archetype source files live under:

```text
data/human_playthroughs/<archetype>/human_train.jsonl
```

Current archetype profiles used in the main collation command include:

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

## Human Data Collation

`tools/collate_human_archetype_data.py` combines per-archetype files into one training JSONL.

Important functions:

- `collate(input_root, output, profiles)`: reads each profile file, adds profile labels, and writes combined rows.
- `strip_deprecated_policy_fields(row)`: sanitizes stale fields from older source rows before writing the training file.

Collation command:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl \
  --profiles cautious_survivor compliant_loyalist deceptive_appeaser empathetic_reformer fearful_dissident honest_dissident opportunistic_appeaser performative_loyalist quiet_reformer truthful_noncompliant
```

The collator currently removes stale compatibility fields from older human source files before writing the canonical training file. This means the training file can be clean even if some source playthrough files were produced before the current schema.

To audit the canonical training files:

```bash
grep -n "hearing_ai_action\|policy_logits\|chosen_action\|action_logits" \
  data/training/auto_train_story.jsonl \
  data/training/human_train_all_archetypes.jsonl
```

No matches should appear in the canonical training files.

## Two-Head Model Training

The current neural controller is defined in `pc_jpc_tensorflow_npc_demo.py`.

It combines:

- a JPC/JAX predictive-coding encoder,
- a TensorFlow/Keras belief delta head,
- a TensorFlow/Keras question probe intent head.

`TensorFlowHearingAIHeads` outputs:

```text
belief_raw_delta
question_probe_logits
```

Current saved model metadata uses:

```text
schema_version: 3
tf_output_heads: ["belief_raw_delta", "question_probe_logits"]
```

Old three-output checkpoints must be retrained.

## Training Script

`train_from_jsonl.py` trains from auto and/or human JSONL.

Important functions:

- `train_from_jsonl(...)`: performs JSONL epochs and returns aggregate metrics.
- `main()`: handles synthetic warmup, JSONL loading, oversampling, saving, and final reporting.

Training metrics are:

```text
total
belief_mse
probe_ce
probe_acc
```

`total` is the sum of belief loss and probe loss. `belief_mse` measures belief delta prediction error. `probe_ce` is cross-entropy for question probe intent. `probe_acc` is probe intent accuracy against the teacher intent.

## Current Model Directories

The current model set is:

```text
models/demo_npc_story_auto
models/demo_npc_story_human_only
models/demo_npc_story_human_mixed
```

Each model directory contains:

```text
tf_heads.weights.h5
jpc_encoder.eqx
meta.json
```

## Training Commands

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

Verify model metadata:

```bash
python3 - <<'PY'
import json
from pathlib import Path
for model_dir in [
    Path('models/demo_npc_story_auto'),
    Path('models/demo_npc_story_human_only'),
    Path('models/demo_npc_story_human_mixed'),
]:
    meta = json.loads((model_dir / 'meta.json').read_text(encoding='utf-8'))
    print(model_dir, meta.get('schema_version'), meta.get('tf_output_heads'))
PY
```

Expected output shape:

```text
3 ['belief_raw_delta', 'question_probe_logits']
```

## Deterministic Profile Reports

`test_playthrough_profiles.py` runs deterministic profile playthroughs and verifies expected classifications and flags.

Important functions:

- `run_profile(...)`: runs one profile through the scene.
- `write_reports(...)`: writes JSONL and Markdown reports.
- `main()`: loads a model, runs all profiles, and prints pass/fail summaries.

Run the three current report sets:

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

Each output directory contains:

```text
profile_playthroughs.jsonl
profile_playthroughs.md
```

Reports include:

- expected classification,
- actual classification,
- confidence,
- flags,
- citizen model values,
- classification distribution,
- story metrics,
- per-turn claims/protects/exposes,
- preferred neural probe,
- selected next question,
- selector reason and score.

## Aggregate Playtest Summary

The compact cross-model summary lives at:

```text
playtest_logs/playtest_audit_summary.md
playtest_logs/playtest_audit_summary.json
```

It summarizes each model's profile count, pass/fail count, average confidence, average story metrics, classification counts, flag counts, and cross-model classification differences.

If this summary is regenerated manually, it should read from:

```text
playtest_logs/story_auto_profiles/profile_playthroughs.jsonl
playtest_logs/story_human_only_profiles/profile_playthroughs.jsonl
playtest_logs/story_human_mixed_profiles/profile_playthroughs.jsonl
```

## Scene Balance Audit

`tools/scene_balance_audit.py` checks authored scene structure and choice metadata balance.

Run:

```bash
python3 tools/scene_balance_audit.py
```

Output:

```text
audit_scene_balance.md
```

The audit reports:

- node count,
- playable node count,
- choice count,
- average trust/suspicion deltas,
- missing `discriminates` metadata,
- choice count issues,
- duplicate choice issues,
- pressure distribution,
- semantic tag coverage.

## Narrative Audit

`tools/narrative_audit.py` checks broader narrative flow, state logic, repetition, active-inference plausibility, coverage, and optional training-data statistics.

Run:

```bash
python3 tools/narrative_audit.py \
  --episodes 60 \
  --max-turns 14 \
  --seed 2026 \
  --report audit_report.md \
  --training-jsonl data/training/human_train_all_archetypes.jsonl
```

Output:

```text
audit_report.md
```

## Dialogue Graph And YAML Regeneration

Export the authored scene YAML:

```bash
python3 tools/export_scene_yaml.py
```

Output:

```text
data/scenes/citizen_appeal_hearing.yaml
```

Regenerate the text dialogue graph:

```bash
python3 make_text_dialogue_graph.py
```

Outputs:

```text
text_dialogue_graph.md
text_dialogue_graph.txt
```

The dialogue graph is useful for inspecting authored question nodes, choices, story metadata, discriminates metadata, and fact-probe annotations without running the game.

## Manual Playtest Command

To play the current mixed model interactively:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model \
  --interactive
```

For selector and network trace output:

```bash
python3 pc_jpc_tensorflow_npc_demo.py \
  --model-dir models/demo_npc_story_human_mixed \
  --load-model \
  --interactive \
  --debug-trace
```

## Recommended Command Sequence After Gameplay Or Model Changes

After changing authored questions, choice metadata, story mechanics, or model training code, run this sequence.

Compile changed code:

```bash
python3 -m py_compile \
  pc_jpc_tensorflow_npc_demo.py \
  engine_style_scene.py \
  train_from_jsonl.py \
  generate_training_examples.py \
  generate_human_training_examples.py \
  test_playthrough_profiles.py
```

Regenerate auto training data:

```bash
python3 generate_training_examples.py \
  --episodes 40 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/training/auto_train_story.jsonl
```

Collate human-style data:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl \
  --profiles cautious_survivor compliant_loyalist deceptive_appeaser empathetic_reformer fearful_dissident honest_dissident opportunistic_appeaser performative_loyalist quiet_reformer truthful_noncompliant
```

Retrain models:

```bash
python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_story.jsonl \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_auto

python3 train_from_jsonl.py \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 1 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_human_only

python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_story.jsonl \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 3 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_story_human_mixed
```

Regenerate deterministic profile reports:

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

Regenerate audits and exports:

```bash
python3 tools/export_scene_yaml.py
python3 tools/scene_balance_audit.py
python3 tools/narrative_audit.py \
  --episodes 60 \
  --max-turns 14 \
  --seed 2026 \
  --report audit_report.md \
  --training-jsonl data/training/human_train_all_archetypes.jsonl
python3 make_text_dialogue_graph.py
```

Finally, inspect:

```bash
ls -lh \
  data/training/auto_train_story.jsonl \
  data/training/human_train_all_archetypes.jsonl \
  models/demo_npc_story_auto \
  models/demo_npc_story_human_only \
  models/demo_npc_story_human_mixed \
  playtest_logs/playtest_audit_summary.md \
  audit_report.md \
  audit_scene_balance.md
```
