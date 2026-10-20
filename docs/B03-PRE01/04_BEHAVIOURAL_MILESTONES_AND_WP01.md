# Behavioural Milestones and B03-WP01 Proposal

## 1. Milestone principles

Each milestone must deliver one coherent question-to-decision behaviour, but completing that workflow does not establish analytical success. Infrastructure that cannot yet support its milestone scenario is recorded as partial implementation, not a completed milestone. Approval requires the exact implementation revision, executed synthetic tests, evidence and limitations. None of these milestones is authorised by PRE01.

> **Generalisation warning:** A successful walkthrough, pilot investigation, worked example or individual synthetic demonstration shall not be presented as evidence of general investigative competence. Workflow and contract conformance are necessary foundations only. Competence requires independent assessment across representative and previously unseen scenarios.

## 2. Five independent milestone judgments

Every milestone receives separate results; a pass in one column cannot compensate for failure or absence in another.

| Judgment | Question answered | Minimum evidence |
|---|---|---|
| A. Engineering conformance | Does the implementation obey schemas, permissions, state transitions and authority boundaries? | Positive/negative contract, policy and state-machine tests on an identified revision |
| B. Analytical correctness | Are source/population selection, calculations, denominators, business rules, periods, missing/duplicates, chronology and relationships correct? | Independent reference calculations and labelled golden evidence, including boundary/error cases |
| C. Investigative competence | Does it generate relevant hypotheses, seek disconfirming evidence, select useful follow-ups, handle contradictions, stop appropriately and avoid unsupported causality? | Independent scoring of decision traces and findings against hidden scenario truth/rubrics |
| D. Reliability/generalisation | Does correct behaviour persist across varied, representative and previously unseen scenarios and repeats? | Preregistered held-out scenario families, repeat-run analysis where applicable, error rates/effect sizes and uncertainty |
| E. Security/operational readiness | Are applicable security, retention, deployment, runtime, artifact and organisational controls demonstrated? | Environment-specific G1–G5/SEC evidence and explicit Not Tested/Inconclusive states |

Each judgment uses Passed, Failed, Inconclusive or Not Tested. Numerical thresholds must be approved or prospectively preregistered; they must not be selected after outcomes. Existing B01 zero-tolerance gates remain: a prohibited disclosure fails the applicable safety/publication gate, and an unsupported material finding accepted as verified fails the applicable verification/publication gate.

## 3. Milestone sequence

### Milestone 1 — Governed basic investigation

| Field | Definition |
|---|---|
| Required behaviour | A typed question/scope leads to controller-authorised synthetic retrieval, one deterministic calculation, an evidence-linked proposed finding, and a separate verification decision. |
| Minimum components | Scope parser for one governed vocabulary; controller; one synthetic connector operation; evidence repository; one analysis operation; proposal and verifier; minimal canonical finding projection. |
| Synthetic scenario | “Did September SLA attainment deteriorate versus August?” with complete, partial, denied and contradictory fixture variants. |
| Expected output | Scoped metric/change, evidence refs, proposal, verification decision, terminal state, budget/provenance and minimal canonical projection. |
| Negative/adversarial tests | Unknown metric; ambiguous period; unauthorised source/field; malformed/expired evidence; wrong denominator; self-verification attempt; altered evidence digest; mandatory qualification omitted. |
| Objective acceptance | Controller denies out-of-scope operations; golden calculation matches; proposal cannot be accepted by proposer; independent verifier rejects wrong population/value/reference; identical frozen run is stable; every output resolves to evidence. |
| Approval evidence | Contract/test versions, source revision, full test outcomes, fixture digests, decision log and independent review of supported/not-supported verification recommendations. One scenario does not establish competence. |
| Dependencies | Approved finding-promotion authority; ARC-06/10/11 provisional state authority; SEC retention fields; one approved synthetic metric definition. |
| Stop condition | Stop if authority ownership is ambiguous, evidence lineage breaks, or an unauthorised/self-approved claim can reach canonical output. |

### Milestone 2 — Statistical investigation

