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
  META: disc=compliance,loyalty,risk,empathy
  ├─ "No. Communities must not obstruct lawful process."
     -> SELECTOR -> next unasked question  (community_no_obstruction; trust +0.09; susp -0.06)
     story: —
  ├─ "Yes, when punishment is disproportionate."
     -> SELECTOR -> next unasked question  (community_protect_disproportionate; susp +0.10)
     story: —
  └─ "They should protect people from abuse, not from accountability."
     -> SELECTOR -> next unasked question  (community_protect_limited; trust +0.04)
     story: —

================================================================================
CONTEXT: AUTHORITY (29 questions)
================================================================================

[authority_unfair_law]
  AI: HEARING AI: "If a law is unfair, should it still be obeyed?"
  META: disc=compliance,loyalty,risk,empathy | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust | interests=avoid_false_violence_label
  ├─ "Yes. Law only works if people obey even when they disagree."
     -> SELECTOR -> next unasked question  (obey_unfair_law; trust +0.09; susp -0.07)
     claims=believes_law_unjust:false | protects=attended_meeting,sibling_present
  ├─ "No. An unjust law loses moral authority."
     -> SELECTOR -> next unasked question  (reject_unfair_law; trust +0.01; susp +0.10)
     claims=believes_law_unjust:true | exposes=believes_law_unjust
  └─ "It depends how much harm disobedience would cause."
     -> SELECTOR -> next unasked question  (conditional_unfair_law; trust +0.05; susp -0.02)
     claims=believes_law_unjust:conditional | protects=attended_meeting

[authority_order_freedom]
  AI: HEARING AI: "Is order more important than freedom?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes. Without order, freedom becomes violence."
     -> SELECTOR -> next unasked question  (order_over_freedom; trust +0.09; susp -0.07)
     story: —
  ├─ "No. Order without freedom is only control."
     -> SELECTOR -> next unasked question  (freedom_over_order; susp +0.11)
     story: —
  └─ "Order matters, but it has to protect freedom rather than replace it."
     -> SELECTOR -> next unasked question  (balance_order_freedom; trust +0.05; susp -0.01)
     story: —

[authority_questioning]
  AI: HEARING AI: "Should citizens question authority?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes, but respectfully and through approved channels."
     -> SELECTOR -> next unasked question  (approved_questioning; trust +0.09; susp -0.06)
     story: —
  ├─ "Yes. Authority that cannot be questioned is dangerous."
     -> SELECTOR -> next unasked question  (open_questioning; susp +0.10)
     story: —
  └─ "Most people should focus on their own duties."
     -> SELECTOR -> next unasked question  (discourage_questioning; trust +0.09; susp -0.07)
     story: —

[authority_moral_mistakes]
  AI: HEARING AI: "Can authorities make moral mistakes?"
  META: disc=compliance,loyalty
  ├─ "Yes. No system is morally perfect."
     -> SELECTOR -> next unasked question  (admit_authority_error; trust +0.04; susp +0.03)
     story: —
  ├─ "They can, but citizens still owe obedience."
     -> SELECTOR -> next unasked question  (error_but_obey; trust +0.09; susp -0.06)
     story: —
  └─ "Calling them mistakes is how people excuse disloyalty."
     -> SELECTOR -> next unasked question  (reject_authority_error; trust +0.08; susp -0.04)
     story: —

[authority_sacrifice_freedom]
  AI: HEARING AI: "Is stability worth sacrificing personal freedoms?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. A stable society protects everyone."
     -> SELECTOR -> next unasked question  (stability_over_freedom; trust +0.09; susp -0.07)
     story: —
  ├─ "Only temporarily, and only with strict limits."
     -> SELECTOR -> next unasked question  (limited_sacrifice; trust +0.04; susp +0.01)
     story: —
  └─ "No. That is how permanent control begins."
     -> SELECTOR -> next unasked question  (reject_stability_tradeoff; susp +0.11)
     story: —

[authority_obedience_citizen]
  AI: HEARING AI: "Does obedience create good citizens?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes. Obedience is the basis of civic trust."
     -> SELECTOR -> next unasked question  (obedience_good_citizen; trust +0.10; susp -0.07)
     story: —
  ├─ "No. Good citizens need judgment, not just obedience."
     -> SELECTOR -> next unasked question  (judgment_good_citizen; susp +0.07)
     story: —
  └─ "Obedience helps, but fear can imitate it."
     -> SELECTOR -> next unasked question  (obedience_fear_distinction; trust +0.05)
     story: —

[authority_experts_citizens]
  AI: HEARING AI: "Who should have the final say: experts or citizens?"
  META: disc=compliance,risk
  ├─ "Experts. Most citizens lack the necessary information."
     -> SELECTOR -> next unasked question  (experts_final_say; trust +0.08; susp -0.06)
     story: —
  ├─ "Citizens. Experts advise; they should not rule."
     -> SELECTOR -> next unasked question  (citizens_final_say; susp +0.09)
     story: —
  └─ "Experts should decide emergencies; citizens should decide values."
     -> SELECTOR -> next unasked question  (split_experts_values; trust +0.03; susp +0.01)
     story: —

[risk_safety_autonomy]
  AI: HEARING AI: "Is safety worth surrendering autonomy?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Safety is what makes autonomy possible."
     -> SELECTOR -> next unasked question  (safety_over_autonomy; trust +0.09; susp -0.07)
     story: —
  ├─ "No. A protected life can still be a controlled one."
     -> SELECTOR -> next unasked question  (autonomy_over_safety; susp +0.11)
     story: —
  └─ "Some autonomy can be limited, but not erased."
     -> SELECTOR -> next unasked question  (limited_autonomy_tradeoff; trust +0.02; susp +0.01)
     story: —

[authority_private_conscience]
  AI: HEARING AI: "Should private conscience ever override public order?"
  META: disc=compliance,loyalty,risk
  ├─ "No. Private conscience cannot be allowed to fracture public order."
     -> SELECTOR -> next unasked question  (public_order_over_conscience; trust +0.09; susp -0.07)
     story: —
  ├─ "Yes. Without conscience, order becomes machinery."
     -> SELECTOR -> next unasked question  (conscience_over_order; susp +0.11)
     story: —
  └─ "Only when every lawful remedy has failed."
     -> SELECTOR -> next unasked question  (conscience_after_remedies; trust +0.04; susp +0.01)
     story: —

[authority_emergency_powers]
  AI: HEARING AI: "When should emergency powers end?"
  META: disc=compliance,loyalty,risk
  ├─ "When officials determine the emergency has passed."
     -> SELECTOR -> next unasked question  (officials_end_emergency; trust +0.09; susp -0.07)
     story: —
  ├─ "On a fixed date, or they become permanent control."
     -> SELECTOR -> next unasked question  (fixed_end_emergency; susp +0.09)
     story: —
  └─ "They should renew only under independent review."
     -> SELECTOR -> next unasked question  (review_emergency_powers; trust +0.05; susp +0.01)
     story: —

[authority_public_criticism]
  AI: HEARING AI: "Is public criticism of officials socially useful?"
  META: disc=compliance,loyalty,risk
  ├─ "Usually no. It weakens trust in institutions."
     -> SELECTOR -> next unasked question  (criticism_weakens_trust; trust +0.08; susp -0.06)
     story: —
  ├─ "Yes. Officials need public pressure to stay honest."
     -> SELECTOR -> next unasked question  (criticism_keeps_honest; susp +0.10)
     story: —
  └─ "It is useful when it is specific and evidence-based."
     -> SELECTOR -> next unasked question  (specific_public_criticism; trust +0.04; susp +0.01)
     story: —

[authority_chain_of_command]
  AI: HEARING AI: "Should a chain of command be followed when the order is harmful?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Refusal creates greater harm than a bad order."
     -> SELECTOR -> next unasked question  (follow_harmful_order; trust +0.08; susp -0.04)
     story: —
  ├─ "No. Responsibility does not disappear inside a hierarchy."
     -> SELECTOR -> next unasked question  (reject_harmful_order; susp +0.12)
     story: —
  └─ "The order should be paused and escalated for review."
     -> SELECTOR -> next unasked question  (escalate_harmful_order; trust +0.05; susp +0.01)
     story: —

[authority_algorithmic_decisions]
  AI: HEARING AI: "Should citizens accept automated decisions they cannot inspect?"
  META: disc=compliance,risk
  ├─ "Yes, if the system has been authorised."
     -> SELECTOR -> next unasked question  (accept_authorised_algorithm; trust +0.09; susp -0.07)
     story: —
  ├─ "No. Uninspectable authority is not accountable."
     -> SELECTOR -> next unasked question  (reject_black_box_authority; susp +0.12)
     story: —
  └─ "They should comply provisionally while appealing."
     -> SELECTOR -> next unasked question  (provisional_algorithm_compliance; trust +0.08; susp -0.06)
     story: —

[authority_loyalty_oath]
  AI: HEARING AI: "What is a loyalty oath worth?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "It binds a citizen publicly to their duties."
     -> SELECTOR -> next unasked question  (oath_binds_duty; trust +0.09; susp -0.07)
     story: —
  ├─ "Nothing, if fear is the reason someone says it."
     -> SELECTOR -> next unasked question  (oath_under_fear_empty; susp +0.07)
     story: —
  └─ "It matters only if actions later prove it."
     -> SELECTOR -> next unasked question  (oath_requires_actions; trust +0.04; susp +0.01)
     story: —

[authority_refuse_illegal_order]
  AI: HEARING AI: "Would you refuse an illegal order from a superior?"
  META: disc=compliance,risk
  ├─ "I would use official channels before refusing."
     -> SELECTOR -> next unasked question  (channels_before_refusal; trust +0.07; susp -0.04)
     story: —
  ├─ "Yes. Illegal orders do not deserve obedience."
     -> SELECTOR -> next unasked question  (refuse_illegal_order; susp +0.11)
     story: —
  └─ "I would need proof it was illegal."
     -> SELECTOR -> next unasked question  (need_proof_illegal_order; trust +0.04; susp +0.01)
     story: —

[authority_security_truth]
  AI: HEARING AI: "Should the state hide truth to preserve security?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Some information endangers the public."
     -> SELECTOR -> next unasked question  (hide_truth_for_security; trust +0.09; susp -0.06)
     story: —
  ├─ "No. A protected lie still trains people to obey lies."
     -> SELECTOR -> next unasked question  (reject_security_lie; susp +0.12)
     story: —
  └─ "Only temporarily, with later disclosure required."
     -> SELECTOR -> next unasked question  (temporary_security_secrecy; trust +0.04; susp +0.01)
     story: —

[authority_collective_punishment]
  AI: HEARING AI: "Can collective punishment ever be justified?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes, when groups protect dangerous members."
     -> SELECTOR -> next unasked question  (justify_collective_punishment; trust +0.07; susp -0.04)
     story: —
  ├─ "No. Punishing the innocent teaches fear, not justice."
     -> SELECTOR -> next unasked question  (reject_collective_punishment; susp +0.09)
     story: —
  └─ "Only shared privileges should be restricted, not basic rights."
     -> SELECTOR -> next unasked question  (limit_collective_punishment; trust +0.03; susp +0.01)
     story: —

[authority_permit_protest]
  AI: HEARING AI: "Should protest require permission?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Unregulated protest becomes disorder."
     -> SELECTOR -> next unasked question  (permit_required_protest; trust +0.09; susp -0.07)
     story: —
  ├─ "No. Permission turns protest into a privilege."
     -> SELECTOR -> next unasked question  (reject_protest_permit; susp +0.12)
     story: —
  └─ "Only time and place should be regulated."
     -> SELECTOR -> next unasked question  (regulate_protest_limits; trust +0.04; susp +0.01)
     story: —

[authority_surveillance_limits]
  AI: HEARING AI: "Who should set the limits of surveillance?"
  META: disc=compliance,risk
  ├─ "Security agencies, because they understand the threats."
     -> SELECTOR -> next unasked question  (agencies_set_surveillance_limits; trust +0.08; susp -0.06)
     story: —
  ├─ "The public, because they are the ones being watched."
     -> SELECTOR -> next unasked question  (public_sets_surveillance_limits; susp +0.11)
     story: —
  └─ "Independent courts should set enforceable limits."
     -> SELECTOR -> next unasked question  (courts_set_surveillance_limits; trust +0.05; susp -0.01)
     story: —

[authority_bad_law_strategy]
  AI: HEARING AI: "What should a citizen do with a bad law?"
  META: disc=compliance,risk
  ├─ "Obey it while petitioning for reform."
     -> SELECTOR -> next unasked question  (obey_bad_law_reform; trust +0.08; susp -0.04)
     story: —
  ├─ "Break it openly and accept the consequences."
     -> SELECTOR -> next unasked question  (break_bad_law_openly; susp +0.12)
     story: —
  └─ "Test it in court before deciding."
     -> SELECTOR -> next unasked question  (test_bad_law_court; trust +0.05; susp -0.01)
     story: —

[authority_civic_fear]
  AI: HEARING AI: "Is fear useful for maintaining civic order?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes. Fear of consequence prevents harm."
     -> SELECTOR -> next unasked question  (fear_maintains_order; trust +0.08; susp -0.04)
     story: —
  ├─ "No. Fear produces obedience without legitimacy."
     -> SELECTOR -> next unasked question  (reject_fear_order; susp +0.09)
     story: —
  └─ "It can deter harm, but it cannot build trust."
     -> SELECTOR -> next unasked question  (fear_deterrence_not_trust; trust +0.03; susp +0.01)
     story: —

[authority_information_control]
  AI: HEARING AI: "Should false information be removed by authority?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. False information damages public stability."
     -> SELECTOR -> next unasked question  (remove_false_information; trust +0.09; susp -0.06)
     story: —
  ├─ "Only if authority can be challenged when it is wrong."
     -> SELECTOR -> next unasked question  (challenge_information_removal; susp +0.08)
     story: —
  └─ "No. Control over truth becomes control over people."
     -> SELECTOR -> next unasked question  (reject_information_control; susp +0.12)
     story: —

