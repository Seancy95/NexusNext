# Frozen Authority and State-Transition Restrictions

## 1. Responsibility allocation used for WP01

| Role | May produce/request | May approve or decide | Explicit limit |
|---|---|---|---|
| Investigation engine | Hypotheses, retrieval proposals and proposed findings | Nothing beyond validity of its own deterministic output envelope | Cannot authorise retrieval, verify its own proposal or assign finding disposition |
| Independent verifier | Verification result for an exact proposed-finding revision | Evidence/analytical support outcome: `supported`, `not_supported`, `unresolved` | Cannot accept, reject or publish a finding |
| Controller | Scope admission; retrieval allow/deny; budget and terminal workflow records; future disposition request | Applies an approved finding-disposition policy only in a later work package | WP01 contains no finding-disposition policy and no final transition API |
| Reporting controller | Future request to include accepted findings | Future canonical inclusion gate | Outside WP01; cannot turn a proposal or verification result into an accepted finding |
| RCV/DEV | Future artifact-validation decisions | Their separate artifact checks | Outside WP01; cannot decide analytical truth or publication |
| Publication authority | Future publication request/decision | Final publication only after all gates | Outside WP01 and cannot override failed analytical, artifact, security or classification gates |

Roles are logical authorities represented in provenance. WP01 does not require separate processes merely to represent them. Process or identity separation is a later security/deployment decision.

## 2. Permitted WP01 transitions

| Current state | Permitted transition | Requester | Decider/validator | Required conditions | Failure behavior |
|---|---|---|---|---|---|
| Raw request | `InvestigationScope(admitted/clarification_required/blocked)` | User-facing boundary | Controller | Valid objective, policy, scope and authority refs | Typed failure or clarification; no implied scope |
| Admitted scope | `RetrievalRequest(proposed)` | Engine or authorised operator | Schema validator only | Within syntax and refers to scope/budget | Invalid proposal rejected; no execution |
| Proposed retrieval | `AuthorisationDecision(allow/deny)` | Controller workflow | Controller | Exact request digest, registered operation/source, scope and budget | Deny on mismatch/uncertainty; no evidence on denial |
| Allowed retrieval | `RetrievalResult(status)` | Registered synthetic provider during WP01 fixtures | Connector/result validator | Exact unexpired allow decision and actual charge | Fail closed; invalid refs never admitted |
| Valid retrieval result | `EvidenceRef(available/partial/...)` | Synthetic evidence repository | Evidence validator/repository | Digest, lineage, scope, expiry and classification valid | Mark invalid/inaccessible; no silent repair |
| Scoped trigger evidence | `Hypothesis(open)` | Engine or authorised operator | Controller admits record | Traceable trigger, predictions, falsifiers, confounders and proposer | Reject record; creates no retrieval authority |
| Hypothesis revision | New immutable hypothesis revision | Engine or authorised operator | Contract validator/controller admission | Predecessor, reason and new evidence; no cycle | Preserve old revision; reject cycle/overwrite |
| Analysis evidence | `ProposedFinding(proposed)` | Engine | Controller admits structurally valid proposal only | Supporting/refuting refs, qualifications, obligations and proposer | Reject malformed/untraceable proposal; never auto-promote |
| Proposed finding | `verification_pending` plus `VerificationRequest` | Controller | Controller | Exact proposal revision/digest and eligible independent verifier policy | Remain proposed if request invalid |
| Verification request | `VerificationResult(supported/not_supported/unresolved)` | Independent verifier | Verification contract validator | Producer/verifier separation and completed required checks | Invalid result rejected; proposal stays pending/proposed |
| Active investigation | `InvestigationOutcome(terminal)` | Controller | Outcome validator | Full references, budget record, failures and unresolved questions | Inconclusive/failed typed outcome; no hidden failure |

## 3. Prohibited transitions

These transitions must be impossible to construct through the WP01 public API and must fail with an auditable authority/state error if attempted:

- hypothesis or proposed finding → `AcceptedFinding`;
- proposed finding → final `RejectedFinding` or `UnresolvedFinding` disposition;
- `VerificationResult(supported)` → accepted finding;
- `VerificationResult(not_supported)` → final rejected finding;
- `VerificationResult(unresolved)` → final unresolved-finding disposition;
- engine proposal → self-verification;
- verifier result → verifier-approved promotion;
- controller structural admission → analytical acceptance;
- proposed/pending/verified finding → canonical report inclusion;
- any WP01 object → artifact validation or publication;
- finding/report state change through version transformation, unknown field, extension data or canonical-serialization ambiguity;
- scope widening, budget bypass, evidence expiry extension or classification downgrade through revision or derivation.

WP01 schemas must not expose accepted, rejected, unresolved-disposition, canonical-inclusion, artifact-validation or publication commands. Representing a future state name in documentation does not enable its transition.

## 4. Unapproved authority dependencies

Architecture review still must approve:

1. the final finding-disposition policy and the accountable approver for acceptance, rejection and unresolved disposition;
2. the precise ARC-06/10/11 state ownership and whether controller action records or applies another authority's decision;
3. identity and independence evidence required to qualify an independent verifier in deployment;
4. reporting-controller inclusion rules and exact accepted-finding contract in a later work package;
5. RCV/DEV and publication authority bindings; and
6. employer classification, destination, retention and label controls.

None of these dependencies blocks defining a proposal and verification-support record. All block the associated promotion or publication transition.
