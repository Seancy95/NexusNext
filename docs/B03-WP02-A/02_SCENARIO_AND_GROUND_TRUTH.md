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

## 5. Proposed counts and sampling

- Approximately 10 open development/pilot scenarios may validate procedure and variance assumptions. They provide no confirmatory competence evidence.
- The controlled hidden evaluation is **proposed** to start with at least 40 distinct scenarios, including at least 6 no-material and 6 insufficient-evidence scenarios, with the other required families represented according to the frozen sampling plan.
- Final count is set by prospective paired power or precision analysis using pilot variance, the smallest decision-relevant effect, planned strata, multiplicity and scenario-family clustering. Forty is a planning floor, not automatic proof of adequacy.
- Extended evaluation may use 100+ distinct scenarios when rare critical failures, category conclusions or narrow intervals require it.
- Deterministic builds run once per scenario for the primary estimate; at least 20% receive a duplicate execution selected before outcomes to detect nondeterminism. Any stochastic component would require at least three seeded repeats per scenario/configuration cell, still clustered by scenario.

## 6. Scenario acceptance checks

A hidden scenario is admitted only if both systems can reach every scored evidence item under the common operation catalogue and budget; the reference calculations reproduce; materiality rules are unambiguous; the correct terminal class is independently agreed; alternative valid paths are represented; no package metadata or identifiers reveal protected truth; and the scenario is absent from implementation-accessible training, prompt, fixture and repository material.

If a scenario defect is found after freeze, it is quarantined. The adjudicator applies the preregistered invalid-scenario rule without seeing system identity where possible. Replacement uses a new scenario from the same frozen sampling frame and is fully disclosed.
