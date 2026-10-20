# Contract Maturity Register and Minimum WP01 Specification

## 1. Status rules

Statuses are independent. Documentation does not imply implementation; implementation does not imply a passing test; a passing test does not imply independent verification. Because the accessible architecture defines boundaries but no approved executable WP01 schema, every contract below is **Proposed**, **Not Implemented**, **Not Tested** and **Not Verified**.

## 2. Contract maturity and evidence register

| Contract/version | Design | Implementation | Test | Independent verification | Governing requirement and authority boundary | Source/test evidence |
|---|---|---|---|---|---|---|
| `InvestigationScope/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-03, ARC-06, SIC-01; controller owns admitted scope revision | PRE01 04 §6.2; no WP01 source/test exists |
| `InvestigationBudget/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-06, ARC-10; policy/controller issues limits | PRE01 04 §6.2; no WP01 source/test exists |
| `BudgetUsage/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-10; controller records append-only usage, producer reports actual charge | PRE01 `BudgetLedger` proposal; no WP01 source/test exists |
| `RetrievalRequest/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-04, ARC-10, SEC-05; requester proposes, controller authorises | PRE01 04 §6.2 and B03 Path A; G2 request is pattern evidence only |
| `AuthorisationDecision/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-10; controller alone issues allow/deny for exact request revision | PRE01 04 §6.2; G2 class is semantically different and untracked |
| `RetrievalResult/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-04, SEC-05/06; connector reports result, evidence repository validates refs | PRE01 04 §6.2; no WP01 source/test exists |
| `EvidenceRef/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-01.2, SEC-01/06, SIC-01.4; repository issues local immutable reference | PRE01 01 §§3–4 and 04 §6.2; G2 evidence utility is not product evidence |
| `Hypothesis/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-06, ARC-10, SIC-01; engine/human proposes, controller admits only | PRE01 01 §5 and 04 §6.2; no WP01 source/test exists |
| `ProposedFinding/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-10, ARC-11, SIC-01.4; engine proposes and cannot promote | PRE01 authority matrix; no WP01 source/test exists |
| `VerificationRequest/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-01.2, ARC-11; controller requests independent review of exact proposal | Derived minimum request envelope from accepted responsibility allocation; exact schema unapproved |
| `VerificationResult/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-01.2, ARC-11, SIC-01.4; independent verifier records support only | PRE01 `VerificationDecision`; renamed to avoid implying final disposition |
| `InvestigationOutcome/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-06, ARC-10; controller assembles terminal record without accepting findings | PRE01 `InvestigationResult`; no WP01 source/test exists |
| `ContractFailure/1.0.0` | Proposed | Not Implemented | Not Tested | Not Verified | ARC-01, SEC fail-closed principles; boundary detecting failure emits typed non-authoritative record | Consolidates required safe failure behavior; exact schema unapproved |

`CanonicalFindingProjection` is intentionally excluded from WP01 implementation readiness. Final finding disposition is not approved and reporting is outside scope. The PRE01 proposal remains design input for a later work package.

## 3. Common envelope, canonical form and validation

Every top-level object embeds these mandatory fields rather than inheriting a runtime base class:

| Field | Rule |
|---|---|
| `schema_name` | Exact registered name; case-sensitive |
| `schema_version` | `MAJOR.MINOR.PATCH`, ASCII digits without leading zeroes except zero |
| `object_id` | Stable, bounded opaque identifier; unique within type/authority namespace |
| `revision` | Positive integer; immutable revisions use predecessor reference rather than overwrite |
| `created_at` | UTC RFC 3339 timestamp with `Z`; chronology must be valid |
| `producer` | Logical role, component name/version and instance/run identifier; no credential or personal secret |
| `correlation_id` | Bounded investigation correlation identifier |
| `parent_refs` | Typed IDs plus exact revision and digest where lineage applies |
| `classification` | Approved classification label or `synthetic`; derived records cannot silently downgrade it |

Canonical serialization is proposed as RFC 8785 JSON Canonicalization Scheme over UTF-8 JSON, followed by SHA-256. Contracts must avoid binary floating-point for governed measures: transmit decimal values as canonical decimal strings with explicit unit and scale. Sets are encoded as arrays sorted by their registered semantic key; ordered event lists retain order. Timestamps normalize to UTC `Z`. Duplicate JSON keys, NaN/infinity, invalid Unicode and non-canonical numeric forms are rejected. This algorithm remains Proposed until architecture approval.

Validation order is fixed: decode and size bounds; schema/version; fields/types/enums; identifier and chronology; scope/authority; referential integrity/digests; lineage cycles; state restrictions; canonical reserialization. Failure at any stage returns one `ContractFailure` with a stable code and path, records the attempted object digest when safely available, and yields no partially authoritative object.

## 4. Minimum fields by contract

### `InvestigationScope/1.0.0`

Mandatory: request digest or local text reference; objective; audience; entities; metrics; populations; primary/comparison periods; permitted source domains and operation classes; obligations; knowledge snapshot; unresolved ambiguities; scope status (`admitted`, `clarification_required`, `blocked`); controller identity and policy revision. Empty material scope dimensions are rejected. A revision cannot widen sources, fields, periods or audience without fresh controller admission.

