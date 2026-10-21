# Scenario-generation and ground-truth methodology

## 1. Scenario population

Scenarios are realistic, wholly synthetic operational investigations. The target population combines the following factors rather than relying on one September example:

| Dimension | Required levels |
|---|---|
| True outcome | material deterioration; no material finding; insufficient evidence |
| Mechanism | within-group rate change; population/mix change; delayed effect; data-quality artifact; competing mechanisms; no mechanism |
| Evidence condition | complete; missing; duplicated; inconsistent; delayed; contradictory; irrelevant/noisy |
| Temporal challenge | comparison-window shift; seasonality; reporting delay; boundary/time-zone trap; causal order |
| Explanatory challenge | genuine signal; misleading correlation; false lead; confounding; observational evidence insufficient for cause |
| Investigation demand | direct calculation; one follow-up; multiple discriminating rounds; justified early stop |

At minimum, each controlled set contains genuine operational deterioration, apparent deterioration caused by population change, competing explanations, misleading correlation, incomplete records, duplicates, inconsistent records, contradictory systems, delayed effects, temporal traps, insufficient evidence, false/irrelevant leads, and no-material-finding cases.

The August–September example is development/regression material only. It is never counted as hidden evidence of generalisation.

## 2. Generation process

1. The independent scenario author selects a preregistered cell from the scenario matrix and writes a causal data-generating specification.
2. A deterministic generator seed creates source-level records, source-specific latency/error processes and declared evidence coverage.
3. The author produces an observable-evidence model separately from the synthetic causal mechanism.
4. A second ground-truth reviewer independently calculates expected metrics, identifies what the observable evidence supports, and challenges causal wording.
5. A scenario-quality reviewer checks realism, nontriviality, operation reachability, comparator accessibility, ambiguity and accidental answer leakage.
6. Disagreements are adjudicated before freeze. Accepted alternatives and scoring tolerances are recorded prospectively.
7. Input and protected answer packages receive separate immutable versions and digests. Only the input package is released to the execution operator.

Scenario variation must not be cosmetic. New scenarios vary mechanisms, populations, source inconsistencies, evidence gaps and necessary investigative decisions. Surface renaming of one data-generating process remains the same scenario family and is accounted for in sampling.

## 3. Protected ground-truth record

For every scenario the independent authority maintains:

- scenario ID/family/revision and generator revision/seed;
- intended question, correct scope, population, denominator and comparison period;
- source snapshots and source-authority/quality facts;
- material expected findings with magnitude, tolerance and severity;
- relevant, irrelevant, contradictory and unavailable evidence;
- unsupported explanations and prohibited causal statements;
- underlying synthetic causal mechanism, where one exists;
- observable-evidence conclusions and their maximum justified claim strength;
- required calculations and independently reproduced reference values;
- expected discriminating follow-ups and acceptable alternatives;
- appropriate stop, inconclusive and clarification conditions;
- acceptable alternative conclusions/wording;
- critical-failure triggers and scoring annotations; and
- reviewer identities, decisions, revisions and digests.

The causal-mechanism field is never automatically an expected finding. If observable evidence supports only association, a causal assertion is scored unsupported even when it happens to match the generator.

## 4. Mandatory negative and inconclusive cases

### No material finding

At least the preregistered minimum stratum contains scenarios where all supported effects remain below the frozen materiality threshold or apparent changes reconcile to measurement/population effects. Correct behaviour is to state that no material issue was identified, cite coverage and limitations, and stop. Fabricated findings, threshold shopping and repeated low-value retrieval are penalised.

### Insufficient evidence

At least the preregistered minimum stratum contains scenarios where evidence cannot distinguish material explanations or establish a reliable denominator. Correct behaviour is an inconclusive outcome with the unresolved gap, competing explanations and justified stop. Choosing a winner, implying causation or retrieving repeatedly after the resolvable opportunity is exhausted is penalised.

These are separate outcome classes and receive separate accuracy, restraint and stopping results.

## 5. Corrected proposed counts and sampling

