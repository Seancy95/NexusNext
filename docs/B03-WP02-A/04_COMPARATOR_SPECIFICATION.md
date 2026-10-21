# Competent deterministic comparator specification

## 1. Purpose and boundary

The comparator represents a competent conventional deterministic reporting and analytics solution, not a deliberately weak straw baseline and not automatically Nexus 10.3.43. It uses conventional scheduled/on-demand calculations, a reviewed diagnostic playbook and rule-driven follow-up. It does not use the proposed Nexus hypothesis graph or adaptive lexicographic investigation policy.

Legacy code may inform domain rules only when provenance, correctness and authority are separately approved. It is not the scientific control by default.

## 2. Mandatory capability

| Capability | Minimum comparator behaviour | Acceptance fixture |
|---|---|---|
| KPI/SLA calculation | Correct governed numerator, denominator, exclusions, calendar and rounding | Golden boundaries, zero denominator and exclusion cases |
| Trend/period comparison | Absolute/relative change and consistent windows | Stable, deteriorating, improving and missing-period series |
| Population/cohort comparison | Fixed reviewed segment list, contribution/mix table and reconciliation | Within-group and mix-shift cases including Simpson-type reversal |
| Anomaly detection | Reviewed robust/control-limit rule with fixed threshold and qualification | Injected anomaly/no-anomaly with sparse-history qualification |
| Relationship exploration | Approved key joins and basic correlation table with sample/coverage warning | True join, collision, misleading correlation and missing link |
| Rule exceptions | Effective-dated deterministic exception rules | Boundary, superseded rule and missing-fact cases |
| Data quality | Missingness, duplicates, inconsistency, freshness and coverage indicators | Known incomplete/duplicate/contradictory sources |
| Follow-up | Reviewed finite decision tree may request relevant segment, source reconciliation or quality detail | Multi-step cases with specified branch triggers |
| Qualification/stopping | State limitations, no material finding or insufficient evidence; stop at playbook/budget boundary | Mandatory negative and inconclusive scenarios |

The comparator can recover findings from any of these standard operations and receives fair follow-up opportunities. Its fixed playbook may combine operations over multiple rounds. It must not be restricted to a static predefined report when the question calls for a competent analyst to drill down.

## 3. Shared experimental services

The comparator and Nexus use the same WP01 logical contracts, synthetic provider, registered calculations, evidence repository, authorisation controller, budget accounting, independent verifier and scoring/output schema. Neither can accept its own finding. The comparator can cite the same evidence and submit the same `ProposedFinding` shape.

The following must be equal: visible metadata, authorised sources/fields, snapshots, retrieval catalogue, failure responses, retry policy, maximum rounds/retrievals/bytes/time, materiality policy, governed calculations and verifier access. Differences in internal reasoning traces are expected and recorded.

## 4. Ownership and independent review

- A comparator owner distinct from the Nexus implementation owner maintains the specification and reference implementation.
- A domain/calculation reviewer checks KPI, population and rule correctness.
- An evaluation-method reviewer checks that capability and budget are competent and fair.
- A scenario representative checks, without disclosing hidden answers to implementers, that comparator operations can reach scored evidence.
- The evaluation authority approves or rejects comparator readiness before any hidden run.

Consensus among AI reviewers is not empirical proof.

## 5. Gate C-SPEC — specification approval before WP02-B authorisation

Comparator **specification** approval is required before bounded WP02-B implementation may be authorised. The independent review confirms the capability catalogue, ordinary analytical methods, multi-round opportunity, evidence equivalence, resource model, limitations, open fixtures and challenge process. It records every objection and its accepted resolution, rejected rationale or blocking status.

C-SPEC does not require an implemented comparator. Passing it allows Nexus and comparator development to proceed against a stable fair interface; it does not authorise comparative execution. An unresolved material fairness or competence objection blocks WP02-B authorisation.

## 6. Gate C-IMPL — implementation approval before comparative execution

After it is implemented and before any comparative hidden evaluation, the comparator must:

1. pass all public golden KPI, trend, segmentation, anomaly, quality, relationship and exception fixtures;
2. correctly produce no-finding and insufficient-evidence outcomes on open fixtures;
3. demonstrate every permitted follow-up branch and budget stop;
4. use valid evidence references and the shared verifier without authority bypass;
5. pass an independent code/spec review that identifies capability limitations;
6. receive a fairness sign-off confirming evidence and opportunity parity; and
7. freeze source, dependencies, configuration, playbook, thresholds and digest; and
8. pass an independent competence and fairness review against the approved C-SPEC, including evidence-access and opportunity-budget parity dry runs.

A challenge window occurs before hidden execution. Substantiated deficiencies are corrected for both fairness and fixtures, followed by a new freeze and C-IMPL review. Unresolved reviewer objections are recorded and block execution when material. After hidden outcomes, comparator changes are prohibited for that evaluation block. If a previously unknown material comparator defect invalidates fairness, the affected comparison is Inconclusive; the defect and rerun decision remain public.

## 7. Limitations to report

The comparator is expected to be weaker at selecting among unfamiliar competing explanations and adapting follow-ups beyond its reviewed playbook. It may nevertheless equal or beat Nexus. Its limitations, fixed dimensions, rules and operation branches are published before execution so they cannot be tailored retrospectively.
