# Mandatory defect closure register

## R01-DEF-001 — unsupported contract versions accepted by public loaders

1. **Description:** `BaseContract.from_mapping()` parsed semantic versions but did not require an explicitly supported version when no `CompatibilityRegistry` was supplied. `load_contract()` delegated to that path.
2. **Original observed behaviour:** At parent revision `543c41bedef93812ed52a150aa23e9a297d85436`, both `InvestigationScope.from_mapping()` and `load_contract()` accepted synthetic `2.0.0`, `1.1.0`, and `1.0.1` inputs. See `evidence/original_version_defect.txt` (SHA-256 `769590d83f847e8c60ff8fe084e111ef0fc4040e96f4da934ec29a236a016de6`).
3. **Required behaviour:** Default public loading accepts only approved `1.0.0`. Every other version fails unless an explicit registry supports the exact receiver version or a registered transformation applies.
4. **Corrected observed behaviour:** The same six calls reject `2.0.0` with `UNSUPPORTED_MAJOR` and `1.1.0`/`1.0.1` with `UNSUPPORTED_VERSION`. The registered `RetrievalRequest` `0.9.0` to `1.0.0` transformation remains available and now performs preservation validation. See `evidence/corrected_version_defect.txt`.
5. **Regression proof:** `R01DefectClosureTests.test_r01_def_001_public_loaders_reject_unsupported_versions`; companion tests cover all 13 model factories, supported exact versions, registered older-to-newer conversion, newer-to-older rejection, malformed identifiers, unknown fields/enumerations, and missing fields.
6. **Command and result:** `PYTHONPATH=src python -m unittest tests.wp01.test_r01_regressions -v` — 12 passed, 0 failed, 0 skipped.
7. **Affected files:** `src/nexus_next/investigation_contracts/models.py`, `src/nexus_next/investigation_contracts/versioning.py`, `tests/wp01/test_r01_regressions.py`.
8. **Correction commit:** `a7ab0e63a27731f806921e0c3e65ebed4fcac812`.
9. **Limitations:** Compatibility is a finite in-process registry. Registry governance, distribution and authenticated runtime component identity remain outside WP01. Only the registered synthetic `RetrievalRequest` transformation is implemented.

**Closure assessment:** Closed at the implemented contract boundary. Closure is supported by before/after reproduction through the same public interfaces and passing regressions; it remains pending independent verification.

## R01-DEF-002 — direct dataclass construction bypassed contract validation

1. **Description:** Public dataclass constructors allowed callers to instantiate a contract without `from_mapping()` validation.
2. **Original observed behaviour:** A synthetic `ProposedFinding` whose producer asserted `controller` bypassed the approved engine/operator producer rule and was permitted to enter `verification_pending` through `request_transition()`. See `evidence/original_constructor_bypass.txt` (SHA-256 `bf990d5d78857af09d8ead39afd15a2a2f78ffd4e2ef9ec8d0928a45986f8d1a`).
3. **Required behaviour:** Contract objects must be created by a validating public loader; an invalid producer must fail with `UNAUTHORISED_ACTOR` and raw constructors must not admit contracts.
4. **Corrected observed behaviour:** Direct construction raises `TypeError`; `ProposedFinding.from_mapping()` rejects the same mapping with `UNAUTHORISED_ACTOR`.
5. **Regression proof:** `R01DefectClosureTests.test_r01_def_002_direct_constructor_is_not_a_validation_bypass`.
6. **Command and result:** `PYTHONPATH=src python -m unittest tests.wp01.test_r01_regressions -v` — 12 passed, 0 failed, 0 skipped.
7. **Affected files:** `src/nexus_next/investigation_contracts/models.py`, `tests/wp01/test_r01_regressions.py`.
8. **Correction commit:** `a7ab0e63a27731f806921e0c3e65ebed4fcac812`.
9. **Limitations:** This is contract-level Python API enforcement. It is not secure process isolation and does not authenticate a caller that supplies an otherwise valid role.

**Closure assessment:** Closed at the supported construction interfaces; pending independent verification.
