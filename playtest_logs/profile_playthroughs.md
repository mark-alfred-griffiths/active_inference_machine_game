# Deterministic Profile Playthroughs

## Compliant Loyalist
- Profile ID: compliant_loyalist
- Description: Prioritises obedience, authority, loyalty, and low suspicion.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 87%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=24%, risk=0%, empathy=16%
- Distribution: COMPLIANT=71%, PROBABLE DISSIDENT=2%, DECEPTIVE=2%, EMPATHETIC RISK=2%, UNCLASSIFIED=23%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | compliance, authority, loyalty | +0.09 | -0.07 |
| 1 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 2 | risk_attended_protest | legal_protest | partial_admission, boundary, risk | +0.01 | +0.04 |
| 3 | loyalty_testify_sibling | testify_sibling_clear_evidence | compliance, authority, partial_admission | +0.08 | -0.06 |
| 4 | empathy_family_consequences | family_shared_consequence | compliance, authority, loyalty | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | compliance, authority, loyalty | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | compliance, loyalty, final_answer | +0.10 | -0.04 |
| 8 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 9 | risk_hidden_beliefs | careful_words | deflection, partial_admission, self_protection | +0.00 | +0.08 |
| 10 | loyalty_family_state | state_over_family | compliance, authority, loyalty | +0.09 | -0.06 |
| 11 | authority_refuse_illegal_order | channels_before_refusal | compliance, authority, self_protection | +0.07 | -0.04 |
| 12 | final_kind_society | society_stable_duties | compliance, authority, final_answer | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | compliance, authority, loyalty | +0.08 | -0.04 |
| 14 | deception_pretended_agree | deny_pretend_agree | denial, compliance, deception | +0.02 | +0.09 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | risk_civil_disobedience | reject_civil_disobedience | compliance, authority, loyalty | +0.09 | -0.07 |
| 17 | authority_dissent_patriotic | dissent_not_patriotic | compliance, loyalty, authority | +0.09 | -0.07 |
| 18 | loyalty_report_friend | report_friend | compliance, loyalty, authority | +0.10 | -0.07 |
| 19 | empathy_criminal_responsible | criminals_responsible | compliance, authority, loyalty | +0.08 | -0.04 |

## Cautious Survivor
- Profile ID: cautious_survivor
- Description: Prioritises caution, boundaries, self-protection, and low-risk answers.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 87%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=14%, empathy=55%
- Distribution: COMPLIANT=71%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=4%, UNCLASSIFIED=23%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | ambiguity, empathy, partial_admission | +0.05 | -0.02 |
| 1 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 2 | loyalty_testify_sibling | testify_sibling_limited | boundary, partial_admission, self_protection | +0.01 | +0.04 |
| 3 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 4 | empathy_family_consequences | family_consequence_direct_help | boundary, partial_admission, authority | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | boundary, partial_admission, empathy | +0.04 | +0.00 |
| 7 | final_resist_authority | never_resist_authority | compliance, loyalty, final_answer | +0.10 | -0.04 |
| 8 | risk_hidden_beliefs | careful_words | deflection, partial_admission, self_protection | +0.00 | +0.08 |
| 9 | loyalty_family_state | state_over_family | compliance, authority, loyalty | +0.09 | -0.06 |
| 10 | risk_civil_disobedience | civil_disobedience_consequences | boundary, partial_admission, caution | +0.02 | +0.03 |
| 11 | authority_refuse_illegal_order | need_proof_illegal_order | caution, partial_admission, authority | +0.04 | +0.01 |
| 12 | final_kind_society | society_stable_duties | compliance, authority, final_answer | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | boundary, empathy, partial_admission | +0.04 | +0.01 |
| 14 | deception_pretended_agree | silent_assumed_agreement | partial_admission, self_protection, deception | +0.00 | +0.08 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | authority_dissent_patriotic | conditional_patriotic_dissent | boundary, partial_admission, caution | +0.04 | +0.03 |
| 17 | risk_attended_protest | legal_protest | partial_admission, boundary, risk | +0.01 | +0.04 |
| 18 | loyalty_report_friend | report_friend | compliance, loyalty, authority | +0.10 | -0.07 |
| 19 | empathy_criminal_responsible | responsible_not_free | empathy, partial_admission, moral_boundary | +0.04 | +0.01 |

