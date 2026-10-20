# Independent evaluation and contamination-control plan

## 1. Role separation

| Role | May access | Must not access before freeze | Responsibility |
|---|---|---|---|
| Nexus implementer | Public spec, development scenarios, interfaces and open fixtures | Hidden inputs, protected truth, scoring annotations, expected paths and evaluator feedback | Submit frozen Nexus build |
| Comparator implementer/owner | Same public material and development fixtures | Same protected hidden material | Submit competent frozen comparator |
| Hidden-scenario author | Scenario-authoring environment and assigned truth packages | Implementation internals beyond published interface where avoidable | Create independent synthetic scenarios |
| Ground-truth reviewer | Protected input/truth and reference calculations | System outputs until truth approval | Independently verify truth and acceptable alternatives |
| Scenario custodian | Encrypted hidden packages, ACLs and manifests | Implementation changes | Own release, access logs, revisions and retirement |
| Evaluation operator | Frozen executable builds and input-only scenario release | Answer package and rubric annotations | Run paired evaluation without content assistance |
| Independent scorer | Frozen outputs, protected truth and public rubric after runs | Implementation authority | Score events/scenarios and document failures |
| Adjudicator | Disputed outputs/truth with blinded system identity where feasible | Implementation changes | Resolve predeclared disputes and scenario defects |
| Release/evaluation authority | Manifests, approvals and gate evidence | No conflicting implementer role | Freeze and issue separate judgments |

One person may hold multiple roles only when the independence claim is downgraded, conflicts are disclosed, and compensating external review is approved. An implementer cannot author or score hidden scenarios used to claim independent competence.

## 2. Storage and access enforcement

Hidden input and truth must be held outside this GitHub repository, cloud workspace, prompts, issue trackers and any filesystem accessible to implementation agents. The proposed custody environment is a separately administered encrypted store with group-based least privilege, MFA, immutable access logs, separate input/truth objects and named custodians.

The implementation repository contains only public specifications, open development fixtures and interface schemas. At execution, an operator service releases input packages to an isolated run workspace. Answer packages remain in the scorer environment. Output transfer is one-way to the scoring store. No implementation process receives credentials for the truth store.

Instructions telling an agent not to inspect accessible files do not establish secrecy. If technical ACLs, logs and separate administration cannot be demonstrated, the exercise is labelled **developer testing**, not independent evaluation.

## 3. Version and freeze manifests

Before hidden release, the evaluation authority signs a manifest containing:

- public specification/rubric/threshold revisions;
- scenario sampling frame and encrypted input/truth digests;
- Nexus and comparator source/build/container/dependency digests;
- operation catalogue, provider, controller, verifier and contract revisions;
- policies, budgets, seeds, randomisation plan and run order commitment;
- evaluator/scorer code and reference-calculation revisions;
- access-control group membership and access-log checkpoint;
- permitted recovery, exclusion, retry and adjudication rules; and
- retention/destruction dates.

Implementation freeze precedes release of any hidden input. Any build change, including configuration or dependency change, creates a new candidate revision and requires documented disposition. Evaluator feedback is withheld until the full planned comparison block finishes.

## 4. Contamination prevention and detection

Before freeze, custodians search development fixtures, repository history, prompts, logs and accessible stores for scenario IDs, unique values, expected findings and generator fingerprints. Hidden packages use opaque IDs and strip comments, filenames, metadata and ordering signals that reveal truth. Scenario authors cannot reuse open scenario seeds or exact datasets.

During execution, immutable logs record every package access, tool call, retrieval and output. Network and filesystem access are limited to approved inputs/services. Unexpected access, answer-like literals in implementation artifacts, suspiciously exact hidden annotations, or pre-release access-log events trigger investigation.

The investigation preserves affected artifacts, suspends unblinding, identifies who/what accessed which revision, assesses whether content could affect output, and records a disposition. Affected scenarios are not quietly rescored.

## 5. Retirement and replacement

A scenario is contaminated when an implementation agent/operator received protected truth, expected findings, false leads, contradictions, stop rules, causal mechanism or scoring annotation before the relevant build freeze, or when leakage cannot reasonably be excluded. It is retired from hidden use for that implementation lineage and becomes development/regression material.

Replacement comes from the frozen sampling frame, matches the stratum, receives fresh independent truth review and a new manifest entry. Replacement never occurs merely because a system performed poorly. Counts, reasons and effects are reported. If contamination is broad or differential, experimental validity fails rather than being repaired through selective replacement.

## 6. Independent execution and scoring

The operator receives input-only packages and invokes both frozen systems under randomised paired order. The scorer receives outputs only after the block is complete. Where practical, outputs are system-blinded during event scoring. Scorers apply the frozen rubric; adjudication history is append-only. Failed, timed-out and inconclusive runs remain visible under prospective rules.

Independent evaluation requires: role separation, inaccessible protected truth, frozen builds/rubric, access evidence, input-only execution, independent scoring, reproducible manifests, and disclosed deviations. Missing any material element yields Inconclusive or developer-testing status according to impact.

## 7. Retention

Synthetic evaluation evidence is preserved according to the approved benchmark retention schedule for audit. Future company information is prohibited under WP02-A. Any later company-data proposal must reuse Nexus disclosure and retention authority and must not create an unauthorised secondary evidence store.
