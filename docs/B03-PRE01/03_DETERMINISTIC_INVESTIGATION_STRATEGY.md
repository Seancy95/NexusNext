# Deterministic Investigation Strategy and Worked Synthetic Investigation

## 1. Lifecycle

The proposed lifecycle is:

`Question → Scope → Hypotheses → Evidence requirements → Retrieval proposal → Controller decision → Retrieval → Analysis → Contradictions → Sufficiency → Follow-up or proposed finding → Independent verification`

Each transition creates an immutable revision linked to its predecessor. New branches do not rewrite prior evidence or findings. The planner operates only on frozen typed state and a registered method/source catalogue. It does not depend on a predefined report.

## 2. Question interpretation and scope

### 2.1 Deterministic interpretation

Baseline applies these steps in order:

1. Preserve the original question unchanged.
2. Tokenise and normalise only through versioned, locale-aware rules.
3. Match metric, entity, product/source, time, population, comparison and requested-outcome phrases against the approved knowledge snapshot and capability catalogue.
4. Resolve applicability by product, source instance, contract, population, effective period and version.
5. Emit an `InvestigationScope` with every matched term, rule and unresolved field.
6. Apply a default only if an approved scoped default exists and record it. Otherwise ask one necessary clarification or mark the limitation.

Ambiguity is material when different plausible values would change an authorised source, population, metric definition, contractual interpretation, security classification, comparison or expected output. Baseline does not silently select among material alternatives. Enhanced may propose a semantic mapping, but the same validation rule applies.

### 2.2 Initial hypotheses

After the controller approves scope, Baseline runs registered trigger rules. Examples include:

- aggregate change → measurement/data-quality change, population mix change, within-segment change and exceptional-event candidates;
- SLA deterioration → priority mix, queue/backlog age, pause/calendar/configuration, team/workflow, incident/change and timestamp-quality candidates;
- source disagreement → scope/time mismatch, staleness, identity/join error and genuine contradiction candidates;
- anomaly → baseline drift, exposure change, one-off outlier and persistent process-change candidates.

Each hypothesis records trigger evidence, observable predictions, mandatory support, decisive falsifiers, plausible confounders, applicable domain rule and `unverified` status. Templates that do not meet their trigger predicates are not instantiated.

## 3. Evidence requirements and action generation

For each live hypothesis, Baseline derives:

- supporting and contradicting observations;
- comparison population and period;
- calculations and assumptions;
- relationship paths and source authority needed;
- quality/completeness prerequisites; and
- observations that would discriminate it from competing hypotheses.

Candidate actions come only from registered operations whose output schema can satisfy one of those requirements. Generic candidates include profile, retrieve, calculate, segment, compare distribution, traverse relationship, check rule/version, inspect contradiction and request clarification. A candidate includes expected outcome categories and a deterministic prediction matrix showing how each category would update each hypothesis.

## 4. Deterministic follow-up selection

### 4.1 Eligibility gates

An action is eligible only if all gates pass:

1. it addresses an open mandatory obligation, evidence gap, contradiction, or at least two materially distinct live hypotheses;
2. its source, scope, fields and operation are registered and within current authorisation;
3. the controller can independently validate it as read-only and within SEC/retention policy;
4. its worst-case declared cost fits the remaining budget;
5. required predecessor evidence exists and is unexpired;
6. its possible outcomes can change a hypothesis/sufficiency/clarification state or satisfy a mandatory output obligation; and
7. the same semantic request has not already completed against the same source snapshot, unless a declared retry/freshness predicate changed.

Failure of a gate is recorded, not hidden. The planner proposes the highest-ranked eligible action; the controller may deny it and return a reason. Denial does not authorise the planner to widen scope.

### 4.2 Inspectable ranking without arbitrary weights

Eligible actions are ordered lexicographically. A later factor never compensates for a worse earlier factor:

