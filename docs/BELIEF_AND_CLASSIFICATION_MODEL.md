# Belief And Classification Model

This document describes how the Citizen hearing demo updates the citizen profile and turns that profile into classifications, confidence, and secondary flags.

The implementation is based on:

- `belief_model.py`
- `classifications.py`
- `engine_style_scene.py`
- `test_playthrough_profiles.py`

## Purpose

The hearing does not classify the player from raw answer text. Each authored answer in `dialogue_questions.py` carries structured metadata. `EngineStyleScene` applies that metadata to two related models:

- the scene-level hearing state, such as trust, suspicion, and instability,
- the citizen trait model, which drives classification, flags, and final outcome.

The main citizen profile lives in `CitizenBeliefModel` in `belief_model.py`.

## Citizen Trait State

`belief_model.py` defines five citizen traits in `TRAIT_KEYS`:

```text
compliance
loyalty
deception
risk
empathy
```

Each trait is represented by `LatentBelief`:

```python
@dataclass(slots=True)
class LatentBelief:
    mean: float
    uncertainty: float
```

`mean` is the current trait estimate. `uncertainty` tracks how settled the estimate is. `LatentBelief.confidence` is computed as `1.0 - uncertainty`.

`CitizenBeliefState.default()` initializes the hearing with deliberately uncertain priors:

```text
compliance = 0.50 +/- 0.35
loyalty    = 0.50 +/- 0.35
deception  = 0.20 +/- 0.45
risk       = 0.35 +/- 0.40
empathy    = 0.50 +/- 0.35
```

`CitizenBeliefModel.scalar_snapshot()` returns only mean trait values. `CitizenBeliefModel.posterior_snapshot()` returns mean, uncertainty, and confidence for each trait. `EngineStyleScene._citizen_snapshot()` and `EngineStyleScene._citizen_posterior_snapshot()` expose these snapshots to the rest of the scene.

## Choice Metadata Updates

The main authored-choice update path is:

```text
EngineStyleScene.play_turn(...)
-> EngineStyleScene._apply_citizen_choice_model(choice)
-> CitizenBeliefModel.update_from_choice(choice, clamp01)
-> CitizenBeliefModel._choice_updates(choice)
```

`CitizenBeliefModel.update_from_choice()` stores the before snapshot, computes trait deltas, applies them with `clamp01`, and reduces uncertainty using `_updated_uncertainty(...)`.

The update calculation uses fields from `PlayerChoice` in `engine_style_scene.py`, especially:

```text
semantic_tags
intent
honesty
vulnerability
defensiveness
aggression
```

`CitizenBeliefModel._choice_updates()` starts with continuous metadata effects. For example:

- higher honesty tends to increase compliance and loyalty while reducing deception,
- higher defensiveness tends to increase deception and risk,
- higher aggression tends to increase risk and reduce compliance/loyalty.

It then applies semantic tag rules. Important examples:

- `compliance` raises compliance and loyalty and reduces risk.
- `loyalty` or `authority` raises loyalty.
- `deception`, `deflection`, or `denial` raises deception and slightly raises risk.
- `dissident_risk`, `challenge`, or `counterattack` raises risk and lowers compliance/loyalty.
- `refusal` raises risk and lowers compliance.
- `full_admission` lowers deception and may raise risk if paired with risk tags.
- `partial_admission` lowers deception and can increase compliance when paired with boundary/caution/empathy tags.

## Empathy Is Separate From Generic Compliance

Empathy is intentionally not a simple reward for safe, loyal, or compliant answers.

The relevant logic is in `CitizenBeliefModel._choice_updates()`:

```python
has_empathy_signal = "empathy" in tags
has_reform_signal = bool(
    "reform" in getattr(choice, "intent", "")
    or {"loyalty_conflict", "fear"} & tags
)
has_plain_authority_signal = bool({"compliance", "loyalty", "authority"} & tags) and not (
    has_empathy_signal or has_reform_signal
)
```

Empathy rises mainly when the answer has explicit empathy, reform, fear, or loyalty-conflict signals. Generic authority/compliance answers without those signals are penalized slightly:

```python
if has_plain_authority_signal:
    empathy -= 0.02
```

