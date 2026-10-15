# Behavioural Milestones and B03-WP01 Proposal

## 1. Milestone principles

Each milestone must demonstrate one coherent question-to-decision behavior. Infrastructure that cannot yet support its milestone scenario is recorded as partial implementation, not a completed milestone. Approval requires the exact implementation revision, executed synthetic tests, evidence and limitations. None of these milestones is authorised by PRE01.

## 2. Milestone sequence

### Milestone 1 — Governed basic investigation

| Field | Definition |
|---|---|
| Required behaviour | A typed question/scope leads to controller-authorised synthetic retrieval, one deterministic calculation, an evidence-linked proposed finding, and a separate verification decision. |
| Minimum components | Scope parser for one governed vocabulary; controller; one synthetic connector operation; evidence repository; one analysis operation; proposal and verifier; minimal canonical finding projection. |
| Synthetic scenario | “Did September SLA attainment deteriorate versus August?” with complete, partial, denied and contradictory fixture variants. |
| Expected output | Scoped metric/change, evidence refs, proposal, verification decision, terminal state, budget/provenance and minimal canonical projection. |
| Negative/adversarial tests | Unknown metric; ambiguous period; unauthorised source/field; malformed/expired evidence; wrong denominator; self-verification attempt; altered evidence digest; mandatory qualification omitted. |
| Objective acceptance | Controller denies out-of-scope operations; golden calculation matches; proposal cannot be accepted by proposer; independent verifier rejects wrong population/value/reference; identical frozen run is stable; every output resolves to evidence. |
| Approval evidence | Contract/test versions, source revision, full test outcomes, fixture digests, decision log and independent review of at least one accepted and one rejected proposal. |
| Dependencies | ARC-06/10/11 provisional state authority; SEC retention fields; one approved synthetic metric definition. |
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
| Approval evidence | Full replay ledger, ranking sensitivity results, branch/state conformance and independent decision-trace review. |
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

## 3. B03-WP01 scope

**Title:** Shared Investigation Contracts and Synthetic Conformance Fixtures
**Decision requested later:** authorise a narrow implementation supporting Milestone 1 only.

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
| `VerificationDecision` | Decision ID, proposal revision/digest, verifier identity/role/version, accepted/rejected/unresolved, checked evidence, assumptions/contradictions, rationale, limitations, timestamp | Same producer/verifier; proposal mismatch; missing checked evidence; silent edit | Independent verifier solely owns; decision creates no edited claim | Role separation; counterevidence; stale proposal; acceptance with invalid ref denied | New. G2 assurance enum is not ARC-11 claim strength. |
| `InvestigationResult` | Scope/revision, terminal state/reason, action/controller decisions, ledger, hypothesis refs, proposal/verification refs, failures, unresolved questions, provenance/config versions | Complete with unmet mandatory obligation; hidden failure; dangling refs; expired mandatory support | Controller assembles; components retain their own authority | complete/partial/inconclusive/blocked/failed/budget exhausted; full graph validation | New. G2 `TestResult` cannot be repurposed. |
| `CanonicalFindingProjection` | Minimal Milestone-1 bridge: analytical revision, accepted/unresolved/rejected finding refs as policy requires, values/units/populations, mandatory qualifications, obligations and source lineage | Unverified claim in accepted list; altered value/wording strength; missing qualification/obligation | ARC-08 canonical/report boundary owns projection; presentation has no analytical authority | Accepted-only projection; qualification preservation; revision pin; value immutability | New and intentionally narrower than full ARC-08 AST/layout contracts. |

`AuthorisationDecision` is also required operationally. WP01 should define a product decision containing request/scope/policy revision, allow/deny, reason, evaluated constraints and controller identity. It may reuse a generic validation helper, but must not import the G2 security-harness class as its product schema without a separate compatibility decision.

### 3.3 First useful investigation fixture

WP01 conformance must include one end-to-end synthetic fixture:

1. scope “Did September SLA attainment deteriorate versus August?”;
2. controller allows exactly one bounded synthetic summary retrieval;
3. evidence repository emits two period `EvidenceRef`s;
4. fixture calculation adapter returns 88.0% and 72.2%, −15.8 percentage points;
5. `ProposedFinding` cites both evidence/result refs and the population/qualification;
6. independent fixture verifier accepts the correct proposal;
7. minimal canonical projection includes the accepted finding unchanged.

Negative variants alter the denominator, digest, period, scope, qualification, producer/verifier identity and authorisation. Each must fail at the responsible boundary. A denied retrieval must produce no evidence. This is contract conformance evidence, not implementation of M01/M06 or proof of product analytical performance.

### 3.4 WP01 acceptance gate

WP01 is ready for approval only when:

- the ARC-06/10/11 owner accepts the provisional state/ownership model;
- contract schemas and fixtures are mapped to approved requirements;
- canonical serialization is stable and every reference/digest resolves;
- invalid state transitions, self-verification and authority bypass fail closed;
- SEC classification/expiry survives every derived reference;
- Path A/B/C reasoning adapters could consume/produce the same logical contracts without gaining controller/verifier authority;
- the end-to-end positive and negative fixtures run from a clean revision with recorded evidence; and
- the implementation contains no dependency on Nexus 10.3.43 runtime code or unapproved external service.

## 4. Explicit WP01 exclusions

WP01 does not include the full 20-method catalogue, deterministic follow-up planner, live connectors, SQLite retention implementation, secure Windows IPC, report composition/layout, DOCX/XLSX, RCV/DEV, Enhanced/local model, external paths, privacy filtering, benchmark scoring or G2 modification. Those require later milestone decisions and their own evidence.
