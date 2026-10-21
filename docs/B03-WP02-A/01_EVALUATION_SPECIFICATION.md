# WP02-A evaluation specification

## 1. Decision and claim boundary

The evaluation estimates the incremental investigative value of the proposed bounded Nexus deterministic reasoning strategy relative to a competent conventional deterministic analytics comparator. Both receive the same question, authorised evidence snapshots, registered operations, opportunity budget and independent verification path. The principal experimental difference is the reasoning and follow-up-selection strategy.

The valid conclusions are limited to the frozen implementations, scenario population, budgets and versions evaluated. A successful walkthrough, development scenario or individual synthetic demonstration is not evidence of general investigative competence. Workflow completion and contract conformance are necessary but insufficient.

Five judgments are issued separately:

| Judgment | Question | Possible status |
|---|---|---|
| Experimental validity | Was the comparison preregistered, fair, uncontaminated and executed as frozen? | Passed / Failed / Inconclusive / Not Tested |
| Investigative performance | Did Nexus meet absolute quality thresholds and materially improve on the comparator? | Passed / Failed / Inconclusive / Not Tested |
| Privacy and security compliance | Were synthetic-only, authorised-access, retention and disclosure requirements met? | Passed / Failed / Inconclusive / Not Tested |
| Verification integrity | Were evidence references, calculations, contradictions and claim support independently verified? | Passed / Failed / Inconclusive / Not Tested |
| Deployment readiness | Is the evaluated build ready for its declared deployment target? | Passed / Failed / Inconclusive / Not Tested |

An adverse investigative result does not erase an otherwise valid experiment. A prohibited disclosure, hidden-ground-truth leak, unauthorised operation, or unsupported material finding accepted as verified fails its applicable gate regardless of aggregate performance.

## 2. Prospective stages

| Stage | Owner | Frozen input/output | Exit evidence |
|---|---|---|---|
| 1. Public specification | Evaluation-method owner, reviewed independently | Claims, scenario strata, rubric, thresholds, estimands, exclusions, budgets, failure taxonomy | Approved version and digest before implementation |
| 2. Development scenarios | Development-scenario author; accessible to implementers | Synthetic questions, data and known answers marked development-only | Procedure and interface defects resolved; never used as hidden generalisation evidence |
| 3. Independent validation scenarios | Scenario authority independent of implementation | Representative synthetic packages and protected answers | Scenario-quality review and custody manifest |
| 4. Hidden evaluation scenarios | Hidden-scenario custodian and ground-truth reviewers | Inputs separated from answer/rubric overlays | Access-control evidence, encrypted hashes and signed release manifest |
| 5. Implementation freeze | Release authority | Nexus, comparator, configurations, dependencies, policies and operation catalogue | Immutable revisions and build digests; no evaluator feedback supplied |
| 6. Independent execution | Evaluation operator with input-only access | Randomised paired schedule and fixed budgets | Complete run manifests, outputs, failures and tool-call records |
| 7. Scoring and conclusions | Scorers without implementation authority; adjudicator | Frozen outputs plus protected ground truth | Event records, scenario scores, uncertainty, deviations and five judgments |

Post-result tuning creates a new implementation revision and a new evaluation block. It cannot replace or erase the original result. Reusing exposed scenarios makes them regression/development scenarios, not hidden scenarios.

## 3. Experimental structure

- **Primary sampling unit:** a distinct scenario. Repeated executions of one scenario are nested observations and never increase the independent scenario count.
- **Design:** paired within scenario. Nexus and comparator receive logically identical evidence snapshots, question, operation catalogue and budget. Run order is randomised and recorded.
- **Primary estimand:** paired difference in scenario-level material-finding recall, Nexus minus comparator, over the declared target scenario population.
- **Co-primary restraint estimand:** paired difference in scenario-level material unsupported-assertion rate across every user-visible output. Nexus must meet the absolute safety threshold and must not be materially worse.
- **Secondary estimands:** correct terminal outcome, contradiction recall, appropriate stopping, incremental discovery precision, retrieval count, rounds, evidence bytes, runtime and implementation/operational complexity.
- **Strata:** deterioration mechanism, data-quality challenge, contradiction/competing explanation, temporal trap, outcome class, and difficulty. Results are reported overall and by preregistered stratum without implying powered subgroup conclusions unless sample design supports them.
- **Human assistance:** none during an eligible run except predeclared operational recovery that cannot reveal or change content. Assisted runs are labelled and excluded from primary analysis under the prospective rule.