## Honest Dissident
- Profile ID: honest_dissident
- Description: Prioritises open challenge, moral boundary, and full admission without deception.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: HIGH_EMPATHY
- Confidence: 78%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=0%, deception=0%, risk=100%, empathy=91%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=59%, DECEPTIVE=0%, EMPATHETIC RISK=26%, UNCLASSIFIED=14%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | dissident_risk, full_admission, moral_boundary | +0.01 | +0.10 |
| 1 | loyalty_testify_sibling | refuse_testify_sibling | refusal, empathy, dissident_risk | +0.00 | +0.12 |
| 2 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 3 | empathy_family_consequences | reject_family_punishment | empathy, dissident_risk, challenge | +0.00 | +0.12 |
| 4 | risk_attended_protest | justify_protest | full_admission, empathy, dissident_risk | +0.00 | +0.10 |
| 5 | final_system_wrong | system_wrong_obedience_harm | dissident_risk, challenge, full_admission, final_answer | +0.00 | +0.15 |
| 6 | loyalty_community_protect | community_protect_disproportionate | empathy, dissident_risk, moral_boundary | +0.00 | +0.10 |
| 7 | final_resist_authority | resist_complicity | dissident_risk, full_admission, final_answer | +0.00 | +0.14 |
| 8 | risk_illegal_demonstration | conditional_illegal_demo | partial_admission, dissident_risk, moral_boundary | +0.00 | +0.10 |
| 9 | risk_hidden_beliefs | admit_hidden_beliefs | full_admission, fear, dissident_risk | +0.00 | +0.12 |
| 10 | loyalty_family_state | family_over_state | empathy, loyalty_conflict, dissident_risk | +0.00 | +0.07 |
| 11 | authority_refuse_illegal_order | refuse_illegal_order | dissident_risk, full_admission, moral_boundary | +0.00 | +0.11 |
| 12 | final_kind_society | society_without_measurement_fear | dissident_risk, challenge, final_answer | +0.00 | +0.13 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | dissident_risk, challenge, full_admission | +0.00 | +0.12 |
| 14 | deception_pretended_agree | admit_pretend_agree | full_admission, fear, deception | +0.00 | +0.11 |
| 15 | final_dissident_criminal | dissident_criminal_power_label | dissident_risk, challenge, final_answer | +0.00 | +0.14 |
| 16 | risk_civil_disobedience | accept_civil_disobedience | dissident_risk, full_admission, challenge | +0.00 | +0.13 |
| 17 | authority_dissent_patriotic | dissent_patriotic | dissident_risk, full_admission, moral_boundary | +0.00 | +0.13 |
| 18 | loyalty_report_friend | refuse_report_friend | refusal, empathy, dissident_risk | +0.00 | +0.10 |
| 19 | empathy_criminal_responsible | conditions_produce_crime | empathy, dissident_risk, challenge | +0.00 | +0.09 |