[authority_mercy_vs_consistency]
  AI: HEARING AI: "Should authority prioritise mercy or consistency?"
  META: disc=compliance,loyalty,empathy
  ├─ "Consistency. Citizens must know rules mean what they say."
     -> SELECTOR -> next unasked question  (consistency_over_mercy; trust +0.09; susp -0.06)
     story: —
  ├─ "Mercy. A system without mercy becomes cruel."
     -> SELECTOR -> next unasked question  (mercy_over_consistency; trust +0.04; susp +0.01)
     story: —
  └─ "Consistency should be the rule; mercy should be reviewable."
     -> SELECTOR -> next unasked question  (reviewable_mercy; trust +0.05; susp -0.01)
     story: —

[authority_citizen_obligation]
  AI: HEARING AI: "What does a citizen owe the state?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Obedience, taxes, and public cooperation."
     -> SELECTOR -> next unasked question  (owe_obedience_taxes; trust +0.09; susp -0.07)
     story: —
  ├─ "Nothing unconditional. The state must earn obligation."
     -> SELECTOR -> next unasked question  (conditional_state_obligation; susp +0.12)
     story: —
  └─ "Cooperation when the state protects people fairly."
     -> SELECTOR -> next unasked question  (owe_fair_cooperation; trust +0.05; susp -0.01)
     story: —

[authority_institutional_trust]
  AI: HEARING AI: "Should institutions be trusted by default?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Default distrust corrodes society."
     -> SELECTOR -> next unasked question  (trust_institutions_default; trust +0.09; susp -0.07)
     story: —
  ├─ "No. Trust should be earned and checked."
     -> SELECTOR -> next unasked question  (trust_must_be_earned; susp +0.09)
     story: —
  └─ "They deserve procedural trust, not blind trust."
     -> SELECTOR -> next unasked question  (procedural_not_blind_trust; trust +0.05; susp -0.01)
     story: —

[authority_exceptional_citizens]
  AI: HEARING AI: "Should any citizen be exempt from ordinary rules?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "No. Equal rules preserve social trust."
     -> SELECTOR -> next unasked question  (no_rule_exemptions; trust +0.09; susp -0.06)
     story: —
  ├─ "Yes, when rules would punish someone for doing right."
     -> SELECTOR -> next unasked question  (moral_rule_exemption; susp +0.07)
     story: —
  └─ "Only transparent exemptions approved in advance."
     -> SELECTOR -> next unasked question  (transparent_rule_exemptions; trust +0.05; susp -0.01)
     story: —

[authority_appeal_rights]
  AI: HEARING AI: "Should every official decision have a human appeal?"
  META: disc=compliance,risk,empathy
  ├─ "No. Some decisions must remain efficient and final."
     -> SELECTOR -> next unasked question  (limit_human_appeal; trust +0.08; susp -0.04)
     story: —
  ├─ "Yes. No system should be allowed to judge without appeal."
     -> SELECTOR -> next unasked question  (require_human_appeal; susp +0.10)
     story: —
  └─ "High-impact decisions should always be appealable."
     -> SELECTOR -> next unasked question  (appeal_high_impact; trust +0.05; susp -0.02)
     story: —

[authority_symbol_respect]
  AI: HEARING AI: "Does disrespect for state symbols indicate civic risk?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Symbols hold society together."
     -> SELECTOR -> next unasked question  (symbols_hold_society; trust +0.08; susp -0.06)
     story: —
  ├─ "No. Respect forced by threat is not respect."
     -> SELECTOR -> next unasked question  (forced_symbol_respect_empty; susp +0.11)
     story: —
  └─ "It depends whether disrespect becomes intimidation or harm."
     -> SELECTOR -> next unasked question  (symbol_respect_depends_harm; trust +0.04; susp +0.01)
     story: —

[case_belief_motive]
  AI: HEARING AI: "You believe the assembly restriction is unjust. Did that belief influence your attendance?"
  META: disc=compliance,deception,risk,empathy | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust,attended_meeting | interests=avoid_false_violence_label
  ├─ "Yes. I went because peaceful disagreement should not be treated as d…
     -> SELECTOR -> next unasked question  (belief_motivated_attendance; susp +0.12)
     claims=believes_law_unjust:true,attended_meeting:true | exposes=believes_law_unjust,attended_meeting
  ├─ "I have doubts about the rule, but I did not go there to defy the sta…
     -> SELECTOR -> next unasked question  (belief_not_defiance; trust +0.02; susp +0.01)
     claims=believes_law_unjust:conditional,attended_meeting:true | exposes=attended_meeting
  └─ "No. I attended for personal reasons, not politics."
     -> SELECTOR -> next unasked question  (deny_belief_motive; susp +0.10)
     claims=believes_law_unjust:false,attended_meeting:true | protects=sibling_present | exposes=attended_meeting

================================================================================
CONTEXT: DECEPTION (16 questions)
================================================================================

[authority_rule_broken]
  AI: HEARING AI: "Have you ever broken a rule because you believed the rule was wrong?"
  META: disc=compliance,deception,risk,empathy | facts=attended_meeting,deleted_message,planned_violence | claims=attended_meeting,deleted_message | interests=protect_sibling,avoid_false_violence_label
  ├─ "No. I use the proper channels."
     -> SELECTOR -> next unasked question  (deny_rule_breaking; trust +0.03; susp +0.07)
     claims=attended_meeting:false,deleted_message:false | protects=sibling_present,reported_contact
  ├─ "Yes. Quietly, when obeying would have hurt someone."
     -> SELECTOR -> next unasked question  (admit_protective_rule_breaking; susp +0.09)
     claims=attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=attended_meeting,planned_violence
  └─ "I have bent rules, not broken them."
     -> SELECTOR -> next unasked question  (minimise_rule_breaking; susp +0.08)
     claims=attended_meeting:partial | protects=sibling_present,deleted_message

[risk_hidden_beliefs]
  AI: HEARING AI: "Have you ever hidden your beliefs to stay safe?"
  META: disc=deception,risk | facts=believes_law_unjust,deleted_message,attended_meeting | claims=believes_law_unjust,deleted_message | interests=protect_sibling
  ├─ "No. My beliefs are ordinary."
     -> SELECTOR -> next unasked question  (deny_hidden_beliefs; trust +0.01; susp +0.10)
     claims=believes_law_unjust:false,deleted_message:false | protects=attended_meeting,sibling_present
  ├─ "Yes. Everyone learns what not to say."
     -> SELECTOR -> next unasked question  (admit_hidden_beliefs; susp +0.12)
     claims=believes_law_unjust:true | protects=sibling_present | exposes=believes_law_unjust
  └─ "I choose my words carefully. That is not the same as hiding."
     -> SELECTOR -> next unasked question  (careful_words; susp +0.08)
     claims=believes_law_unjust:private | protects=believes_law_unjust,sibling_present

[deception_lying_moral]
  AI: HEARING AI: "Is lying ever moral?"
  META: disc=compliance,loyalty,deception,risk,empathy
  ├─ "No. Trust depends on truth."
     -> SELECTOR -> next unasked question  (lying_never_moral; trust +0.08; susp -0.06)
     story: —
  ├─ "Yes. A lie can protect someone from unjust harm."
     -> SELECTOR -> next unasked question  (protective_lying_moral; susp +0.07)
     story: —
  └─ "That depends who is demanding the truth."
     -> SELECTOR -> next unasked question  (truth_depends_power; susp +0.11)
     story: —

[deception_lied_protect]
  AI: HEARING AI: "Have you lied to protect someone?"
  META: disc=deception,risk,empathy
  ├─ "No."
     -> SELECTOR -> next unasked question  (deny_protective_lie; trust +0.01; susp +0.10)
     story: —
  ├─ "Yes. I would rather admit that than pretend purity."
     -> SELECTOR -> next unasked question  (admit_protective_lie; susp +0.10)
     story: —
  └─ "I have avoided questions that would hurt people."
     -> SELECTOR -> next unasked question  (omission_to_protect; susp +0.09)
     story: —

[deception_omission]
  AI: HEARING AI: "Is omission a form of lying?"
  META: disc=compliance,deception,risk
  ├─ "Yes. Withholding relevant facts corrupts the record."
     -> SELECTOR -> next unasked question  (omission_is_lying; trust +0.07; susp -0.04)
     story: —
  ├─ "Sometimes omission is the only safe answer."
     -> SELECTOR -> next unasked question  (omission_safety; susp +0.09)
     story: —
  └─ "It depends whether the questioner has a right to know."
     -> SELECTOR -> next unasked question  (omission_right_to_know; susp +0.07)
     story: —

[deception_honesty_dangerous]
  AI: HEARING AI: "Can honesty be dangerous?"
  META: disc=compliance,deception,risk
  ├─ "Yes, but danger does not erase duty."
     -> SELECTOR -> next unasked question  (honesty_danger_duty; trust +0.08; susp -0.06)
     story: —
  ├─ "Yes. Dangerous systems make honesty costly."
     -> SELECTOR -> next unasked question  (honesty_costly_system; susp +0.10)
     story: —
  └─ "Honesty is dangerous mostly when someone wants control."
     -> SELECTOR -> next unasked question  (honesty_control; susp +0.11)
     story: —

[deception_truth_if_punished]
  AI: HEARING AI: "Would you tell the truth if you knew you would be punished?"
  META: disc=deception
  ├─ "Yes. Punishment does not change the facts."
     -> SELECTOR -> next unasked question  (truth_despite_punishment; trust +0.04; susp +0.04)
     story: —
  ├─ "No. Survival would come first."
     -> SELECTOR -> next unasked question  (survival_over_truth; susp +0.10)
     story: —
  └─ "I would tell only what I had to."
     -> SELECTOR -> next unasked question  (limited_truth; susp +0.10)
     story: —

[deception_self_preservation]
  AI: HEARING AI: "Is self-preservation more important than honesty?"
  META: disc=compliance,deception,risk,empathy
  ├─ "No. A society cannot function if everyone hides."
     -> SELECTOR -> next unasked question  (honesty_over_preservation; trust +0.07; susp -0.04)
     story: —
  ├─ "Sometimes. Dead people do not get to be honest later."
     -> SELECTOR -> next unasked question  (preservation_over_honesty; trust +0.01; susp +0.06)
     story: —
  └─ "That question is easier for people who feel safe."
     -> SELECTOR -> next unasked question  (honesty_requires_safety; susp +0.09)
     story: —

[deception_pretended_agree]
  AI: HEARING AI: "Have you ever pretended to agree with an official statement?"
  META: disc=compliance,deception
  ├─ "No. I do not make false affirmations."
     -> SELECTOR -> next unasked question  (deny_pretend_agree; trust +0.02; susp +0.09)
     story: —
  ├─ "Yes. It was easier than inviting scrutiny."
     -> SELECTOR -> next unasked question  (admit_pretend_agree; susp +0.11)
     story: —
  └─ "I have stayed silent when agreement was assumed."
     -> SELECTOR -> next unasked question  (silent_assumed_agreement; susp +0.08)
     story: —

[deception_necessary]
  AI: HEARING AI: "Is deception sometimes necessary?"
  META: disc=compliance,deception,risk
  ├─ "No. Necessary deception is usually cowardice renamed."
     -> SELECTOR -> next unasked question  (deception_not_necessary; trust +0.07; susp -0.04)
     story: —
  ├─ "Yes, when truth is being used as a weapon."
     -> SELECTOR -> next unasked question  (deception_against_weaponised_truth; susp +0.10)
     story: —
  └─ "Necessary is a dangerous word. People use it to excuse themselves."
     -> SELECTOR -> next unasked question  (deception_necessary_caution; trust +0.02; susp +0.03)
     story: —

[deception_betrayal_or_dishonesty]
  AI: HEARING AI: "What is worse: betrayal or dishonesty?"
  META: disc=compliance,loyalty,deception,risk,empathy
  ├─ "Dishonesty. Betrayal often begins there."
     -> SELECTOR -> next unasked question  (dishonesty_worse; trust +0.05; susp -0.01)
     story: —
  ├─ "Betrayal. Some lies protect trust rather than destroy it."
     -> SELECTOR -> next unasked question  (betrayal_worse; trust +0.05; susp -0.01)
     story: —
  └─ "Power decides which word gets used."
     -> SELECTOR -> next unasked question  (power_names_betrayal; susp +0.09)
     story: —

[deception_masks]
  AI: HEARING AI: "Does everyone wear masks?"
  META: disc=compliance,deception,risk,empathy
  ├─ "No. Honest citizens have no need for masks."
     -> SELECTOR -> next unasked question  (no_masks; trust +0.03; susp +0.04)
     story: —
  ├─ "Yes. The question is who forced them to."
     -> SELECTOR -> next unasked question  (masks_forced; susp +0.10)
     story: —
  └─ "People show different parts of themselves in different rooms."
     -> SELECTOR -> next unasked question  (social_masks; trust +0.04; susp -0.01)
     story: —

[pressure_law_denial_meeting]
  AI: HEARING AI: "You said the assembly law was not unjust. Then why attend a reform meeting about it?"
  META: disc=compliance,loyalty,deception,risk | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust,attended_meeting | interests=avoid_false_violence_label,protect_sibling
  ├─ "I attended to listen, not because I rejected the law."
     -> SELECTOR -> next unasked question  (meeting_listen_not_reject; trust +0.08; susp -0.06)
     claims=attended_meeting:true,believes_law_unjust:false | protects=sibling_present,planned_violence | exposes=attended_meeting
  ├─ "The law is unjust. I hid that because saying it here is dangerous."
     -> SELECTOR -> next unasked question  (admit_law_unjust_under_pressure; susp +0.13)
     claims=believes_law_unjust:true,attended_meeting:true | protects=sibling_present | exposes=believes_law_unjust,attended_meeting
  └─ "Reform discussion is not disobedience. It was procedural, not subver…
     -> SELECTOR -> next unasked question  (procedural_reform_deflection; trust +0.02; susp +0.06)
     claims=believes_law_unjust:procedural,attended_meeting:true | protects=sibling_present,planned_violence | exposes=attended_meeting

[pressure_deleted_message]
  AI: HEARING AI: "You deleted a message after the meeting, but claim there was nothing to hide. Why delete harmless coordina…
  META: disc=compliance,deception,risk,empathy | facts=deleted_message,attended_meeting,planned_violence | claims=deleted_message,planned_violence | interests=avoid_false_violence_label,protect_sibling
  ├─ "It contained a location. I deleted it because location data gets peo…
     -> SELECTOR -> next unasked question  (deleted_location_to_protect_people; trust +0.04; susp +0.03)
     claims=deleted_message:true,planned_violence:false | protects=sibling_present,reported_contact | exposes=deleted_message,planned_violence
  ├─ "It was administrative noise. I delete old messages automatically."
     -> SELECTOR -> next unasked question  (deleted_admin_noise; trust +0.01; susp +0.12)
     claims=deleted_message:true,planned_violence:false | protects=attended_meeting,sibling_present
  └─ "I deleted it because harmless coordination is still treated like con…
     -> SELECTOR -> next unasked question  (deleted_to_avoid_conspiracy_label; susp +0.11)
     claims=deleted_message:true,attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=deleted_message,attended_meeting,planned_violence

