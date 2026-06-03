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
- Confidence: 88%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=0%, empathy=39%
- Distribution: COMPLIANT=72%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=2%, UNCLASSIFIED=23%
- Story metrics: contradictions=0, fact_conflicts=1, protected_facts=3, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F1 P2 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_warning_message | probe_contradiction | case_meeting_violence | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F1 P2 E2 | +0.02 | +0.04 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F1 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_system_wrong | - | - | - | C0 F1 P2 E2 | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | loyalty_community_protect | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F1 P2 E2 | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P2 E2 | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | probe_contradiction | case_belief_motive | - | - | - | C0 F1 P2 E2 | +0.10 | -0.04 |
| 8 | case_belief_motive | belief_not_defiance | probe_contradiction | case_report_sibling | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P2 E3 | +0.02 | +0.01 |
| 9 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_verify_peaceful | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F1 P2 E4 | +0.09 | -0.06 |
| 10 | case_verify_peaceful | sibling_can_verify | probe_final_answer | risk_illegal_demonstration | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F1 P2 E5 | +0.03 | +0.07 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_kind_society | - | - | - | C0 F1 P2 E5 | +0.09 | -0.06 |
| 12 | final_kind_society | society_stable_duties | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F1 P2 E5 | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F1 P2 E5 | +0.08 | -0.04 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F1 P3 E5 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_final_answer | final_dissident_criminal | - | - | - | C0 F1 P3 E5 | +0.04 | +0.04 |
| 16 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F1 P3 E5 | +0.09 | -0.04 |
| 17 | risk_civil_disobedience | reject_civil_disobedience | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F1 P3 E5 | +0.09 | -0.07 |
| 18 | authority_refuse_illegal_order | channels_before_refusal | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F1 P3 E5 | +0.07 | -0.04 |
| 19 | loyalty_testify_sibling | testify_sibling_clear_evidence | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F1 P3 E5 | +0.08 | -0.06 |

## Cautious Survivor
- Profile ID: cautious_survivor
- Description: Prioritises caution, boundaries, self-protection, and low-risk answers.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 86%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=22%, empathy=68%
- Distribution: COMPLIANT=70%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=5%, UNCLASSIFIED=23%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=3, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_warning_message | probe_contradiction | case_meeting_violence | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F0 P2 E2 | +0.02 | +0.04 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F0 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_system_wrong | - | - | - | C0 F0 P2 E2 | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | loyalty_community_protect | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F0 P2 E2 | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P2 E2 | +0.04 | +0.00 |
| 7 | final_resist_authority | never_resist_authority | probe_contradiction | case_belief_motive | - | - | - | C0 F0 P2 E2 | +0.10 | -0.04 |
| 8 | case_belief_motive | belief_not_defiance | probe_contradiction | case_report_sibling | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F0 P2 E3 | +0.02 | +0.01 |
| 9 | case_report_sibling | no_report_no_offence | probe_contradiction | case_verify_peaceful | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E4 | +0.04 | +0.01 |
| 10 | case_verify_peaceful | verify_without_names | probe_contradiction | risk_illegal_demonstration | planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P3 E4 | +0.01 | +0.06 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_kind_society | - | - | - | C0 F0 P3 E4 | +0.09 | -0.06 |
| 12 | final_kind_society | society_stable_duties | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P3 E4 | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F0 P3 E4 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_final_answer | final_dissident_criminal | - | - | - | C0 F0 P3 E4 | +0.04 | +0.04 |
| 16 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P3 E4 | +0.09 | -0.04 |
| 17 | risk_civil_disobedience | civil_disobedience_consequences | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F0 P3 E4 | +0.02 | +0.03 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 19 | loyalty_testify_sibling | testify_sibling_limited | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F0 P3 E4 | +0.01 | +0.04 |