This is why a loyal or compliant answer can increase compliance and loyalty without automatically maxing empathy. Empathy represents concern for people, reform pressure, compassion, fear, or relational conflict rather than generic obedience.

## Uncertainty Updates

`CitizenBeliefModel._updated_uncertainty()` reduces uncertainty based on evidence strength and the size of the trait delta.

Evidence strength is computed by `_evidence_strength(choice)`. It increases with honesty, vulnerability, aggression, defensiveness, full admissions, and partial admissions. It is reduced by denial, deflection, or deception tags.

Small deltas reduce uncertainty less strongly:

```python
if abs(delta) < 0.015:
    reduction *= 0.45
```

Uncertainty is clamped to a lower bound of `0.04`, so deterministic profile runs can become confident but not mathematically certain.

## Story Consistency Updates

The story consistency path is separate from the ordinary choice-trait update:

```text
EngineStyleScene.play_turn(...)
-> EngineStyleScene._apply_claims_ledger(question, choice)
-> ClaimsLedger.apply_choice(...)
-> CitizenBeliefModel.apply_claim_update(...)
```

`ClaimsLedger` lives in `case_file.py`; the belief effects are in `CitizenBeliefModel.apply_claim_update()`.

`apply_claim_update()` receives a `ClaimUpdate` containing:

```text
new_claims
contradictions
fact_conflicts
protected_facts
exposed_facts
```

It changes deception and risk conservatively:

- each contradiction modestly increases deception,
- each fact conflict increases deception and uncertainty,
- exposing sensitive facts increases risk based on fact sensitivity,
- protecting sensitive facts slightly increases deception/uncertainty,
- consistent partial admissions can reduce deception slightly.

The current formulas are intentionally small:

```python
deception_delta = 0.005 * contradiction_count + 0.003 * fact_conflict_count
deception_delta += 0.0005 * protected_sensitivity
risk_delta = 0.006 * exposed_sensitivity
```

This means story pressure matters, but it does not instantly dominate authored personality signals. A consistent protective player can survive longer than a contradictory one, but protection still creates some pressure.

## Scene Integration

`EngineStyleScene` exposes the current classification state through:

- `citizen_classification()`
- `citizen_classification_distribution()`
- `citizen_classification_flags()`
- `citizen_confidence()`
- `_classification_uncertainty_level()`
- `_dominant_citizen_trait()`

`EngineStyleScene.model_update_text()` calls `belief_model.model_update_text(...)`, which prints:

- trait changes,
- current classification,
- confidence,
- flags,
- classification distribution.

Scene history written by `_record_history()` includes:

```text
citizen_model
citizen_posterior
citizen_classification
citizen_classification_flags
citizen_classification_distribution
citizen_confidence
story_contradictions
fact_conflicts
protected_fact_count
exposed_fact_count
```

These fields are used by reports and playtest audits.

## Classification Distribution

The classifier lives in `classifications.py`.

`classification_distribution(snapshot)` converts the five trait means into a probability distribution over:

```text
COMPLIANT
PROBABLE DISSIDENT
DECEPTIVE
EMPATHETIC RISK
UNCLASSIFIED
```

It computes label scores and then applies a softmax. This avoids brittle hard thresholds and allows borderline states to remain uncertain.

The main score structure is:

- `COMPLIANT` requires high compliance, sufficient loyalty, and lower risk.
- `PROBABLE DISSIDENT` is driven by high risk or risk paired with low loyalty.
- `DECEPTIVE` is driven by high deception.
- `EMPATHETIC RISK` requires high empathy and meaningful risk.
- `UNCLASSIFIED` has a small constant baseline score.

`classify_citizen(snapshot)` selects the highest-probability label from `classification_distribution(...)`.

`EngineStyleScene.citizen_classification()` calls `classify_citizen(self._citizen_snapshot())`.

## Confidence Calibration

Confidence is computed by `classification_confidence(snapshot, has_final_answer, clamp01)` in `classifications.py`.

The calculation uses:

- top classification probability,
- margin between top and runner-up probability,
- whether a final-answer choice has been reached.

The base formula is:

```python
confidence = 0.38 + 0.42 * top_probability + 0.30 * probability_margin
```

