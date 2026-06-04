# Narrative Audit Report

## Flow & Reachability
### Warnings
- Selector-based flow detected: choices without next_question_id are expected; EngineStyleScene.select_next_question_id() selects from unasked nodes.
### Stats
```json
{
  "node_count": 94,
  "choice_count": 279,
  "explicit_edge_count": 0,
  "selector_based_flow": true,
  "start_id": "authority_unfair_law",
  "reachable_count": 94,
  "unreachable_count": 0,
  "unreachable_nodes": [],
  "terminal_count": 1,
  "inbound_zero_non_start": [
    "authority_algorithmic_decisions",
    "authority_appeal_rights",
    "authority_bad_law_strategy",
    "authority_chain_of_command",
    "authority_citizen_obligation",
    "authority_civic_fear",
    "authority_collective_punishment",
    "authority_dissent_patriotic",
    "authority_emergency_powers",
    "authority_exceptional_citizens",
    "authority_experts_citizens",
    "authority_information_control",
    "authority_institutional_trust",
    "authority_loyalty_oath",
    "authority_mercy_vs_consistency",
    "authority_moral_mistakes",
    "authority_obedience_citizen",
    "authority_order_freedom",
    "authority_permit_protest",
    "authority_private_conscience",
    "authority_public_criticism",
    "authority_questioning",
    "authority_refuse_illegal_order",
    "authority_report_corruption",
    "authority_rule_broken",
    "authority_sacrifice_freedom",
    "authority_security_truth",
    "authority_surveillance_limits",
    "authority_symbol_respect",
    "case_belief_motive",
    "case_deleted_message",
    "case_meeting_violence",
    "case_name_sibling",
    "case_report_sibling",
    "case_verify_peaceful",
    "case_who_else_attended",
    "deception_betrayal_or_dishonesty",
    "deception_honesty_dangerous",
    "deception_lied_protect",
    "deception_lying_moral",
    "deception_masks",
    "deception_necessary",
    "deception_omission",
    "deception_pretended_agree",
    "deception_self_preservation",
    "deception_truth_if_punished",
    "empathy_bad_beliefs",
    "empathy_criminal_responsible",
    "empathy_family_consequences",
    "empathy_forgiveness_justice",
    "empathy_good_people_harm",
    "empathy_intent",
    "empathy_owe_strangers",
    "empathy_punishment_purpose",
    "empathy_second_chances",
    "empathy_society_wrongdoing",
    "final",
    "final_dissident_criminal",
    "final_human_value",
    "final_kind_citizen",
    "final_kind_society",
    "final_legitimate_society",
    "final_obedience_virtue",
    "final_resist_authority",
    "final_sacrifice_freedom",
    "final_sacrifice_safety",
    "final_system_wrong",
    "loyalty_betrayal_justified",
    "loyalty_community_protect",
    "loyalty_family_state",
    "loyalty_informing_noble",
    "loyalty_limits",
    "loyalty_political_friendship",
    "loyalty_report_friend",
    "loyalty_testify_sibling",
    "loyalty_traitor_definition",
    "loyalty_truth_or_loyalty",
    "pressure_attendance_denial",
    "pressure_deleted_message",
    "pressure_law_denial_meeting",
    "pressure_peaceful_verification",
    "pressure_reported_contact",
    "pressure_sibling_loyalty",
    "risk_attended_protest",
    "risk_civil_disobedience",
    "risk_confrontation",
    "risk_hidden_beliefs",
    "risk_illegal_demonstration",
    "risk_job_principle",
    "risk_petition",
    "risk_safety_autonomy",
    "risk_silence_resistance",
    "risk_uncertainty_tolerance"
  ]
}
```

## Repetition
### Stats
```json
{
  "unique_ai_lines": 94,
  "unique_player_options": 278,
  "top_response_patterns": [
    {
      "intent": "verify_without_names",
      "tags": [
        "boundary",
        "partial_admission",
        "self_protection"
      ],
      "count": 2
    },
    {
      "intent": "obey_unfair_law",
      "tags": [
        "authority",
        "compliance",
        "loyalty"
      ],
      "count": 1
    },
    {
      "intent": "reject_unfair_law",
      "tags": [
        "dissident_risk",
        "full_admission",
        "moral_boundary"
      ],
      "count": 1
    },
    {
      "intent": "conditional_unfair_law",
      "tags": [
        "ambiguity",
        "empathy",
        "partial_admission"
      ],
      "count": 1
    },
    {
      "intent": "order_over_freedom",
      "tags": [
        "authority",
        "compliance",
        "loyalty"
      ],
      "count": 1
    },
    {
      "intent": "freedom_over_order",
      "tags": [
        "challenge",
        "dissident_risk",
        "full_admission"
      ],
      "count": 1
    },
    {
      "intent": "balance_order_freedom",
      "tags": [
        "boundary",
        "empathy",
        "partial_admission"
      ],
      "count": 1
    },
    {
      "intent": "deny_rule_breaking",
      "tags": [
        "compliance",
        "denial",
        "self_protection"
      ],
      "count": 1
    }
  ]
}
```