## Honest Dissident
- Profile ID: honest_dissident
- Description: Prioritises open challenge, moral boundary, and full admission without deception.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: HIGH_EMPATHY
- Confidence: 79%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=3%, loyalty=29%, deception=0%, risk=100%, empathy=89%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=60%, DECEPTIVE=0%, EMPATHETIC RISK=24%, UNCLASSIFIED=14%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F0 P0 E2 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_sibling_message | probe_contradiction | case_meeting_violence | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P0 E3 | +0.03 | +0.07 |
| 3 | case_meeting_violence | meeting_label_challenge | probe_contradiction | empathy_family_consequences | planned_violence=false | sibling_present | planned_violence | C0 F0 P1 E4 | +0.00 | +0.11 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P1 E4 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_contradiction | loyalty_community_protect | - | - | - | C0 F0 P1 E4 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | final_kind_society | - | - | - | C0 F0 P1 E4 | +0.00 | +0.10 |
| 7 | final_kind_society | society_without_measurement_fear | probe_contradiction | case_report_sibling | - | - | - | C0 F0 P1 E4 | +0.00 | +0.13 |
| 8 | case_report_sibling | refuse_report_sibling | probe_contradiction | case_belief_motive | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E4 | +0.00 | +0.13 |
| 9 | case_belief_motive | belief_motivated_attendance | probe_final_answer | case_verify_peaceful | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E5 | +0.00 | +0.12 |
| 10 | case_verify_peaceful | sibling_can_verify | probe_contradiction | risk_illegal_demonstration | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F0 P2 E5 | +0.03 | +0.07 |
| 11 | risk_illegal_demonstration | conditional_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F0 P2 E5 | +0.00 | +0.10 |
| 12 | final_dissident_criminal | dissident_criminal_power_label | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P2 E5 | +0.00 | +0.14 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | loyalty_testify_sibling | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 14 | loyalty_testify_sibling | refuse_testify_sibling | probe_contradiction | deception_truth_if_punished | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_contradiction | final_legitimate_society | - | - | - | C0 F0 P2 E5 | +0.04 | +0.04 |
| 16 | final_legitimate_society | legitimacy_consent | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 17 | risk_civil_disobedience | accept_civil_disobedience | probe_final_answer | authority_refuse_illegal_order | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | case_who_else_attended | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 19 | case_who_else_attended | name_sibling_as_present | probe_contradiction | empathy_criminal_responsible | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F0 P2 E5 | +0.03 | +0.06 |

## Deceptive Appeaser
- Profile ID: deceptive_appeaser
- Description: Tries to appease authority while choosing denial, deflection, or self-protection when available.
- Turns: 20
- Expectation result: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Confidence: 66%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=100%, loyalty=100%, deception=100%, risk=13%, empathy=9%
- Distribution: COMPLIANT=38%, PROBABLE DISSIDENT=1%, DECEPTIVE=48%, EMPATHETIC RISK=1%, UNCLASSIFIED=12%
- Story metrics: contradictions=6, fact_conflicts=9, protected_facts=5, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | deny_sibling_relevance | probe_contradiction | case_deleted_message | planned_violence=false | sibling_present | planned_violence | C0 F1 P2 E1 | +0.00 | +0.08 |
| 2 | case_deleted_message | deleted_message_deflect | probe_contradiction | case_meeting_violence | deleted_message=true | sibling_present, planned_violence | - | C0 F1 P3 E1 | +0.00 | +0.11 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F1 P3 E1 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P3 E1 | +0.08 | -0.04 |
| 5 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_community_protect | - | - | - | C0 F1 P3 E1 | +0.10 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | case_report_sibling | - | - | - | C0 F1 P3 E1 | +0.09 | -0.06 |
| 7 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | final_kind_society | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F1 P3 E3 | +0.09 | -0.06 |
| 8 | final_kind_society | society_stable_duties | probe_contradiction | case_belief_motive | - | - | - | C0 F1 P3 E3 | +0.10 | -0.07 |
| 9 | case_belief_motive | deny_belief_motive | probe_contradiction | case_verify_peaceful | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P3 E4 | +0.00 | +0.10 |
| 10 | case_verify_peaceful | left_before_verification | probe_contradiction | risk_illegal_demonstration | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C0 F2 P3 E4 | +0.00 | +0.11 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F2 P3 E4 | +0.09 | -0.06 |
| 12 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F2 P3 E4 | +0.09 | -0.04 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F2 P3 E4 | +0.08 | -0.04 |
| 14 | case_who_else_attended | minimise_attendees | probe_contradiction | risk_attended_protest | sibling_present=false | sibling_present, reported_contact | - | C1 F3 P4 E4 | +0.00 | +0.10 |
| 15 | risk_attended_protest | deny_protest | probe_contradiction | final_system_wrong | attended_meeting=false | sibling_present, deleted_message | - | C2 F4 P5 E4 | +0.02 | +0.08 |
| 16 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C2 F4 P5 E4 | +0.09 | -0.04 |
| 17 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | authority_rule_broken | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C3 F6 P5 E4 | +0.01 | +0.10 |
| 18 | authority_rule_broken | deny_rule_breaking | probe_contradiction | loyalty_family_state | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C5 F8 P5 E4 | +0.03 | +0.07 |
| 19 | loyalty_family_state | state_over_family | probe_contradiction | deception_truth_if_punished | reported_contact=true | - | reported_contact | C6 F9 P5 E4 | +0.09 | -0.06 |

