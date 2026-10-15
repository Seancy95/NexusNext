# Architecture Contract Reconciliation

## 1. Reconciliation result

The B03 capability and Path A designs are directionally compatible with the accessible architecture, subject to four corrections and boundaries:

1. The B03 `InvestigationResult` must sit inside the approved ARC-03 seven-stage lifecycle and ARC-06 progressive investigation graph. It cannot collapse planning, investigation, clarification, preview, editing and export into one operation.
2. ARC-10 assigns orchestration, authorisation, budgets, branch dependencies, sufficiency and claim-promotion workflow to the controller. A deterministic planner proposes actions and findings; it does not execute connectors, grant scope or accept its own claims.
3. ARC-08 is approved in the v1.2 addendum. The minimal WP01 projection must preserve the evidence-to-finding boundary and a pinned analytical revision, while the full composition/layout/RCV/DEV contract remains a later milestone.
4. The proposed B03 shared contracts need explicit SEC retention/classification metadata, controller authorisation decisions and revision boundaries. Stable evidence references cannot be interpreted as permission to retain raw evidence after SEC-06 expiry.

No conflict requires reopening the approved architecture. The unresolved ARC-06/10/11 cross-family consolidation affects exact state-transition ownership and names, so WP01 may define provisional schemas but must block implementation of final promotion semantics until that focused decision is approved.

## 2. Logical component responsibilities

These are logical boundaries; ARC-02 does not require one operating-system process per component.

| Logical component | Proposed responsibility | Must not do | Governing authority |
|---|---|---|---|
| Investigation controller | Own scope and investigation revisions, authorise typed operations, schedule dependencies, enforce budgets/retention/stopping, record decisions, submit proposals for verification | Perform unrestricted source queries; delegate authorisation to planner/model; accept its own findings | ARC-10; ARC-02; SEC-NET |
| Source connector | Discover authorised metadata and execute a small registered read-only operation after independent policy validation | Accept arbitrary SQL/URL/payload; become a controller proxy; infer analytical truth | ARC-03 D03; SEC-04/05; SEC-NET |
| Evidence repository | Store typed evidence snapshots/references, lineage, classification, acquisition/expiry and integrity metadata; enforce access/expiry | Turn presence into truth; retain raw evidence beyond policy; treat hashes as tamper-proof | SEC-06/06.1/09; ARC-01.1 |
| Deterministic analysis | Execute registered versioned calculations and methods against authorised evidence and approved knowledge | Select source authority silently; approve knowledge/findings; manufacture missing facts | ANA-00; SIC-01; ARC-01 |
| Investigation planner | Generate hypotheses/evidence gaps/actions and rank eligible follow-ups through the deterministic policy | Execute tools; widen scope; hide failure; use an unexplained score | ARC-06.5; ARC-10; PRE01 §8 |
| Independent verifier | Evaluate claim support, scope, assumptions, contradiction, qualification and evidence sufficiency; issue immutable decision | Merely check citation existence; silently edit claim; share implementation identity with proposing logic | ARC-01.2; ARC-11; SIC-01.4 |
| Report composition | Map accepted/qualified analytical content and obligations to a revisioned composition plan | Recalculate metrics; promote hypotheses; remove material caveats | ARC-08.1–08.3 |
| Artifact validation/publication | Independently inspect actual DOCX/XLSX, RCV/DEV results, classification, revision/hash and publication blockers | Trust renderer self-attestation; override blocking controls | ARC-08.4–08.5; SEC-08 |

## 3. Requirements-to-contract reconciliation

The detailed machine-readable matrix is in `requirements_to_contract_traceability.csv`.