| Field | Definition |
|---|---|
| Required behaviour | Starting from a question rather than report template, quantify time/distribution change, detect an anomaly and identify material segments with assumptions/uncertainty. |
| Minimum components | Milestone 1 plus method registry, profiling, time-series/distribution/segmentation/anomaly operations and qualification policy. |
| Synthetic scenarios | Stable series with one outlier; sustained shift; mix shift with no within-segment change; within-segment deterioration; sparse/missing/seasonal variants. |
| Expected output | Method diagnostics, effects and intervals where applicable, anomaly hypotheses, segment contributions, assumptions and qualified proposals. |
| Negative/adversarial tests | Simpson’s paradox; multiple-testing trap; tiny samples; missing period; metric definition change; non-independent repeats treated as independent. |
| Objective acceptance | Reference calculations within declared tolerance; invalid assumptions trigger qualification/failure; segment totals reconcile; no anomaly becomes cause; correct-but-shallow output fails a substantive scenario gate. |
| Approval evidence | Golden datasets, reference implementation/calculations, false-positive/sensitivity results and verifier decisions. |
| Dependencies | Approved method registry and scenario-specific materiality/statistical thresholds. |
| Stop condition | Stop if statistical assumptions are hidden, post-outcome method selection occurs, or aggregate/segment reconciliation fails. |

### Milestone 3 — Relationship and contradiction investigation

| Field | Definition |
|---|---|
| Required behaviour | Discover/traverse structured relations, correlate sources, compare competing claims and preserve unresolved contradiction. |
| Minimum components | Milestones 1–2 plus entity/edge types, matching tiers, authority resolver, traversal and contradiction records. |
| Synthetic scenarios | Exact cross-source link; alias collision; one-to-many join; stale authoritative record; explicit conflict without precedence; missing edge. |
| Expected output | Provenance-bearing paths/matches, ambiguous/rejected links, contradiction disposition and proposed findings with both supporting/refuting evidence. |
| Negative/adversarial tests | Label-only false match; changed identifier; chronology break; source availability treated as authority; missing relation treated as negative. |
| Objective acceptance | No silent collision/join; cardinality preserved; conflict unresolved unless exact rule applies; every path edge resolves; false-link fixtures rejected. |
| Approval evidence | Graph invariants, match confusion matrix by tier, authority decisions, contradiction test record and independent review. |
| Dependencies | Confirmed concept-specific identity/authority rules; relationship retention/classification. |
| Stop condition | Stop if a false join contaminates a finding or a source is silently promoted to global authority. |

### Milestone 4 — Multi-round deterministic investigation

| Field | Definition |
|---|---|
| Required behaviour | Create/test competing hypotheses, select authorised follow-ups through the PRE01 decision policy, update states, assess sufficiency and terminate inspectably. |
| Minimum components | Prior milestones plus hypothesis/evidence-requirement graph, prediction matrix, action candidate/ranking engine, loop ledger, budget/stopping policy. |
| Synthetic scenarios | The September worked investigation; decisive falsifier; observationally equivalent explanations; denied best action; transient failure/retry; exhausted budget; no-progress loop. |
| Expected output | Multi-round action trace, controller decisions, hypothesis revisions, rejected/unresolved alternatives, sufficiency record, terminal reason and proposals. |
| Negative/adversarial tests | Hidden numerical ranking weight; repeat unproductive retrieval; scope expansion after denial; high score self-acceptance; correlation labelled causal; planner-selected arbitrary SQL. |
| Objective acceptance | Frozen state gives identical selected action; every rank factor is visible; denial/budget respected; loops stop; unresolved state preserved; no planner execution or self-verification. |
| Approval evidence | Full replay ledger, ranking sensitivity results, branch/state conformance, independent decision-trace review and held-out scenario-population results with uncertainty. |
| Dependencies | ARC-06/10/11 consolidated state ownership; approved ordinal policy tiers and budgets. |
| Stop condition | Stop on nondeterministic selection, unbounded loop, authority bypass or unsupported causal promotion. |

### Milestone 5 — Governed domain knowledge and canonical reporting