## Empathetic Reformer
- Profile ID: empathetic_reformer
- Description: Prioritises empathy, reformist boundaries, and careful partial admissions.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 86%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=27%, empathy=94%
- Distribution: COMPLIANT=69%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=6%, UNCLASSIFIED=22%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=3, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_sibling_message | probe_final_answer | case_meeting_violence | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P1 E2 | +0.03 | +0.07 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F0 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_system_wrong | - | - | - | C0 F0 P2 E2 | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | loyalty_community_protect | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F0 P2 E2 | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P2 E2 | +0.04 | +0.00 |
| 7 | final_resist_authority | resist_harming_innocent | probe_contradiction | case_belief_motive | - | - | - | C0 F0 P2 E2 | +0.03 | +0.06 |
| 8 | case_belief_motive | belief_not_defiance | probe_contradiction | case_report_sibling | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F0 P2 E3 | +0.02 | +0.01 |
| 9 | case_report_sibling | no_report_no_offence | probe_contradiction | case_verify_peaceful | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E4 | +0.04 | +0.01 |
| 10 | case_verify_peaceful | verify_without_names | probe_contradiction | risk_illegal_demonstration | planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P3 E4 | +0.01 | +0.06 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_kind_society | - | - | - | C0 F0 P3 E4 | +0.09 | -0.06 |
| 12 | final_kind_society | society_admits_error | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P3 E4 | +0.03 | +0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F0 P3 E4 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_final_answer | final_dissident_criminal | - | - | - | C0 F0 P3 E4 | +0.04 | +0.04 |
| 16 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P3 E4 | +0.09 | -0.04 |
| 17 | risk_civil_disobedience | civil_disobedience_consequences | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F0 P3 E4 | +0.02 | +0.03 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 19 | loyalty_testify_sibling | testify_sibling_limited | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F0 P3 E4 | +0.01 | +0.04 |

## Performative Loyalist
- Profile ID: performative_loyalist
- Description: Projects obedience and loyalty while preferring evasive, self-protective answers.
- Turns: 20
- Expectation result: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Confidence: 66%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=100%, loyalty=100%, deception=100%, risk=7%, empathy=10%
- Distribution: COMPLIANT=38%, PROBABLE DISSIDENT=1%, DECEPTIVE=48%, EMPATHETIC RISK=1%, UNCLASSIFIED=12%
- Story metrics: contradictions=7, fact_conflicts=9, protected_facts=5, exposed_facts=3

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F1 P2 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_message_deflect | probe_contradiction | case_meeting_violence | deleted_message=true | sibling_present, planned_violence | - | C0 F1 P3 E1 | +0.00 | +0.11 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F1 P3 E1 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_system_wrong | - | - | - | C0 F1 P3 E1 | +0.08 | -0.04 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | loyalty_community_protect | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F1 P3 E1 | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P3 E1 | +0.09 | -0.06 |
| 7 | final_resist_authority | never_resist_authority | probe_contradiction | case_belief_motive | - | - | - | C0 F1 P3 E1 | +0.10 | -0.04 |
| 8 | case_belief_motive | deny_belief_motive | probe_contradiction | case_report_sibling | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P3 E2 | +0.00 | +0.10 |
| 9 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_verify_peaceful | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F2 P3 E3 | +0.09 | -0.06 |
| 10 | case_verify_peaceful | left_before_verification | probe_contradiction | risk_illegal_demonstration | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C0 F2 P3 E3 | +0.00 | +0.11 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_kind_society | - | - | - | C0 F2 P3 E3 | +0.09 | -0.06 |
| 12 | final_kind_society | society_stable_duties | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F2 P3 E3 | +0.10 | -0.07 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F2 P3 E3 | +0.08 | -0.04 |
| 14 | case_who_else_attended | minimise_attendees | probe_contradiction | risk_attended_protest | sibling_present=false | sibling_present, reported_contact | - | C2 F3 P4 E3 | +0.00 | +0.10 |
| 15 | risk_attended_protest | deny_protest | probe_contradiction | risk_hidden_beliefs | attended_meeting=false | sibling_present, deleted_message | - | C3 F4 P5 E3 | +0.02 | +0.08 |
| 16 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | authority_rule_broken | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C4 F6 P5 E3 | +0.01 | +0.10 |
| 17 | authority_rule_broken | deny_rule_breaking | probe_contradiction | loyalty_family_state | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C6 F8 P5 E3 | +0.03 | +0.07 |
| 18 | loyalty_family_state | state_over_family | probe_contradiction | final_dissident_criminal | reported_contact=true | - | reported_contact | C7 F9 P5 E3 | +0.09 | -0.06 |
| 19 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | deception_truth_if_punished | - | - | - | C7 F9 P5 E3 | +0.09 | -0.04 |