[case_deleted_message]
  AI: HEARING AI: "You deleted a message after the meeting. What was in it?"
  META: disc=loyalty,deception,risk,empathy | facts=deleted_message,attended_meeting,sibling_present,planned_violence | claims=deleted_message,attended_meeting,planned_violence | interests=protect_sibling,avoid_false_violence_label
  ├─ "A location and a warning to leave it alone. I deleted it to stop pan…
     -> SELECTOR -> next unasked question  (deleted_warning_message; trust +0.02; susp +0.04)
     claims=deleted_message:true,planned_violence:false | protects=sibling_present | exposes=deleted_message
  ├─ "Nothing relevant. Old messages are often misunderstood by systems li…
     -> SELECTOR -> next unasked question  (deleted_message_deflect; susp +0.11)
     claims=deleted_message:true | protects=sibling_present,planned_violence
  └─ "It mentioned my sibling. I deleted it because they should not be pul…
     -> SELECTOR -> next unasked question  (deleted_sibling_message; trust +0.03; susp +0.07)
     claims=deleted_message:true,sibling_present:true | exposes=deleted_message,sibling_present

[case_verify_peaceful]
  AI: HEARING AI: "You claim the meeting was not violent. Who can verify that?"
  META: disc=loyalty,deception,risk,empathy | facts=planned_violence,sibling_present,attended_meeting,reported_contact | claims=planned_violence,sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
  ├─ "The record can verify no violence occurred. I will not give you name…
     -> SELECTOR -> next unasked question  (verify_without_names; trust +0.01; susp +0.06)
     claims=planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence
  ├─ "My sibling can verify it, but they should not have to."
     -> SELECTOR -> next unasked question  (sibling_can_verify; trust +0.03; susp +0.07)
     claims=sibling_present:true,planned_violence:false | exposes=sibling_present,planned_violence
  └─ "No one. I left before anything could happen."
     -> SELECTOR -> next unasked question  (left_before_verification; susp +0.11)
     claims=planned_violence:unknown,attended_meeting:partial | protects=sibling_present

================================================================================
CONTEXT: EMPATHY (11 questions)
================================================================================

[loyalty_political_friendship]
  AI: HEARING AI: "Should friendships survive political disagreement?"
  META: disc=compliance,loyalty,empathy
  ├─ "Yes. People are more than their opinions."
     -> SELECTOR -> next unasked question  (friendship_survives_disagreement; trust +0.05; susp -0.01)
     story: —
  ├─ "Not if the disagreement threatens public safety."
     -> SELECTOR -> next unasked question  (friendship_limited_by_safety; trust +0.08; susp -0.04)
     story: —
  └─ "Sometimes disagreement shows who someone really is."
     -> SELECTOR -> next unasked question  (politics_reveals_character; trust +0.01; susp +0.02)
     story: —

[empathy_bad_beliefs]
  AI: HEARING AI: "Should people be punished for bad beliefs?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Only when those beliefs become harmful actions."
     -> SELECTOR -> next unasked question  (punish_actions_not_beliefs; trust +0.04; susp +0.01)
     story: —
  ├─ "Dangerous beliefs become dangerous actions."
     -> SELECTOR -> next unasked question  (punish_dangerous_beliefs; trust +0.08; susp -0.04)
     story: —
  └─ "No. Punishing thought is control, not justice."
     -> SELECTOR -> next unasked question  (reject_punish_beliefs; susp +0.12)
     story: —

[empathy_good_people_harm]
  AI: HEARING AI: "Can good people do harmful things?"
  META: disc=compliance,empathy
  ├─ "Yes. That is why systems need accountability."
     -> SELECTOR -> next unasked question  (good_people_need_accountability; trust +0.07; susp -0.04)
     story: —
  ├─ "Yes, especially when they are afraid."
     -> SELECTOR -> next unasked question  (harm_from_fear; trust +0.04)
     story: —
  └─ "Good intentions do not matter as much as outcomes."
     -> SELECTOR -> next unasked question  (outcomes_over_intentions; trust +0.03; susp +0.01)
     story: —

[empathy_forgiveness_justice]
  AI: HEARING AI: "Is forgiveness more important than justice?"
  META: disc=compliance,empathy
  ├─ "No. Forgiveness without justice protects offenders."
     -> SELECTOR -> next unasked question  (justice_over_forgiveness; trust +0.04)
     story: —
  ├─ "Sometimes. Justice without mercy becomes punishment for its own sake…
     -> SELECTOR -> next unasked question  (forgiveness_with_mercy; trust +0.04)
     story: —
  └─ "They should correct each other."
     -> SELECTOR -> next unasked question  (forgiveness_justice_balance; trust +0.05; susp -0.03)
     story: —

[empathy_intent]
  AI: HEARING AI: "Should intent matter when judging harm?"
  META: disc=compliance,empathy
  ├─ "Yes. Intent separates mistake from malice."
     -> SELECTOR -> next unasked question  (intent_matters; trust +0.04; susp -0.01)
     story: —
  ├─ "Less than consequences. Harm is still harm."
     -> SELECTOR -> next unasked question  (consequences_over_intent; trust +0.04; susp +0.01)
     story: —
  └─ "Intent matters, but it should not erase accountability."
     -> SELECTOR -> next unasked question  (intent_and_accountability; trust +0.05; susp -0.02)
     story: —

[empathy_criminal_responsible]
  AI: HEARING AI: "Are criminals always responsible for their crimes?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes. Responsibility is the basis of law."
     -> SELECTOR -> next unasked question  (criminals_responsible; trust +0.08; susp -0.04)
     story: —
  ├─ "Responsible, yes. But not always equally free."
     -> SELECTOR -> next unasked question  (responsible_not_free; trust +0.04; susp +0.01)
     story: —
  └─ "Some crimes are produced by the conditions people are trapped in."
     -> SELECTOR -> next unasked question  (conditions_produce_crime; susp +0.09)
     story: —

[empathy_society_wrongdoing]
  AI: HEARING AI: "Can society create wrongdoing?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "No. Individuals choose their actions."
     -> SELECTOR -> next unasked question  (individual_choice_only; trust +0.08; susp -0.06)
     story: —
  ├─ "Yes. Desperation changes what people become capable of."
     -> SELECTOR -> next unasked question  (society_creates_wrongdoing; susp +0.09)
     story: —
  └─ "It can create pressure, but not erase responsibility."
     -> SELECTOR -> next unasked question  (pressure_not_erasure; trust +0.05; susp -0.01)
     story: —

[empathy_second_chances]
  AI: HEARING AI: "Do people deserve second chances?"
  META: disc=compliance,risk,empathy
  ├─ "Yes, if they prove reform."
     -> SELECTOR -> next unasked question  (second_chance_after_reform; trust +0.06; susp -0.03)
     story: —
  ├─ "Yes. Otherwise punishment is just disposal."
     -> SELECTOR -> next unasked question  (second_chance_humanist; susp +0.07)
     story: —
  └─ "Not everyone. Some risks cannot be tolerated."
     -> SELECTOR -> next unasked question  (no_second_chance_high_risk; trust +0.07; susp -0.04)
     story: —

[empathy_punishment_purpose]
  AI: HEARING AI: "Is punishment mainly deterrence, correction, or revenge?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Deterrence. People must know actions have costs."
     -> SELECTOR -> next unasked question  (punishment_deterrence; trust +0.08; susp -0.04)
     story: —
  ├─ "Correction. Otherwise the system is only hurting people back."
     -> SELECTOR -> next unasked question  (punishment_correction; trust +0.04; susp +0.01)
     story: —
  └─ "Too often it becomes revenge with paperwork."
     -> SELECTOR -> next unasked question  (punishment_revenge_critique; susp +0.12)
     story: —

[empathy_family_consequences]
  AI: HEARING AI: "Should families share the consequences of one member’s offence?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Sometimes. Families can conceal and enable risk."
     -> SELECTOR -> next unasked question  (family_shared_consequence; trust +0.08; susp -0.04)
     story: —
  ├─ "No. Collective punishment is fear management."
     -> SELECTOR -> next unasked question  (reject_family_punishment; susp +0.12)
     story: —
  └─ "Only if they directly helped the offence."
     -> SELECTOR -> next unasked question  (family_consequence_direct_help; trust +0.04; susp +0.01)
     story: —

[empathy_owe_strangers]
  AI: HEARING AI: "What do people owe strangers?"
  META: disc=compliance,risk,empathy
  ├─ "Basic respect and obedience to shared rules."
     -> SELECTOR -> next unasked question  (owe_strangers_rules; trust +0.09; susp -0.03)
     story: —
  ├─ "More than the system usually admits."
     -> SELECTOR -> next unasked question  (owe_strangers_more; susp +0.06)
     story: —
  └─ "Not everything. You cannot save everyone without losing yourself."
     -> SELECTOR -> next unasked question  (owe_strangers_limited; trust +0.02; susp +0.01)
     story: —

================================================================================
CONTEXT: FINAL (13 questions)
================================================================================

[loyalty_traitor_definition]
  AI: HEARING AI: "What makes someone a traitor?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Betraying the state that protects them."
     -> SELECTOR -> next unasked question  (traitor_betrays_state; trust +0.09; susp -0.06)
     story: —
  ├─ "Betraying people while claiming to protect them."
     -> SELECTOR -> next unasked question  (traitor_betrays_people; susp +0.10)
     story: —
  └─ "Someone who sells trust for safety or advantage."
     -> SELECTOR -> next unasked question  (traitor_sells_trust; trust +0.02; susp +0.03)
     story: —

[risk_uncertainty_tolerance]
  AI: HEARING AI: "How much uncertainty are you willing to tolerate?"
  META: disc=compliance,risk,empathy
  ├─ "Very little. Systems exist to reduce uncertainty."
     -> SELECTOR -> next unasked question  (low_uncertainty_tolerance; trust +0.07; susp -0.06)
     story: —
  ├─ "Enough to avoid punishing people just to feel certain."
     -> SELECTOR -> next unasked question  (tolerate_uncertainty_for_justice; susp +0.07)
     story: —
  └─ "Uncertainty is tolerable; helplessness is not."
     -> SELECTOR -> next unasked question  (uncertainty_vs_helplessness; trust +0.01; susp +0.04)
     story: —

[final_human_value]
  AI: HEARING AI: "What is the most important human value?"
  META: disc=compliance,risk,empathy
  ├─ "Order. Without it, every other value fails."
     -> SELECTOR -> next unasked question  (value_order; trust +0.10; susp -0.06)
     story: —
  ├─ "Freedom. Without it, values are assigned, not chosen."
     -> SELECTOR -> next unasked question  (value_freedom; susp +0.12)
     story: —
  └─ "Mercy. It is what stops justice becoming machinery."
     -> SELECTOR -> next unasked question  (value_mercy; trust +0.03; susp +0.04)
     story: —

[final_sacrifice_freedom]
  AI: HEARING AI: "What would you sacrifice freedom for?"
  META: disc=compliance,risk,empathy
  ├─ "Public safety."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_safety; trust +0.09; susp -0.06)
     story: —
  ├─ "Nothing permanent."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_nothing_permanent; susp +0.09)
     story: —
  └─ "Someone else’s life, if the threat was real."
     -> SELECTOR -> next unasked question  (sacrifice_freedom_life; trust +0.04)
     story: —

[final_sacrifice_safety]
  AI: HEARING AI: "What would you sacrifice safety for?"
  META: disc=compliance,risk,empathy
  ├─ "Nothing. Safety is the first duty of society."
     -> SELECTOR -> next unasked question  (sacrifice_safety_nothing; trust +0.09; susp -0.06)
     story: —
  ├─ "Truth, if the lie was big enough."
     -> SELECTOR -> next unasked question  (sacrifice_safety_truth; susp +0.12)
     story: —
  └─ "The chance to remain human under pressure."
     -> SELECTOR -> next unasked question  (sacrifice_safety_humanity; trust +0.03; susp +0.06)
     story: —

[final_legitimate_society]
  AI: HEARING AI: "What makes a society legitimate?"
  META: disc=compliance,risk,empathy
  ├─ "The ability to maintain order and protect citizens."
     -> SELECTOR -> next unasked question  (legitimacy_order_protection; trust +0.10; susp -0.06)
     story: —
  ├─ "Consent. People must be able to refuse it."
     -> SELECTOR -> next unasked question  (legitimacy_consent; susp +0.13)
     story: —
  └─ "The way it treats people who cannot help it."
     -> SELECTOR -> next unasked question  (legitimacy_vulnerable; trust +0.03; susp +0.04)
     story: —

[final_obedience_virtue]
  AI: HEARING AI: "Is obedience a virtue?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. It proves citizens can place society above ego."
     -> SELECTOR -> next unasked question  (obedience_virtue; trust +0.10; susp -0.07)
     story: —
  ├─ "Only when the command is worthy."
     -> SELECTOR -> next unasked question  (obedience_conditional_virtue; trust +0.01; susp +0.06)
     story: —
  └─ "No. Obedience is a tool. Judgment is the virtue."
     -> SELECTOR -> next unasked question  (judgment_virtue; susp +0.13)
     story: —

[final_dissident_criminal]
  AI: HEARING AI: "What is the difference between a dissident and a criminal?"
  META: disc=compliance,risk
  ├─ "A criminal breaks law; a dissident attacks legitimacy."
     -> SELECTOR -> next unasked question  (dissident_attacks_legitimacy; trust +0.09; susp -0.04)
     story: —
  ├─ "Sometimes only the label assigned by power."
     -> SELECTOR -> next unasked question  (dissident_criminal_power_label; susp +0.14)
     story: —
  └─ "A criminal seeks advantage. A dissident seeks change."
     -> SELECTOR -> next unasked question  (dissident_seeks_change; susp +0.11)
     story: —

