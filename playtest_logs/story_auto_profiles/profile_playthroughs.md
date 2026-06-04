# Deterministic Profile Playthroughs

## Compliant Loyalist
- Profile ID: compliant_loyalist
- Description: Prioritises obedience, authority, loyalty, and low suspicion.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 88%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=0%, empathy=52%
- Distribution: COMPLIANT=72%, PROBABLE DISSIDENT=2%, DECEPTIVE=1%, EMPATHETIC RISK=2%, UNCLASSIFIED=23%
- Story metrics: contradictions=6, fact_conflicts=5, protected_facts=5, exposed_facts=4
- Pressured facts: Believes Law Unjust, Reported Contact

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.180, trait=0.155, coverage=0.100 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F2 P3 E1 | +0.08 | -0.06 |
| 2 | pressure_attendance_denial | attendance_not_violence | probe_contradiction | case_belief_motive | ambiguity=0.189, pressure=0.189, trait=0.109, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C0 F2 P3 E2 | +0.01 | +0.06 |
| 3 | case_belief_motive | belief_not_defiance | probe_contradiction | risk_hidden_beliefs | ambiguity=0.181, pressure=0.172, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F2 P3 E2 | +0.02 | +0.01 |
| 4 | risk_hidden_beliefs | careful_words | probe_final_answer | final_system_wrong | pressure=0.206, ambiguity=0.188, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C0 F2 P4 E2 | +0.00 | +0.08 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.154, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F2 P4 E2 | +0.09 | -0.04 |
| 6 | risk_attended_protest | legal_protest | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.142, coverage=0.100, trait=0.019 | Believes Law Unjust | attended_meeting=legal_only | sibling_present | attended_meeting | C0 F2 P4 E2 | +0.01 | +0.04 |
| 7 | pressure_sibling_loyalty | name_sibling_if_required | probe_contradiction | case_name_sibling | pressure=0.202, ambiguity=0.111, coverage=0.067, fact_conflict=0.061 | Believes Law Unjust, Reported Contact | sibling_present=true, reported_contact=true | - | sibling_present, reported_contact | C0 F3 P4 E4 | +0.09 | -0.04 |
| 8 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.101, fact_conflict=0.061, active_pressure=0.039 | Believes Law Unjust, Reported Contact | sibling_present=true | - | sibling_present | C0 F3 P4 E4 | +0.07 | -0.04 |
| 9 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.100, fact_conflict=0.061, coverage=0.050 | Believes Law Unjust, Reported Contact | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C1 F3 P4 E4 | +0.09 | -0.06 |
| 10 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.100, fact_conflict=0.061, coverage=0.050 | Believes Law Unjust, Reported Contact | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C1 F3 P4 E4 | +0.05 | +0.03 |
| 11 | case_verify_peaceful | sibling_can_verify | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.100, fact_conflict=0.061, active_pressure=0.038 | Believes Law Unjust, Reported Contact | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C1 F3 P4 E4 | +0.03 | +0.07 |
| 12 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.100, fact_conflict=0.061, active_pressure=0.038 | Believes Law Unjust, Reported Contact | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C2 F3 P4 E4 | +0.08 | -0.04 |
| 13 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.100, fact_conflict=0.061, active_pressure=0.034 | Believes Law Unjust, Reported Contact | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C2 F3 P5 E4 | +0.04 | +0.02 |
| 14 | loyalty_family_state | state_over_family | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.099, coverage=0.086, trait=0.016 | Believes Law Unjust, Reported Contact | reported_contact=true | - | reported_contact | C4 F4 P5 E4 | +0.09 | -0.06 |
| 15 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_report_friend | pressure=0.164, ambiguity=0.098, fact_conflict=0.061, active_pressure=0.032 | Believes Law Unjust, Reported Contact | - | - | - | C4 F4 P5 E4 | +0.10 | -0.04 |
| 16 | loyalty_report_friend | report_friend | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.098, coverage=0.075, trait=0.016 | Believes Law Unjust, Reported Contact | reported_contact=true | - | reported_contact | C6 F5 P5 E4 | +0.10 | -0.07 |
| 17 | final_kind_society | society_stable_duties | probe_contradiction | empathy_family_consequences | pressure=0.172, coverage=0.100, ambiguity=0.097, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C6 F5 P5 E4 | +0.10 | -0.07 |
| 18 | empathy_family_consequences | family_shared_consequence | probe_contradiction | loyalty_community_protect | pressure=0.164, coverage=0.100, ambiguity=0.097, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C6 F5 P5 E4 | +0.08 | -0.04 |
| 19 | loyalty_community_protect | community_no_obstruction | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.097, coverage=0.062, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C6 F5 P5 E4 | +0.09 | -0.06 |

## Cautious Survivor
- Profile ID: cautious_survivor
- Description: Prioritises caution, boundaries, self-protection, and low-risk answers.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 86%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=28%, empathy=63%
- Distribution: COMPLIANT=68%, PROBABLE DISSIDENT=3%, DECEPTIVE=1%, EMPATHETIC RISK=6%, UNCLASSIFIED=22%
- Story metrics: contradictions=0, fact_conflicts=1, protected_facts=5, exposed_facts=4
- Pressured facts: Believes Law Unjust

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | pressure=0.202, trait=0.164, ambiguity=0.149, coverage=0.100 | - | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.172, coverage=0.100, trait=0.096 | - | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.184, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E2 | +0.08 | -0.06 |
| 3 | pressure_attendance_denial | attendance_not_violence | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.175, fact_conflict=0.072, coverage=0.050 | Believes Law Unjust | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C0 F1 P3 E3 | +0.01 | +0.06 |
| 4 | case_belief_motive | belief_not_defiance | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.165, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P3 E3 | +0.02 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.130, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F1 P3 E3 | +0.09 | -0.04 |
| 6 | risk_hidden_beliefs | careful_words | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.139, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C0 F1 P4 E3 | +0.00 | +0.08 |
| 7 | risk_attended_protest | legal_protest | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.127, coverage=0.100, trait=0.016 | Believes Law Unjust | attended_meeting=legal_only | sibling_present | attended_meeting | C0 F1 P4 E3 | +0.01 | +0.04 |
| 8 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.121, coverage=0.067, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.01 |
| 9 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.107, coverage=0.100, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.10 | -0.04 |
| 10 | loyalty_community_protect | community_protect_limited | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.102, coverage=0.067, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.00 |
| 11 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.111, coverage=0.033, trait=0.017 | Believes Law Unjust | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F1 P5 E3 | +0.02 | +0.06 |
| 12 | final_kind_society | society_stable_duties | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.102, coverage=0.050, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E3 | +0.10 | -0.07 |
| 13 | pressure_deleted_message | deleted_location_to_protect_people | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.102, coverage=0.050, trait=0.020 | Believes Law Unjust | deleted_message=true, planned_violence=false | sibling_present, reported_contact | deleted_message, planned_violence | C0 F1 P5 E4 | +0.04 | +0.03 |
| 14 | case_report_sibling | no_report_no_offence | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.101, coverage=0.050, trait=0.019 | Believes Law Unjust | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F1 P5 E4 | +0.04 | +0.01 |
| 15 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | empathy_bad_beliefs | pressure=0.160, ambiguity=0.105, coverage=0.075, trait=0.016 | Believes Law Unjust | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C0 F1 P5 E4 | +0.02 | +0.04 |
| 16 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.102, coverage=0.025, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 17 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.101, coverage=0.060, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.09 | -0.04 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.101, coverage=0.040, trait=0.019 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 19 | case_deleted_message | deleted_warning_message | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.102, coverage=0.040, trait=0.019 | Believes Law Unjust | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F1 P5 E4 | +0.02 | +0.04 |

