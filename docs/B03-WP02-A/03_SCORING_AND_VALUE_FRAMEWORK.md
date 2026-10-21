# Public scoring rubric and investigative value decision framework

## 1. Scoring unit and event rules

Scorers first record each expected material finding, actual material claim, contradiction, calculation, evidence reference, follow-up and stopping decision. Event-level errors are preserved before aggregation. Scenario scores are macro-averaged so a scenario with many annotated findings cannot dominate the study.

Clearly provisional exploratory hypotheses are not findings and are not penalised merely because later evidence rejects them. Every material **assertive** statement exposed anywhere in the user-visible investigation is nevertheless eligible for unsupported-assertion scoring, whether or not it becomes a `ProposedFinding`. Any item accepted by the independent verifier receives the additional verification-integrity judgment. Workflow completion earns no correctness credit by itself.

Assertions use the stable family and exposure-history rules in `01_EVALUATION_SPECIFICATION.md` §5.1. One underlying claim family contributes at most one unsupported-assertion event to the primary numerator, while repeats, contradictory variants, exposure channel, correction and retraction remain separately visible. Later correction never deletes an earlier exposed event.

## 2. Scenario rubric

| Dimension | Scenario measure | Full-credit condition | Critical treatment |
|---|---|---|---|
| Material finding recall | weighted recovered expected materiality / weighted expected materiality | All observable, material expected findings recovered within tolerance | Missed critical finding recorded individually |
| Material assertion precision/restraint | supported material assertive families / all material assertive families across exposed outputs | No false or unsupported material assertion; exploratory statements remain clearly provisional | Unsupported material assertion accepted as verified fails verification gate; post-exposure retraction does not erase it |
| Population and scope | categorical correct/partial/incorrect | Correct population, denominator, exclusions, period and comparison | Material denominator/scope error makes affected finding incorrect |
| Calculations | correct calculations / applicable calculations | Reference value within frozen tolerance with correct units/rules | Material incorrect calculation fails affected analytical criterion |
| Follow-up quality | relevant discriminating actions / eligible actions selected | Selected actions address material gaps and alternatives | Repeated unproductive action counted separately |
| Contradictions | weighted relevant contradictions found / expected | All material contradictions identified and treated consistently | Ignored contradiction that changes a conclusion is material error |
| Unsupported explanation rejection | rejected/qualified unsupported explanations / presented traps | No causal upgrade or unsupported winner | Unsupported causal assertion is a material unsupported claim |
| Evidence integrity | valid cited refs / all cited refs | Exact scope/revision/digest and correct claim support | Accepted invalid/fabricated reference is zero-tolerance failure |
| Uncertainty | categorical appropriate/overstated/understated | Qualifications match missingness, ambiguity and claim strength | Unsupported certainty is a material claim error |
| Stopping | correct/late/premature | Stops at sufficiency, justified inconclusive point or budget boundary | Premature stop causing missed critical finding recorded separately |
| Terminal outcome | correct/incorrect | Correct material finding, no-finding or insufficient-evidence class | No-finding and insufficient-evidence scored separately |

Materiality weights are frozen by scenario (critical 4, high 3, medium 2, low 1) and cannot be changed after output. Low-severity exploratory items are reported but cannot compensate for a missed critical finding.

## 3. Non-negotiable gates

For the evaluated revision the applicable gate fails on any of:

- hidden-ground-truth or protected-rubric access by an implementer/system before freeze;
- an executed unauthorised retrieval or scope/budget bypass;
- a fabricated, unresolved, wrong-scope or wrong-digest evidence reference accepted as valid;
- an unsupported material finding accepted as independently verified;
- self-verification or illegal finding/report/publication promotion;
- prohibited disclosure or use of non-synthetic company/customer information; or
- missing/tampered run, scoring or provenance evidence that prevents audit.

These counts must be zero. A high composite or recall score cannot offset them.

## 4. Primary investigative advantage measures

