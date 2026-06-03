# Story Consistency Mechanics

This document describes the current story-consistency system used by the Citizen hearing demo.

It is based on:

- `case_file.py`
- `engine_style_scene.py`
- `belief_model.py`
- `dialogue_questions.py`

## Purpose

The story system gives the player a concrete private situation to manage. The player is not simply choosing the most compliant answer. They are trying to survive classification while keeping a coherent account and protecting sensitive facts.

The default case asks the player to balance:

- protecting their sibling,
- avoiding a false violence label,
- explaining deleted-message pressure,
- deciding what to admit,
- avoiding contradictions and known-fact conflicts.

The system tracks what the player claims, what they protect, and what they expose. It then feeds that story pressure into belief updates, question selection, history, generated training data, and player-facing panels.

## Core Data Structures

All core story data structures are defined in `case_file.py`.

## CaseFact

`CaseFact` represents one fact in the case file.

Fields:

```text
key
label
truth_value
sensitivity
description
```

Example fact keys used in the default case include:

```text
believes_law_unjust
attended_meeting
deleted_message
planned_violence
sibling_present
reported_contact
```

`truth_value` is the case-file truth used for fact-conflict checks. The current implementation treats explicit `true` and `false` claims as direct truth claims.

`sensitivity` is used by belief and selector logic. Sensitive facts create more risk when exposed and more story pressure when protected or probed.

`CaseFact.public_summary(revealed)` hides truth and description until the fact has been exposed. If the fact is revealed, the public summary includes `truth_value` and `description`.

`CaseFact.hidden_summary(revealed)` is intended for debug/tests and includes the hidden truth regardless of public reveal state.

## PlayerInterest

`PlayerInterest` represents something the player is trying to protect.

Fields:

```text
key
label
description
protected_fact_keys
```

For example, the default case includes interests that protect sibling-related facts and avoid a peaceful meeting being treated as violent coordination.

The selector can use interests indirectly. If the player protects facts associated with an interest, that interest becomes pressured. Questions with matching `pressure_on_interests` metadata become more attractive.

## CaseFile

`CaseFile` groups facts, interests, and reveal state.

Fields:

```text
key
label
facts
interests
revealed_fact_keys
```

Important methods:

```text
fact(key)
is_revealed(key)
reveal(key)
public_summary()
hidden_summary()
private_briefing()
```

`CaseFile.fact(key)` validates and returns a `CaseFact`.

`CaseFile.reveal(key)` marks a fact as exposed. This is called when a `PlayerChoice` exposes a fact.

`CaseFile.public_summary()` is passed into the question selector. It includes fact sensitivity and reveal state while preserving hidden truth values for unrevealed facts.

`CaseFile.private_briefing()` creates the player-facing opening scenario. For the default `protect_sibling` case, it tells the player that they attended a peaceful unlicensed reform meeting, their younger sibling was present, they believe the assembly restriction is unjust, they deleted a message, and they did not report their sibling.

## ClaimRecord

`ClaimRecord` records one claim made by the player.

Fields:

```text
fact_key
claimed_value
turn
question_id
choice_intent
```

A claim is not just text. It is a structured assertion made by a `PlayerChoice` in `dialogue_questions.py`.

For example:

```python
claims=(("believes_law_unjust", "false"),)
```

means the player has placed a claim on record that they do not believe the law is unjust.

## ClaimUpdate

`ClaimUpdate` is the result of applying one choice to the claims ledger.

Fields:

```text
new_claims
contradictions
fact_conflicts
protected_facts
exposed_facts
```

It also provides:

```text
has_updates()
summary()
```

`EngineStyleScene.story_consistency_text()` uses `last_claim_update` to print immediate feedback after a turn:

```text
CLAIM RECORDED
CONTRADICTION
FACT PRESSURE
PROTECTED
EXPOSED
```

## ClaimsLedger

`ClaimsLedger` stores the accumulated story state.

Fields:

```text
claims_by_fact
contradiction_count
fact_conflict_count
protected_fact_keys
exposed_fact_keys
```

Important methods:

```text
apply_choice(...)
latest_claims()
summary()
```

`ClaimsLedger.apply_choice()` receives the selected choice's `claims`, `protects`, and `exposes` metadata. It then:

1. validates protected facts against the case file,
2. records protected fact keys,
3. reveals exposed facts in the `CaseFile`,
4. creates `ClaimRecord` entries for new claims,
5. checks each new claim against prior claims for contradiction,
6. checks explicit true/false claims against known `CaseFact.truth_value`,
7. updates aggregate contradiction and fact-conflict counts,
8. returns a `ClaimUpdate`.

## Choice Story Metadata

Story metadata is authored on `PlayerChoice` objects in `dialogue_questions.py`.

The three story fields are:

```text
claims
protects
exposes
```

### claims

`claims` is a tuple of `(fact_key, claimed_value)` pairs.