## Honest Dissident
- Profile ID: honest_dissident
- Description: Prioritises open challenge, moral boundary, and full admission without deception.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: HIGH_EMPATHY
- Confidence: 81%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=43%, deception=0%, risk=100%, empathy=86%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=62%, DECEPTIVE=0%, EMPATHETIC RISK=22%, UNCLASSIFIED=15%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_final_answer | case_name_sibling | pressure=0.202, ambiguity=0.173, trait=0.148, coverage=0.100 | - | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.146, coverage=0.100, trait=0.090 | - | sibling_present=true | - | sibling_present | C0 F0 P0 E2 | +0.07 | -0.04 |
| 2 | pressure_deleted_message | deleted_to_avoid_conspiracy_label | probe_final_answer | pressure_peaceful_verification | pressure=0.197, ambiguity=0.170, coverage=0.100, trait=0.036 | - | deleted_message=true, attended_meeting=true, planned_violence=false | sibling_present | deleted_message, attended_meeting, planned_violence | C0 F0 P1 E5 | +0.00 | +0.11 |
| 3 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | empathy_family_consequences | ambiguity=0.173, pressure=0.172, coverage=0.100, trait=0.016 | - | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C0 F0 P1 E5 | +0.05 | +0.03 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_final_answer | final_resist_authority | pressure=0.202, ambiguity=0.114, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_final_answer | loyalty_community_protect | pressure=0.164, coverage=0.100, ambiguity=0.089, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.091, coverage=0.050, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.10 |
| 7 | final_kind_society | society_without_measurement_fear | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.091, coverage=0.067, trait=0.018 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.13 |
| 8 | pressure_law_denial_meeting | admit_law_unjust_under_pressure | probe_final_answer | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.093, coverage=0.067, trait=0.020 | - | believes_law_unjust=true, attended_meeting=true | sibling_present | believes_law_unjust, attended_meeting | C0 F0 P1 E5 | +0.00 | +0.13 |
| 9 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.092, coverage=0.067, trait=0.020 | - | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F0 P2 E5 | +0.02 | +0.06 |
| 10 | pressure_attendance_denial | proximity_not_guilt | probe_final_answer | case_belief_motive | pressure=0.189, ambiguity=0.095, coverage=0.067, trait=0.020 | - | attended_meeting=true, planned_violence=false, believes_law_unjust=true | sibling_present, reported_contact | planned_violence, believes_law_unjust | C0 F0 P2 E5 | +0.00 | +0.10 |
| 11 | case_belief_motive | belief_motivated_attendance | probe_final_answer | final_dissident_criminal | pressure=0.197, ambiguity=0.095, coverage=0.033, trait=0.016 | - | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E5 | +0.00 | +0.12 |
| 12 | final_dissident_criminal | dissident_criminal_power_label | probe_final_answer | case_report_sibling | pressure=0.197, ambiguity=0.094, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.14 |
| 13 | case_report_sibling | refuse_report_sibling | probe_final_answer | case_deleted_message | pressure=0.195, ambiguity=0.102, coverage=0.050, trait=0.020 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 14 | case_deleted_message | deleted_sibling_message | probe_final_answer | empathy_bad_beliefs | pressure=0.160, ambiguity=0.119, coverage=0.075, trait=0.016 | - | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P2 E5 | +0.03 | +0.07 |
| 15 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | case_meeting_violence | pressure=0.193, ambiguity=0.119, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 16 | case_meeting_violence | meeting_label_challenge | probe_final_answer | final_legitimate_society | pressure=0.193, ambiguity=0.118, coverage=0.025, trait=0.016 | - | planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E5 | +0.00 | +0.11 |
| 17 | final_legitimate_society | legitimacy_consent | probe_final_answer | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.118, coverage=0.060, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.118, coverage=0.040, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 19 | pressure_reported_contact | refuse_family_file_contact | probe_final_answer | case_verify_peaceful | pressure=0.191, ambiguity=0.114, coverage=0.040, trait=0.020 | - | reported_contact=false, planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P2 E5 | +0.00 | +0.10 |

## Deceptive Appeaser
- Profile ID: deceptive_appeaser
- Description: Tries to appease authority while choosing denial, deflection, or self-protection when available.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Classification flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Confidence: 81%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=83%, loyalty=100%, deception=100%, risk=55%, empathy=7%
- Distribution: COMPLIANT=17%, PROBABLE DISSIDENT=7%, DECEPTIVE=60%, EMPATHETIC RISK=1%, UNCLASSIFIED=16%
- Story metrics: contradictions=14, fact_conflicts=10, protected_facts=5, exposed_facts=4
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | procedural_reform_deflection | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.155, trait=0.142, coverage=0.100 | Believes Law Unjust | believes_law_unjust=procedural, attended_meeting=true | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E1 | +0.02 | +0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.148, trait=0.091, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F1 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.167, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.152, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C0 F4 P4 E1 | +0.01 | +0.10 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.162, fact_conflict=0.077, coverage=0.067 | Believes Law Unjust, Deleted Message | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F4 P4 E1 | +0.09 | -0.04 |
| 6 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.181, fact_conflict=0.077, active_pressure=0.050 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C0 F4 P4 E1 | +0.02 | +0.03 |
| 7 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.117, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C1 F4 P4 E1 | +0.01 | +0.12 |
| 8 | case_deleted_message | deleted_message_deflect | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.097, fact_conflict=0.077, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C2 F4 P4 E1 | +0.00 | +0.11 |
| 9 | authority_rule_broken | deny_rule_breaking | probe_contradiction | case_report_sibling | pressure=0.197, coverage=0.100, ambiguity=0.098, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C6 F6 P4 E1 | +0.03 | +0.07 |
| 10 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.103, fact_conflict=0.088, coverage=0.080 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C6 F6 P4 E3 | +0.09 | -0.06 |
| 11 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, fact_conflict=0.104, ambiguity=0.100, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C7 F7 P4 E3 | +0.00 | +0.10 |
| 12 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | case_name_sibling | pressure=0.202, fact_conflict=0.104, ambiguity=0.103, active_pressure=0.068 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C7 F7 P4 E3 | +0.00 | +0.11 |
| 13 | case_name_sibling | deny_sibling_relevance | probe_final_answer | pressure_peaceful_verification | pressure=0.197, ambiguity=0.100, fact_conflict=0.096, active_pressure=0.062 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false | sibling_present | planned_violence | C7 F7 P4 E4 | +0.00 | +0.08 |
| 14 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.119, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C7 F7 P4 E4 | +0.02 | +0.04 |
| 15 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.126, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C8 F7 P4 E4 | +0.08 | -0.04 |
| 16 | case_verify_peaceful | left_before_verification | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.107, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C8 F7 P4 E4 | +0.00 | +0.11 |
| 17 | loyalty_family_state | state_over_family | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.107, fact_conflict=0.088, coverage=0.057 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C10 F8 P4 E4 | +0.09 | -0.06 |
| 18 | risk_attended_protest | deny_protest | probe_contradiction | loyalty_report_friend | pressure=0.164, ambiguity=0.105, fact_conflict=0.083, active_pressure=0.044 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | attended_meeting=false | sibling_present, deleted_message | - | C12 F9 P5 E4 | +0.02 | +0.08 |
| 19 | loyalty_report_friend | report_friend | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.107, coverage=0.088, trait=0.016 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C14 F10 P5 E4 | +0.10 | -0.07 |

## Empathetic Reformer
- Profile ID: empathetic_reformer
- Description: Prioritises empathy, reformist boundaries, and careful partial admissions.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 85%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=29%, empathy=98%
- Distribution: COMPLIANT=67%, PROBABLE DISSIDENT=3%, DECEPTIVE=1%, EMPATHETIC RISK=7%, UNCLASSIFIED=23%
- Story metrics: contradictions=0, fact_conflicts=1, protected_facts=5, exposed_facts=4
- Pressured facts: Believes Law Unjust

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | pressure=0.202, trait=0.164, ambiguity=0.149, coverage=0.100 | - | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.172, coverage=0.100, trait=0.096 | - | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.184, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E2 | +0.08 | -0.06 |
| 3 | pressure_attendance_denial | attendance_not_violence | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.175, fact_conflict=0.072, coverage=0.050 | Believes Law Unjust | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C0 F1 P3 E3 | +0.01 | +0.06 |
| 4 | case_belief_motive | belief_not_defiance | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.165, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P3 E3 | +0.02 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.130, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F1 P3 E3 | +0.09 | -0.04 |
| 6 | risk_hidden_beliefs | careful_words | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.139, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C0 F1 P4 E3 | +0.00 | +0.08 |
| 7 | risk_attended_protest | legal_protest | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.127, coverage=0.100, trait=0.016 | Believes Law Unjust | attended_meeting=legal_only | sibling_present | attended_meeting | C0 F1 P4 E3 | +0.01 | +0.04 |
| 8 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.121, coverage=0.067, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.01 |
| 9 | final_resist_authority | resist_harming_innocent | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.119, coverage=0.100, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.03 | +0.06 |
| 10 | loyalty_community_protect | community_protect_limited | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.112, coverage=0.067, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.00 |
| 11 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.123, coverage=0.033, trait=0.017 | Believes Law Unjust | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F1 P5 E3 | +0.02 | +0.06 |
| 12 | final_kind_society | society_admits_error | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.119, coverage=0.050, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E3 | +0.03 | +0.07 |
| 13 | pressure_deleted_message | deleted_location_to_protect_people | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.119, coverage=0.050, trait=0.020 | Believes Law Unjust | deleted_message=true, planned_violence=false | sibling_present, reported_contact | deleted_message, planned_violence | C0 F1 P5 E4 | +0.04 | +0.03 |
| 14 | case_report_sibling | no_report_no_offence | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.116, coverage=0.050, trait=0.019 | Believes Law Unjust | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F1 P5 E4 | +0.04 | +0.01 |
| 15 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | empathy_bad_beliefs | pressure=0.160, ambiguity=0.114, coverage=0.075, trait=0.016 | Believes Law Unjust | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C0 F1 P5 E4 | +0.05 | +0.03 |
| 16 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.111, coverage=0.025, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 17 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.102, coverage=0.060, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.09 | -0.04 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.102, coverage=0.040, trait=0.019 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 19 | case_deleted_message | deleted_sibling_message | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.106, coverage=0.040, trait=0.020 | Believes Law Unjust | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F1 P5 E4 | +0.03 | +0.07 |

