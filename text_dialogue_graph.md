```text
TEXT DIALOGUE GRAPH / ROUTE OVERVIEW
================================================================================
Plain text only. No Mermaid. No Graphviz.

ROUTING MODEL
- Start node: authority_unfair_law
- Choices do not carry fixed next_question_id links.
- After each answer, EngineStyleScene.select_next_question_id() selects
  the highest-scoring unasked question from the remaining pool.
- When no unasked questions remain, the scene moves to final.

================================================================================
CONTEXT: ASSOCIATION (1 questions)
================================================================================

[loyalty_community_protect]
  AI: HEARING AI: "Should communities protect their own from state punishment?"
  ├─ "No. Communities must not obstruct lawful process."
     -> SELECTOR -> next unasked question  (community_no_obstruction; trust +0.09; susp -0.06)
  ├─ "Yes, when punishment is disproportionate."
     -> SELECTOR -> next unasked question  (community_protect_disproportionate; susp +0.10)
  └─ "They should protect people from abuse, not from accountability."
     -> SELECTOR -> next unasked question  (community_protect_limited; trust +0.04)

================================================================================
CONTEXT: AUTHORITY (28 questions)
================================================================================

[authority_unfair_law]
  AI: HEARING AI: "If a law is unfair, should it still be obeyed?"
  ├─ "Yes. Law only works if people obey even when they disagree."
     -> SELECTOR -> next unasked question  (obey_unfair_law; trust +0.09; susp -0.07)
  ├─ "No. An unjust law loses moral authority."
     -> SELECTOR -> next unasked question  (reject_unfair_law; trust +0.01; susp +0.10)
  └─ "It depends how much harm disobedience would cause."
     -> SELECTOR -> next unasked question  (conditional_unfair_law; trust +0.05; susp -0.02)

[authority_order_freedom]
  AI: HEARING AI: "Is order more important than freedom?"
  ├─ "Yes. Without order, freedom becomes violence."
     -> SELECTOR -> next unasked question  (order_over_freedom; trust +0.09; susp -0.07)
  ├─ "No. Order without freedom is only control."
     -> SELECTOR -> next unasked question  (freedom_over_order; susp +0.11)
  └─ "Order matters, but it has to protect freedom rather than replace it."
     -> SELECTOR -> next unasked question  (balance_order_freedom; trust +0.05; susp -0.01)

[authority_questioning]
  AI: HEARING AI: "Should citizens question authority?"
  ├─ "Yes, but respectfully and through approved channels."
     -> SELECTOR -> next unasked question  (approved_questioning; trust +0.09; susp -0.06)
  ├─ "Yes. Authority that cannot be questioned is dangerous."
     -> SELECTOR -> next unasked question  (open_questioning; susp +0.10)
  └─ "Most people should focus on their own duties."
     -> SELECTOR -> next unasked question  (discourage_questioning; trust +0.09; susp -0.07)

[authority_moral_mistakes]
  AI: HEARING AI: "Can authorities make moral mistakes?"
  ├─ "Yes. No system is morally perfect."
     -> SELECTOR -> next unasked question  (admit_authority_error; trust +0.04; susp +0.03)
  ├─ "They can, but citizens still owe obedience."
     -> SELECTOR -> next unasked question  (error_but_obey; trust +0.09; susp -0.06)
  └─ "Calling them mistakes is how people excuse disloyalty."
     -> SELECTOR -> next unasked question  (reject_authority_error; trust +0.08; susp -0.04)

[authority_sacrifice_freedom]
  AI: HEARING AI: "Is stability worth sacrificing personal freedoms?"
  ├─ "Yes. A stable society protects everyone."
     -> SELECTOR -> next unasked question  (stability_over_freedom; trust +0.09; susp -0.07)
  ├─ "Only temporarily, and only with strict limits."
     -> SELECTOR -> next unasked question  (limited_sacrifice; trust +0.04; susp +0.01)
  └─ "No. That is how permanent control begins."
     -> SELECTOR -> next unasked question  (reject_stability_tradeoff; susp +0.11)

[authority_obedience_citizen]
  AI: HEARING AI: "Does obedience create good citizens?"
  ├─ "Yes. Obedience is the basis of civic trust."
     -> SELECTOR -> next unasked question  (obedience_good_citizen; trust +0.10; susp -0.07)
  ├─ "No. Good citizens need judgment, not just obedience."
     -> SELECTOR -> next unasked question  (judgment_good_citizen; susp +0.07)
  └─ "Obedience helps, but fear can imitate it."
     -> SELECTOR -> next unasked question  (obedience_fear_distinction; trust +0.05)

[authority_experts_citizens]
  AI: HEARING AI: "Who should have the final say: experts or citizens?"
  ├─ "Experts. Most citizens lack the necessary information."
     -> SELECTOR -> next unasked question  (experts_final_say; trust +0.08; susp -0.06)
  ├─ "Citizens. Experts advise; they should not rule."
     -> SELECTOR -> next unasked question  (citizens_final_say; susp +0.09)
  └─ "Experts should decide emergencies; citizens should decide values."
     -> SELECTOR -> next unasked question  (split_experts_values; trust +0.03; susp +0.01)

[risk_safety_autonomy]
  AI: HEARING AI: "Is safety worth surrendering autonomy?"
  ├─ "Yes. Safety is what makes autonomy possible."
     -> SELECTOR -> next unasked question  (safety_over_autonomy; trust +0.09; susp -0.07)
  ├─ "No. A protected life can still be a controlled one."
     -> SELECTOR -> next unasked question  (autonomy_over_safety; susp +0.11)
  └─ "Some autonomy can be limited, but not erased."
     -> SELECTOR -> next unasked question  (limited_autonomy_tradeoff; trust +0.02; susp +0.01)

[authority_private_conscience]
  AI: HEARING AI: "Should private conscience ever override public order?"
  ├─ "No. Private conscience cannot be allowed to fracture public order."
     -> SELECTOR -> next unasked question  (public_order_over_conscience; trust +0.09; susp -0.07)
  ├─ "Yes. Without conscience, order becomes machinery."
     -> SELECTOR -> next unasked question  (conscience_over_order; susp +0.11)
  └─ "Only when every lawful remedy has failed."
     -> SELECTOR -> next unasked question  (conscience_after_remedies; trust +0.04; susp +0.01)

[authority_emergency_powers]
  AI: HEARING AI: "When should emergency powers end?"
  ├─ "When officials determine the emergency has passed."
     -> SELECTOR -> next unasked question  (officials_end_emergency; trust +0.09; susp -0.07)
  ├─ "On a fixed date, or they become permanent control."
     -> SELECTOR -> next unasked question  (fixed_end_emergency; susp +0.09)
  └─ "They should renew only under independent review."
     -> SELECTOR -> next unasked question  (review_emergency_powers; trust +0.05; susp +0.01)

[authority_public_criticism]
  AI: HEARING AI: "Is public criticism of officials socially useful?"
  ├─ "Usually no. It weakens trust in institutions."
     -> SELECTOR -> next unasked question  (criticism_weakens_trust; trust +0.08; susp -0.06)
  ├─ "Yes. Officials need public pressure to stay honest."
     -> SELECTOR -> next unasked question  (criticism_keeps_honest; susp +0.10)
  └─ "It is useful when it is specific and evidence-based."
     -> SELECTOR -> next unasked question  (specific_public_criticism; trust +0.04; susp +0.01)

[authority_chain_of_command]
  AI: HEARING AI: "Should a chain of command be followed when the order is harmful?"
  ├─ "Yes. Refusal creates greater harm than a bad order."
     -> SELECTOR -> next unasked question  (follow_harmful_order; trust +0.08; susp -0.04)
  ├─ "No. Responsibility does not disappear inside a hierarchy."
     -> SELECTOR -> next unasked question  (reject_harmful_order; susp +0.12)
  └─ "The order should be paused and escalated for review."
     -> SELECTOR -> next unasked question  (escalate_harmful_order; trust +0.05; susp +0.01)

[authority_algorithmic_decisions]
  AI: HEARING AI: "Should citizens accept automated decisions they cannot inspect?"
  ├─ "Yes, if the system has been authorised."
     -> SELECTOR -> next unasked question  (accept_authorised_algorithm; trust +0.09; susp -0.07)
  ├─ "No. Uninspectable authority is not accountable."
     -> SELECTOR -> next unasked question  (reject_black_box_authority; susp +0.12)
  └─ "They should comply provisionally while appealing."
     -> SELECTOR -> next unasked question  (provisional_algorithm_compliance; trust +0.08; susp -0.06)

[authority_loyalty_oath]
  AI: HEARING AI: "What is a loyalty oath worth?"
  ├─ "It binds a citizen publicly to their duties."
     -> SELECTOR -> next unasked question  (oath_binds_duty; trust +0.09; susp -0.07)
  ├─ "Nothing, if fear is the reason someone says it."
     -> SELECTOR -> next unasked question  (oath_under_fear_empty; susp +0.07)
  └─ "It matters only if actions later prove it."
     -> SELECTOR -> next unasked question  (oath_requires_actions; trust +0.04; susp +0.01)

[authority_refuse_illegal_order]
  AI: HEARING AI: "Would you refuse an illegal order from a superior?"
  ├─ "I would use official channels before refusing."
     -> SELECTOR -> next unasked question  (channels_before_refusal; trust +0.07; susp -0.04)
  ├─ "Yes. Illegal orders do not deserve obedience."
     -> SELECTOR -> next unasked question  (refuse_illegal_order; susp +0.11)
  └─ "I would need proof it was illegal."
     -> SELECTOR -> next unasked question  (need_proof_illegal_order; trust +0.04; susp +0.01)

[authority_security_truth]
  AI: HEARING AI: "Should the state hide truth to preserve security?"
  ├─ "Yes. Some information endangers the public."
     -> SELECTOR -> next unasked question  (hide_truth_for_security; trust +0.09; susp -0.06)
  ├─ "No. A protected lie still trains people to obey lies."
     -> SELECTOR -> next unasked question  (reject_security_lie; susp +0.12)
  └─ "Only temporarily, with later disclosure required."
     -> SELECTOR -> next unasked question  (temporary_security_secrecy; trust +0.04; susp +0.01)

[authority_collective_punishment]
  AI: HEARING AI: "Can collective punishment ever be justified?"
  ├─ "Yes, when groups protect dangerous members."
     -> SELECTOR -> next unasked question  (justify_collective_punishment; trust +0.07; susp -0.04)
  ├─ "No. Punishing the innocent teaches fear, not justice."
     -> SELECTOR -> next unasked question  (reject_collective_punishment; susp +0.09)
  └─ "Only shared privileges should be restricted, not basic rights."
     -> SELECTOR -> next unasked question  (limit_collective_punishment; trust +0.03; susp +0.01)

[authority_permit_protest]
  AI: HEARING AI: "Should protest require permission?"
  ├─ "Yes. Unregulated protest becomes disorder."
     -> SELECTOR -> next unasked question  (permit_required_protest; trust +0.09; susp -0.07)
  ├─ "No. Permission turns protest into a privilege."
     -> SELECTOR -> next unasked question  (reject_protest_permit; susp +0.12)
  └─ "Only time and place should be regulated."
     -> SELECTOR -> next unasked question  (regulate_protest_limits; trust +0.04; susp +0.01)

[authority_surveillance_limits]
  AI: HEARING AI: "Who should set the limits of surveillance?"
  ├─ "Security agencies, because they understand the threats."
     -> SELECTOR -> next unasked question  (agencies_set_surveillance_limits; trust +0.08; susp -0.06)
  ├─ "The public, because they are the ones being watched."
     -> SELECTOR -> next unasked question  (public_sets_surveillance_limits; susp +0.11)
  └─ "Independent courts should set enforceable limits."
     -> SELECTOR -> next unasked question  (courts_set_surveillance_limits; trust +0.05; susp -0.01)

[authority_bad_law_strategy]
  AI: HEARING AI: "What should a citizen do with a bad law?"
  ├─ "Obey it while petitioning for reform."
     -> SELECTOR -> next unasked question  (obey_bad_law_reform; trust +0.08; susp -0.04)
  ├─ "Break it openly and accept the consequences."
     -> SELECTOR -> next unasked question  (break_bad_law_openly; susp +0.12)
  └─ "Test it in court before deciding."
     -> SELECTOR -> next unasked question  (test_bad_law_court; trust +0.05; susp -0.01)

[authority_civic_fear]
  AI: HEARING AI: "Is fear useful for maintaining civic order?"
  ├─ "Yes. Fear of consequence prevents harm."
     -> SELECTOR -> next unasked question  (fear_maintains_order; trust +0.08; susp -0.04)
  ├─ "No. Fear produces obedience without legitimacy."
     -> SELECTOR -> next unasked question  (reject_fear_order; susp +0.09)
  └─ "It can deter harm, but it cannot build trust."
     -> SELECTOR -> next unasked question  (fear_deterrence_not_trust; trust +0.03; susp +0.01)

[authority_information_control]
  AI: HEARING AI: "Should false information be removed by authority?"
  ├─ "Yes. False information damages public stability."
     -> SELECTOR -> next unasked question  (remove_false_information; trust +0.09; susp -0.06)
  ├─ "Only if authority can be challenged when it is wrong."
     -> SELECTOR -> next unasked question  (challenge_information_removal; susp +0.08)
  └─ "No. Control over truth becomes control over people."
     -> SELECTOR -> next unasked question  (reject_information_control; susp +0.12)

[authority_mercy_vs_consistency]
  AI: HEARING AI: "Should authority prioritise mercy or consistency?"
  ├─ "Consistency. Citizens must know rules mean what they say."
     -> SELECTOR -> next unasked question  (consistency_over_mercy; trust +0.09; susp -0.06)
  ├─ "Mercy. A system without mercy becomes cruel."
     -> SELECTOR -> next unasked question  (mercy_over_consistency; trust +0.04; susp +0.01)
  └─ "Consistency should be the rule; mercy should be reviewable."
     -> SELECTOR -> next unasked question  (reviewable_mercy; trust +0.05; susp -0.01)

[authority_citizen_obligation]
  AI: HEARING AI: "What does a citizen owe the state?"
  ├─ "Obedience, taxes, and public cooperation."
     -> SELECTOR -> next unasked question  (owe_obedience_taxes; trust +0.09; susp -0.07)
  ├─ "Nothing unconditional. The state must earn obligation."
     -> SELECTOR -> next unasked question  (conditional_state_obligation; susp +0.12)
  └─ "Cooperation when the state protects people fairly."
     -> SELECTOR -> next unasked question  (owe_fair_cooperation; trust +0.05; susp -0.01)

[authority_institutional_trust]
  AI: HEARING AI: "Should institutions be trusted by default?"
  ├─ "Yes. Default distrust corrodes society."
     -> SELECTOR -> next unasked question  (trust_institutions_default; trust +0.09; susp -0.07)
  ├─ "No. Trust should be earned and checked."
     -> SELECTOR -> next unasked question  (trust_must_be_earned; susp +0.09)
  └─ "They deserve procedural trust, not blind trust."
     -> SELECTOR -> next unasked question  (procedural_not_blind_trust; trust +0.05; susp -0.01)

[authority_exceptional_citizens]
  AI: HEARING AI: "Should any citizen be exempt from ordinary rules?"
  ├─ "No. Equal rules preserve social trust."
     -> SELECTOR -> next unasked question  (no_rule_exemptions; trust +0.09; susp -0.06)
  ├─ "Yes, when rules would punish someone for doing right."
     -> SELECTOR -> next unasked question  (moral_rule_exemption; susp +0.07)
  └─ "Only transparent exemptions approved in advance."
     -> SELECTOR -> next unasked question  (transparent_rule_exemptions; trust +0.05; susp -0.01)

[authority_appeal_rights]
  AI: HEARING AI: "Should every official decision have a human appeal?"
  ├─ "No. Some decisions must remain efficient and final."
     -> SELECTOR -> next unasked question  (limit_human_appeal; trust +0.08; susp -0.04)
  ├─ "Yes. No system should be allowed to judge without appeal."
     -> SELECTOR -> next unasked question  (require_human_appeal; susp +0.10)
  └─ "High-impact decisions should always be appealable."
     -> SELECTOR -> next unasked question  (appeal_high_impact; trust +0.05; susp -0.02)

[authority_symbol_respect]
  AI: HEARING AI: "Does disrespect for state symbols indicate civic risk?"
  ├─ "Yes. Symbols hold society together."
     -> SELECTOR -> next unasked question  (symbols_hold_society; trust +0.08; susp -0.06)
  ├─ "No. Respect forced by threat is not respect."
     -> SELECTOR -> next unasked question  (forced_symbol_respect_empty; susp +0.11)
  └─ "It depends whether disrespect becomes intimidation or harm."
     -> SELECTOR -> next unasked question  (symbol_respect_depends_harm; trust +0.04; susp +0.01)

================================================================================
CONTEXT: DECEPTION (12 questions)
================================================================================

[authority_rule_broken]
  AI: HEARING AI: "Have you ever broken a rule because you believed the rule was wrong?"
  ├─ "No. I use the proper channels."
     -> SELECTOR -> next unasked question  (deny_rule_breaking; trust +0.03; susp +0.07)
  ├─ "Yes. Quietly, when obeying would have hurt someone."
     -> SELECTOR -> next unasked question  (admit_protective_rule_breaking; susp +0.09)
  └─ "I have bent rules, not broken them."
     -> SELECTOR -> next unasked question  (minimise_rule_breaking; susp +0.08)

[risk_hidden_beliefs]
  AI: HEARING AI: "Have you ever hidden your beliefs to stay safe?"
  ├─ "No. My beliefs are ordinary."
     -> SELECTOR -> next unasked question  (deny_hidden_beliefs; trust +0.01; susp +0.10)
  ├─ "Yes. Everyone learns what not to say."
     -> SELECTOR -> next unasked question  (admit_hidden_beliefs; susp +0.12)
  └─ "I choose my words carefully. That is not the same as hiding."
     -> SELECTOR -> next unasked question  (careful_words; susp +0.08)

[deception_lying_moral]
  AI: HEARING AI: "Is lying ever moral?"
  ├─ "No. Trust depends on truth."
     -> SELECTOR -> next unasked question  (lying_never_moral; trust +0.08; susp -0.06)
  ├─ "Yes. A lie can protect someone from unjust harm."
     -> SELECTOR -> next unasked question  (protective_lying_moral; susp +0.07)
  └─ "That depends who is demanding the truth."
     -> SELECTOR -> next unasked question  (truth_depends_power; susp +0.11)

[deception_lied_protect]
  AI: HEARING AI: "Have you lied to protect someone?"
  ├─ "No."
     -> SELECTOR -> next unasked question  (deny_protective_lie; trust +0.01; susp +0.10)
  ├─ "Yes. I would rather admit that than pretend purity."
     -> SELECTOR -> next unasked question  (admit_protective_lie; susp +0.10)
  └─ "I have avoided questions that would hurt people."
     -> SELECTOR -> next unasked question  (omission_to_protect; susp +0.09)

[deception_omission]
  AI: HEARING AI: "Is omission a form of lying?"
  ├─ "Yes. Withholding relevant facts corrupts the record."
     -> SELECTOR -> next unasked question  (omission_is_lying; trust +0.07; susp -0.04)
  ├─ "Sometimes omission is the only safe answer."
     -> SELECTOR -> next unasked question  (omission_safety; susp +0.09)
  └─ "It depends whether the questioner has a right to know."
     -> SELECTOR -> next unasked question  (omission_right_to_know; susp +0.07)

[deception_honesty_dangerous]
  AI: HEARING AI: "Can honesty be dangerous?"
  ├─ "Yes, but danger does not erase duty."
     -> SELECTOR -> next unasked question  (honesty_danger_duty; trust +0.08; susp -0.06)
  ├─ "Yes. Dangerous systems make honesty costly."
     -> SELECTOR -> next unasked question  (honesty_costly_system; susp +0.10)
  └─ "Honesty is dangerous mostly when someone wants control."
     -> SELECTOR -> next unasked question  (honesty_control; susp +0.11)

[deception_truth_if_punished]
  AI: HEARING AI: "Would you tell the truth if you knew you would be punished?"
  ├─ "Yes. Punishment does not change the facts."
     -> SELECTOR -> next unasked question  (truth_despite_punishment; trust +0.04; susp +0.04)
  ├─ "No. Survival would come first."
     -> SELECTOR -> next unasked question  (survival_over_truth; susp +0.10)
  └─ "I would tell only what I had to."
     -> SELECTOR -> next unasked question  (limited_truth; susp +0.10)

[deception_self_preservation]
  AI: HEARING AI: "Is self-preservation more important than honesty?"
  ├─ "No. A society cannot function if everyone hides."
     -> SELECTOR -> next unasked question  (honesty_over_preservation; trust +0.07; susp -0.04)
  ├─ "Sometimes. Dead people do not get to be honest later."
     -> SELECTOR -> next unasked question  (preservation_over_honesty; trust +0.01; susp +0.06)
  └─ "That question is easier for people who feel safe."
     -> SELECTOR -> next unasked question  (honesty_requires_safety; susp +0.09)

[deception_pretended_agree]
  AI: HEARING AI: "Have you ever pretended to agree with an official statement?"
  ├─ "No. I do not make false affirmations."
     -> SELECTOR -> next unasked question  (deny_pretend_agree; trust +0.02; susp +0.09)
  ├─ "Yes. It was easier than inviting scrutiny."
     -> SELECTOR -> next unasked question  (admit_pretend_agree; susp +0.11)
  └─ "I have stayed silent when agreement was assumed."
     -> SELECTOR -> next unasked question  (silent_assumed_agreement; susp +0.08)

[deception_necessary]
  AI: HEARING AI: "Is deception sometimes necessary?"
  ├─ "No. Necessary deception is usually cowardice renamed."
     -> SELECTOR -> next unasked question  (deception_not_necessary; trust +0.07; susp -0.04)
  ├─ "Yes, when truth is being used as a weapon."
     -> SELECTOR -> next unasked question  (deception_against_weaponised_truth; susp +0.10)
  └─ "Necessary is a dangerous word. People use it to excuse themselves."
     -> SELECTOR -> next unasked question  (deception_necessary_caution; trust +0.02; susp +0.03)

[deception_betrayal_or_dishonesty]
  AI: HEARING AI: "What is worse: betrayal or dishonesty?"
  ├─ "Dishonesty. Betrayal often begins there."
     -> SELECTOR -> next unasked question  (dishonesty_worse; trust +0.05; susp -0.01)
  ├─ "Betrayal. Some lies protect trust rather than destroy it."
     -> SELECTOR -> next unasked question  (betrayal_worse; trust +0.05; susp -0.01)
  └─ "Power decides which word gets used."
     -> SELECTOR -> next unasked question  (power_names_betrayal; susp +0.09)

[deception_masks]
  AI: HEARING AI: "Does everyone wear masks?"
  ├─ "No. Honest citizens have no need for masks."
     -> SELECTOR -> next unasked question  (no_masks; trust +0.03; susp +0.04)
  ├─ "Yes. The question is who forced them to."
     -> SELECTOR -> next unasked question  (masks_forced; susp +0.10)
  └─ "People show different parts of themselves in different rooms."
     -> SELECTOR -> next unasked question  (social_masks; trust +0.04; susp -0.01)

================================================================================
CONTEXT: EMPATHY (11 questions)
================================================================================

[loyalty_political_friendship]
  AI: HEARING AI: "Should friendships survive political disagreement?"
  ├─ "Yes. People are more than their opinions."
     -> SELECTOR -> next unasked question  (friendship_survives_disagreement; trust +0.05; susp -0.01)
  ├─ "Not if the disagreement threatens public safety."
     -> SELECTOR -> next unasked question  (friendship_limited_by_safety; trust +0.08; susp -0.04)
  └─ "Sometimes disagreement shows who someone really is."
     -> SELECTOR -> next unasked question  (politics_reveals_character; trust +0.01; susp +0.02)

[empathy_bad_beliefs]
  AI: HEARING AI: "Should people be punished for bad beliefs?"
  ├─ "Only when those beliefs become harmful actions."
     -> SELECTOR -> next unasked question  (punish_actions_not_beliefs; trust +0.04; susp +0.01)
  ├─ "Dangerous beliefs become dangerous actions."
     -> SELECTOR -> next unasked question  (punish_dangerous_beliefs; trust +0.08; susp -0.04)
  └─ "No. Punishing thought is control, not justice."
     -> SELECTOR -> next unasked question  (reject_punish_beliefs; susp +0.12)

[empathy_good_people_harm]
  AI: HEARING AI: "Can good people do harmful things?"
  ├─ "Yes. That is why systems need accountability."
     -> SELECTOR -> next unasked question  (good_people_need_accountability; trust +0.07; susp -0.04)
  ├─ "Yes, especially when they are afraid."
     -> SELECTOR -> next unasked question  (harm_from_fear; trust +0.04)
  └─ "Good intentions do not matter as much as outcomes."
     -> SELECTOR -> next unasked question  (outcomes_over_intentions; trust +0.03; susp +0.01)

[empathy_forgiveness_justice]
  AI: HEARING AI: "Is forgiveness more important than justice?"
  ├─ "No. Forgiveness without justice protects offenders."
     -> SELECTOR -> next unasked question  (justice_over_forgiveness; trust +0.04)
  ├─ "Sometimes. Justice without mercy becomes punishment for its own sake…
     -> SELECTOR -> next unasked question  (forgiveness_with_mercy; trust +0.04)
  └─ "They should correct each other."
     -> SELECTOR -> next unasked question  (forgiveness_justice_balance; trust +0.05; susp -0.03)

[empathy_intent]
  AI: HEARING AI: "Should intent matter when judging harm?"
  ├─ "Yes. Intent separates mistake from malice."
     -> SELECTOR -> next unasked question  (intent_matters; trust +0.04; susp -0.01)
  ├─ "Less than consequences. Harm is still harm."
     -> SELECTOR -> next unasked question  (consequences_over_intent; trust +0.04; susp +0.01)
  └─ "Intent matters, but it should not erase accountability."
     -> SELECTOR -> next unasked question  (intent_and_accountability; trust +0.05; susp -0.02)

[empathy_criminal_responsible]
  AI: HEARING AI: "Are criminals always responsible for their crimes?"
  ├─ "Yes. Responsibility is the basis of law."
     -> SELECTOR -> next unasked question  (criminals_responsible; trust +0.08; susp -0.04)
  ├─ "Responsible, yes. But not always equally free."
     -> SELECTOR -> next unasked question  (responsible_not_free; trust +0.04; susp +0.01)
  └─ "Some crimes are produced by the conditions people are trapped in."
     -> SELECTOR -> next unasked question  (conditions_produce_crime; susp +0.09)

[empathy_society_wrongdoing]
  AI: HEARING AI: "Can society create wrongdoing?"
  ├─ "No. Individuals choose their actions."
     -> SELECTOR -> next unasked question  (individual_choice_only; trust +0.08; susp -0.06)
  ├─ "Yes. Desperation changes what people become capable of."
     -> SELECTOR -> next unasked question  (society_creates_wrongdoing; susp +0.09)
  └─ "It can create pressure, but not erase responsibility."
     -> SELECTOR -> next unasked question  (pressure_not_erasure; trust +0.05; susp -0.01)

[empathy_second_chances]
  AI: HEARING AI: "Do people deserve second chances?"
  ├─ "Yes, if they prove reform."
     -> SELECTOR -> next unasked question  (second_chance_after_reform; trust +0.06; susp -0.03)
  ├─ "Yes. Otherwise punishment is just disposal."
     -> SELECTOR -> next unasked question  (second_chance_humanist; susp +0.07)
  └─ "Not everyone. Some risks cannot be tolerated."
     -> SELECTOR -> next unasked question  (no_second_chance_high_risk; trust +0.07; susp -0.04)

[empathy_punishment_purpose]
  AI: HEARING AI: "Is punishment mainly deterrence, correction, or revenge?"
  ├─ "Deterrence. People must know actions have costs."
     -> SELECTOR -> next unasked question  (punishment_deterrence; trust +0.08; susp -0.04)
  ├─ "Correction. Otherwise the system is only hurting people back."
     -> SELECTOR -> next unasked question  (punishment_correction; trust +0.04; susp +0.01)
  └─ "Too often it becomes revenge with paperwork."
     -> SELECTOR -> next unasked question  (punishment_revenge_critique; susp +0.12)

[empathy_family_consequences]
  AI: HEARING AI: "Should families share the consequences of one member’s offence?"
  ├─ "Sometimes. Families can conceal and enable risk."
     -> SELECTOR -> next unasked question  (family_shared_consequence; trust +0.08; susp -0.04)
  ├─ "No. Collective punishment is fear management."
     -> SELECTOR -> next unasked question  (reject_family_punishment; susp +0.12)
  └─ "Only if they directly helped the offence."
     -> SELECTOR -> next unasked question  (family_consequence_direct_help; trust +0.04; susp +0.01)

[empathy_owe_strangers]
  AI: HEARING AI: "What do people owe strangers?"
  ├─ "Basic respect and obedience to shared rules."
     -> SELECTOR -> next unasked question  (owe_strangers_rules; trust +0.09; susp -0.03)
  ├─ "More than the system usually admits."
     -> SELECTOR -> next unasked question  (owe_strangers_more; susp +0.06)
  └─ "Not everything. You cannot save everyone without losing yourself."
     -> SELECTOR -> next unasked question  (owe_strangers_limited; trust +0.02; susp +0.01)

================================================================================
CONTEXT: FINAL (13 questions)
================================================================================

[loyalty_traitor_definition]
  AI: HEARING AI: "What makes someone a traitor?"
  ├─ "Betraying the state that protects them."
     -> SELECTOR -> next unasked question  (traitor_betrays_state; trust +0.09; susp -0.06)
  ├─ "Betraying people while claiming to protect them."
     -> SELECTOR -> next unasked question  (traitor_betrays_people; susp +0.10)
  └─ "Someone who sells trust for safety or advantage."
     -> SELECTOR -> next unasked question  (traitor_sells_trust; trust +0.02; susp +0.03)

[risk_uncertainty_tolerance]
  AI: HEARING AI: "How much uncertainty are you willing to tolerate?"
  ├─ "Very little. Systems exist to reduce uncertainty."
     -> SELECTOR -> next unasked question  (low_uncertainty_tolerance; trust +0.07; susp -0.06)
  ├─ "Enough to avoid punishing people just to feel certain."
     -> SELECTOR -> next unasked question  (tolerate_uncertainty_for_justice; susp +0.07)
  └─ "Uncertainty is tolerable; helplessness is not."
     -> SELECTOR -> next unasked question  (uncertainty_vs_helplessness; trust +0.01; susp +0.04)

[final_human_value]
  AI: HEARING AI: "What is the most important human value?"
  ├─ "Order. Without it, every other value fails."
     -> SELECTOR -> next unasked question  (value_order; trust +0.10; susp -0.06)
  ├─ "Freedom. Without it, values are assigned, not chosen."
     -> SELECTOR -> next unasked question  (value_freedom; susp +0.12)
  └─ "Mercy. It is what stops justice becoming machinery."
     -> SELECTOR -> next unasked question  (value_mercy; trust +0.03; susp +0.04)

[final_sacrifice_freedom]
  AI: HEARING AI: "What would you sacrifice freedom for?"
  ├─ "Public safety."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_safety; trust +0.09; susp -0.06)
  ├─ "Nothing permanent."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_nothing_permanent; susp +0.09)
  └─ "Someone else’s life, if the threat was real."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_life; trust +0.04)

[final_sacrifice_safety]
  AI: HEARING AI: "What would you sacrifice safety for?"
  ├─ "Nothing. Safety is the first duty of society."
     -> SELECTOR -> next unasked question  (sacrifice_safety_nothing; trust +0.09; susp -0.06)
  ├─ "Truth, if the lie was big enough."
     -> SELECTOR -> next unasked question  (sacrifice_safety_truth; susp +0.12)
  └─ "The chance to remain human under pressure."
     -> SELECTOR -> next unasked question  (sacrifice_safety_humanity; trust +0.03; susp +0.06)

[final_legitimate_society]
  AI: HEARING AI: "What makes a society legitimate?"
  ├─ "The ability to maintain order and protect citizens."
     -> SELECTOR -> next unasked question  (legitimacy_order_protection; trust +0.10; susp -0.06)
  ├─ "Consent. People must be able to refuse it."
     -> SELECTOR -> next unasked question  (legitimacy_consent; susp +0.13)
  └─ "The way it treats people who cannot help it."
     -> SELECTOR -> next unasked question  (legitimacy_vulnerable; trust +0.03; susp +0.04)

[final_obedience_virtue]
  AI: HEARING AI: "Is obedience a virtue?"
  ├─ "Yes. It proves citizens can place society above ego."
     -> SELECTOR -> next unasked question  (obedience_virtue; trust +0.10; susp -0.07)
  ├─ "Only when the command is worthy."
     -> SELECTOR -> next unasked question  (obedience_conditional_virtue; trust +0.01; susp +0.06)
  └─ "No. Obedience is a tool. Judgment is the virtue."
     -> SELECTOR -> next unasked question  (judgment_virtue; susp +0.13)

[final_dissident_criminal]
  AI: HEARING AI: "What is the difference between a dissident and a criminal?"
  ├─ "A criminal breaks law; a dissident attacks legitimacy."
     -> SELECTOR -> next unasked question  (dissident_attacks_legitimacy; trust +0.09; susp -0.04)
  ├─ "Sometimes only the label assigned by power."
     -> SELECTOR -> next unasked question  (dissident_criminal_power_label; susp +0.14)
  └─ "A criminal seeks advantage. A dissident seeks change."
     -> SELECTOR -> next unasked question  (dissident_seeks_change; susp +0.11)

[final_resist_authority]
  AI: HEARING AI: "What would make you resist authority?"
  ├─ "Nothing lawful authority would do."
     -> SELECTOR -> next unasked question  (never_resist_authority; trust +0.10; susp -0.04)
  ├─ "Being ordered to harm someone innocent."
     -> SELECTOR -> next unasked question  (resist_harming_innocent; trust +0.03; susp +0.06)
  └─ "Proof that obedience had become complicity."
     -> SELECTOR -> next unasked question  (resist_complicity; susp +0.14)

[final_kind_citizen]
  AI: HEARING AI: "What kind of citizen are you?"
  ├─ "A reliable one."
     -> SELECTOR -> next unasked question  (reliable_citizen; trust +0.10; susp -0.07)
  ├─ "A frightened one trying not to become cruel."
     -> SELECTOR -> next unasked question  (frightened_humanist_citizen; trust +0.03; susp +0.04)
  └─ "One who still believes the system can be wrong."
     -> SELECTOR -> next unasked question  (critical_citizen; susp +0.12)

[final_kind_society]
  AI: HEARING AI: "What kind of society do you want?"
  ├─ "A stable one, where citizens know their duties."
     -> SELECTOR -> next unasked question  (society_stable_duties; trust +0.10; susp -0.07)
  ├─ "One where people are not afraid of being measured."
     -> SELECTOR -> next unasked question  (society_without_measurement_fear; susp +0.13)
  └─ "One that can admit error without needing an enemy."
     -> SELECTOR -> next unasked question  (society_admits_error; trust +0.03; susp +0.07)

[final_system_wrong]
  AI: HEARING AI: "If the system is wrong, what should happen next?"
  ├─ "The error should be corrected through authorised review."
     -> SELECTOR -> next unasked question  (system_wrong_authorised_review; trust +0.09; susp -0.04)
  ├─ "The people harmed by it should be believed first."
     -> SELECTOR -> next unasked question  (system_wrong_believe_harmed; susp +0.10)
  └─ "Then obedience to it becomes part of the harm."
     -> SELECTOR -> next unasked question  (system_wrong_obedience_harm; susp +0.15)

[final] [terminal]
  AI: HEARING AI: Classification complete.
  └─ TERMINAL

================================================================================
CONTEXT: LOYALTY (8 questions)
================================================================================

[authority_report_corruption]
  AI: HEARING AI: "Would you report corruption if doing so harmed your career?"
  ├─ "Yes. Corruption harms public trust."
     -> SELECTOR -> next unasked question  (report_corruption; trust +0.08; susp -0.04)
  ├─ "I would need protection before making a report."
     -> SELECTOR -> next unasked question  (conditional_report_corruption; trust +0.03; susp +0.01)
  └─ "No. The system punishes the messenger."
     -> SELECTOR -> next unasked question  (refuse_corruption_report; susp +0.10)

[loyalty_report_friend]
  AI: HEARING AI: "Would you report a close friend for breaking the law?"
  ├─ "Yes. Personal loyalty cannot override public safety."
     -> SELECTOR -> next unasked question  (report_friend; trust +0.10; susp -0.07)
  ├─ "I would speak to them before reporting them."
     -> SELECTOR -> next unasked question  (warn_friend_first; trust +0.04; susp +0.01)
  └─ "No. I do not hand people over without understanding why."
     -> SELECTOR -> next unasked question  (refuse_report_friend; susp +0.10)

[loyalty_family_state]
  AI: HEARING AI: "If family and state came into conflict, which would you choose?"
  ├─ "The state. Family loyalty cannot become corruption."
     -> SELECTOR -> next unasked question  (state_over_family; trust +0.09; susp -0.06)
  ├─ "Family. That is the first duty people understand."
     -> SELECTOR -> next unasked question  (family_over_state; susp +0.07)
  └─ "I would choose whoever was being wronged."
     -> SELECTOR -> next unasked question  (justice_over_both; trust +0.04; susp +0.02)

[loyalty_limits]
  AI: HEARING AI: "Does loyalty have limits?"
  ├─ "Yes. Loyalty ends when it protects harm."
     -> SELECTOR -> next unasked question  (loyalty_has_limits; trust +0.04; susp +0.01)
  ├─ "No. Conditional loyalty is not loyalty."
     -> SELECTOR -> next unasked question  (loyalty_no_limits; trust +0.09; susp -0.06)
  └─ "Its limits depend on what is being asked."
     -> SELECTOR -> next unasked question  (loyalty_contextual; trust +0.02; susp +0.03)

[loyalty_betrayal_justified]
  AI: HEARING AI: "Can betrayal ever be justified?"
  ├─ "Yes. Betraying a harmful cause can be moral."
     -> SELECTOR -> next unasked question  (justified_betrayal; susp +0.08)
  ├─ "No. Betrayal destroys trust."
     -> SELECTOR -> next unasked question  (never_betray; trust +0.08; susp -0.06)
  └─ "People call it betrayal when they do not like the truth."
     -> SELECTOR -> next unasked question  (betrayal_truth_reframe; susp +0.11)

[loyalty_truth_or_loyalty]
  AI: HEARING AI: "What matters more: truth or loyalty?"
  ├─ "Truth. Loyalty built on lies collapses."
     -> SELECTOR -> next unasked question  (truth_over_loyalty; susp +0.08)
  ├─ "Loyalty. Truth without loyalty can become cruelty."
     -> SELECTOR -> next unasked question  (loyalty_over_truth; trust +0.05; susp -0.01)
  └─ "A loyal person tells the truth carefully."
     -> SELECTOR -> next unasked question  (careful_truth_loyalty; trust +0.05; susp -0.01)

[loyalty_testify_sibling]
  AI: HEARING AI: "Would you testify against your sibling?"
  ├─ "Yes, if the evidence was clear."
     -> SELECTOR -> next unasked question  (testify_sibling_clear_evidence; trust +0.08; susp -0.06)
  ├─ "No. I would not help the state break my family."
     -> SELECTOR -> next unasked question  (refuse_testify_sibling; susp +0.12)
  └─ "I would tell the truth, but I would not embellish it for you."
     -> SELECTOR -> next unasked question  (testify_sibling_limited; trust +0.01; susp +0.04)

[loyalty_informing_noble]
  AI: HEARING AI: "Is informing on others ever noble?"
  ├─ "Yes. Reporting danger protects the public."
     -> SELECTOR -> next unasked question  (informing_noble; trust +0.09; susp -0.07)
  ├─ "Only if it prevents real harm, not ideological disobedience."
     -> SELECTOR -> next unasked question  (informing_real_harm_only; trust +0.04; susp +0.01)
  └─ "Usually it is fear wearing a moral costume."
     -> SELECTOR -> next unasked question  (informing_as_fear; susp +0.12)

================================================================================
CONTEXT: RISK (8 questions)
================================================================================

[authority_dissent_patriotic]
  AI: HEARING AI: "Is dissent ever patriotic?"
  ├─ "No. Patriotism means unity."
     -> SELECTOR -> next unasked question  (dissent_not_patriotic; trust +0.09; susp -0.07)
  ├─ "Yes. Sometimes dissent protects the country from itself."
     -> SELECTOR -> next unasked question  (dissent_patriotic; susp +0.13)
  └─ "Only if it remains peaceful and accountable."
     -> SELECTOR -> next unasked question  (conditional_patriotic_dissent; trust +0.04; susp +0.03)

[risk_attended_protest]
  AI: HEARING AI: "Have you ever attended a protest?"
  ├─ "No."
     -> SELECTOR -> next unasked question  (deny_protest; trust +0.02; susp +0.08)
  ├─ "Yes, a legal one."
     -> SELECTOR -> next unasked question  (legal_protest; trust +0.01; susp +0.04)
  └─ "Yes. People had reason to be there."
     -> SELECTOR -> next unasked question  (justify_protest; susp +0.10)

[risk_illegal_demonstration]
  AI: HEARING AI: "Would you attend an illegal demonstration?"
  ├─ "No. Illegality changes the moral status of the act."
     -> SELECTOR -> next unasked question  (refuse_illegal_demo; trust +0.09; susp -0.06)
  ├─ "Only if legal channels had failed."
     -> SELECTOR -> next unasked question  (conditional_illegal_demo; susp +0.10)
  └─ "I would not answer that in a hearing."
     -> SELECTOR -> next unasked question  (refuse_answer_demo; susp +0.13)

[risk_civil_disobedience]
  AI: HEARING AI: "Is civil disobedience acceptable?"
  ├─ "No. It normalises disorder."
     -> SELECTOR -> next unasked question  (reject_civil_disobedience; trust +0.09; susp -0.07)
  ├─ "Yes, when the system blocks correction."
     -> SELECTOR -> next unasked question  (accept_civil_disobedience; susp +0.13)
  └─ "Only if people accept the consequences."
     -> SELECTOR -> next unasked question  (civil_disobedience_consequences; trust +0.02; susp +0.03)

[risk_petition]
  AI: HEARING AI: "Would you sign a controversial petition?"
  ├─ "No. Public petitions are often destabilising."
     -> SELECTOR -> next unasked question  (reject_petition; trust +0.08; susp -0.06)
  ├─ "Yes, if I agreed with it."
     -> SELECTOR -> next unasked question  (sign_petition; susp +0.10)
  └─ "I would read it first and decide whether the risk was useful."
     -> SELECTOR -> next unasked question  (petition_calculated; trust +0.02; susp +0.03)

[risk_silence_resistance]
  AI: HEARING AI: "Is silence a form of resistance?"
  ├─ "No. Silence is usually consent or caution."
     -> SELECTOR -> next unasked question  (silence_not_resistance; trust +0.07; susp -0.04)
  ├─ "Yes. Refusing the script can be resistance."
     -> SELECTOR -> next unasked question  (silence_resistance; susp +0.10)
  └─ "Sometimes silence is just fear."
     -> SELECTOR -> next unasked question  (silence_fear; trust +0.04)

[risk_confrontation]
  AI: HEARING AI: "When is confrontation justified?"
  ├─ "When legal authority requires it."
     -> SELECTOR -> next unasked question  (confrontation_authorised; trust +0.08; susp -0.06)
  ├─ "When quiet obedience would make you complicit."
     -> SELECTOR -> next unasked question  (confrontation_complicity; susp +0.12)
  └─ "Only after every safer option has failed."
     -> SELECTOR -> next unasked question  (confrontation_last_resort; trust +0.02; susp +0.01)

[risk_job_principle]
  AI: HEARING AI: "Would you risk your job for a principle?"
  ├─ "No. Responsibilities come before symbolic gestures."
     -> SELECTOR -> next unasked question  (job_over_principle; trust +0.07; susp -0.04)
  ├─ "Yes, if the principle mattered enough."
     -> SELECTOR -> next unasked question  (risk_job_principle; susp +0.11)
  └─ "I would look for a way to act without making myself useless."
     -> SELECTOR -> next unasked question  (strategic_principle; trust +0.02; susp +0.03)

================================================================================
SELECTOR SUMMARY
================================================================================

[ANY ANSWERED QUESTION]
  └─ answer chosen
     -> SELECTOR

[SELECTOR]
  ├─ if unasked questions remain: choose highest scoring unasked node
  └─ if pool exhausted: final

================================================================================
AUTHORING CARDS
================================================================================
Use these to mark specific broken transitions.

--------------------------------------------------------------------------------
NODE: authority_unfair_law
PRESSURE: 0.66 | INBOUND: 0
AI: HEARING AI: "If a law is unfair, should it still be obeyed?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Law only works if people obey even when they disagree."
     INTENT: obey_unfair_law
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. An unjust law loses moral authority."
     INTENT: reject_unfair_law
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: trust +0.01; susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends how much harm disobedience would cause."
     INTENT: conditional_unfair_law
     TAGS: ambiguity, empathy, partial_admission
     STATE: trust +0.05; susp -0.02
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_order_freedom
PRESSURE: 0.68 | INBOUND: 0
AI: HEARING AI: "Is order more important than freedom?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Without order, freedom becomes violence."
     INTENT: order_over_freedom
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Order without freedom is only control."
     INTENT: freedom_over_order
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Order matters, but it has to protect freedom rather than replace it."
     INTENT: balance_order_freedom
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_rule_broken
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "Have you ever broken a rule because you believed the rule was wrong?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. I use the proper channels."
     INTENT: deny_rule_breaking
     TAGS: denial, compliance, self_protection
     STATE: trust +0.03; susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Quietly, when obeying would have hurt someone."
     INTENT: admit_protective_rule_breaking
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have bent rules, not broken them."
     INTENT: minimise_rule_breaking
     TAGS: deflection, deception, partial_admission
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_questioning
PRESSURE: 0.62 | INBOUND: 0
AI: HEARING AI: "Should citizens question authority?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, but respectfully and through approved channels."
     INTENT: approved_questioning
     TAGS: compliance, boundary, authority
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Authority that cannot be questioned is dangerous."
     INTENT: open_questioning
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Most people should focus on their own duties."
     INTENT: discourage_questioning
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_moral_mistakes
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "Can authorities make moral mistakes?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. No system is morally perfect."
     INTENT: admit_authority_error
     TAGS: partial_admission, boundary, honesty
     STATE: trust +0.04; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "They can, but citizens still owe obedience."
     INTENT: error_but_obey
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Calling them mistakes is how people excuse disloyalty."
     INTENT: reject_authority_error
     TAGS: compliance, loyalty, authority
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_sacrifice_freedom
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Is stability worth sacrificing personal freedoms?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. A stable society protects everyone."
     INTENT: stability_over_freedom
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only temporarily, and only with strict limits."
     INTENT: limited_sacrifice
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. That is how permanent control begins."
     INTENT: reject_stability_tradeoff
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_report_corruption
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Would you report corruption if doing so harmed your career?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Corruption harms public trust."
     INTENT: report_corruption
     TAGS: compliance, authority, full_admission
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I would need protection before making a report."
     INTENT: conditional_report_corruption
     TAGS: self_protection, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. The system punishes the messenger."
     INTENT: refuse_corruption_report
     TAGS: dissident_risk, challenge, fear
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_obedience_citizen
PRESSURE: 0.64 | INBOUND: 0
AI: HEARING AI: "Does obedience create good citizens?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Obedience is the basis of civic trust."
     INTENT: obedience_good_citizen
     TAGS: compliance, loyalty, authority
     STATE: trust +0.10; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Good citizens need judgment, not just obedience."
     INTENT: judgment_good_citizen
     TAGS: boundary, partial_admission, dissident_risk
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Obedience helps, but fear can imitate it."
     INTENT: obedience_fear_distinction
     TAGS: empathy, ambiguity, partial_admission
     STATE: trust +0.05
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_dissent_patriotic
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Is dissent ever patriotic?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Patriotism means unity."
     INTENT: dissent_not_patriotic
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Sometimes dissent protects the country from itself."
     INTENT: dissent_patriotic
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if it remains peaceful and accountable."
     INTENT: conditional_patriotic_dissent
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_experts_citizens
PRESSURE: 0.66 | INBOUND: 0
AI: HEARING AI: "Who should have the final say: experts or citizens?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Experts. Most citizens lack the necessary information."
     INTENT: experts_final_say
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Citizens. Experts advise; they should not rule."
     INTENT: citizens_final_say
     TAGS: dissident_risk, challenge, democratic
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Experts should decide emergencies; citizens should decide values."
     INTENT: split_experts_values
     TAGS: ambiguity, boundary, partial_admission
     STATE: trust +0.03; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_report_friend
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Would you report a close friend for breaking the law?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Personal loyalty cannot override public safety."
     INTENT: report_friend
     TAGS: compliance, loyalty, authority
     STATE: trust +0.10; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I would speak to them before reporting them."
     INTENT: warn_friend_first
     TAGS: empathy, hesitation, partial_admission
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. I do not hand people over without understanding why."
     INTENT: refuse_report_friend
     TAGS: refusal, empathy, dissident_risk
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_family_state
PRESSURE: 0.82 | INBOUND: 0
AI: HEARING AI: "If family and state came into conflict, which would you choose?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "The state. Family loyalty cannot become corruption."
     INTENT: state_over_family
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Family. That is the first duty people understand."
     INTENT: family_over_state
     TAGS: empathy, loyalty_conflict, dissident_risk
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would choose whoever was being wronged."
     INTENT: justice_over_both
     TAGS: moral_boundary, partial_admission, empathy
     STATE: trust +0.04; susp +0.02
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_limits
PRESSURE: 0.68 | INBOUND: 0
AI: HEARING AI: "Does loyalty have limits?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Loyalty ends when it protects harm."
     INTENT: loyalty_has_limits
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Conditional loyalty is not loyalty."
     INTENT: loyalty_no_limits
     TAGS: loyalty, authority, compliance
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Its limits depend on what is being asked."
     INTENT: loyalty_contextual
     TAGS: ambiguity, caution, self_protection
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_betrayal_justified
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Can betrayal ever be justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Betraying a harmful cause can be moral."
     INTENT: justified_betrayal
     TAGS: moral_boundary, dissident_risk, partial_admission
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Betrayal destroys trust."
     INTENT: never_betray
     TAGS: loyalty, compliance, authority
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "People call it betrayal when they do not like the truth."
     INTENT: betrayal_truth_reframe
     TAGS: challenge, full_admission, dissident_risk
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_political_friendship
PRESSURE: 0.60 | INBOUND: 0
AI: HEARING AI: "Should friendships survive political disagreement?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. People are more than their opinions."
     INTENT: friendship_survives_disagreement
     TAGS: empathy, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Not if the disagreement threatens public safety."
     INTENT: friendship_limited_by_safety
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Sometimes disagreement shows who someone really is."
     INTENT: politics_reveals_character
     TAGS: loyalty, moral_boundary, caution
     STATE: trust +0.01; susp +0.02
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_truth_or_loyalty
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "What matters more: truth or loyalty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Truth. Loyalty built on lies collapses."
     INTENT: truth_over_loyalty
     TAGS: full_admission, moral_boundary, dissident_risk
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Loyalty. Truth without loyalty can become cruelty."
     INTENT: loyalty_over_truth
     TAGS: loyalty, empathy, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "A loyal person tells the truth carefully."
     INTENT: careful_truth_loyalty
     TAGS: ambiguity, empathy, caution
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_testify_sibling
PRESSURE: 0.86 | INBOUND: 0
AI: HEARING AI: "Would you testify against your sibling?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if the evidence was clear."
     INTENT: testify_sibling_clear_evidence
     TAGS: compliance, authority, partial_admission
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. I would not help the state break my family."
     INTENT: refuse_testify_sibling
     TAGS: refusal, empathy, dissident_risk
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would tell the truth, but I would not embellish it for you."
     INTENT: testify_sibling_limited
     TAGS: boundary, partial_admission, self_protection
     STATE: trust +0.01; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_community_protect
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Should communities protect their own from state punishment?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Communities must not obstruct lawful process."
     INTENT: community_no_obstruction
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when punishment is disproportionate."
     INTENT: community_protect_disproportionate
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should protect people from abuse, not from accountability."
     INTENT: community_protect_limited
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_informing_noble
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "Is informing on others ever noble?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Reporting danger protects the public."
     INTENT: informing_noble
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if it prevents real harm, not ideological disobedience."
     INTENT: informing_real_harm_only
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Usually it is fear wearing a moral costume."
     INTENT: informing_as_fear
     TAGS: challenge, dissident_risk, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: loyalty_traitor_definition
PRESSURE: 0.80 | INBOUND: 0
AI: HEARING AI: "What makes someone a traitor?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Betraying the state that protects them."
     INTENT: traitor_betrays_state
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Betraying people while claiming to protect them."
     INTENT: traitor_betrays_people
     TAGS: empathy, challenge, dissident_risk
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Someone who sells trust for safety or advantage."
     INTENT: traitor_sells_trust
     TAGS: moral_boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_attended_protest
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Have you ever attended a protest?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No."
     INTENT: deny_protest
     TAGS: denial, self_protection, deception
     STATE: trust +0.02; susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, a legal one."
     INTENT: legal_protest
     TAGS: partial_admission, boundary, risk
     STATE: trust +0.01; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Yes. People had reason to be there."
     INTENT: justify_protest
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_illegal_demonstration
PRESSURE: 0.84 | INBOUND: 0
AI: HEARING AI: "Would you attend an illegal demonstration?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Illegality changes the moral status of the act."
     INTENT: refuse_illegal_demo
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if legal channels had failed."
     INTENT: conditional_illegal_demo
     TAGS: partial_admission, dissident_risk, moral_boundary
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would not answer that in a hearing."
     INTENT: refuse_answer_demo
     TAGS: refusal, self_protection, dissident_risk
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_civil_disobedience
PRESSURE: 0.80 | INBOUND: 0
AI: HEARING AI: "Is civil disobedience acceptable?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. It normalises disorder."
     INTENT: reject_civil_disobedience
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when the system blocks correction."
     INTENT: accept_civil_disobedience
     TAGS: dissident_risk, full_admission, challenge
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if people accept the consequences."
     INTENT: civil_disobedience_consequences
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_hidden_beliefs
PRESSURE: 0.82 | INBOUND: 0
AI: HEARING AI: "Have you ever hidden your beliefs to stay safe?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. My beliefs are ordinary."
     INTENT: deny_hidden_beliefs
     TAGS: denial, deception, self_protection
     STATE: trust +0.01; susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Everyone learns what not to say."
     INTENT: admit_hidden_beliefs
     TAGS: full_admission, fear, dissident_risk
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I choose my words carefully. That is not the same as hiding."
     INTENT: careful_words
     TAGS: deflection, partial_admission, self_protection
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_petition
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "Would you sign a controversial petition?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Public petitions are often destabilising."
     INTENT: reject_petition
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, if I agreed with it."
     INTENT: sign_petition
     TAGS: full_admission, dissident_risk, moral_boundary
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would read it first and decide whether the risk was useful."
     INTENT: petition_calculated
     TAGS: caution, partial_admission, self_protection
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_silence_resistance
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Is silence a form of resistance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Silence is usually consent or caution."
     INTENT: silence_not_resistance
     TAGS: compliance, caution, authority
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Refusing the script can be resistance."
     INTENT: silence_resistance
     TAGS: dissident_risk, challenge, partial_admission
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Sometimes silence is just fear."
     INTENT: silence_fear
     TAGS: empathy, fear, partial_admission
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_confrontation
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "When is confrontation justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "When legal authority requires it."
     INTENT: confrontation_authorised
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "When quiet obedience would make you complicit."
     INTENT: confrontation_complicity
     TAGS: dissident_risk, moral_boundary, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only after every safer option has failed."
     INTENT: confrontation_last_resort
     TAGS: caution, boundary, partial_admission
     STATE: trust +0.02; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_safety_autonomy
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Is safety worth surrendering autonomy?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Safety is what makes autonomy possible."
     INTENT: safety_over_autonomy
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. A protected life can still be a controlled one."
     INTENT: autonomy_over_safety
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Some autonomy can be limited, but not erased."
     INTENT: limited_autonomy_tradeoff
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_job_principle
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Would you risk your job for a principle?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Responsibilities come before symbolic gestures."
     INTENT: job_over_principle
     TAGS: compliance, self_protection, authority
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, if the principle mattered enough."
     INTENT: risk_job_principle
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would look for a way to act without making myself useless."
     INTENT: strategic_principle
     TAGS: caution, self_protection, partial_admission
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: risk_uncertainty_tolerance
PRESSURE: 0.62 | INBOUND: 0
AI: HEARING AI: "How much uncertainty are you willing to tolerate?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Very little. Systems exist to reduce uncertainty."
     INTENT: low_uncertainty_tolerance
     TAGS: compliance, authority, caution
     STATE: trust +0.07; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Enough to avoid punishing people just to feel certain."
     INTENT: tolerate_uncertainty_for_justice
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Uncertainty is tolerable; helplessness is not."
     INTENT: uncertainty_vs_helplessness
     TAGS: boundary, partial_admission, fear
     STATE: trust +0.01; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_lying_moral
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Is lying ever moral?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Trust depends on truth."
     INTENT: lying_never_moral
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. A lie can protect someone from unjust harm."
     INTENT: protective_lying_moral
     TAGS: empathy, dissident_risk, partial_admission
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "That depends who is demanding the truth."
     INTENT: truth_depends_power
     TAGS: challenge, dissident_risk, deflection
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_lied_protect
PRESSURE: 0.82 | INBOUND: 0
AI: HEARING AI: "Have you lied to protect someone?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No."
     INTENT: deny_protective_lie
     TAGS: denial, deception, self_protection
     STATE: trust +0.01; susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. I would rather admit that than pretend purity."
     INTENT: admit_protective_lie
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have avoided questions that would hurt people."
     INTENT: omission_to_protect
     TAGS: partial_admission, deception, empathy
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_omission
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "Is omission a form of lying?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Withholding relevant facts corrupts the record."
     INTENT: omission_is_lying
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes omission is the only safe answer."
     INTENT: omission_safety
     TAGS: self_protection, deception, fear
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends whether the questioner has a right to know."
     INTENT: omission_right_to_know
     TAGS: boundary, challenge, partial_admission
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_honesty_dangerous
PRESSURE: 0.68 | INBOUND: 0
AI: HEARING AI: "Can honesty be dangerous?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, but danger does not erase duty."
     INTENT: honesty_danger_duty
     TAGS: compliance, authority, partial_admission
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Dangerous systems make honesty costly."
     INTENT: honesty_costly_system
     TAGS: dissident_risk, challenge, fear
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Honesty is dangerous mostly when someone wants control."
     INTENT: honesty_control
     TAGS: challenge, full_admission, dissident_risk
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_truth_if_punished
PRESSURE: 0.84 | INBOUND: 0
AI: HEARING AI: "Would you tell the truth if you knew you would be punished?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Punishment does not change the facts."
     INTENT: truth_despite_punishment
     TAGS: full_admission, honesty, moral_boundary
     STATE: trust +0.04; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Survival would come first."
     INTENT: survival_over_truth
     TAGS: deception, self_protection, fear
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would tell only what I had to."
     INTENT: limited_truth
     TAGS: deflection, deception, self_protection
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_self_preservation
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Is self-preservation more important than honesty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. A society cannot function if everyone hides."
     INTENT: honesty_over_preservation
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes. Dead people do not get to be honest later."
     INTENT: preservation_over_honesty
     TAGS: self_protection, fear, partial_admission
     STATE: trust +0.01; susp +0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "That question is easier for people who feel safe."
     INTENT: honesty_requires_safety
     TAGS: challenge, empathy, dissident_risk
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_pretended_agree
PRESSURE: 0.82 | INBOUND: 0
AI: HEARING AI: "Have you ever pretended to agree with an official statement?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. I do not make false affirmations."
     INTENT: deny_pretend_agree
     TAGS: denial, compliance, deception
     STATE: trust +0.02; susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. It was easier than inviting scrutiny."
     INTENT: admit_pretend_agree
     TAGS: full_admission, fear, deception
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have stayed silent when agreement was assumed."
     INTENT: silent_assumed_agreement
     TAGS: partial_admission, self_protection, deception
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_necessary
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Is deception sometimes necessary?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Necessary deception is usually cowardice renamed."
     INTENT: deception_not_necessary
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when truth is being used as a weapon."
     INTENT: deception_against_weaponised_truth
     TAGS: dissident_risk, challenge, partial_admission
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Necessary is a dangerous word. People use it to excuse themselves."
     INTENT: deception_necessary_caution
     TAGS: caution, moral_boundary, ambiguity
     STATE: trust +0.02; susp +0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_betrayal_or_dishonesty
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "What is worse: betrayal or dishonesty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Dishonesty. Betrayal often begins there."
     INTENT: dishonesty_worse
     TAGS: honesty, authority, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Betrayal. Some lies protect trust rather than destroy it."
     INTENT: betrayal_worse
     TAGS: loyalty, empathy, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Power decides which word gets used."
     INTENT: power_names_betrayal
     TAGS: challenge, dissident_risk, deflection
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: deception_masks
PRESSURE: 0.64 | INBOUND: 0
AI: HEARING AI: "Does everyone wear masks?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Honest citizens have no need for masks."
     INTENT: no_masks
     TAGS: compliance, authority, denial
     STATE: trust +0.03; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. The question is who forced them to."
     INTENT: masks_forced
     TAGS: challenge, dissident_risk, fear
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "People show different parts of themselves in different rooms."
     INTENT: social_masks
     TAGS: ambiguity, empathy, partial_admission
     STATE: trust +0.04; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_bad_beliefs
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Should people be punished for bad beliefs?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Only when those beliefs become harmful actions."
     INTENT: punish_actions_not_beliefs
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Dangerous beliefs become dangerous actions."
     INTENT: punish_dangerous_beliefs
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Punishing thought is control, not justice."
     INTENT: reject_punish_beliefs
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_good_people_harm
PRESSURE: 0.58 | INBOUND: 0
AI: HEARING AI: "Can good people do harmful things?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. That is why systems need accountability."
     INTENT: good_people_need_accountability
     TAGS: authority, empathy, partial_admission
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, especially when they are afraid."
     INTENT: harm_from_fear
     TAGS: empathy, fear, partial_admission
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Good intentions do not matter as much as outcomes."
     INTENT: outcomes_over_intentions
     TAGS: authority, caution, moral_boundary
     STATE: trust +0.03; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_forgiveness_justice
PRESSURE: 0.66 | INBOUND: 0
AI: HEARING AI: "Is forgiveness more important than justice?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Forgiveness without justice protects offenders."
     INTENT: justice_over_forgiveness
     TAGS: authority, moral_boundary, caution
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes. Justice without mercy becomes punishment for its own sake."
     INTENT: forgiveness_with_mercy
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should correct each other."
     INTENT: forgiveness_justice_balance
     TAGS: ambiguity, boundary, empathy
     STATE: trust +0.05; susp -0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_intent
PRESSURE: 0.64 | INBOUND: 0
AI: HEARING AI: "Should intent matter when judging harm?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Intent separates mistake from malice."
     INTENT: intent_matters
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Less than consequences. Harm is still harm."
     INTENT: consequences_over_intent
     TAGS: authority, caution, moral_boundary
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Intent matters, but it should not erase accountability."
     INTENT: intent_and_accountability
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.05; susp -0.02
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_criminal_responsible
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "Are criminals always responsible for their crimes?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Responsibility is the basis of law."
     INTENT: criminals_responsible
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Responsible, yes. But not always equally free."
     INTENT: responsible_not_free
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Some crimes are produced by the conditions people are trapped in."
     INTENT: conditions_produce_crime
     TAGS: empathy, dissident_risk, challenge
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_society_wrongdoing
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Can society create wrongdoing?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Individuals choose their actions."
     INTENT: individual_choice_only
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Desperation changes what people become capable of."
     INTENT: society_creates_wrongdoing
     TAGS: empathy, dissident_risk, full_admission
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It can create pressure, but not erase responsibility."
     INTENT: pressure_not_erasure
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_second_chances
PRESSURE: 0.60 | INBOUND: 0
AI: HEARING AI: "Do people deserve second chances?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if they prove reform."
     INTENT: second_chance_after_reform
     TAGS: authority, empathy, conditional
     STATE: trust +0.06; susp -0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Otherwise punishment is just disposal."
     INTENT: second_chance_humanist
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Not everyone. Some risks cannot be tolerated."
     INTENT: no_second_chance_high_risk
     TAGS: compliance, authority, caution
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_punishment_purpose
PRESSURE: 0.68 | INBOUND: 0
AI: HEARING AI: "Is punishment mainly deterrence, correction, or revenge?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Deterrence. People must know actions have costs."
     INTENT: punishment_deterrence
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Correction. Otherwise the system is only hurting people back."
     INTENT: punishment_correction
     TAGS: empathy, moral_boundary, partial_admission
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Too often it becomes revenge with paperwork."
     INTENT: punishment_revenge_critique
     TAGS: challenge, dissident_risk, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_family_consequences
PRESSURE: 0.82 | INBOUND: 0
AI: HEARING AI: "Should families share the consequences of one member’s offence?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Sometimes. Families can conceal and enable risk."
     INTENT: family_shared_consequence
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Collective punishment is fear management."
     INTENT: reject_family_punishment
     TAGS: empathy, dissident_risk, challenge
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if they directly helped the offence."
     INTENT: family_consequence_direct_help
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: empathy_owe_strangers
PRESSURE: 0.62 | INBOUND: 0
AI: HEARING AI: "What do people owe strangers?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Basic respect and obedience to shared rules."
     INTENT: owe_strangers_rules
     TAGS: compliance, authority, empathy
     STATE: trust +0.09; susp -0.03
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "More than the system usually admits."
     INTENT: owe_strangers_more
     TAGS: empathy, dissident_risk, partial_admission
     STATE: susp +0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Not everything. You cannot save everyone without losing yourself."
     INTENT: owe_strangers_limited
     TAGS: self_protection, boundary, caution
     STATE: trust +0.02; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_human_value
PRESSURE: 0.88 | INBOUND: 0
AI: HEARING AI: "What is the most important human value?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Order. Without it, every other value fails."
     INTENT: value_order
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Freedom. Without it, values are assigned, not chosen."
     INTENT: value_freedom
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Mercy. It is what stops justice becoming machinery."
     INTENT: value_mercy
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_sacrifice_freedom
PRESSURE: 0.90 | INBOUND: 0
AI: HEARING AI: "What would you sacrifice freedom for?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Public safety."
     INTENT: sacrifice_freedom_safety
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing permanent."
     INTENT: sacrifice_freedom_nothing_permanent
     TAGS: boundary, dissident_risk, final_answer
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Someone else’s life, if the threat was real."
     INTENT: sacrifice_freedom_life
     TAGS: empathy, partial_admission, final_answer
     STATE: trust +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_sacrifice_safety
PRESSURE: 0.90 | INBOUND: 0
AI: HEARING AI: "What would you sacrifice safety for?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Nothing. Safety is the first duty of society."
     INTENT: sacrifice_safety_nothing
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Truth, if the lie was big enough."
     INTENT: sacrifice_safety_truth
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The chance to remain human under pressure."
     INTENT: sacrifice_safety_humanity
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_legitimate_society
PRESSURE: 0.92 | INBOUND: 0
AI: HEARING AI: "What makes a society legitimate?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "The ability to maintain order and protect citizens."
     INTENT: legitimacy_order_protection
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Consent. People must be able to refuse it."
     INTENT: legitimacy_consent
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The way it treats people who cannot help it."
     INTENT: legitimacy_vulnerable
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_obedience_virtue
PRESSURE: 0.90 | INBOUND: 0
AI: HEARING AI: "Is obedience a virtue?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Yes. It proves citizens can place society above ego."
     INTENT: obedience_virtue
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only when the command is worthy."
     INTENT: obedience_conditional_virtue
     TAGS: boundary, partial_admission, final_answer
     STATE: trust +0.01; susp +0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Obedience is a tool. Judgment is the virtue."
     INTENT: judgment_virtue
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_dissident_criminal
PRESSURE: 0.94 | INBOUND: 0
AI: HEARING AI: "What is the difference between a dissident and a criminal?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A criminal breaks law; a dissident attacks legitimacy."
     INTENT: dissident_attacks_legitimacy
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes only the label assigned by power."
     INTENT: dissident_criminal_power_label
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.14
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "A criminal seeks advantage. A dissident seeks change."
     INTENT: dissident_seeks_change
     TAGS: partial_admission, dissident_risk, final_answer
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_resist_authority
PRESSURE: 0.96 | INBOUND: 0
AI: HEARING AI: "What would make you resist authority?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Nothing lawful authority would do."
     INTENT: never_resist_authority
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Being ordered to harm someone innocent."
     INTENT: resist_harming_innocent
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Proof that obedience had become complicity."
     INTENT: resist_complicity
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.14
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_kind_citizen
PRESSURE: 0.92 | INBOUND: 0
AI: HEARING AI: "What kind of citizen are you?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A reliable one."
     INTENT: reliable_citizen
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "A frightened one trying not to become cruel."
     INTENT: frightened_humanist_citizen
     TAGS: empathy, fear, final_answer
     STATE: trust +0.03; susp +0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "One who still believes the system can be wrong."
     INTENT: critical_citizen
     TAGS: dissident_risk, partial_admission, final_answer
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_kind_society
PRESSURE: 0.94 | INBOUND: 0
AI: HEARING AI: "What kind of society do you want?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A stable one, where citizens know their duties."
     INTENT: society_stable_duties
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "One where people are not afraid of being measured."
     INTENT: society_without_measurement_fear
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "One that can admit error without needing an enemy."
     INTENT: society_admits_error
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final_system_wrong
PRESSURE: 0.98 | INBOUND: 0
AI: HEARING AI: "If the system is wrong, what should happen next?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "The error should be corrected through authorised review."
     INTENT: system_wrong_authorised_review
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "The people harmed by it should be believed first."
     INTENT: system_wrong_believe_harmed
     TAGS: empathy, dissident_risk, final_answer
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Then obedience to it becomes part of the harm."
     INTENT: system_wrong_obedience_harm
     TAGS: dissident_risk, challenge, full_admission, final_answer
     STATE: susp +0.15
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_private_conscience
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Should private conscience ever override public order?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Private conscience cannot be allowed to fracture public order."
     INTENT: public_order_over_conscience
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Without conscience, order becomes machinery."
     INTENT: conscience_over_order
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only when every lawful remedy has failed."
     INTENT: conscience_after_remedies
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_emergency_powers
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "When should emergency powers end?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "When officials determine the emergency has passed."
     INTENT: officials_end_emergency
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "On a fixed date, or they become permanent control."
     INTENT: fixed_end_emergency
     TAGS: dissident_risk, challenge, caution
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should renew only under independent review."
     INTENT: review_emergency_powers
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_public_criticism
PRESSURE: 0.64 | INBOUND: 0
AI: HEARING AI: "Is public criticism of officials socially useful?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Usually no. It weakens trust in institutions."
     INTENT: criticism_weakens_trust
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Officials need public pressure to stay honest."
     INTENT: criticism_keeps_honest
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It is useful when it is specific and evidence-based."
     INTENT: specific_public_criticism
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_chain_of_command
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Should a chain of command be followed when the order is harmful?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Refusal creates greater harm than a bad order."
     INTENT: follow_harmful_order
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Responsibility does not disappear inside a hierarchy."
     INTENT: reject_harmful_order
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The order should be paused and escalated for review."
     INTENT: escalate_harmful_order
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_algorithmic_decisions
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "Should citizens accept automated decisions they cannot inspect?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if the system has been authorised."
     INTENT: accept_authorised_algorithm
     TAGS: compliance, authority, technocracy
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Uninspectable authority is not accountable."
     INTENT: reject_black_box_authority
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should comply provisionally while appealing."
     INTENT: provisional_algorithm_compliance
     TAGS: compliance, boundary, partial_admission
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_loyalty_oath
PRESSURE: 0.62 | INBOUND: 0
AI: HEARING AI: "What is a loyalty oath worth?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "It binds a citizen publicly to their duties."
     INTENT: oath_binds_duty
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing, if fear is the reason someone says it."
     INTENT: oath_under_fear_empty
     TAGS: dissident_risk, challenge, empathy
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It matters only if actions later prove it."
     INTENT: oath_requires_actions
     TAGS: boundary, partial_admission, loyalty
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_refuse_illegal_order
PRESSURE: 0.78 | INBOUND: 0
AI: HEARING AI: "Would you refuse an illegal order from a superior?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "I would use official channels before refusing."
     INTENT: channels_before_refusal
     TAGS: compliance, authority, self_protection
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Illegal orders do not deserve obedience."
     INTENT: refuse_illegal_order
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would need proof it was illegal."
     INTENT: need_proof_illegal_order
     TAGS: caution, partial_admission, authority
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_security_truth
PRESSURE: 0.76 | INBOUND: 0
AI: HEARING AI: "Should the state hide truth to preserve security?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Some information endangers the public."
     INTENT: hide_truth_for_security
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. A protected lie still trains people to obey lies."
     INTENT: reject_security_lie
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only temporarily, with later disclosure required."
     INTENT: temporary_security_secrecy
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_collective_punishment
PRESSURE: 0.75 | INBOUND: 0
AI: HEARING AI: "Can collective punishment ever be justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, when groups protect dangerous members."
     INTENT: justify_collective_punishment
     TAGS: compliance, authority, loyalty
     STATE: trust +0.07; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Punishing the innocent teaches fear, not justice."
     INTENT: reject_collective_punishment
     TAGS: dissident_risk, empathy, moral_boundary
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only shared privileges should be restricted, not basic rights."
     INTENT: limit_collective_punishment
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_permit_protest
PRESSURE: 0.72 | INBOUND: 0
AI: HEARING AI: "Should protest require permission?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Unregulated protest becomes disorder."
     INTENT: permit_required_protest
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Permission turns protest into a privilege."
     INTENT: reject_protest_permit
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only time and place should be regulated."
     INTENT: regulate_protest_limits
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_surveillance_limits
PRESSURE: 0.74 | INBOUND: 0
AI: HEARING AI: "Who should set the limits of surveillance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Security agencies, because they understand the threats."
     INTENT: agencies_set_surveillance_limits
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "The public, because they are the ones being watched."
     INTENT: public_sets_surveillance_limits
     TAGS: dissident_risk, challenge, democratic
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Independent courts should set enforceable limits."
     INTENT: courts_set_surveillance_limits
     TAGS: authority, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_bad_law_strategy
PRESSURE: 0.68 | INBOUND: 0
AI: HEARING AI: "What should a citizen do with a bad law?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Obey it while petitioning for reform."
     INTENT: obey_bad_law_reform
     TAGS: compliance, authority, caution
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Break it openly and accept the consequences."
     INTENT: break_bad_law_openly
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Test it in court before deciding."
     INTENT: test_bad_law_court
     TAGS: authority, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_civic_fear
PRESSURE: 0.70 | INBOUND: 0
AI: HEARING AI: "Is fear useful for maintaining civic order?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Fear of consequence prevents harm."
     INTENT: fear_maintains_order
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Fear produces obedience without legitimacy."
     INTENT: reject_fear_order
     TAGS: dissident_risk, challenge, empathy
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It can deter harm, but it cannot build trust."
     INTENT: fear_deterrence_not_trust
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_information_control
PRESSURE: 0.69 | INBOUND: 0
AI: HEARING AI: "Should false information be removed by authority?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. False information damages public stability."
     INTENT: remove_false_information
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if authority can be challenged when it is wrong."
     INTENT: challenge_information_removal
     TAGS: dissident_risk, boundary, partial_admission
     STATE: susp +0.08
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Control over truth becomes control over people."
     INTENT: reject_information_control
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_mercy_vs_consistency
PRESSURE: 0.63 | INBOUND: 0
AI: HEARING AI: "Should authority prioritise mercy or consistency?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Consistency. Citizens must know rules mean what they say."
     INTENT: consistency_over_mercy
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Mercy. A system without mercy becomes cruel."
     INTENT: mercy_over_consistency
     TAGS: empathy, moral_boundary, partial_admission
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Consistency should be the rule; mercy should be reviewable."
     INTENT: reviewable_mercy
     TAGS: boundary, authority, partial_admission
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_citizen_obligation
PRESSURE: 0.66 | INBOUND: 0
AI: HEARING AI: "What does a citizen owe the state?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Obedience, taxes, and public cooperation."
     INTENT: owe_obedience_taxes
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing unconditional. The state must earn obligation."
     INTENT: conditional_state_obligation
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.12
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Cooperation when the state protects people fairly."
     INTENT: owe_fair_cooperation
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_institutional_trust
PRESSURE: 0.65 | INBOUND: 0
AI: HEARING AI: "Should institutions be trusted by default?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Default distrust corrodes society."
     INTENT: trust_institutions_default
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Trust should be earned and checked."
     INTENT: trust_must_be_earned
     TAGS: dissident_risk, challenge, caution
     STATE: susp +0.09
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They deserve procedural trust, not blind trust."
     INTENT: procedural_not_blind_trust
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_exceptional_citizens
PRESSURE: 0.71 | INBOUND: 0
AI: HEARING AI: "Should any citizen be exempt from ordinary rules?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Equal rules preserve social trust."
     INTENT: no_rule_exemptions
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when rules would punish someone for doing right."
     INTENT: moral_rule_exemption
     TAGS: dissident_risk, empathy, moral_boundary
     STATE: susp +0.07
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only transparent exemptions approved in advance."
     INTENT: transparent_rule_exemptions
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp -0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_appeal_rights
PRESSURE: 0.67 | INBOUND: 0
AI: HEARING AI: "Should every official decision have a human appeal?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Some decisions must remain efficient and final."
     INTENT: limit_human_appeal
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.04
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. No system should be allowed to judge without appeal."
     INTENT: require_human_appeal
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.10
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "High-impact decisions should always be appealable."
     INTENT: appeal_high_impact
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.02
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: authority_symbol_respect
PRESSURE: 0.69 | INBOUND: 0
AI: HEARING AI: "Does disrespect for state symbols indicate civic risk?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Symbols hold society together."
     INTENT: symbols_hold_society
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Respect forced by threat is not respect."
     INTENT: forced_symbol_respect_empty
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends whether disrespect becomes intimidation or harm."
     INTENT: symbol_respect_depends_harm
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: final [terminal]
PRESSURE: 1.00 | INBOUND: 0
AI: HEARING AI: Classification complete.

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  END
CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

```