### `InvestigationBudget/1.0.0` and `BudgetUsage/1.0.0`

Budget mandatory: scope ID/revision; maximum rounds, retrievals, evidence bytes/units, elapsed time, retries and operator interventions; optional compute dimensions; effective/expiry times; issuer and policy version. Usage mandatory: budget ID/revision; ordered entries with action/request ID, reservation/charge/release, dimension, amount, timestamp and resulting balance. Negative limits, unit substitution, overcharge, duplicate action charge and unknown release fail closed.

### `RetrievalRequest/1.0.0`

Mandatory: exact scope and budget references; registered operation name/version; source ID; typed parameters; field, population and row/byte limits; evidence requirement; purpose; worst-case charge; expiry; requester role/version; idempotency key. URLs, free-form SQL and executable expressions are prohibited. A valid request is only a proposal until an exact `AuthorisationDecision` allows it.

### `AuthorisationDecision/1.0.0`

Mandatory: request ID/revision/digest; scope, budget and policy revisions; decision (`allow`, `deny`); evaluated constraints; stable reason code; controller identity; timestamp; validity window. An allow decision binds only the exact request digest. Mutation, expiry, budget change or scope revision requires a new decision.

### `RetrievalResult/1.0.0`

Mandatory: request and allow-decision references; source snapshot; status (`success`, `partial`, `denied`, `unavailable`, `timeout`, `integrity_failure`, `internal_failure`, `budget_denied`); evidence references; completeness/coverage; actual charge; limitations; retry classification. Denied requests return no evidence. `success` requires at least one valid evidence reference unless the registered operation explicitly permits an authoritative empty result.

### `EvidenceRef/1.0.0`

Mandatory: evidence ID; source/snapshot/record locator; evidence type; scope ID/revision; acquired and expiry UTC; classification; digest and algorithm; lineage parents; completeness; access state (`available`, `partial`, `expired`, `inaccessible`, `contradicted`, `invalid`); issuing repository identity. The reference contains no source body. An ID or derived record cannot extend expiry. Missing parent, digest mismatch, scope mismatch or classification downgrade is invalid.

### `Hypothesis/1.0.0`

Mandatory: hypothesis ID/revision; scope reference; statement; trigger evidence/approved-knowledge refs; testable predictions; supporting requirements; decisive falsifiers; confounders; evidence gaps; materiality class; state (`open`, `supported`, `weakened`, `rejected`, `revised`, `unresolved`); proposer; predecessor where revised. State is descriptive provenance, not finding disposition. `accepted` is not a valid value.

### `ProposedFinding/1.0.0`

Mandatory: finding ID/revision; scope; typed claim; materiality; proposed claim strength; supporting and refuting evidence refs; calculation/result refs if applicable; required qualifications; obligations; proposer; created time. Its only WP01 lifecycle values are `proposed` and `verification_pending`. Fields named or semantically equivalent to `accepted`, `published` or final disposition are prohibited.

### `VerificationRequest/1.0.0`

Mandatory: exact proposed-finding ID/revision/digest; required checks; evidence set and expected digests; assumptions and known contradictions; verifier eligibility policy/version; requester; deadline. The controller may request verification but cannot nominate the proposal producer as verifier.

### `VerificationResult/1.0.0`

Mandatory: request and exact proposal references; verifier role/component/version; independence assertions; outcome (`supported`, `not_supported`, `unresolved`); checked evidence and calculations; contradiction/assumption results; rationale; limitations; timestamp. These outcomes assess support only. They do not accept, reject or publish a finding.

### `InvestigationOutcome/1.0.0`

Mandatory: scope/revision; terminal status (`complete`, `partial`, `inconclusive`, `blocked`, `failed`, `budget_exhausted`, `clarification_required`); stable terminal reason; retrieval/decision/evidence/hypothesis/proposal/verification/failure references; budget ledger; unresolved questions; configuration versions and controller identity. `complete` means the bounded workflow completed, not that any finding was accepted.

### `ContractFailure/1.0.0`

Mandatory: failure ID; boundary/component; related correlation/object/digest when safe; stable category and code; non-sensitive field path; retryability; timestamp; policy/version; public-safe message. It must not echo secret values, evidence bodies or malformed payloads. Failure creation cannot convert an invalid input into a valid domain object.

## 5. Compatibility policy

- Components support a finite, configured set of schema versions; input cannot negotiate arbitrary versions.
- Same-version objects are accepted only after full validation.
- An older minor version may be processed by a newer component only through a registered, one-way transformation with tests proving preserved meaning, authority, classification, expiry and evidence references.
- A newer object received by an older component is rejected by default. Downgrade requires a separately registered lossless transformation; dropping an unknown field is not lossless proof.
- Unsupported major versions, malformed versions, changed required-field meanings and incompatible enum values are rejected.
- Unknown top-level fields are rejected. Extensions are permitted only in a registered `extensions` namespace whose size, owner and semantics are known; extensions cannot alter authority, state, evidence or classification.
- Original bytes/digest, original version, transformation ID/version and transformed bytes/digest are retained in audit lineage.
- Version handling never bypasses normal scope, authority, evidence or transition validation.

The prospective compatibility cases and expected results are frozen in `synthetic_conformance_matrix.csv`.