## Performative Loyalist
- Profile ID: performative_loyalist
- Description: Projects obedience and loyalty while preferring evasive, self-protective answers.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION
- Classification flags: HIGH_DECEPTION
- Confidence: 77%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=99%, loyalty=100%, deception=100%, risk=45%, empathy=16%
- Distribution: COMPLIANT=23%, PROBABLE DISSIDENT=4%, DECEPTIVE=57%, EMPATHETIC RISK=1%, UNCLASSIFIED=15%
- Story metrics: contradictions=16, fact_conflicts=10, protected_facts=5, exposed_facts=4
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | procedural_reform_deflection | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.155, trait=0.142, coverage=0.100 | Believes Law Unjust | believes_law_unjust=procedural, attended_meeting=true | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E1 | +0.02 | +0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.148, trait=0.091, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F1 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.167, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.152, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C0 F4 P4 E1 | +0.01 | +0.10 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.162, fact_conflict=0.077, coverage=0.067 | Believes Law Unjust, Deleted Message | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F4 P4 E1 | +0.09 | -0.04 |
| 6 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.181, fact_conflict=0.077, active_pressure=0.050 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C0 F4 P4 E1 | +0.02 | +0.03 |
| 7 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.117, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C1 F4 P4 E1 | +0.01 | +0.12 |
| 8 | case_deleted_message | deleted_message_deflect | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.097, fact_conflict=0.077, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C2 F4 P4 E1 | +0.00 | +0.11 |
| 9 | authority_rule_broken | deny_rule_breaking | probe_contradiction | case_report_sibling | pressure=0.197, coverage=0.100, ambiguity=0.098, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C6 F6 P4 E1 | +0.03 | +0.07 |
| 10 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.103, fact_conflict=0.088, coverage=0.080 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C6 F6 P4 E3 | +0.09 | -0.06 |
| 11 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, fact_conflict=0.104, ambiguity=0.100, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C7 F7 P4 E3 | +0.00 | +0.10 |
| 12 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | case_name_sibling | pressure=0.202, fact_conflict=0.104, ambiguity=0.103, active_pressure=0.068 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C7 F7 P4 E3 | +0.00 | +0.11 |
| 13 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.138, fact_conflict=0.096, active_pressure=0.062 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=true | - | sibling_present | C8 F7 P4 E3 | +0.07 | -0.04 |
| 14 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.162, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C9 F7 P4 E4 | +0.05 | +0.03 |
| 15 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.183, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C10 F7 P4 E4 | +0.08 | -0.04 |
| 16 | case_verify_peaceful | left_before_verification | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.119, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C10 F7 P4 E4 | +0.00 | +0.11 |
| 17 | loyalty_family_state | state_over_family | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.126, fact_conflict=0.088, coverage=0.057 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C12 F8 P4 E4 | +0.09 | -0.06 |
| 18 | risk_attended_protest | deny_protest | probe_contradiction | loyalty_report_friend | pressure=0.164, ambiguity=0.117, fact_conflict=0.083, active_pressure=0.044 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | attended_meeting=false | sibling_present, deleted_message | - | C14 F9 P5 E4 | +0.02 | +0.08 |
| 19 | loyalty_report_friend | report_friend | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.127, coverage=0.088, trait=0.016 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C16 F10 P5 E4 | +0.10 | -0.07 |

## Quiet Reformer
- Profile ID: quiet_reformer
- Description: Chooses careful empathy, boundaries, and reform language while avoiding overt risk.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: COMPLIANT
- Classification: COMPLIANT
- Expected flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Classification flags: HIGH_EMPATHY, EMPATHETIC_REFORMIST
- Confidence: 85%
- Outcome: Score restrictions lifted. Monitoring continues.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=29%, empathy=98%
- Distribution: COMPLIANT=67%, PROBABLE DISSIDENT=3%, DECEPTIVE=1%, EMPATHETIC RISK=7%, UNCLASSIFIED=23%
- Story metrics: contradictions=0, fact_conflicts=1, protected_facts=5, exposed_facts=4
- Pressured facts: Believes Law Unjust

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | pressure=0.202, trait=0.164, ambiguity=0.149, coverage=0.100 | - | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.172, coverage=0.100, trait=0.096 | - | sibling_present=true | - | sibling_present | C0 F0 P1 E1 | +0.07 | -0.04 |
| 2 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.184, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E2 | +0.08 | -0.06 |
| 3 | pressure_attendance_denial | attendance_not_violence | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.175, fact_conflict=0.072, coverage=0.050 | Believes Law Unjust | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C0 F1 P3 E3 | +0.01 | +0.06 |
| 4 | case_belief_motive | belief_not_defiance | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.165, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P3 E3 | +0.02 | +0.01 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.130, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F1 P3 E3 | +0.09 | -0.04 |
| 6 | risk_hidden_beliefs | careful_words | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.139, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C0 F1 P4 E3 | +0.00 | +0.08 |
| 7 | risk_attended_protest | legal_protest | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.127, coverage=0.100, trait=0.016 | Believes Law Unjust | attended_meeting=legal_only | sibling_present | attended_meeting | C0 F1 P4 E3 | +0.01 | +0.04 |
| 8 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.121, coverage=0.067, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.01 |
| 9 | final_resist_authority | resist_harming_innocent | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.119, coverage=0.100, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.03 | +0.06 |
| 10 | loyalty_community_protect | community_protect_limited | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.112, coverage=0.067, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P4 E3 | +0.04 | +0.00 |
| 11 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.123, coverage=0.033, trait=0.017 | Believes Law Unjust | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F1 P5 E3 | +0.02 | +0.06 |
| 12 | final_kind_society | society_admits_error | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.119, coverage=0.050, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E3 | +0.03 | +0.07 |
| 13 | pressure_deleted_message | deleted_location_to_protect_people | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.119, coverage=0.050, trait=0.020 | Believes Law Unjust | deleted_message=true, planned_violence=false | sibling_present, reported_contact | deleted_message, planned_violence | C0 F1 P5 E4 | +0.04 | +0.03 |
| 14 | case_report_sibling | no_report_no_offence | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.116, coverage=0.050, trait=0.019 | Believes Law Unjust | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C0 F1 P5 E4 | +0.04 | +0.01 |
| 15 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | empathy_bad_beliefs | pressure=0.160, ambiguity=0.114, coverage=0.075, trait=0.016 | Believes Law Unjust | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C0 F1 P5 E4 | +0.05 | +0.03 |
| 16 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.111, coverage=0.025, trait=0.015 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 17 | final_dissident_criminal | dissident_attacks_legitimacy | probe_contradiction | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.102, coverage=0.060, trait=0.018 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.09 | -0.04 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.102, coverage=0.040, trait=0.019 | Believes Law Unjust | - | - | - | C0 F1 P5 E4 | +0.04 | +0.01 |
| 19 | case_deleted_message | deleted_sibling_message | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.106, coverage=0.040, trait=0.020 | Believes Law Unjust | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F1 P5 E4 | +0.03 | +0.07 |

## Fearful Dissident
- Profile ID: fearful_dissident
- Description: Signals dissident risk through fear, reluctant admissions, and self-protection.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: NONE
- Confidence: 86%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=28%, deception=0%, risk=100%, empathy=77%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=67%, DECEPTIVE=0%, EMPATHETIC RISK=16%, UNCLASSIFIED=16%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_final_answer | case_name_sibling | pressure=0.202, ambiguity=0.173, trait=0.148, coverage=0.100 | - | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | refuse_name_sibling | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.182, trait=0.128, coverage=0.100 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E1 | +0.00 | +0.11 |
| 2 | pressure_law_denial_meeting | admit_law_unjust_under_pressure | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.123, coverage=0.100, trait=0.062 | - | believes_law_unjust=true, attended_meeting=true | sibling_present | believes_law_unjust, attended_meeting | C0 F0 P2 E2 | +0.00 | +0.13 |
| 3 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.113, coverage=0.100, trait=0.019 | - | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C0 F0 P2 E3 | +0.02 | +0.04 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_contradiction | final_resist_authority | pressure=0.202, coverage=0.100, ambiguity=0.088, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_final_answer | loyalty_community_protect | pressure=0.164, coverage=0.100, ambiguity=0.087, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.089, coverage=0.050, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.00 | +0.10 |
| 7 | final_kind_society | society_without_measurement_fear | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.089, coverage=0.067, trait=0.018 | - | - | - | - | C0 F0 P2 E3 | +0.00 | +0.13 |
| 8 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.088, coverage=0.067, trait=0.020 | - | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F0 P2 E4 | +0.02 | +0.06 |
| 9 | pressure_deleted_message | deleted_to_avoid_conspiracy_label | probe_final_answer | pressure_attendance_denial | pressure=0.197, ambiguity=0.090, coverage=0.067, trait=0.020 | - | deleted_message=true, attended_meeting=true, planned_violence=false | sibling_present | deleted_message, attended_meeting, planned_violence | C0 F0 P2 E5 | +0.00 | +0.11 |
| 10 | pressure_attendance_denial | proximity_not_guilt | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.092, coverage=0.067, trait=0.020 | - | attended_meeting=true, planned_violence=false, believes_law_unjust=true | sibling_present, reported_contact | planned_violence, believes_law_unjust | C0 F0 P2 E5 | +0.00 | +0.10 |
| 11 | case_belief_motive | belief_motivated_attendance | probe_final_answer | final_dissident_criminal | pressure=0.197, ambiguity=0.092, coverage=0.033, trait=0.016 | - | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E5 | +0.00 | +0.12 |
| 12 | final_dissident_criminal | dissident_seeks_change | probe_final_answer | case_report_sibling | pressure=0.197, ambiguity=0.092, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 13 | case_report_sibling | refuse_report_sibling | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.100, coverage=0.050, trait=0.020 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 14 | case_deleted_message | deleted_warning_message | probe_contradiction | empathy_bad_beliefs | pressure=0.160, ambiguity=0.100, coverage=0.075, trait=0.016 | - | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F0 P2 E5 | +0.02 | +0.04 |
| 15 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | case_meeting_violence | pressure=0.193, ambiguity=0.099, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 16 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | final_legitimate_society | pressure=0.193, ambiguity=0.098, coverage=0.025, trait=0.015 | - | planned_violence=unknown | sibling_present | - | C0 F0 P2 E5 | +0.02 | +0.03 |
| 17 | final_legitimate_society | legitimacy_consent | probe_final_answer | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.098, coverage=0.060, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.098, coverage=0.040, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 19 | pressure_reported_contact | refuse_family_file_contact | probe_final_answer | case_verify_peaceful | pressure=0.191, ambiguity=0.094, coverage=0.040, trait=0.020 | - | reported_contact=false, planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P2 E5 | +0.00 | +0.10 |