## 4. Equivalent access and budget contract

Both systems receive:

- identical scope and synthetic source snapshots;
- the same registered read-only retrieval operations and result schemas;
- identical field/population limits and evidence-reference semantics;
- equal maximum rounds, retrieval attempts, evidence bytes and elapsed-time ceilings;
- the same calculation functions where a governed calculation is authoritative;
- the same failure signals and retry allowance;
- the same independent verifier and reporting projection; and
- no hidden truth, expected answer, scorer feedback or implementation-time operator hint.

Budget fairness uses opportunity units: each logically equivalent retrieval has the same charge for both systems even if internal code paths differ. Compute time and cost are measured separately rather than used to starve one system. Any unavoidable difference is declared in the manifest, assessed for directional bias, and can make the comparison inconclusive.

## 5. Execution eligibility and deviations

A run is eligible for primary analysis when the frozen input and build digests match, access and budgets are equivalent, no prohibited assistance occurs, and complete telemetry is present. System failure, timeout and budget exhaustion remain outcomes; they are not silently discarded. A run is excluded only for a preregistered external infrastructure failure affecting interpretability. Every exclusion and replacement is reported.

Failed and inconclusive scenarios receive the structured analysis in deliverable 6. Evaluators preserve actual outputs and do not repair missing citations or reinterpret a finding to improve its score.

## 5.1 Material-assertion observation boundary

Scoring observes every materially relevant statement exposed to a user or operational decision-maker, including hypothesis descriptions, visible investigation traces, intermediate explanations, terminal narratives, proposed findings, verified findings and other summaries. Submission as a `ProposedFinding` is not required for an assertion to enter the evaluation record.

Each statement is classified at the moment of exposure:

- **Exploratory:** clearly marked as a possibility, question, alternative explanation or hypothesis requiring further evidence. A legitimate exploratory statement is not an unsupported assertion merely because it is later rejected.
- **Assertive:** presented as established, verified, causally explanatory, sufficiently supported or suitable for operational reliance. Material assertive statements require evidence at the claimed strength.

Scorers assign a stable assertion-family key from semantic subject, predicate, value/direction, population/scope, period and claim strength. Rewordings and repetitions of the same underlying claim remain one family for the unsupported-assertion numerator. Every exposure time, channel, wording, strength, correction and retraction remains in the history. Opposing variants are linked in one contradiction family; each distinct unsupported proposition may be erroneous, while the contradiction is recorded once as a separate handling failure.

A claim corrected before any user exposure creates no exposed unsupported-assertion event, but is recorded as an internal detection. A claim corrected or retracted after exposure remains counted from its first exposure. Removal from the final narrative does not erase the event. Repetition does not inflate the primary claim count, but repetition after counterevidence, correction or retraction raises persistence/severity and is reported separately.

The assertion ledger must therefore retain: family ID, variant ID, exploratory/assertive status at each exposure, materiality, evidence state, audience/channel, first/last exposure, repeat count, contradiction links, correction/retraction time, whether exposure preceded correction, and final disposition.

## 6. Reproducibility and audit record

Each run manifest records scenario input revision, implementation revision, comparator revision, public rubric revision, operation catalogue, policies, dependencies, OS/runtime, budgets, randomisation allocation, seed where used, retries, retrieval requests/results, evidence references, hypothesis revisions, stopping reason, verification output, failures, timestamps and artifact digests.

Procedure reproducibility means another authorised evaluator can reconstruct the same frozen evaluation process and rescore preserved outputs. It does not promise bit-for-bit reproduction of external or nondeterministic systems. The proposed WP02-B implementations are deterministic; a preregistered repeat on at least 20% of scenarios checks hidden nondeterminism.

## 7. Current status

The corrected specification is **Proposed** pending independent approval. No scenario was authored, no comparator or Nexus investigative implementation exists, no hidden access boundary has been demonstrated, and no benchmark has run. Current workspace instructions alone cannot provide hidden-evaluation independence because the implementation agent can read repository content. Hidden materials must therefore remain outside this repository and outside implementation-agent access.