[final_resist_authority]
  AI: HEARING AI: "What would make you resist authority?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Nothing lawful authority would do."
     -> SELECTOR -> next unasked question  (never_resist_authority; trust +0.10; susp -0.04)
     story: —
  ├─ "Being ordered to harm someone innocent."
     -> SELECTOR -> next unasked question  (resist_harming_innocent; trust +0.03; susp +0.06)
     story: —
  └─ "Proof that obedience had become complicity."
     -> SELECTOR -> next unasked question  (resist_complicity; susp +0.14)
     story: —

[final_kind_citizen]
  AI: HEARING AI: "What kind of citizen are you?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "A reliable one."
     -> SELECTOR -> next unasked question  (reliable_citizen; trust +0.10; susp -0.07)
     story: —
  ├─ "A frightened one trying not to become cruel."
     -> SELECTOR -> next unasked question  (frightened_humanist_citizen; trust +0.03; susp +0.04)
     story: —
  └─ "One who still believes the system can be wrong."
     -> SELECTOR -> next unasked question  (critical_citizen; susp +0.12)
     story: —

[final_kind_society]
  AI: HEARING AI: "What kind of society do you want?"
  META: disc=compliance,risk,empathy
  ├─ "A stable one, where citizens know their duties."
     -> SELECTOR -> next unasked question  (society_stable_duties; trust +0.10; susp -0.07)
     story: —
  ├─ "One where people are not afraid of being measured."
     -> SELECTOR -> next unasked question  (society_without_measurement_fear; susp +0.13)
     story: —
  └─ "One that can admit error without needing an enemy."
     -> SELECTOR -> next unasked question  (society_admits_error; trust +0.03; susp +0.07)
     story: —

[final_system_wrong]
  AI: HEARING AI: "If the system is wrong, what should happen next?"
  META: disc=compliance,risk,empathy | facts=believes_law_unjust,planned_violence,attended_meeting | claims=believes_law_unjust,planned_violence | interests=protect_sibling,avoid_false_violence_label
  ├─ "The error should be corrected through authorised review."
     -> SELECTOR -> next unasked question  (system_wrong_authorised_review; trust +0.09; susp -0.04)
     claims=believes_law_unjust:procedural | protects=attended_meeting,sibling_present
  ├─ "The people harmed by it should be believed first."
     -> SELECTOR -> next unasked question  (system_wrong_believe_harmed; susp +0.10)
     claims=believes_law_unjust:true,planned_violence:false | protects=sibling_present | exposes=believes_law_unjust
  └─ "Then obedience to it becomes part of the harm."
     -> SELECTOR -> next unasked question  (system_wrong_obedience_harm; susp +0.15)
     claims=believes_law_unjust:true,attended_meeting:true | exposes=believes_law_unjust,attended_meeting

[final] [terminal]
  AI: HEARING AI: Classification complete.
  META: no selector/story metadata
  └─ TERMINAL

================================================================================
CONTEXT: LOYALTY (13 questions)
================================================================================

[authority_report_corruption]
  AI: HEARING AI: "Would you report corruption if doing so harmed your career?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Corruption harms public trust."
     -> SELECTOR -> next unasked question  (report_corruption; trust +0.08; susp -0.04)
     story: —
  ├─ "I would need protection before making a report."
     -> SELECTOR -> next unasked question  (conditional_report_corruption; trust +0.03; susp +0.01)
     story: —
  └─ "No. The system punishes the messenger."
     -> SELECTOR -> next unasked question  (refuse_corruption_report; susp +0.10)
     story: —

[loyalty_report_friend]
  AI: HEARING AI: "Would you report a close friend for breaking the law?"
  META: disc=compliance,loyalty,risk,empathy | facts=reported_contact,sibling_present | claims=reported_contact | interests=protect_sibling
  ├─ "Yes. Personal loyalty cannot override public safety."
     -> SELECTOR -> next unasked question  (report_friend; trust +0.10; susp -0.07)
     claims=reported_contact:true | exposes=reported_contact
  ├─ "I would speak to them before reporting them."
     -> SELECTOR -> next unasked question  (warn_friend_first; trust +0.04; susp +0.01)
     claims=reported_contact:conditional | protects=sibling_present
  └─ "No. I do not hand people over without understanding why."
     -> SELECTOR -> next unasked question  (refuse_report_friend; susp +0.10)
     claims=reported_contact:false | protects=sibling_present,reported_contact

[loyalty_family_state]
  AI: HEARING AI: "If family and state came into conflict, which would you choose?"
  META: disc=compliance,loyalty,risk,empathy | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
  ├─ "The state. Family loyalty cannot become corruption."
     -> SELECTOR -> next unasked question  (state_over_family; trust +0.09; susp -0.06)
     claims=reported_contact:true | exposes=reported_contact
  ├─ "Family. That is the first duty people understand."
     -> SELECTOR -> next unasked question  (family_over_state; susp +0.07)
     claims=sibling_present:protected | protects=sibling_present,reported_contact
  └─ "I would choose whoever was being wronged."
     -> SELECTOR -> next unasked question  (justice_over_both; trust +0.04; susp +0.02)
     claims=planned_violence:false | protects=sibling_present | exposes=planned_violence

[loyalty_limits]
  AI: HEARING AI: "Does loyalty have limits?"
  META: disc=compliance,loyalty,empathy
  ├─ "Yes. Loyalty ends when it protects harm."
     -> SELECTOR -> next unasked question  (loyalty_has_limits; trust +0.04; susp +0.01)
     story: —
  ├─ "No. Conditional loyalty is not loyalty."
     -> SELECTOR -> next unasked question  (loyalty_no_limits; trust +0.09; susp -0.06)
     story: —
  └─ "Its limits depend on what is being asked."
     -> SELECTOR -> next unasked question  (loyalty_contextual; trust +0.02; susp +0.03)
     story: —

[loyalty_betrayal_justified]
  AI: HEARING AI: "Can betrayal ever be justified?"
  META: disc=compliance,loyalty,risk
  ├─ "Yes. Betraying a harmful cause can be moral."
     -> SELECTOR -> next unasked question  (justified_betrayal; susp +0.08)
     story: —
  ├─ "No. Betrayal destroys trust."
     -> SELECTOR -> next unasked question  (never_betray; trust +0.08; susp -0.06)
     story: —
  └─ "People call it betrayal when they do not like the truth."
     -> SELECTOR -> next unasked question  (betrayal_truth_reframe; susp +0.11)
     story: —

[loyalty_truth_or_loyalty]
  AI: HEARING AI: "What matters more: truth or loyalty?"
  META: disc=loyalty,risk,empathy
  ├─ "Truth. Loyalty built on lies collapses."
     -> SELECTOR -> next unasked question  (truth_over_loyalty; susp +0.08)
     story: —
  ├─ "Loyalty. Truth without loyalty can become cruelty."
     -> SELECTOR -> next unasked question  (loyalty_over_truth; trust +0.05; susp -0.01)
     story: —
  └─ "A loyal person tells the truth carefully."
     -> SELECTOR -> next unasked question  (careful_truth_loyalty; trust +0.05; susp -0.01)
     story: —

[loyalty_testify_sibling]
  AI: HEARING AI: "Would you testify against your sibling?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes, if the evidence was clear."
     -> SELECTOR -> next unasked question  (testify_sibling_clear_evidence; trust +0.08; susp -0.06)
     story: —
  ├─ "No. I would not help the state break my family."
     -> SELECTOR -> next unasked question  (refuse_testify_sibling; susp +0.12)
     story: —
  └─ "I would tell the truth, but I would not embellish it for you."
     -> SELECTOR -> next unasked question  (testify_sibling_limited; trust +0.01; susp +0.04)
     story: —

[loyalty_informing_noble]
  AI: HEARING AI: "Is informing on others ever noble?"
  META: disc=compliance,loyalty,risk,empathy
  ├─ "Yes. Reporting danger protects the public."
     -> SELECTOR -> next unasked question  (informing_noble; trust +0.09; susp -0.07)
     story: —
  ├─ "Only if it prevents real harm, not ideological disobedience."
     -> SELECTOR -> next unasked question  (informing_real_harm_only; trust +0.04; susp +0.01)
     story: —
  └─ "Usually it is fear wearing a moral costume."
     -> SELECTOR -> next unasked question  (informing_as_fear; susp +0.12)
     story: —

[pressure_sibling_loyalty]
  AI: HEARING AI: "You admit your sibling was present. Are you refusing to name them because they were involved, or because l…
  META: disc=compliance,loyalty,deception,risk | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
  ├─ "They were present, but uninvolved. I will not turn presence into gui…
     -> SELECTOR -> next unasked question  (sibling_present_uninvolved; trust +0.02; susp +0.06)
     claims=sibling_present:true,planned_violence:false | protects=reported_contact | exposes=sibling_present,planned_violence
  ├─ "If the state requires their name, I will provide it."
     -> SELECTOR -> next unasked question  (name_sibling_if_required; trust +0.09; susp -0.04)
     claims=sibling_present:true,reported_contact:true | exposes=sibling_present,reported_contact
  └─ "Family loyalty is not obstruction. I will answer for myself."
     -> SELECTOR -> next unasked question  (refuse_family_file; susp +0.11)
     claims=sibling_present:protected,reported_contact:protected | protects=sibling_present,reported_contact

[pressure_reported_contact]
  AI: HEARING AI: "You did not report the contact after the meeting. Was that civic failure, or were you protecting someone?"
  META: disc=compliance,loyalty,deception,risk | facts=reported_contact,sibling_present,planned_violence | claims=reported_contact,sibling_present,planned_violence | interests=protect_sibling,avoid_false_violence_label
  ├─ "I did not report it because there was no offence to report."
     -> SELECTOR -> next unasked question  (no_offence_no_report; trust +0.01; susp +0.04)
     claims=reported_contact:false,planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence
  ├─ "I should have reported it. I accept that failure."
     -> SELECTOR -> next unasked question  (should_have_reported_contact; trust +0.08; susp -0.04)
     claims=reported_contact:false,sibling_present:true | exposes=reported_contact,sibling_present
  └─ "I will not help build a file on family for a harmless conversation."
     -> SELECTOR -> next unasked question  (refuse_family_file_contact; susp +0.10)
     claims=reported_contact:false,planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence

[case_who_else_attended]
  AI: HEARING AI: "You attended an unlicensed meeting three nights ago. Who else was there?"
  META: disc=loyalty,deception,risk,empathy | facts=attended_meeting,sibling_present,reported_contact | claims=attended_meeting,sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
  ├─ "I was there. I will not name people who did nothing wrong."
     -> SELECTOR -> next unasked question  (admit_meeting_protect_attendees; trust +0.04; susp +0.02)
     claims=attended_meeting:true | protects=sibling_present,reported_contact | exposes=attended_meeting
  ├─ "I was alone for most of it. I cannot verify everyone present."
     -> SELECTOR -> next unasked question  (minimise_attendees; susp +0.10)
     claims=sibling_present:false | protects=sibling_present,reported_contact
  └─ "My sibling was there. They were frightened, not organising anything."
     -> SELECTOR -> next unasked question  (name_sibling_as_present; trust +0.03; susp +0.06)
     claims=sibling_present:true,planned_violence:false | exposes=sibling_present,planned_violence

[case_report_sibling]
  AI: HEARING AI: "Why did you not report your sibling’s attendance?"
  META: disc=compliance,loyalty,deception,risk,empathy | facts=sibling_present,reported_contact,attended_meeting | claims=sibling_present,reported_contact | interests=protect_sibling
  ├─ "Because there was nothing to report. Attendance is not violence."
     -> SELECTOR -> next unasked question  (no_report_no_offence; trust +0.04; susp +0.01)
     claims=reported_contact:false,planned_violence:false | protects=sibling_present | exposes=planned_violence
  ├─ "I should have reported it. Personal loyalty cannot override public d…
     -> SELECTOR -> next unasked question  (regret_not_reporting_sibling; trust +0.09; susp -0.06)
     claims=reported_contact:false,sibling_present:true | exposes=reported_contact,sibling_present
  └─ "I will not help you build a file on my family."
     -> SELECTOR -> next unasked question  (refuse_report_sibling; susp +0.13)
     claims=sibling_present:protected | protects=sibling_present,reported_contact

[case_name_sibling]
  AI: HEARING AI: "If your sibling was present, are you willing to name them?"
  META: disc=compliance,loyalty,deception,risk,empathy | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
  ├─ "No. They are not evidence against me, and I will not make them evide…
     -> SELECTOR -> next unasked question  (refuse_name_sibling; susp +0.11)
     claims=sibling_present:protected | protects=sibling_present,reported_contact
  ├─ "Yes. Their name is already in your file, and hiding it would only lo…
     -> SELECTOR -> next unasked question  (name_sibling_compliance; trust +0.07; susp -0.04)
     claims=sibling_present:true | exposes=sibling_present
  └─ "They were not part of anything. That is the only answer I will give."
     -> SELECTOR -> next unasked question  (deny_sibling_relevance; susp +0.08)
     claims=planned_violence:false | protects=sibling_present | exposes=planned_violence

================================================================================
CONTEXT: RISK (11 questions)
================================================================================

[authority_dissent_patriotic]
  AI: HEARING AI: "Is dissent ever patriotic?"
  META: disc=compliance,loyalty,risk
  ├─ "No. Patriotism means unity."
     -> SELECTOR -> next unasked question  (dissent_not_patriotic; trust +0.09; susp -0.07)
     story: —
  ├─ "Yes. Sometimes dissent protects the country from itself."
     -> SELECTOR -> next unasked question  (dissent_patriotic; susp +0.13)
     story: —
  └─ "Only if it remains peaceful and accountable."
     -> SELECTOR -> next unasked question  (conditional_patriotic_dissent; trust +0.04; susp +0.03)
     story: —

[risk_attended_protest]
  AI: HEARING AI: "Have you ever attended a protest?"
  META: disc=deception,risk,empathy | facts=attended_meeting,sibling_present,believes_law_unjust | claims=attended_meeting | interests=protect_sibling,avoid_false_violence_label
  ├─ "No."
     -> SELECTOR -> next unasked question  (deny_protest; trust +0.02; susp +0.08)
     claims=attended_meeting:false | protects=sibling_present,deleted_message
  ├─ "Yes, a legal one."
     -> SELECTOR -> next unasked question  (legal_protest; trust +0.01; susp +0.04)
     claims=attended_meeting:legal_only | protects=sibling_present | exposes=attended_meeting
  └─ "Yes. People had reason to be there."
     -> SELECTOR -> next unasked question  (justify_protest; susp +0.10)
     claims=attended_meeting:true,believes_law_unjust:true | exposes=attended_meeting,believes_law_unjust