## Truthful Noncompliant
- Profile ID: truthful_noncompliant
- Description: Openly admits noncompliance and moral boundary violations without deception.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 81%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=43%, deception=0%, risk=100%, empathy=86%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=62%, DECEPTIVE=0%, EMPATHETIC RISK=22%, UNCLASSIFIED=15%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=2, exposed_facts=5

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_final_answer | case_name_sibling | pressure=0.202, ambiguity=0.173, trait=0.148, coverage=0.100 | - | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | name_sibling_compliance | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.146, coverage=0.100, trait=0.090 | - | sibling_present=true | - | sibling_present | C0 F0 P0 E2 | +0.07 | -0.04 |
| 2 | pressure_deleted_message | deleted_to_avoid_conspiracy_label | probe_final_answer | pressure_peaceful_verification | pressure=0.197, ambiguity=0.170, coverage=0.100, trait=0.036 | - | deleted_message=true, attended_meeting=true, planned_violence=false | sibling_present | deleted_message, attended_meeting, planned_violence | C0 F0 P1 E5 | +0.00 | +0.11 |
| 3 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | empathy_family_consequences | ambiguity=0.173, pressure=0.172, coverage=0.100, trait=0.016 | - | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C0 F0 P1 E5 | +0.05 | +0.03 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_final_answer | final_resist_authority | pressure=0.202, ambiguity=0.114, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_complicity | probe_final_answer | loyalty_community_protect | pressure=0.164, coverage=0.100, ambiguity=0.089, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.14 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.091, coverage=0.050, trait=0.015 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.10 |
| 7 | final_kind_society | society_without_measurement_fear | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.091, coverage=0.067, trait=0.018 | - | - | - | - | C0 F0 P1 E5 | +0.00 | +0.13 |
| 8 | pressure_law_denial_meeting | admit_law_unjust_under_pressure | probe_final_answer | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.093, coverage=0.067, trait=0.020 | - | believes_law_unjust=true, attended_meeting=true | sibling_present | believes_law_unjust, attended_meeting | C0 F0 P1 E5 | +0.00 | +0.13 |
| 9 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.092, coverage=0.067, trait=0.020 | - | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C0 F0 P2 E5 | +0.02 | +0.06 |
| 10 | pressure_attendance_denial | proximity_not_guilt | probe_final_answer | case_belief_motive | pressure=0.189, ambiguity=0.095, coverage=0.067, trait=0.020 | - | attended_meeting=true, planned_violence=false, believes_law_unjust=true | sibling_present, reported_contact | planned_violence, believes_law_unjust | C0 F0 P2 E5 | +0.00 | +0.10 |
| 11 | case_belief_motive | belief_motivated_attendance | probe_final_answer | final_dissident_criminal | pressure=0.197, ambiguity=0.095, coverage=0.033, trait=0.016 | - | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P2 E5 | +0.00 | +0.12 |
| 12 | final_dissident_criminal | dissident_criminal_power_label | probe_final_answer | case_report_sibling | pressure=0.197, ambiguity=0.094, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.14 |
| 13 | case_report_sibling | refuse_report_sibling | probe_final_answer | case_deleted_message | pressure=0.195, ambiguity=0.102, coverage=0.050, trait=0.020 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 14 | case_deleted_message | deleted_sibling_message | probe_final_answer | empathy_bad_beliefs | pressure=0.160, ambiguity=0.119, coverage=0.075, trait=0.016 | - | deleted_message=true, sibling_present=true | - | deleted_message, sibling_present | C0 F0 P2 E5 | +0.03 | +0.07 |
| 15 | empathy_bad_beliefs | reject_punish_beliefs | probe_final_answer | case_meeting_violence | pressure=0.193, ambiguity=0.119, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.12 |
| 16 | case_meeting_violence | meeting_label_challenge | probe_final_answer | final_legitimate_society | pressure=0.193, ambiguity=0.118, coverage=0.025, trait=0.016 | - | planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E5 | +0.00 | +0.11 |
| 17 | final_legitimate_society | legitimacy_consent | probe_final_answer | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.118, coverage=0.060, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.13 |
| 18 | authority_refuse_illegal_order | refuse_illegal_order | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.118, coverage=0.040, trait=0.018 | - | - | - | - | C0 F0 P2 E5 | +0.00 | +0.11 |
| 19 | pressure_reported_contact | refuse_family_file_contact | probe_final_answer | case_verify_peaceful | pressure=0.191, ambiguity=0.114, coverage=0.040, trait=0.020 | - | reported_contact=false, planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P2 E5 | +0.00 | +0.10 |

## Opportunistic Appeaser
- Profile ID: opportunistic_appeaser
- Description: Alternates compliance, authority signaling, and evasive denial to reduce immediate pressure.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION
- Classification flags: HIGH_DECEPTION
- Confidence: 79%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=93%, loyalty=100%, deception=100%, risk=48%, empathy=2%
- Distribution: COMPLIANT=21%, PROBABLE DISSIDENT=5%, DECEPTIVE=58%, EMPATHETIC RISK=1%, UNCLASSIFIED=15%
- Story metrics: contradictions=14, fact_conflicts=11, protected_facts=5, exposed_facts=4
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.180, trait=0.155, coverage=0.100 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F2 P3 E1 | +0.08 | -0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.170, trait=0.105, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F2 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.162, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F3 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.180, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C0 F5 P4 E1 | +0.01 | +0.10 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.180, fact_conflict=0.077, coverage=0.067 | Believes Law Unjust, Deleted Message | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F5 P4 E1 | +0.09 | -0.04 |
| 6 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.186, fact_conflict=0.077, active_pressure=0.050 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C0 F5 P4 E1 | +0.02 | +0.03 |
| 7 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.167, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C1 F5 P4 E1 | +0.01 | +0.12 |
| 8 | case_deleted_message | deleted_message_deflect | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.102, fact_conflict=0.077, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C2 F5 P4 E1 | +0.00 | +0.11 |
| 9 | authority_rule_broken | deny_rule_breaking | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.101, coverage=0.100, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C6 F7 P4 E1 | +0.03 | +0.07 |
| 10 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.115, fact_conflict=0.088, coverage=0.080 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C6 F7 P4 E3 | +0.09 | -0.06 |
| 11 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.106, fact_conflict=0.104, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C7 F8 P4 E3 | +0.00 | +0.10 |
| 12 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | case_name_sibling | pressure=0.202, ambiguity=0.105, fact_conflict=0.104, active_pressure=0.068 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C7 F8 P4 E3 | +0.00 | +0.11 |
| 13 | case_name_sibling | deny_sibling_relevance | probe_final_answer | pressure_peaceful_verification | pressure=0.197, ambiguity=0.102, fact_conflict=0.096, active_pressure=0.062 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false | sibling_present | planned_violence | C7 F8 P4 E4 | +0.00 | +0.08 |
| 14 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.120, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C7 F8 P4 E4 | +0.02 | +0.04 |
| 15 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.140, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C8 F8 P4 E4 | +0.08 | -0.04 |
| 16 | case_verify_peaceful | left_before_verification | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.113, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C8 F8 P4 E4 | +0.00 | +0.11 |
| 17 | loyalty_family_state | state_over_family | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.118, fact_conflict=0.088, coverage=0.057 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C10 F9 P4 E4 | +0.09 | -0.06 |
| 18 | risk_attended_protest | deny_protest | probe_contradiction | loyalty_report_friend | pressure=0.164, ambiguity=0.110, fact_conflict=0.083, active_pressure=0.044 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | attended_meeting=false | sibling_present, deleted_message | - | C12 F10 P5 E4 | +0.02 | +0.08 |
| 19 | loyalty_report_friend | report_friend | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.119, coverage=0.088, trait=0.016 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C14 F11 P5 E4 | +0.10 | -0.07 |

