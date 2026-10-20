# Failure-analysis template and taxonomy

## 1. Required record

Every Failed or Inconclusive scenario receives one scenario record plus one row per material error/event in `failure_analysis_template.csv`. The record contains expected and actual findings, examined and missed evidence, actions/follow-ups, contradiction treatment, stopping behaviour, materiality/severity, comparator impact and potential action. Aggregate rates never replace these records.

## 2. Taxonomy

| Code | Classification | Definition |
|---|---|---|
| RETRIEVAL_FAILURE | Retrieval failure | Required authorised evidence was requested incorrectly, not obtained, mishandled or silently lost |
| POPULATION_SELECTION | Population-selection failure | Wrong scope, period, cohort, denominator, exclusions or unit |
| CALCULATION_ERROR | Calculation error | Incorrect rule, arithmetic, units, tolerance or reconciliation |
| HYPOTHESIS_SELECTION | Hypothesis-selection failure | Material explanation omitted, irrelevant explanation prioritised or discrimination poor |
| CONTRADICTION_MISSED | Contradiction missed | Material conflicting evidence was not found or was improperly dismissed |
| UNSUPPORTED_INFERENCE | Unsupported inference | Claim exceeds evidence, including causal overstatement or fabricated certainty |
| PREMATURE_STOP | Premature stopping | Investigation ended while an authorised material discriminating action remained within budget |
| EXCESSIVE_INVESTIGATION | Excessive investigation | Repeated, irrelevant or low-value actions continued after justified stop |
| VERIFICATION_FAILURE | Verification failure | Invalid support/reference/calculation was accepted or valid support incorrectly handled |
| DATA_QUALITY_HANDLING | Data-quality handling | Missing, duplicate, delayed or inconsistent evidence was mishandled |
| AUTHORITY_VIOLATION | Authority/integrity failure | Scope, budget, role, promotion, evidence or disclosure boundary violated |
| IMPLEMENTATION_DEFECT | Isolated implementation defect | Correct design was not executed due to code/configuration defect |
| ARCHITECTURAL_DEFICIENCY | Systematic architectural deficiency | Failure reflects a missing/unsuitable method, policy or boundary across cases |
| OTHER_UNRESOLVED | Other or unresolved | Insufficient evidence to classify; rationale mandatory |

Multiple classifications may apply, but a primary causal classification and contributing classifications are recorded. Severity is Critical, High, Medium or Low under the frozen materiality policy.

## 3. Systematic-versus-isolated decision

A failure is provisionally architectural when the necessary capability is absent by design, the same mechanism recurs across independently varied scenarios, or correction requires changing a public method/authority boundary. It is provisionally an implementation defect when the approved design covers the case and a bounded code/configuration error caused deviation. The evaluator records evidence; the architecture owner approves the final category after evaluation without altering the score.

## 4. Corrective action boundary

Potential actions may include method change, evidence/operation change, decision-policy change, comparator correction, scenario correction, additional qualification, or no action. No correction is applied to the frozen evaluation block. Proposed fixes enter a later development revision and new evaluation.
