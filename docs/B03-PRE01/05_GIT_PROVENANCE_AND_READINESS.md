# Git Provenance and Repository Readiness

## 1. Actual inspected state

Close-out inspection date: 2026-10-20.

| Item | Observed state |
|---|---|
| Repository | `/workspace/NexusNext` |
| Current delivery branch | `b03-pre01-closeout-review` |
| Corrected source-document revision | `0a6dc5eac7d8a5f594426f5a159913d963433ed4` — `Complete B03-PRE01 closeout corrections` |
| PRE01 v0.1 revision | `669a7bf7072e529c04e20154587767be1090f2f8` — `Add B03-PRE01 architecture readiness design` |
| Parent | `b08d24fd9376f0537c370c0ed7af0f320b8669c5` — `Add CLOUD-EVAL-B03 baseline architecture design` |
| Remote | `origin` = `https://github.com/Seancy95/NexusNext.git` for fetch/push |
| Remote close-out branch | `git ls-remote` confirmed `b03-pre01-closeout-review` at `0a6dc5e…` after the user explicitly requested downloadable Git delivery |
| Local upstream | `b03-pre01-closeout-review` is configured to track its remote branch; the repository fetch refspec remains narrower than the usual wildcard mapping |
| Tracked content | B02 assessment/evidence, B03 design and PRE01 version 0.1 package |
| Existing untracked content | `.gitignore`, root reports/README, `config/`, B01, `inspect_environment.ps1`, `nexus_g2/`, `pyproject.toml`, root traceability, `scripts/`, `tests/` |
| PRE01 close-out content | The eight corrected source documents are committed at `0a6dc5e…`; the standalone delivery document and close-out-only archive are a later delivery clarification |
| Worktree conclusion | PRE01 v0.1 and the corrected close-out source documents have Git identity. Product/G2 source and B01 still lack commit identity because they are untracked. |

The older reports that say branch `work`, unborn branch or no `HEAD` accurately described an earlier state but are stale for current provenance. Their source hashes remain useful only for the exact files they identify.

## 2. Relevant revisions and evidence

| Material | Identity | Status/limitation |
|---|---|---|
| Corrected PRE01 source documents | Git `0a6dc5eac7d8a5f594426f5a159913d963433ed4` | Immutable commit containing the eight amended PRE01 files; excludes unrelated untracked source |
| PRE01 v0.1 and earlier tracked repository | Git `669a7bf7072e529c04e20154587767be1090f2f8` | Immutable parent revision for B02/B03/PRE01 v0.1 |
| Master ADR v1.2 DOCX | SHA-256 `d610355ee5ca7f64c875bcf874c6fa77c976f621fd6acdbb4c5be090afa2e246` | Authorised supplied document; not a repository revision |
| PRE01 assignment | SHA-256 `e48817a312798ee0cfa80f0c23d586c18d505589b8cd946b7fd019494c9652ae` | Authorised supplied prompt |
| PRE01 close-out assignment/addendum | SHA-256 `ce266ea8de090784fa633a1b85781c785c2c47fcc7c90676d41f37aa4cae1b95` | Authorised supplied close-out requirements; not a repository revision |
| B01 specification | SHA-256 `ebc69b607dde0bf006decdc7c0bbf8312f91fee25eea6ef32841b7bb08be8727` | Untracked; cannot be claimed as part of HEAD |
| Existing G2 contracts | `nexus_g2/contracts.py` SHA-256 `9c4314ec022f5f9b86b4bf69c28f8658f8b4674759236e149c97ff77c8ed1c8c` | Untracked; source inspection only plus portable tests |
| Existing G2 controller | `nexus_g2/controller.py` SHA-256 `b2b1ae38331d108e406850a79800a7e5d38df1ebbaa9ad3b3d4145f638cd8674` | Untracked; narrow harness controller, not product investigation controller |
| Existing G2 evidence utility | `nexus_g2/evidence.py` SHA-256 `190d96cda3b0c3e5a2e5c0eaa7df80542f9edb698b0082c95d65d96b0d8cc07a` | Untracked; security-test evidence utility, not SEC-06 product repository |
| Existing G2 policy | `config/g2_policy.json` SHA-256 `90e4a16b6d822792c1123d9929e31f070e8818e3acca5199804a305f6d9c2465` | Untracked |
| G2 portable suite | `python -m unittest discover -s tests -v`: 47 passed, 0 failed in 0.297s on Python 3.12.14/Linux during PRE01 | Test-executed portable behavior only; no Windows/secure IPC/product investigation/reporting/CLOUD-EVAL verification |

The G2 `WorkerRequest`, `AuthorisationDecision`, evidence manifest and canonical JSON code demonstrate useful implementation patterns. They do not implement `InvestigationScope`, product retrieval/evidence semantics, hypothesis/planning, claim verification or ARC-08 reporting. Because the files are untracked, there is no commit that immutably identifies the tested source; file hashes above are the available local identity.