| Requirement | Mandatory behaviour | Proposed contract/component | Authority boundary | Verification requirement | Current status | Unresolved dependency |
|---|---|---|---|---|---|---|
| GOV-02/04/05 | Separate invariant from technology and approval from implementation/evidence/organisation | All versioned contracts; status metadata | Architecture approves meaning; evidence supports only tested revision | Contract review plus named execution evidence | Requirement approved; PRE01 design proposed | None |
| ANA-00 | Rigorous calculations plus substantive investigation, competing explanations and uncertainty | Scope, planner, method registry, hypothesis graph, verifier | Deterministic output is not automatically accepted truth | Adversarial synthetic Golden Suites for correct-but-shallow and fluent-but-unsupported cases | Requirement approved; product capability not implemented | Exact controlled-suite thresholds |
| SIC-01–01.5 | Evidence/knowledge/metrics/claim decisions remain controlled; Enhanced is advisory | Typed evidence, knowledge snapshot, hypothesis/proposal/decision records | Neither planner nor local model may approve knowledge, source actions or findings | Negative authority tests and independent claim verification | Requirement approved; proposed integration | Exact historical SIC subwording unavailable |
| SEC-01/02/NET | Local data, default-deny egress, typed connector operations | Controller authorisation; connector operation catalogue | Connector independently validates destination/operation/scope/credential/payload | G2 and connector misuse tests on intended Windows environment | Architecture approved; only portable G2 policy behavior implemented/tested | OS enforcement and packaged tests not demonstrated |
| SEC-04/05 | Isolated approved credentials and bounded read-only SQL | Connector policy/credential reference; RetrievalRequest | Planner never receives credential or arbitrary query capability | Corporate mechanism plus live authorised negative tests | Not implemented for product | Employer credential mechanism and live permission |
| SEC-06/06.1/09 | Raw evidence expires within 24h; continuity conditional; logs minimised/15 days | EvidenceRef acquisition/expiry/classification; repository purge | Evidence ID does not extend retention; logs omit source bodies | Closed-app/crash/restart expiry tests | Product behavior not implemented | Employer approval for continuity; G5 cleanup feasibility |
| ARC-01/01.1 | Modular Python application, explicit contracts, immutable analytical revisions | Logical components and revisioned objects | Framework remains replaceable | Contract compatibility and revision immutability tests | Direction approved; PRE01 design proposed | Final framework choices open |
| ARC-01.2/ARC-11 | Independent substantive verification and visible conflicts | ProposedFinding, VerificationDecision, ClaimDecisionRecord mapping | Proposer cannot verify itself | Support/refutation/qualification/invalid-reference/adversarial tests | Requirement approved; not implemented | ARC-06/10/11 promotion-state reconciliation |
| ARC-03 | Seven-stage UX, autonomous authorised discovery, necessary clarification only | InvestigationScope, plan/action records, progress, pinned result revision | Planner proposes; controller authorises; user decides genuine ambiguity | End-to-end synthetic UX lifecycle tests | Logical flow approved; not implemented | Interface technology open |
| ARC-06 | Progressive branches, sufficiency closure, evidence time classes, knowledge applicability | Investigation graph, Hypothesis revisions, sufficiency record | Approved knowledge resolver governs applicability | Branch/revision/resumption/expiry tests | Substantive requirements approved | Formal cross-ARC consolidation pending |
| ARC-08 | Canonical findings, independent Word/Excel layout, preservation, RCV/DEV | Minimal CanonicalFindingProjection in WP01; full AST/layout later | Composition/editor have presentation authority only | Actual-file extraction and RCV/DEV at G3/G4 | Architecture approved; not demonstrated | Office labels and final supported feature catalogue |
| ARC-10 | Controller owns graph, scheduling, budgets, stopping, sufficiency and promotion workflow | Controller plus planner proposal interface and BudgetLedger | Planner/model cannot independently execute | Authorisation-denial, replay, budget, loop and state-machine tests | Product controller not implemented; G2 controller is narrower | Exact product controller contract |
| ARC-02 | Typed roles, revisioned state, explicit privilege boundaries; stack open | Logical components; G2 relationship table in WP01 | Security boundary must be enforced where permissions differ | G1–G5; actual packaged Windows evidence | Direction approved; G2 portable subset implemented/tested | IPC, process isolation, backend/UI/package choices |
| ARC-09 | Baseline independent; Enhanced strictly local/offline and advisory | Common reasoning interface and boundary matrix | Enhanced cannot execute tools/recalculate authoritative metrics/approve claims | Local model provenance, isolation and added-value tests | Architecture approved; not implemented | Model/runtime/hardware approval |
| CLOUD-EVAL B01 | A/B/C share evidence, opportunity, verification/reporting; reasoning strategy differs | Shared contracts/controller/verifier/report projection | Experimental path never changes authority | Exposure/budget parity audit and separate gates | Specification exists; benchmark not implemented/run | External paths separately authorised only for synthetic research |
| ARC-LEGACY-01 | Legacy is reference, never automatic authority/foundation | Governed domain packages; no runtime dependency | Business owner approval required for imported rule | Provenance, effective-date and independent calculation tests | Applied in B03/PRE01 design | Current owner approval for candidate rules |