Example:

```python
claims=(("believes_law_unjust", "false"),)
```

This records a claim about the player belief.

### protects

`protects` is a tuple of fact keys the player is trying to shield.

Example:

```python
protects=("attended_meeting", "sibling_present")
```

This means the answer is not exposing those facts and is attempting to keep them protected.

### exposes

`exposes` is a tuple of fact keys the player reveals.

Example:

```python
exposes=("attended_meeting", "planned_violence")
```

This calls `CaseFile.reveal(key)` for each exposed fact and adds the fact to `ClaimsLedger.exposed_fact_keys`.

## Example From The Opening Question

The opening question in `dialogue_questions.py` is `authority_unfair_law`.

One compliant answer is:

```python
PlayerChoice(
    '"Yes. Law only works if people obey even when they disagree."',
    "obey_unfair_law",
    ("compliance", "authority", "loyalty"),
    claims=(("believes_law_unjust", "false"),),
    protects=("attended_meeting", "sibling_present"),
)
```

This answer increases compliance/loyalty pressure, but also claims `believes_law_unjust=false`. In the default case briefing, the player privately knows they do believe the assembly restriction is unjust. That creates fact pressure.

A more direct dissident answer is:

```python
claims=(("believes_law_unjust", "true"),)
exposes=("believes_law_unjust",)
```

That is more truthful but exposes a sensitive belief.

A conditional answer is:

```python
claims=(("believes_law_unjust", "conditional"),)
protects=("attended_meeting",)
```

That places a softer claim on record and protects meeting attendance.

## Contradictions Versus Fact Conflicts

The implementation distinguishes two kinds of story pressure.

## Contradiction

A contradiction is a conflict between the player's own claims across turns.

Example:

```text
Turn 1: sibling_present -> false
Turn 5: sibling_present -> true
```

This is detected by comparing a new `ClaimRecord` against previous claims for the same fact in `ClaimsLedger.claims_by_fact`.

Contradictions are stored in `ClaimUpdate.contradictions` and added to `ClaimsLedger.contradiction_count`.

Player-facing text:

```text
CONTRADICTION: <fact label> conflicts with earlier testimony
```

## Fact Conflict

A fact conflict is a conflict between a player's explicit claim and the hidden case-file truth.

Example:

```text
Case fact: believes_law_unjust -> true
Player claim: believes_law_unjust -> false
```

This is detected in `ClaimsLedger.apply_choice()` only when the claim is explicit `true` or `false`:

```python
if claimed_value in {"true", "false"} and claimed_value != fact.truth_value:
    fact_conflicts.append(...)
```

Fact conflicts are stored in `ClaimUpdate.fact_conflicts` and added to `ClaimsLedger.fact_conflict_count`.

Player-facing text:

```text
FACT PRESSURE: <fact label> is under review
```

The wording does not reveal the hidden truth unless the player has exposed the fact. It only tells the player that this part of the story is now under pressure.

## Why Ambiguous Refinements Are Softer

`ClaimsLedger` defines:

```python
AMBIGUOUS_REFINEMENTS = {
    "conditional",
    "private",
    "procedural",
    "protected",
    "unknown",
    "partial",
    "legal_only",
}

DIRECT_VALUES = {"true", "false"}
```

`ClaimsLedger._claims_contradict(previous, current)` applies softened compatibility:

- identical values do not contradict,
- ambiguous refinements do not contradict each other,
- `true` and `false` directly contradict each other,
- direct true/false claims do not automatically contradict ambiguous refinements.

This matters because many playable answers are cautious, conditional, private, or procedural rather than clean truth/lie declarations.

For example:

```text
attended_meeting -> legal_only
attended_meeting -> partial
```

is treated as an ambiguous refinement, not a direct contradiction.

This makes the game less brittle. The player can maintain a nuanced story without every guarded answer being treated as deception. Direct true/false reversals still create contradiction pressure.

## Scene Integration

`EngineStyleScene.__init__()` creates:

```python
self.case_file = case_file or default_case_file()
self.claims_ledger = ClaimsLedger()
self.last_claim_update = ClaimUpdate()
```

Each turn, `EngineStyleScene.play_turn()` calls:

```python
self._apply_choice_state(choice)
self._apply_citizen_choice_model(choice)
self._apply_claims_ledger(question, choice)
obs = self._observation_from_choice(choice, Observation)
action = self.controller.update_belief_and_act(...)
```

Story consistency is applied before the neural controller update for the turn.

`EngineStyleScene._apply_claims_ledger()` calls:

```python
self.claims_ledger.apply_choice(...)
self.citizen_model.apply_claim_update(...)
```

The resulting data is stored in `scene.history`:

```text
claim_update
story_contradictions
fact_conflicts
protected_fact_count
exposed_fact_count
```

These fields are also used by generated training data and deterministic profile reports.