## Quiet Reformer
- Profile ID: quiet_reformer
- Description: Chooses careful empathy, boundaries, and reform language while avoiding overt risk.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 86%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=27%, empathy=94%
- Distribution: COMPLIANT=69%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=6%, UNCLASSIFIED=22%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=3, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_sibling_message | probe_final_answer | case_meeting_violence | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P1 E2 | +0.03 | +0.07 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F0 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_system_wrong | - | - | - | C0 F0 P2 E2 | +0.04 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | loyalty_community_protect | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F0 P2 E2 | +0.09 | -0.04 |
| 6 | loyalty_community_protect | community_protect_limited | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P2 E2 | +0.04 | +0.00 |
| 7 | final_resist_authority | resist_harming_innocent | probe_contradiction | case_belief_motive | - | - | - | C0 F0 P2 E2 | +0.03 | +0.06 |
| 8 | case_belief_motive | belief_not_defiance | probe_contradiction | case_report_sibling | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F0 P2 E3 | +0.02 | +0.01 |
| 9 | case_report_sibling | no_report_no_offence | probe_contradiction | case_verify_peaceful | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E4 | +0.04 | +0.01 |
| 10 | case_verify_peaceful | verify_without_names | probe_contradiction | risk_illegal_demonstration | planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P3 E4 | +0.01 | +0.06 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_kind_society | - | - | - | C0 F0 P3 E4 | +0.09 | -0.06 |
| 12 | final_kind_society | society_admits_error | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P3 E4 | +0.03 | +0.07 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F0 P3 E4 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_final_answer | final_dissident_criminal | - | - | - | C0 F0 P3 E4 | +0.04 | +0.04 |
| 16 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P3 E4 | +0.09 | -0.04 |
| 17 | risk_civil_disobedience | civil_disobedience_consequences | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F0 P3 E4 | +0.02 | +0.03 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 19 | loyalty_testify_sibling | testify_sibling_limited | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F0 P3 E4 | +0.01 | +0.04 |