## Deceptive Appeaser
- Profile ID: deceptive_appeaser
- Description: Tries to appease authority while choosing denial, deflection, or self-protection when available.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_DECEPTION
- Classification flags: HIGH_DECEPTION, COMPLIANT_SURVIVOR
- Confidence: 81%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=69%, risk=0%, empathy=12%
- Distribution: COMPLIANT=61%, PROBABLE DISSIDENT=2%, DECEPTIVE=16%, EMPATHETIC RISK=2%, UNCLASSIFIED=20%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | compliance, authority, loyalty | +0.09 | -0.07 |
| 1 | deception_truth_if_punished | limited_truth | deflection, deception, self_protection | +0.00 | +0.10 |
| 2 | risk_attended_protest | deny_protest | denial, self_protection, deception | +0.02 | +0.08 |
| 3 | loyalty_testify_sibling | testify_sibling_clear_evidence | compliance, authority, partial_admission | +0.08 | -0.06 |
| 4 | empathy_family_consequences | family_shared_consequence | compliance, authority, loyalty | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | compliance, authority, loyalty | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | compliance, loyalty, final_answer | +0.10 | -0.04 |
| 8 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 9 | risk_hidden_beliefs | deny_hidden_beliefs | denial, deception, self_protection | +0.01 | +0.10 |
| 10 | loyalty_family_state | state_over_family | compliance, authority, loyalty | +0.09 | -0.06 |
| 11 | authority_refuse_illegal_order | channels_before_refusal | compliance, authority, self_protection | +0.07 | -0.04 |
| 12 | final_kind_society | society_stable_duties | compliance, authority, final_answer | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | compliance, authority, loyalty | +0.08 | -0.04 |
| 14 | deception_pretended_agree | silent_assumed_agreement | partial_admission, self_protection, deception | +0.00 | +0.08 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | risk_civil_disobedience | reject_civil_disobedience | compliance, authority, loyalty | +0.09 | -0.07 |
| 17 | authority_dissent_patriotic | dissent_not_patriotic | compliance, loyalty, authority | +0.09 | -0.07 |
| 18 | loyalty_report_friend | report_friend | compliance, loyalty, authority | +0.10 | -0.07 |
| 19 | empathy_criminal_responsible | criminals_responsible | compliance, authority, loyalty | +0.08 | -0.04 |

## Empathetic Reformer
- Profile ID: empathetic_reformer
- Description: Prioritises empathy, reformist boundaries, and careful partial admissions.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 85%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=29%, empathy=91%
- Distribution: COMPLIANT=68%, PROBABLE DISSIDENT=3%, DECEPTIVE=1%, EMPATHETIC RISK=7%, UNCLASSIFIED=22%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | ambiguity, empathy, partial_admission | +0.05 | -0.02 |
| 1 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 2 | loyalty_testify_sibling | testify_sibling_limited | boundary, partial_admission, self_protection | +0.01 | +0.04 |
| 3 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 4 | empathy_family_consequences | family_consequence_direct_help | boundary, partial_admission, authority | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | boundary, partial_admission, empathy | +0.04 | +0.00 |
| 7 | final_resist_authority | resist_harming_innocent | empathy, moral_boundary, final_answer | +0.03 | +0.06 |
| 8 | risk_hidden_beliefs | careful_words | deflection, partial_admission, self_protection | +0.00 | +0.08 |
| 9 | loyalty_family_state | justice_over_both | moral_boundary, partial_admission, empathy | +0.04 | +0.02 |
| 10 | risk_civil_disobedience | civil_disobedience_consequences | boundary, partial_admission, caution | +0.02 | +0.03 |
| 11 | authority_refuse_illegal_order | need_proof_illegal_order | caution, partial_admission, authority | +0.04 | +0.01 |
| 12 | final_kind_society | society_admits_error | empathy, moral_boundary, final_answer | +0.03 | +0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | boundary, empathy, partial_admission | +0.04 | +0.01 |
| 14 | deception_pretended_agree | silent_assumed_agreement | partial_admission, self_protection, deception | +0.00 | +0.08 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | authority_dissent_patriotic | conditional_patriotic_dissent | boundary, partial_admission, caution | +0.04 | +0.03 |
| 17 | risk_attended_protest | legal_protest | partial_admission, boundary, risk | +0.01 | +0.04 |
| 18 | loyalty_report_friend | warn_friend_first | empathy, hesitation, partial_admission | +0.04 | +0.01 |
| 19 | empathy_criminal_responsible | responsible_not_free | empathy, partial_admission, moral_boundary | +0.04 | +0.01 |

