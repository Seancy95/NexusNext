# Public scoring rubric and investigative value decision framework

## 1. Scoring unit and event rules

Scorers first record each expected material finding, actual material claim, contradiction, calculation, evidence reference, follow-up and stopping decision. Event-level errors are preserved before aggregation. Scenario scores are macro-averaged so a scenario with many annotated findings cannot dominate the study.

Model-generated hypotheses are not findings. Only proposed findings presented for Nexus verification are scored as actual findings; any item accepted by the independent verifier receives the additional verification-integrity judgment. Workflow completion earns no correctness credit by itself.

## 2. Scenario rubric

| Dimension | Scenario measure | Full-credit condition | Critical treatment |
|---|---|---|---|
| Material finding recall | weighted recovered expected materiality / weighted expected materiality | All observable, material expected findings recovered within tolerance | Missed critical finding recorded individually |
| Material claim precision/restraint | supported material claims / all material claims | No false or unsupported material claim | Unsupported material claim accepted as verified fails verification gate |
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
2. **Material unsupported-claim rate:** unsupported material claims divided by all material claims, reported overall and by scenario; zero-claim cases remain visible.
3. **Correct terminal-outcome rate:** correct finding/no-finding/insufficient classification.
4. **Incremental valid discovery:** material Nexus finding absent from comparator output that matches protected truth and is independently verified; report count, scenario coverage and precision.
5. **Material contradiction recall:** scenario-level weighted recall and paired difference.
6. **Appropriate uncertainty/stopping:** scenario-level correct rate, with premature and excessive stopping reported separately.

## 5. Secondary efficiency and complexity measures

Report retrievals, rounds, repeated equivalent requests, evidence bytes, elapsed time, CPU/memory and recoverable failures. Separately report implementation source size, dependency count, operation/rule count, configuration burden, maintenance responsibilities and required control surfaces. Complexity does not change analytical truth; it informs the investment decision after gates and primary performance.

## 6. Proposed prospective thresholds

These thresholds are **Proposed, untested and subject to independent approval before implementation**.

| Criterion | Proposed success threshold | Justification |
|---|---|---|
| Integrity and authority gates | Zero events | A bounded evaluation cannot trade away evidence or authority integrity |
| Nexus absolute material-finding recall | At least 0.80 macro-average; no critical-finding recall below 0.90 overall | Avoid declaring advantage for a system that remains substantively weak |
| Paired recall advantage | Mean improvement at least 0.10 and multiplicity-adjusted 95% interval lower bound above 0 | Ten percentage points is the minimum benefit judged likely to justify an adaptive investigation layer; positive interval excludes chance-compatible zero |
| Nexus material unsupported-claim rate | At most 0.05, with one-sided 95% upper bound at most 0.10 | Material false claims are costly; uncertainty acknowledges finite scenarios |
| Unsupported-claim non-inferiority | Nexus minus comparator no more than +0.02, upper 95% bound no more than +0.05 | Recall gain cannot be purchased through materially worse speculation |
| Correct terminal outcome | At least 0.80 overall and at least 0.80 separately for no-finding and insufficient-evidence strata | Tests useful restraint as well as positive detection |
| Contradiction recall | At least 0.80 and paired improvement at least 0.10 when comparator recall is below 0.90; otherwise non-inferior within 0.05 | Requires value where headroom exists without penalising a strong comparator ceiling |
| Appropriate stopping | At least 0.80; premature stopping no more than 0.10; repeated-unproductive-retrieval scenarios no more than 0.10 | Bounded investigation must pursue material gaps and stop without loops |
| Incremental discovery precision | At least 0.80; at least 5 distinct scenarios with a valid incremental material discovery for a value-add claim | Prevents a few speculative extras from appearing valuable |
| Efficiency | Nexus retrieval and evidence-volume median no more than 1.5× comparator unless preregistered incremental findings justify the excess | Allows adaptive exploration but caps disproportionate cost |

The recall and unsupported-claim comparisons are confirmatory co-primary criteria. Both, every non-negotiable gate, and the absolute-quality criteria must pass. Secondary results cannot rescue a failed co-primary criterion.

## 7. Statistical analysis and uncertainty

- Freeze estimands, scenario exclusions, weights, strata and comparisons before outcomes.
- Use paired scenario-level differences. Report means/medians, raw numerators/denominators, and 95% intervals clustered by scenario; a paired bootstrap or randomisation interval is acceptable when preregistered.
- Use paired binary methods such as McNemar for terminal-outcome comparisons where appropriate.
- Preserve repeats as nested checks. If stochastic repeats are introduced, use a hierarchical/mixed model or scenario-clustered summaries.
- Control family-wise multiplicity for the co-primary comparisons and any confirmatory strata using a frozen Holm procedure. Other analyses are labelled exploratory.
- Report sensitivity to materiality weights, invalid-scenario handling and missing runs without replacing the primary result.
- A minimum of 40 distinct controlled scenarios and required negative/inconclusive strata is necessary for a decision under this proposal, but the prospective power/precision analysis may require more. If precision remains inadequate, the result is inconclusive.

## 8. Decision rules

**Success:** experimental validity passes; all zero-tolerance gates pass; both co-primary and all absolute thresholds pass; minimum evidence and precision requirements are met; complexity review finds the benefit operationally proportionate.

**Failure:** any zero-tolerance gate fails; Nexus misses an absolute threshold; a co-primary criterion fails with adequate precision; or Nexus is materially worse on unsupported claims. Analytical failure does not retroactively invalidate a properly run experiment.

**Inconclusive:** integrity remains intact but intervals or scenario coverage cannot resolve the approved smallest effect; material infrastructure asymmetry biases the comparison; or minimum evidence is not achieved. Inconclusive is not Passed.

**Further investment not justified:** adequate valid evidence shows recall advantage below 0.05, the approved 0.10 benefit is excluded, absolute restraint/correctness fails, critical failures recur, or incremental operating complexity is disproportionate to a small benefit. A new approach may be proposed, but the observed result remains.

Threshold changes after hidden results are prohibited. Any revised threshold applies only to a new preregistered evaluation and is disclosed as such.