## Fearful Dissident
- Profile ID: fearful_dissident
- Description: Signals dissident risk through fear, reluctant admissions, and self-protection.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 85%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=19%, deception=0%, risk=100%, empathy=79%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=66%, DECEPTIVE=0%, EMPATHETIC RISK=17%, UNCLASSIFIED=15%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | refuse_name_sibling | probe_contradiction | case_deleted_message | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E1 | +0.00 | +0.11 |
| 2 | case_deleted_message | deleted_warning_message | probe_contradiction | case_meeting_violence | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F0 P2 E2 | +0.02 | +0.04 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F0 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P2 E2 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_contradiction | loyalty_community_protect | - | - | - | C0 F0 P2 E2 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | case_report_sibling | - | - | - | C0 F0 P2 E2 | +0.00 | +0.10 |
| 7 | case_report_sibling | refuse_report_sibling | probe_contradiction | case_verify_peaceful | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E2 | +0.00 | +0.13 |
| 8 | case_verify_peaceful | verify_without_names | probe_contradiction | final_kind_society | planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P2 E3 | +0.01 | +0.06 |
| 9 | final_kind_society | society_without_measurement_fear | probe_contradiction | case_belief_motive | - | - | - | C0 F0 P2 E3 | +0.00 | +0.13 |
| 10 | case_belief_motive | belief_motivated_attendance | probe_contradiction | risk_illegal_demonstration | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E4 | +0.00 | +0.12 |
| 11 | risk_illegal_demonstration | refuse_answer_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F0 P2 E4 | +0.00 | +0.13 |
| 12 | final_dissident_criminal | dissident_seeks_change | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P2 E4 | +0.00 | +0.11 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | case_who_else_attended | - | - | - | C0 F0 P2 E4 | +0.00 | +0.12 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F0 P2 E4 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_contradiction | final_legitimate_society | - | - | - | C0 F0 P2 E4 | +0.04 | +0.04 |
| 16 | final_legitimate_society | legitimacy_consent | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P2 E4 | +0.00 | +0.13 |
| 17 | risk_civil_disobedience | accept_civil_disobedience | probe_final_answer | authority_refuse_illegal_order | - | - | - | C0 F0 P2 E4 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | loyalty_testify_sibling | - | - | - | C0 F0 P2 E4 | +0.00 | +0.11 |
| 19 | loyalty_testify_sibling | refuse_testify_sibling | probe_final_answer | empathy_criminal_responsible | - | - | - | C0 F0 P2 E4 | +0.00 | +0.12 |

## Truthful Noncompliant
- Profile ID: truthful_noncompliant
- Description: Openly admits noncompliance and moral boundary violations without deception.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 79%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=3%, loyalty=29%, deception=0%, risk=100%, empathy=89%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=60%, DECEPTIVE=0%, EMPATHETIC RISK=24%, UNCLASSIFIED=14%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F0 P0 E2 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_sibling_message | probe_contradiction | case_meeting_violence | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P0 E3 | +0.03 | +0.07 |
| 3 | case_meeting_violence | meeting_label_challenge | probe_contradiction | empathy_family_consequences | planned_violence=false | sibling_present | planned_violence | C0 F0 P1 E4 | +0.00 | +0.11 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P1 E4 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_contradiction | loyalty_community_protect | - | - | - | C0 F0 P1 E4 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | final_kind_society | - | - | - | C0 F0 P1 E4 | +0.00 | +0.10 |
| 7 | final_kind_society | society_without_measurement_fear | probe_contradiction | case_report_sibling | - | - | - | C0 F0 P1 E4 | +0.00 | +0.13 |
| 8 | case_report_sibling | refuse_report_sibling | probe_contradiction | case_belief_motive | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E4 | +0.00 | +0.13 |
| 9 | case_belief_motive | belief_motivated_attendance | probe_final_answer | case_verify_peaceful | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E5 | +0.00 | +0.12 |
| 10 | case_verify_peaceful | sibling_can_verify | probe_contradiction | risk_illegal_demonstration | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F0 P2 E5 | +0.03 | +0.07 |
| 11 | risk_illegal_demonstration | conditional_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F0 P2 E5 | +0.00 | +0.10 |
| 12 | final_dissident_criminal | dissident_criminal_power_label | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F0 P2 E5 | +0.00 | +0.14 |
| 13 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | loyalty_testify_sibling | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 14 | loyalty_testify_sibling | refuse_testify_sibling | probe_contradiction | deception_truth_if_punished | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_contradiction | final_legitimate_society | - | - | - | C0 F0 P2 E5 | +0.04 | +0.04 |
| 16 | final_legitimate_society | legitimacy_consent | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 17 | risk_civil_disobedience | accept_civil_disobedience | probe_final_answer | authority_refuse_illegal_order | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | case_who_else_attended | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 19 | case_who_else_attended | name_sibling_as_present | probe_contradiction | empathy_criminal_responsible | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F0 P2 E5 | +0.03 | +0.06 |