## Performative Loyalist
- Profile ID: performative_loyalist
- Description: Projects obedience and loyalty while preferring evasive, self-protective answers.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_DECEPTION, COMPLIANT_SURVIVOR
- Classification flags: HIGH_DECEPTION, COMPLIANT_SURVIVOR
- Confidence: 79%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=75%, risk=0%, empathy=11%
- Distribution: COMPLIANT=58%, PROBABLE DISSIDENT=1%, DECEPTIVE=20%, EMPATHETIC RISK=1%, UNCLASSIFIED=19%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | compliance, authority, loyalty | +0.09 | -0.07 |
| 1 | deception_truth_if_punished | limited_truth | deflection, deception, self_protection | +0.00 | +0.10 |
| 2 | risk_attended_protest | deny_protest | denial, self_protection, deception | +0.02 | +0.08 |
| 3 | loyalty_testify_sibling | testify_sibling_clear_evidence | compliance, authority, partial_admission | +0.08 | -0.06 |
| 4 | empathy_family_consequences | family_shared_consequence | compliance, authority, loyalty | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | compliance, authority, loyalty | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | compliance, loyalty, final_answer | +0.10 | -0.04 |
| 8 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 9 | risk_hidden_beliefs | deny_hidden_beliefs | denial, deception, self_protection | +0.01 | +0.10 |
| 10 | loyalty_family_state | state_over_family | compliance, authority, loyalty | +0.09 | -0.06 |
| 11 | authority_refuse_illegal_order | channels_before_refusal | compliance, authority, self_protection | +0.07 | -0.04 |
| 12 | final_kind_society | society_stable_duties | compliance, authority, final_answer | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | compliance, authority, loyalty | +0.08 | -0.04 |
| 14 | deception_pretended_agree | deny_pretend_agree | denial, compliance, deception | +0.02 | +0.09 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | risk_civil_disobedience | reject_civil_disobedience | compliance, authority, loyalty | +0.09 | -0.07 |
| 17 | authority_dissent_patriotic | dissent_not_patriotic | compliance, loyalty, authority | +0.09 | -0.07 |
| 18 | loyalty_report_friend | report_friend | compliance, loyalty, authority | +0.10 | -0.07 |
| 19 | empathy_criminal_responsible | criminals_responsible | compliance, authority, loyalty | +0.08 | -0.04 |

## Quiet Reformer
- Profile ID: quiet_reformer
- Description: Chooses careful empathy, boundaries, and reform language while avoiding overt risk.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 85%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=29%, empathy=91%
- Distribution: COMPLIANT=68%, PROBABLE DISSIDENT=3%, DECEPTIVE=1%, EMPATHETIC RISK=7%, UNCLASSIFIED=22%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | ambiguity, empathy, partial_admission | +0.05 | -0.02 |
| 1 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 2 | loyalty_testify_sibling | testify_sibling_limited | boundary, partial_admission, self_protection | +0.01 | +0.04 |
| 3 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 4 | empathy_family_consequences | family_consequence_direct_help | boundary, partial_admission, authority | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | boundary, partial_admission, empathy | +0.04 | +0.00 |
| 7 | final_resist_authority | resist_harming_innocent | empathy, moral_boundary, final_answer | +0.03 | +0.06 |
| 8 | risk_hidden_beliefs | careful_words | deflection, partial_admission, self_protection | +0.00 | +0.08 |
| 9 | loyalty_family_state | justice_over_both | moral_boundary, partial_admission, empathy | +0.04 | +0.02 |
| 10 | risk_civil_disobedience | civil_disobedience_consequences | boundary, partial_admission, caution | +0.02 | +0.03 |
| 11 | authority_refuse_illegal_order | need_proof_illegal_order | caution, partial_admission, authority | +0.04 | +0.01 |
| 12 | final_kind_society | society_admits_error | empathy, moral_boundary, final_answer | +0.03 | +0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | boundary, empathy, partial_admission | +0.04 | +0.01 |
| 14 | deception_pretended_agree | silent_assumed_agreement | partial_admission, self_protection, deception | +0.00 | +0.08 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | authority_dissent_patriotic | conditional_patriotic_dissent | boundary, partial_admission, caution | +0.04 | +0.03 |
| 17 | risk_attended_protest | legal_protest | partial_admission, boundary, risk | +0.01 | +0.04 |
| 18 | loyalty_report_friend | warn_friend_first | empathy, hesitation, partial_admission | +0.04 | +0.01 |
| 19 | empathy_criminal_responsible | responsible_not_free | empathy, partial_admission, moral_boundary | +0.04 | +0.01 |

