# B03-PRE01 — Architecture Reconciliation and Implementation Readiness

**Version:** 0.2 — close-out correction
**Date:** 2026-10-20
**Status:** Corrected design and inspection output for architectural review
**Implementation authority:** None
**Governing principle:** ARC-LEGACY-01

## Answer to the primary question

The specified Baseline design moves from a question toward independently verifiable findings through a deterministic, revisioned investigation graph. It parses the question into a governed scope, creates explicitly unverified hypotheses from approved knowledge and measurable deviations, derives evidence requirements, proposes typed retrieval operations, and lets the controller independently authorise operations. Deterministic analytical methods update the hypothesis graph. An inspectable lexicographic policy selects the next eligible action according to mandatory integrity needs, materiality, discriminatory value, evidence authority, coverage, assumption risk and cost. The planner stops on sufficient proposals, a material need for clarification, exhausted opportunity/budget, or explicit insufficiency. Finding acceptance remains subject to the unresolved promotion authority described in document 01. Canonical reporting may consume only duly accepted findings without changing them.

This specifies an investigation process rather than a report selector; a predefined report is not required. It does not establish that Nexus Next can yet execute the process.

> **Generalisation warning:** A successful walkthrough, pilot investigation, worked example or individual synthetic demonstration shall not be presented as evidence of general investigative competence. Investigative competence requires independently assessed correctness, reliability, appropriate investigative decisions, generalisation and verification integrity across representative and previously unseen scenarios. Workflow execution and contract conformance are necessary foundations, not sufficient proof.

## Deliverables

1. [B03-PRE01 Close-out — Final Authority and Quality Addendum](B03-PRE01-CLOSEOUT.md)
2. [Architecture Contract Reconciliation](01_ARCHITECTURE_CONTRACT_RECONCILIATION.md)
3. [Reasoning Boundary and Investigative Method Catalogue](02_REASONING_BOUNDARY_AND_METHOD_CATALOGUE.md)
4. [Deterministic Investigation Strategy and Worked Example](03_DETERMINISTIC_INVESTIGATION_STRATEGY.md)
5. [Behavioural Milestones and B03-WP01 Proposal](04_BEHAVIOURAL_MILESTONES_AND_WP01.md)
6. [Git Provenance and Repository Readiness](05_GIT_PROVENANCE_AND_READINESS.md)
7. [Requirements-to-contract traceability](requirements_to_contract_traceability.csv)
8. `SHA256SUMS.txt` — local integrity manifest for this package

## Claim labels used throughout

| Label | Meaning |
|---|---|
| Approved requirement | Supported by the current PRE01 assignment or accessible approved v1.2 decision register/B01 material |
| Proposed design | Defined here for later architecture approval |
| Conceptually feasible | The investigation can be described or theoretically performed; no executable capability is implied |
| Specified | A concrete process, algorithm, contract or acceptance method has been designed |
| Implemented | Code is present in the inspected working tree; no commit provenance is implied for untracked files |
| Test-executed | A named test was actually run in a stated environment |
| Independently verified | An independent acceptance gate has supported the stated behaviour |
| Reliably demonstrated | Independent evaluation across sufficiently varied, representative and previously unseen scenarios supports the defined competence claim with preregistered thresholds and uncertainty |
| Unresolved dependency | Required decision, authority or evidence is unavailable |

Conceptual feasibility, specification, implementation, test execution, independent verification and reliable demonstration are separate classifications. No PRE01 contract, planner, analytical method, external reasoning component or benchmark scenario was implemented or executed. The existing portable G2 unit suite passed 47/47 on Linux during PRE01, but that result does not demonstrate Windows enforcement, product investigation behaviour, reporting, CLOUD-EVAL or general investigative competence.

## Source basis

- `Nexus Next Master Architecture, Governing Principles and Decision Register v1.2`, 2026-10-13, SHA-256 `d610355ee5ca7f64c875bcf874c6fa77c976f621fd6acdbb4c5be090afa2e246`.
- B03-PRE01 assignment, SHA-256 `e48817a312798ee0cfa80f0c23d586c18d505589b8cd946b7fd019494c9652ae`.
- B03-PRE01 close-out assignment and authority/quality addendum, supplied 2026-10-20; SHA-256 recorded in document 05.
- `docs/CLOUD-EVAL-B01_Adaptive_Investigation_Benchmark_Specification.md`, untracked working-tree file, SHA-256 `ebc69b607dde0bf006decdc7c0bbf8312f91fee25eea6ef32841b7bb08be8727`.
- Tracked B02, B03 and PRE01 v0.1 packages at repository revision `669a7bf7072e529c04e20154587767be1090f2f8`; corrected close-out source documents were subsequently committed at `0a6dc5eac7d8a5f594426f5a159913d963433ed4` after the user explicitly requested a downloadable Git delivery.
- Untracked G2 source and tests identified in the provenance report. Their portable suite passed 47 tests on Python 3.12.14/Linux during initial PRE01 inspection on 2026-10-15; it was not rerun for this documentation-only close-out.
- Nexus 10.3.43 is used only through the B02/B03 recorded assessment and domain catalogue; no legacy engine was modified or reused.

## Review boundary

Enhanced Mode is location-neutral at the reasoning boundary: it extends the governed architecture through semantic interpretation, contextual reasoning and adaptive proposals. ARC-09-R01 identifies local filtering and authorised disclosure controls followed by external reasoning, controlled local restoration and independent Nexus verification as the leading research candidate; a local LLM remains an alternative. No final production inference architecture has been selected, and no company-data transmission or external service activation is authorised.

## Close-out decision

B03-WP01 is **not ready for implementation authorisation**. Its contract shapes and conformance fixtures can be reviewed provisionally, but implementation is blocked until the finding-promotion authority decision is approved, the ARC-06/10/11 lifecycle is reconciled sufficiently for WP01 transitions, and a reproducible source-control baseline is established. WP01 can ultimately demonstrate engineering conformance and a bounded functional walkthrough; it cannot demonstrate investigative competence or general reliability.

## Close-out change log

- `README.md`: capability classifications, generalisation warning, Enhanced positioning and WP01 decision.
- `01_ARCHITECTURE_CONTRACT_RECONCILIATION.md`: mandatory promotion authority matrix and blocked transitions.
- `02_REASONING_BOUNDARY_AND_METHOD_CATALOGUE.md`: location-neutral Enhanced architecture and competence limits.
- `03_DETERMINISTIC_INVESTIGATION_STRATEGY.md`: corrected P2 calculations, decomposition and illustrative status.
- `04_BEHAVIOURAL_MILESTONES_AND_WP01.md`: five-axis acceptance model and reliability/adversarial scenario methodology.
- `05_GIT_PROVENANCE_AND_READINESS.md`: current branch/HEAD/tracking state and remediation steps.
- `requirements_to_contract_traceability.csv`: close-out authority, generalisation, reliability and ARC-09-R01 mappings.

Approval of this package would approve corrected design direction only. It would not approve implementation, production source access, external LLM access, G2 changes, real company evidence, benchmark execution, publication, or a Git commit/push.