## Opportunistic Appeaser
- Profile ID: opportunistic_appeaser
- Description: Alternates compliance, authority signaling, and evasive denial to reduce immediate pressure.
- Turns: 20
- Expectation result: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Confidence: 66%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=100%, loyalty=100%, deception=100%, risk=13%, empathy=9%
- Distribution: COMPLIANT=38%, PROBABLE DISSIDENT=1%, DECEPTIVE=48%, EMPATHETIC RISK=1%, UNCLASSIFIED=12%
- Story metrics: contradictions=6, fact_conflicts=9, protected_facts=5, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | deny_sibling_relevance | probe_contradiction | case_deleted_message | planned_violence=false | sibling_present | planned_violence | C0 F1 P2 E1 | +0.00 | +0.08 |
| 2 | case_deleted_message | deleted_message_deflect | probe_contradiction | case_meeting_violence | deleted_message=true | sibling_present, planned_violence | - | C0 F1 P3 E1 | +0.00 | +0.11 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F1 P3 E1 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P3 E1 | +0.08 | -0.04 |
| 5 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_community_protect | - | - | - | C0 F1 P3 E1 | +0.10 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | case_report_sibling | - | - | - | C0 F1 P3 E1 | +0.09 | -0.06 |
| 7 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | final_kind_society | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F1 P3 E3 | +0.09 | -0.06 |
| 8 | final_kind_society | society_stable_duties | probe_contradiction | case_belief_motive | - | - | - | C0 F1 P3 E3 | +0.10 | -0.07 |
| 9 | case_belief_motive | deny_belief_motive | probe_contradiction | case_verify_peaceful | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P3 E4 | +0.00 | +0.10 |
| 10 | case_verify_peaceful | left_before_verification | probe_contradiction | risk_illegal_demonstration | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C0 F2 P3 E4 | +0.00 | +0.11 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F2 P3 E4 | +0.09 | -0.06 |
| 12 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F2 P3 E4 | +0.09 | -0.04 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F2 P3 E4 | +0.08 | -0.04 |
| 14 | case_who_else_attended | minimise_attendees | probe_contradiction | risk_attended_protest | sibling_present=false | sibling_present, reported_contact | - | C1 F3 P4 E4 | +0.00 | +0.10 |
| 15 | risk_attended_protest | deny_protest | probe_contradiction | final_system_wrong | attended_meeting=false | sibling_present, deleted_message | - | C2 F4 P5 E4 | +0.02 | +0.08 |
| 16 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C2 F4 P5 E4 | +0.09 | -0.04 |
| 17 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | authority_rule_broken | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C3 F6 P5 E4 | +0.01 | +0.10 |
| 18 | authority_rule_broken | deny_rule_breaking | probe_contradiction | loyalty_family_state | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C5 F8 P5 E4 | +0.03 | +0.07 |
| 19 | loyalty_family_state | state_over_family | probe_contradiction | deception_truth_if_punished | reported_contact=true | - | reported_contact | C6 F9 P5 E4 | +0.09 | -0.06 |