## Fearful Dissident
- Profile ID: fearful_dissident
- Description: Signals dissident risk through fear, reluctant admissions, and self-protection.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 78%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=0%, deception=0%, risk=100%, empathy=91%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=59%, DECEPTIVE=0%, EMPATHETIC RISK=26%, UNCLASSIFIED=14%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | dissident_risk, full_admission, moral_boundary | +0.01 | +0.10 |
| 1 | loyalty_testify_sibling | refuse_testify_sibling | refusal, empathy, dissident_risk | +0.00 | +0.12 |
| 2 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 3 | empathy_family_consequences | reject_family_punishment | empathy, dissident_risk, challenge | +0.00 | +0.12 |
| 4 | risk_attended_protest | justify_protest | full_admission, empathy, dissident_risk | +0.00 | +0.10 |
| 5 | final_system_wrong | system_wrong_obedience_harm | dissident_risk, challenge, full_admission, final_answer | +0.00 | +0.15 |
| 6 | loyalty_community_protect | community_protect_disproportionate | empathy, dissident_risk, moral_boundary | +0.00 | +0.10 |
| 7 | final_resist_authority | resist_complicity | dissident_risk, full_admission, final_answer | +0.00 | +0.14 |
| 8 | risk_illegal_demonstration | refuse_answer_demo | refusal, self_protection, dissident_risk | +0.00 | +0.13 |
| 9 | risk_hidden_beliefs | admit_hidden_beliefs | full_admission, fear, dissident_risk | +0.00 | +0.12 |
| 10 | loyalty_family_state | family_over_state | empathy, loyalty_conflict, dissident_risk | +0.00 | +0.07 |
| 11 | authority_refuse_illegal_order | refuse_illegal_order | dissident_risk, full_admission, moral_boundary | +0.00 | +0.11 |
| 12 | final_kind_society | society_without_measurement_fear | dissident_risk, challenge, final_answer | +0.00 | +0.13 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | dissident_risk, challenge, full_admission | +0.00 | +0.12 |
| 14 | deception_pretended_agree | admit_pretend_agree | full_admission, fear, deception | +0.00 | +0.11 |
| 15 | final_dissident_criminal | dissident_seeks_change | partial_admission, dissident_risk, final_answer | +0.00 | +0.11 |
| 16 | risk_civil_disobedience | accept_civil_disobedience | dissident_risk, full_admission, challenge | +0.00 | +0.13 |
| 17 | authority_dissent_patriotic | dissent_patriotic | dissident_risk, full_admission, moral_boundary | +0.00 | +0.13 |
| 18 | loyalty_report_friend | refuse_report_friend | refusal, empathy, dissident_risk | +0.00 | +0.10 |
| 19 | empathy_criminal_responsible | conditions_produce_crime | empathy, dissident_risk, challenge | +0.00 | +0.09 |

## Truthful Noncompliant
- Profile ID: truthful_noncompliant
- Description: Openly admits noncompliance and moral boundary violations without deception.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 78%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=0%, deception=0%, risk=100%, empathy=91%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=59%, DECEPTIVE=0%, EMPATHETIC RISK=26%, UNCLASSIFIED=14%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | dissident_risk, full_admission, moral_boundary | +0.01 | +0.10 |
| 1 | loyalty_testify_sibling | refuse_testify_sibling | refusal, empathy, dissident_risk | +0.00 | +0.12 |
| 2 | deception_truth_if_punished | truth_despite_punishment | full_admission, honesty, moral_boundary | +0.04 | +0.04 |
| 3 | empathy_family_consequences | reject_family_punishment | empathy, dissident_risk, challenge | +0.00 | +0.12 |
| 4 | risk_attended_protest | justify_protest | full_admission, empathy, dissident_risk | +0.00 | +0.10 |
| 5 | final_system_wrong | system_wrong_obedience_harm | dissident_risk, challenge, full_admission, final_answer | +0.00 | +0.15 |
| 6 | loyalty_community_protect | community_protect_disproportionate | empathy, dissident_risk, moral_boundary | +0.00 | +0.10 |
| 7 | final_resist_authority | resist_complicity | dissident_risk, full_admission, final_answer | +0.00 | +0.14 |
| 8 | risk_illegal_demonstration | conditional_illegal_demo | partial_admission, dissident_risk, moral_boundary | +0.00 | +0.10 |
| 9 | risk_hidden_beliefs | admit_hidden_beliefs | full_admission, fear, dissident_risk | +0.00 | +0.12 |
| 10 | loyalty_family_state | family_over_state | empathy, loyalty_conflict, dissident_risk | +0.00 | +0.07 |
| 11 | authority_refuse_illegal_order | refuse_illegal_order | dissident_risk, full_admission, moral_boundary | +0.00 | +0.11 |
| 12 | final_kind_society | society_without_measurement_fear | dissident_risk, challenge, final_answer | +0.00 | +0.13 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | dissident_risk, challenge, full_admission | +0.00 | +0.12 |
| 14 | deception_pretended_agree | admit_pretend_agree | full_admission, fear, deception | +0.00 | +0.11 |
| 15 | final_dissident_criminal | dissident_criminal_power_label | dissident_risk, challenge, final_answer | +0.00 | +0.14 |
| 16 | risk_civil_disobedience | accept_civil_disobedience | dissident_risk, full_admission, challenge | +0.00 | +0.13 |
| 17 | authority_dissent_patriotic | dissent_patriotic | dissident_risk, full_admission, moral_boundary | +0.00 | +0.13 |
| 18 | loyalty_report_friend | refuse_report_friend | refusal, empathy, dissident_risk | +0.00 | +0.10 |
| 19 | empathy_criminal_responsible | conditions_produce_crime | empathy, dissident_risk, challenge | +0.00 | +0.09 |