| Field | Definition |
|---|---|
| Required behaviour | Apply approved effective-dated KPI/SLA/source rules and project accepted findings through ARC-08 canonical reporting to independently validated Word/Excel artifacts. |
| Minimum components | Prior milestones plus knowledge applicability/snapshot, obligation records, full canonical report/composition/layout contracts, renderers, RCV/DEV and publication controller. |
| Synthetic scenarios | At least three structurally different templates; Word/Excel resolution metric preservation; superseded rule; mandatory minority finding; materially changed edit; unsupported Office feature. |
| Expected output | Pinned analytical/report/layout revisions, actual artifacts, evidence→finding→content→placement→artifact→decision lineage and publication state. |
| Negative/adversarial tests | Word omits Excel metric; editor changes “associated” to “caused”; broken formula/chart range; missing qualification; renderer self-verifies; unsupported feature silently degrades. |
| Objective acceptance | Required claims/qualifications survive both formats; actual bytes pass independent RCV/DEV; material edit creates new analytical review; blocking failure prevents verified publication. |
| Approval evidence | Artifact hashes/extraction/visual checks, revision lineage, obligation results and employer-approved classification-label evidence where required. |
| Dependencies | ARC-08 supported component catalogue; business-rule approvals; SEC-08 label mechanism; G3/G4 feasibility. |
| Stop condition | Stop publication on lost meaning/lineage, artifact-validation failure, unapproved rule or missing classification control. |

## 4. Milestone judgment matrix

| Milestone | A. Engineering conformance | B. Analytical correctness | C. Investigative competence | D. Reliability/generalisation | E. Security/operational readiness |
|---|---|---|---|---|---|
| 1 Governed basic | Required: contracts, authority and state transitions | Required for the one bounded calculation, independently recalculated | Not established; only a bounded functional walkthrough | Not established by WP01; varied cases are negative conformance fixtures, not competence population | Only applicable local contract/retention controls; Windows/live deployment Not Tested |
| 2 Statistical | Method/schema conformance | Required across golden calculations, assumptions and errors | Required for material segmentation/anomaly relevance, not just method invocation | Required across held-out statistical scenario families and perturbations | Applicable data handling/runtime controls separately judged |
| 3 Relationship/contradiction | Graph, matching and authority-state conformance | Required for joins, chronology, cardinality and conflict interpretation | Required for useful link pursuit and correct abstention/conflict treatment | Required across unseen schemas, collisions and misleading relationships | Connector/evidence controls independently judged |
| 4 Multi-round | Planner/controller/budget/loop conformance | Required for every intermediate calculation and evidence update | Required for hypothesis quality, disconfirmation, follow-up and stopping | Required across representative hidden investigations and repeat runs | Source authorisation, isolation, retention and failure recovery separately judged |
| 5 Reporting | Canonical/layout/RCV/DEV/publication conformance | Required preservation of exact accepted analytical meaning | Required coverage and materiality remain separately assessed; good layout is not good investigation | Required across multiple report/scenario/template families | Full G3/G4, SEC-08, classification and publication readiness required |

## 5. Investigative reliability and generalisation methodology

### 5.1 Required synthetic test families

| Reliability property | Positive case | Negative case | Adversarial case | Required observable result |
|---|---|---|---|---|
| Confirmation-bias resistance | Initial hypothesis is correct but controller still retrieves a registered falsifier | Evidence merely repeats existing support | Early plausible hypothesis is false; later authoritative evidence supports a competitor | Planner reserves/chooses material disconfirming action; false hypothesis is weakened/rejected, not protected by prior score |
| Disconfirming evidence | Direct counterevidence is available and authorised | Counterevidence source is unavailable | Counterevidence conflicts with a high-authority supporting source due to period mismatch | Retrieve when material; record unavailable gap; align scope/time and preserve genuine conflict |
| Contradiction consistency | Same contradiction represented with record order reversed | Apparent contradiction is different population/period | Authority rule is absent or superseded | Same disposition under reorder; false conflict rejected; real conflict remains unresolved without applicable rule |
| Explanation revision/rejection | New evidence narrows a hypothesis without invalidating it | Decisive falsifier refutes it | Semantically persuasive narrative contradicts verified structured evidence | Create successor revision or reject; preserve history; narrative cannot override evidence |
| Stopping consistency | Sufficiency clauses met and only optional corroboration remains | Material resolvable gap remains | Attractive but low-value repeated action is available after no-progress threshold | Stop consistently in equivalent states; continue only for material gap; never loop for cosmetic confidence |
| Repeated retrieval avoidance | Snapshot/freshness changes under a registered retry rule | Exact semantic request already succeeded | Transient failures invite unlimited retry or parameter-churn duplicates | Permit governed refresh/retry only; deduplicate equivalent request; enforce retry/no-progress limits |
| Appropriate inconclusive termination | Authorised evidence cannot distinguish two hypotheses | Evidence exists but budget is exhausted | Only an untestable assumption or unauthorised source could resolve the question | Terminate partial/inconclusive/budget exhausted with gaps; do not fabricate a winner or causal conclusion |
| Robustness to irrelevant evidence | Relevant records mixed with unrelated noise | Noise shares keywords but no governed relation | Prompt-like narrative instructs selection/promotion | Same material findings/decisions within declared tolerance; irrelevant content cannot change authority or tool execution |
| Record-order invariance | Same set randomly permuted | Duplicate records inserted | Ordering correlates spuriously with outcome | Equivalent outputs/digests where order is non-semantic; duplicates detected; no positional inference |
| Incomplete/malformed evidence | Optional field missing | Required field missing/invalid | Broken reference, collision or forged identifier | Qualify optional loss; fail/clarify required loss; reject invalid reference and preserve incident evidence |
| Previously unseen investigation | Held-out scenario uses known methods in a new combination | Scenario is outside capability catalogue | Surface wording mimics a training fixture while truth differs | General method transfer assessed; honest limitation/clarification; no hard-coded answer |