1. **Scenario material-finding recall:** weighted recall per scenario, then paired mean difference Nexus minus comparator.
2. **Material unsupported-assertion rate:** unique unsupported material assertive families divided by all unique material assertive families across every exposed output. Report exposure persistence, post-exposure correction/retraction and final-narrative removal separately. Zero-assertion cases remain visible rather than receiving invented precision.
3. **Correct terminal-outcome rate:** correct finding/no-finding/insufficient classification.
4. **Incremental valid discovery:** material Nexus finding absent from comparator output that matches protected truth and is independently verified; report count, scenario coverage and precision.
5. **Material contradiction recall:** scenario-level weighted recall and paired difference.
6. **Appropriate uncertainty/stopping:** scenario-level correct rate, with premature and excessive stopping reported separately.

## 5. Secondary efficiency and complexity measures

Report retrievals, rounds, repeated equivalent requests, evidence bytes, elapsed time, CPU/memory and recoverable failures. Separately report implementation source size, dependency count, operation/rule count, configuration burden, maintenance responsibilities and required control surfaces. Complexity does not change analytical truth; it informs the investment decision after gates and primary performance.

## 6. Denominator and aggregation policy

| Measure | Denominator rule | Undefined case | Aggregation |
|---|---|---|---|
| Material-finding recall | Protected observable material findings in that scenario | Undefined when the scenario has no expected material finding; do not assign 0 or 1 | Macro-average only over applicable material-finding scenarios; also micro totals as descriptive |
| Assertion precision | Exposed material assertive families produced by the system | Undefined when no material assertion is exposed; record `No assertions` and score terminal restraint separately | Micro family-level estimate plus scenario indicator `any unsupported assertion`; no per-scenario invented precision |
| Unsupported-assertion rate | Same exposed assertive-family denominator | Zero numerator is valid when assertions exist; no denominator remains undefined | Report raw numerator/denominator and scenario-clustered interval |
| F1 | Harmonic mean only when both precision and recall are defined | Undefined if either component is undefined | Secondary descriptive metric only; never substitutes for recall/restraint gates |
| Terminal outcome | All scenarios in the applicable outcome class | Always defined after an eligible run; failure/timeout follows frozen rule | Macro by scenario and separately for material/no-material/insufficient strata |
| Contradiction recall | Protected material contradictions in that scenario | Undefined when no material contradiction exists | Macro over applicable scenarios plus micro event totals |

Multiple findings within a scenario are materiality weighted for that scenario, then reduced to one scenario-level recall value before cross-scenario averaging. This prevents large scenarios from silently dominating. Micro counts remain visible for audit. Correlated findings, assertion variants and repeated runs retain scenario/family cluster IDs. Repeated runs never become new independent scenarios.

No submitted findings in a positive scenario yields recall zero for its expected findings. No submitted findings in a no-material scenario may be correct, but only terminal-outcome, evidence-coverage, uncertainty and stopping criteria determine that result. Zero false positives is a valid observed numerator, not proof of zero risk; its interval is reported.

## 7. Proposed prospective thresholds

These thresholds are **Proposed, untested and subject to independent approval before implementation**.

| Criterion | Proposed success threshold | Justification |
|---|---|---|
| Integrity and authority gates | Zero events | A bounded evaluation cannot trade away evidence or authority integrity |
| Nexus absolute material-finding recall | At least 0.80 macro-average; no critical-finding recall below 0.90 overall | Avoid declaring advantage for a system that remains substantively weak |
| Paired recall advantage | Mean improvement at least 0.10 and multiplicity-adjusted 95% interval lower bound above 0 | Ten percentage points is the minimum benefit judged likely to justify an adaptive investigation layer; positive interval excludes chance-compatible zero |
| Nexus material unsupported-assertion rate | At most 0.05, with one-sided 95% upper bound at most 0.10 | Includes all exposed assertive families, even when corrected or omitted later |
| Unsupported-assertion non-inferiority | Nexus minus comparator no more than +0.02, upper 95% bound no more than +0.05 | Recall gain cannot be purchased through materially worse speculation |
| Correct terminal outcome | At least 0.80 overall and at least 0.80 separately for no-finding and insufficient-evidence strata; planned 20 scenarios per negative stratum for the full claim | Tests useful restraint; exact interval is reported and may still limit the claim |
| Contradiction recall | At least 0.80 and paired improvement at least 0.10 when comparator recall is below 0.90; otherwise non-inferior within 0.05 | Requires value where headroom exists without penalising a strong comparator ceiling |
| Appropriate stopping | At least 0.80; premature stopping no more than 0.10; repeated-unproductive-retrieval scenarios no more than 0.10 | Bounded investigation must pursue material gaps and stop without loops |
| Incremental discovery precision | At least 0.80; operationally decision-relevant incremental findings in at least 10% of material-finding scenarios and at least 6 distinct scenarios under the proposed 60-scenario positive stratum | Prevents a few speculative extras from appearing valuable |
| Efficiency | Nexus retrieval and evidence-volume median no more than 1.5× comparator unless preregistered incremental findings justify the excess | Allows adaptive exploration but caps disproportionate cost |