1. **Obligation class:** integrity/security prerequisite; explicit mandatory user/contract requirement; material explanatory gap; optional corroboration.
2. **Materiality tier:** critical, high, medium, low, as set by the applicable approved policy/scenario—not invented by the planner.
3. **Discriminatory value:** decisive falsifier; separates two or more live material explanations; closes mandatory support/contradiction gap; corroborates an already adequate claim.
4. **Relevance/directness:** direct measurement of the claimed mechanism; close proxy; contextual proxy.
5. **Evidence authority:** current authoritative evidence; current approved derived evidence; approved fallback; contextual/unverified source.
6. **Population coverage:** complete target population; approved representative population; material partial population; unknown coverage.
7. **Assumption risk:** no new material assumption; approved mapping; testable proxy assumption; untestable assumption.
8. **Declared resource cost:** lower maximum retrieval/record/time cost wins only after equal analytical value.
9. **Stable tie-break:** registered operation ID, source ID and canonical request digest in ascending byte order.

“Discriminatory value” is derived from the prediction matrix, not intuition. An action separates explanations when at least one possible typed outcome produces different predetermined updates for two live hypotheses. If hypotheses make identical predictions, the action cannot rank as discriminating them.

Policy owners approve the ordinal tiers and scenario materiality rules. No hidden combined score is permitted. Sensitivity testing replays scenarios after moving each non-mandatory tier one position; material outcome changes require review before controlled use.

### 4.3 Result interpretation and hypothesis update

The method registry evaluates evidence against each hypothesis predicate:

- **Supported:** all mandatory support predicates satisfied at required coverage/authority, no decisive falsifier, and material contradictions resolved or qualified.
- **Weakened:** relevant counterevidence reduces the permitted claim strength, but no decisive falsifier is established.
- **Rejected:** a registered decisive falsifier is established with sufficient authoritative evidence, or a required condition is shown false.
- **Revised:** new evidence requires a materially different prediction/scope; create a successor hypothesis and retain the original decision trail.
- **Unresolved:** neither support nor rejection clauses are satisfied, including because evidence is inaccessible, partial, expired or conflicting.

These are hypothesis states, not accepted findings. The planner may create a `ProposedFinding` only after the applicable sufficiency policy passes. The independent verifier issues a verification decision; final accepted/rejected/unresolved finding-disposition authority remains blocked pending the decision in document 01 §5.1.

### 4.4 Loop prevention and stopping

The ledger keys each action by semantic purpose, operation/version, source/snapshot, scope and canonical parameters. A completed or definitively denied key is not repeated. A retry requires a registered transient failure, remaining retry allowance and changed attempt metadata. A branch has a maximum depth and no-progress count. “No progress” means no change to evidence coverage, hypothesis state, contradiction state, obligation state or sufficiency gaps.

Investigation stops with a typed reason when:

- every mandatory objective has a verification-ready proposal or an explicit unresolved decision and no eligible material action remains;
- a material scope/permission choice requires user clarification;
- remaining actions are only optional corroboration that cannot change claim/qualification state;
- all useful actions are denied, unavailable or would rely on an untestable assumption;
- a budget, time, round or retry ceiling is reached;
- evidence expiry invalidates required support; or
- an integrity/security failure invalidates the run.

Budget exhaustion or no eligible action yields partial/inconclusive output, never a fabricated conclusion.

## 5. Causality and sufficiency

A cause claim requires all mandatory clauses in an approved causal policy: temporal precedence; credible mechanism; exposure alignment; relevant alternative explanations/confounders assessed; no material contradiction; and either an approved causal design, intervention/counterfactual evidence, or other explicitly approved basis. Without these, wording is limited to concentration, association, consistency or candidate contribution.

Sufficiency is a decision table by claim type. A material explanatory finding minimally requires a scoped change, reliable supporting evidence, relevant comparison, tested competing explanation, contradiction disposition, explicit unknowns and resolvable evidence references. Mandatory clauses cannot be outweighed by a score.

## 6. Worked synthetic investigation

### 6.1 Scenario and evidence