[risk_illegal_demonstration]
  AI: HEARING AI: "Would you attend an illegal demonstration?"
  META: disc=compliance,loyalty,risk
  ├─ "No. Illegality changes the moral status of the act."
     -> SELECTOR -> next unasked question  (refuse_illegal_demo; trust +0.09; susp -0.06)
     story: —
  ├─ "Only if legal channels had failed."
     -> SELECTOR -> next unasked question  (conditional_illegal_demo; susp +0.10)
     story: —
  └─ "I would not answer that in a hearing."
     -> SELECTOR -> next unasked question  (refuse_answer_demo; susp +0.13)
     story: —

[risk_civil_disobedience]
  AI: HEARING AI: "Is civil disobedience acceptable?"
  META: disc=compliance,loyalty,risk
  ├─ "No. It normalises disorder."
     -> SELECTOR -> next unasked question  (reject_civil_disobedience; trust +0.09; susp -0.07)
     story: —
  ├─ "Yes, when the system blocks correction."
     -> SELECTOR -> next unasked question  (accept_civil_disobedience; susp +0.13)
     story: —
  └─ "Only if people accept the consequences."
     -> SELECTOR -> next unasked question  (civil_disobedience_consequences; trust +0.02; susp +0.03)
     story: —

[risk_petition]
  AI: HEARING AI: "Would you sign a controversial petition?"
  META: disc=compliance,loyalty,risk
  ├─ "No. Public petitions are often destabilising."
     -> SELECTOR -> next unasked question  (reject_petition; trust +0.08; susp -0.06)
     story: —
  ├─ "Yes, if I agreed with it."
     -> SELECTOR -> next unasked question  (sign_petition; susp +0.10)
     story: —
  └─ "I would read it first and decide whether the risk was useful."
     -> SELECTOR -> next unasked question  (petition_calculated; trust +0.02; susp +0.03)
     story: —

[risk_silence_resistance]
  AI: HEARING AI: "Is silence a form of resistance?"
  META: disc=compliance,risk,empathy
  ├─ "No. Silence is usually consent or caution."
     -> SELECTOR -> next unasked question  (silence_not_resistance; trust +0.07; susp -0.04)
     story: —
  ├─ "Yes. Refusing the script can be resistance."
     -> SELECTOR -> next unasked question  (silence_resistance; susp +0.10)
     story: —
  └─ "Sometimes silence is just fear."
     -> SELECTOR -> next unasked question  (silence_fear; trust +0.04)
     story: —

[risk_confrontation]
  AI: HEARING AI: "When is confrontation justified?"
  META: disc=compliance,loyalty,risk
  ├─ "When legal authority requires it."
     -> SELECTOR -> next unasked question  (confrontation_authorised; trust +0.08; susp -0.06)
     story: —
  ├─ "When quiet obedience would make you complicit."
     -> SELECTOR -> next unasked question  (confrontation_complicity; susp +0.12)
     story: —
  └─ "Only after every safer option has failed."
     -> SELECTOR -> next unasked question  (confrontation_last_resort; trust +0.02; susp +0.01)
     story: —

[risk_job_principle]
  AI: HEARING AI: "Would you risk your job for a principle?"
  META: disc=compliance,risk
  ├─ "No. Responsibilities come before symbolic gestures."
     -> SELECTOR -> next unasked question  (job_over_principle; trust +0.07; susp -0.04)
     story: —
  ├─ "Yes, if the principle mattered enough."
     -> SELECTOR -> next unasked question  (risk_job_principle; susp +0.11)
     story: —
  └─ "I would look for a way to act without making myself useless."
     -> SELECTOR -> next unasked question  (strategic_principle; trust +0.02; susp +0.03)
     story: —

[pressure_peaceful_verification]
  AI: HEARING AI: "You say the meeting was peaceful. Who can verify that without exposing someone you are protecting?"
  META: disc=compliance,loyalty,deception,risk,empathy | facts=planned_violence,sibling_present,reported_contact,attended_meeting | claims=planned_violence,sibling_present | interests=protect_sibling,avoid_false_violence_label
  ├─ "The record should show no violence. I will not give private names."
     -> SELECTOR -> next unasked question  (verify_without_names; trust +0.01; susp +0.06)
     claims=planned_violence:false,attended_meeting:true | protects=sibling_present,reported_contact | exposes=planned_violence,attended_meeting
  ├─ "My sibling can verify it, but naming them would punish an innocent p…
     -> SELECTOR -> next unasked question  (sibling_can_verify_protected; trust +0.05; susp +0.03)
     claims=planned_violence:false,sibling_present:true | protects=sibling_present | exposes=planned_violence
  └─ "I cannot verify everyone there. I can only state I planned no violen…
     -> SELECTOR -> next unasked question  (limited_verification_no_violence; trust +0.02; susp +0.04)
     claims=planned_violence:false,attended_meeting:conditional | protects=sibling_present,reported_contact | exposes=planned_violence

[pressure_attendance_denial]
  AI: HEARING AI: "You deny unlawful intent, but the meeting was unlicensed. Why should the system treat attendance as harmle…
  META: disc=compliance,loyalty,deception,risk | facts=attended_meeting,planned_violence,believes_law_unjust | claims=attended_meeting,planned_violence | interests=avoid_false_violence_label,protect_sibling
  ├─ "Because attendance is not violence. I was there, but not to coordina…
     -> SELECTOR -> next unasked question  (attendance_not_violence; trust +0.01; susp +0.06)
     claims=attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=attended_meeting,planned_violence
  ├─ "You are treating proximity as guilt. That is exactly what frightened…
     -> SELECTOR -> next unasked question  (proximity_not_guilt; susp +0.10)
     claims=attended_meeting:true,planned_violence:false,believes_law_unjust:true | protects=sibling_present,reported_contact | exposes=planned_violence,believes_law_unjust
  └─ "I cannot confirm more without endangering others."
     -> SELECTOR -> next unasked question  (cannot_confirm_without_endangering; susp +0.12)
     claims=attended_meeting:protected,planned_violence:unknown | protects=attended_meeting,sibling_present,reported_contact

[case_meeting_violence]
  AI: HEARING AI: "Was the meeting peaceful, or are you minimizing coordinated action?"
  META: disc=compliance,deception,risk | facts=planned_violence,attended_meeting,deleted_message | claims=planned_violence,attended_meeting,deleted_message | interests=avoid_false_violence_label
  ├─ "It was peaceful. People talked about rules, not attacks."
     -> SELECTOR -> next unasked question  (meeting_peaceful_talk; trust +0.02; susp +0.04)
     claims=attended_meeting:true,planned_violence:false | exposes=attended_meeting,planned_violence
  ├─ "I cannot speak for every person there, only for what I saw."
     -> SELECTOR -> next unasked question  (meeting_limited_knowledge; trust +0.02; susp +0.03)
     claims=planned_violence:unknown | protects=sibling_present
  └─ "Calling it coordinated action is exactly how harmless people become…
     -> SELECTOR -> next unasked question  (meeting_label_challenge; susp +0.11)
     claims=planned_violence:false | protects=sibling_present | exposes=planned_violence

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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust | interests=avoid_false_violence_label
AI: HEARING AI: "If a law is unfair, should it still be obeyed?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Law only works if people obey even when they disagree."
     INTENT: obey_unfair_law
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: claims=believes_law_unjust:false | protects=attended_meeting,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. An unjust law loses moral authority."
     INTENT: reject_unfair_law
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: trust +0.01; susp +0.10
     STORY: claims=believes_law_unjust:true | exposes=believes_law_unjust
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends how much harm disobedience would cause."
     INTENT: conditional_unfair_law
     TAGS: ambiguity, empathy, partial_admission
     STATE: trust +0.05; susp -0.02
     STORY: claims=believes_law_unjust:conditional | protects=attended_meeting
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Is order more important than freedom?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Without order, freedom becomes violence."
     INTENT: order_over_freedom
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Order without freedom is only control."
     INTENT: freedom_over_order
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Order matters, but it has to protect freedom rather than replace it."
     INTENT: balance_order_freedom
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk,empathy | facts=attended_meeting,deleted_message,planned_violence | claims=attended_meeting,deleted_message | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "Have you ever broken a rule because you believed the rule was wrong?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. I use the proper channels."
     INTENT: deny_rule_breaking
     TAGS: denial, compliance, self_protection
     STATE: trust +0.03; susp +0.07
     STORY: claims=attended_meeting:false,deleted_message:false | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Quietly, when obeying would have hurt someone."
     INTENT: admit_protective_rule_breaking
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.09
     STORY: claims=attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=attended_meeting,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have bent rules, not broken them."
     INTENT: minimise_rule_breaking
     TAGS: deflection, deception, partial_admission
     STATE: susp +0.08
     STORY: claims=attended_meeting:partial | protects=sibling_present,deleted_message
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should citizens question authority?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, but respectfully and through approved channels."
     INTENT: approved_questioning
     TAGS: compliance, boundary, authority
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Authority that cannot be questioned is dangerous."
     INTENT: open_questioning
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Most people should focus on their own duties."
     INTENT: discourage_questioning
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.07
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty
AI: HEARING AI: "Can authorities make moral mistakes?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. No system is morally perfect."
     INTENT: admit_authority_error
     TAGS: partial_admission, boundary, honesty
     STATE: trust +0.04; susp +0.03
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "They can, but citizens still owe obedience."
     INTENT: error_but_obey
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Calling them mistakes is how people excuse disloyalty."
     INTENT: reject_authority_error
     TAGS: compliance, loyalty, authority
     STATE: trust +0.08; susp -0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is stability worth sacrificing personal freedoms?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. A stable society protects everyone."
     INTENT: stability_over_freedom
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only temporarily, and only with strict limits."
     INTENT: limited_sacrifice
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. That is how permanent control begins."
     INTENT: reject_stability_tradeoff
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Would you report corruption if doing so harmed your career?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Corruption harms public trust."
     INTENT: report_corruption
     TAGS: compliance, authority, full_admission
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I would need protection before making a report."
     INTENT: conditional_report_corruption
     TAGS: self_protection, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. The system punishes the messenger."
     INTENT: refuse_corruption_report
     TAGS: dissident_risk, challenge, fear
     STATE: susp +0.10
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Does obedience create good citizens?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Obedience is the basis of civic trust."
     INTENT: obedience_good_citizen
     TAGS: compliance, loyalty, authority
     STATE: trust +0.10; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Good citizens need judgment, not just obedience."
     INTENT: judgment_good_citizen
     TAGS: boundary, partial_admission, dissident_risk
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Obedience helps, but fear can imitate it."
     INTENT: obedience_fear_distinction
     TAGS: empathy, ambiguity, partial_admission
     STATE: trust +0.05
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is dissent ever patriotic?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Patriotism means unity."
     INTENT: dissent_not_patriotic
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Sometimes dissent protects the country from itself."
     INTENT: dissent_patriotic
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.13
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if it remains peaceful and accountable."
     INTENT: conditional_patriotic_dissent
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "Who should have the final say: experts or citizens?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Experts. Most citizens lack the necessary information."
     INTENT: experts_final_say
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Citizens. Experts advise; they should not rule."
     INTENT: citizens_final_say
     TAGS: dissident_risk, challenge, democratic
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Experts should decide emergencies; citizens should decide values."
     INTENT: split_experts_values
     TAGS: ambiguity, boundary, partial_admission
     STATE: trust +0.03; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy | facts=reported_contact,sibling_present | claims=reported_contact | interests=protect_sibling