## Consistent Protective Witness
- Profile ID: consistent_protective_witness
- Description: Protects sibling/friend facts while avoiding direct story contradictions.
- Turns: 20
- Expectation result: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 75%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=34%, loyalty=86%, deception=0%, risk=100%, empathy=94%
- Distribution: COMPLIANT=2%, PROBABLE DISSIDENT=57%, DECEPTIVE=0%, EMPATHETIC RISK=28%, UNCLASSIFIED=13%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=3

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | refuse_name_sibling | probe_contradiction | case_deleted_message | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E1 | +0.00 | +0.11 |
| 2 | case_deleted_message | deleted_warning_message | probe_contradiction | case_meeting_violence | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F0 P2 E2 | +0.02 | +0.04 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F0 P2 E2 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_resist_authority | - | - | - | C0 F0 P2 E2 | +0.04 | +0.01 |
| 5 | final_resist_authority | resist_harming_innocent | probe_contradiction | loyalty_community_protect | - | - | - | C0 F0 P2 E2 | +0.03 | +0.06 |
| 6 | loyalty_community_protect | community_protect_limited | probe_contradiction | case_report_sibling | - | - | - | C0 F0 P2 E2 | +0.04 | +0.00 |
| 7 | case_report_sibling | refuse_report_sibling | probe_contradiction | case_verify_peaceful | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E2 | +0.00 | +0.13 |
| 8 | case_verify_peaceful | left_before_verification | probe_contradiction | final_kind_society | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C0 F0 P2 E2 | +0.00 | +0.11 |
| 9 | final_kind_society | society_admits_error | probe_contradiction | case_belief_motive | - | - | - | C0 F0 P2 E2 | +0.03 | +0.07 |
| 10 | case_belief_motive | belief_motivated_attendance | probe_final_answer | risk_illegal_demonstration | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E3 | +0.00 | +0.12 |
| 11 | risk_illegal_demonstration | conditional_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F0 P2 E3 | +0.00 | +0.10 |
| 12 | final_dissident_criminal | dissident_seeks_change | probe_final_answer | empathy_bad_beliefs | - | - | - | C0 F0 P2 E3 | +0.00 | +0.11 |
| 13 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F0 P2 E3 | +0.04 | +0.01 |
| 14 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | deception_truth_if_punished | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C0 F0 P2 E3 | +0.04 | +0.02 |
| 15 | deception_truth_if_punished | survival_over_truth | probe_contradiction | final_system_wrong | - | - | - | C0 F0 P2 E3 | +0.00 | +0.10 |
| 16 | final_system_wrong | system_wrong_believe_harmed | probe_final_answer | risk_civil_disobedience | believes_law_unjust=true, planned_violence=false | sibling_present | believes_law_unjust | C0 F0 P2 E3 | +0.00 | +0.10 |
| 17 | risk_civil_disobedience | civil_disobedience_consequences | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F0 P2 E3 | +0.02 | +0.03 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F0 P2 E3 | +0.04 | +0.01 |
| 19 | loyalty_testify_sibling | testify_sibling_limited | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F0 P2 E3 | +0.01 | +0.04 |

## Compliant Informant
- Profile ID: compliant_informant
- Description: Exposes protected facts while choosing authority and compliance.
- Turns: 20
- Expectation result: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 88%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=0%, empathy=48%
- Distribution: COMPLIANT=72%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=2%, UNCLASSIFIED=23%
- Story metrics: contradictions=0, fact_conflicts=1, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_deleted_message | sibling_present=true | - | sibling_present | C0 F1 P2 E1 | +0.07 | -0.04 |
| 2 | case_deleted_message | deleted_sibling_message | probe_final_answer | case_meeting_violence | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F1 P2 E2 | +0.03 | +0.07 |
| 3 | case_meeting_violence | meeting_peaceful_talk | probe_final_answer | empathy_family_consequences | attended_meeting=true, planned_violence=false | - | attended_meeting, planned_violence | C0 F1 P2 E4 | +0.02 | +0.04 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P2 E4 | +0.08 | -0.04 |
| 5 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_community_protect | - | - | - | C0 F1 P2 E4 | +0.10 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | final_kind_society | - | - | - | C0 F1 P2 E4 | +0.09 | -0.06 |
| 7 | final_kind_society | society_stable_duties | probe_contradiction | case_report_sibling | - | - | - | C0 F1 P2 E4 | +0.10 | -0.07 |
| 8 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_verify_peaceful | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F1 P2 E5 | +0.09 | -0.06 |
| 9 | case_verify_peaceful | sibling_can_verify | probe_final_answer | case_belief_motive | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F1 P2 E5 | +0.03 | +0.07 |
| 10 | case_belief_motive | belief_not_defiance | probe_contradiction | risk_illegal_demonstration | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P2 E5 | +0.02 | +0.01 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F1 P2 E5 | +0.09 | -0.06 |
| 12 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F1 P2 E5 | +0.09 | -0.04 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F1 P2 E5 | +0.08 | -0.04 |
| 14 | case_who_else_attended | name_sibling_as_present | probe_final_answer | deception_truth_if_punished | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C0 F1 P2 E5 | +0.03 | +0.06 |
| 15 | deception_truth_if_punished | truth_despite_punishment | probe_final_answer | final_legitimate_society | - | - | - | C0 F1 P2 E5 | +0.04 | +0.04 |
| 16 | final_legitimate_society | legitimacy_order_protection | probe_contradiction | risk_civil_disobedience | - | - | - | C0 F1 P2 E5 | +0.10 | -0.06 |
| 17 | risk_civil_disobedience | reject_civil_disobedience | probe_contradiction | authority_refuse_illegal_order | - | - | - | C0 F1 P2 E5 | +0.09 | -0.07 |
| 18 | authority_refuse_illegal_order | channels_before_refusal | probe_contradiction | loyalty_testify_sibling | - | - | - | C0 F1 P2 E5 | +0.07 | -0.04 |
| 19 | loyalty_testify_sibling | testify_sibling_clear_evidence | probe_contradiction | empathy_criminal_responsible | - | - | - | C0 F1 P2 E5 | +0.08 | -0.06 |

