# CLOUD-EVAL-B03 — Requirements-Led Baseline Architecture and Path A Design

**Version:** 0.1
**Date:** 2026-10-15
**Status:** Design for architectural review; implementation and benchmark execution are not authorised
**Governing principle:** ARC-LEGACY-01

## Purpose and authority

This package designs a new deterministic Baseline Mode for Nexus Next and the Path A contract for CLOUD-EVAL. The current B03 assignment and the approved B01 benchmark specification are normative for this design. Nexus 10.3.43 is an evidence source for candidate domain knowledge, observed behaviour and historical lessons only. Its module boundaries, engines and coupling are not an implementation foundation.

The package deliberately distinguishes four levels of claim:

| Label | Meaning |
|---|---|
| Approved requirement | Stated by the B03 assignment or accessible B01 specification |
| Design proposal | Proposed here and awaiting architectural approval |
| Observed legacy behaviour | Located in Nexus 10.3.43 source or tests; not proof of a current requirement |
| Verified implementation | Supported by recorded execution evidence at an identified revision |

No Baseline implementation, legacy migration, external model access, benchmark run, G2 change or G2 Phase 1 work is included.

## Deliverables

1. [Baseline Capability Catalogue](01_BASELINE_CAPABILITY_CATALOGUE.md)
2. [Domain Knowledge Catalogue](02_DOMAIN_KNOWLEDGE_CATALOGUE.md)
3. [Legacy Behaviour and Defect Register](03_LEGACY_BEHAVIOUR_AND_DEFECT_REGISTER.csv)
4. [CLOUD-EVAL Path A Contract](04_PATH_A_CONTRACT.md)
5. [Requirements Traceability](requirements_traceability.csv)

The capability catalogue owns the reusable analysis vocabulary. The domain catalogue owns candidate business knowledge. The defect register records legacy observations without turning them into requirements. The Path A contract owns benchmark-facing interfaces and comparison rules. The traceability matrix points to these documents rather than repeating their content.

## Architectural decisions proposed for review

- Build Baseline Mode as a new Nexus Next component against versioned evidence, retrieval, budget, analysis, finding, verification and reporting contracts.
- Express domain rules as versioned, reviewable data or isolated rule packages behind the general operation interface. A domain rule cannot acquire authority from code location or legacy presence.
- Keep hypotheses, proposed findings, verification decisions and editorial projections as distinct records.
- Give Paths A, B and C the same scenario evidence identifiers, permissions, retrieval service, investigation-state model, verification service and canonical report projection. Their reasoning strategies differ.
- Measure equal access through evidence exposure and budgets. Record irreducible runtime differences instead of pretending that deterministic record processing and model token inference consume identical resources.

These are proposals until the architecture owner approves them.

## Risks, dependencies and decisions still required

| ID | Item | Impact or required decision |
|---|---|---|
| B03-R01 | Accessible materials do not include the full approved ARC, SEC, analytical, evidence, verification and reporting decision set. | Confirm contract names, mandatory fields and authority owners before implementation. Do not infer approval from legacy code. |
| B03-R02 | Several legacy constants describe live business rules but their current business-owner approval and effective dates are unavailable. | Ratify, replace or retire each `Requires confirmation` domain item before use. |
| B03-R03 | Evidence-unit and compute costs differ across deterministic and model paths. | Approve a multidimensional budget and the comparison claims it supports. |
| B03-R04 | Anomaly and statistical methods can produce many leads and implicit multiple comparisons. | Approve method registry, thresholds, correction policy and qualification text before controlled runs. |
| B03-R05 | Entity resolution can create false joins that contaminate later reasoning. | Approve match tiers, minimum evidence, abstention and human-verification requirements. |
| B03-R06 | Canonical report fields may tempt renderers to promote unverified claims. | Enforce type and state checks at projection boundaries. |
| B03-D01 | Definition of one comparable evidence unit across tables, documents and graph edges. | Architecture and evaluation owners must decide before budget schema freeze. |
| B03-D02 | Which analyses are mandatory for every scenario category versus available on demand. | Evaluation owner must preregister per-category operation expectations. |
| B03-D03 | Whether a domain-rule package may contain executable code or only declarative expressions. | Security and architecture owners must decide after threat and maintainability review. |
| B03-D04 | Numerical acceptance thresholds for performance and operational budgets. | Must be preregistered under B01 before outcome observation. |
| B03-D05 | Current source authorities, SLA/KPI owners and effective dates. | Business owners must confirm before live or representative use. |

Required dependencies are an approved canonical evidence schema, local authorised retrieval service, immutable evidence ledger, domain-rule governance process, verification interface, scenario package schema, deterministic clock/calendar inputs, and synthetic fixtures with protected ground truth.

## Recommended stages

1. **Contract foundation:** approve and implement the shared schemas, state machines and conformance validators using synthetic fixtures.
2. **Evidence foundation:** implement authorised retrieval, immutable evidence references, provenance and budget accounting.
3. **General analysis kernel:** implement the operation registry, profiling, descriptive statistics, deterministic comparisons and qualification rules.
4. **Relationship and integrity analysis:** add entity/link operations, contradiction detection and evidence-sufficiency checks.
5. **Governed domain packages:** add only confirmed KPI, SLA and business rules with effective dates and approval records.
6. **Verification and projection:** implement independent verification and canonical-to-editorial projection controls.
7. **Path A conformance:** run synthetic contract, determinism, failure and fairness tests. Benchmark execution remains a later, separately authorised activity.

## Recommended first implementation work package

**B03-WP01 — Shared Investigation Contracts and Synthetic Conformance Fixtures**

After architectural approval, define versioned schemas for `EvidenceRef`, `RetrievalRequest`, `RetrievalResult`, `InvestigationBudget`, `BudgetLedger`, `AnalysisOperation`, `Hypothesis`, `ProposedFinding`, `VerificationDecision`, `InvestigationResult` and `CanonicalReport`. Add synthetic fixtures and schema/state-transition tests. Include stable serialization, identifier rules, provenance requirements, failure states and forward-compatibility rules.

Exit criteria are: schema review completed; every type maps to the approved requirement set; invalid references and illegal state transitions fail closed; round trips are stable; Path A/B/C adapters can target the same contracts; and no legacy runtime dependency, connector, external model or report renderer is introduced. This work package does not implement analytical methods or execute the benchmark.

## Source and evidence limits

The inspected legacy source came from `Nexus_Stage_10.3.43_SPI4_Hotfix_Integrity_Fixed.zip`, SHA-256 `19e58f2dac184f2cbeccb6f93c81883f47b68120d17ee7f02d90dcbdeff6b3df`. B02 recorded selected Linux test executions against an extracted copy; this package relies on that recorded evidence and does not rerun or extend the legacy suite. Portable or Linux execution does not establish Windows, connector, database or live-source behaviour.