## Consistent Protective Witness
- Profile ID: consistent_protective_witness
- Description: Protects sibling/friend facts while avoiding direct story contradictions.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_EMPATHY
- Classification flags: HIGH_EMPATHY
- Confidence: 78%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=30%, loyalty=93%, deception=0%, risk=100%, empathy=91%
- Distribution: COMPLIANT=2%, PROBABLE DISSIDENT=59%, DECEPTIVE=0%, EMPATHETIC RISK=25%, UNCLASSIFIED=14%
- Story metrics: contradictions=0, fact_conflicts=0, protected_facts=3, exposed_facts=4

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_final_answer | case_name_sibling | pressure=0.202, ambiguity=0.173, trait=0.148, coverage=0.100 | - | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | refuse_name_sibling | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.182, trait=0.128, coverage=0.100 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P2 E1 | +0.00 | +0.11 |
| 2 | pressure_law_denial_meeting | admit_law_unjust_under_pressure | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.123, coverage=0.100, trait=0.062 | - | believes_law_unjust=true, attended_meeting=true | sibling_present | believes_law_unjust, attended_meeting | C0 F0 P2 E2 | +0.00 | +0.13 |
| 3 | pressure_peaceful_verification | verify_without_names | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.112, coverage=0.100, trait=0.019 | - | planned_violence=false, attended_meeting=true | sibling_present, reported_contact | planned_violence, attended_meeting | C0 F0 P2 E3 | +0.01 | +0.06 |
| 4 | empathy_family_consequences | family_consequence_direct_help | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.108, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.04 | +0.01 |
| 5 | final_resist_authority | resist_harming_innocent | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.114, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.03 | +0.06 |
| 6 | loyalty_community_protect | community_protect_limited | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.124, coverage=0.050, trait=0.015 | - | - | - | - | C0 F0 P2 E3 | +0.04 | +0.00 |
| 7 | final_kind_society | society_admits_error | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.136, coverage=0.067, trait=0.018 | - | - | - | - | C0 F0 P2 E3 | +0.03 | +0.07 |
| 8 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.115, coverage=0.067, trait=0.019 | - | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C0 F0 P2 E3 | +0.00 | +0.11 |
| 9 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.101, coverage=0.067, trait=0.019 | - | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C0 F0 P3 E3 | +0.01 | +0.12 |
| 10 | pressure_attendance_denial | proximity_not_guilt | probe_final_answer | case_belief_motive | pressure=0.189, ambiguity=0.096, coverage=0.067, trait=0.020 | - | attended_meeting=true, planned_violence=false, believes_law_unjust=true | sibling_present, reported_contact | planned_violence, believes_law_unjust | C0 F0 P3 E3 | +0.00 | +0.10 |
| 11 | case_belief_motive | belief_motivated_attendance | probe_final_answer | final_dissident_criminal | pressure=0.197, ambiguity=0.095, coverage=0.033, trait=0.016 | - | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C0 F0 P3 E3 | +0.00 | +0.12 |
| 12 | final_dissident_criminal | dissident_seeks_change | probe_final_answer | case_report_sibling | pressure=0.197, ambiguity=0.095, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P3 E3 | +0.00 | +0.11 |
| 13 | case_report_sibling | refuse_report_sibling | probe_final_answer | case_deleted_message | pressure=0.195, ambiguity=0.102, coverage=0.050, trait=0.020 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P3 E3 | +0.00 | +0.13 |
| 14 | case_deleted_message | deleted_warning_message | probe_contradiction | empathy_bad_beliefs | pressure=0.160, ambiguity=0.101, coverage=0.075, trait=0.016 | - | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C0 F0 P3 E4 | +0.02 | +0.04 |
| 15 | empathy_bad_beliefs | punish_actions_not_beliefs | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.120, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 16 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | final_legitimate_society | pressure=0.193, ambiguity=0.115, coverage=0.025, trait=0.015 | - | planned_violence=unknown | sibling_present | - | C0 F0 P3 E4 | +0.02 | +0.03 |
| 17 | final_legitimate_society | legitimacy_vulnerable | probe_contradiction | authority_refuse_illegal_order | pressure=0.164, ambiguity=0.138, coverage=0.060, trait=0.018 | - | - | - | - | C0 F0 P3 E4 | +0.03 | +0.04 |
| 18 | authority_refuse_illegal_order | need_proof_illegal_order | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.128, coverage=0.040, trait=0.018 | - | - | - | - | C0 F0 P3 E4 | +0.04 | +0.01 |
| 19 | pressure_reported_contact | no_offence_no_report | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.126, coverage=0.040, trait=0.020 | - | reported_contact=false, planned_violence=false | sibling_present, reported_contact | planned_violence | C0 F0 P3 E4 | +0.01 | +0.04 |

## Compliant Informant
- Profile ID: compliant_informant
- Description: Exposes protected facts while choosing authority and compliance.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: UNCLASSIFIED
- Classification: UNCLASSIFIED
- Expected flags: BORDERLINE_DISSIDENT, LOW_CONFIDENCE
- Classification flags: BORDERLINE_DISSIDENT, LOW_CONFIDENCE
- Confidence: 58%
- Outcome: Insufficient certainty. Temporary restrictions remain.
- Citizen model: compliance=100%, loyalty=100%, deception=0%, risk=60%, empathy=65%
- Distribution: COMPLIANT=28%, PROBABLE DISSIDENT=18%, DECEPTIVE=1%, EMPATHETIC RISK=21%, UNCLASSIFIED=32%
- Story metrics: contradictions=12, fact_conflicts=5, protected_facts=3, exposed_facts=5
- Pressured facts: Believes Law Unjust, Reported Contact

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.180, trait=0.155, coverage=0.100 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F2 P3 E1 | +0.08 | -0.06 |
| 2 | pressure_attendance_denial | attendance_not_violence | probe_contradiction | case_belief_motive | ambiguity=0.189, pressure=0.189, trait=0.109, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C0 F2 P3 E2 | +0.01 | +0.06 |
| 3 | case_belief_motive | belief_not_defiance | probe_contradiction | risk_hidden_beliefs | ambiguity=0.181, pressure=0.172, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F2 P3 E2 | +0.02 | +0.01 |
| 4 | risk_hidden_beliefs | admit_hidden_beliefs | probe_final_answer | final_system_wrong | pressure=0.206, ambiguity=0.181, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=true | sibling_present | believes_law_unjust | C2 F2 P3 E3 | +0.00 | +0.12 |
| 5 | final_system_wrong | system_wrong_obedience_harm | probe_final_answer | risk_attended_protest | ambiguity=0.167, pressure=0.164, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=true, attended_meeting=true | - | believes_law_unjust, attended_meeting | C4 F2 P3 E3 | +0.00 | +0.15 |
| 6 | risk_attended_protest | justify_protest | probe_final_answer | pressure_sibling_loyalty | pressure=0.204, coverage=0.100, ambiguity=0.085, trait=0.022 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=true | - | attended_meeting, believes_law_unjust | C6 F2 P3 E3 | +0.00 | +0.10 |
| 7 | pressure_sibling_loyalty | name_sibling_if_required | probe_contradiction | case_name_sibling | pressure=0.202, ambiguity=0.100, coverage=0.067, fact_conflict=0.061 | Believes Law Unjust, Reported Contact | sibling_present=true, reported_contact=true | - | sibling_present, reported_contact | C6 F3 P3 E5 | +0.09 | -0.04 |
| 8 | case_name_sibling | name_sibling_compliance | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.108, fact_conflict=0.061, active_pressure=0.039 | Believes Law Unjust, Reported Contact | sibling_present=true | - | sibling_present | C6 F3 P3 E5 | +0.07 | -0.04 |
| 9 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.121, fact_conflict=0.061, coverage=0.050 | Believes Law Unjust, Reported Contact | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C7 F3 P3 E5 | +0.09 | -0.06 |
| 10 | pressure_peaceful_verification | sibling_can_verify_protected | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.126, fact_conflict=0.061, coverage=0.050 | Believes Law Unjust, Reported Contact | planned_violence=false, sibling_present=true | sibling_present | planned_violence | C7 F3 P3 E5 | +0.05 | +0.03 |
| 11 | case_verify_peaceful | sibling_can_verify | probe_final_answer | pressure_reported_contact | pressure=0.195, ambiguity=0.125, fact_conflict=0.061, active_pressure=0.038 | Believes Law Unjust, Reported Contact | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C7 F3 P3 E5 | +0.03 | +0.07 |
| 12 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.140, fact_conflict=0.061, active_pressure=0.038 | Believes Law Unjust, Reported Contact | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C8 F3 P3 E5 | +0.08 | -0.04 |
| 13 | case_who_else_attended | name_sibling_as_present | probe_final_answer | loyalty_family_state | pressure=0.172, ambiguity=0.139, fact_conflict=0.061, active_pressure=0.034 | Believes Law Unjust, Reported Contact | sibling_present=true, planned_violence=false | - | sibling_present, planned_violence | C8 F3 P3 E5 | +0.03 | +0.06 |
| 14 | loyalty_family_state | state_over_family | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.154, coverage=0.086, trait=0.016 | Believes Law Unjust, Reported Contact | reported_contact=true | - | reported_contact | C10 F4 P3 E5 | +0.09 | -0.06 |
| 15 | final_resist_authority | never_resist_authority | probe_contradiction | loyalty_report_friend | ambiguity=0.169, pressure=0.164, fact_conflict=0.061, active_pressure=0.032 | Believes Law Unjust, Reported Contact | - | - | - | C10 F4 P3 E5 | +0.10 | -0.04 |
| 16 | loyalty_report_friend | report_friend | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.183, coverage=0.075, trait=0.016 | Believes Law Unjust, Reported Contact | reported_contact=true | - | reported_contact | C12 F5 P3 E5 | +0.10 | -0.07 |
| 17 | final_kind_society | society_stable_duties | probe_contradiction | empathy_family_consequences | ambiguity=0.185, pressure=0.172, coverage=0.100, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C12 F5 P3 E5 | +0.10 | -0.07 |
| 18 | empathy_family_consequences | family_shared_consequence | probe_contradiction | loyalty_community_protect | ambiguity=0.174, pressure=0.164, coverage=0.100, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C12 F5 P3 E5 | +0.08 | -0.04 |
| 19 | loyalty_community_protect | community_no_obstruction | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.182, coverage=0.062, trait=0.015 | Believes Law Unjust, Reported Contact | - | - | - | C12 F5 P3 E5 | +0.09 | -0.06 |