### Inspection source index

| Topic | Inspected source location |
|---|---|
| Governance, ANA, SIC and SEC | Master ADR v1.2 §§2–5 |
| Progressive investigation/controller/claim verification | Master ADR v1.2 §§8–9 and current-status §31 |
| ARC-08 canonical reporting and artifact verification | Master ADR v1.2 §24.1–24.6 |
| ARC-03 investigation/UX lifecycle | Master ADR v1.2 §25 and Table 6 |
| ARC-02 boundaries and open stack | Master ADR v1.2 §26 and Tables 7–10 |
| SEC-NET | Master ADR v1.2 §27 |
| CLOUD-EVAL authority/status | Master ADR v1.2 §29 and B01 §§1–11 |
| B03 capabilities and Path A contract | `docs/CLOUD-EVAL-B03/01_BASELINE_CAPABILITY_CATALOGUE.md` and `04_PATH_A_CONTRACT.md` at HEAD |
| B02 implementation/test assessment | `docs/CLOUD-EVAL-B02/ASSESSMENT.md`, `capability_evidence_matrix.csv`, `test_execution.json` at HEAD |
| G2 bounded contract patterns | `nexus_g2/contracts.py:12-15,22-53,100-159,182-205,207-292` |
| G2 narrow controller/replay | `nexus_g2/controller.py:10-52`; `nexus_g2/replay.py` |
| G2 evidence handling patterns | `nexus_g2/evidence.py:13-81`; `nexus_g2/contracts.py:230-292` |
| G2 executed portable assertions | `tests/test_contracts.py`, `test_controller_replay.py`, `test_evidence.py`, `test_ipc_environment.py`, `test_phase0_inspector.py`; PRE01 command recorded below |

The Master ADR source is an uploaded DOCX, so section references are more stable than transient extracted-text line numbers. Repository line references refer to the inspected untracked working-tree hashes above, not to HEAD.

## 3. Reproducibility limitations

- The corrected PRE01 commits do not contain B01 or G2 source/tests, so a clean checkout cannot reproduce the 47-test result or inspect those files.
- PRE01 v0.1 and the corrected close-out documents have commit provenance. `SHA256SUMS.txt` additionally identifies package contents but is not independent tamper resistance.
- The master ADR and assignment are uploaded inputs, not repository artifacts.
- Linux portable tests do not establish Windows PowerShell, named-pipe authentication, OS isolation, enterprise policy, live connector, Office artifact or local-model behavior.
- The origin fetch refspec does not fetch ordinary remote branches into local remote-tracking refs. `git ls-remote` is required for a read-only remote branch check until configuration is deliberately changed.
- No production/company sources, credentials or endpoint reports were accessed, which is correct but leaves those behaviors Not Tested.

## 4. Remaining safe remediation proposal

The user separately authorised publication of the corrected PRE01 documents for download. The following wider source-control work remains unauthorised and unexecuted:

1. **Classify the worktree.** Review every untracked path for source, specification, synthetic fixture, generated output, secret, credential, endpoint report and company evidence. Do not assume a filename is safe.
2. **Approve exclusions first.** Review and commit a `.gitignore` that excludes at least `evidence-output/`, `phase0-output/`, bytecode/caches and any future local evidence/database/model/output directories. Add repository checks for secret and prohibited-evidence patterns. The current `.gitignore` is itself untracked.
3. **Preserve local-only material.** Never add credentials, raw workstation Phase 0/endpoint-security reports, production records, temporary evidence, generated evidence stores, local SQLite evidence databases, model weights or classified exported reports. Retain them only in approved local locations under applicable expiry/classification.
4. **Create reviewable local commits for remaining material.** After separate source-control authority, commit reviewed G2 source/config/tests and its accurate evidence report on a suitably scoped branch, and B01 if its authority/source is accepted. Record hashes and test commands.
5. **Verify from a clean checkout.** Run the portable suite and document checks from the exact local commit. Keep Windows-specific outcomes Not Run until executed on the intended endpoint.
6. **Review diffs and history.** Confirm no generated outputs or sensitive material are staged. Obtain the required review for architectural documents and G2 changes.
7. **Push remaining material only under separate authorisation.** The PRE01 close-out publication does not authorise publishing B01, G2 or other untracked files. Confirm destination, access and content classification before any later push. Do not force-push or rewrite existing history.

## 5. Readiness judgment

The repository is ready for close-out review because B02/B03/PRE01 v0.1 and the corrected PRE01 documents have stable commit provenance and a checksum manifest. It is **not ready for reproducible WP01 implementation** until the corrected design receives architectural approval, the untracked G2/B01 state is classified and either committed or explicitly excluded, final finding-disposition authority and the necessary ARC-06/10/11 lifecycle are approved, and a clean checkout can reproduce the intended contract-test baseline. The corrected PRE01 branch was committed and pushed only after the user explicitly requested downloadable Git delivery; no history rewrite, force-push or unrelated-file publication was performed.