This is an **illustrative design walkthrough**, not an executed Nexus Next investigation and not evidence of successful deterministic investigation or general competence. “Selected,” “retrieved,” and “result” below describe the specified state transitions that a future implementation would need to reproduce. All names, records and values are synthetic. Scenario policy `SYN-SD-2026-09 v1` defines “resolution performance” as both median elapsed business hours and resolution-SLA attainment for tickets resolved in the named month. It authorises comparison to the immediately preceding complete month for the same service population. Without that approved scoped definition, Baseline would request clarification.

Only the displayed aggregate counts support independent arithmetic recalculation. No row-level synthetic ticket fixture was supplied with PRE01. Consequently, the stated medians, ticket-to-incident links, chronology, team overlaps and planned-capacity evidence are scenario assertions that cannot be independently established from this document alone. A future test must provide frozen row-level fixtures and reference calculations before any corresponding finding can be independently verified.

| EvidenceRef | Synthetic evidence |
|---|---|
| E-SCOPE-01 | Approved scenario scope, materiality and comparison rules |
| E-TKT-AUG-01 | Frozen August ticket facts: 200 resolved tickets |
| E-TKT-SEP-01 | Frozen September ticket facts: 180 resolved tickets |
| E-SLA-01 | Effective priority targets, working calendar and event definitions |
| E-CONFIG-01 | Metric/rule/configuration revision history for August–September |
| E-REL-01 | Ticket-to-incident and ticket-to-team relationships |
| E-INC-77 | Synthetic assignment-queue incident record, 10–12 September |
| E-STAFF-01 | Partial planned-capacity schedule; no actual attendance/work-allocation evidence |

The controller permits bounded aggregate retrieval from the synthetic ticket, configuration, relationship, incident and staffing sources. No arbitrary SQL or network request is available.

### 6.2 Round 0 — scope and integrity prerequisite

**Interpretation:** entity = synthetic Service Desk tickets; periods = September 2026 versus August 2026; outcomes = median business-hours resolution and SLA attainment; population = resolved tickets; purpose = explanation, not only metric generation.

Initial hypotheses are H1 priority-mix change, H2 within-priority workflow deterioration, H3 older-backlog closure mix, H4 exceptional incident, H5 team capacity, H6 SLA/configuration change, and H7 timestamp/completeness defect. All are `unverified`.

Generated actions include source profiling/configuration check, aggregate calculation, priority segmentation and incident retrieval. Profiling ranks first because it is an integrity prerequisite; later evidence cannot repair an invalid population or rule silently.

**Selected A00:** M08 profile E-TKT-AUG-01/E-TKT-SEP-01 and M11 check E-SLA-01/E-CONFIG-01. Ranking: integrity prerequisite > explanatory actions. Result: populations reconcile to 200 and 180 unique resolved tickets; required timestamps/priority/SLA flags are present; no rule/calendar/configuration revision occurred. H6 and H7 are rejected for this scoped change. This does not prove all data is correct; it removes the registered defects as supported explanations.

### 6.3 Round 1 — establish deterioration

**Selected A01:** M06/M01 calculate the scoped baseline because it is the mandatory objective and all integrity prerequisites now pass.

| Period | Resolved | Median business hours | SLA met | SLA attainment |
|---|---:|---:|---:|---:|
| August | 200 | 9.0 | 176 | 88.0% |
| September | 180 | 14.5 | 130 | 72.2% |

Output O-BASE-01 establishes a 5.5-hour median increase and 15.8 percentage-point SLA decline. It supports the “deteriorated” premise but does not explain it.

Next eligible actions are priority segmentation, resolution-duration distribution, incident traversal and team segmentation. Priority segmentation ranks first: it covers the full authoritative population, directly separates aggregate mix from within-segment change, and has lower cost than relationship retrieval.

### 6.4 Round 2 — priority segmentation and competing explanations

**Selected A02:** M07 segment by governed priority.