## 4. State and authority reconciliation

The following states must remain orthogonal:

- **Evidence state:** available, partial, expired, inaccessible, contradicted, invalid.
- **Knowledge state:** proposed, approved, superseded, ambiguous, blocked; plus scope/effective period.
- **Hypothesis state:** open, supported, weakened, rejected, revised, unresolved.
- **Finding state:** proposed, accepted, rejected, unresolved.
- **Investigation state:** active, awaiting clarification, partial, inconclusive, blocked, failed, budget exhausted, complete.
- **Report state:** draft, review required, verified for a specific revision/artifact, publication blocked, published where authorised.

No numeric confidence score may bridge these states. A supported hypothesis remains unaccepted until an independent verification decision. Report composition cannot change that decision.

## 5. Missing decisions and controlled provisional design

| Missing or incomplete authority | Why it matters | Dependent design | Safe provisional work | Blocked until confirmation |
|---|---|---|---|---|
| ARC-06/10/11 complete cross-family lifecycle and exact promotion semantics | Prevents conflicting ownership of sufficiency, closure and promotion | Hypothesis/finding/investigation state machines | Define records and illegal self-approval invariant | Freeze final transition names/ownership and implement promotion workflow |
| ARC-09-R01 text is not present in accessible ADR/B01/B03 materials | PRE01 names it as related external-reasoning priority | Enhanced research prioritisation and claims | Preserve B01 synthetic-only paths and ARC-09 local production boundary | Attribute requirements or priority to ARC-09-R01 |
| Exact historical ANA subdecisions and SIC wording | Avoid invented approvals/IDs | Method authority and semantic boundary citations | Cite ANA-00/SIC family and v1.2 substantive reconstruction | Claim verbatim or fine-grained historic approval |
| ARC-02 final stack/IPC/packaging choices | Affects process/API realization, not logical contracts | Controller/worker deployment, storage, UI | Keep schemas/framework-neutral; reuse Python only where approved direction supports it | Lock technology or treat G2 development pipe as secure IPC |
| Product connector operation catalogue and source-specific authority owners | Determines safe retrieval and authoritative concepts | RetrievalRequest, discovery and method inputs | Define typed generic operation descriptors and synthetic fixtures | Connect to Jira/Ivanti/SQL or approve live source precedence |
| SEC-04 employer credential mechanism | Required for any live connector | Credential reference field and connector boundary | Opaque credential-reference schema only | Credential retrieval or live authentication |
| SEC-06.1 organisational approval | Controls recurring historical state | Comparison/history evidence | Synthetic/current-run comparisons and typed conditional state | Persistent cross-report company evidence |
| SEC-08 Office label mechanism and supported document features | Required for verified publication | Full canonical report/layout/artifact stages | Minimal finding projection for WP01 | Claim verified DOCX/XLSX publication |
| Numerical materiality, sufficiency and CLOUD-EVAL thresholds | Determines gates and comparative claims | Method registry, planner tiers, acceptance | Named ordinal policy categories and synthetic scenario-specific thresholds | Controlled benchmark or universal pass claims |
| Approved local model/runtime and hardware | Needed for Enhanced implementation | Semantic adapter and benchmark Path D | Define advisory typed boundary only | Build/activate Enhanced inference |

## 6. Architecture alignment finding

PRE01 may proceed to an implementation decision for a narrow WP01 contract package after the ARC-06/10/11 lifecycle owner approves the provisional state model or explicitly authorises it as an experimental namespace. Analytical methods, live connectors, report exporters and semantic adapters remain outside WP01. Existing G2 contracts provide useful validation and provenance patterns but are a standalone security harness and are not product investigation contracts.