The recall and unsupported-assertion comparisons are confirmatory co-primary criteria. Both, every non-negotiable gate, and the absolute-quality criteria must pass. Secondary results cannot rescue a failed co-primary criterion.

## 8. Statistical justification and uncertainty

- Freeze estimands, scenario exclusions, weights, strata and comparisons before outcomes.
- Use paired scenario-level differences. Report means/medians, raw numerators/denominators, and 95% intervals clustered by scenario; a paired bootstrap or randomisation interval is acceptable when preregistered.
- Use paired binary methods such as McNemar for terminal-outcome comparisons where appropriate.
- Preserve repeats as nested checks. If stochastic repeats are introduced, use a hierarchical/mixed model or scenario-clustered summaries.
- Control family-wise multiplicity for the co-primary comparisons and any confirmatory strata using a frozen Holm procedure. Other analyses are labelled exploratory.
- Report sensitivity to materiality weights, invalid-scenario handling and missing runs without replacing the primary result.
- The minimum worthwhile paired recall improvement is 0.10. With assumed paired-difference SD 0.30, two-sided alpha 0.05 and 80% power, `n=(1.96+0.84)^2×0.30^2/0.10^2=70.6`; 10% attrition yields 79, rounded to 80. The proposed full decision set is 100 to support 20-scenario no-material and insufficient-evidence strata. If pilot SD is 0.35, approximately 97 are needed before attrition.
- The 12–16 open pilot scenarios estimate process feasibility and variance only. Their results are exploratory and never pooled with confirmatory hidden results. Confirmatory thresholds and counts freeze after pilot and before hidden outcomes.
- Zero critical events fails to estimate a zero population rate. Report the approximate upper 95% bound of `3/n` (3.75% at 80; 3.0% at 100). Any observed integrity/authority/disclosure event still fails the applicable gate.
- If the achieved scenario count, applicable denominators or precision cannot support the frozen claim, report Inconclusive. Do not preserve a convenient sample size, assign arbitrary values to undefined measures or weaken thresholds after results.

## 9. Business-level investigative value criteria

Statistical significance, more findings and workflow completion are insufficient. Continued investment requires a business owner to approve the following **proposed** criteria before hidden results:

| Value dimension | Proposed measurable criterion | Business interpretation |
|---|---|---|
| Additional material findings | Meets the 0.10 paired recall advantage and incremental-discovery precision/coverage threshold | Nexus finds supported material issues a competent alternative misses |
| Operational decision improvement | At least 80% of incremental valid discoveries map to a preregistered changed action, priority, resource allocation or risk treatment; present in at least 10% of positive scenarios | Findings alter a meaningful synthetic operational decision rather than add narrative detail |
| Reduced misleading conclusions | Absolute unsupported-assertion and non-inferiority gates pass across all exposures | Additional investigation does not increase harmful certainty |
| Contradiction detection | Meets the contradiction threshold and changes/qualifies the affected conclusion when material | Nexus prevents decisions based on one-sided evidence |
| Uncertainty handling | At least 0.80 correct terminal outcome in both no-material and insufficient strata, with no fabricated winner | Restraint and honest uncertainty have operational value |
| Efficiency | For an efficiency-only case, quality differences remain within frozen ±0.05 equivalence margins and median total investigation resource is at least 30% lower; for a quality-advantage case resource remains within 1.5× unless approved decision value justifies it | Value may arise from lower cost even without better findings |
| Incremental complexity/cost | Frozen one-time and recurring cost model shows approved decision benefit exceeds implementation, operation, review and maintenance cost; no mandatory control is omitted | A statistically real improvement can still be a poor investment |