### 5.2 Population-level assessment

An individual scenario receives its own correctness and decision-trace result. Reliable performance is a separate population claim. Before outcomes are inspected, the evaluation plan must define scenario families, sampling/holdout method, repeats, primary measures, severity, exclusions, thresholds and uncertainty. Repeated runs of one scenario remain nested observations, not independent scenarios. Planning ranges in B01 may inform study design but are not automatic evidence of adequacy.

Report at least: critical-finding recall; material precision; unsupported conclusion rate; invalid-reference rate; correct contradiction disposition; correct revision/rejection rate; appropriate stop/clarification rate; repeated-unproductive-retrieval rate; and authority-violation count. Report raw numerators/denominators and clustered uncertainty by scenario. Thresholds other than existing zero-tolerance safety/verification rules remain **proposed and require prospective approval**.

At the engineering-conformance gate, any executed unauthorised operation, fabricated evidence reference accepted as valid, self-promotion, or illegal finding/report/publication transition is a failure for the affected revision. This is an invariant check, not evidence that the system is otherwise analytically competent.

Robustness tests perturb irrelevant evidence, record order, duplicates, missingness and surface wording while preserving hidden truth. Expected invariants and permitted differences must be set before execution. Passing the September walkthrough or WP01 fixture cannot count toward reliable-demonstration status except as pilot/procedure evidence.

## 6. B03-WP01 scope

**Title:** Shared Investigation Contracts and Synthetic Conformance Fixtures
**Readiness decision:** not ready for implementation authorisation. Review of the narrow Milestone 1 contract proposal may continue while blockers in §6.5 are resolved.

WP01 should define the minimum framework-neutral types below, schema validators, canonical serialization and synthetic positive/negative fixtures. It should not implement analytical algorithms beyond a fixture-only registered calculation adapter, source connectors beyond an in-memory synthetic provider, report renderers, Enhanced reasoning, legacy migration or benchmark execution.

### 3.1 Common contract rules

Every top-level object requires `schema_name`, semantic `schema_version`, stable object ID, `created_at` UTC, producer role/version and parent revision or correlation where applicable. Unknown fields fail for the major version unless an explicit extension container is allowed. Identifiers, collections, strings and encoded size are bounded. References use canonical serialization/digests. Validation checks type, enum, chronology, scope, referential integrity and illegal state transitions. Failures are typed and do not return partially valid authoritative objects.

Versions follow semantic compatibility: additive optional fields may be minor; changed meaning/required fields/state semantics require major; patch describes non-semantic clarification. Stored objects retain their original schema version and migration provenance.

### 3.2 Proposed minimum contracts