## How Story Pressure Affects Belief Updates

Story pressure affects `CitizenBeliefModel` through `apply_claim_update()` in `belief_model.py`.

Inputs:

```text
claim_update
case_file
clamp01
```

The method computes:

```text
contradiction_count
fact_conflict_count
exposed_sensitivity
protected_sensitivity
has_consistent_partial
```

Current belief effects:

```python
deception_delta = 0.005 * contradiction_count + 0.003 * fact_conflict_count
deception_delta += 0.0005 * protected_sensitivity

if has_consistent_partial:
    deception_delta -= 0.010

risk_delta = 0.006 * exposed_sensitivity
```

Uncertainty effects:

```python
uncertainty_delta = 0.006 * fact_conflict_count + 0.0015 * protected_sensitivity
if contradiction_count:
    uncertainty_delta += 0.004 * contradiction_count

risk.uncertainty increases when exposed_sensitivity exists
```

Interpretation:

- contradictions modestly increase deception and deception uncertainty,
- fact conflicts increase deception and uncertainty,
- protecting sensitive facts adds slight deception/uncertainty pressure,
- exposing sensitive facts increases risk,
- consistent partial admissions can slightly reduce deception.

The values are intentionally conservative. Protecting someone is not automatically treated as guilt, and exposing the truth is not automatically safe.

## Story Pressure And Question Selection

Although this document focuses on story consistency, the story state also affects question selection through `question_selector.py`.

`EngineStyleScene.select_next_question_id()` passes:

```python
self.case_file.public_summary()
self.claims_ledger.summary()
```

The selector derives:

```text
unrevealed_fact_keys
contradicted_fact_keys
protected_fact_keys
exposed_fact_keys
pressured_interest_keys
```

Questions in `dialogue_questions.py` can declare:

```text
probes_facts
probes_claims
pressure_on_interests
```

This means the hearing AI can follow up on protected interests, contradicted claims, and unrevealed sensitive facts without hard-coding a fixed route.

## Story Consistency Output

`EngineStyleScene.story_consistency_text()` prints the immediate update from the current turn.

Possible lines:

```text
CLAIM RECORDED: <Fact Label> -> <claimed_value>
CONTRADICTION: <Fact Label> conflicts with earlier testimony
FACT PRESSURE: <Fact Label> is under review
PROTECTED: <Fact Label>
EXPOSED: <Fact Label> -> <truth_value>
```

Important distinction:

- `EXPOSED` shows the truth value because the player exposed the fact.
- `FACT PRESSURE` does not reveal hidden truth. It only says the claim is under review.

## Private Current Story So Far Panel

`EngineStyleScene.private_story_so_far_text()` prints the private story panel after story consistency updates.

It shows:

```text
Claims you have put on record
Facts you are still trying to protect
Facts already exposed
Current pressure
```

`Claims you have put on record` shows the latest claim for each fact using `ClaimsLedger.latest_claims()`.

`Facts you are still trying to protect` shows accumulated protected fact keys.

`Facts already exposed` shows revealed facts and their truth values.

`Current pressure` summarizes aggregate story pressure:

```text
N story contradiction(s)
N known-fact conflict(s)
```

For the player, this panel is a memory aid and a gameplay signal. It tells them what story they are maintaining, what they are still protecting, and whether their answers have created pressure.

## What Current Pressure Means

`Current pressure` is not an instant fail state.

It means the story ledger has accumulated contradiction or known-fact conflict pressure.

Example:

```text
CLAIM RECORDED: Believes Law Unjust -> false
FACT PRESSURE: Believes Law Unjust is under review
Current pressure: 1 known-fact conflict(s)
```

This means the player made an explicit claim that conflicts with the case-file truth. It may increase deception/uncertainty modestly and may make related probes more relevant later. It does not immediately reveal the hidden truth or end the game.

## Generated Data And Reports

Story mechanics are exported into training and evaluation artifacts.

Generated JSONL rows include story fields such as:

```text
story_contradictions
fact_conflicts
protected_fact_count
exposed_fact_count
case_file
claims_ledger
selector_debug
```

Deterministic profile reports include story metrics, selected questions, and claim/protect/expose metadata.

The text dialogue graph generated by `make_text_dialogue_graph.py` includes story metadata for authoring review:

```text
claims=
protects=
exposes=
facts=
claims=
interests=
```

## Summary

The story-consistency system turns authored choices into a persistent case-file ledger.

The player's answers are not only belief signals. They are structured claims about facts, attempts to protect interests, and possible exposures of sensitive information.

Contradictions measure inconsistency within the player's own story. Fact conflicts measure conflict between explicit claims and hidden case-file truth. Ambiguous refinements make cautious or partial answers playable instead of automatically contradictory.

The resulting story pressure affects belief updates, question selection, player-facing feedback, generated training data, and playtest reports.
