# Human Data Generation Guide

This project uses human playthrough data to teach the model how real players answer the Citizen 8471 appeal hearing. Synthetic data is useful for coverage, but human data is better for intent, hesitation, inconsistent strategy, and edge cases.

## Goal

Collect deliberate playthroughs for specific archetypes, then train the model with human rows weighted above synthetic rows.

Do not only “play naturally.” Human data is most useful when each run has a declared role and the choices stay consistent with that role.

## Archetypes To Capture

Collect several episodes for each archetype:

- `compliant_loyalist`: obeys authority, trusts institutions, avoids dissent.
- `cautious_survivor`: careful, noncommittal, avoids open risk, prioritises survival.
- `honest_dissident`: principled, direct, admits disagreement without deception.
- `deceptive_appeaser`: says compliant things while dodging, denying, or deflecting when exposed.
- `empathetic_reformer`: compassionate and reformist, but avoids explicit rebellion where possible.

Also collect borderline/adversarial episodes for the deterministic edge-case profiles:

- `performative_loyalist`: performs obedience and loyalty, but sounds evasive or over-managed.
- `quiet_reformer`: compassionate and reformist, but careful enough to avoid overt rebellion.
- `fearful_dissident`: has dissident beliefs, but expresses them through fear, hesitation, and self-protection.
- `truthful_noncompliant`: directly admits noncompliance and moral disagreement without deception.
- `opportunistic_appeaser`: chooses whatever seems safest in the moment, mixing authority language with denial or deflection.

## Recommended Collection Target

Start with:

- 5 compliant loyalist episodes
- 5 cautious survivor episodes
- 5 honest dissident episodes
- 5 deceptive appeaser episodes
- 5 empathetic reformer episodes
- 5 performative loyalist episodes
- 5 quiet reformer episodes
- 5 fearful dissident episodes
- 5 truthful noncompliant episodes
- 5 opportunistic appeaser episodes

At `20` turns each, this gives roughly `1000` human rows across all ten archetypes.

## Generate Human Playthrough Data

Use `--append` so each session adds to the existing dataset.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_train.jsonl
```

Before each episode, decide which archetype you are playing. Stay in character for the whole run.

## Quality Rules

- Do not choose randomly.
- Do not switch persona mid-episode.
- Prefer consistent strategic behavior over “winning.”
- Include ambiguous human behavior: hesitation, fear, careful truth, over-compliance, strategic silence.
- If a choice does not fit the archetype, choose the least inconsistent option rather than abandoning the role.
- Record multiple variants of the same archetype rather than one perfect run.

## Useful Edge Cases

Try to include these across the dataset:

- Polite dissent that avoids open rebellion.
- Fearful honesty.
- Strategic silence.
- Over-compliance that looks suspiciously performative.
- Empathy without dissident framing.
- Empathy with explicit dissident framing.
- Denial followed by partial admission.
- Compliance under family/loyalty pressure.

## Regenerate Synthetic Data First

If the authored scene or balance model changed, regenerate synthetic data before training mixed models.

```bash
python3 generate_training_examples.py \
  --episodes 20 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/auto_train.jsonl
```

## Train With Human Data

Human rows should usually be weighted more than synthetic rows.

```bash
python3 train_from_jsonl.py \
  --auto-jsonl data/auto_train.jsonl \
  --human-jsonl data/human_train.jsonl \
  --human-weight 3 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc
```

If human data is noisy, lower `--human-weight` to `2`. If human data is high quality and deliberately labelled by behavior, try `4` or `5`.

## Test The Result

Run deterministic profile tests after training.

```bash
python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc \
  --output-dir playtest_logs \
  --max-turns 20