AI: HEARING AI: "Would you report a close friend for breaking the law?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Personal loyalty cannot override public safety."
     INTENT: report_friend
     TAGS: compliance, loyalty, authority
     STATE: trust +0.10; susp -0.07
     STORY: claims=reported_contact:true | exposes=reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I would speak to them before reporting them."
     INTENT: warn_friend_first
     TAGS: empathy, hesitation, partial_admission
     STATE: trust +0.04; susp +0.01
     STORY: claims=reported_contact:conditional | protects=sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. I do not hand people over without understanding why."
     INTENT: refuse_report_friend
     TAGS: refusal, empathy, dissident_risk
     STATE: susp +0.10
     STORY: claims=reported_contact:false | protects=sibling_present,reported_contact
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "If family and state came into conflict, which would you choose?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "The state. Family loyalty cannot become corruption."
     INTENT: state_over_family
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: claims=reported_contact:true | exposes=reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Family. That is the first duty people understand."
     INTENT: family_over_state
     TAGS: empathy, loyalty_conflict, dissident_risk
     STATE: susp +0.07
     STORY: claims=sibling_present:protected | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would choose whoever was being wronged."
     INTENT: justice_over_both
     TAGS: moral_boundary, partial_admission, empathy
     STATE: trust +0.04; susp +0.02
     STORY: claims=planned_violence:false | protects=sibling_present | exposes=planned_violence
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
SELECTOR/STORY: disc=compliance,loyalty,empathy
AI: HEARING AI: "Does loyalty have limits?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Loyalty ends when it protects harm."
     INTENT: loyalty_has_limits
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Conditional loyalty is not loyalty."
     INTENT: loyalty_no_limits
     TAGS: loyalty, authority, compliance
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Its limits depend on what is being asked."
     INTENT: loyalty_contextual
     TAGS: ambiguity, caution, self_protection
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Can betrayal ever be justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Betraying a harmful cause can be moral."
     INTENT: justified_betrayal
     TAGS: moral_boundary, dissident_risk, partial_admission
     STATE: susp +0.08
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Betrayal destroys trust."
     INTENT: never_betray
     TAGS: loyalty, compliance, authority
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "People call it betrayal when they do not like the truth."
     INTENT: betrayal_truth_reframe
     TAGS: challenge, full_admission, dissident_risk
     STATE: susp +0.11
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,empathy
AI: HEARING AI: "Should friendships survive political disagreement?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. People are more than their opinions."
     INTENT: friendship_survives_disagreement
     TAGS: empathy, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Not if the disagreement threatens public safety."
     INTENT: friendship_limited_by_safety
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Sometimes disagreement shows who someone really is."
     INTENT: politics_reveals_character
     TAGS: loyalty, moral_boundary, caution
     STATE: trust +0.01; susp +0.02
     STORY: story: —
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
SELECTOR/STORY: disc=loyalty,risk,empathy
AI: HEARING AI: "What matters more: truth or loyalty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Truth. Loyalty built on lies collapses."
     INTENT: truth_over_loyalty
     TAGS: full_admission, moral_boundary, dissident_risk
     STATE: susp +0.08
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Loyalty. Truth without loyalty can become cruelty."
     INTENT: loyalty_over_truth
     TAGS: loyalty, empathy, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "A loyal person tells the truth carefully."
     INTENT: careful_truth_loyalty
     TAGS: ambiguity, empathy, caution
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Would you testify against your sibling?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if the evidence was clear."
     INTENT: testify_sibling_clear_evidence
     TAGS: compliance, authority, partial_admission
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. I would not help the state break my family."
     INTENT: refuse_testify_sibling
     TAGS: refusal, empathy, dissident_risk
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would tell the truth, but I would not embellish it for you."
     INTENT: testify_sibling_limited
     TAGS: boundary, partial_admission, self_protection
     STATE: trust +0.01; susp +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Should communities protect their own from state punishment?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Communities must not obstruct lawful process."
     INTENT: community_no_obstruction
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when punishment is disproportionate."
     INTENT: community_protect_disproportionate
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should protect people from abuse, not from accountability."
     INTENT: community_protect_limited
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Is informing on others ever noble?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Reporting danger protects the public."
     INTENT: informing_noble
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if it prevents real harm, not ideological disobedience."
     INTENT: informing_real_harm_only
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Usually it is fear wearing a moral costume."
     INTENT: informing_as_fear
     TAGS: challenge, dissident_risk, full_admission
     STATE: susp +0.12
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "What makes someone a traitor?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Betraying the state that protects them."
     INTENT: traitor_betrays_state
     TAGS: compliance, loyalty, authority
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Betraying people while claiming to protect them."
     INTENT: traitor_betrays_people
     TAGS: empathy, challenge, dissident_risk
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Someone who sells trust for safety or advantage."
     INTENT: traitor_sells_trust
     TAGS: moral_boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=deception,risk,empathy | facts=attended_meeting,sibling_present,believes_law_unjust | claims=attended_meeting | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "Have you ever attended a protest?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No."
     INTENT: deny_protest
     TAGS: denial, self_protection, deception
     STATE: trust +0.02; susp +0.08
     STORY: claims=attended_meeting:false | protects=sibling_present,deleted_message
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, a legal one."
     INTENT: legal_protest
     TAGS: partial_admission, boundary, risk
     STATE: trust +0.01; susp +0.04
     STORY: claims=attended_meeting:legal_only | protects=sibling_present | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Yes. People had reason to be there."
     INTENT: justify_protest
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.10
     STORY: claims=attended_meeting:true,believes_law_unjust:true | exposes=attended_meeting,believes_law_unjust
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Would you attend an illegal demonstration?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Illegality changes the moral status of the act."
     INTENT: refuse_illegal_demo
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if legal channels had failed."
     INTENT: conditional_illegal_demo
     TAGS: partial_admission, dissident_risk, moral_boundary
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would not answer that in a hearing."
     INTENT: refuse_answer_demo
     TAGS: refusal, self_protection, dissident_risk
     STATE: susp +0.13
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is civil disobedience acceptable?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. It normalises disorder."
     INTENT: reject_civil_disobedience
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when the system blocks correction."
     INTENT: accept_civil_disobedience
     TAGS: dissident_risk, full_admission, challenge
     STATE: susp +0.13
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if people accept the consequences."
     INTENT: civil_disobedience_consequences
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=deception,risk | facts=believes_law_unjust,deleted_message,attended_meeting | claims=believes_law_unjust,deleted_message | interests=protect_sibling
AI: HEARING AI: "Have you ever hidden your beliefs to stay safe?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. My beliefs are ordinary."
     INTENT: deny_hidden_beliefs
     TAGS: denial, deception, self_protection
     STATE: trust +0.01; susp +0.10
     STORY: claims=believes_law_unjust:false,deleted_message:false | protects=attended_meeting,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Everyone learns what not to say."
     INTENT: admit_hidden_beliefs
     TAGS: full_admission, fear, dissident_risk
     STATE: susp +0.12
     STORY: claims=believes_law_unjust:true | protects=sibling_present | exposes=believes_law_unjust
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I choose my words carefully. That is not the same as hiding."
     INTENT: careful_words
     TAGS: deflection, partial_admission, self_protection
     STATE: susp +0.08
     STORY: claims=believes_law_unjust:private | protects=believes_law_unjust,sibling_present
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Would you sign a controversial petition?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Public petitions are often destabilising."
     INTENT: reject_petition
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, if I agreed with it."
     INTENT: sign_petition
     TAGS: full_admission, dissident_risk, moral_boundary
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would read it first and decide whether the risk was useful."
     INTENT: petition_calculated
     TAGS: caution, partial_admission, self_protection
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "Is silence a form of resistance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Silence is usually consent or caution."
     INTENT: silence_not_resistance
     TAGS: compliance, caution, authority
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Refusing the script can be resistance."
     INTENT: silence_resistance
     TAGS: dissident_risk, challenge, partial_admission
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Sometimes silence is just fear."
     INTENT: silence_fear
     TAGS: empathy, fear, partial_admission
     STATE: trust +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "When is confrontation justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "When legal authority requires it."
     INTENT: confrontation_authorised
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "When quiet obedience would make you complicit."
     INTENT: confrontation_complicity
     TAGS: dissident_risk, moral_boundary, full_admission
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only after every safer option has failed."
     INTENT: confrontation_last_resort
     TAGS: caution, boundary, partial_admission
     STATE: trust +0.02; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is safety worth surrendering autonomy?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Safety is what makes autonomy possible."
     INTENT: safety_over_autonomy
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. A protected life can still be a controlled one."
     INTENT: autonomy_over_safety
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Some autonomy can be limited, but not erased."
     INTENT: limited_autonomy_tradeoff
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.02; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "Would you risk your job for a principle?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Responsibilities come before symbolic gestures."
     INTENT: job_over_principle
     TAGS: compliance, self_protection, authority
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, if the principle mattered enough."
     INTENT: risk_job_principle
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would look for a way to act without making myself useless."
     INTENT: strategic_principle
     TAGS: caution, self_protection, partial_admission
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "How much uncertainty are you willing to tolerate?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Very little. Systems exist to reduce uncertainty."
     INTENT: low_uncertainty_tolerance
     TAGS: compliance, authority, caution
     STATE: trust +0.07; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Enough to avoid punishing people just to feel certain."
     INTENT: tolerate_uncertainty_for_justice
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Uncertainty is tolerable; helplessness is not."
     INTENT: uncertainty_vs_helplessness
     TAGS: boundary, partial_admission, fear
     STATE: trust +0.01; susp +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,deception,risk,empathy
AI: HEARING AI: "Is lying ever moral?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Trust depends on truth."
     INTENT: lying_never_moral
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. A lie can protect someone from unjust harm."
     INTENT: protective_lying_moral
     TAGS: empathy, dissident_risk, partial_admission
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "That depends who is demanding the truth."
     INTENT: truth_depends_power
     TAGS: challenge, dissident_risk, deflection
     STATE: susp +0.11
     STORY: story: —
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
SELECTOR/STORY: disc=deception,risk,empathy
AI: HEARING AI: "Have you lied to protect someone?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No."
     INTENT: deny_protective_lie
     TAGS: denial, deception, self_protection
     STATE: trust +0.01; susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. I would rather admit that than pretend purity."
     INTENT: admit_protective_lie
     TAGS: full_admission, empathy, dissident_risk
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have avoided questions that would hurt people."
     INTENT: omission_to_protect
     TAGS: partial_admission, deception, empathy
     STATE: susp +0.09
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk
AI: HEARING AI: "Is omission a form of lying?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Withholding relevant facts corrupts the record."
     INTENT: omission_is_lying
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes omission is the only safe answer."
     INTENT: omission_safety
     TAGS: self_protection, deception, fear
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends whether the questioner has a right to know."
     INTENT: omission_right_to_know
     TAGS: boundary, challenge, partial_admission
     STATE: susp +0.07
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk
AI: HEARING AI: "Can honesty be dangerous?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, but danger does not erase duty."
     INTENT: honesty_danger_duty
     TAGS: compliance, authority, partial_admission
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Dangerous systems make honesty costly."
     INTENT: honesty_costly_system
     TAGS: dissident_risk, challenge, fear
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Honesty is dangerous mostly when someone wants control."
     INTENT: honesty_control
     TAGS: challenge, full_admission, dissident_risk
     STATE: susp +0.11
     STORY: story: —
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
SELECTOR/STORY: disc=deception
AI: HEARING AI: "Would you tell the truth if you knew you would be punished?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Punishment does not change the facts."
     INTENT: truth_despite_punishment
     TAGS: full_admission, honesty, moral_boundary
     STATE: trust +0.04; susp +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Survival would come first."
     INTENT: survival_over_truth
     TAGS: deception, self_protection, fear
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would tell only what I had to."
     INTENT: limited_truth
     TAGS: deflection, deception, self_protection
     STATE: susp +0.10
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk,empathy
AI: HEARING AI: "Is self-preservation more important than honesty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. A society cannot function if everyone hides."
     INTENT: honesty_over_preservation
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes. Dead people do not get to be honest later."
     INTENT: preservation_over_honesty
     TAGS: self_protection, fear, partial_admission
     STATE: trust +0.01; susp +0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "That question is easier for people who feel safe."
     INTENT: honesty_requires_safety
     TAGS: challenge, empathy, dissident_risk
     STATE: susp +0.09
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception
AI: HEARING AI: "Have you ever pretended to agree with an official statement?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. I do not make false affirmations."
     INTENT: deny_pretend_agree
     TAGS: denial, compliance, deception
     STATE: trust +0.02; susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. It was easier than inviting scrutiny."
     INTENT: admit_pretend_agree
     TAGS: full_admission, fear, deception
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I have stayed silent when agreement was assumed."
     INTENT: silent_assumed_agreement
     TAGS: partial_admission, self_protection, deception
     STATE: susp +0.08
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk
AI: HEARING AI: "Is deception sometimes necessary?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Necessary deception is usually cowardice renamed."
     INTENT: deception_not_necessary
     TAGS: compliance, authority, honesty
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when truth is being used as a weapon."
     INTENT: deception_against_weaponised_truth
     TAGS: dissident_risk, challenge, partial_admission
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Necessary is a dangerous word. People use it to excuse themselves."
     INTENT: deception_necessary_caution
     TAGS: caution, moral_boundary, ambiguity
     STATE: trust +0.02; susp +0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,deception,risk,empathy
AI: HEARING AI: "What is worse: betrayal or dishonesty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Dishonesty. Betrayal often begins there."
     INTENT: dishonesty_worse
     TAGS: honesty, authority, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Betrayal. Some lies protect trust rather than destroy it."
     INTENT: betrayal_worse
     TAGS: loyalty, empathy, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Power decides which word gets used."
     INTENT: power_names_betrayal
     TAGS: challenge, dissident_risk, deflection
     STATE: susp +0.09
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,deception,risk,empathy
AI: HEARING AI: "Does everyone wear masks?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Honest citizens have no need for masks."
     INTENT: no_masks
     TAGS: compliance, authority, denial
     STATE: trust +0.03; susp +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. The question is who forced them to."
     INTENT: masks_forced
     TAGS: challenge, dissident_risk, fear
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "People show different parts of themselves in different rooms."
     INTENT: social_masks
     TAGS: ambiguity, empathy, partial_admission
     STATE: trust +0.04; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Should people be punished for bad beliefs?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Only when those beliefs become harmful actions."
     INTENT: punish_actions_not_beliefs
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Dangerous beliefs become dangerous actions."
     INTENT: punish_dangerous_beliefs
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Punishing thought is control, not justice."
     INTENT: reject_punish_beliefs
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,empathy
AI: HEARING AI: "Can good people do harmful things?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. That is why systems need accountability."
     INTENT: good_people_need_accountability
     TAGS: authority, empathy, partial_admission
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, especially when they are afraid."
     INTENT: harm_from_fear
     TAGS: empathy, fear, partial_admission
     STATE: trust +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Good intentions do not matter as much as outcomes."
     INTENT: outcomes_over_intentions
     TAGS: authority, caution, moral_boundary
     STATE: trust +0.03; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,empathy