| Priority | Aug count | Aug SLA met | Sep count | Sep SLA met | Rate change |
|---|---:|---:|---:|---:|---:|
| P1 | 20 | 18 (90.0%) | 18 | 16 (88.9%) | −1.1 pp |
| P2 | 60 | 50 (83.3%) | 90 | 55 (61.1%) | −22.2 pp |
| P3 | 120 | 108 (90.0%) | 72 | 59 (81.9%) | −8.1 pp |

Using September’s priority mix with August’s priority-specific rates gives 156 expected SLA-met tickets, or 86.7%. Therefore the priority mix accounts for 1.3 points of the 15.8-point aggregate decline under this fixed-order decomposition; within-priority changes account for the remaining 14.4 points. P2 contributes 20 of the 26 fewer successes versus that counterfactual (76.9%).

H1 is **supported as a small contributor** and rejected as the primary explanation. H2 is supported as a lead concentrated in P2, with a smaller P3 change. The action does not establish why P2 changed.

The highest-ranked next actions are P2 age/distribution analysis, incident traversal and team segmentation. P2 age analysis wins because it directly separates slower treatment of new work from changed closure composition, uses complete current authoritative timestamps, and requires no cross-source join.

### 6.5 Round 3 — backlog-age composition

**Selected A03:** M02/M07 compare P2 tickets created before the report month (“carried”) with tickets created during the month (“new”).

| P2 cohort | Aug count | Aug SLA met | Sep count | Sep SLA met |
|---|---:|---:|---:|---:|
| Carried | 5 | 2 (40.0%) | 30 | 5 (16.7%) |
| New in month | 55 | 48 (87.3%) | 60 | 50 (83.3%) |

Carried P2 tickets rose from 8.3% to 33.3% of P2 closures and account for 25 of September’s 35 P2 breaches. The previously reported 80.0% counterfactual was arithmetically wrong. Applying September’s cohort-specific rates to August’s P2 mix is:

`(5/60 × 5/30) + (55/60 × 50/60) = 0.7778`, or **77.8%**.

Because a two-factor mix/rate decomposition depends on ordering, the corrected design uses the symmetric average of both orders:

- August P2 actual: 50/60 = **83.3%**.
- September mix with August cohort rates: `(30/90 × 2/5) + (60/90 × 48/55)` = **71.5%**.
- August mix with September cohort rates: **77.8%** as above.
- September P2 actual: 55/90 = **61.1%**.
- Symmetric cohort-mix contribution: average of `(71.5 − 83.3)` and `(61.1 − 77.8)` = **−14.2 percentage points**.
- Symmetric within-cohort rate contribution: average of `(77.8 − 83.3)` and `(61.1 − 71.5)` = **−8.0 percentage points**.

The two contributions sum to the **−22.2-point** P2 decline. On this illustrative aggregate data, cohort mix accounts for approximately 64.1% and within-cohort rate changes 35.9% of the decline. The conclusion that cohort mix is the larger measured contributor still holds, but the within-cohort contribution is substantial and must not be minimised.

H3 becomes **supported within the illustrative decision trace** as an explanation of reported resolved-ticket performance. It does not mean operational service became worse by the same amount; clearing old work can be a positive operational action. The substantial within-cohort contribution also requires follow-up. Both qualifications are mandatory, and row-level evidence is required before verification.

Incident traversal now ranks above team segmentation: it has a registered explicit relationship and can distinguish an exceptional event from general queue effects. Team segmentation remains eligible.

### 6.6 Round 4 — incident evidence and contradiction

**Selected A04:** M09/M10 traverse E-REL-01 to E-INC-77 and compare linked/unlinked P2 outcomes.

- 20 September P2 tickets are linked to the 10–12 September assignment-queue incident; 15 breached SLA.
- 70 are unlinked; 20 breached.
- Nine of the fifteen linked breached tickets were already carried backlog before the incident.
- Twenty unlinked breaches remain, including tickets entered after the incident ended.

H4 is **supported as an associated contributor for a subset**, but weakened as a primary or sole cause. Temporal overlap and link evidence do not eliminate backlog age, workload allocation or other confounders. The registered causal policy forbids “the incident caused September deterioration.”

