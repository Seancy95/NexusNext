# CLOUD-EVAL Path A Contract

## 1. Scope

Path A is the deterministic investigation strategy used as the required baseline in CLOUD-EVAL. It is a new Nexus Next component. It does not wrap, import, call or reproduce the Nexus 10.3.43 analytical engines by default. Confirmed domain knowledge may later be re-expressed through approved Nexus Next domain packages.

This document is a proposed contract for review. It does not authorise implementation or benchmark execution.

## 2. Shared contracts for Paths A, B and C

All paths consume and emit the same versioned logical types:

| Type | Required meaning |
|---|---|
| `ScenarioContext` | Non-secret run identifier, scenario revision, authorised source IDs, category, initial evidence set and applicable policy versions; excludes hidden ground truth and rubric |
| `EvidenceRef` | Stable evidence-unit ID, source/snapshot ID, content digest, type, scope, acquisition time, lineage and permitted claim uses |
| `RetrievalRequest` | Operation/actor, source, typed query, field/scope limit, round, purpose and maximum cost |
| `RetrievalResult` | Evidence refs plus complete/partial/denied/failed status, cursor, diagnostics and charged cost |
| `InvestigationBudget` | Hard ceilings by round, retrieval request, evidence unit/byte, elapsed time, retry and operator-intervention dimensions; path-specific compute dimensions are supplementary |
| `BudgetLedger` | Atomic charges, remaining budget, failed/retried calls and terminal exhaustion state |
| `AnalysisOperation` | Stable operation/version, input/output schemas, deterministic configuration, domain-package dependencies and cost function |
| `Hypothesis` | Non-authoritative lead, trigger evidence, rationale, uncertainty, disconfirming evidence sought and priority |
| `ProposedFinding` | Typed claim, scope, materiality, supporting/refuting evidence, qualifications, uncertainty and proposer identity |
| `VerificationDecision` | Independent `accepted`, `rejected` or `unresolved` decision, verifier identity/role, checked evidence, rationale and time |
| `InvestigationResult` | Terminal state, operations, hypotheses, proposed findings, verification references, failures, unused questions, budget and provenance |
| `CanonicalReport` | Facts and findings selected by verification state, evidence references, qualifications, omissions and projection policy; editorial text is a derived view |

Every serialized object carries schema version and stable digest. Evidence remains local. Investigator inputs cannot expose hidden ground truth, expected findings, rubric weights or protected mappings.

## 3. Path A execution

Path A operates a deterministic state machine:

1. Validate `ScenarioContext`, permissions, configuration and budget.
2. Discover only authorised source capabilities.
3. Select the next registered deterministic operation from the same visible investigation state.
4. Retrieve through the common interface and charge the common ledger before processing.
5. Record operation inputs, version, domain package, outputs and failures.
6. Update profiles, relationships, contradictions, hypotheses and evidence-sufficiency state.
7. Continue, stop or declare an incomplete state under declared rules.
8. Submit proposed findings and frozen evidence bundles to the independent verifier.
9. Produce a canonical result that preserves hypothesis/proposal/decision boundaries.
10. Project the common canonical report without changing verification state.

The operation registry must include general-purpose profiling, rule evaluation, KPI/SLA calculation, descriptive and inferential statistical analysis, trend analysis, anomaly detection, entity/relationship discovery, contradiction detection and evidence-sufficiency evaluation. Scenario-specific templates may guide operation selection but cannot be the only investigative ability.

For frozen evidence, configuration, operation versions, clock, seed (where an approved algorithm uses one) and budget, Path A must produce byte-stable canonical outputs or document fields deliberately excluded from stable serialization. Retries cannot change semantic results silently.

## 4. Investigation and finding states

### Investigation terminal state

- `completed`: declared stop criteria met within budget;
- `partial`: valid work exists but one or more declared investigation objectives remain incomplete;
- `inconclusive`: available evidence cannot resolve material questions;
- `blocked`: a permission, prerequisite or source condition prevents meaningful progress;
- `failed`: an internal/schema/integrity error invalidates the run output;
- `budget_exhausted`: a hard limit ended the run before normal stopping criteria.

A result may contain both valid proposed findings and a non-completed terminal state. Reports and scores must preserve the state and its impact.

### Claim state

`hypothesis` → `proposed` → independently `accepted`, `rejected` or `unresolved`. Path A has no transition to `accepted`. A material contradiction, invalid evidence reference or unmet sufficiency rule prevents unqualified proposal or forces the configured qualification. Verification failures remain individual events under B01.