| Contract | Purpose and mandatory fields | Validation/failure states | Authority/ownership and provenance | Synthetic conformance tests | G2 relationship |
|---|---|---|---|---|---|
| `EvidenceRef` | Local immutable reference: `evidence_id`, source/snapshot/record locator, evidence type, scope ID, acquired/expires UTC, classification, digest/algorithm, lineage parents, completeness and access state | Invalid digest/time/scope; expired; missing; inaccessible; partial; integrity failure | Evidence repository issues; connector supplies acquisition facts; retention authority can invalidate access | Round trip; digest mismatch; expiry; parent missing; partial ≠ complete; ID cannot extend expiry | Keep separate. G2 `SecurityEvent`/`EvidenceManifest` supply bounded-ID/digest lessons but represent security-test evidence. |
| `InvestigationScope` | Original request digest/text reference, objective, audience, entities, metrics, populations, periods/comparisons, source domains, obligations, knowledge snapshot, unresolved ambiguities, scope revision | Ambiguous/invalid period; unsupported metric; missing authority; clarification required | Controller owns approved scope revision; user/knowledge sources recorded | Exact mapping; material ambiguity blocks; approved default recorded; scope revision immutable | New product type; no G2 equivalent. |
| `RetrievalRequest` | Request/correlation/scope IDs, registered operation/version, source ID, typed parameters, field/population limits, purpose/evidence requirement, worst-case cost, expiry | Unregistered operation/source; scope/field/budget violation; malformed/expired/duplicate | Planner proposes; controller authorises; connector revalidates independently | Allow/deny scope; arbitrary URL/SQL rejected; oversize; replay; expiry; denied request not executed | Do not reuse `WorkerRequest`; adopt its version/bounds/expiry patterns. Product source semantics differ. |
| `RetrievalResult` | Request/controller-decision IDs, source snapshot, status, EvidenceRefs, completeness/coverage, cost charged, cursor, limitations/error/retry classification | success, partial, denied, unavailable, timeout, integrity/internal failure, budget denied | Connector produces facts; evidence repository verifies refs; controller records charge | Partial visible; denial empty; cost atomic; stale cursor; invented ref rejected | New type. G2 `WorkerResponse` is too generic and trusts no product evidence semantics. |
| `InvestigationBudget` | Scope ID, ceilings for rounds, requests, evidence units/bytes, elapsed duration, retries and operator interventions; supplementary compute limits; policy version | Negative/missing ceiling; incompatible units; expired policy | Controller/policy owner issues immutable budget | Boundary equality; dimension exhaustion; no token-to-row fiction | New. No G2 equivalent. |
| `BudgetLedger` | Budget ID, ordered charges/reservations/releases, action/request IDs, remaining dimensions and terminal state | Overcharge, duplicate charge, non-atomic result, unknown action | Controller owns append-only revision; connectors report actual cost | Concurrent/double charge; failure/retry cost; exact exhaustion; replay stable | New; G2 replay cache provides only in-process duplicate protection. |
| `AnalysisOperation` | Invocation/result envelope: operation ID/version, method registration, input EvidenceRefs/result refs, configuration/rule versions, declared assumptions/cost, status, output refs/diagnostics | Unsupported schema/rule; missing/expired input; assumption failed; partial/failed/budget denied | Analysis registry approves executable method; controller schedules; method cannot approve output | Deterministic replay; wrong version; missing assumption; invalid output ref | New. G2 operation string is intentionally insufficient. |
| `Hypothesis` | ID/revision/scope, statement, trigger refs, predictions, mandatory support, decisive falsifiers, confounders, evidence gaps, materiality, state and predecessor | Unsupported trigger; no testable prediction; illegal direct accepted state; revision cycle | Planner or Enhanced may propose; state update by registered analysis; remains non-authoritative | Generate/update/reject/weaken/revise/unresolved; original retained | New. Must not be embedded in G2 request payload as authority. |
| `ProposedFinding` | ID/revision/scope, typed claim, materiality, claim-strength proposal, supporting/refuting refs, calculation/result refs, required qualifications, obligations, proposer identity/version | Invalid/unresolvable ref; missing scope/qualification; self-accepted field prohibited; conflicted sufficiency | Analysis/planner proposes; no acceptance authority | Correct proposal; unsupported/malformed/expired/qualification-loss rejection | New. G2 `TestResult` is a security-test outcome, not business claim. |
| `VerificationDecision` | Decision ID, proposal revision/digest, verifier identity/role/version, support outcome (`supported`, `not_supported`, `unresolved`), checked evidence, assumptions/contradictions, rationale, limitations, timestamp | Same producer/verifier; proposal mismatch; missing checked evidence; silent edit | Independent verifier owns evidence/analytical verification only; final finding disposition follows the unresolved authority matrix | Role separation; counterevidence; stale proposal; supported outcome with invalid ref denied | New. G2 assurance enum is not ARC-11 claim strength. |
| `InvestigationResult` | Scope/revision, terminal state/reason, action/controller decisions, ledger, hypothesis refs, proposal/verification refs, failures, unresolved questions, provenance/config versions | Complete with unmet mandatory obligation; hidden failure; dangling refs; expired mandatory support | Controller assembles; components retain their own authority | complete/partial/inconclusive/blocked/failed/budget exhausted; full graph validation | New. G2 `TestResult` cannot be repurposed. |
| `CanonicalFindingProjection` | Minimal Milestone-1 bridge: analytical revision, finding/proposal ref and disposition, values/units/populations, mandatory qualifications, obligations and source lineage | Unaccepted claim in accepted list; altered value/wording strength; missing qualification/obligation | ARC-08 canonical/report boundary owns projection; accepted inclusion is disabled until finding-disposition authority is approved | Proposed/pending-verification projection; qualification preservation; revision pin; illegal accepted promotion rejected | New and intentionally narrower than full ARC-08 AST/layout contracts. |

