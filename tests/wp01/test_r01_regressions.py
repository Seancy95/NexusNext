"""B03-WP01-R01 defect-closure and authority-path regressions."""

from __future__ import annotations

import copy
import json
import unittest

from nexus_next.investigation_contracts import (
    CompatibilityRegistry,
    ContractValidationError,
    EvidenceIndex,
    EvidenceRef,
    Hypothesis,
    InvestigationScope,
    ProposedFinding,
    RetrievalRequest,
    canonical_bytes,
    load_contract,
    request_transition,
    validate_transformation_preservation,
)
from nexus_next.investigation_contracts.models import CONTRACT_TYPES

from .fixture_factory import evidence_pointer, valid_mapping


def registry(*, patch: bool = False) -> CompatibilityRegistry:
    versions = ["1.0.0", "1.0.1"] if patch else ["1.0.0"]
    return CompatibilityRegistry({name: versions for name in CONTRACT_TYPES})


class R01DefectClosureTests(unittest.TestCase):
    def assert_code(self, code: str, action) -> ContractValidationError:
        with self.assertRaises(ContractValidationError) as caught:
            action()
        self.assertEqual(code, caught.exception.code)
        return caught.exception

    def test_r01_def_001_public_loaders_reject_unsupported_versions(self):
        loaders = (
            ("InvestigationScope.from_mapping", InvestigationScope.from_mapping),
            ("load_contract", load_contract),
        )
        for loader_name, loader in loaders:
            for version, code in (
                ("2.0.0", "UNSUPPORTED_MAJOR"),
                ("1.1.0", "UNSUPPORTED_VERSION"),
                ("1.0.1", "UNSUPPORTED_VERSION"),
            ):
                with self.subTest(loader=loader_name, version=version):
                    raw = valid_mapping("InvestigationScope")
                    raw["schema_version"] = version
                    self.assert_code(code, lambda raw=raw, loader=loader: loader(raw))

    def test_r01_def_001_every_model_factory_rejects_unknown_patch(self):
        for schema_name, contract_type in CONTRACT_TYPES.items():
            with self.subTest(schema=schema_name):
                raw = valid_mapping(schema_name)
                raw["schema_version"] = "1.0.1"
                self.assert_code("UNSUPPORTED_VERSION", lambda: contract_type.from_mapping(raw))

    def test_r01_def_001_supported_default_and_registered_patch(self):
        default = load_contract(valid_mapping("InvestigationScope"))
        self.assertEqual("1.0.0", default.schema_version)
        patch = valid_mapping("InvestigationScope")
        patch["schema_version"] = "1.0.1"
        loaded = load_contract(patch, compatibility=registry(patch=True), receiver_version="1.0.1")
        self.assertEqual("1.0.1", loaded.schema_version)

    def test_r01_def_001_registered_older_to_newer_transform_only(self):
        older = valid_mapping("RetrievalRequest")
        older["schema_version"] = "0.9.0"
        transformed = load_contract(older, compatibility=registry())
        self.assertEqual("1.0.0", transformed.schema_version)
        self.assertEqual("retrieval-request-0.9-to-1.0", transformed.transformation.transform_id)
        newer = valid_mapping("RetrievalRequest")
        self.assert_code(
            "UNSUPPORTED_MAJOR",
            lambda: load_contract(newer, compatibility=registry(), receiver_version="0.9.0"),
        )

    def test_r01_def_001_malformed_unknown_and_missing_fields_remain_closed(self):
        malformed = valid_mapping("InvestigationScope")
        malformed["schema_version"] = "1.x"
        self.assert_code("MALFORMED_VERSION", lambda: load_contract(malformed))
        unknown = valid_mapping("InvestigationScope")
        unknown["new_field"] = True
        self.assert_code("UNKNOWN_FIELD", lambda: load_contract(unknown))
        missing = valid_mapping("InvestigationScope")
        del missing["payload"]["policy_revision"]
        self.assert_code("REQUIRED_FIELD", lambda: load_contract(missing))
        altered = valid_mapping("VerificationResult")
        altered["payload"]["outcome"] = "accepted"
        self.assert_code("INVALID_ENUM", lambda: load_contract(altered))

    def test_r01_def_002_direct_constructor_is_not_a_validation_bypass(self):
        raw = valid_mapping("ProposedFinding")
        raw["producer"]["role"] = "controller"
        with self.assertRaises(TypeError):
            ProposedFinding(**raw)
        with self.assertRaises(TypeError):
            ProposedFinding()
        self.assert_code("UNAUTHORISED_ACTOR", lambda: ProposedFinding.from_mapping(raw))

    def test_r01_transform_preserves_actor_metadata_and_payload_meaning(self):
        raw = valid_mapping("RetrievalRequest")
        raw["schema_version"] = "0.9.0"
        loaded = load_contract(raw, compatibility=registry())
        self.assertEqual(raw["producer"], dict(loaded.producer))
        self.assertEqual(raw["parent_refs"], list(loaded.parent_refs))
        for key, value in raw["payload"].items():
            self.assertEqual(value, loaded.to_mapping()["payload"][key])

    def test_r01_transform_cannot_elevate_role_or_change_lifecycle(self):
        original = valid_mapping("ProposedFinding")
        elevated = copy.deepcopy(original)
        elevated["producer"]["role"] = "controller"
        self.assert_code(
            "SEMANTIC_LOSS",
            lambda: validate_transformation_preservation(original, elevated),
        )
        relabelled = copy.deepcopy(original)
        relabelled["payload"]["lifecycle"] = "verification_pending"
        self.assert_code(
            "SEMANTIC_LOSS",
            lambda: validate_transformation_preservation(original, relabelled),
        )

    def test_r01_asserted_role_is_the_effective_role_without_reinterpretation(self):
        hypothesis = Hypothesis.from_mapping(valid_mapping("Hypothesis"))
        decision = request_transition(hypothesis, target="supported", actor_role="engine")
        self.assertEqual("engine", decision.asserted_actor_role)
        self.assertEqual("engine", decision.effective_actor_role)
        self.assertEqual("engine", decision.authorised_by)
        self.assert_code(
            "UNAUTHORISED_ACTOR",
            lambda: request_transition(hypothesis, target="rejected", actor_role="verifier"),
        )

    def test_r01_parsing_and_transform_do_not_reinterpret_producer_role(self):
        finding = load_contract(json.loads(canonical_bytes(valid_mapping("ProposedFinding"))))
        self.assertEqual("engine", finding.producer["role"])
        raw = valid_mapping("RetrievalRequest")
        raw["schema_version"] = "0.9.0"
        transformed = RetrievalRequest.from_mapping(raw, compatibility=registry())
        self.assertEqual(raw["producer"]["role"], transformed.producer["role"])

    def test_r01_provisional_hypothesis_states_cannot_promote_findings_or_reports(self):
        for state in ("supported", "rejected", "unresolved"):
            raw = valid_mapping("Hypothesis")
            raw["payload"]["state"] = state
            hypothesis = Hypothesis.from_mapping(raw)
            for target in ("accepted_finding", "canonical_report", "published"):
                with self.subTest(state=state, target=target):
                    self.assert_code(
                        "PROHIBITED_PROMOTION",
                        lambda target=target: request_transition(
                            hypothesis, target=target, actor_role="controller"
                        ),
                    )

    def test_r01_evidence_reference_and_canonical_round_trip(self):
        evidence = EvidenceRef.from_mapping(valid_mapping("EvidenceRef"))
        EvidenceIndex([evidence]).validate_refs(
            [evidence_pointer(evidence)], expected_scope=str(evidence.payload["scope_id"])
        )
        restored = load_contract(json.loads(evidence.canonical_bytes()))
        self.assertEqual(evidence.canonical_bytes(), restored.canonical_bytes())


if __name__ == "__main__":
    unittest.main()
