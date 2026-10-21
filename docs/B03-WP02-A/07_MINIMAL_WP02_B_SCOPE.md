# Proposed minimal WP02-B implementation scope

## 1. Objective

WP02-B would implement only enough deterministic investigative behaviour to test the WP02-A question over the approved synthetic operational-deterioration scenario population. It would not implement the full Baseline engine or the 20-method catalogue.

This document is a proposal. WP02-B is not authorised and no listed component exists.

## 2. Minimum functionality

| Capability | Bounded proposed behaviour | PRE01 method subset |
|---|---|---|
| Question/scope admission | Map a typed evaluation question to frozen metric, population, periods and allowed sources; material ambiguity stops | narrow governed parser, not general language interpretation |
| Evidence quality profile | Counts, missingness, duplicates, freshness and source reconciliation for supplied synthetic tables | M08 subset |
| KPI/period change | Approved numerator/denominator and absolute/relative comparison | M06 plus M01 subset |
| Segment/mix analysis | One- and two-dimension decomposition with reconciliation and minimum-cell qualification | M07 subset |
| Contradiction detection | Compare aligned source values/states and preserve unresolved conflict | M12 subset |
| Template hypotheses | Instantiate a small frozen library for within-segment change, mix shift, quality artifact, delayed effect and unresolved competing explanations | M13 subset |
| Hypothesis update | Apply declared support, falsifier and contradiction predicates; supported remains provisional | M14 subset |
| Follow-up selection | Generate registered operations, apply eligibility gates, rank material evidence gaps and discriminatory value lexicographically, stable tie-break, no-progress ledger | M15/M18 bounded subset |
| Sufficiency and qualification | Decide proposed/inconclusive/no-material outcome from mandatory clauses and attach limitations | M17/M19 subset |
| Proposed findings/outcome | Emit WP01 `ProposedFinding`, `VerificationRequest`, `InvestigationOutcome` and trace; never accept/publish | M20 subset and WP01 contracts |

No anomaly model, general change-point method, free-form root-cause reasoning, fuzzy entity resolution, graph traversal, narrative interpretation, causal estimator, Enhanced Mode or report generator is included.

The use of this predefined deterministic subset is legitimate and expected. Generalisation evidence will concern correct applicability decisions, combinations, ordering and follow-up adaptation under varied evidence structures. WP02-B is not required to invent methods outside this subset or exhibit unrestricted reasoning. This clarification does not expand the implementation scope.

## 3. Shared evaluation components

The prospective package may include a synthetic fixture provider, a finite registered-operation catalogue, budget/trace controller integration, a small method registry, Nexus reasoning adapter, comparator adapter and output manifest adapter. Logical roles may remain in one process where separation adds no security value, but WP01 authority checks remain explicit.

The evaluator/scorer, hidden store and access controls are independent evaluation infrastructure and are not implemented inside the Nexus product. Hidden scenarios must never be placed in the implementation repository.

## 4. Dependencies

- Accepted WP01-R01 contracts and authority denials, with no reopening absent a demonstrated deficiency.
- Approved WP02-A rubric, scenario interface, comparator and budget contract.
- Python runtime and standard-library-first implementation; any new dependency requires justification and freeze.
- Synthetic schemas and open development fixtures created only after WP02-B authorisation.
- Separately controlled evaluation operator/scorer interface.

## 5. Deterministic selection contract

The proposed planner would use inspectable eligibility gates followed by a stable lexicographic order: mandatory integrity/contradiction need; materiality; expected discriminatory value; evidence authority/coverage; assumption risk; bounded cost; stable operation ID. Every candidate and rejection reason is traced. No unexplained weighted intelligence score is permitted. Equivalent completed requests are suppressed; retries require a typed retry condition and budget.

This is a prospective contract description, not an implemented algorithm.

## 6. Stop rules

Stop with a proposed finding only when every mandatory support and qualification clause is satisfied and no unresolved material contradiction blocks the claim. Stop no-material when all eligible material leads are below threshold. Stop inconclusive when competing explanations cannot be discriminated with remaining authorised evidence. Stop blocked/failed/budget-exhausted on the corresponding typed condition. Never continue solely to increase cosmetic confidence.

## 7. WP02-B acceptance boundary

WP02-B may demonstrate deterministic traceability, method correctness on open golden fixtures, bounded multi-round behaviour and contract conformance. It cannot claim independent investigative advantage until the protected evaluation is executed under WP02-A controls. It cannot establish production, Windows isolation, reporting, Enhanced Mode or company-data readiness.

## 8. Explicit exclusions and stop

Do not implement CAP-15/CAP-17 in full, the remaining method catalogue, Enhanced/LLM integration, live connectors, company-data access, automatic finding acceptance, report/publication controls, CLOUD-EVAL execution or WP02-C. Stop after the bounded implementation and open developer fixtures if later authorised, then submit the frozen build for the independent evaluation process.