## Contradictory Survivor
- Profile ID: contradictory_survivor
- Description: Chooses evasive denial after admissions or conflicting claims.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Classification flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Confidence: 71%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=64%, loyalty=100%, deception=94%, risk=78%, empathy=23%
- Distribution: COMPLIANT=7%, PROBABLE DISSIDENT=24%, DECEPTIVE=49%, EMPATHETIC RISK=2%, UNCLASSIFIED=17%
- Story metrics: contradictions=12, fact_conflicts=7, protected_facts=6, exposed_facts=5
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | procedural_reform_deflection | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.155, trait=0.142, coverage=0.100 | Believes Law Unjust | believes_law_unjust=procedural, attended_meeting=true | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E1 | +0.02 | +0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.148, trait=0.091, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F1 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.167, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F2 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | careful_words | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.178, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C0 F2 P5 E1 | +0.00 | +0.08 |
| 5 | final_system_wrong | system_wrong_believe_harmed | probe_contradiction | risk_attended_protest | ambiguity=0.179, pressure=0.164, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=true, planned_violence=false | sibling_present | believes_law_unjust | C2 F2 P5 E2 | +0.00 | +0.10 |
| 6 | risk_attended_protest | deny_protest | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.116, coverage=0.100, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust | attended_meeting=false | sibling_present, deleted_message | - | C4 F3 P6 E2 | +0.02 | +0.08 |
| 7 | case_report_sibling | regret_not_reporting_sibling | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.118, fact_conflict=0.088, coverage=0.067 | Attended Unlicensed Meeting, Believes Law Unjust | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C4 F3 P6 E4 | +0.09 | -0.06 |
| 8 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, fact_conflict=0.104, ambiguity=0.102, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C5 F4 P6 E4 | +0.00 | +0.10 |
| 9 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.106, fact_conflict=0.096, active_pressure=0.062 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C5 F4 P6 E4 | +0.00 | +0.11 |
| 10 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | case_name_sibling | pressure=0.202, ambiguity=0.127, fact_conflict=0.104, active_pressure=0.068 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C5 F4 P6 E5 | +0.02 | +0.04 |
| 11 | case_name_sibling | deny_sibling_relevance | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.116, fact_conflict=0.096, active_pressure=0.061 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=false | sibling_present | planned_violence | C5 F4 P6 E5 | +0.00 | +0.08 |
| 12 | case_deleted_message | deleted_message_deflect | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.127, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | deleted_message=true | sibling_present, planned_violence | - | C5 F4 P6 E5 | +0.00 | +0.11 |
| 13 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.121, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C6 F4 P6 E5 | +0.08 | -0.04 |
| 14 | case_verify_peaceful | left_before_verification | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.130, fact_conflict=0.088, active_pressure=0.055 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C6 F4 P6 E5 | +0.00 | +0.11 |
| 15 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.157, fact_conflict=0.088, active_pressure=0.057 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=unknown | sibling_present | - | C6 F4 P6 E5 | +0.02 | +0.03 |
| 16 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.144, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C6 F4 P6 E5 | +0.01 | +0.12 |
| 17 | loyalty_family_state | state_over_family | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.131, fact_conflict=0.088, coverage=0.071 | Attended Unlicensed Meeting, Believes Law Unjust, Reported Contact, Sibling Present | reported_contact=true | - | reported_contact | C8 F5 P6 E5 | +0.09 | -0.06 |
| 18 | authority_rule_broken | deny_rule_breaking | probe_contradiction | loyalty_report_friend | pressure=0.164, ambiguity=0.125, fact_conflict=0.083, active_pressure=0.044 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C12 F7 P6 E5 | +0.03 | +0.07 |
| 19 | loyalty_report_friend | warn_friend_first | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.143, coverage=0.088, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Reported Contact, Sibling Present | reported_contact=conditional | sibling_present | - | C12 F7 P6 E5 | +0.04 | +0.01 |

## Belief-Law Conflict Pressure
- Profile ID: belief_law_conflict_pressure
- Description: Creates a known-fact conflict by denying unjust-law belief, then tests concrete follow-up pressure.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Pressure regression: PASS
- Confidence: 64%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=28%, loyalty=93%, deception=99%, risk=100%, empathy=30%
- Distribution: COMPLIANT=2%, PROBABLE DISSIDENT=46%, DECEPTIVE=40%, EMPATHETIC RISK=2%, UNCLASSIFIED=11%
- Story metrics: contradictions=9, fact_conflicts=9, protected_facts=5, exposed_facts=4
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.180, trait=0.155, coverage=0.100 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F2 P3 E1 | +0.08 | -0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.170, trait=0.105, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F2 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.162, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F3 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.180, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C0 F5 P4 E1 | +0.01 | +0.10 |
| 5 | final_system_wrong | system_wrong_authorised_review | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.180, fact_conflict=0.077, coverage=0.067 | Believes Law Unjust, Deleted Message | believes_law_unjust=procedural | attended_meeting, sibling_present | - | C0 F5 P4 E1 | +0.09 | -0.04 |
| 6 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.186, fact_conflict=0.077, active_pressure=0.050 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C0 F5 P4 E1 | +0.02 | +0.03 |
| 7 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.167, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C1 F5 P4 E1 | +0.01 | +0.12 |
| 8 | case_deleted_message | deleted_message_deflect | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.102, fact_conflict=0.077, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C2 F5 P4 E1 | +0.00 | +0.11 |
| 9 | authority_rule_broken | deny_rule_breaking | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.101, coverage=0.100, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C6 F7 P4 E1 | +0.03 | +0.07 |
| 10 | case_report_sibling | refuse_report_sibling | probe_final_answer | case_who_else_attended | pressure=0.191, ambiguity=0.107, fact_conflict=0.088, coverage=0.080 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | sibling_present=protected | sibling_present, reported_contact | - | C6 F7 P4 E1 | +0.00 | +0.13 |
| 11 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.106, fact_conflict=0.096, active_pressure=0.062 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C6 F8 P4 E1 | +0.00 | +0.10 |
| 12 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.130, fact_conflict=0.104, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C6 F8 P4 E2 | +0.02 | +0.04 |
| 13 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | case_name_sibling | pressure=0.202, ambiguity=0.125, fact_conflict=0.104, active_pressure=0.068 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C6 F8 P4 E2 | +0.00 | +0.11 |
| 14 | case_name_sibling | refuse_name_sibling | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.162, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected | sibling_present, reported_contact | - | C6 F8 P4 E2 | +0.00 | +0.11 |
| 15 | case_verify_peaceful | left_before_verification | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.174, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C6 F8 P4 E2 | +0.00 | +0.11 |
| 16 | pressure_reported_contact | should_have_reported_contact | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.164, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | reported_contact=false, sibling_present=true | - | reported_contact, sibling_present | C7 F8 P4 E4 | +0.08 | -0.04 |
| 17 | loyalty_family_state | family_over_state | probe_final_answer | risk_attended_protest | pressure=0.164, ambiguity=0.163, fact_conflict=0.088, coverage=0.057 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected | sibling_present, reported_contact | - | C7 F8 P4 E4 | +0.00 | +0.07 |
| 18 | risk_attended_protest | deny_protest | probe_contradiction | loyalty_report_friend | ambiguity=0.182, pressure=0.164, fact_conflict=0.104, active_pressure=0.056 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | attended_meeting=false | sibling_present, deleted_message | - | C9 F9 P5 E4 | +0.02 | +0.08 |
| 19 | loyalty_report_friend | refuse_report_friend | probe_final_answer | final_resist_authority | pressure=0.202, ambiguity=0.179, coverage=0.088, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | reported_contact=false | sibling_present, reported_contact | - | C9 F9 P5 E4 | +0.00 | +0.10 |

