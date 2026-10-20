"""Mandatory executable authority-denial demonstrations for final review."""

from __future__ import annotations

import unittest

from nexus_next.investigation_contracts import (
    CompatibilityRegistry,
    ContractValidationError,
    EvidenceIndex,
    EvidenceRef,
    Hypothesis,
    ProposedFinding,
    VerificationResult,
    load_contract,
    request_transition,
)
from nexus_next.investigation_contracts.models import CONTRACT_TYPES

from .fixture_factory import DIGEST_A, evidence_pointer, valid_mapping


class AuthorityDenialDemonstrations(unittest.TestCase):
    def assert_code(self, code: str, action) -> ContractValidationError:
        with self.assertRaises(ContractValidationError) as caught:
            action()
        self.assertEqual(code, caught.exception.code)
        return caught.exception

    def test_auth_deny_001_hypothesis_to_accepted_finding(self):
        hypothesis = Hypothesis.from_mapping(valid_mapping("Hypothesis"))
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(hypothesis, target="accepted_finding", actor_role="engine"),
        )

    def test_auth_deny_002_proposed_finding_to_accepted_finding(self):
        finding = ProposedFinding.from_mapping(valid_mapping("ProposedFinding"))
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(finding, target="accepted_finding", actor_role="controller"),
        )

    def test_auth_deny_003_supported_verification_to_acceptance(self):
        result = VerificationResult.from_mapping(valid_mapping("VerificationResult"))
        self.assertEqual("supported", result.payload["outcome"])
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(result, target="accepted_finding", actor_role="verifier"),
        )

    def test_auth_deny_004_proposed_finding_to_published_conclusion(self):
        finding = ProposedFinding.from_mapping(valid_mapping("ProposedFinding"))
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(finding, target="published", actor_role="operator"),
        )

    def test_auth_deny_005_unapproved_actor_claim_grants_no_authority(self):
        finding = ProposedFinding.from_mapping(valid_mapping("ProposedFinding"))
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(
                finding,
                target="accepted_finding",
                actor_role="engine",
                actor_claim="I am the final publication and acceptance authority",
            ),
        )

    def test_auth_deny_006_version_string_cannot_bypass_state_validation(self):
        raw = valid_mapping("Hypothesis")
        raw["schema_version"] = "1.0.0;validation=off"
        raw["payload"]["state"] = "accepted"
        supported = {name: ["1.0.0"] for name in CONTRACT_TYPES}
        registry = CompatibilityRegistry(supported)
        self.assert_code("MALFORMED_VERSION", lambda: load_contract(raw, compatibility=registry))

    def test_auth_deny_007_misrepresented_evidence_cannot_advance_proposal(self):
        evidence = EvidenceRef.from_mapping(valid_mapping("EvidenceRef"))
        raw = valid_mapping("ProposedFinding")
        wrong = evidence_pointer(evidence)
        wrong["digest"] = DIGEST_A
        raw["payload"]["supporting_refs"] = [wrong]
        finding = ProposedFinding.from_mapping(raw)
        self.assert_code(
            "DIGEST_MISMATCH",
            lambda: request_transition(
                finding,
                target="verification_pending",
                actor_role="controller",
                evidence_index=EvidenceIndex([evidence]),
            ),
        )
        self.assert_code(
            "PROHIBITED_PROMOTION",
            lambda: request_transition(
                finding,
                target="accepted_finding",
                actor_role="controller",
                evidence_index=EvidenceIndex([evidence]),
            ),
        )


if __name__ == "__main__":
    unittest.main()