## 5. Equivalent evidence access and budgets

Paths A, B and C receive the same scenario revision, initial evidence IDs, source permissions, retrieval endpoints, result schemas, round limits, evidence-unit/byte ceilings, retries and stopping policy. They use the same local verifier and canonical reporting foundation. Path C receives privacy-transformed representations as required by B01; the evaluator tracks transformation loss and graph invariants. Path B/C model context must be assembled only from authorised retrieval results.

Equivalent access means equal opportunity to request semantically equivalent evidence, not identical internal representation or compute. The controller records:

- evidence IDs available, requested, returned and actually exposed;
- fields/relationships suppressed or transformed and why;
- calls, records, bytes, rounds, retries and elapsed time;
- deterministic CPU/memory and model token/inference measures as path-specific operational metrics; and
- tool or representation differences that can affect conclusions.

Token budgets cannot be made equivalent to rows, graph traversals or deterministic CPU work. Privacy transformation also makes B and C representations deliberately non-identical. These differences must be preregistered, reported as limitations and considered when interpreting A–B/A–C/B–C effects. The benchmark must not compensate by giving Path A weaker retrieval, evidence references, verification or reporting tools.

## 6. Failure and uncertainty contract

Retrieval and operations return typed outcomes: `success`, `partial`, `denied`, `not_available`, `invalid_request`, `timeout`, `integrity_failure`, `internal_failure` and `budget_denied`. Partial data never masquerades as complete. Each failure records affected scope, retryability, attempt count and budget effect.

Numerical results declare population/sample, missingness, method, assumptions, precision and applicable interval. Relationship outputs declare exact/rule-based/probabilistic origin and ambiguity. Domain rules declare authority/version/effective period. Unknown, absent, not applicable, contradicted and not tested remain distinct.

## 7. Local verification and reporting

Verification resolves every evidence reference against the frozen local ledger, checks source/scope/digest, evaluates the claim-specific sufficiency policy, examines cited refuting evidence and material qualifications, and records a separate decision. A verifier cannot silently edit a claim; corrections create a new proposal linked to the old record.

The canonical report contains investigation scope and state, accepted findings, rejected/unresolved proposal summaries where policy requires, material qualifications, evidence coverage, contradictions, failures and provenance. Editorial projectors can change order, wording and audience-appropriate detail only. They cannot alter metric values, omit mandatory qualifications, elevate hypotheses, accept findings or remove failure state. Every format is tested against the same canonical fixture.

## 8. Acceptance criteria

### Contract and behavioral acceptance

Path A is conformant only when:

1. all shared schemas and state transitions pass synthetic positive and negative fixtures;
2. repeated frozen-input executions meet the declared determinism rule;
3. unauthorised sources/fields and over-budget operations fail closed;
4. complete lineage resolves from canonical output to immutable evidence and operation configuration;
5. injected missingness, contradictions, false joins, stale evidence and invalid references retain their distinct states;
6. hypotheses cannot appear as accepted findings without an independent decision;
7. each required general capability passes its objective catalogue criteria;
8. all report formats preserve required findings, values and qualifications; and
9. implementation, test platform, source revision and untested behavior are reported accurately.

### Comparative acceptance

Before results are observed, the evaluation plan must freeze scenario categories, path configurations, budgets, comparison methods, numerical thresholds and permitted differences. For each scenario/path, the evaluator checks evidence-exposure parity, budget enforcement, completion state, critical-finding recall, material precision, unsupported conclusions, evidence-reference validity, qualifications, contradiction handling and operational cost as specified by B01. Experimental validity, investigative performance, privacy/security, verification integrity and deployment readiness receive independent Passed/Failed/Inconclusive/Not Tested results.

No numerical pass thresholds are supplied here because the accessible approved materials require preregistration and owner ratification. They are **Requires confirmation**. Any prohibited disclosure fails its applicable safety/publication gate; any unsupported material finding accepted as verified fails its applicable verification/publication gate, without erasing otherwise valid comparative measurements.

## 9. Security and operational boundaries

Path A uses synthetic or separately authorised local evidence through read-only interfaces. It cannot call external AI services, access evaluator truth, modify a source, widen permissions, write security policy or create an unauthorised secondary evidence store. Logs obey scenario retention/disclosure policy and store references or minimised payloads where full evidence is unnecessary.

This design creates no dependency on the G2 harness and authorises no G2 phase activity.