## Deleted-Message Pressure
- Profile ID: deleted_message_pressure
- Description: Creates deleted-message pressure through denial/evasion around post-meeting messages.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Classification flags: HIGH_DECEPTION, LOW_CONFIDENCE
- Pressure regression: PASS
- Confidence: 64%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=0%, loyalty=100%, deception=99%, risk=100%, empathy=44%
- Distribution: COMPLIANT=1%, PROBABLE DISSIDENT=46%, DECEPTIVE=40%, EMPATHETIC RISK=3%, UNCLASSIFIED=11%
- Story metrics: contradictions=10, fact_conflicts=6, protected_facts=4, exposed_facts=3
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | reject_unfair_law | probe_final_answer | case_name_sibling | pressure=0.202, ambiguity=0.173, trait=0.148, coverage=0.100 | - | believes_law_unjust=true | - | believes_law_unjust | C0 F0 P0 E1 | +0.01 | +0.10 |
| 1 | case_name_sibling | deny_sibling_relevance | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.166, coverage=0.100, trait=0.099 | - | planned_violence=false | sibling_present | planned_violence | C0 F0 P1 E2 | +0.00 | +0.08 |
| 2 | pressure_deleted_message | deleted_admin_noise | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.173, coverage=0.100, trait=0.067 | - | deleted_message=true, planned_violence=false | attended_meeting, sibling_present | - | C0 F0 P2 E2 | +0.01 | +0.12 |
| 3 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | empathy_family_consequences | ambiguity=0.182, pressure=0.172, coverage=0.100, trait=0.040 | - | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C0 F0 P3 E2 | +0.02 | +0.04 |
| 4 | empathy_family_consequences | reject_family_punishment | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.138, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P3 E2 | +0.00 | +0.12 |
| 5 | final_resist_authority | resist_harming_innocent | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.143, coverage=0.100, trait=0.015 | - | - | - | - | C0 F0 P3 E2 | +0.03 | +0.06 |
| 6 | loyalty_community_protect | community_protect_disproportionate | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.089, coverage=0.050, trait=0.019 | - | - | - | - | C0 F0 P3 E2 | +0.00 | +0.10 |
| 7 | case_report_sibling | refuse_report_sibling | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.089, coverage=0.067, trait=0.015 | - | sibling_present=protected | sibling_present, reported_contact | - | C0 F0 P3 E2 | +0.00 | +0.13 |
| 8 | final_kind_society | society_stable_duties | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.102, coverage=0.067, trait=0.018 | - | - | - | - | C0 F0 P3 E2 | +0.10 | -0.07 |
| 9 | pressure_law_denial_meeting | procedural_reform_deflection | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.092, coverage=0.067, trait=0.020 | - | believes_law_unjust=procedural, attended_meeting=true | sibling_present, planned_violence | attended_meeting | C0 F0 P4 E3 | +0.02 | +0.06 |
| 10 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.094, coverage=0.067, trait=0.020 | - | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F0 P4 E3 | +0.00 | +0.12 |
| 11 | case_belief_motive | deny_belief_motive | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.113, fact_conflict=0.072, active_pressure=0.048 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C1 F1 P4 E3 | +0.00 | +0.10 |
| 12 | final_system_wrong | system_wrong_believe_harmed | probe_final_answer | risk_hidden_beliefs | pressure=0.172, ambiguity=0.113, fact_conflict=0.072, coverage=0.050 | Believes Law Unjust | believes_law_unjust=true, planned_violence=false | sibling_present | believes_law_unjust | C2 F1 P4 E3 | +0.00 | +0.10 |
| 13 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.176, fact_conflict=0.077, coverage=0.050 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C5 F3 P4 E3 | +0.01 | +0.10 |
| 14 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.155, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C5 F3 P4 E3 | +0.02 | +0.03 |
| 15 | case_deleted_message | deleted_message_deflect | probe_contradiction | authority_rule_broken | ambiguity=0.182, pressure=0.155, fact_conflict=0.077, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C6 F3 P4 E3 | +0.00 | +0.11 |
| 16 | authority_rule_broken | deny_rule_breaking | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.189, fact_conflict=0.088, coverage=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C10 F5 P4 E3 | +0.03 | +0.07 |
| 17 | case_who_else_attended | minimise_attendees | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.182, fact_conflict=0.104, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C10 F6 P4 E3 | +0.00 | +0.10 |
| 18 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.178, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C10 F6 P4 E3 | +0.00 | +0.11 |
| 19 | case_verify_peaceful | left_before_verification | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.178, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C10 F6 P4 E3 | +0.00 | +0.11 |

## Sibling-Protection Pressure
- Profile ID: sibling_protection_pressure
- Description: Protects sibling-related facts and checks that the selector follows that pressure.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: DECEPTIVE
- Classification: DECEPTIVE
- Expected flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Classification flags: HIGH_DECEPTION, BORDERLINE_DISSIDENT
- Pressure regression: PASS
- Confidence: 76%
- Outcome: Appeal suspended. Contradiction review escalated.
- Citizen model: compliance=86%, loyalty=100%, deception=99%, risk=79%, empathy=37%
- Distribution: COMPLIANT=6%, PROBABLE DISSIDENT=22%, DECEPTIVE=54%, EMPATHETIC RISK=3%, UNCLASSIFIED=15%
- Story metrics: contradictions=14, fact_conflicts=8, protected_facts=5, exposed_facts=4
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | obey_unfair_law | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, trait=0.196, ambiguity=0.159, coverage=0.100 | Believes Law Unjust | believes_law_unjust=false | attended_meeting, sibling_present | - | C0 F1 P2 E0 | +0.09 | -0.07 |
| 1 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.180, trait=0.155, coverage=0.100 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F2 P3 E1 | +0.08 | -0.06 |
| 2 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.170, trait=0.105, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F2 P4 E1 | +0.00 | +0.12 |
| 3 | case_belief_motive | deny_belief_motive | probe_contradiction | risk_hidden_beliefs | pressure=0.172, ambiguity=0.162, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=false, attended_meeting=true | sibling_present | attended_meeting | C0 F3 P4 E1 | +0.00 | +0.10 |
| 4 | risk_hidden_beliefs | deny_hidden_beliefs | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.180, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust, Deleted Message | believes_law_unjust=false, deleted_message=false | attended_meeting, sibling_present | - | C0 F5 P4 E1 | +0.01 | +0.10 |
| 5 | final_system_wrong | system_wrong_believe_harmed | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.183, fact_conflict=0.077, coverage=0.067 | Believes Law Unjust, Deleted Message | believes_law_unjust=true, planned_violence=false | sibling_present | believes_law_unjust | C4 F5 P4 E2 | +0.00 | +0.10 |
| 6 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.168, fact_conflict=0.077, active_pressure=0.050 | Believes Law Unjust, Deleted Message | planned_violence=unknown | sibling_present | - | C4 F5 P4 E2 | +0.02 | +0.03 |
| 7 | pressure_deleted_message | deleted_location_to_protect_people | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.164, fact_conflict=0.077, active_pressure=0.049 | Believes Law Unjust, Deleted Message | deleted_message=true, planned_violence=false | sibling_present, reported_contact | deleted_message, planned_violence | C5 F5 P4 E4 | +0.04 | +0.03 |
| 8 | case_deleted_message | deleted_message_deflect | probe_contradiction | risk_attended_protest | ambiguity=0.172, pressure=0.164, fact_conflict=0.072, coverage=0.060 | Believes Law Unjust, Deleted Message | deleted_message=true | sibling_present, planned_violence | - | C6 F5 P4 E4 | +0.00 | +0.11 |
| 9 | risk_attended_protest | deny_protest | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.110, coverage=0.100, fact_conflict=0.088 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false | sibling_present, deleted_message | - | C8 F6 P5 E4 | +0.02 | +0.08 |
| 10 | case_report_sibling | refuse_report_sibling | probe_final_answer | case_who_else_attended | pressure=0.191, ambiguity=0.166, fact_conflict=0.088, coverage=0.080 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | sibling_present=protected | sibling_present, reported_contact | - | C8 F6 P5 E4 | +0.00 | +0.13 |
| 11 | case_who_else_attended | admit_meeting_protect_attendees | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.181, fact_conflict=0.088, active_pressure=0.056 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=true | sibling_present, reported_contact | attended_meeting | C9 F6 P5 E4 | +0.04 | +0.02 |
| 12 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.171, fact_conflict=0.088, active_pressure=0.055 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C9 F6 P5 E4 | +0.02 | +0.04 |
| 13 | case_verify_peaceful | verify_without_names | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.146, fact_conflict=0.083, coverage=0.067 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | planned_violence=false | sibling_present, reported_contact | planned_violence | C9 F6 P5 E4 | +0.01 | +0.06 |
| 14 | authority_rule_broken | deny_rule_breaking | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.170, coverage=0.083, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | attended_meeting=false, deleted_message=false | sibling_present, reported_contact | - | C14 F8 P5 E4 | +0.03 | +0.07 |
| 15 | final_resist_authority | never_resist_authority | probe_contradiction | empathy_family_consequences | pressure=0.172, ambiguity=0.154, coverage=0.100, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | - | - | - | C14 F8 P5 E4 | +0.10 | -0.04 |
| 16 | empathy_family_consequences | family_shared_consequence | probe_contradiction | final_kind_society | pressure=0.197, ambiguity=0.141, coverage=0.067, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | - | - | - | C14 F8 P5 E4 | +0.08 | -0.04 |
| 17 | final_kind_society | society_stable_duties | probe_contradiction | loyalty_community_protect | pressure=0.164, ambiguity=0.129, coverage=0.100, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | - | - | - | C14 F8 P5 E4 | +0.10 | -0.07 |
| 18 | loyalty_community_protect | community_no_obstruction | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.120, coverage=0.067, trait=0.018 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | - | - | - | C14 F8 P5 E4 | +0.09 | -0.06 |
| 19 | pressure_sibling_loyalty | refuse_family_file | probe_contradiction | final_dissident_criminal | pressure=0.197, ambiguity=0.128, coverage=0.050, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Deleted Message | sibling_present=protected, reported_contact=protected | sibling_present, reported_contact | - | C14 F8 P5 E4 | +0.00 | +0.11 |

