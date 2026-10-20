# B03-PRE01-CLOSEOUT — Final Authority and Quality Addendum

**Project:** Nexus Next  
**Date:** 2026-10-20  
**Status:** Corrected specification delivered for architectural review  
**Implementation authority:** None  
**Corrected source-document revision:** `0a6dc5eac7d8a5f594426f5a159913d963433ed4`

## 1. Close-out decision

B03-WP01 is **not ready for implementation authorisation**. Architecture review may continue on the proposed contract shapes, synthetic conformance fixtures and self-promotion prohibitions. Implementation remains blocked by:

1. unresolved final authority for `AcceptedFinding`, `RejectedFinding` and `UnresolvedFinding` dispositions;
2. incomplete reconciliation of the ARC-06, ARC-10 and ARC-11 lifecycle and state ownership needed by WP01;
3. the absence of a reproducible reviewed repository baseline for the wider product source; and
4. the need to approve a prospective WP01 acceptance plan before implementation evidence is observed.

No analytical method, investigation planner, benchmark, external reasoning service, report renderer or G2 Phase 1 component was implemented or executed as part of this close-out.

## 2. Finding-promotion authority

The mandatory ten-transition authority matrix is in [01_ARCHITECTURE_CONTRACT_RECONCILIATION.md](01_ARCHITECTURE_CONTRACT_RECONCILIATION.md#5-mandatory-finding-promotion-authority-matrix). It covers:

1. hypothesis creation;
2. proposed finding submission;
3. independent evidence and analytical verification;
4. finding acceptance;
5. finding rejection;
6. unresolved-finding disposition;
7. canonical-report inclusion;
8. editorial modification;
9. artifact validation; and
10. final publication.

For every transition, the matrix identifies the current state, requested transition, permitted requester, authorised approver, mandatory evidence and validation, failure behaviour, governing requirement and approval dependency.

The matrix establishes these binding boundaries:

- Admission of a hypothesis or proposal does not establish truth or acceptance.
- Evidence verification, analytical finding acceptance, report composition and publication are separate decisions.
- Deterministic engines, local or external LLMs, human operators and reporting components are governed by the same promotion rules.
- No component may promote its own output beyond its explicitly granted authority.
- Accessible decisions do not conclusively allocate final accepted, rejected and unresolved finding disposition between the verifier, controller policy and a designated human authority.
- Those final transitions and dependent canonical inclusion remain blocked until architecture review approves the authority allocation.

## 3. Generalisation and quality principle

> **A successful walkthrough, pilot investigation, worked example or individual synthetic demonstration shall not be presented as evidence of general investigative competence.**

Investigative competence requires independently assessed correctness, reliability, appropriate investigative decisions, generalisation and verification integrity across representative and previously unseen scenarios. Workflow execution and contract conformance are necessary foundations, not sufficient proof.

The milestone method therefore records five independent judgments:

1. engineering conformance;
2. analytical correctness;
3. investigative competence;
4. reliability and generalisation; and
5. security and operational readiness.

Each applicable judgment is reported independently as **Passed**, **Failed**, **Inconclusive** or **Not Tested**. An adverse investigative result does not automatically invalidate an otherwise sound experimental comparison. A prohibited disclosure fails its safety or publication gate, and an unsupported material finding accepted as verified fails its verification or publication gate.

## 4. Investigative reliability requirements

The corrected behavioural methodology in [04_BEHAVIOURAL_MILESTONES_AND_WP01.md](04_BEHAVIOURAL_MILESTONES_AND_WP01.md#5-investigative-reliability-and-generalisation-methodology) defines synthetic positive, negative and adversarial cases for:

- resistance to confirmation bias;
- active pursuit of material disconfirming evidence;
- consistent treatment of contradictory evidence;
- revision or rejection when new evidence changes support;
- consistent stopping decisions;
- prevention of repeated unproductive retrievals;
- appropriate inconclusive termination;
- robustness to irrelevant evidence and record ordering;
- malformed or incomplete evidence; and
- transfer to previously unseen investigations.

An individual scenario receives an individual result. A reliability claim requires a prospectively defined representative scenario population, held-out cases, repeat policy, primary measures, thresholds and uncertainty. Repeated runs of one scenario are nested observations and are not independent scenarios.

## 5. Corrected September calculation

The worked example is an illustrative specification walkthrough. It is not execution evidence or proof of competence. The corrected P2 decomposition in [03_DETERMINISTIC_INVESTIGATION_STRATEGY.md](03_DETERMINISTIC_INVESTIGATION_STRATEGY.md#65-round-3--backlog-age-composition) is:

- August P2 actual: `50/60 = 83.3%`.
- September P2 actual: `55/90 = 61.1%`.
- September cohort rates with August mix: `(5/60 × 5/30) + (55/60 × 50/60) = 77.8%`.
- September mix with August cohort rates: `(30/90 × 2/5) + (60/90 × 48/55) = 71.5%`.
- Symmetric cohort-mix contribution: **−14.2 percentage points**.
- Symmetric within-cohort-rate contribution: **−8.0 percentage points**.
- Total P2 decline: **−22.2 percentage points**.
- Illustrative shares: approximately **64.1% mix** and **35.9% within-cohort rate**.

The corrected conclusion is limited: backlog composition is the larger measured contributor in the displayed aggregate data, while within-cohort deterioration is also material. Correlation does not establish causation. Row-level evidence is required before verification.

## 6. Enhanced Mode position

Enhanced Mode remains location-neutral at its governed reasoning boundary. Under the supplied ARC-09-R01 summary, the leading research candidate is:

`local filtering and authorised disclosure → external LLM reasoning → controlled local restoration → independent Nexus verification → canonical reporting`

A locally hosted LLM remains an alternative. The final production inference architecture has not been selected. No company information transmission, external model activation or implementation is authorised by PRE01.

## 7. WP01 permissible scope and exclusions

If the blocking decisions are resolved, WP01 may demonstrate versioned contract conformance, authority-boundary enforcement, canonical serialisation, synthetic evidence lineage and one bounded verification walkthrough. The walkthrough must end at a verification recommendation unless an approved final disposition authority exists.

WP01 cannot demonstrate the full analytical method catalogue, autonomous follow-up selection, investigative competence, population reliability, report fidelity, Enhanced reasoning, Windows isolation or deployment readiness.

WP01 excludes live connectors, persistent company evidence, DOCX/XLSX publication, RCV/DEV implementation, external disclosure infrastructure, benchmark execution, G2 modification and reuse of Nexus 10.3.43 runtime code.

## 8. Outstanding authority questions

Architecture review must resolve:

1. Who approves final `AcceptedFinding`, `RejectedFinding` and `UnresolvedFinding` dispositions?
2. Does the controller record a verifier or human decision, or apply a separately approved policy decision?
3. What exact ARC-06/10/11 state subset and transition ownership applies to WP01?
4. Which scenario population, independent reference calculations and five-axis thresholds form the prospective WP01 acceptance plan?
5. Which reviewed source revision is the reproducible baseline for any later implementation?

Until these are answered, promotion beyond verification recommendation and implementation-dependent canonical reporting remain blocked.

## 9. Repository and validation record

The corrected source documents were committed on branch `b03-pre01-closeout-review` at revision `0a6dc5eac7d8a5f594426f5a159913d963433ed4`. That revision contains only the eight amended PRE01 files. Unrelated untracked product, G2 and assessment files were excluded.

Close-out validation performed in the Linux cloud environment:

- Git whitespace validation: passed.
- Authority-matrix transition count: 10.
- Investigative method catalogue count: 20.
- Requirements traceability rows: 37.
- Corrected P2 calculations independently reproduced from the displayed aggregates: passed.
- Markdown table consistency check: passed.
- Package SHA-256 manifest validation: passed for the corrected source documents.

Existing product/G2 tests were not rerun because this was a documentation-only assignment. Previously recorded portable test results do not constitute Windows security verification or investigative competence evidence.

## 10. Close-out document set

- [README.md](README.md)
- [01_ARCHITECTURE_CONTRACT_RECONCILIATION.md](01_ARCHITECTURE_CONTRACT_RECONCILIATION.md)
- [02_REASONING_BOUNDARY_AND_METHOD_CATALOGUE.md](02_REASONING_BOUNDARY_AND_METHOD_CATALOGUE.md)
- [03_DETERMINISTIC_INVESTIGATION_STRATEGY.md](03_DETERMINISTIC_INVESTIGATION_STRATEGY.md)
- [04_BEHAVIOURAL_MILESTONES_AND_WP01.md](04_BEHAVIOURAL_MILESTONES_AND_WP01.md)
- [05_GIT_PROVENANCE_AND_READINESS.md](05_GIT_PROVENANCE_AND_READINESS.md)
- [requirements_to_contract_traceability.csv](requirements_to_contract_traceability.csv)
- `SHA256SUMS.txt`

This document closes the specification correction for architectural review. It grants no implementation, benchmark, external-service, company-data, publication or G2 Phase 1 authority.
