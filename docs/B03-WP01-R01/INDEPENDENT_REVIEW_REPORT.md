# B03-WP01-R01 independent review submission

## Review status

The bounded corrective implementation is ready for independent technical review. Codex performed all test execution recorded here; therefore independent verification remains **Not Verified** and WP01 is not formally closed.

Corrective source revision: `a7ab0e63a27731f806921e0c3e65ebed4fcac812` on branch `b03-wp01-r01`. The parent downloadable WP01 delivery is `543c41bedef93812ed52a150aa23e9a297d85436`.

## Confirmed defects and closure evidence

`R01-DEF-001` reproduced the acceptance of unsupported `2.0.0`, `1.1.0`, and `1.0.1` versions through both `InvestigationScope.from_mapping()` and `load_contract()`. The original transcript is preserved in `evidence/original_version_defect.txt`. At the correction revision, identical calls reject with `UNSUPPORTED_MAJOR` or `UNSUPPORTED_VERSION`; see `evidence/corrected_version_defect.txt` and `test_r01_def_001_public_loaders_reject_unsupported_versions`.

`R01-DEF-002` reproduced a direct-constructor bypass that admitted a `ProposedFinding` with a controller producer and allowed transition to `verification_pending`. The correction disables raw contract construction and requires validating factories. See the before/after constructor transcripts and `test_r01_def_002_direct_constructor_is_not_a_validation_bypass`.

The full mandatory fields, affected files, correction commit, limitations and closure assessments are in `DEFECT_CLOSURE_REGISTER.md`. Both defects are closed at the supported contract boundary by developer-executed evidence and remain pending independent verification.

## Authority-path audit

`AUTHORITY_PATH_AUDIT.csv` records initial state, requested operation, asserted actor, effective actor, decision, enforcement point, observed result and test evidence for the public construction, loading, transformation, transition, binding, evidence and outcome paths.

For `request_transition()`, the effective actor is exactly the asserted `actor_role`; the implementation performs no role mapping or defaulting, and successful decisions record both values. For contract loading, the asserted producer role is preserved as the effective role used by schema validation. Parsing and the registered compatibility transformation do not reinterpret that role. A modified role or lifecycle in a transformation fails with `SEMANTIC_LOSS`.

These controls validate contract data. They do not authenticate runtime identity, secure IPC, or prevent a malicious process from forging an otherwise structurally valid role.

## Version compatibility

Default loading supports exactly version `1.0.0`. Exact versions may additionally be accepted only through an explicit finite registry. The sole registered transform is `RetrievalRequest` `0.9.0` to `1.0.0`; it preserves producer metadata, parent references, existing payload meaning and transformation digests. There is no reverse rule. Malformed versions, unknown minor/patch versions, unsupported majors and payload-directed negotiation fail closed. Detailed results are in `VERSION_COMPATIBILITY_RESULTS.csv`.

## Canonical serialisation, evidence and lineage

The eight original serialisation cases passed. R01 additionally round-tripped an `EvidenceRef` through canonical bytes and public loading with byte-for-byte equality. Evidence reference resolution, digest, scope, availability, parent existence, cycle, expiry, classification and terminal provenance checks passed the original LIN-001 through LIN-008 cases. The evidence index remains synthetic and in memory; no durable repository or external source was tested.

## Executed tests

| Command | Passed | Failed | Skipped | Transcript |
|---|---:|---:|---:|---|
| `PYTHONPATH=src python -m unittest tests.wp01.test_frozen_matrix -v` | 68 | 0 | 0 | `evidence/frozen_68.txt` |
| `PYTHONPATH=src python -m unittest tests.wp01.test_authority_denials tests.wp01.test_registry tests.wp01.test_regressions -v` | 11 | 0 | 0 | `evidence/supporting_11.txt` |
| `PYTHONPATH=src python -m unittest tests.wp01.test_r01_regressions -v` | 12 | 0 | 0 | `evidence/r01_12.txt` |
| `PYTHONPATH=src python -m unittest discover -s tests/wp01 -t . -v` | 91 | 0 | 0 | `evidence/aggregate_91.txt` |

The 91-test aggregate is the union of the same tests and is not an additional independent population.

## Maturity and manifest

All 13 WP01 contracts remain design **Approved**, implementation **Implemented**, developer testing **Passed**, and independent verification **Not Verified**. `CONTRACT_MATURITY_REGISTER.csv` records each status independently. `SHA256SUMS.txt` binds the correction source, tests, frozen matrix and review evidence. `REQUIREMENTS_TRACEABILITY.csv` maps the R01 requirements to tests and artifacts.

## Independent reproduction

From a checkout at `a7ab0e63a27731f806921e0c3e65ebed4fcac812`, with Python 3.11 or newer:

```text
PYTHONPATH=src python -m unittest tests.wp01.test_r01_regressions -v
PYTHONPATH=src python -m unittest tests.wp01.test_frozen_matrix -v
PYTHONPATH=src python -m unittest discover -s tests/wp01 -t . -v
```

On Windows PowerShell, set `$env:PYTHONPATH = (Join-Path (Get-Location) 'src')` and replace `python` with `py -3` if required.

## Known limitations and unresolved findings

- Independent technical verification has not occurred.
- Runtime actor authentication, secure IPC and hostile-process isolation are outside WP01.
- Windows execution has not occurred; the recorded tests ran on cloud-hosted Linux with Python 3.12.14.
- Compatibility registry governance and distribution are not implemented.
- No analytical correctness, investigative competence, reporting fidelity, inference, publication, benchmark, production readiness or WP02 capability is established.

**Passing WP01 contract and conformance tests does not establish analytical correctness, investigative competence, secure IPC, Windows isolation, canonical report fidelity or production readiness.**