`AuthorisationDecision` is also required operationally. WP01 should define a product decision containing request/scope/policy revision, allow/deny, reason, evaluated constraints and controller identity. It may reuse a generic validation helper, but must not import the G2 security-harness class as its product schema without a separate compatibility decision.

### 3.3 First useful investigation fixture

WP01 conformance must include one end-to-end synthetic fixture:

1. scope “Did September SLA attainment deteriorate versus August?”;
2. controller allows exactly one bounded synthetic summary retrieval;
3. evidence repository emits two period `EvidenceRef`s;
4. fixture calculation adapter returns 88.0% and 72.2%, −15.8 percentage points;
5. `ProposedFinding` cites both evidence/result refs and the population/qualification;
6. independent fixture verifier returns `supported` for the correct proposal; and
7. minimal canonical projection represents it as `verification_supported_pending_disposition`, not accepted.

Negative variants alter the denominator, digest, period, scope, qualification, producer/verifier identity and authorisation. Each must fail at the responsible boundary. A denied retrieval must produce no evidence. This is contract conformance and bounded functional-correctness evidence, not implementation of M01/M06, investigative competence, general reliability or deployment readiness.

### 3.4 WP01 acceptance gate

WP01 may be reconsidered for implementation approval only when:

- the accountable architecture owner approves final finding acceptance/rejection/unresolved authority or a bounded experimental transition model that cannot escape WP01;
- the ARC-06/10/11 owner accepts the provisional state/ownership model;
- contract schemas and fixtures are mapped to approved requirements;
- canonical serialization is stable and every reference/digest resolves;
- invalid state transitions, self-verification and authority bypass fail closed;
- SEC classification/expiry survives every derived reference;
- Path A/B/C reasoning adapters could consume/produce the same logical contracts without gaining controller/verifier authority;
- the end-to-end positive and negative fixtures run from a clean revision with recorded evidence; and
- the implementation contains no dependency on Nexus 10.3.43 runtime code or unapproved external service.

### 6.5 Outstanding WP01 blockers and legitimate claim

| Blocker | Current status | Required resolution |
|---|---|---|
| Final finding-disposition authority | Unresolved and implementation-blocking | Approve request/decision ownership for accepted, rejected and unresolved findings |
| ARC-06/10/11 lifecycle/state ownership | Substantive requirements approved; reconciliation incomplete | Approve the WP01 state subset and transition invariants |
| Reproducible repository baseline | PRE01 committed; G2/product source and B01 remain untracked | Classify/exclude sensitive material, create reviewed local source commits under separate authority, verify clean checkout |
| WP01 prospective acceptance plan | Proposed | Approve fixture set, independent reference calculations and five-axis outcome labels before implementation evidence |

If those blockers are resolved, WP01 may demonstrate versioned contract conformance, authority-boundary enforcement, canonical serialization, synthetic evidence lineage and one bounded verification walkthrough. It cannot demonstrate the 20 analytical methods, autonomous follow-up selection, investigative competence, population reliability, reporting fidelity, external/local Enhanced reasoning, Windows isolation or deployment readiness.

## 7. Explicit WP01 exclusions

WP01 does not include the full 20-method catalogue, deterministic follow-up planner, live connectors, SQLite retention implementation, secure Windows IPC, report composition/layout, DOCX/XLSX, RCV/DEV, Enhanced reasoning of any location, external disclosure/privacy infrastructure, benchmark scoring or G2 modification. Those require later milestone decisions and their own evidence.
