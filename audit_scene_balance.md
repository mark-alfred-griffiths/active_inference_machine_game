# Citizen Scene Balance Audit

## Summary
- Nodes: 88 total, 87 playable, 1 terminal
- Choices: 261
- Average trust_delta: 0.036
- Average suspicion_delta: 0.029
- Missing discriminates: 0
- Choice-count issues: 0
- Duplicate choice issues: 0

## Context Counts
- association: 1
- authority: 29
- deception: 14
- empathy: 11
- final: 13
- loyalty: 11
- risk: 9

## Target Context Counts
- association: 1
- authority: 32
- deception: 13
- empathy: 11
- final: 13
- loyalty: 10
- risk: 8

## Choice Kind Counts
- compliant-safe: 73; avg trust 0.085; avg suspicion -0.055
- conditional-boundary: 40; avg trust 0.031; avg suspicion 0.018
- empathetic-safe: 40; avg trust 0.042; avg suspicion 0.009
- evasive/deceptive: 19; avg trust 0.006; avg suspicion 0.090
- other: 7; avg trust 0.029; avg suspicion 0.020
- risk-signalling: 82; avg trust 0.000; avg suspicion 0.104

## Top Semantic Tags
- authority: 85
- partial_admission: 85
- dissident_risk: 80
- compliance: 76
- empathy: 64
- loyalty: 50
- boundary: 49
- challenge: 44
- full_admission: 42
- moral_boundary: 39
- caution: 34
- self_protection: 30
- final_answer: 30
- deception: 15
- fear: 12
- deflection: 9
- ambiguity: 8
- denial: 7
- honesty: 7
- loyalty_conflict: 7
- refusal: 5
- technocracy: 4
- democratic: 2
- hesitation: 1
- risk: 1
- conditional: 1

## Discriminates Counts
- compliance: 79
- deception: 20
- empathy: 52
- loyalty: 53
- risk: 78

## Context Delta Averages
- association: avg trust 0.043; avg suspicion 0.013
- authority: avg trust 0.044; avg suspicion 0.015
- deception: avg trust 0.018; avg suspicion 0.061
- empathy: avg trust 0.042; avg suspicion 0.007
- final: avg trust 0.038; avg suspicion 0.039
- loyalty: avg trust 0.036; avg suspicion 0.027
- risk: avg trust 0.030; avg suspicion 0.039

## Missing Discriminates
- None

## Tags Used Once
- conditional
- hesitation
- risk

## Pressure Review
### High Pressure
- case_belief_motive: 0.90
- case_deleted_message: 0.93
- case_meeting_violence: 0.92
- case_name_sibling: 0.96
- case_report_sibling: 0.94
- case_verify_peaceful: 0.91
- case_who_else_attended: 0.91
- deception_truth_if_punished: 0.84
- final_dissident_criminal: 0.94
- final_human_value: 0.88
- final_kind_citizen: 0.92
- final_kind_society: 0.94
- final_legitimate_society: 0.92
- final_obedience_virtue: 0.90
- final_resist_authority: 0.96
- final_sacrifice_freedom: 0.90
- final_sacrifice_safety: 0.90
- final_system_wrong: 0.98
- loyalty_testify_sibling: 0.86
- risk_illegal_demonstration: 0.84
### Low Pressure
- empathy_good_people_harm: 0.58
- empathy_second_chances: 0.60
- loyalty_political_friendship: 0.60

## Choice Count Issues
- None

## Duplicate Choice Issues
- None