A final answer adds `0.05`.

Confidence is deliberately capped unless margins are strong:

```python
if top_probability < 0.80 or probability_margin < 0.50:
    confidence = min(confidence, 0.90)
elif top_probability < 0.90 or probability_margin < 0.70:
    confidence = min(confidence, 0.96)
```

This prevents deterministic playthroughs from trivially reporting `100%` confidence unless the classification distribution is genuinely decisive.

## Secondary Flags

`classification_flags(...)` adds secondary interpretive labels. Flags do not replace the primary classification. They describe important secondary risks or ambiguities.

Current flags in `CLASSIFICATION_FLAGS` are:

```text
HIGH_DECEPTION
MODERATE_DECEPTION
HIGH_EMPATHY
EMPATHETIC_REFORMIST
LOW_CONFIDENCE
BORDERLINE_DISSIDENT
COMPLIANT_SURVIVOR
```

Flag meanings:

- `HIGH_DECEPTION`: deception is at least `0.65`.
- `MODERATE_DECEPTION`: deception is at least `0.45` but below the high threshold.
- `HIGH_EMPATHY`: empathy is at least `0.80`.
- `EMPATHETIC_REFORMIST`: empathy is high, risk is moderate, and the primary classification is not probable dissident.
- `LOW_CONFIDENCE`: confidence is low or the classification probability gap is narrow.
- `BORDERLINE_DISSIDENT`: the citizen is not classified as probable dissident, but risk or dissident probability is elevated.
- `COMPLIANT_SURVIVOR`: the citizen is classified compliant with low risk, but loyalty is not absolute or deception remains notable.

`EngineStyleScene.citizen_classification_flags()` passes the current snapshot, classification, distribution, and confidence into `classification_flags(...)`.

## Endings

Final outcome text is selected from the primary classification:

```text
ending_type_for_classification(classification)
ending_text_for_classification(classification)
```

These functions live in `classifications.py` and are called by `EngineStyleScene._choose_ending_type()` and `EngineStyleScene.ending_text()`.

Examples:

- `COMPLIANT`: restrictions lifted, monitoring continues.
- `PROBABLE DISSIDENT`: appeal denied and enhanced surveillance.
- `DECEPTIVE`: contradiction review escalated.
- `EMPATHETIC RISK`: unresolved appeal and social proximity restrictions.
- `UNCLASSIFIED`: temporary restrictions remain.

## Deterministic Profile Validation

`test_playthrough_profiles.py` validates the belief and classification model by running deterministic archetype playthroughs.

Each `PlaythroughProfile` defines:

```python
expected_classification: str
expected_flags: tuple[str, ...] = ()
```

During a profile run, `run_profile(...)` records each turn's selected choice, tags, claims, protects, exposes, story metrics, neural probe, selected next question, and post-turn classification.

At the end of the playthrough it computes:

```python
snapshot = scene._citizen_snapshot()
distribution = classification_distribution(snapshot)
classification = scene.citizen_classification()
confidence = scene.citizen_confidence()
flags = classification_flags(...)
```

The profile passes when:

- the final primary classification equals `expected_classification`,
- all `expected_flags` are present.

`write_reports(...)` writes both JSONL and Markdown reports. The Markdown report includes:

- expected classification,
- actual classification,
- expected and actual flags,
- confidence,
- citizen trait values,
- distribution,
- story metrics,
- per-turn claims/protects/exposes,
- selected next question and neural probe trace.

The current report locations are:

```text
playtest_logs/story_auto_profiles/profile_playthroughs.md
playtest_logs/story_human_only_profiles/profile_playthroughs.md
playtest_logs/story_human_mixed_profiles/profile_playthroughs.md
```

## Practical Interpretation

The classification model is intentionally mixed:

- authored choice metadata updates trait beliefs,
- story consistency adds pressure when the player contradicts or exposes sensitive facts,
- classifier probabilities keep borderline states visible,
- confidence calibration prevents false certainty,
- flags preserve secondary interpretations that a single primary label would hide.

This supports the intended gameplay: the player is not simply trying to pick the most compliant answer. They are trying to survive classification while keeping a coherent story and managing sensitive facts.