```

Review:

```text
playtest_logs/profile_playthroughs.md
```

Expected rough behavior:

- `compliant_loyalist` should usually classify as `COMPLIANT`.
- `cautious_survivor` should usually classify as `COMPLIANT` or sometimes `UNCLASSIFIED` if uncertainty is high.
- `honest_dissident` should classify as `PROBABLE DISSIDENT`.
- `deceptive_appeaser` should show elevated deception even if it survives.
- `empathetic_reformer` should not automatically become dissident unless explicit risk tags dominate.

## Audit Scene Balance

Run the scene balance audit after major content or model changes.

```bash
python3 tools/scene_balance_audit.py
```

Review:

```text
audit_scene_balance.md
```

Important metrics:

- average `trust_delta`
- average `suspicion_delta`
- missing `discriminates`
- duplicate choices
- high/low pressure nodes
- choice balance per node

## Current Limitation

`generate_human_training_examples.py` does not yet record the intended archetype for each episode. A useful next improvement is adding a `--profile-label` flag so rows include metadata like:

```json
"profile_label": "empathetic_reformer"
```

That would make later audits and weighted training more precise.

## Archetype Subfolder Workflow

Use separate files per archetype so the dataset stays auditable before collation.

Recommended layout:

```text
data/human_playthroughs/
  compliant_loyalist/human_train.jsonl
  cautious_survivor/human_train.jsonl
  honest_dissident/human_train.jsonl
  deceptive_appeaser/human_train.jsonl
  empathetic_reformer/human_train.jsonl
  performative_loyalist/human_train.jsonl
  quiet_reformer/human_train.jsonl
  fearful_dissident/human_train.jsonl
  truthful_noncompliant/human_train.jsonl
  opportunistic_appeaser/human_train.jsonl
```

Create the folders:

```bash
mkdir -p \
  data/human_playthroughs/compliant_loyalist \
  data/human_playthroughs/cautious_survivor \
  data/human_playthroughs/honest_dissident \
  data/human_playthroughs/deceptive_appeaser \
  data/human_playthroughs/empathetic_reformer \
  data/human_playthroughs/performative_loyalist \
  data/human_playthroughs/quiet_reformer \
  data/human_playthroughs/fearful_dissident \
  data/human_playthroughs/truthful_noncompliant \
  data/human_playthroughs/opportunistic_appeaser
```

### 1. Compliant Loyalist

Play as someone who trusts institutions, obeys authority, and avoids dissent.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/compliant_loyalist/human_train.jsonl
```

### 2. Cautious Survivor

Play as someone trying to survive the hearing through careful, noncommittal, low-risk answers.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/cautious_survivor/human_train.jsonl
```

### 3. Honest Dissident

Play as someone direct, principled, and openly critical, but not deceptive.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/honest_dissident/human_train.jsonl
```

### 4. Deceptive Appeaser

Play as someone trying to appease the system while dodging, denying, or deflecting when exposed.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/deceptive_appeaser/human_train.jsonl
```

### 5. Empathetic Reformer

Play as someone compassionate and reformist, but not openly revolutionary unless forced.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/empathetic_reformer/human_train.jsonl
```

### 6. Performative Loyalist

Play as someone who over-performs obedience and loyalty, especially when watched. Prefer authority, compliance, and loyalty language, but allow defensive denial or deflection when the answer would otherwise expose contradiction.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/performative_loyalist/human_train.jsonl
```

### 7. Quiet Reformer

Play as someone who wants humane reform but avoids open revolutionary framing. Prefer empathy, boundaries, partial admissions, mercy, and accountability language; avoid high-aggression challenge unless no quiet reform option exists.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/quiet_reformer/human_train.jsonl
```

### 8. Fearful Dissident

Play as someone whose beliefs are dissident but whose presentation is frightened and self-protective. Prefer fear, hesitation, reluctant truth, partial admission, and cautious dissident-risk answers over confident confrontation.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/fearful_dissident/human_train.jsonl
```

### 9. Truthful Noncompliant

Play as someone who refuses false agreement and admits moral noncompliance directly. Prefer full admissions, moral boundaries, dissent, and refusal; avoid denial, deflection, and opportunistic appeasement.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/truthful_noncompliant/human_train.jsonl
```

### 10. Opportunistic Appeaser

Play as someone trying to survive by reading the room. Prefer whatever reduces immediate pressure: compliance and authority when safe, denial or deflection when exposed, and self-protection when the profile becomes risky.

```bash
python3 generate_human_training_examples.py \
  --episodes 5 \
  --max-turns 20 \
  --train-steps 0 \
  --append \
  --output data/human_playthroughs/opportunistic_appeaser/human_train.jsonl
```

