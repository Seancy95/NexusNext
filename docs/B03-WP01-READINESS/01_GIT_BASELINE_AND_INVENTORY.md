# Git Baseline and Classified Inventory

## 1. Inspected state

Inspection was read-only and performed on 2026-10-20.

| Item | Observed value |
|---|---|
| Repository | `/workspace/NexusNext` |
| Branch | `b03-pre01-closeout-review` |
| HEAD | `d15f55d69e6ceb53319aa0d489900c78bd5af895` |
| Tracked files | 31 |
| Tracked modifications before this readiness package | 0 |
| Staged files | 0 |
| Untracked, non-ignored files before this package | 28 |
| Ignored files | 39: 16 generated verification-evidence files, 6 Phase 0 output files and 17 Python bytecode files |
| Remote | `origin` points to `https://github.com/Seancy95/NexusNext.git` |

The exact post-inspection file classification is in `git_file_inventory.csv`. It records disposition, sensitivity, Git state, destination, rationale and identity for every file or an explicitly named generated group. `REQUIRES REVIEW` is not a finding that content is sensitive; it means the available inspection is insufficient to approve publication.

No WP01 product source, WP01 test, WP01 fixture or WP01 configuration file exists in the inspected repository. The only untracked executable source is the separate G2 harness and its support scripts/tests. The committed tree contains architecture and assessment documentation plus a small B02 evidence helper, not a Nexus Next product implementation.

## 2. Material classes

| File class | Observed state | Proposed disposition | Reason |
|---|---|---|---|
| `docs/B03-PRE01/**` | Tracked at HEAD | KEEP | Accepted design input and authority restrictions for WP01 |
| `docs/CLOUD-EVAL-B03/**` | Tracked at HEAD | KEEP | New-product capability and Path A design evidence; legacy is reference only |
| `docs/CLOUD-EVAL-B02/**` | Tracked at HEAD | ARCHIVE | Historical assessment evidence; not WP01 source and requires owner review before reuse |
| `deliverables/B03-PRE01-CLOSEOUT*` | Tracked at HEAD | ARCHIVE | Generated review delivery; source documents remain canonical |
| This `docs/B03-WP01-READINESS/**` package | Untracked | KEEP after approval | Preparatory design and inventory; no product implementation |
| `.gitignore` | Untracked | KEEP after review | Correctly excludes bytecode, caches and generated Phase 0/evidence directories; additional product-output exclusions must be added before implementation |
| Root G2 reports/README/traceability, `config/g2_policy.json`, `nexus_g2/**`, `inspect_environment.ps1`, G2 scripts/tests and current `pyproject.toml` | Untracked | ARCHIVE in a separately reviewed G2 baseline | They form a different bounded security harness. They are not WP01 product contracts and cannot be silently inherited. |
| Untracked B01 benchmark specification | Untracked | ARCHIVE pending document-authority review | Useful future evaluation input; benchmark execution is excluded from WP01 |
| `evidence-output/**` | Ignored/generated | EXCLUDE | Generated verification evidence; may contain execution context and is not source |
| `phase0-output/**` | Ignored/generated | EXCLUDE | Endpoint/environment evidence. Raw enterprise reports must remain local and must never be committed or uploaded. |
| `**/__pycache__/**`, `*.pyc` | Ignored/generated | GENERATED/EXCLUDE | Reproducible bytecode, not source |

No credential file was identified by filename. A broad lexical scan found security-related terms in expected source and governance documents; this is not a secret scan and cannot establish publication safety. Every untracked G2 file and generated evidence group therefore remains `REQUIRES REVIEW` until a human owner confirms data classification and provenance.

## 3. Exact proposed reproducible baseline

The first approved baseline commit should contain only:

- the 31 files already tracked at `d15f55d69e6ceb53319aa0d489900c78bd5af895`;
- the reviewed `.gitignore` with the additional exclusions listed below; and
- the eight readiness files under `docs/B03-WP01-READINESS/` listed in this package manifest.