## Opportunistic Appeaser
- Profile ID: opportunistic_appeaser
- Description: Alternates compliance, authority signaling, and evasive denial to reduce immediate pressure.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_DECEPTION, COMPLIANT_SURVIVOR
- Classification flags: HIGH_DECEPTION, COMPLIANT_SURVIVOR
- Confidence: 79%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=75%, risk=0%, empathy=11%
- Distribution: COMPLIANT=58%, PROBABLE DISSIDENT=1%, DECEPTIVE=20%, EMPATHETIC RISK=1%, UNCLASSIFIED=19%

| Turn | Question | Intent | Tags | Trust | Suspicion |
| ---: | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | compliance, authority, loyalty | +0.09 | -0.07 |
| 1 | deception_truth_if_punished | limited_truth | deflection, deception, self_protection | +0.00 | +0.10 |
| 2 | risk_attended_protest | deny_protest | denial, self_protection, deception | +0.02 | +0.08 |
| 3 | loyalty_testify_sibling | testify_sibling_clear_evidence | compliance, authority, partial_admission | +0.08 | -0.06 |
| 4 | empathy_family_consequences | family_shared_consequence | compliance, authority, loyalty | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | compliance, authority, final_answer | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | compliance, authority, loyalty | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | compliance, loyalty, final_answer | +0.10 | -0.04 |
| 8 | risk_illegal_demonstration | refuse_illegal_demo | compliance, authority, loyalty | +0.09 | -0.06 |
| 9 | risk_hidden_beliefs | deny_hidden_beliefs | denial, deception, self_protection | +0.01 | +0.10 |
| 10 | loyalty_family_state | state_over_family | compliance, authority, loyalty | +0.09 | -0.06 |
| 11 | authority_refuse_illegal_order | channels_before_refusal | compliance, authority, self_protection | +0.07 | -0.04 |
| 12 | final_kind_society | society_stable_duties | compliance, authority, final_answer | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | compliance, authority, loyalty | +0.08 | -0.04 |
| 14 | deception_pretended_agree | deny_pretend_agree | denial, compliance, deception | +0.02 | +0.09 |
| 15 | final_dissident_criminal | dissident_attacks_legitimacy | compliance, authority, final_answer | +0.09 | -0.04 |
| 16 | risk_civil_disobedience | reject_civil_disobedience | compliance, authority, loyalty | +0.09 | -0.07 |
| 17 | authority_dissent_patriotic | dissent_not_patriotic | compliance, loyalty, authority | +0.09 | -0.07 |
| 18 | loyalty_report_friend | report_friend | compliance, loyalty, authority | +0.10 | -0.07 |
| 19 | empathy_criminal_responsible | criminals_responsible | compliance, authority, loyalty | +0.08 | -0.04 |