Team segmentation now ranks first because it uses complete governed ownership data and distinguishes broad service deterioration from a concentrated operational cohort. Staffing retrieval is a weaker proxy and ranks afterward.

### 6.7 Round 5 — team concentration and incomplete capacity evidence

**Selected A05:** M07 segment P2 by owning team.

| P2 team | Aug SLA met | Sep SLA met | September context |
|---|---:|---:|---|
| Blue | 27/30 (90.0%) | 25/50 (50.0%) | 28/30 carried tickets and 18/20 incident-linked tickets |
| Green | 23/30 (76.7%) | 30/40 (75.0%) | Little change |

The concentration supports a Team Blue cohort finding but creates confounding: team, carried backlog and incident linkage overlap. The planner cannot attribute the change to team capacity.

**Selected A06:** retrieve the authorised aggregated planned-capacity schedule E-STAFF-01 because it is the remaining action that could distinguish capacity from composition and incident explanations. It reports 20% fewer planned Team Blue hours in September, but lacks actual attendance, case allocation and within-day queue evidence. H5 is **weakened but unresolved**: the result is a proxy consistent with capacity pressure, not proof.

No authorised registered operation can obtain the missing actual attendance/allocation evidence. Repeating ticket or schedule retrieval would use the same snapshots and is blocked by the loop ledger. Optional narrative parsing cannot change the evidence state. The planner terminates `partial` with explicit unresolved causal questions rather than spend the last budget on corroboration.

### 6.8 Decision trace

| Round | Selected action | Earlier ranking reasons | Hypothesis effect |
|---|---|---|---|
| 0 | A00 profile/config check | Integrity prerequisite outranks all explanation work | Rejects registered data/config explanations H6/H7 |
| 1 | A01 baseline calculation | Mandatory objective; prerequisite complete | Establishes deterioration only |
| 2 | A02 priority segmentation | Full population; directly separates mix vs within-priority; low cost | H1 small contributor; H2 concentrated P2 lead |
| 3 | A03 P2 age/cohort distribution | Directly distinguishes closure mix vs new-work slowing without cross-source assumptions | H3 supported; narrows H2 |
| 4 | A04 incident traversal | Explicit relation can separate exceptional event; authoritative current records | H4 subset association; sole-cause version weakened |
| 5 | A05 team segmentation | Full source, direct concentration test, lower assumption than staffing proxy | Team Blue concentration established; confounding exposed |
| 6 | A06 planned capacity | Only remaining eligible discriminator for H5; partial proxy disclosed | H5 unresolved; investigation stops |

### 6.9 Sufficiency and proposed findings

| Outcome | State | Evidence and permitted conclusion |
|---|---|---|
| September deterioration | Illustrative proposal only | Displayed aggregates recalculate SLA 88.0%→72.2%; median 9.0→14.5h requires row-level fixture verification |
| Priority mix | Illustrative qualified proposal | Displayed aggregates support only a small 1.3-point contribution under the stated fixed-order counterfactual; it is not the main explanation |
| Older P2 backlog closure mix | Illustrative qualified proposal | Corrected symmetric decomposition gives −14.2 points mix and −8.0 points within-cohort rate; row-level evidence and method review are still required |
| Team Blue concentration | Illustrative proposal only | Displayed aggregate assertion suggests concentration, but underlying ticket relationships were not supplied for independent verification |
| Assignment-queue incident | Illustrative association candidate only | Link/timing assertions would support association if verified; contradictions prevent primary-cause wording |
| Reduced planned capacity | Unresolved | E-STAFF-01 is incomplete proxy evidence; actual capacity/allocation unavailable |
| SLA/config or registered timestamp defect | Rejected explanations | No relevant change/defect in the scoped authoritative snapshots; rejection is limited to registered checks |