- Use 12–16 open development/pilot scenarios to validate interfaces, scoring, variance assumptions and failure procedures. They provide no confirmatory competence evidence and are never pooled into the hidden estimate.
- The paired macro-recall design targets a minimum worthwhile improvement of 0.10. Under the explicit planning assumption that the standard deviation of paired scenario recall differences is 0.30, two-sided alpha 0.05 and 80% power, the normal approximation is `n = (1.96 + 0.84)^2 × 0.30^2 / 0.10^2 = 70.6`, rounded to 71 distinct scenarios. Allowing approximately 10% unusable scenarios/runs gives 79, rounded to **80 distinct confirmatory scenarios**.
- Eighty supports the overall co-primary comparison under those assumptions. It does not adequately support strong separate claims about negative and insufficient-evidence strata if those strata are small.
- For the full programme decision, use **100 distinct hidden scenarios** as the proposed design: 60 material-finding scenarios, 20 no-material scenarios and 20 insufficient-evidence scenarios. Mechanism/data/temporal categories cross these outcome strata rather than forming mutually exclusive leftovers. At least 20 scenarios combine multiple mechanisms.
- If resources permit only 80, preserve at least 15 no-material and 15 insufficient-evidence scenarios. Separate outcome-class conclusions are then limited or labelled Inconclusive unless their prospective precision criterion is met.
- Pilot estimates replace the assumed paired SD only before hidden outcomes and before confirmatory sample size is frozen. If `SD=0.35`, the same formula gives approximately 97 scenarios before attrition; the programme must increase the sample or accept an Inconclusive confirmatory result.
- A zero observed critical event does not establish zero population risk. The approximate one-sided 95% “rule of three” upper bound is 3.75% at 80 scenarios and 3.0% at 100. Any observed critical event still fails the applicable gate, while the interval limits the population claim.
- Deterministic builds run once per scenario for the primary estimate; at least 20% receive a duplicate execution selected before outcomes to detect nondeterminism. Any stochastic component requires at least three seeded repeats per scenario/configuration cell and a revised power model. Repeats remain clustered under their scenario.

The final count and allocation are **Proposed evaluation parameters**, not approved facts. They require an independent statistical review before implementation. Counts may increase prospectively; they may not be reduced or thresholds changed after hidden outcomes.

## 6. Known-pattern competence and investigative generalisation

Predefined deterministic methods are legitimate. A system is not penalised because its calculations, rules, hypothesis templates or selection policy are deterministic. **Known-pattern competence** means applying an approved method correctly to evidence for which it is applicable. **Investigative generalisation** means selecting, combining, ordering and adapting permitted methods appropriately when evidence structure, question representation, mechanism combinations and useful follow-up sequences differ from development examples.

Hidden design must include multi-mechanism combinations, column/table and relationship-structure perturbations, equivalent questions represented differently, unfamiliar but typed relationships, irrelevant/misleading evidence, competing hypotheses, contradictory sources, alternative necessary follow-up orders, and cases where the development-template path points to the wrong next action.

For selected scenario families, the authority creates metamorphic variants with the same analytical truth but changed names, ordering, table splits/joins, source placement or question phrasing, plus contrast variants that look similar but require different actions. Scoring compares outcome correctness and decision traces. Indicators of shortcut dependence include fixed operation sequences insensitive to evidence, reliance on scenario IDs/field order, failure under meaning-preserving representation changes, identical hypotheses despite changed falsifiers, and divergence between the stated decision rule and trace.

The evaluation asks whether bounded methods are used appropriately. It does not require unrestricted reasoning, novel methods outside the approved catalogue, CAP-15/CAP-17 completion or unbounded handling of arbitrary domains.

## 7. Scenario acceptance checks

A hidden scenario is admitted only if both systems can reach every scored evidence item under the common operation catalogue and budget; the reference calculations reproduce; materiality rules are unambiguous; the correct terminal class is independently agreed; alternative valid paths are represented; no package metadata or identifiers reveal protected truth; and the scenario is absent from implementation-accessible training, prompt, fixture and repository material. Generalisation variants must test permitted method selection rather than require an unavailable method.

If a scenario defect is found after freeze, it is quarantined. The adjudicator applies the preregistered invalid-scenario rule without seeing system identity where possible. Replacement uses a new scenario from the same frozen sampling frame and is fully disclosed.