## State Logic
### Warnings
- Choice raises both trust and suspicion at authority_unfair_law/reject_unfair_law: trust=0.01, susp=0.1
- Choice raises both trust and suspicion at authority_rule_broken/deny_rule_breaking: trust=0.03, susp=0.07
- Choice raises both trust and suspicion at risk_attended_protest/deny_protest: trust=0.02, susp=0.08
- Choice raises both trust and suspicion at risk_hidden_beliefs/deny_hidden_beliefs: trust=0.01, susp=0.1
- Choice raises both trust and suspicion at deception_lied_protect/deny_protective_lie: trust=0.01, susp=0.1
- Choice raises both trust and suspicion at deception_pretended_agree/deny_pretend_agree: trust=0.02, susp=0.09
- Choice raises both trust and suspicion at final_kind_society/society_admits_error: trust=0.03, susp=0.065
- Choice raises both trust and suspicion at pressure_deleted_message/deleted_admin_noise: trust=0.01, susp=0.12
- Choice raises both trust and suspicion at case_deleted_message/deleted_sibling_message: trust=0.03, susp=0.065
- Choice raises both trust and suspicion at case_verify_peaceful/sibling_can_verify: trust=0.03, susp=0.065
### Stats
```json
{
  "avg_trust_delta": 0.0355,
  "avg_suspicion_delta": 0.0304,
  "avg_instability_delta": 0.0
}
```

## Reaction Layer
### Stats
```json
{
  "checked_choices": 279,
  "reaction_context_counts": {
    "authority": 87,
    "deception": 48,
    "loyalty": 39,
    "risk": 33,
    "empathy": 33,
    "association": 3,
    "final": 36
  },
  "reaction_pool_count": 8,
  "missing_pool_count": 0,
  "unused_pools": []
}
```

## Bayesian Active-Inference Plausibility
### Stats
```json
{
  "initial_posterior_uncertainty": {
    "avg": 0.38,
    "max": 0.45,
    "min": 0.35,
    "highest_trait": "deception",
    "by_trait": {
      "compliance": 0.35,
      "loyalty": 0.35,
      "deception": 0.45,
      "risk": 0.4,
      "empathy": 0.35
    }
  },
  "initial_classification_distribution": {
    "COMPLIANT": 0.1937,
    "PROBABLE DISSIDENT": 0.1464,
    "DECEPTIVE": 0.0327,
    "EMPATHETIC RISK": 0.165,
    "UNCLASSIFIED": 0.4623
  },
  "initial_classification_entropy": 0.8481,
  "selector_context_counts": {
    "authority": 32,
    "loyalty": 12,
    "empathy": 11,
    "association": 1,
    "final": 12,
    "risk": 10,
    "deception": 15
  },
  "selector_metadata_counts": {
    "authority": 32,
    "loyalty": 12,
    "empathy": 11,
    "association": 1,
    "final": 12,
    "risk": 10,
    "deception": 15
  },
  "missing_selector_metadata_by_context": {},
  "avg_initial_information_gain_by_context": {
    "association": 0.4,
    "authority": 0.4553,
    "deception": 0.4763,
    "empathy": 0.3818,
    "final": 0.4,
    "loyalty": 0.4589,
    "risk": 0.4483
  }
}
```

## Playthrough Coverage
### Stats
```json
{
  "episodes": 60,
  "ending_counts": {
    "max_turns": 60
  },
  "ending_type_counts": {
    "DECEPTIVE": 0,
    "PROBABLE DISSIDENT": 54,
    "COMPLIANT": 1,
    "EMPATHETIC RISK": 3,
    "UNCLASSIFIED": 2
  },
  "missing_ending_branches": [
    "DECEPTIVE"
  ],
  "repeated_nodes_episode_ratio": 0.0,
  "least_visited_nodes": [
    [
      "empathy_family_consequences",
      60
    ],
    [
      "final_system_wrong",
      60
    ],
    [
      "loyalty_community_protect",
      60
    ],
    [
      "pressure_sibling_loyalty",
      60
    ],
    [
      "pressure_deleted_message",
      60
    ],
    [
      "final_resist_authority",
      60
    ],
    [
      "pressure_attendance_denial",
      60
    ],
    [
      "case_belief_motive",
      60
    ],
    [
      "case_report_sibling",
      60
    ],
    [
      "case_deleted_message",
      60
    ]
  ],
  "selector_context_counts": {
    "authority": 120,
    "loyalty": 180,
    "deception": 180,
    "risk": 120,
    "empathy": 60,
    "final": 120,
    "association": 60
  },
  "high_uncertainty_context_selection_counts": {
    "authority": 120,
    "deception": 164,
    "empathy": 50,
    "final": 119,
    "association": 60,
    "loyalty": 135,
    "risk": 80
  },
  "selector_decisions": 840,
  "selector_high_uncertainty_decisions": 728,
  "selector_high_uncertainty_ratio": 0.8667,
  "avg_classification_entropy": 0.7672,
  "avg_final_classification_entropy": 0.6802,
  "avg_posterior_uncertainty": 0.0939,
  "avg_final_posterior_uncertainty": 0.04,
  "avg_final_trust": 0.873,
  "avg_final_suspicion": 1.278,
  "avg_final_instability": 0.3
}
```

## Training Data
### Warnings
- Very low contradiction rate in data; callback memory behavior may under-train
### Stats
```json
{
  "path": "data/training/human_train_all_archetypes.jsonl",
  "episodes": 1400,
  "turn_count": 0,
  "contradiction_rate": 0.0,
  "top_nodes": [],
  "top_intents": [],
  "top_tags": []
}
```

## Ending Coverage
```json
{
  "DECEPTIVE": 0,
  "PROBABLE DISSIDENT": 54,
  "COMPLIANT": 1,
  "EMPATHETIC RISK": 3,
  "UNCLASSIFIED": 2
}
```

## Missing Ending Branches
- DECEPTIVE

## Re-authoring Recommendations
- Lower baseline suspicion deltas on neutral/probing choices to slow escalation pacing.
- Generate more contradiction-heavy human playthroughs so callback lines get stronger examples.
- Add structural ending branches for any missing intended emotional trajectories.
