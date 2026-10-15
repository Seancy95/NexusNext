# B03-PRE01 — Architecture Reconciliation and Implementation Readiness

**Version:** 0.1
**Date:** 2026-10-15
**Status:** Design and inspection output for architectural review
**Implementation authority:** None
**Governing principle:** ARC-LEGACY-01

## Answer to the primary question

Baseline Mode moves from a question to verifiable findings through a deterministic, revisioned investigation graph. It parses the question into a governed scope, creates explicitly unverified hypotheses from approved knowledge and measurable deviations, derives evidence requirements, proposes typed retrieval operations, and lets the controller independently authorise and execute those operations. Deterministic analytical methods update the hypothesis graph. An inspectable lexicographic decision policy selects the next eligible action according to mandatory integrity needs, materiality, discriminatory value, evidence authority, coverage, assumption risk and cost. The planner stops on sufficient proposals, a material need for clarification, exhausted opportunity/budget, or explicit insufficiency. Only an independent verifier can accept a proposed finding. Canonical reporting consumes the resulting decisions without changing them.

This is an investigation process, not a report selector. A predefined report is not required.

## Deliverables

1. [Architecture Contract Reconciliation](01_ARCHITECTURE_CONTRACT_RECONCILIATION.md)
2. [Reasoning Boundary and Investigative Method Catalogue](02_REASONING_BOUNDARY_AND_METHOD_CATALOGUE.md)
3. [Deterministic Investigation Strategy and Worked Example](03_DETERMINISTIC_INVESTIGATION_STRATEGY.md)
4. [Behavioural Milestones and B03-WP01 Proposal](04_BEHAVIOURAL_MILESTONES_AND_WP01.md)
5. [Git Provenance and Repository Readiness](05_GIT_PROVENANCE_AND_READINESS.md)
6. [Requirements-to-contract traceability](requirements_to_contract_traceability.csv)
7. `SHA256SUMS.txt` — local integrity manifest for this package

## Claim labels used throughout

| Label | Meaning |
|---|---|
| Approved requirement | Supported by the current PRE01 assignment or accessible approved v1.2 decision register/B01 material |
| Proposed design | Defined here for later architecture approval |
| Implemented | Code is present in the inspected working tree; no commit provenance is implied for untracked files |
| Test-executed | A named test was actually run in a stated environment |
| Independently verified | An independent acceptance gate has supported the stated behaviour |
| Unresolved dependency | Required decision, authority or evidence is unavailable |

No PRE01 contract, planner, analytical method, external reasoning component or benchmark scenario was implemented or executed. The only execution during PRE01 was inspection plus the existing portable G2 unit suite, which passed 47/47 on Linux. That result does not demonstrate Windows enforcement, product investigation behaviour, reporting, or CLOUD-EVAL.

## Source basis

- `Nexus Next Master Architecture, Governing Principles and Decision Register v1.2`, 2026-10-13, SHA-256 `d610355ee5ca7f64c875bcf874c6fa77c976f621fd6acdbb4c5be090afa2e246`.
- B03-PRE01 assignment, SHA-256 `e48817a312798ee0cfa80f0c23d586c18d505589b8cd946b7fd019494c9652ae`.
- `docs/CLOUD-EVAL-B01_Adaptive_Investigation_Benchmark_Specification.md`, untracked working-tree file, SHA-256 `ebc69b607dde0bf006decdc7c0bbf8312f91fee25eea6ef32841b7bb08be8727`.
- Tracked B02 and B03 packages at repository `HEAD` `b08d24fd9376f0537c370c0ed7af0f320b8669c5`.
- Untracked G2 source and tests identified in the provenance report. Their current portable suite passed 47 tests on Python 3.12.14/Linux during this inspection.
- Nexus 10.3.43 is used only through the B02/B03 recorded assessment and domain catalogue; no legacy engine was modified or reused.

## Review boundary

Approval of this package would approve a design direction only. It would not approve implementation, production source access, external LLM access, G2 changes, real company evidence, benchmark execution, publication, or a Git commit/push.