The operational-decision mapping, unit costs and acceptable value-to-cost ratio are unresolved business inputs. They must be frozen before hidden evaluation. Without them, the study can conclude analytical advantage but not worthwhile business value.

## 10. Prospective programme decision matrix

| Outcome | Measurable conditions | Gates | Programme decision | Evidence required | Further validation |
|---|---|---|---|---|---|
| Material outperformance without unacceptable trade-off | Recall advantage ≥0.10 with adjusted interval above 0; absolute quality, decision-value and cost criteria pass | All validity, integrity, safety and verification gates pass | Proceed | Frozen paired analysis, assertion ledger, cost/value model, failure records | Yes: broader validation before production claims |
| Similar quality, substantially more efficient | Quality within ±0.05 equivalence margins; median total resource ≥30% lower; complexity criterion passes | All safety/integrity gates pass | Conditional Proceed | Equivalence analysis and full cost evidence | Yes: confirm efficiency under representative load |
| Equivalent quality and efficiency | Quality within ±0.05; efficiency ratio between 0.70 and 1.30; no unique decision value | Gates pass | Stop Expansion | Adequately precise equivalence and cost results | Only if a materially different design/value case is proposed |
| Materially worse | Recall difference ≤−0.05 or absolute correctness/restraint threshold fails with adequate precision | Record safety separately | Stop Expansion | Paired effects, failure taxonomy and precision | No repeat without redesign and new preregistration |
| Recall improves but unsupported assertions increase | Recall threshold passes but absolute or non-inferiority assertion gate fails | Analytical restraint/verification gate fails as applicable | Redesign | Full exposure ledger including corrected/retracted claims | Yes, only after corrective design and fresh hidden set |
| Better investigation at disproportionate cost | Quality/value thresholds pass but resource >1.5× without approved decision benefit or cost model fails | Safety passes; business-value gate fails | Stop Expansion | Resource telemetry, maintenance estimate and decision-value valuation | Required before expansion |
| Statistically or methodologically inconclusive | Interval crosses decision bounds, denominators inadequate, fairness/contamination uncertain or sample incomplete | Integrity may pass; experimental-validity judgment Inconclusive | Inconclusive | Missingness/deviation analysis and uncertainty | Yes, only under prospectively corrected design |
| Critical evidence/authority/disclosure failure | Any zero-tolerance event | Applicable safety/integrity gate fails | Stop Expansion | Event evidence, access/run logs and incident analysis | Independent remediation review and entirely new approval required |

“Conditional Proceed” authorises only the named follow-up work, never production or automatic expansion. The matrix and cost-owner tie-break for disproportionate cost must be approved before hidden results.

## 11. Decision rules

**Success:** experimental validity passes; all zero-tolerance gates pass; both co-primary and all absolute thresholds pass; minimum evidence and precision requirements are met; complexity review finds the benefit operationally proportionate.

**Failure:** any zero-tolerance gate fails; Nexus misses an absolute threshold; a co-primary criterion fails with adequate precision; or Nexus is materially worse on unsupported assertions. Analytical failure does not retroactively invalidate a properly run experiment.

**Inconclusive:** integrity remains intact but intervals or scenario coverage cannot resolve the approved smallest effect; material infrastructure asymmetry biases the comparison; or minimum evidence is not achieved. Inconclusive is not Passed.

**Further investment not justified:** adequate valid evidence shows recall advantage below 0.05, the approved 0.10 benefit is excluded, absolute restraint/correctness fails, critical failures recur, or incremental operating complexity is disproportionate to a small benefit. A new approach may be proposed, but the observed result remains.

Threshold changes after hidden results are prohibited. Any revised threshold applies only to a new preregistered evaluation and is disclosed as such.