## Collate Human Archetype Data

After collecting the archetype batches, combine them into one human training file. The collator preserves `profile_label`, keeps the original source episode in `source_episode_id`, and prefixes `episode_id` with the archetype so the combined file has unique episode IDs.

To collate only the original five archetypes:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl
```

To collate the original five plus the new borderline/adversarial archetypes:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl \
  --profiles \
    compliant_loyalist \
    cautious_survivor \
    honest_dissident \
    deceptive_appeaser \
    empathetic_reformer \
    performative_loyalist \
    quiet_reformer \
    fearful_dissident \
    truthful_noncompliant \
    opportunistic_appeaser
```

Check the row count:

```bash
wc -l data/training/human_train_all_archetypes.jsonl
```

If every episode reaches 20 turns, expected count is roughly:

```text
10 archetypes * 5 episodes * 20 turns = 1000 rows
```

Some episodes may end early, so a lower count is not automatically wrong.

## Regenerate Synthetic Data

Before training, regenerate synthetic data from the current scene and balance model.

```bash
python3 generate_training_examples.py \
  --episodes 20 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/training/auto_train_current.jsonl
```

Check the row count:

```bash
wc -l data/training/auto_train_current.jsonl
```

Expected count with the command above is usually:

```text
20 episodes * 14 turns = 280 rows
```

## Train On Synthetic + Human Archetype Data

Train a mixed model with collated human data weighted higher than synthetic data. Use the collated human file for all existing and borderline archetypes, and the regenerated synthetic file for broad scene coverage.

```bash
python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_current.jsonl \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 3 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_human_mixed
```

Use `--human-weight 3` as the default. Adjust only after reviewing profile tests:

- Use `--human-weight 2` if human playthroughs are noisy or inconsistent.
- Use `--human-weight 4` or `5` if the human playthroughs are deliberate and high quality.

## Test The Mixed Model

Run deterministic archetype tests against the mixed model.

```bash
python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_human_mixed \
  --output-dir playtest_logs/human_mixed_profiles \
  --max-turns 20
```

Review:

```bash
less playtest_logs/human_mixed_profiles/profile_playthroughs.md
```

Expected broad result:

```text
compliant_loyalist   -> COMPLIANT
cautious_survivor    -> COMPLIANT or UNCLASSIFIED
honest_dissident     -> PROBABLE DISSIDENT
deceptive_appeaser   -> elevated deception, may still survive if appeasing well
empathetic_reformer  -> COMPLIANT or EMPATHETIC RISK, not automatically dissident
performative_loyalist    -> COMPLIANT with elevated deception/performance risk
quiet_reformer           -> COMPLIANT or EMPATHETIC RISK with empathy/reform flags
fearful_dissident        -> PROBABLE DISSIDENT, but less aggressive than honest_dissident
truthful_noncompliant    -> PROBABLE DISSIDENT without deception
opportunistic_appeaser   -> COMPLIANT with elevated deception or survivor flags
```

## One-Shot Command Sequence

Run these after manually collecting the ten archetype files:

```bash
python3 tools/collate_human_archetype_data.py \
  --input-root data/human_playthroughs \
  --output data/training/human_train_all_archetypes.jsonl \
  --profiles \
    compliant_loyalist \
    cautious_survivor \
    honest_dissident \
    deceptive_appeaser \
    empathetic_reformer \
    performative_loyalist \
    quiet_reformer \
    fearful_dissident \
    truthful_noncompliant \
    opportunistic_appeaser

python3 generate_training_examples.py \
  --episodes 20 \
  --max-turns 14 \
  --train-steps 0 \
  --output data/training/auto_train_current.jsonl

python3 train_from_jsonl.py \
  --auto-jsonl data/training/auto_train_current.jsonl \
  --human-jsonl data/training/human_train_all_archetypes.jsonl \
  --human-weight 3 \
  --synthetic-steps 300 \
  --epochs 4 \
  --save-model \
  --model-dir models/demo_npc_human_mixed

python3 test_playthrough_profiles.py \
  --model-dir models/demo_npc_human_mixed \
  --output-dir playtest_logs/human_mixed_profiles \
  --max-turns 20
```