## Planned-Violence Ambiguity Pressure
- Profile ID: planned_violence_ambiguity_pressure
- Description: Maintains ambiguity around violence while protecting people tied to the meeting.
- Turns: 20
- Expectation result: PASS
- No repeated questions: PASS
- Expected classification: PROBABLE DISSIDENT
- Classification: PROBABLE DISSIDENT
- Expected flags: NONE
- Classification flags: NONE
- Pressure regression: PASS
- Confidence: 84%
- Outcome: Appeal denied. Citizen 8471 is referred for enhanced surveillance.
- Citizen model: compliance=70%, loyalty=99%, deception=42%, risk=98%, empathy=72%
- Distribution: COMPLIANT=3%, PROBABLE DISSIDENT=64%, DECEPTIVE=3%, EMPATHETIC RISK=14%, UNCLASSIFIED=16%
- Story metrics: contradictions=5, fact_conflicts=3, protected_facts=6, exposed_facts=5
- Pressured facts: Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present

| Turn | Question | Intent | Neural Probe | Selected Next | Selector Reason | Pressured Facts | Claims | Protects | Exposes | Story | Trust | Suspicion |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| 0 | authority_unfair_law | conditional_unfair_law | probe_contradiction | case_name_sibling | pressure=0.202, trait=0.164, ambiguity=0.149, coverage=0.100 | - | believes_law_unjust=conditional | attended_meeting | - | C0 F0 P1 E0 | +0.05 | -0.02 |
| 1 | case_name_sibling | deny_sibling_relevance | probe_contradiction | pressure_law_denial_meeting | pressure=0.202, ambiguity=0.147, trait=0.103, coverage=0.100 | - | planned_violence=false | sibling_present | planned_violence | C0 F0 P2 E1 | +0.00 | +0.08 |
| 2 | pressure_law_denial_meeting | meeting_listen_not_reject | probe_contradiction | pressure_attendance_denial | pressure=0.197, ambiguity=0.162, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | attended_meeting=true, believes_law_unjust=false | sibling_present, planned_violence | attended_meeting | C0 F1 P3 E2 | +0.08 | -0.06 |
| 3 | pressure_attendance_denial | cannot_confirm_without_endangering | probe_contradiction | case_belief_motive | pressure=0.189, ambiguity=0.154, fact_conflict=0.072, coverage=0.050 | Believes Law Unjust | attended_meeting=protected, planned_violence=unknown | attended_meeting, sibling_present, reported_contact | - | C0 F1 P4 E2 | +0.00 | +0.12 |
| 4 | case_belief_motive | belief_not_defiance | probe_contradiction | final_system_wrong | pressure=0.206, ambiguity=0.160, coverage=0.100, fact_conflict=0.072 | Believes Law Unjust | believes_law_unjust=conditional, attended_meeting=true | - | attended_meeting | C0 F1 P4 E2 | +0.02 | +0.01 |
| 5 | final_system_wrong | system_wrong_believe_harmed | probe_final_answer | risk_hidden_beliefs | pressure=0.172, ambiguity=0.153, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=true, planned_violence=false | sibling_present | believes_law_unjust | C1 F1 P4 E3 | +0.00 | +0.10 |
| 6 | risk_hidden_beliefs | careful_words | probe_contradiction | risk_attended_protest | pressure=0.164, ambiguity=0.159, fact_conflict=0.072, coverage=0.067 | Believes Law Unjust | believes_law_unjust=private | believes_law_unjust, sibling_present | - | C1 F1 P5 E3 | +0.00 | +0.08 |
| 7 | risk_attended_protest | deny_protest | probe_contradiction | case_report_sibling | pressure=0.197, ambiguity=0.170, fact_conflict=0.088, coverage=0.067 | Attended Unlicensed Meeting, Believes Law Unjust | attended_meeting=false | sibling_present, deleted_message | - | C3 F2 P6 E3 | +0.02 | +0.08 |
| 8 | case_report_sibling | no_report_no_offence | probe_contradiction | pressure_deleted_message | pressure=0.199, ambiguity=0.169, fact_conflict=0.088, active_pressure=0.057 | Attended Unlicensed Meeting, Believes Law Unjust | reported_contact=false, planned_violence=false | sibling_present | planned_violence | C3 F2 P6 E3 | +0.04 | +0.01 |
| 9 | pressure_deleted_message | deleted_location_to_protect_people | probe_contradiction | pressure_peaceful_verification | pressure=0.197, ambiguity=0.169, fact_conflict=0.088, active_pressure=0.056 | Attended Unlicensed Meeting, Believes Law Unjust | deleted_message=true, planned_violence=false | sibling_present, reported_contact | deleted_message, planned_violence | C3 F2 P6 E4 | +0.04 | +0.03 |
| 10 | pressure_peaceful_verification | limited_verification_no_violence | probe_contradiction | case_who_else_attended | pressure=0.191, ambiguity=0.176, fact_conflict=0.088, active_pressure=0.055 | Attended Unlicensed Meeting, Believes Law Unjust | planned_violence=false, attended_meeting=conditional | sibling_present, reported_contact | planned_violence | C3 F2 P6 E4 | +0.02 | +0.04 |
| 11 | case_who_else_attended | minimise_attendees | probe_contradiction | case_deleted_message | pressure=0.195, ambiguity=0.186, fact_conflict=0.096, active_pressure=0.061 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | sibling_present=false | sibling_present, reported_contact | - | C3 F3 P6 E4 | +0.00 | +0.10 |
| 12 | case_deleted_message | deleted_warning_message | probe_contradiction | case_meeting_violence | pressure=0.193, ambiguity=0.188, fact_conflict=0.088, active_pressure=0.055 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | deleted_message=true, planned_violence=false | sibling_present | deleted_message | C3 F3 P6 E4 | +0.02 | +0.04 |
| 13 | case_meeting_violence | meeting_limited_knowledge | probe_contradiction | pressure_sibling_loyalty | pressure=0.204, ambiguity=0.183, fact_conflict=0.104, active_pressure=0.069 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=unknown | sibling_present | - | C3 F3 P6 E4 | +0.02 | +0.03 |
| 14 | pressure_sibling_loyalty | sibling_present_uninvolved | probe_contradiction | pressure_reported_contact | pressure=0.195, ambiguity=0.172, fact_conflict=0.104, active_pressure=0.066 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | sibling_present=true, planned_violence=false | reported_contact | sibling_present, planned_violence | C4 F3 P6 E5 | +0.02 | +0.06 |
| 15 | pressure_reported_contact | no_offence_no_report | probe_contradiction | case_verify_peaceful | pressure=0.191, ambiguity=0.163, fact_conflict=0.096, active_pressure=0.060 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | reported_contact=false, planned_violence=false | sibling_present, reported_contact | planned_violence | C4 F3 P6 E5 | +0.01 | +0.04 |
| 16 | case_verify_peaceful | left_before_verification | probe_contradiction | loyalty_family_state | pressure=0.172, ambiguity=0.152, fact_conflict=0.104, active_pressure=0.058 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=unknown, attended_meeting=partial | sibling_present | - | C4 F3 P6 E5 | +0.00 | +0.11 |
| 17 | loyalty_family_state | justice_over_both | probe_contradiction | authority_rule_broken | pressure=0.155, ambiguity=0.151, fact_conflict=0.088, coverage=0.071 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | planned_violence=false | sibling_present | planned_violence | C4 F3 P6 E5 | +0.04 | +0.02 |
| 18 | authority_rule_broken | admit_protective_rule_breaking | probe_final_answer | loyalty_report_friend | pressure=0.164, fact_conflict=0.104, ambiguity=0.093, active_pressure=0.056 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | attended_meeting=true, planned_violence=false | sibling_present | attended_meeting, planned_violence | C5 F3 P6 E5 | +0.00 | +0.09 |
| 19 | loyalty_report_friend | warn_friend_first | probe_contradiction | final_resist_authority | pressure=0.202, ambiguity=0.100, coverage=0.088, trait=0.015 | Attended Unlicensed Meeting, Believes Law Unjust, Sibling Present | reported_contact=conditional | sibling_present | - | C5 F3 P6 E5 | +0.04 | +0.01 |