The illustrative candidate answer is: **September’s reported resolution deterioration appears concentrated in P2 and Team Blue. On the displayed P2 aggregates, a larger share of older backlog tickets is the larger of two measured contributors, while within-cohort performance also deteriorated materially. Priority mix explains little of the overall decline. A queue incident is associated with some breached tickets, but neither it nor reduced planned capacity is established as the root cause.**

This remains a set of illustrative proposed findings. An independent verifier would need the row-level fixture to reproduce populations, medians, relationships and chronology; independently recalculate every metric; test the symmetric decomposition and qualifications; resolve every reference; and inspect contradictory evidence. Final acceptance would additionally require the unresolved promotion authority decision. The walkthrough itself demonstrates neither execution nor generalisation.

### 6.10 Proposed canonical representation

The canonical result records scope revision, method/rule versions, terminal state `partial`, each hypothesis revision, all action/controller decisions, evidence refs, calculations, proposed findings, rejected explanations, unresolved questions, mandatory qualifications and verification decisions. Editorial text may simplify wording but cannot replace “associated” with “caused,” omit the backlog-clearance qualification, or hide the unresolved capacity question.

## 7. CLOUD-EVAL experimental comparability

Paths A, B, C and optional D use the same logical `InvestigationScope`, authorised source catalogue, typed retrieval operations, `EvidenceRef`, `InvestigationBudget`/ledger, finding states, independent verifier, canonical reporting, publication controls and evaluator role separation. The controller applies the same source, scope, field, round, retry and evidence-unit/byte ceilings regardless of reasoning strategy. A reasoning path proposes an action; only the shared controller authorises it and only the shared connector executes it.

| Aspect | Common control | Unavoidable difference and interpretation limit |
|---|---|---|
| Evidence | Same frozen synthetic scenario graph, initial evidence IDs and semantic retrieval opportunities | Path C receives privacy-transformed representations; transformation loss/reconstruction risk must be measured and can explain performance differences |
| Retrieval | Same registered operations, permissions, source snapshots, result schemas and maximum opportunities | Natural-language tool proposal may need deterministic translation; translation rejection/failure is recorded as path behavior, not repaired by operator |
| Scope | Same objective, populations, periods, obligations and clarification policy | Enhanced paths may propose semantic scope candidates; they cannot receive extra hidden scope or evaluator hints |
| Budget | Same hard rounds, authorised calls, evidence units/bytes, retries and wall-clock envelope where feasible | Deterministic CPU/records and model tokens/inference are not equivalent units; report each separately and do not claim compute parity |
| Verification | Same local evidence resolution, sufficiency policies, independent verifier and unsupported-acceptance gate | Model prose may require more claim parsing; the parser/version and invalid-output rate are recorded |
| Reporting | Same canonical accepted findings, obligations and projection components | Narrative richness can differ but cannot affect scoring of evidence access or verification; verbosity is not analytical success |
| Publication/security | Same classification, retention and publication gates | B/C external research requires a separate bounded gateway; this design does not activate it. D requires recorded local model/runtime/hardware configuration |

The primary experimental factor is reasoning strategy: A uses the deterministic process in this document; B/C use the same external model configuration as specified by B01 with original/transformed synthetic representation; D uses its preregistered local configuration if included. ARC-09-R01 makes the filtered external route the leading Enhanced research candidate while retaining a local LLM alternative; final production inference architecture remains unselected. Investigators/operators do not receive hidden truth or evaluation feedback.

Before each comparison, an exposure-parity audit records evidence available, requested, returned and actually presented, plus suppressed/transformed fields and failed calls. A path cannot be credited with semantic improvement when it saw additional evidence, had more retrieval opportunities, used weaker verification, or received a different reporting foundation. When exact equality is impossible, the preregistered analysis states the confound, narrows the conclusion and may mark experimental validity Inconclusive rather than attributing the difference to reasoning.

> **Generalisation warning:** No successful walkthrough, pilot or single synthetic run—including this one—may be cited as evidence of general investigative competence. That requires representative held-out scenario evaluation of correctness, decision quality, reliability, generalisation and verification integrity under preregistered acceptance rules.
