# JPC + TensorFlow Hearing AI Demo — Engine-Style Version

This project is the streamlined **engine-design** version of the Hearing AI demo.

The older basic `scene.py` implementation has been removed. The playable flow now uses `engine_style_scene.py`, where every Hearing AI question owns its exact hard-coded response menu.

The machine-learning model still runs underneath the authored engine flow:

```text
Hearing AI question node
        ↓
hard-coded player response menu
        ↓
semantic metadata attached to chosen response
        ↓
numerical observation generated for the model
        ↓
JPC predictive-coding encoder
        ↓
TensorFlow belief-update and policy heads
        ↓
updated Hearing AI belief, uncertainty, free energy, and action pressure
        ↓
engine advances to the next authored question node
```

---

## Files

```text
pc_jpc_tensorflow_npc_demo.py      # Main runnable demo
engine_style_scene.py              # Canonical engine-style authored scene tree
dialogue.py                        # Hearing AI response line variation by action tier
generate_training_examples.py      # Auto-generate semantic JSONL from engine flow
generate_human_training_examples.py# Collect human semantic JSONL from engine flow
README.md                          # This file
```

There is intentionally **no `scene.py`** in this version.

---

## Main Design Change

The project no longer uses a generic scene object with a loose list of choices.

Instead, it uses an engine-style authored tree:

```text
QuestionNode
  ├── Hearing AI line
  ├── pressure value
  └── exact PlayerChoice options
          ├── player-facing text
          ├── semantic tags
          ├── honesty / vulnerability / defensiveness / aggression
          ├── trust / suspicion / instability deltas
          └── next_question_id
```

This makes the game feel more coherent because Hearing AI is always asking a specific question, and the available choices are authored specifically for that question.

---

## Run the Demo

Install dependencies:

```bash
pip install tensorflow equinox optax "jax[cpu]"
pip install git+https://github.com/thebuckleylab/jpc.git
```

Run the deterministic demo:

```bash
python pc_jpc_tensorflow_npc_demo.py
```

Run interactively:

```bash
python pc_jpc_tensorflow_npc_demo.py --interactive
```

Optional shorter training run for quick testing:

```bash
python pc_jpc_tensorflow_npc_demo.py --train-steps 100 --interactive
```

### Save/load trained network checkpoints

The demo now automatically tries to load a trained network from `models/demo_npc`.
If no checkpoint exists, it trains, prints loss/accuracy metrics, and saves a new checkpoint.

Train from scratch and overwrite checkpoint:

```bash
python pc_jpc_tensorflow_npc_demo.py --fresh-train --train-steps 700
```

Load the previously trained checkpoint for interactive play:

```bash
python pc_jpc_tensorflow_npc_demo.py --interactive
```

Load/save from a custom checkpoint directory:

```bash
python pc_jpc_tensorflow_npc_demo.py --model-dir models/alice_v2 --interactive
```

Disable saving after a scratch run:

```bash
python pc_jpc_tensorflow_npc_demo.py --fresh-train --no-save-model
```

Training output includes model performance at the end of training (running `total`, `belief_mse`, `policy_ce`, and `policy_acc`).

### Train from JSONL and then load in the demo

Save a checkpoint from JSONL training:

```bash
python train_from_jsonl.py --synthetic-steps 300 --epochs 4 --save-model --model-dir models/demo_npc
```

Then run demo using that trained network:

```bash
python pc_jpc_tensorflow_npc_demo.py --model-dir models/demo_npc --interactive
```

---

## Data + Training + Run Workflow (Synthetic / Human / Both)

This section is the end-to-end recipe for:

1. creating synthetic data,
2. creating human data,
3. training on synthetic only, human only, or both,
4. loading the trained model in the demo game.

### 1) Create synthetic training data (auto-generated)

```bash
python generate_training_examples.py --episodes 20 --max-turns 14 --output data/auto_train.jsonl
```

Useful flags:

- `--episodes`: number of generated episodes.
- `--max-turns`: max turns per episode.
- `--train-steps`: synthetic warmup used by the generator's internal controller (`0` disables).
- `--seed`: reproducible generation.

### 2) Create human training data (interactive playthrough)

