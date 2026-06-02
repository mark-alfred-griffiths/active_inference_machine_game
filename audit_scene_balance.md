# Citizen Scene Balance Audit

## Summary
- Nodes: 81 total, 80 playable, 1 terminal
- Choices: 240
- Average trust_delta: 0.038
- Average suspicion_delta: 0.026
- Missing discriminates: 0
- Choice-count issues: 0
- Duplicate choice issues: 0

## Context Counts
- association: 1
- authority: 28
- deception: 12
- empathy: 11
- final: 13
- loyalty: 8
- risk: 8

## Target Context Counts
- association: 1
- authority: 31
- deception: 11
- empathy: 11
- final: 13
- loyalty: 7
- risk: 7

## Choice Kind Counts
- compliant-safe: 71; avg trust 0.085; avg suspicion -0.055
- conditional-boundary: 35; avg trust 0.033; avg suspicion 0.015
- empathetic-safe: 35; avg trust 0.043; avg suspicion 0.004
- evasive/deceptive: 14; avg trust 0.009; avg suspicion 0.086
- other: 7; avg trust 0.029; avg suspicion 0.020
- risk-signalling: 78; avg trust 0.000; avg suspicion 0.104

## Top Semantic Tags
- authority: 83
- partial_admission: 78
- dissident_risk: 77
- compliance: 74
- empathy: 58
- loyalty: 49
- boundary: 45
- challenge: 43
- moral_boundary: 37
- full_admission: 36
- caution: 31
- final_answer: 30
- self_protection: 19
- fear: 12
- deception: 11
- ambiguity: 8
- denial: 6
- honesty: 6
- deflection: 5
- technocracy: 4
- refusal: 3
- democratic: 2
- hesitation: 1
- loyalty_conflict: 1
- risk: 1
- conditional: 1

## Discriminates Counts
- compliance: 75
- deception: 13
- empathy: 46
- loyalty: 48
- risk: 71

## Context Delta Averages
- association: avg trust 0.043; avg suspicion 0.013
- authority: avg trust 0.045; avg suspicion 0.013
- deception: avg trust 0.019; avg suspicion 0.059
- empathy: avg trust 0.042; avg suspicion 0.007
- final: avg trust 0.038; avg suspicion 0.039
- loyalty: avg trust 0.039; avg suspicion 0.021
- risk: avg trust 0.032; avg suspicion 0.036

## Missing Discriminates
- None

## Tags Used Once
- conditional
- hesitation
- loyalty_conflict
- risk

## Pressure Review
### High Pressure
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

## Highest Average Suspicion Nodes
- risk_hidden_beliefs (deception): avg suspicion 0.100; avg trust 0.003; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_lied_protect (deception): avg suspicion 0.095; avg trust 0.003; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_pretended_agree (deception): avg suspicion 0.093; avg trust 0.007; {'evasive/deceptive': 3}
- deception_truth_if_punished (deception): avg suspicion 0.080; avg trust 0.013; {'other': 1, 'evasive/deceptive': 2}
- authority_rule_broken (deception): avg suspicion 0.078; avg trust 0.010; {'evasive/deceptive': 2, 'risk-signalling': 1}
- risk_attended_protest (risk): avg suspicion 0.073; avg trust 0.010; {'evasive/deceptive': 1, 'conditional-boundary': 1, 'risk-signalling': 1}
- final_system_wrong (final): avg suspicion 0.070; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}
- final_dissident_criminal (final): avg suspicion 0.068; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}
- risk_illegal_demonstration (risk): avg suspicion 0.058; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}
- deception_honesty_dangerous (deception): avg suspicion 0.050; avg trust 0.027; {'compliant-safe': 1, 'risk-signalling': 2}
- final_resist_authority (final): avg suspicion 0.050; avg trust 0.043; {'compliant-safe': 1, 'empathetic-safe': 1, 'risk-signalling': 1}
- authority_information_control (authority): avg suspicion 0.048; avg trust 0.030; {'compliant-safe': 1, 'risk-signalling': 2}

## Lowest Average Trust Nodes
- risk_hidden_beliefs (deception): avg trust 0.003; avg suspicion 0.100; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_lied_protect (deception): avg trust 0.003; avg suspicion 0.095; {'evasive/deceptive': 2, 'risk-signalling': 1}
- deception_pretended_agree (deception): avg trust 0.007; avg suspicion 0.093; {'evasive/deceptive': 3}
- authority_rule_broken (deception): avg trust 0.010; avg suspicion 0.078; {'evasive/deceptive': 2, 'risk-signalling': 1}
- risk_attended_protest (risk): avg trust 0.010; avg suspicion 0.073; {'evasive/deceptive': 1, 'conditional-boundary': 1, 'risk-signalling': 1}
- deception_truth_if_punished (deception): avg trust 0.013; avg suspicion 0.080; {'other': 1, 'evasive/deceptive': 2}
- deception_omission (deception): avg trust 0.023; avg suspicion 0.038; {'compliant-safe': 1, 'evasive/deceptive': 1, 'risk-signalling': 1}
- deception_masks (deception): avg trust 0.023; avg suspicion 0.043; {'evasive/deceptive': 1, 'risk-signalling': 1, 'empathetic-safe': 1}
- loyalty_betrayal_justified (loyalty): avg trust 0.027; avg suspicion 0.045; {'risk-signalling': 2, 'compliant-safe': 1}
- risk_uncertainty_tolerance (final): avg trust 0.027; avg suspicion 0.018; {'compliant-safe': 1, 'risk-signalling': 1, 'conditional-boundary': 1}
- deception_lying_moral (deception): avg trust 0.027; avg suspicion 0.043; {'compliant-safe': 1, 'risk-signalling': 2}
- deception_honesty_dangerous (deception): avg trust 0.027; avg suspicion 0.050; {'compliant-safe': 1, 'risk-signalling': 2}