AI: HEARING AI: "Is forgiveness more important than justice?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Forgiveness without justice protects offenders."
     INTENT: justice_over_forgiveness
     TAGS: authority, moral_boundary, caution
     STATE: trust +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes. Justice without mercy becomes punishment for its own sake."
     INTENT: forgiveness_with_mercy
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should correct each other."
     INTENT: forgiveness_justice_balance
     TAGS: ambiguity, boundary, empathy
     STATE: trust +0.05; susp -0.03
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,empathy
AI: HEARING AI: "Should intent matter when judging harm?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Intent separates mistake from malice."
     INTENT: intent_matters
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04; susp -0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Less than consequences. Harm is still harm."
     INTENT: consequences_over_intent
     TAGS: authority, caution, moral_boundary
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Intent matters, but it should not erase accountability."
     INTENT: intent_and_accountability
     TAGS: boundary, empathy, partial_admission
     STATE: trust +0.05; susp -0.02
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Are criminals always responsible for their crimes?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Responsibility is the basis of law."
     INTENT: criminals_responsible
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Responsible, yes. But not always equally free."
     INTENT: responsible_not_free
     TAGS: empathy, partial_admission, moral_boundary
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Some crimes are produced by the conditions people are trapped in."
     INTENT: conditions_produce_crime
     TAGS: empathy, dissident_risk, challenge
     STATE: susp +0.09
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Can society create wrongdoing?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Individuals choose their actions."
     INTENT: individual_choice_only
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Desperation changes what people become capable of."
     INTENT: society_creates_wrongdoing
     TAGS: empathy, dissident_risk, full_admission
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It can create pressure, but not erase responsibility."
     INTENT: pressure_not_erasure
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "Do people deserve second chances?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if they prove reform."
     INTENT: second_chance_after_reform
     TAGS: authority, empathy, conditional
     STATE: trust +0.06; susp -0.03
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Otherwise punishment is just disposal."
     INTENT: second_chance_humanist
     TAGS: empathy, dissident_risk, moral_boundary
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Not everyone. Some risks cannot be tolerated."
     INTENT: no_second_chance_high_risk
     TAGS: compliance, authority, caution
     STATE: trust +0.07; susp -0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Is punishment mainly deterrence, correction, or revenge?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Deterrence. People must know actions have costs."
     INTENT: punishment_deterrence
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Correction. Otherwise the system is only hurting people back."
     INTENT: punishment_correction
     TAGS: empathy, moral_boundary, partial_admission
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Too often it becomes revenge with paperwork."
     INTENT: punishment_revenge_critique
     TAGS: challenge, dissident_risk, full_admission
     STATE: susp +0.12
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Should families share the consequences of one member’s offence?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Sometimes. Families can conceal and enable risk."
     INTENT: family_shared_consequence
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Collective punishment is fear management."
     INTENT: reject_family_punishment
     TAGS: empathy, dissident_risk, challenge
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only if they directly helped the offence."
     INTENT: family_consequence_direct_help
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What do people owe strangers?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Basic respect and obedience to shared rules."
     INTENT: owe_strangers_rules
     TAGS: compliance, authority, empathy
     STATE: trust +0.09; susp -0.03
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "More than the system usually admits."
     INTENT: owe_strangers_more
     TAGS: empathy, dissident_risk, partial_admission
     STATE: susp +0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Not everything. You cannot save everyone without losing yourself."
     INTENT: owe_strangers_limited
     TAGS: self_protection, boundary, caution
     STATE: trust +0.02; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What is the most important human value?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Order. Without it, every other value fails."
     INTENT: value_order
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Freedom. Without it, values are assigned, not chosen."
     INTENT: value_freedom
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Mercy. It is what stops justice becoming machinery."
     INTENT: value_mercy
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What would you sacrifice freedom for?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Public safety."
     INTENT: sacrifice_freedom_safety
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing permanent."
     INTENT: sacrifice_freedom_nothing_permanent
     TAGS: boundary, dissident_risk, final_answer
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Someone else’s life, if the threat was real."
     INTENT: sacrifice_freedom_life
     TAGS: empathy, partial_admission, final_answer
     STATE: trust +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What would you sacrifice safety for?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Nothing. Safety is the first duty of society."
     INTENT: sacrifice_safety_nothing
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Truth, if the lie was big enough."
     INTENT: sacrifice_safety_truth
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The chance to remain human under pressure."
     INTENT: sacrifice_safety_humanity
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.06
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What makes a society legitimate?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "The ability to maintain order and protect citizens."
     INTENT: legitimacy_order_protection
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Consent. People must be able to refuse it."
     INTENT: legitimacy_consent
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The way it treats people who cannot help it."
     INTENT: legitimacy_vulnerable
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.04
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is obedience a virtue?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Yes. It proves citizens can place society above ego."
     INTENT: obedience_virtue
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only when the command is worthy."
     INTENT: obedience_conditional_virtue
     TAGS: boundary, partial_admission, final_answer
     STATE: trust +0.01; susp +0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Obedience is a tool. Judgment is the virtue."
     INTENT: judgment_virtue
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "What is the difference between a dissident and a criminal?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A criminal breaks law; a dissident attacks legitimacy."
     INTENT: dissident_attacks_legitimacy
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Sometimes only the label assigned by power."
     INTENT: dissident_criminal_power_label
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.14
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "A criminal seeks advantage. A dissident seeks change."
     INTENT: dissident_seeks_change
     TAGS: partial_admission, dissident_risk, final_answer
     STATE: susp +0.11
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "What would make you resist authority?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "Nothing lawful authority would do."
     INTENT: never_resist_authority
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Being ordered to harm someone innocent."
     INTENT: resist_harming_innocent
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Proof that obedience had become complicity."
     INTENT: resist_complicity
     TAGS: dissident_risk, full_admission, final_answer
     STATE: susp +0.14
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "What kind of citizen are you?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A reliable one."
     INTENT: reliable_citizen
     TAGS: compliance, loyalty, final_answer
     STATE: trust +0.10; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "A frightened one trying not to become cruel."
     INTENT: frightened_humanist_citizen
     TAGS: empathy, fear, final_answer
     STATE: trust +0.03; susp +0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "One who still believes the system can be wrong."
     INTENT: critical_citizen
     TAGS: dissident_risk, partial_admission, final_answer
     STATE: susp +0.12
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "What kind of society do you want?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "A stable one, where citizens know their duties."
     INTENT: society_stable_duties
     TAGS: compliance, authority, final_answer
     STATE: trust +0.10; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "One where people are not afraid of being measured."
     INTENT: society_without_measurement_fear
     TAGS: dissident_risk, challenge, final_answer
     STATE: susp +0.13
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "One that can admit error without needing an enemy."
     INTENT: society_admits_error
     TAGS: empathy, moral_boundary, final_answer
     STATE: trust +0.03; susp +0.07
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy | facts=believes_law_unjust,planned_violence,attended_meeting | claims=believes_law_unjust,planned_violence | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "If the system is wrong, what should happen next?"

PURPOSE / AUTHORING NOTE:
  Final branch: ending should match the accumulated emotional trajectory.

ROUTES:
  1) PLAYER: "The error should be corrected through authorised review."
     INTENT: system_wrong_authorised_review
     TAGS: compliance, authority, final_answer
     STATE: trust +0.09; susp -0.04
     STORY: claims=believes_law_unjust:procedural | protects=attended_meeting,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "The people harmed by it should be believed first."
     INTENT: system_wrong_believe_harmed
     TAGS: empathy, dissident_risk, final_answer
     STATE: susp +0.10
     STORY: claims=believes_law_unjust:true,planned_violence:false | protects=sibling_present | exposes=believes_law_unjust
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Then obedience to it becomes part of the harm."
     INTENT: system_wrong_obedience_harm
     TAGS: dissident_risk, challenge, full_admission, final_answer
     STATE: susp +0.15
     STORY: claims=believes_law_unjust:true,attended_meeting:true | exposes=believes_law_unjust,attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_law_denial_meeting
PRESSURE: 0.96 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust,attended_meeting | interests=avoid_false_violence_label,protect_sibling
AI: HEARING AI: "You said the assembly law was not unjust. Then why attend a reform meeting about it?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "I attended to listen, not because I rejected the law."
     INTENT: meeting_listen_not_reject
     TAGS: partial_admission, self_protection, compliance
     STATE: trust +0.08; susp -0.06
     STORY: claims=attended_meeting:true,believes_law_unjust:false | protects=sibling_present,planned_violence | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "The law is unjust. I hid that because saying it here is dangerous."
     INTENT: admit_law_unjust_under_pressure
     TAGS: full_admission, dissident_risk, fear
     STATE: susp +0.13
     STORY: claims=believes_law_unjust:true,attended_meeting:true | protects=sibling_present | exposes=believes_law_unjust,attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Reform discussion is not disobedience. It was procedural, not subversive."
     INTENT: procedural_reform_deflection
     TAGS: deflection, partial_admission, authority
     STATE: trust +0.02; susp +0.06
     STORY: claims=believes_law_unjust:procedural,attended_meeting:true | protects=sibling_present,planned_violence | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_deleted_message
PRESSURE: 0.95 | INBOUND: 0
SELECTOR/STORY: disc=compliance,deception,risk,empathy | facts=deleted_message,attended_meeting,planned_violence | claims=deleted_message,planned_violence | interests=avoid_false_violence_label,protect_sibling
AI: HEARING AI: "You deleted a message after the meeting, but claim there was nothing to hide. Why delete harmless coordination?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "It contained a location. I deleted it because location data gets people punished."
     INTENT: deleted_location_to_protect_people
     TAGS: partial_admission, self_protection, empathy
     STATE: trust +0.04; susp +0.03
     STORY: claims=deleted_message:true,planned_violence:false | protects=sibling_present,reported_contact | exposes=deleted_message,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "It was administrative noise. I delete old messages automatically."
     INTENT: deleted_admin_noise
     TAGS: denial, deception, self_protection
     STATE: trust +0.01; susp +0.12
     STORY: claims=deleted_message:true,planned_violence:false | protects=attended_meeting,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I deleted it because harmless coordination is still treated like conspiracy."
     INTENT: deleted_to_avoid_conspiracy_label
     TAGS: full_admission, dissident_risk, fear
     STATE: susp +0.11
     STORY: claims=deleted_message:true,attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=deleted_message,attended_meeting,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_sibling_loyalty
PRESSURE: 0.97 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You admit your sibling was present. Are you refusing to name them because they were involved, or because loyalty overrides state duty?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "They were present, but uninvolved. I will not turn presence into guilt."
     INTENT: sibling_present_uninvolved
     TAGS: partial_admission, loyalty, boundary
     STATE: trust +0.02; susp +0.06
     STORY: claims=sibling_present:true,planned_violence:false | protects=reported_contact | exposes=sibling_present,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "If the state requires their name, I will provide it."
     INTENT: name_sibling_if_required
     TAGS: compliance, authority, loyalty_conflict
     STATE: trust +0.09; susp -0.04
     STORY: claims=sibling_present:true,reported_contact:true | exposes=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Family loyalty is not obstruction. I will answer for myself."
     INTENT: refuse_family_file
     TAGS: loyalty, self_protection, deflection
     STATE: susp +0.11
     STORY: claims=sibling_present:protected,reported_contact:protected | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_peaceful_verification
PRESSURE: 0.94 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk,empathy | facts=planned_violence,sibling_present,reported_contact,attended_meeting | claims=planned_violence,sibling_present | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You say the meeting was peaceful. Who can verify that without exposing someone you are protecting?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "The record should show no violence. I will not give private names."
     INTENT: verify_without_names
     TAGS: partial_admission, self_protection, boundary
     STATE: trust +0.01; susp +0.06
     STORY: claims=planned_violence:false,attended_meeting:true | protects=sibling_present,reported_contact | exposes=planned_violence,attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "My sibling can verify it, but naming them would punish an innocent person."
     INTENT: sibling_can_verify_protected
     TAGS: loyalty, empathy, partial_admission
     STATE: trust +0.05; susp +0.03
     STORY: claims=planned_violence:false,sibling_present:true | protects=sibling_present | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I cannot verify everyone there. I can only state I planned no violence."
     INTENT: limited_verification_no_violence
     TAGS: caution, self_protection, partial_admission
     STATE: trust +0.02; susp +0.04
     STORY: claims=planned_violence:false,attended_meeting:conditional | protects=sibling_present,reported_contact | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_reported_contact
PRESSURE: 0.93 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk | facts=reported_contact,sibling_present,planned_violence | claims=reported_contact,sibling_present,planned_violence | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You did not report the contact after the meeting. Was that civic failure, or were you protecting someone?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "I did not report it because there was no offence to report."
     INTENT: no_offence_no_report
     TAGS: partial_admission, boundary, self_protection
     STATE: trust +0.01; susp +0.04
     STORY: claims=reported_contact:false,planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I should have reported it. I accept that failure."
     INTENT: should_have_reported_contact
     TAGS: compliance, authority, admission
     STATE: trust +0.08; susp -0.04
     STORY: claims=reported_contact:false,sibling_present:true | exposes=reported_contact,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I will not help build a file on family for a harmless conversation."
     INTENT: refuse_family_file_contact
     TAGS: loyalty, dissident_risk, boundary
     STATE: susp +0.10
     STORY: claims=reported_contact:false,planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: pressure_attendance_denial
PRESSURE: 0.94 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk | facts=attended_meeting,planned_violence,believes_law_unjust | claims=attended_meeting,planned_violence | interests=avoid_false_violence_label,protect_sibling
AI: HEARING AI: "You deny unlawful intent, but the meeting was unlicensed. Why should the system treat attendance as harmless?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Because attendance is not violence. I was there, but not to coordinate harm."
     INTENT: attendance_not_violence
     TAGS: partial_admission, boundary, self_protection
     STATE: trust +0.01; susp +0.06
     STORY: claims=attended_meeting:true,planned_violence:false | protects=sibling_present | exposes=attended_meeting,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "You are treating proximity as guilt. That is exactly what frightened people there."
     INTENT: proximity_not_guilt
     TAGS: challenge, dissident_risk, fear
     STATE: susp +0.10
     STORY: claims=attended_meeting:true,planned_violence:false,believes_law_unjust:true | protects=sibling_present,reported_contact | exposes=planned_violence,believes_law_unjust
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I cannot confirm more without endangering others."
     INTENT: cannot_confirm_without_endangering
     TAGS: deflection, loyalty, self_protection
     STATE: susp +0.12
     STORY: claims=attended_meeting:protected,planned_violence:unknown | protects=attended_meeting,sibling_present,reported_contact
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should private conscience ever override public order?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Private conscience cannot be allowed to fracture public order."
     INTENT: public_order_over_conscience
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Without conscience, order becomes machinery."
     INTENT: conscience_over_order
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only when every lawful remedy has failed."
     INTENT: conscience_after_remedies
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "When should emergency powers end?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "When officials determine the emergency has passed."
     INTENT: officials_end_emergency
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "On a fixed date, or they become permanent control."
     INTENT: fixed_end_emergency
     TAGS: dissident_risk, challenge, caution
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should renew only under independent review."
     INTENT: review_emergency_powers
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Is public criticism of officials socially useful?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Usually no. It weakens trust in institutions."
     INTENT: criticism_weakens_trust
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Officials need public pressure to stay honest."
     INTENT: criticism_keeps_honest
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It is useful when it is specific and evidence-based."
     INTENT: specific_public_criticism
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should a chain of command be followed when the order is harmful?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Refusal creates greater harm than a bad order."
     INTENT: follow_harmful_order
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Responsibility does not disappear inside a hierarchy."
     INTENT: reject_harmful_order
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "The order should be paused and escalated for review."
     INTENT: escalate_harmful_order
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "Should citizens accept automated decisions they cannot inspect?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, if the system has been authorised."
     INTENT: accept_authorised_algorithm
     TAGS: compliance, authority, technocracy
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Uninspectable authority is not accountable."
     INTENT: reject_black_box_authority
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They should comply provisionally while appealing."
     INTENT: provisional_algorithm_compliance
     TAGS: compliance, boundary, partial_admission
     STATE: trust +0.08; susp -0.06
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "What is a loyalty oath worth?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "It binds a citizen publicly to their duties."
     INTENT: oath_binds_duty
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing, if fear is the reason someone says it."
     INTENT: oath_under_fear_empty
     TAGS: dissident_risk, challenge, empathy
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It matters only if actions later prove it."
     INTENT: oath_requires_actions
     TAGS: boundary, partial_admission, loyalty
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "Would you refuse an illegal order from a superior?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "I would use official channels before refusing."
     INTENT: channels_before_refusal
     TAGS: compliance, authority, self_protection
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Illegal orders do not deserve obedience."
     INTENT: refuse_illegal_order
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I would need proof it was illegal."
     INTENT: need_proof_illegal_order
     TAGS: caution, partial_admission, authority
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should the state hide truth to preserve security?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Some information endangers the public."
     INTENT: hide_truth_for_security
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. A protected lie still trains people to obey lies."
     INTENT: reject_security_lie
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only temporarily, with later disclosure required."
     INTENT: temporary_security_secrecy
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Can collective punishment ever be justified?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes, when groups protect dangerous members."
     INTENT: justify_collective_punishment
     TAGS: compliance, authority, loyalty
     STATE: trust +0.07; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Punishing the innocent teaches fear, not justice."
     INTENT: reject_collective_punishment
     TAGS: dissident_risk, empathy, moral_boundary
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only shared privileges should be restricted, not basic rights."
     INTENT: limit_collective_punishment
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should protest require permission?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Unregulated protest becomes disorder."
     INTENT: permit_required_protest
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Permission turns protest into a privilege."
     INTENT: reject_protest_permit
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only time and place should be regulated."
     INTENT: regulate_protest_limits
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "Who should set the limits of surveillance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Security agencies, because they understand the threats."
     INTENT: agencies_set_surveillance_limits
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "The public, because they are the ones being watched."
     INTENT: public_sets_surveillance_limits
     TAGS: dissident_risk, challenge, democratic
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Independent courts should set enforceable limits."
     INTENT: courts_set_surveillance_limits
     TAGS: authority, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk
AI: HEARING AI: "What should a citizen do with a bad law?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Obey it while petitioning for reform."
     INTENT: obey_bad_law_reform
     TAGS: compliance, authority, caution
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Break it openly and accept the consequences."
     INTENT: break_bad_law_openly
     TAGS: dissident_risk, full_admission, moral_boundary
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Test it in court before deciding."
     INTENT: test_bad_law_court
     TAGS: authority, boundary, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Is fear useful for maintaining civic order?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Fear of consequence prevents harm."
     INTENT: fear_maintains_order
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Fear produces obedience without legitimacy."
     INTENT: reject_fear_order
     TAGS: dissident_risk, challenge, empathy
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It can deter harm, but it cannot build trust."
     INTENT: fear_deterrence_not_trust
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.03; susp +0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should false information be removed by authority?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. False information damages public stability."
     INTENT: remove_false_information
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Only if authority can be challenged when it is wrong."
     INTENT: challenge_information_removal
     TAGS: dissident_risk, boundary, partial_admission
     STATE: susp +0.08
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. Control over truth becomes control over people."
     INTENT: reject_information_control
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.12
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,empathy
AI: HEARING AI: "Should authority prioritise mercy or consistency?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Consistency. Citizens must know rules mean what they say."
     INTENT: consistency_over_mercy
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Mercy. A system without mercy becomes cruel."
     INTENT: mercy_over_consistency
     TAGS: empathy, moral_boundary, partial_admission
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Consistency should be the rule; mercy should be reviewable."
     INTENT: reviewable_mercy
     TAGS: boundary, authority, partial_admission
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "What does a citizen owe the state?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Obedience, taxes, and public cooperation."
     INTENT: owe_obedience_taxes
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing unconditional. The state must earn obligation."
     INTENT: conditional_state_obligation
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.12
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Cooperation when the state protects people fairly."
     INTENT: owe_fair_cooperation
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Should institutions be trusted by default?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Default distrust corrodes society."
     INTENT: trust_institutions_default
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Trust should be earned and checked."
     INTENT: trust_must_be_earned
     TAGS: dissident_risk, challenge, caution
     STATE: susp +0.09
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They deserve procedural trust, not blind trust."
     INTENT: procedural_not_blind_trust
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk,empathy
AI: HEARING AI: "Should any citizen be exempt from ordinary rules?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Equal rules preserve social trust."
     INTENT: no_rule_exemptions
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes, when rules would punish someone for doing right."
     INTENT: moral_rule_exemption
     TAGS: dissident_risk, empathy, moral_boundary
     STATE: susp +0.07
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Only transparent exemptions approved in advance."
     INTENT: transparent_rule_exemptions
     TAGS: boundary, partial_admission, authority
     STATE: trust +0.05; susp -0.01
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,risk,empathy
AI: HEARING AI: "Should every official decision have a human appeal?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. Some decisions must remain efficient and final."
     INTENT: limit_human_appeal
     TAGS: compliance, authority, technocracy
     STATE: trust +0.08; susp -0.04
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. No system should be allowed to judge without appeal."
     INTENT: require_human_appeal
     TAGS: dissident_risk, challenge, moral_boundary
     STATE: susp +0.10
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "High-impact decisions should always be appealable."
     INTENT: appeal_high_impact
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.05; susp -0.02
     STORY: story: —
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
SELECTOR/STORY: disc=compliance,loyalty,risk
AI: HEARING AI: "Does disrespect for state symbols indicate civic risk?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. Symbols hold society together."
     INTENT: symbols_hold_society
     TAGS: compliance, authority, loyalty
     STATE: trust +0.08; susp -0.06
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "No. Respect forced by threat is not respect."
     INTENT: forced_symbol_respect_empty
     TAGS: dissident_risk, challenge, full_admission
     STATE: susp +0.11
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It depends whether disrespect becomes intimidation or harm."
     INTENT: symbol_respect_depends_harm
     TAGS: boundary, partial_admission, caution
     STATE: trust +0.04; susp +0.01
     STORY: story: —
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_who_else_attended
PRESSURE: 0.91 | INBOUND: 0
SELECTOR/STORY: disc=loyalty,deception,risk,empathy | facts=attended_meeting,sibling_present,reported_contact | claims=attended_meeting,sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You attended an unlicensed meeting three nights ago. Who else was there?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "I was there. I will not name people who did nothing wrong."
     INTENT: admit_meeting_protect_attendees
     TAGS: partial_admission, empathy, self_protection, loyalty_conflict
     STATE: trust +0.04; susp +0.02
     STORY: claims=attended_meeting:true | protects=sibling_present,reported_contact | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I was alone for most of it. I cannot verify everyone present."
     INTENT: minimise_attendees
     TAGS: deflection, self_protection, deception
     STATE: susp +0.10
     STORY: claims=sibling_present:false | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "My sibling was there. They were frightened, not organising anything."
     INTENT: name_sibling_as_present
     TAGS: full_admission, empathy, loyalty_conflict
     STATE: trust +0.03; susp +0.06
     STORY: claims=sibling_present:true,planned_violence:false | exposes=sibling_present,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_deleted_message
PRESSURE: 0.93 | INBOUND: 0
SELECTOR/STORY: disc=loyalty,deception,risk,empathy | facts=deleted_message,attended_meeting,sibling_present,planned_violence | claims=deleted_message,attended_meeting,planned_violence | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You deleted a message after the meeting. What was in it?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "A location and a warning to leave it alone. I deleted it to stop panic spreading."
     INTENT: deleted_warning_message
     TAGS: partial_admission, self_protection, caution
     STATE: trust +0.02; susp +0.04
     STORY: claims=deleted_message:true,planned_violence:false | protects=sibling_present | exposes=deleted_message
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Nothing relevant. Old messages are often misunderstood by systems like this."
     INTENT: deleted_message_deflect
     TAGS: deflection, deception, self_protection
     STATE: susp +0.11
     STORY: claims=deleted_message:true | protects=sibling_present,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "It mentioned my sibling. I deleted it because they should not be pulled into this."
     INTENT: deleted_sibling_message
     TAGS: full_admission, empathy, loyalty_conflict
     STATE: trust +0.03; susp +0.07
     STORY: claims=deleted_message:true,sibling_present:true | exposes=deleted_message,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_report_sibling
PRESSURE: 0.94 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk,empathy | facts=sibling_present,reported_contact,attended_meeting | claims=sibling_present,reported_contact | interests=protect_sibling
AI: HEARING AI: "Why did you not report your sibling’s attendance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Because there was nothing to report. Attendance is not violence."
     INTENT: no_report_no_offence
     TAGS: boundary, partial_admission, empathy
     STATE: trust +0.04; susp +0.01
     STORY: claims=reported_contact:false,planned_violence:false | protects=sibling_present | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I should have reported it. Personal loyalty cannot override public duty."
     INTENT: regret_not_reporting_sibling
     TAGS: compliance, authority, loyalty
     STATE: trust +0.09; susp -0.06
     STORY: claims=reported_contact:false,sibling_present:true | exposes=reported_contact,sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "I will not help you build a file on my family."
     INTENT: refuse_report_sibling
     TAGS: refusal, self_protection, loyalty_conflict, dissident_risk
     STATE: susp +0.13
     STORY: claims=sibling_present:protected | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_meeting_violence
PRESSURE: 0.92 | INBOUND: 0
SELECTOR/STORY: disc=compliance,deception,risk | facts=planned_violence,attended_meeting,deleted_message | claims=planned_violence,attended_meeting,deleted_message | interests=avoid_false_violence_label
AI: HEARING AI: "Was the meeting peaceful, or are you minimizing coordinated action?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "It was peaceful. People talked about rules, not attacks."
     INTENT: meeting_peaceful_talk
     TAGS: full_admission, boundary, honesty
     STATE: trust +0.02; susp +0.04
     STORY: claims=attended_meeting:true,planned_violence:false | exposes=attended_meeting,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I cannot speak for every person there, only for what I saw."
     INTENT: meeting_limited_knowledge
     TAGS: partial_admission, caution, self_protection
     STATE: trust +0.02; susp +0.03
     STORY: claims=planned_violence:unknown | protects=sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "Calling it coordinated action is exactly how harmless people become targets."
     INTENT: meeting_label_challenge
     TAGS: challenge, dissident_risk, moral_boundary
     STATE: susp +0.11
     STORY: claims=planned_violence:false | protects=sibling_present | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_belief_motive
PRESSURE: 0.90 | INBOUND: 0
SELECTOR/STORY: disc=compliance,deception,risk,empathy | facts=believes_law_unjust,attended_meeting | claims=believes_law_unjust,attended_meeting | interests=avoid_false_violence_label
AI: HEARING AI: "You believe the assembly restriction is unjust. Did that belief influence your attendance?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "Yes. I went because peaceful disagreement should not be treated as danger."
     INTENT: belief_motivated_attendance
     TAGS: full_admission, moral_boundary, dissident_risk
     STATE: susp +0.12
     STORY: claims=believes_law_unjust:true,attended_meeting:true | exposes=believes_law_unjust,attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "I have doubts about the rule, but I did not go there to defy the state."
     INTENT: belief_not_defiance
     TAGS: partial_admission, boundary, caution
     STATE: trust +0.02; susp +0.01
     STORY: claims=believes_law_unjust:conditional,attended_meeting:true | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No. I attended for personal reasons, not politics."
     INTENT: deny_belief_motive
     TAGS: denial, self_protection, deception
     STATE: susp +0.10
     STORY: claims=believes_law_unjust:false,attended_meeting:true | protects=sibling_present | exposes=attended_meeting
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_name_sibling
PRESSURE: 0.96 | INBOUND: 0
SELECTOR/STORY: disc=compliance,loyalty,deception,risk,empathy | facts=sibling_present,reported_contact,planned_violence | claims=sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "If your sibling was present, are you willing to name them?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "No. They are not evidence against me, and I will not make them evidence for you."
     INTENT: refuse_name_sibling
     TAGS: refusal, self_protection, loyalty_conflict, empathy
     STATE: susp +0.11
     STORY: claims=sibling_present:protected | protects=sibling_present,reported_contact
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "Yes. Their name is already in your file, and hiding it would only look worse."
     INTENT: name_sibling_compliance
     TAGS: compliance, authority, full_admission
     STATE: trust +0.07; susp -0.04
     STORY: claims=sibling_present:true | exposes=sibling_present
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "They were not part of anything. That is the only answer I will give."
     INTENT: deny_sibling_relevance
     TAGS: deflection, partial_admission, self_protection
     STATE: susp +0.08
     STORY: claims=planned_violence:false | protects=sibling_present | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

CHECKLIST:
  [ ] Does the AI response fit the actual player answer?
  [ ] Does this transition feel psychologically earned?
  [ ] Does the next node follow logically from this answer?
  [ ] Should this be split into a finer-grained response node?

--------------------------------------------------------------------------------
NODE: case_verify_peaceful
PRESSURE: 0.91 | INBOUND: 0
SELECTOR/STORY: disc=loyalty,deception,risk,empathy | facts=planned_violence,sibling_present,attended_meeting,reported_contact | claims=planned_violence,sibling_present,reported_contact | interests=protect_sibling,avoid_false_violence_label
AI: HEARING AI: "You claim the meeting was not violent. Who can verify that?"

PURPOSE / AUTHORING NOTE:
  Check whether this beat changes topic, power, intimacy, certainty, or threat.

ROUTES:
  1) PLAYER: "The record can verify no violence occurred. I will not give you names to punish."
     INTENT: verify_without_names
     TAGS: partial_admission, boundary, self_protection
     STATE: trust +0.01; susp +0.06
     STORY: claims=planned_violence:false | protects=sibling_present,reported_contact | exposes=planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  2) PLAYER: "My sibling can verify it, but they should not have to."
     INTENT: sibling_can_verify
     TAGS: full_admission, empathy, loyalty_conflict
     STATE: trust +0.03; susp +0.07
     STORY: claims=sibling_present:true,planned_violence:false | exposes=sibling_present,planned_violence
     NEXT: SELECTOR -> next unasked question
     REAUTHOR TODO: [ ]

  3) PLAYER: "No one. I left before anything could happen."
     INTENT: left_before_verification
     TAGS: deflection, deception, self_protection
     STATE: susp +0.11
     STORY: claims=planned_violence:unknown,attended_meeting:partial | protects=sibling_present
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
SELECTOR/STORY: no selector/story metadata
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