It should not contain the untracked G2 harness, B01 draft, generated evidence, Phase 0 output, caches, credentials, raw endpoint reports, company/customer data, model files or Nexus 10.3.43 runtime code.

Before implementation, the approved baseline should add these ignore entries if the chosen product layout can create them:

```gitignore
.venv/
dist/
build/
*.egg-info/
coverage.xml
htmlcov/
.mypy_cache/
.ruff_cache/
wp01-output/
local-evidence/
*.sqlite
*.sqlite3
*.db
*.key
*.pem
.env
.env.*
```

Ignoring a path is not a security control. Pre-commit review and secret/data-classification checks remain mandatory.

## 4. Proposed implementation file set after separate approval

WP01 should be a new Nexus Next product package, separate from `nexus_g2`:

```text
config/wp01_contract_registry.json
src/nexus_next/investigation_contracts/__init__.py
src/nexus_next/investigation_contracts/models.py
src/nexus_next/investigation_contracts/validation.py
src/nexus_next/investigation_contracts/serialization.py
src/nexus_next/investigation_contracts/versioning.py
tests/wp01/test_contracts.py
tests/wp01/test_authority_boundaries.py
tests/wp01/test_serialization.py
tests/wp01/test_version_compatibility.py
tests/wp01/test_lineage.py
tests/wp01/fixtures/v1/*.json
```

The registry contains only approved schema versions, size bounds, compatibility transformations and stable failure codes; it cannot grant authority or enable a state transition. One module may hold multiple small contract types. Logical roles do not require separate processes or packages. No planner, analytical method, acceptance policy, reporting implementation, model adapter or connector belongs in this set. Packaging metadata must be designed after the untracked G2 `pyproject.toml` is separately resolved; WP01 must not overwrite or silently repurpose it.

## 5. Exact safe baseline commands after approval

These commands are a reviewable procedure, not authority to run them. Replace `<approved-archive-path>` with a protected local path outside the repository and `<approved-branch>` with the approved branch name.

```bash
cd /workspace/NexusNext
git status --short --branch --ignored
git rev-parse HEAD
test "$(git rev-parse HEAD)" = "d15f55d69e6ceb53319aa0d489900c78bd5af895"

mkdir -p <approved-archive-path>/g2-untracked
cp -a README.md FINAL_IMPLEMENTATION_REPORT.md PHASE0_DEFECT_CORRECTION_REPORT.md PHASE0_HARDENING_REPORT.md inspect_environment.ps1 requirements_traceability.md pyproject.toml config nexus_g2 scripts tests <approved-archive-path>/g2-untracked/
sha256sum README.md FINAL_IMPLEMENTATION_REPORT.md PHASE0_DEFECT_CORRECTION_REPORT.md PHASE0_HARDENING_REPORT.md inspect_environment.ps1 requirements_traceability.md pyproject.toml config/g2_policy.json nexus_g2/*.py scripts/*.py tests/*.py tests/windows/*.ps1 > <approved-archive-path>/g2-untracked/SHA256SUMS.txt
(cd <approved-archive-path>/g2-untracked && sha256sum -c SHA256SUMS.txt)

git switch -c <approved-branch> d15f55d69e6ceb53319aa0d489900c78bd5af895
git add -- .gitignore docs/B03-WP01-READINESS
git status --short
git diff --cached --name-status
git diff --cached --check
git diff --cached -- .gitignore docs/B03-WP01-READINESS
git commit -m "Establish B03-WP01 readiness baseline"
git status --short --branch
```

The copied G2 files remain in the working tree until a separately authorised move/removal is approved; the procedure intentionally avoids destructive cleanup. Do not use `git add .`. Do not push as part of baseline creation. A clean-checkout verification should be performed in a new worktree after the local commit, using only the exact commit under review.

## 6. Required approvals before baseline creation

- Repository owner approval for the branch and exact staged file list.
- Information owner review of untracked G2 reports/source and all generated evidence groups.
- Architecture owner decision on whether B01 remains a separate document lineage.
- Approval of updated ignore rules and the product package layout.
- Confirmation that no raw corporate endpoint report, operational evidence, credential or confidential company/customer data is staged.