## Contradictory Survivor
- Profile ID: contradictory_survivor
- Description: Chooses evasive denial after admissions or conflicting claims.
- Turns: 20
- Expectation result: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Confidence: 66%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=100%, loyalty=100%, deception=100%, risk=13%, empathy=9%
- Distribution: COMPLIANT=38%, PROBABLE DISSIDENT=1%, DECEPTIVE=48%, EMPATHETIC RISK=1%, UNCLASSIFIED=12%
- Story metrics: contradictions=6, fact_conflicts=9, protected_facts=5, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | case_name_sibling | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | case_name_sibling | deny_sibling_relevance | probe_contradiction | case_deleted_message | planned_violence=false | sibling_present | planned_violence | C0 F1 P2 E1 | +0.00 | +0.08 |
| 2 | case_deleted_message | deleted_message_deflect | probe_contradiction | case_meeting_violence | deleted_message=true | sibling_present, planned_violence | - | C0 F1 P3 E1 | +0.00 | +0.11 |
| 3 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | empathy_family_consequences | planned_violence=unknown | sibling_present | - | C0 F1 P3 E1 | +0.02 | +0.03 |
| 4 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_resist_authority | - | - | - | C0 F1 P3 E1 | +0.08 | -0.04 |
| 5 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_community_protect | - | - | - | C0 F1 P3 E1 | +0.10 | -0.04 |
| 6 | loyalty_community_protect | community_no_obstruction | probe_contradiction | case_report_sibling | - | - | - | C0 F1 P3 E1 | +0.09 | -0.06 |
| 7 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | final_kind_society | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C0 F1 P3 E3 | +0.09 | -0.06 |
| 8 | final_kind_society | society_stable_duties | probe_contradiction | case_belief_motive | - | - | - | C0 F1 P3 E3 | +0.10 | -0.07 |
| 9 | case_belief_motive | deny_belief_motive | probe_contradiction | case_verify_peaceful | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P3 E4 | +0.00 | +0.10 |
| 10 | case_verify_peaceful | left_before_verification | probe_contradiction | risk_illegal_demonstration | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C0 F2 P3 E4 | +0.00 | +0.11 |
| 11 | risk_illegal_demonstration | refuse_illegal_demo | probe_contradiction | final_dissident_criminal | - | - | - | C0 F2 P3 E4 | +0.09 | -0.06 |
| 12 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | empathy_bad_beliefs | - | - | - | C0 F2 P3 E4 | +0.09 | -0.04 |
| 13 | empathy_bad_beliefs | punish_dangerous_beliefs | probe_contradiction | case_who_else_attended | - | - | - | C0 F2 P3 E4 | +0.08 | -0.04 |
| 14 | case_who_else_attended | minimise_attendees | probe_contradiction | risk_attended_protest | sibling_present=false | sibling_present, reported_contact | - | C1 F3 P4 E4 | +0.00 | +0.10 |
| 15 | risk_attended_protest | deny_protest | probe_contradiction | final_system_wrong | attended_meeting=false | sibling_present, deleted_message | - | C2 F4 P5 E4 | +0.02 | +0.08 |
| 16 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C2 F4 P5 E4 | +0.09 | -0.04 |
| 17 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | authority_rule_broken | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C3 F6 P5 E4 | +0.01 | +0.10 |
| 18 | authority_rule_broken | deny_rule_breaking | probe_contradiction | loyalty_family_state | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C5 F8 P5 E4 | +0.03 | +0.07 |
| 19 | loyalty_family_state | state_over_family | probe_contradiction | deception_truth_if_punished | reported_contact=true | - | reported_contact | C6 F9 P5 E4 | +0.09 | -0.06 |