```bash
python generate_human_training_examples.py --episodes 3 --max-turns 14 --append --output data/human_train.jsonl
```

Useful flags:

- `--append`: add to existing file instead of overwrite.
- `--episodes`: number of human sessions.
- `--max-turns`: max turns per session.
- `--train-steps`: warmup for the model before each session (`0` disables).

### 3) Train a model from JSONL

Train script:

```bash
python train_from_jsonl.py [options]
```

By default, the script reads both:

- `data/auto_train.jsonl`
- `data/human_train.jsonl`

and trains on a combined set (`auto + human * human_weight`).

#### Train on **both** synthetic + human data

```bash
python train_from_jsonl.py \
  --auto-jsonl data/auto_train.jsonl \
  --human-jsonl data/human_train.jsonl \
  --human-weight 3 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc
```

#### Train on **synthetic only**

```bash
python train_from_jsonl.py \
  --auto-jsonl data/auto_train.jsonl \
  --human-jsonl data/empty.jsonl \
  --human-weight 1 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_synth
```

#### Train on **human only**

```bash
python train_from_jsonl.py \
  --auto-jsonl data/empty.jsonl \
  --human-jsonl data/human_train.jsonl \
  --human-weight 1 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_human
```

Notes:

- `data/empty.jsonl` can be a non-existent path; missing files are treated as zero rows.
- `--load-existing` lets you continue training from a prior checkpoint in `--model-dir`.
- training prints performance metrics: `total`, `belief_mse`, `policy_ce`, `policy_acc`.

### 4) Load trained model and run the demo game

The demo auto-loads from `models/demo_npc` (or your `--model-dir`) if checkpoint files exist.

Run interactively with trained model:

```bash
python pc_jpc_tensorflow_npc_demo.py --interactive --model-dir models/demo_npc
```

Run deterministic demo with trained model:

```bash
python pc_jpc_tensorflow_npc_demo.py --model-dir models/demo_npc
```

Force fresh training (ignore checkpoint):

```bash
python pc_jpc_tensorflow_npc_demo.py --fresh-train --train-steps 700 --model-dir models/demo_npc
```

Train fresh but do not persist:

```bash
python pc_jpc_tensorflow_npc_demo.py --fresh-train --no-save-model
```

Checkpoint files saved in `--model-dir`:

- `tf_heads.weights.h5`
- `jpc_encoder.eqx`
- `meta.json`

---

## Why the Engine Design Is Now Canonical

The basic scene version was useful as a sandbox, but it made the playable experience feel less coherent because choices were drawn from a broad generic menu.

The engine version is better because:

- every Hearing AI prompt has its own authored response menu,
- state transitions are explicit through `next_question_id`,
- drug states, suspicion, trust, instability, contradictions, and belief updates remain persistent,
- the PC/JPC + TensorFlow model still receives structured observations,
- semantic labels are preserved for JSONL training rather than shown as gameplay text.

---

## Core ML Components

The model in `pc_jpc_tensorflow_npc_demo.py` contains:

- `JPCPredictiveCodingEncoder`: actual JPC/JAX predictive-coding encoder,
- `TensorFlowHearingAIHeads`: TensorFlow belief-update and policy heads,
- `JPCTensorFlowHearingAIController`: combined controller used by the engine scene.

The older `TensorFlowNPCHeads` and `JPCTensorFlowNPCController` names remain as backward compatibility aliases.

The engine scene in `engine_style_scene.py` supplies the authored context and converts player choices into model-facing observations.

---

## Suspicion as Tone, Not Game Over

The engine-style scene now treats Hearing AI's suspicion as a tonal pressure variable rather than an early fail state.

Low suspicion makes Hearing AI more curious. Medium suspicion makes her guarded and testing. High suspicion makes her sharper, more hostile, and more likely to accuse the player of evasion.

This means defensive choices still matter, but they no longer kill the scene before the acid/LSD branch. Suspicion now changes Hearing AI's wording while the authored question route continues.

Run normal gameplay:

```bash
python pc_jpc_tensorflow_npc_demo.py --interactive
```

Run with model/debug trace:

```bash
python pc_jpc_tensorflow_npc_demo.py --interactive --debug-trace
```
