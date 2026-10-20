# Objective Acceptance Criteria and Readiness Recommendation

## 1. WP01 implementation acceptance criteria

An eventual WP01 implementation may be accepted only if all criteria below are evaluated against one immutable source revision from a clean checkout. These criteria establish foundational contract behavior only.

| ID | Objective criterion | Required evidence | Failure condition |
|---|---|---|---|
| AC-01 | Every contract in the approved WP01 set has an approved versioned schema and implementation mapping | Contract register, source locations and schema digest | Missing/extra contract or undocumented field semantics |
| AC-02 | Every positive fixture serializes to the approved canonical bytes and round-trips without semantic change | Golden bytes/digests and independent comparison | Byte/digest mismatch or semantic drift |
| AC-03 | Every mandatory-field, type, enum, bound, chronology and malformed-input case returns its frozen typed failure | Full matrix results with zero unexpected pass | Invalid input creates a valid/partial authoritative object |
| AC-04 | Scope, source, field, operation, budget and expiry restrictions fail closed | Denial tests and dispatch spy showing zero execution | Out-of-scope/expired/denied operation executes or emits evidence |
| AC-05 | Every evidence and parent reference resolves to exact type, revision, scope and digest; cycles and expiry extension are rejected | Lineage graph tests and golden invalid graphs | Dangling, mismatched, cyclic or extended-expiry lineage accepted |
| AC-06 | Engine, verifier and controller authorities remain separate in every state path | Authority tests for every permitted/prohibited transition | Self-verification or unauthorised promotion constructible |
| AC-07 | No final finding disposition, canonical inclusion, artifact validation or publication transition exists in the WP01 API | Public API/schema inspection plus negative fixtures | Any excluded transition is callable or representable as valid command |
| AC-08 | Same-version and registered compatibility paths preserve meaning, authority, classification, expiry and evidence refs | Golden original/transformed bytes, transformation ID and semantic assertions | Silent field loss, changed authority or unrecorded transformation |
| AC-09 | Unsupported/malformed versions and negotiation-bypass attempts are rejected and audited | Compatibility test results for every `VER-*` case | Fallback, silent assumption or validator bypass |
| AC-10 | Failures are bounded, typed and non-sensitive and do not echo evidence bodies or credentials | Failure snapshots and sensitive sentinel tests | Secret/body echo, crash, unbounded output or partial authority |
| AC-11 | Synthetic fixture set and expected results were approved before the implementation test run | Signed/reviewed matrix revision predating results | Test oracle altered after outcomes without a new review revision |
| AC-12 | Clean checkout reproduces the same package build and complete conformance result in the declared environment | Commit, tool/runtime versions, commands and artifact hashes | Dependency on untracked/local file or non-reproducible outcome |
| AC-13 | Source contains no Nexus 10.3.43 runtime dependency and no import from `nexus_g2` product schemas | Dependency/import scan and reviewer inspection | Legacy or G2 schema used as implementation foundation |
| AC-14 | Only synthetic fixtures are used and no live connector, model, report renderer or external service is reachable | Fixture manifest, network/connector absence review | Company data, live source or external inference used |
| AC-15 | Contract and test classifications are reported independently | Final maturity register with actual evidence per status | Passing test represented as independent verification or competence |

All applicable AC-01 through AC-15 must pass. `Inconclusive` or `Not Tested` on an applicable criterion is not implementation acceptance. Any unauthorised transition, executed denied operation, fabricated evidence reference accepted as valid, prohibited disclosure or unsupported final promotion is a hard failure.

## 2. Permitted claims after a successful WP01 implementation

A passing package may state only that the approved foundational contracts:

- validate and canonically serialize the tested schemas;
- preserve tested lineage, classification, expiry and scope invariants;
- reject the tested malformed, incompatible and unauthorised cases;
- separate proposal, verification-support and controller-authorisation roles in the tested contract layer; and
- reproduce the recorded synthetic conformance results from the exact revision and environment.

It may not claim analytical correctness, investigative competence, reliable hypothesis generation, deterministic follow-up quality, generalisation, Enhanced Mode effectiveness, Word/Excel correctness, Windows security isolation, production readiness or any accepted finding.

## 3. Outstanding approvals

| Decision | Owner needed | Current status | Effect |
|---|---|---|---|
| Exact Git baseline and staged file list | Repository/information owner | Proposed | No baseline commit or clean-checkout proof until approved |
| Updated `.gitignore` | Repository/security owner | Proposed | Generated/sensitive output exclusions not frozen |
| Product package/build layout | Architecture/repository owner | Proposed | Implementation paths and packaging metadata not frozen |
| Contract names, fields and v1 compatibility policy | Architecture owner | Proposed | All contracts remain design-only |
| Canonical JSON and digest profile | Architecture/security owner | Proposed | Golden serialization cannot be authoritative |
| ARC-06/10/11 WP01 state subset | Architecture owner | Proposed | State validators cannot be approved |
| Independent verifier eligibility metadata | Architecture/security owner | Proposed | Logical separation testable; deployment identity is not |
| Synthetic matrix and golden fixtures | Test/architecture owner | Proposed | Prospective oracle not approved |
| Final finding disposition | Accountable architecture/business authority | Explicitly outside WP01 and unresolved | Acceptance/rejection/unresolved transitions remain disabled |
| G2 untracked material classification/provenance | G2 owner and information owner | Requires review | Must remain separate from WP01 baseline |

## 4. Readiness recommendation

**Recommendation: Conditionally Ready for WP01 implementation approval, but Not Yet Authorised.**

The bounded contract set, authority denials, compatibility rules, prospective test oracle and exact baseline contents are now specific enough for architectural and repository review. Implementation can begin only after the first eight applicable approvals above are recorded and a clean Git baseline is authorised. Final finding-disposition authority may remain unresolved because WP01 deliberately omits those transitions.

PRE01 acceptance establishes design authority only. It does not demonstrate the investigation strategy or analytical competence. This readiness package contains no product implementation and no executed WP01 tests.