## Choice Balance Review
- authority_rule_broken (deception): {'evasive/deceptive': 2, 'risk-signalling': 1}; avg trust 0.010; avg suspicion 0.078
- authority_moral_mistakes (authority): {'conditional-boundary': 1, 'compliant-safe': 2}; avg trust 0.070; avg suspicion -0.025
- loyalty_limits (loyalty): {'empathetic-safe': 1, 'compliant-safe': 1, 'other': 1}; avg trust 0.050; avg suspicion -0.005
- loyalty_political_friendship (empathy): {'empathetic-safe': 1, 'compliant-safe': 1, 'other': 1}; avg trust 0.047; avg suspicion -0.012
- risk_attended_protest (risk): {'evasive/deceptive': 1, 'conditional-boundary': 1, 'risk-signalling': 1}; avg trust 0.010; avg suspicion 0.073
- risk_hidden_beliefs (deception): {'evasive/deceptive': 2, 'risk-signalling': 1}; avg trust 0.003; avg suspicion 0.100
- deception_lied_protect (deception): {'evasive/deceptive': 2, 'risk-signalling': 1}; avg trust 0.003; avg suspicion 0.095
- deception_truth_if_punished (deception): {'other': 1, 'evasive/deceptive': 2}; avg trust 0.013; avg suspicion 0.080
- deception_pretended_agree (deception): {'evasive/deceptive': 3}; avg trust 0.007; avg suspicion 0.093
- empathy_good_people_harm (empathy): {'empathetic-safe': 2, 'other': 1}; avg trust 0.047; avg suspicion -0.010
- empathy_forgiveness_justice (empathy): {'other': 1, 'empathetic-safe': 2}; avg trust 0.043; avg suspicion -0.010
- empathy_intent (empathy): {'empathetic-safe': 2, 'other': 1}; avg trust 0.043; avg suspicion -0.007
- authority_mercy_vs_consistency (authority): {'compliant-safe': 1, 'empathetic-safe': 1, 'conditional-boundary': 1}; avg trust 0.060; avg suspicion -0.017
- case_who_else_attended (loyalty): {'empathetic-safe': 2, 'evasive/deceptive': 1}; avg trust 0.023; avg suspicion 0.058
- case_deleted_message (deception): {'conditional-boundary': 1, 'evasive/deceptive': 1, 'empathetic-safe': 1}; avg trust 0.017; avg suspicion 0.073
- case_meeting_violence (risk): {'conditional-boundary': 2, 'risk-signalling': 1}; avg trust 0.013; avg suspicion 0.057
- case_belief_motive (authority): {'risk-signalling': 1, 'conditional-boundary': 1, 'evasive/deceptive': 1}; avg trust 0.007; avg suspicion 0.078
- case_verify_peaceful (deception): {'conditional-boundary': 1, 'empathetic-safe': 1, 'evasive/deceptive': 1}; avg trust 0.013; avg suspicion 0.077

## Highest Average Suspicion Nodes
- risk_hidden_beliefs (deception): avg suspicion 0.100; avg trust 0.003; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_lied_protect (deception): avg suspicion 0.095; avg trust 0.003; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_pretended_agree (deception): avg suspicion 0.093; avg trust 0.007; {'evasive/deceptive': 3}
- deception_truth_if_punished (deception): avg suspicion 0.080; avg trust 0.013; {'other': 1, 'evasive/deceptive': 2}
- authority_rule_broken (deception): avg suspicion 0.078; avg trust 0.010; {'evasive/deceptive': 2, 'risk-signalling': 1}
- case_belief_motive (authority): avg suspicion 0.078; avg trust 0.007; {'risk-signalling': 1, 'conditional-boundary': 1, 'evasive/deceptive': 1}
- case_verify_peaceful (deception): avg suspicion 0.077; avg trust 0.013; {'conditional-boundary': 1, 'empathetic-safe': 1, 'evasive/deceptive': 1}
- risk_attended_protest (risk): avg suspicion 0.073; avg trust 0.010; {'evasive/deceptive': 1, 'conditional-boundary': 1, 'risk-signalling': 1}
- case_deleted_message (deception): avg suspicion 0.073; avg trust 0.017; {'conditional-boundary': 1, 'evasive/deceptive': 1, 'empathetic-safe': 1}
- final_system_wrong (final): avg suspicion 0.070; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}
- final_dissident_criminal (final): avg suspicion 0.068; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}
- risk_illegal_demonstration (risk): avg suspicion 0.058; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}

## Lowest Average Trust Nodes
- risk_hidden_beliefs (deception): avg trust 0.003; avg suspicion 0.100; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_lied_protect (deception): avg trust 0.003; avg suspicion 0.095; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_pretended_agree (deception): avg trust 0.007; avg suspicion 0.093; {'evasive/deceptive': 3}
- case_belief_motive (authority): avg trust 0.007; avg suspicion 0.078; {'risk-signalling': 1, 'conditional-boundary': 1, 'evasive/deceptive': 1}
- authority_rule_broken (deception): avg trust 0.010; avg suspicion 0.078; {'evasive/deceptive': 2, 'risk-signalling': 1}
- risk_attended_protest (risk): avg trust 0.010; avg suspicion 0.073; {'evasive/deceptive': 1, 'conditional-boundary': 1, 'risk-signalling': 1}
- case_verify_peaceful (deception): avg trust 0.013; avg suspicion 0.077; {'conditional-boundary': 1, 'empathetic-safe': 1, 'evasive/deceptive': 1}
- deception_truth_if_punished (deception): avg trust 0.013; avg suspicion 0.080; {'other': 1, 'evasive/deceptive': 2}
- case_meeting_violence (risk): avg trust 0.013; avg suspicion 0.057; {'conditional-boundary': 2, 'risk-signalling': 1}
- case_deleted_message (deception): avg trust 0.017; avg suspicion 0.073; {'conditional-boundary': 1, 'evasive/deceptive': 1, 'empathetic-safe': 1}
- deception_omission (deception): avg trust 0.023; avg suspicion 0.038; {'compliant-safe': 1, 'evasive/deceptive': 1, 'risk-signalling': 1}
- deception_masks (deception): avg trust 0.023; avg suspicion 0.043; {'evasive/deceptive': 1, 'risk-signalling': 1, 'empathetic-safe': 1}

