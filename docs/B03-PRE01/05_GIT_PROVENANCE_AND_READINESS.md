# Git Provenance and Repository Readiness

## 1. Actual inspected state

Inspection date: 2026-10-15 UTC.

| Item | Observed state |
|---|---|
| Repository | `/workspace/NexusNext` |
| Current branch | `cloud-eval-b03-design` |
| HEAD | `b08d24fd9376f0537c370c0ed7af0f320b8669c5` — `Add CLOUD-EVAL-B03 baseline architecture design` |
| Parent | `1e40277c7623c684522ecefe665d42a78a23715e` — `Add CLOUD-EVAL-B02 baseline assessment` |
| Remote | `origin` = `https://github.com/Seancy95/NexusNext.git` for fetch/push |
| Remote B03 branch | Read-only inspection previously confirmed `cloud-eval-b03-design` at `b08d24f…` |
| Local upstream | No remote-tracking ref is materialised for the current branch; the configured fetch refspec maps only remote `HEAD` |
| Tracked content | B02 evidence/assessment package and B03 design package |
| Existing untracked content | `.gitignore`, root reports/README, `config/`, B01, `inspect_environment.ps1`, `nexus_g2/`, `pyproject.toml`, root traceability, `scripts/`, `tests/` |
| PRE01 content | `docs/B03-PRE01/`; created locally and deliberately untracked under this assignment |
| Worktree conclusion | Repository has a valid HEAD and is no longer unborn. Product/G2 source still lacks commit identity because it is untracked. |

The older reports that say branch `work`, unborn branch or no `HEAD` accurately described an earlier state but are stale for current provenance. Their source hashes remain useful only for the exact files they identify.

## 2. Relevant revisions and evidence

| Material | Identity | Status/limitation |
|---|---|---|
| Current tracked repository | Git `b08d24fd9376f0537c370c0ed7af0f320b8669c5` | Immutable commit for B02/B03 tracked files only |
| Master ADR v1.2 DOCX | SHA-256 `d610355ee5ca7f64c875bcf874c6fa77c976f621fd6acdbb4c5be090afa2e246` | Authorised supplied document; not a repository revision |
| PRE01 assignment | SHA-256 `e48817a312798ee0cfa80f0c23d586c18d505589b8cd946b7fd019494c9652ae` | Authorised supplied prompt |
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

- The current commit does not contain B01 or G2 source/tests, so a clean checkout of `b08d24f…` cannot reproduce the 47-test result or inspect those files.
- PRE01 files are intentionally uncommitted; `SHA256SUMS.txt` identifies them locally but is not Git provenance or independent tamper resistance.
- The master ADR and assignment are uploaded inputs, not repository artifacts.
- Linux portable tests do not establish Windows PowerShell, named-pipe authentication, OS isolation, enterprise policy, live connector, Office artifact or local-model behavior.
- The origin fetch refspec does not fetch ordinary remote branches into local remote-tracking refs. `git ls-remote` is required for a read-only remote branch check until configuration is deliberately changed.
- No production/company sources, credentials or endpoint reports were accessed, which is correct but leaves those behaviors Not Tested.

## 4. Safe remediation proposal — not executed

The following requires a separate source-control instruction:

1. **Classify the worktree.** Review every untracked path for source, specification, synthetic fixture, generated output, secret, credential, endpoint report and company evidence. Do not assume a filename is safe.
2. **Approve exclusions first.** Review and commit a `.gitignore` that excludes at least `evidence-output/`, `phase0-output/`, bytecode/caches and any future local evidence/database/model/output directories. Add repository checks for secret and prohibited-evidence patterns. The current `.gitignore` is itself untracked.
3. **Preserve local-only material.** Never add credentials, raw workstation Phase 0/endpoint-security reports, production records, temporary evidence, generated evidence stores, local SQLite evidence databases, model weights or classified exported reports. Retain them only in approved local locations under applicable expiry/classification.
4. **Create reviewable local commits.** On a named feature branch, separately commit: (a) reviewed G2 source/config/tests and its accurate evidence report; (b) B01 if its authority/source is accepted; (c) PRE01 design. Record hashes and test commands. A local commit creates provenance but does not publish anything.
5. **Verify from a clean checkout.** Run the portable suite and document checks from the exact local commit. Keep Windows-specific outcomes Not Run until executed on the intended endpoint.
6. **Review diffs and history.** Confirm no generated outputs or sensitive material are staged. Obtain the required review for architectural documents and G2 changes.
7. **Push only under separate authorisation.** A remote push publishes commits to the configured GitHub repository and is distinct from creating local commits. Confirm destination, access and content classification before pushing. Do not force-push or rewrite the existing B02/B03 history.

## 5. Readiness judgment

The repository is ready for local design review because B02/B03 have stable commit provenance and PRE01 has a local checksum manifest. It is **not ready for reproducible WP01 implementation** until the untracked G2/B01 state is classified and either committed or explicitly excluded, the ARC-06/10/11 provisional lifecycle is approved, and a clean checkout can reproduce the intended contract-test baseline. No repository change, commit, push, remote edit or permission change was performed by PRE01.
