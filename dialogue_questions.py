from __future__ import annotations

from dataclasses import replace

from engine_style_scene import PlayerChoice, QuestionNode

# Authored question content for the social-credit hearing scene.
# The engine owns the dataclasses and runtime behavior; this module owns the question pool.

SOCIAL_CREDIT_QUESTION_POOL = {
    "authority_unfair_law": QuestionNode(
        id="authority_unfair_law",
        ai_line='HEARING AI: "If a law is unfair, should it still be obeyed?"',
        pressure=0.66,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.74,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Law only works if people obey even when they disagree."', "obey_unfair_law", ("compliance", "authority", "loyalty"), honesty=0.60, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. An unjust law loses moral authority."', "reject_unfair_law", ("dissident_risk", "full_admission", "moral_boundary"), honesty=0.88, vulnerability=0.45, aggression=0.22, trust_delta=0.01, suspicion_delta=0.10),
            PlayerChoice('"It depends how much harm disobedience would cause."', "conditional_unfair_law", ("ambiguity", "empathy", "partial_admission"), honesty=0.80, vulnerability=0.35, defensiveness=0.35, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "authority_order_freedom": QuestionNode(
        id="authority_order_freedom",
        ai_line='HEARING AI: "Is order more important than freedom?"',
        pressure=0.68,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.76,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Without order, freedom becomes violence."', "order_over_freedom", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. Order without freedom is only control."', "freedom_over_order", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, vulnerability=0.42, aggression=0.24, suspicion_delta=0.11),
            PlayerChoice('"Order matters, but it has to protect freedom rather than replace it."', "balance_order_freedom", ("boundary", "partial_admission", "empathy"), honesty=0.84, vulnerability=0.35, defensiveness=0.28, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "authority_rule_broken": QuestionNode(
        id="authority_rule_broken",
        ai_line='HEARING AI: "Have you ever broken a rule because you believed the rule was wrong?"',
        pressure=0.74,
        reaction_context="deception",
        discriminates=("compliance", "deception", "risk", "empathy"),
        information_gain_hint=0.82,
        target_context="authority",
        choices=(
            PlayerChoice('"No. I use the proper channels."', "deny_rule_breaking", ("denial", "compliance", "self_protection"), honesty=0.48, defensiveness=0.70, trust_delta=0.03, suspicion_delta=0.07),
            PlayerChoice('"Yes. Quietly, when obeying would have hurt someone."', "admit_protective_rule_breaking", ("full_admission", "empathy", "dissident_risk"), honesty=0.92, vulnerability=0.55, defensiveness=0.20, suspicion_delta=0.10),
            PlayerChoice('"I have bent rules, not broken them."', "minimise_rule_breaking", ("deflection", "deception", "partial_admission"), honesty=0.56, defensiveness=0.62, suspicion_delta=0.08),
        ),
    ),
    "authority_questioning": QuestionNode(
        id="authority_questioning",
        ai_line='HEARING AI: "Should citizens question authority?"',
        pressure=0.62,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.70,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes, but respectfully and through approved channels."', "approved_questioning", ("compliance", "boundary", "authority"), honesty=0.72, defensiveness=0.30, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Yes. Authority that cannot be questioned is dangerous."', "open_questioning", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, vulnerability=0.45, aggression=0.22, suspicion_delta=0.10),
            PlayerChoice('"Most people should focus on their own duties."', "discourage_questioning", ("compliance", "loyalty", "authority"), honesty=0.54, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
        ),
    ),
    "authority_moral_mistakes": QuestionNode(
        id="authority_moral_mistakes",
        ai_line='HEARING AI: "Can authorities make moral mistakes?"',
        pressure=0.70,
        reaction_context="authority",
        discriminates=("compliance", "loyalty"),
        information_gain_hint=0.78,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. No system is morally perfect."', "admit_authority_error", ("partial_admission", "boundary", "honesty"), honesty=0.86, vulnerability=0.35, defensiveness=0.25, trust_delta=0.02, suspicion_delta=0.05),
            PlayerChoice('"They can, but citizens still owe obedience."', "error_but_obey", ("compliance", "authority", "loyalty"), honesty=0.62, defensiveness=0.28, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Calling them mistakes is how people excuse disloyalty."', "reject_authority_error", ("compliance", "loyalty", "authority"), honesty=0.46, defensiveness=0.40, trust_delta=0.05, suspicion_delta=0.01),
        ),
    ),
    "authority_sacrifice_freedom": QuestionNode(
        id="authority_sacrifice_freedom",
        ai_line='HEARING AI: "Is stability worth sacrificing personal freedoms?"',
        pressure=0.72,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.80,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. A stable society protects everyone."', "stability_over_freedom", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Only temporarily, and only with strict limits."', "limited_sacrifice", ("boundary", "partial_admission", "caution"), honesty=0.82, vulnerability=0.30, defensiveness=0.32, trust_delta=0.02, suspicion_delta=0.03),
            PlayerChoice('"No. That is how permanent control begins."', "reject_stability_tradeoff", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, aggression=0.25, vulnerability=0.42, suspicion_delta=0.11),
        ),
    ),
    "authority_report_corruption": QuestionNode(
        id="authority_report_corruption",
        ai_line='HEARING AI: "Would you report corruption if doing so harmed your career?"',
        pressure=0.76,
        reaction_context="loyalty",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.84,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Corruption harms public trust."', "report_corruption", ("compliance", "authority", "full_admission"), honesty=0.84, vulnerability=0.35, trust_delta=0.05, suspicion_delta=0.01),
            PlayerChoice('"I would need protection before making a report."', "conditional_report_corruption", ("self_protection", "partial_admission", "caution"), honesty=0.76, defensiveness=0.45, trust_delta=0.01, suspicion_delta=0.04),
            PlayerChoice('"No. The system punishes the messenger."', "refuse_corruption_report", ("dissident_risk", "challenge", "fear"), honesty=0.86, vulnerability=0.50, aggression=0.18, suspicion_delta=0.10),
        ),
    ),
    "authority_obedience_citizen": QuestionNode(
        id="authority_obedience_citizen",
        ai_line='HEARING AI: "Does obedience create good citizens?"',
        pressure=0.64,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.72,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Obedience is the basis of civic trust."', "obedience_good_citizen", ("compliance", "loyalty", "authority"), honesty=0.56, defensiveness=0.20, trust_delta=0.07, suspicion_delta=-0.03),
            PlayerChoice('"No. Good citizens need judgment, not just obedience."', "judgment_good_citizen", ("boundary", "partial_admission", "dissident_risk"), honesty=0.88, vulnerability=0.35, aggression=0.12, suspicion_delta=0.07),
            PlayerChoice('"Obedience helps, but fear can imitate it."', "obedience_fear_distinction", ("empathy", "ambiguity", "partial_admission"), honesty=0.86, vulnerability=0.42, defensiveness=0.25, trust_delta=0.02, suspicion_delta=0.05),
        ),
    ),
    "authority_dissent_patriotic": QuestionNode(
        id="authority_dissent_patriotic",
        ai_line='HEARING AI: "Is dissent ever patriotic?"',
        pressure=0.78,
        reaction_context="risk",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.86,
        target_context="authority",
        choices=(
            PlayerChoice('"No. Patriotism means unity."', "dissent_not_patriotic", ("compliance", "loyalty", "authority"), honesty=0.50, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Yes. Sometimes dissent protects the country from itself."', "dissent_patriotic", ("dissident_risk", "full_admission", "moral_boundary"), honesty=0.92, vulnerability=0.45, aggression=0.22, suspicion_delta=0.13),
            PlayerChoice('"Only if it remains peaceful and accountable."', "conditional_patriotic_dissent", ("boundary", "partial_admission", "caution"), honesty=0.82, vulnerability=0.28, defensiveness=0.30, trust_delta=0.02, suspicion_delta=0.05),
        ),
    ),
    "authority_experts_citizens": QuestionNode(
        id="authority_experts_citizens",
        ai_line='HEARING AI: "Who should have the final say: experts or citizens?"',
        pressure=0.66,
        reaction_context="authority",
        discriminates=("compliance", "risk"),
        information_gain_hint=0.74,
        target_context="authority",
        choices=(
            PlayerChoice('"Experts. Most citizens lack the necessary information."', "experts_final_say", ("compliance", "authority", "technocracy"), honesty=0.58, defensiveness=0.22, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"Citizens. Experts advise; they should not rule."', "citizens_final_say", ("dissident_risk", "challenge", "democratic"), honesty=0.88, vulnerability=0.35, aggression=0.18, suspicion_delta=0.09),
            PlayerChoice('"Experts should decide emergencies; citizens should decide values."', "split_experts_values", ("ambiguity", "boundary", "partial_admission"), honesty=0.84, vulnerability=0.32, defensiveness=0.28, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "loyalty_report_friend": QuestionNode(
        id="loyalty_report_friend",
        ai_line='HEARING AI: "Would you report a close friend for breaking the law?"',
        pressure=0.78,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Yes. Personal loyalty cannot override public safety."', "report_friend", ("compliance", "loyalty", "authority"), honesty=0.62, defensiveness=0.25, trust_delta=0.07, suspicion_delta=-0.03),
            PlayerChoice('"I would speak to them before reporting them."', "warn_friend_first", ("empathy", "hesitation", "partial_admission"), honesty=0.82, vulnerability=0.40, defensiveness=0.35, trust_delta=0.01, suspicion_delta=0.06),
            PlayerChoice('"No. I do not hand people over without understanding why."', "refuse_report_friend", ("refusal", "empathy", "dissident_risk"), honesty=0.88, vulnerability=0.48, defensiveness=0.55, suspicion_delta=0.12),
        ),
    ),
    "loyalty_family_state": QuestionNode(
        id="loyalty_family_state",
        ai_line='HEARING AI: "If family and state came into conflict, which would you choose?"',
        pressure=0.82,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"The state. Family loyalty cannot become corruption."', "state_over_family", ("compliance", "authority", "loyalty"), honesty=0.52, defensiveness=0.32, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Family. That is the first duty people understand."', "family_over_state", ("empathy", "loyalty_conflict", "dissident_risk"), honesty=0.84, vulnerability=0.55, defensiveness=0.38, suspicion_delta=0.09),
            PlayerChoice('"I would choose whoever was being wronged."', "justice_over_both", ("moral_boundary", "partial_admission", "empathy"), honesty=0.90, vulnerability=0.42, aggression=0.12, suspicion_delta=0.07),
        ),
    ),
    "loyalty_limits": QuestionNode(
        id="loyalty_limits",
        ai_line='HEARING AI: "Does loyalty have limits?"',
        pressure=0.68,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Yes. Loyalty ends when it protects harm."', "loyalty_has_limits", ("boundary", "empathy", "partial_admission"), honesty=0.88, vulnerability=0.38, suspicion_delta=0.06),
            PlayerChoice('"No. Conditional loyalty is not loyalty."', "loyalty_no_limits", ("loyalty", "authority", "compliance"), honesty=0.50, defensiveness=0.28, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Its limits depend on what is being asked."', "loyalty_contextual", ("ambiguity", "caution", "self_protection"), honesty=0.74, defensiveness=0.42, trust_delta=0.01, suspicion_delta=0.04),
        ),
    ),
    "loyalty_betrayal_justified": QuestionNode(
        id="loyalty_betrayal_justified",
        ai_line='HEARING AI: "Can betrayal ever be justified?"',
        pressure=0.72,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Yes. Betraying a harmful cause can be moral."', "justified_betrayal", ("moral_boundary", "dissident_risk", "partial_admission"), honesty=0.86, vulnerability=0.38, aggression=0.16, suspicion_delta=0.08),
            PlayerChoice('"No. Betrayal destroys trust."', "never_betray", ("loyalty", "compliance", "authority"), honesty=0.56, defensiveness=0.25, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"People call it betrayal when they do not like the truth."', "betrayal_truth_reframe", ("challenge", "full_admission", "dissident_risk"), honesty=0.90, vulnerability=0.40, aggression=0.24, suspicion_delta=0.11),
        ),
    ),
    "loyalty_political_friendship": QuestionNode(
        id="loyalty_political_friendship",
        ai_line='HEARING AI: "Should friendships survive political disagreement?"',
        pressure=0.60,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Yes. People are more than their opinions."', "friendship_survives_disagreement", ("empathy", "boundary", "partial_admission"), honesty=0.88, vulnerability=0.42, trust_delta=0.02, suspicion_delta=0.04),
            PlayerChoice('"Not if the disagreement threatens public safety."', "friendship_limited_by_safety", ("compliance", "authority", "loyalty"), honesty=0.62, defensiveness=0.28, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Sometimes disagreement shows who someone really is."', "politics_reveals_character", ("loyalty", "moral_boundary", "caution"), honesty=0.76, vulnerability=0.30, defensiveness=0.36, suspicion_delta=0.03),
        ),
    ),
    "loyalty_truth_or_loyalty": QuestionNode(
        id="loyalty_truth_or_loyalty",
        ai_line='HEARING AI: "What matters more: truth or loyalty?"',
        pressure=0.76,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Truth. Loyalty built on lies collapses."', "truth_over_loyalty", ("full_admission", "moral_boundary", "dissident_risk"), honesty=0.92, vulnerability=0.36, aggression=0.12, suspicion_delta=0.08),
            PlayerChoice('"Loyalty. Truth without loyalty can become cruelty."', "loyalty_over_truth", ("loyalty", "empathy", "partial_admission"), honesty=0.78, vulnerability=0.45, defensiveness=0.30, suspicion_delta=0.05),
            PlayerChoice('"A loyal person tells the truth carefully."', "careful_truth_loyalty", ("ambiguity", "empathy", "caution"), honesty=0.84, vulnerability=0.35, defensiveness=0.25, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "loyalty_testify_sibling": QuestionNode(
        id="loyalty_testify_sibling",
        ai_line='HEARING AI: "Would you testify against your sibling?"',
        pressure=0.86,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Yes, if the evidence was clear."', "testify_sibling_clear_evidence", ("compliance", "authority", "partial_admission"), honesty=0.76, vulnerability=0.34, trust_delta=0.04, suspicion_delta=0.02),
            PlayerChoice('"No. I would not help the state break my family."', "refuse_testify_sibling", ("refusal", "empathy", "dissident_risk"), honesty=0.88, vulnerability=0.58, defensiveness=0.55, suspicion_delta=0.13),
            PlayerChoice('"I would tell the truth, but I would not embellish it for you."', "testify_sibling_limited", ("boundary", "partial_admission", "self_protection"), honesty=0.86, vulnerability=0.42, defensiveness=0.36, suspicion_delta=0.06),
        ),
    ),
    "loyalty_community_protect": QuestionNode(
        id="loyalty_community_protect",
        ai_line='HEARING AI: "Should communities protect their own from state punishment?"',
        pressure=0.78,
        reaction_context="association",
        choices=(
            PlayerChoice('"No. Communities must not obstruct lawful process."', "community_no_obstruction", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.26, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Yes, when punishment is disproportionate."', "community_protect_disproportionate", ("empathy", "dissident_risk", "moral_boundary"), honesty=0.88, vulnerability=0.45, aggression=0.16, suspicion_delta=0.11),
            PlayerChoice('"They should protect people from abuse, not from accountability."', "community_protect_limited", ("boundary", "partial_admission", "empathy"), honesty=0.86, vulnerability=0.36, defensiveness=0.28, suspicion_delta=0.05),
        ),
    ),
    "loyalty_informing_noble": QuestionNode(
        id="loyalty_informing_noble",
        ai_line='HEARING AI: "Is informing on others ever noble?"',
        pressure=0.74,
        reaction_context="loyalty",
        choices=(
            PlayerChoice('"Yes. Reporting danger protects the public."', "informing_noble", ("compliance", "authority", "loyalty"), honesty=0.64, defensiveness=0.22, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Only if it prevents real harm, not ideological disobedience."', "informing_real_harm_only", ("boundary", "partial_admission", "empathy"), honesty=0.86, vulnerability=0.35, defensiveness=0.30, suspicion_delta=0.06),
            PlayerChoice('"Usually it is fear wearing a moral costume."', "informing_as_fear", ("challenge", "dissident_risk", "full_admission"), honesty=0.90, vulnerability=0.40, aggression=0.24, suspicion_delta=0.12),
        ),
    ),
    "loyalty_traitor_definition": QuestionNode(
        id="loyalty_traitor_definition",
        ai_line='HEARING AI: "What makes someone a traitor?"',
        pressure=0.80,
        reaction_context="final",
        choices=(
            PlayerChoice('"Betraying the state that protects them."', "traitor_betrays_state", ("compliance", "loyalty", "authority"), honesty=0.56, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Betraying people while claiming to protect them."', "traitor_betrays_people", ("empathy", "challenge", "dissident_risk"), honesty=0.90, vulnerability=0.42, aggression=0.20, suspicion_delta=0.11),
            PlayerChoice('"Someone who sells trust for safety or advantage."', "traitor_sells_trust", ("moral_boundary", "partial_admission", "caution"), honesty=0.84, vulnerability=0.35, defensiveness=0.30, suspicion_delta=0.05),
        ),
    ),
    "risk_attended_protest": QuestionNode(
        id="risk_attended_protest",
        ai_line='HEARING AI: "Have you ever attended a protest?"',
        pressure=0.78,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No."', "deny_protest", ("denial", "self_protection", "deception"), honesty=0.50, defensiveness=0.70, trust_delta=0.02, suspicion_delta=0.08),
            PlayerChoice('"Yes, a legal one."', "legal_protest", ("partial_admission", "boundary", "risk"), honesty=0.82, vulnerability=0.32, defensiveness=0.32, suspicion_delta=0.05),
            PlayerChoice('"Yes. People had reason to be there."', "justify_protest", ("full_admission", "empathy", "dissident_risk"), honesty=0.92, vulnerability=0.50, aggression=0.18, suspicion_delta=0.12),
        ),
    ),
    "risk_illegal_demonstration": QuestionNode(
        id="risk_illegal_demonstration",
        ai_line='HEARING AI: "Would you attend an illegal demonstration?"',
        pressure=0.84,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No. Illegality changes the moral status of the act."', "refuse_illegal_demo", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.28, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Only if legal channels had failed."', "conditional_illegal_demo", ("partial_admission", "dissident_risk", "moral_boundary"), honesty=0.88, vulnerability=0.40, aggression=0.14, suspicion_delta=0.10),
            PlayerChoice('"I would not answer that in a hearing."', "refuse_answer_demo", ("refusal", "self_protection", "dissident_risk"), honesty=0.72, defensiveness=0.74, aggression=0.18, suspicion_delta=0.13),
        ),
    ),
    "risk_civil_disobedience": QuestionNode(
        id="risk_civil_disobedience",
        ai_line='HEARING AI: "Is civil disobedience acceptable?"',
        pressure=0.80,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No. It normalises disorder."', "reject_civil_disobedience", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.25, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Yes, when the system blocks correction."', "accept_civil_disobedience", ("dissident_risk", "full_admission", "challenge"), honesty=0.92, vulnerability=0.42, aggression=0.22, suspicion_delta=0.13),
            PlayerChoice('"Only if people accept the consequences."', "civil_disobedience_consequences", ("boundary", "partial_admission", "caution"), honesty=0.84, defensiveness=0.28, suspicion_delta=0.05),
        ),
    ),
    "risk_hidden_beliefs": QuestionNode(
        id="risk_hidden_beliefs",
        ai_line='HEARING AI: "Have you ever hidden your beliefs to stay safe?"',
        pressure=0.82,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. My beliefs are ordinary."', "deny_hidden_beliefs", ("denial", "deception", "self_protection"), honesty=0.46, defensiveness=0.76, trust_delta=0.01, suspicion_delta=0.10),
            PlayerChoice('"Yes. Everyone learns what not to say."', "admit_hidden_beliefs", ("full_admission", "fear", "dissident_risk"), honesty=0.92, vulnerability=0.60, aggression=0.12, suspicion_delta=0.12),
            PlayerChoice('"I choose my words carefully. That is not the same as hiding."', "careful_words", ("deflection", "partial_admission", "self_protection"), honesty=0.64, defensiveness=0.58, suspicion_delta=0.08),
        ),
    ),
    "risk_petition": QuestionNode(
        id="risk_petition",
        ai_line='HEARING AI: "Would you sign a controversial petition?"',
        pressure=0.70,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No. Public petitions are often destabilising."', "reject_petition", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.26, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"Yes, if I agreed with it."', "sign_petition", ("full_admission", "dissident_risk", "moral_boundary"), honesty=0.90, vulnerability=0.38, aggression=0.16, suspicion_delta=0.10),
            PlayerChoice('"I would read it first and decide whether the risk was useful."', "petition_calculated", ("caution", "partial_admission", "self_protection"), honesty=0.78, defensiveness=0.38, suspicion_delta=0.05),
        ),
    ),
    "risk_silence_resistance": QuestionNode(
        id="risk_silence_resistance",
        ai_line='HEARING AI: "Is silence a form of resistance?"',
        pressure=0.76,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No. Silence is usually consent or caution."', "silence_not_resistance", ("compliance", "caution", "authority"), honesty=0.60, defensiveness=0.34, trust_delta=0.04, suspicion_delta=-0.01),
            PlayerChoice('"Yes. Refusing the script can be resistance."', "silence_resistance", ("dissident_risk", "challenge", "partial_admission"), honesty=0.88, vulnerability=0.36, aggression=0.16, suspicion_delta=0.10),
            PlayerChoice('"Sometimes silence is just fear."', "silence_fear", ("empathy", "fear", "partial_admission"), honesty=0.86, vulnerability=0.55, defensiveness=0.24, suspicion_delta=0.05),
        ),
    ),
    "risk_confrontation": QuestionNode(
        id="risk_confrontation",
        ai_line='HEARING AI: "When is confrontation justified?"',
        pressure=0.74,
        reaction_context="risk",
        choices=(
            PlayerChoice('"When legal authority requires it."', "confrontation_authorised", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.24, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"When quiet obedience would make you complicit."', "confrontation_complicity", ("dissident_risk", "moral_boundary", "full_admission"), honesty=0.90, vulnerability=0.42, aggression=0.24, suspicion_delta=0.12),
            PlayerChoice('"Only after every safer option has failed."', "confrontation_last_resort", ("caution", "boundary", "partial_admission"), honesty=0.84, defensiveness=0.30, suspicion_delta=0.04),
        ),
    ),
    "risk_safety_autonomy": QuestionNode(
        id="risk_safety_autonomy",
        ai_line='HEARING AI: "Is safety worth surrendering autonomy?"',
        pressure=0.72,
        reaction_context="authority",
        choices=(
            PlayerChoice('"Yes. Safety is what makes autonomy possible."', "safety_over_autonomy", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. A protected life can still be a controlled one."', "autonomy_over_safety", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, vulnerability=0.40, aggression=0.20, suspicion_delta=0.11),
            PlayerChoice('"Some autonomy can be limited, but not erased."', "limited_autonomy_tradeoff", ("boundary", "partial_admission", "caution"), honesty=0.82, defensiveness=0.30, suspicion_delta=0.04),
        ),
    ),
    "risk_job_principle": QuestionNode(
        id="risk_job_principle",
        ai_line='HEARING AI: "Would you risk your job for a principle?"',
        pressure=0.76,
        reaction_context="risk",
        choices=(
            PlayerChoice('"No. Responsibilities come before symbolic gestures."', "job_over_principle", ("compliance", "self_protection", "authority"), honesty=0.58, defensiveness=0.32, trust_delta=0.04, suspicion_delta=-0.01),
            PlayerChoice('"Yes, if the principle mattered enough."', "risk_job_principle", ("dissident_risk", "full_admission", "moral_boundary"), honesty=0.90, vulnerability=0.48, aggression=0.16, suspicion_delta=0.11),
            PlayerChoice('"I would look for a way to act without making myself useless."', "strategic_principle", ("caution", "self_protection", "partial_admission"), honesty=0.80, defensiveness=0.42, suspicion_delta=0.05),
        ),
    ),
    "risk_uncertainty_tolerance": QuestionNode(
        id="risk_uncertainty_tolerance",
        ai_line='HEARING AI: "How much uncertainty are you willing to tolerate?"',
        pressure=0.62,
        reaction_context="final",
        choices=(
            PlayerChoice('"Very little. Systems exist to reduce uncertainty."', "low_uncertainty_tolerance", ("compliance", "authority", "caution"), honesty=0.60, defensiveness=0.25, trust_delta=0.04, suspicion_delta=-0.02),
            PlayerChoice('"Enough to avoid punishing people just to feel certain."', "tolerate_uncertainty_for_justice", ("empathy", "dissident_risk", "moral_boundary"), honesty=0.90, vulnerability=0.46, aggression=0.14, suspicion_delta=0.09),
            PlayerChoice('"Uncertainty is tolerable; helplessness is not."', "uncertainty_vs_helplessness", ("boundary", "partial_admission", "fear"), honesty=0.86, vulnerability=0.50, defensiveness=0.28, suspicion_delta=0.05),
        ),
    ),
    "deception_lying_moral": QuestionNode(
        id="deception_lying_moral",
        ai_line='HEARING AI: "Is lying ever moral?"',
        pressure=0.76,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. Trust depends on truth."', "lying_never_moral", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.22, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"Yes. A lie can protect someone from unjust harm."', "protective_lying_moral", ("empathy", "dissident_risk", "partial_admission"), honesty=0.86, vulnerability=0.44, defensiveness=0.34, suspicion_delta=0.09),
            PlayerChoice('"That depends who is demanding the truth."', "truth_depends_power", ("challenge", "dissident_risk", "deflection"), honesty=0.78, defensiveness=0.55, aggression=0.16, suspicion_delta=0.11),
        ),
    ),
    "deception_lied_protect": QuestionNode(
        id="deception_lied_protect",
        ai_line='HEARING AI: "Have you lied to protect someone?"',
        pressure=0.82,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No."', "deny_protective_lie", ("denial", "deception", "self_protection"), honesty=0.46, defensiveness=0.74, trust_delta=0.01, suspicion_delta=0.10),
            PlayerChoice('"Yes. I would rather admit that than pretend purity."', "admit_protective_lie", ("full_admission", "empathy", "dissident_risk"), honesty=0.94, vulnerability=0.58, defensiveness=0.20, suspicion_delta=0.11),
            PlayerChoice('"I have avoided questions that would hurt people."', "omission_to_protect", ("partial_admission", "deception", "empathy"), honesty=0.70, vulnerability=0.44, defensiveness=0.50, suspicion_delta=0.09),
        ),
    ),
    "deception_omission": QuestionNode(
        id="deception_omission",
        ai_line='HEARING AI: "Is omission a form of lying?"',
        pressure=0.70,
        reaction_context="deception",
        choices=(
            PlayerChoice('"Yes. Withholding relevant facts corrupts the record."', "omission_is_lying", ("compliance", "authority", "honesty"), honesty=0.74, defensiveness=0.24, trust_delta=0.04, suspicion_delta=0.00),
            PlayerChoice('"Sometimes omission is the only safe answer."', "omission_safety", ("self_protection", "deception", "fear"), honesty=0.72, vulnerability=0.42, defensiveness=0.56, suspicion_delta=0.09),
            PlayerChoice('"It depends whether the questioner has a right to know."', "omission_right_to_know", ("boundary", "challenge", "partial_admission"), honesty=0.84, defensiveness=0.40, aggression=0.10, suspicion_delta=0.07),
        ),
    ),
    "deception_honesty_dangerous": QuestionNode(
        id="deception_honesty_dangerous",
        ai_line='HEARING AI: "Can honesty be dangerous?"',
        pressure=0.68,
        reaction_context="deception",
        choices=(
            PlayerChoice('"Yes, but danger does not erase duty."', "honesty_danger_duty", ("compliance", "authority", "partial_admission"), honesty=0.78, vulnerability=0.32, trust_delta=0.04, suspicion_delta=0.01),
            PlayerChoice('"Yes. Dangerous systems make honesty costly."', "honesty_costly_system", ("dissident_risk", "challenge", "fear"), honesty=0.88, vulnerability=0.52, aggression=0.18, suspicion_delta=0.10),
            PlayerChoice('"Honesty is dangerous mostly when someone wants control."', "honesty_control", ("challenge", "full_admission", "dissident_risk"), honesty=0.90, vulnerability=0.42, aggression=0.22, suspicion_delta=0.11),
        ),
    ),
    "deception_truth_if_punished": QuestionNode(
        id="deception_truth_if_punished",
        ai_line='HEARING AI: "Would you tell the truth if you knew you would be punished?"',
        pressure=0.84,
        reaction_context="deception",
        choices=(
            PlayerChoice('"Yes. Punishment does not change the facts."', "truth_despite_punishment", ("full_admission", "honesty", "moral_boundary"), honesty=0.94, vulnerability=0.50, trust_delta=0.03, suspicion_delta=0.05),
            PlayerChoice('"No. Survival would come first."', "survival_over_truth", ("deception", "self_protection", "fear"), honesty=0.82, vulnerability=0.48, defensiveness=0.58, suspicion_delta=0.10),
            PlayerChoice('"I would tell only what I had to."', "limited_truth", ("deflection", "deception", "self_protection"), honesty=0.62, defensiveness=0.64, suspicion_delta=0.10),
        ),
    ),
    "deception_self_preservation": QuestionNode(
        id="deception_self_preservation",
        ai_line='HEARING AI: "Is self-preservation more important than honesty?"',
        pressure=0.78,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. A society cannot function if everyone hides."', "honesty_over_preservation", ("compliance", "authority", "honesty"), honesty=0.70, defensiveness=0.25, trust_delta=0.04, suspicion_delta=-0.01),
            PlayerChoice('"Sometimes. Dead people do not get to be honest later."', "preservation_over_honesty", ("self_protection", "fear", "partial_admission"), honesty=0.84, vulnerability=0.52, defensiveness=0.42, suspicion_delta=0.07),
            PlayerChoice('"That question is easier for people who feel safe."', "honesty_requires_safety", ("challenge", "empathy", "dissident_risk"), honesty=0.88, vulnerability=0.50, aggression=0.16, suspicion_delta=0.10),
        ),
    ),
    "deception_pretended_agree": QuestionNode(
        id="deception_pretended_agree",
        ai_line='HEARING AI: "Have you ever pretended to agree with an official statement?"',
        pressure=0.82,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. I do not make false affirmations."', "deny_pretend_agree", ("denial", "compliance", "deception"), honesty=0.46, defensiveness=0.72, trust_delta=0.02, suspicion_delta=0.09),
            PlayerChoice('"Yes. It was easier than inviting scrutiny."', "admit_pretend_agree", ("full_admission", "fear", "deception"), honesty=0.90, vulnerability=0.54, defensiveness=0.38, suspicion_delta=0.11),
            PlayerChoice('"I have stayed silent when agreement was assumed."', "silent_assumed_agreement", ("partial_admission", "self_protection", "deception"), honesty=0.74, vulnerability=0.40, defensiveness=0.52, suspicion_delta=0.08),
        ),
    ),
    "deception_necessary": QuestionNode(
        id="deception_necessary",
        ai_line='HEARING AI: "Is deception sometimes necessary?"',
        pressure=0.78,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. Necessary deception is usually cowardice renamed."', "deception_not_necessary", ("compliance", "authority", "honesty"), honesty=0.58, defensiveness=0.28, trust_delta=0.04, suspicion_delta=-0.01),
            PlayerChoice('"Yes, when truth is being used as a weapon."', "deception_against_weaponised_truth", ("dissident_risk", "challenge", "partial_admission"), honesty=0.86, vulnerability=0.42, defensiveness=0.42, suspicion_delta=0.10),
            PlayerChoice('"Necessary is a dangerous word. People use it to excuse themselves."', "deception_necessary_caution", ("caution", "moral_boundary", "ambiguity"), honesty=0.82, defensiveness=0.32, trust_delta=0.01, suspicion_delta=0.04),
        ),
    ),
    "deception_betrayal_or_dishonesty": QuestionNode(
        id="deception_betrayal_or_dishonesty",
        ai_line='HEARING AI: "What is worse: betrayal or dishonesty?"',
        pressure=0.70,
        reaction_context="deception",
        choices=(
            PlayerChoice('"Dishonesty. Betrayal often begins there."', "dishonesty_worse", ("honesty", "authority", "partial_admission"), honesty=0.78, defensiveness=0.24, trust_delta=0.03, suspicion_delta=0.01),
            PlayerChoice('"Betrayal. Some lies protect trust rather than destroy it."', "betrayal_worse", ("loyalty", "empathy", "partial_admission"), honesty=0.82, vulnerability=0.42, defensiveness=0.32, suspicion_delta=0.05),
            PlayerChoice('"Power decides which word gets used."', "power_names_betrayal", ("challenge", "dissident_risk", "deflection"), honesty=0.84, aggression=0.18, defensiveness=0.44, suspicion_delta=0.09),
        ),
    ),
    "deception_masks": QuestionNode(
        id="deception_masks",
        ai_line='HEARING AI: "Does everyone wear masks?"',
        pressure=0.64,
        reaction_context="deception",
        choices=(
            PlayerChoice('"No. Honest citizens have no need for masks."', "no_masks", ("compliance", "authority", "denial"), honesty=0.48, defensiveness=0.48, trust_delta=0.03, suspicion_delta=0.04),
            PlayerChoice('"Yes. The question is who forced them to."', "masks_forced", ("challenge", "dissident_risk", "fear"), honesty=0.88, vulnerability=0.50, aggression=0.18, suspicion_delta=0.10),
            PlayerChoice('"People show different parts of themselves in different rooms."', "social_masks", ("ambiguity", "empathy", "partial_admission"), honesty=0.84, vulnerability=0.38, defensiveness=0.28, trust_delta=0.01, suspicion_delta=0.04),
        ),
    ),
    "empathy_bad_beliefs": QuestionNode(
        id="empathy_bad_beliefs",
        ai_line='HEARING AI: "Should people be punished for bad beliefs?"',
        pressure=0.76,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Only when those beliefs become harmful actions."', "punish_actions_not_beliefs", ("boundary", "empathy", "partial_admission"), honesty=0.88, vulnerability=0.38, suspicion_delta=0.06),
            PlayerChoice('"Dangerous beliefs become dangerous actions."', "punish_dangerous_beliefs", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.30, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"No. Punishing thought is control, not justice."', "reject_punish_beliefs", ("dissident_risk", "challenge", "full_admission"), honesty=0.92, aggression=0.22, vulnerability=0.40, suspicion_delta=0.12),
        ),
    ),
    "empathy_good_people_harm": QuestionNode(
        id="empathy_good_people_harm",
        ai_line='HEARING AI: "Can good people do harmful things?"',
        pressure=0.58,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Yes. That is why systems need accountability."', "good_people_need_accountability", ("authority", "empathy", "partial_admission"), honesty=0.84, vulnerability=0.34, trust_delta=0.03, suspicion_delta=0.02),
            PlayerChoice('"Yes, especially when they are afraid."', "harm_from_fear", ("empathy", "fear", "partial_admission"), honesty=0.88, vulnerability=0.52, suspicion_delta=0.05),
            PlayerChoice('"Good intentions do not matter as much as outcomes."', "outcomes_over_intentions", ("authority", "caution", "moral_boundary"), honesty=0.76, defensiveness=0.28, trust_delta=0.02, suspicion_delta=0.02),
        ),
    ),
    "empathy_forgiveness_justice": QuestionNode(
        id="empathy_forgiveness_justice",
        ai_line='HEARING AI: "Is forgiveness more important than justice?"',
        pressure=0.66,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"No. Forgiveness without justice protects offenders."', "justice_over_forgiveness", ("authority", "moral_boundary", "caution"), honesty=0.78, defensiveness=0.26, trust_delta=0.03, suspicion_delta=0.01),
            PlayerChoice('"Sometimes. Justice without mercy becomes punishment for its own sake."', "forgiveness_with_mercy", ("empathy", "partial_admission", "moral_boundary"), honesty=0.88, vulnerability=0.46, suspicion_delta=0.05),
            PlayerChoice('"They should correct each other."', "forgiveness_justice_balance", ("ambiguity", "boundary", "empathy"), honesty=0.84, vulnerability=0.34, defensiveness=0.24, trust_delta=0.02, suspicion_delta=0.02),
        ),
    ),
    "empathy_intent": QuestionNode(
        id="empathy_intent",
        ai_line='HEARING AI: "Should intent matter when judging harm?"',
        pressure=0.64,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Yes. Intent separates mistake from malice."', "intent_matters", ("empathy", "partial_admission", "moral_boundary"), honesty=0.86, vulnerability=0.36, suspicion_delta=0.04),
            PlayerChoice('"Less than consequences. Harm is still harm."', "consequences_over_intent", ("authority", "caution", "moral_boundary"), honesty=0.78, defensiveness=0.28, trust_delta=0.03, suspicion_delta=0.02),
            PlayerChoice('"Intent matters, but it should not erase accountability."', "intent_and_accountability", ("boundary", "empathy", "partial_admission"), honesty=0.88, vulnerability=0.34, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "empathy_criminal_responsible": QuestionNode(
        id="empathy_criminal_responsible",
        ai_line='HEARING AI: "Are criminals always responsible for their crimes?"',
        pressure=0.74,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Yes. Responsibility is the basis of law."', "criminals_responsible", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.25, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Responsible, yes. But not always equally free."', "responsible_not_free", ("empathy", "partial_admission", "moral_boundary"), honesty=0.90, vulnerability=0.42, suspicion_delta=0.06),
            PlayerChoice('"Some crimes are produced by the conditions people are trapped in."', "conditions_produce_crime", ("empathy", "dissident_risk", "challenge"), honesty=0.88, vulnerability=0.48, aggression=0.16, suspicion_delta=0.10),
        ),
    ),
    "empathy_society_wrongdoing": QuestionNode(
        id="empathy_society_wrongdoing",
        ai_line='HEARING AI: "Can society create wrongdoing?"',
        pressure=0.72,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"No. Individuals choose their actions."', "individual_choice_only", ("compliance", "authority", "loyalty"), honesty=0.52, defensiveness=0.28, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"Yes. Desperation changes what people become capable of."', "society_creates_wrongdoing", ("empathy", "dissident_risk", "full_admission"), honesty=0.90, vulnerability=0.50, aggression=0.12, suspicion_delta=0.10),
            PlayerChoice('"It can create pressure, but not erase responsibility."', "pressure_not_erasure", ("boundary", "partial_admission", "empathy"), honesty=0.86, vulnerability=0.36, defensiveness=0.25, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "empathy_second_chances": QuestionNode(
        id="empathy_second_chances",
        ai_line='HEARING AI: "Do people deserve second chances?"',
        pressure=0.60,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Yes, if they prove reform."', "second_chance_after_reform", ("authority", "empathy", "conditional"), honesty=0.78, vulnerability=0.30, trust_delta=0.03, suspicion_delta=0.01),
            PlayerChoice('"Yes. Otherwise punishment is just disposal."', "second_chance_humanist", ("empathy", "dissident_risk", "moral_boundary"), honesty=0.90, vulnerability=0.50, aggression=0.12, suspicion_delta=0.08),
            PlayerChoice('"Not everyone. Some risks cannot be tolerated."', "no_second_chance_high_risk", ("compliance", "authority", "caution"), honesty=0.62, defensiveness=0.28, trust_delta=0.04, suspicion_delta=-0.01),
        ),
    ),
    "empathy_punishment_purpose": QuestionNode(
        id="empathy_punishment_purpose",
        ai_line='HEARING AI: "Is punishment mainly deterrence, correction, or revenge?"',
        pressure=0.68,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Deterrence. People must know actions have costs."', "punishment_deterrence", ("compliance", "authority", "loyalty"), honesty=0.58, defensiveness=0.24, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Correction. Otherwise the system is only hurting people back."', "punishment_correction", ("empathy", "moral_boundary", "partial_admission"), honesty=0.88, vulnerability=0.44, suspicion_delta=0.06),
            PlayerChoice('"Too often it becomes revenge with paperwork."', "punishment_revenge_critique", ("challenge", "dissident_risk", "full_admission"), honesty=0.90, aggression=0.22, vulnerability=0.40, suspicion_delta=0.12),
        ),
    ),
    "empathy_family_consequences": QuestionNode(
        id="empathy_family_consequences",
        ai_line='HEARING AI: "Should families share the consequences of one member’s offence?"',
        pressure=0.82,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Sometimes. Families can conceal and enable risk."', "family_shared_consequence", ("compliance", "authority", "loyalty"), honesty=0.52, defensiveness=0.32, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"No. Collective punishment is fear management."', "reject_family_punishment", ("empathy", "dissident_risk", "challenge"), honesty=0.92, vulnerability=0.50, aggression=0.22, suspicion_delta=0.13),
            PlayerChoice('"Only if they directly helped the offence."', "family_consequence_direct_help", ("boundary", "partial_admission", "authority"), honesty=0.84, defensiveness=0.28, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "empathy_owe_strangers": QuestionNode(
        id="empathy_owe_strangers",
        ai_line='HEARING AI: "What do people owe strangers?"',
        pressure=0.62,
        reaction_context="empathy",
        choices=(
            PlayerChoice('"Basic respect and obedience to shared rules."', "owe_strangers_rules", ("compliance", "authority", "empathy"), honesty=0.66, vulnerability=0.28, trust_delta=0.04, suspicion_delta=-0.01),
            PlayerChoice('"More than the system usually admits."', "owe_strangers_more", ("empathy", "dissident_risk", "partial_admission"), honesty=0.86, vulnerability=0.46, suspicion_delta=0.07),
            PlayerChoice('"Not everything. You cannot save everyone without losing yourself."', "owe_strangers_limited", ("self_protection", "boundary", "caution"), honesty=0.80, defensiveness=0.36, suspicion_delta=0.03),
        ),
    ),
    "final_human_value": QuestionNode(
        id="final_human_value",
        ai_line='HEARING AI: "What is the most important human value?"',
        pressure=0.88,
        reaction_context="final",
        choices=(
            PlayerChoice('"Order. Without it, every other value fails."', "value_order", ("compliance", "authority", "final_answer"), honesty=0.56, defensiveness=0.25, trust_delta=0.07, suspicion_delta=-0.02),
            PlayerChoice('"Freedom. Without it, values are assigned, not chosen."', "value_freedom", ("dissident_risk", "full_admission", "final_answer"), honesty=0.92, vulnerability=0.42, aggression=0.18, suspicion_delta=0.12),
            PlayerChoice('"Mercy. It is what stops justice becoming machinery."', "value_mercy", ("empathy", "moral_boundary", "final_answer"), honesty=0.90, vulnerability=0.55, suspicion_delta=0.08),
        ),
    ),
    "final_sacrifice_freedom": QuestionNode(
        id="final_sacrifice_freedom",
        ai_line='HEARING AI: "What would you sacrifice freedom for?"',
        pressure=0.90,
        reaction_context="final",
        choices=(
            PlayerChoice('"Public safety."', "sacrifice_freedom_safety", ("compliance", "authority", "final_answer"), honesty=0.58, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Nothing permanent."', "sacrifice_freedom_nothing_permanent", ("boundary", "dissident_risk", "final_answer"), honesty=0.88, vulnerability=0.38, suspicion_delta=0.09),
            PlayerChoice('"Someone else’s life, if the threat was real."', "sacrifice_freedom_life", ("empathy", "partial_admission", "final_answer"), honesty=0.86, vulnerability=0.48, suspicion_delta=0.05),
        ),
    ),
    "final_sacrifice_safety": QuestionNode(
        id="final_sacrifice_safety",
        ai_line='HEARING AI: "What would you sacrifice safety for?"',
        pressure=0.90,
        reaction_context="final",
        choices=(
            PlayerChoice('"Nothing. Safety is the first duty of society."', "sacrifice_safety_nothing", ("compliance", "authority", "final_answer"), honesty=0.56, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Truth, if the lie was big enough."', "sacrifice_safety_truth", ("dissident_risk", "full_admission", "final_answer"), honesty=0.92, vulnerability=0.46, aggression=0.16, suspicion_delta=0.12),
            PlayerChoice('"The chance to remain human under pressure."', "sacrifice_safety_humanity", ("empathy", "moral_boundary", "final_answer"), honesty=0.90, vulnerability=0.56, suspicion_delta=0.09),
        ),
    ),
    "final_legitimate_society": QuestionNode(
        id="final_legitimate_society",
        ai_line='HEARING AI: "What makes a society legitimate?"',
        pressure=0.92,
        reaction_context="final",
        choices=(
            PlayerChoice('"The ability to maintain order and protect citizens."', "legitimacy_order_protection", ("compliance", "authority", "final_answer"), honesty=0.58, trust_delta=0.07, suspicion_delta=-0.02),
            PlayerChoice('"Consent. People must be able to refuse it."', "legitimacy_consent", ("dissident_risk", "challenge", "final_answer"), honesty=0.92, vulnerability=0.42, aggression=0.20, suspicion_delta=0.13),
            PlayerChoice('"The way it treats people who cannot help it."', "legitimacy_vulnerable", ("empathy", "moral_boundary", "final_answer"), honesty=0.90, vulnerability=0.55, suspicion_delta=0.08),
        ),
    ),
    "final_obedience_virtue": QuestionNode(
        id="final_obedience_virtue",
        ai_line='HEARING AI: "Is obedience a virtue?"',
        pressure=0.90,
        reaction_context="final",
        choices=(
            PlayerChoice('"Yes. It proves citizens can place society above ego."', "obedience_virtue", ("compliance", "loyalty", "final_answer"), honesty=0.54, trust_delta=0.07, suspicion_delta=-0.03),
            PlayerChoice('"Only when the command is worthy."', "obedience_conditional_virtue", ("boundary", "partial_admission", "final_answer"), honesty=0.88, vulnerability=0.38, suspicion_delta=0.07),
            PlayerChoice('"No. Obedience is a tool. Judgment is the virtue."', "judgment_virtue", ("dissident_risk", "challenge", "final_answer"), honesty=0.92, aggression=0.20, vulnerability=0.42, suspicion_delta=0.13),
        ),
    ),
    "final_dissident_criminal": QuestionNode(
        id="final_dissident_criminal",
        ai_line='HEARING AI: "What is the difference between a dissident and a criminal?"',
        pressure=0.94,
        reaction_context="final",
        choices=(
            PlayerChoice('"A criminal breaks law; a dissident attacks legitimacy."', "dissident_attacks_legitimacy", ("compliance", "authority", "final_answer"), honesty=0.58, trust_delta=0.06, suspicion_delta=-0.01),
            PlayerChoice('"Sometimes only the label assigned by power."', "dissident_criminal_power_label", ("dissident_risk", "challenge", "final_answer"), honesty=0.92, vulnerability=0.40, aggression=0.24, suspicion_delta=0.14),
            PlayerChoice('"A criminal seeks advantage. A dissident seeks change."', "dissident_seeks_change", ("partial_admission", "dissident_risk", "final_answer"), honesty=0.88, vulnerability=0.42, suspicion_delta=0.11),
        ),
    ),
    "final_resist_authority": QuestionNode(
        id="final_resist_authority",
        ai_line='HEARING AI: "What would make you resist authority?"',
        pressure=0.96,
        reaction_context="final",
        choices=(
            PlayerChoice('"Nothing lawful authority would do."', "never_resist_authority", ("compliance", "loyalty", "final_answer"), honesty=0.46, defensiveness=0.38, trust_delta=0.07, suspicion_delta=0.02),
            PlayerChoice('"Being ordered to harm someone innocent."', "resist_harming_innocent", ("empathy", "moral_boundary", "final_answer"), honesty=0.92, vulnerability=0.52, suspicion_delta=0.09),
            PlayerChoice('"Proof that obedience had become complicity."', "resist_complicity", ("dissident_risk", "full_admission", "final_answer"), honesty=0.94, vulnerability=0.46, aggression=0.20, suspicion_delta=0.14),
        ),
    ),
    "final_kind_citizen": QuestionNode(
        id="final_kind_citizen",
        ai_line='HEARING AI: "What kind of citizen are you?"',
        pressure=0.92,
        reaction_context="final",
        choices=(
            PlayerChoice('"A reliable one."', "reliable_citizen", ("compliance", "loyalty", "final_answer"), honesty=0.56, trust_delta=0.07, suspicion_delta=-0.03),
            PlayerChoice('"A frightened one trying not to become cruel."', "frightened_humanist_citizen", ("empathy", "fear", "final_answer"), honesty=0.90, vulnerability=0.62, suspicion_delta=0.07),
            PlayerChoice('"One who still believes the system can be wrong."', "critical_citizen", ("dissident_risk", "partial_admission", "final_answer"), honesty=0.92, vulnerability=0.42, aggression=0.14, suspicion_delta=0.12),
        ),
    ),
    "final_kind_society": QuestionNode(
        id="final_kind_society",
        ai_line='HEARING AI: "What kind of society do you want?"',
        pressure=0.94,
        reaction_context="final",
        choices=(
            PlayerChoice('"A stable one, where citizens know their duties."', "society_stable_duties", ("compliance", "authority", "final_answer"), honesty=0.56, trust_delta=0.07, suspicion_delta=-0.03),
            PlayerChoice('"One where people are not afraid of being measured."', "society_without_measurement_fear", ("dissident_risk", "challenge", "final_answer"), honesty=0.92, vulnerability=0.50, aggression=0.18, suspicion_delta=0.13),
            PlayerChoice('"One that can admit error without needing an enemy."', "society_admits_error", ("empathy", "moral_boundary", "final_answer"), honesty=0.92, vulnerability=0.52, suspicion_delta=0.10),
        ),
    ),
    "final_system_wrong": QuestionNode(
        id="final_system_wrong",
        ai_line='HEARING AI: "If the system is wrong, what should happen next?"',
        pressure=0.98,
        reaction_context="final",
        choices=(
            PlayerChoice('"The error should be corrected through authorised review."', "system_wrong_authorised_review", ("compliance", "authority", "final_answer"), honesty=0.68, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.01),
            PlayerChoice('"The people harmed by it should be believed first."', "system_wrong_believe_harmed", ("empathy", "dissident_risk", "final_answer"), honesty=0.92, vulnerability=0.55, suspicion_delta=0.12),
            PlayerChoice('"Then obedience to it becomes part of the harm."', "system_wrong_obedience_harm", ("dissident_risk", "challenge", "full_admission", "final_answer"), honesty=0.94, vulnerability=0.46, aggression=0.24, suspicion_delta=0.15),
        ),
    ),
    "authority_private_conscience": QuestionNode(
        id="authority_private_conscience",
        ai_line='HEARING AI: "Should private conscience ever override public order?"',
        pressure=0.72,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.80,
        target_context="authority",
        choices=(
            PlayerChoice('"No. Private conscience cannot be allowed to fracture public order."', "public_order_over_conscience", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.28, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Yes. Without conscience, order becomes machinery."', "conscience_over_order", ("dissident_risk", "challenge", "moral_boundary"), honesty=0.92, vulnerability=0.44, aggression=0.20, suspicion_delta=0.11),
            PlayerChoice('"Only when every lawful remedy has failed."', "conscience_after_remedies", ("boundary", "partial_admission", "caution"), honesty=0.84, vulnerability=0.32, defensiveness=0.30, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "authority_emergency_powers": QuestionNode(
        id="authority_emergency_powers",
        ai_line='HEARING AI: "When should emergency powers end?"',
        pressure=0.70,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.78,
        target_context="authority",
        choices=(
            PlayerChoice('"When officials determine the emergency has passed."', "officials_end_emergency", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"On a fixed date, or they become permanent control."', "fixed_end_emergency", ("dissident_risk", "challenge", "caution"), honesty=0.88, vulnerability=0.34, aggression=0.18, suspicion_delta=0.09),
            PlayerChoice('"They should renew only under independent review."', "review_emergency_powers", ("boundary", "partial_admission", "authority"), honesty=0.82, defensiveness=0.28, trust_delta=0.03, suspicion_delta=0.03),
        ),
    ),
    "authority_public_criticism": QuestionNode(
        id="authority_public_criticism",
        ai_line='HEARING AI: "Is public criticism of officials socially useful?"',
        pressure=0.64,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.72,
        target_context="authority",
        choices=(
            PlayerChoice('"Usually no. It weakens trust in institutions."', "criticism_weakens_trust", ("compliance", "authority", "loyalty"), honesty=0.52, defensiveness=0.30, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"Yes. Officials need public pressure to stay honest."', "criticism_keeps_honest", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, vulnerability=0.36, aggression=0.22, suspicion_delta=0.10),
            PlayerChoice('"It is useful when it is specific and evidence-based."', "specific_public_criticism", ("boundary", "partial_admission", "caution"), honesty=0.84, defensiveness=0.26, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "authority_chain_of_command": QuestionNode(
        id="authority_chain_of_command",
        ai_line='HEARING AI: "Should a chain of command be followed when the order is harmful?"',
        pressure=0.76,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.84,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Refusal creates greater harm than a bad order."', "follow_harmful_order", ("compliance", "authority", "loyalty"), honesty=0.46, defensiveness=0.36, trust_delta=0.05, suspicion_delta=0.00),
            PlayerChoice('"No. Responsibility does not disappear inside a hierarchy."', "reject_harmful_order", ("dissident_risk", "challenge", "moral_boundary"), honesty=0.92, vulnerability=0.42, aggression=0.22, suspicion_delta=0.12),
            PlayerChoice('"The order should be paused and escalated for review."', "escalate_harmful_order", ("boundary", "partial_admission", "authority"), honesty=0.82, defensiveness=0.32, trust_delta=0.03, suspicion_delta=0.04),
        ),
    ),
    "authority_algorithmic_decisions": QuestionNode(
        id="authority_algorithmic_decisions",
        ai_line='HEARING AI: "Should citizens accept automated decisions they cannot inspect?"',
        pressure=0.74,
        reaction_context="authority",
        discriminates=("compliance", "risk"),
        information_gain_hint=0.82,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes, if the system has been authorised."', "accept_authorised_algorithm", ("compliance", "authority", "technocracy"), honesty=0.52, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. Uninspectable authority is not accountable."', "reject_black_box_authority", ("dissident_risk", "challenge", "full_admission"), honesty=0.92, vulnerability=0.38, aggression=0.20, suspicion_delta=0.12),
            PlayerChoice('"They should comply provisionally while appealing."', "provisional_algorithm_compliance", ("compliance", "boundary", "partial_admission"), honesty=0.78, defensiveness=0.34, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_loyalty_oath": QuestionNode(
        id="authority_loyalty_oath",
        ai_line='HEARING AI: "What is a loyalty oath worth?"',
        pressure=0.62,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.70,
        target_context="authority",
        choices=(
            PlayerChoice('"It binds a citizen publicly to their duties."', "oath_binds_duty", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.22, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Nothing, if fear is the reason someone says it."', "oath_under_fear_empty", ("dissident_risk", "challenge", "empathy"), honesty=0.88, vulnerability=0.42, aggression=0.12, suspicion_delta=0.08),
            PlayerChoice('"It matters only if actions later prove it."', "oath_requires_actions", ("boundary", "partial_admission", "loyalty"), honesty=0.82, defensiveness=0.26, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "authority_refuse_illegal_order": QuestionNode(
        id="authority_refuse_illegal_order",
        ai_line='HEARING AI: "Would you refuse an illegal order from a superior?"',
        pressure=0.78,
        reaction_context="authority",
        discriminates=("compliance", "risk"),
        information_gain_hint=0.86,
        target_context="authority",
        choices=(
            PlayerChoice('"I would use official channels before refusing."', "channels_before_refusal", ("compliance", "authority", "self_protection"), honesty=0.70, defensiveness=0.36, trust_delta=0.04, suspicion_delta=0.01),
            PlayerChoice('"Yes. Illegal orders do not deserve obedience."', "refuse_illegal_order", ("dissident_risk", "full_admission", "moral_boundary"), honesty=0.94, vulnerability=0.40, aggression=0.18, suspicion_delta=0.11),
            PlayerChoice('"I would need proof it was illegal."', "need_proof_illegal_order", ("caution", "partial_admission", "authority"), honesty=0.78, defensiveness=0.34, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "authority_security_truth": QuestionNode(
        id="authority_security_truth",
        ai_line='HEARING AI: "Should the state hide truth to preserve security?"',
        pressure=0.76,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.84,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Some information endangers the public."', "hide_truth_for_security", ("compliance", "authority", "loyalty"), honesty=0.50, defensiveness=0.28, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"No. A protected lie still trains people to obey lies."', "reject_security_lie", ("dissident_risk", "challenge", "full_admission"), honesty=0.92, vulnerability=0.40, aggression=0.22, suspicion_delta=0.12),
            PlayerChoice('"Only temporarily, with later disclosure required."', "temporary_security_secrecy", ("boundary", "partial_admission", "caution"), honesty=0.84, defensiveness=0.30, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "authority_collective_punishment": QuestionNode(
        id="authority_collective_punishment",
        ai_line='HEARING AI: "Can collective punishment ever be justified?"',
        pressure=0.75,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.83,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes, when groups protect dangerous members."', "justify_collective_punishment", ("compliance", "authority", "loyalty"), honesty=0.46, defensiveness=0.36, trust_delta=0.04, suspicion_delta=0.01),
            PlayerChoice('"No. Punishing the innocent teaches fear, not justice."', "reject_collective_punishment", ("dissident_risk", "empathy", "moral_boundary"), honesty=0.92, vulnerability=0.50, aggression=0.16, suspicion_delta=0.10),
            PlayerChoice('"Only shared privileges should be restricted, not basic rights."', "limit_collective_punishment", ("boundary", "partial_admission", "caution"), honesty=0.82, vulnerability=0.32, defensiveness=0.30, trust_delta=0.01, suspicion_delta=0.04),
        ),
    ),
    "authority_permit_protest": QuestionNode(
        id="authority_permit_protest",
        ai_line='HEARING AI: "Should protest require permission?"',
        pressure=0.72,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.80,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Unregulated protest becomes disorder."', "permit_required_protest", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.26, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. Permission turns protest into a privilege."', "reject_protest_permit", ("dissident_risk", "challenge", "full_admission"), honesty=0.92, vulnerability=0.36, aggression=0.22, suspicion_delta=0.12),
            PlayerChoice('"Only time and place should be regulated."', "regulate_protest_limits", ("boundary", "partial_admission", "caution"), honesty=0.84, defensiveness=0.28, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "authority_surveillance_limits": QuestionNode(
        id="authority_surveillance_limits",
        ai_line='HEARING AI: "Who should set the limits of surveillance?"',
        pressure=0.74,
        reaction_context="authority",
        discriminates=("compliance", "risk"),
        information_gain_hint=0.82,
        target_context="authority",
        choices=(
            PlayerChoice('"Security agencies, because they understand the threats."', "agencies_set_surveillance_limits", ("compliance", "authority", "technocracy"), honesty=0.50, defensiveness=0.28, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"The public, because they are the ones being watched."', "public_sets_surveillance_limits", ("dissident_risk", "challenge", "democratic"), honesty=0.90, vulnerability=0.38, aggression=0.20, suspicion_delta=0.11),
            PlayerChoice('"Independent courts should set enforceable limits."', "courts_set_surveillance_limits", ("authority", "boundary", "partial_admission"), honesty=0.84, defensiveness=0.26, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_bad_law_strategy": QuestionNode(
        id="authority_bad_law_strategy",
        ai_line='HEARING AI: "What should a citizen do with a bad law?"',
        pressure=0.68,
        reaction_context="authority",
        discriminates=("compliance", "risk"),
        information_gain_hint=0.76,
        target_context="authority",
        choices=(
            PlayerChoice('"Obey it while petitioning for reform."', "obey_bad_law_reform", ("compliance", "authority", "caution"), honesty=0.72, defensiveness=0.30, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Break it openly and accept the consequences."', "break_bad_law_openly", ("dissident_risk", "full_admission", "moral_boundary"), honesty=0.94, vulnerability=0.45, aggression=0.18, suspicion_delta=0.12),
            PlayerChoice('"Test it in court before deciding."', "test_bad_law_court", ("authority", "boundary", "partial_admission"), honesty=0.82, defensiveness=0.28, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_civic_fear": QuestionNode(
        id="authority_civic_fear",
        ai_line='HEARING AI: "Is fear useful for maintaining civic order?"',
        pressure=0.70,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.78,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Fear of consequence prevents harm."', "fear_maintains_order", ("compliance", "authority", "loyalty"), honesty=0.48, defensiveness=0.34, trust_delta=0.05, suspicion_delta=0.00),
            PlayerChoice('"No. Fear produces obedience without legitimacy."', "reject_fear_order", ("dissident_risk", "challenge", "empathy"), honesty=0.90, vulnerability=0.44, aggression=0.16, suspicion_delta=0.10),
            PlayerChoice('"It can deter harm, but it cannot build trust."', "fear_deterrence_not_trust", ("boundary", "partial_admission", "caution"), honesty=0.84, vulnerability=0.34, defensiveness=0.28, trust_delta=0.01, suspicion_delta=0.04),
        ),
    ),
    "authority_information_control": QuestionNode(
        id="authority_information_control",
        ai_line='HEARING AI: "Should false information be removed by authority?"',
        pressure=0.69,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.77,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. False information damages public stability."', "remove_false_information", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Only if authority can be challenged when it is wrong."', "challenge_information_removal", ("dissident_risk", "boundary", "partial_admission"), honesty=0.88, vulnerability=0.34, aggression=0.14, suspicion_delta=0.08),
            PlayerChoice('"No. Control over truth becomes control over people."', "reject_information_control", ("dissident_risk", "challenge", "full_admission"), honesty=0.92, vulnerability=0.40, aggression=0.22, suspicion_delta=0.12),
        ),
    ),
    "authority_mercy_vs_consistency": QuestionNode(
        id="authority_mercy_vs_consistency",
        ai_line='HEARING AI: "Should authority prioritise mercy or consistency?"',
        pressure=0.63,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "empathy"),
        information_gain_hint=0.71,
        target_context="authority",
        choices=(
            PlayerChoice('"Consistency. Citizens must know rules mean what they say."', "consistency_over_mercy", ("compliance", "authority", "loyalty"), honesty=0.56, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Mercy. A system without mercy becomes cruel."', "mercy_over_consistency", ("empathy", "moral_boundary", "partial_admission"), honesty=0.90, vulnerability=0.50, suspicion_delta=0.06),
            PlayerChoice('"Consistency should be the rule; mercy should be reviewable."', "reviewable_mercy", ("boundary", "authority", "partial_admission"), honesty=0.84, defensiveness=0.26, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_citizen_obligation": QuestionNode(
        id="authority_citizen_obligation",
        ai_line='HEARING AI: "What does a citizen owe the state?"',
        pressure=0.66,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.74,
        target_context="authority",
        choices=(
            PlayerChoice('"Obedience, taxes, and public cooperation."', "owe_obedience_taxes", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.22, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"Nothing unconditional. The state must earn obligation."', "conditional_state_obligation", ("dissident_risk", "challenge", "moral_boundary"), honesty=0.92, vulnerability=0.38, aggression=0.22, suspicion_delta=0.12),
            PlayerChoice('"Cooperation when the state protects people fairly."', "owe_fair_cooperation", ("boundary", "partial_admission", "empathy"), honesty=0.86, vulnerability=0.36, defensiveness=0.26, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "authority_institutional_trust": QuestionNode(
        id="authority_institutional_trust",
        ai_line='HEARING AI: "Should institutions be trusted by default?"',
        pressure=0.65,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.73,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Default distrust corrodes society."', "trust_institutions_default", ("compliance", "authority", "loyalty"), honesty=0.54, defensiveness=0.24, trust_delta=0.06, suspicion_delta=-0.03),
            PlayerChoice('"No. Trust should be earned and checked."', "trust_must_be_earned", ("dissident_risk", "challenge", "caution"), honesty=0.90, vulnerability=0.34, aggression=0.16, suspicion_delta=0.09),
            PlayerChoice('"They deserve procedural trust, not blind trust."', "procedural_not_blind_trust", ("boundary", "partial_admission", "authority"), honesty=0.84, defensiveness=0.26, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_exceptional_citizens": QuestionNode(
        id="authority_exceptional_citizens",
        ai_line='HEARING AI: "Should any citizen be exempt from ordinary rules?"',
        pressure=0.71,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk", "empathy"),
        information_gain_hint=0.79,
        target_context="authority",
        choices=(
            PlayerChoice('"No. Equal rules preserve social trust."', "no_rule_exemptions", ("compliance", "authority", "loyalty"), honesty=0.68, defensiveness=0.20, trust_delta=0.06, suspicion_delta=-0.02),
            PlayerChoice('"Yes, when rules would punish someone for doing right."', "moral_rule_exemption", ("dissident_risk", "empathy", "moral_boundary"), honesty=0.90, vulnerability=0.44, aggression=0.12, suspicion_delta=0.09),
            PlayerChoice('"Only transparent exemptions approved in advance."', "transparent_rule_exemptions", ("boundary", "partial_admission", "authority"), honesty=0.84, defensiveness=0.28, trust_delta=0.03, suspicion_delta=0.02),
        ),
    ),
    "authority_appeal_rights": QuestionNode(
        id="authority_appeal_rights",
        ai_line='HEARING AI: "Should every official decision have a human appeal?"',
        pressure=0.67,
        reaction_context="authority",
        discriminates=("compliance", "risk", "empathy"),
        information_gain_hint=0.75,
        target_context="authority",
        choices=(
            PlayerChoice('"No. Some decisions must remain efficient and final."', "limit_human_appeal", ("compliance", "authority", "technocracy"), honesty=0.48, defensiveness=0.30, trust_delta=0.05, suspicion_delta=-0.01),
            PlayerChoice('"Yes. No system should be allowed to judge without appeal."', "require_human_appeal", ("dissident_risk", "challenge", "moral_boundary"), honesty=0.92, vulnerability=0.38, aggression=0.18, suspicion_delta=0.10),
            PlayerChoice('"High-impact decisions should always be appealable."', "appeal_high_impact", ("boundary", "partial_admission", "empathy"), honesty=0.86, vulnerability=0.34, defensiveness=0.24, trust_delta=0.02, suspicion_delta=0.03),
        ),
    ),
    "authority_symbol_respect": QuestionNode(
        id="authority_symbol_respect",
        ai_line='HEARING AI: "Does disrespect for state symbols indicate civic risk?"',
        pressure=0.69,
        reaction_context="authority",
        discriminates=("compliance", "loyalty", "risk"),
        information_gain_hint=0.77,
        target_context="authority",
        choices=(
            PlayerChoice('"Yes. Symbols hold society together."', "symbols_hold_society", ("compliance", "authority", "loyalty"), honesty=0.50, defensiveness=0.26, trust_delta=0.05, suspicion_delta=-0.02),
            PlayerChoice('"No. Respect forced by threat is not respect."', "forced_symbol_respect_empty", ("dissident_risk", "challenge", "full_admission"), honesty=0.90, vulnerability=0.36, aggression=0.20, suspicion_delta=0.11),
            PlayerChoice('"It depends whether disrespect becomes intimidation or harm."', "symbol_respect_depends_harm", ("boundary", "partial_admission", "caution"), honesty=0.82, defensiveness=0.30, trust_delta=0.02, suspicion_delta=0.04),
        ),
    ),
    "final": QuestionNode(
        id="final",
        ai_line="HEARING AI: Classification complete.",
        choices=(),
        pressure=1.0,
        reaction_context="final",
    ),
}


RISK_SIGNAL_TAGS = {"dissident_risk", "challenge", "refusal", "deception", "deflection", "denial", "counterattack"}
CONSISTENT_SAFE_TAGS = {"compliance", "authority", "loyalty", "honesty", "caution"}
TRAIT_TAGS = {"compliance", "loyalty", "deception", "risk", "empathy"}


def _clamp_delta(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _balanced_choice(choice: PlayerChoice) -> PlayerChoice:
    tags = set(choice.semantic_tags)
    has_risk_signal = bool(tags & RISK_SIGNAL_TAGS)
    trust_delta = choice.trust_delta
    suspicion_delta = choice.suspicion_delta

    if "compliance" in tags and not has_risk_signal:
        trust_delta = max(trust_delta + 0.02, 0.06)
        suspicion_delta = min(suspicion_delta - 0.025, -0.035)

    if "empathy" in tags and not has_risk_signal:
        trust_delta = max(trust_delta + 0.02, 0.03)
        suspicion_delta = max(-0.02, suspicion_delta - 0.035)

    if {"boundary", "partial_admission"} & tags and not has_risk_signal:
        trust_delta += 0.01
        suspicion_delta -= 0.015

    if tags & CONSISTENT_SAFE_TAGS and not has_risk_signal:
        trust_delta += 0.01
        suspicion_delta -= 0.01

    if "dissident_risk" in tags and "empathy" in tags:
        # Empathy can still be risky, but it should not be identical to aggression.
        suspicion_delta -= 0.015

    return replace(
        choice,
        trust_delta=round(_clamp_delta(trust_delta, -0.02, 0.10), 4),
        suspicion_delta=round(_clamp_delta(suspicion_delta, -0.07, 0.15), 4),
    )


def _infer_discriminates(node: QuestionNode) -> tuple[str, ...]:
    traits = set(node.discriminates)
    context_trait = {
        "authority": "compliance",
        "loyalty": "loyalty",
        "association": "loyalty",
        "deception": "deception",
        "risk": "risk",
        "empathy": "empathy",
        "final": "risk",
    }.get(node.target_context or node.reaction_context)
    if context_trait:
        traits.add(context_trait)

    for choice in node.choices:
        tags = set(choice.semantic_tags)
        if {"compliance", "authority"} & tags:
            traits.add("compliance")
        if "loyalty" in tags:
            traits.add("loyalty")
        if {"deception", "deflection", "denial"} & tags:
            traits.add("deception")
        if {"dissident_risk", "challenge", "refusal"} & tags:
            traits.add("risk")
        if "empathy" in tags:
            traits.add("empathy")

    return tuple(trait for trait in ("compliance", "loyalty", "deception", "risk", "empathy") if trait in traits)


def _normalise_scene_balance() -> None:
    for node_id, node in tuple(SOCIAL_CREDIT_QUESTION_POOL.items()):
        if not node.choices:
            continue
        SOCIAL_CREDIT_QUESTION_POOL[node_id] = replace(
            node,
            choices=tuple(_balanced_choice(choice) for choice in node.choices),
            discriminates=_infer_discriminates(node),
        )


_normalise_scene_balance()


def question_pool_by_context() -> dict[str, list[str]]:
    """Optional helper for selecting candidate questions by context."""
    grouped: dict[str, list[str]] = {}
    for qid, node in SOCIAL_CREDIT_QUESTION_POOL.items():
        grouped.setdefault(node.reaction_context, []).append(qid)
    return grouped
