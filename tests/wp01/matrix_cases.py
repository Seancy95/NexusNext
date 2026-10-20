"""Executable scenarios for every row in the frozen 68-case matrix."""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from typing import Callable
from unittest import TestCase

from nexus_next.investigation_contracts import (
    CompatibilityRegistry,
    ContractValidationError,
    EvidenceIndex,
    EvidenceRef,
    Hypothesis,
    InvestigationOutcome,
    InvestigationScope,
    ProposedFinding,
    RetrievalRequest,
    VerificationResult,
    canonical_bytes,
    decode_json,
    load_contract,
    request_transition,
    validate_authorised_binding,
    validate_outcome_completeness,
    validate_retrieval_request,
    validate_transformation_preservation,
)
from nexus_next.investigation_contracts.models import CONTRACT_TYPES

from .fixture_factory import DIGEST_A, evidence_pointer, valid_mapping


def registry(*, patch: bool = False) -> CompatibilityRegistry:
    supported = {name: ["1.0.0"] for name in CONTRACT_TYPES}
    if patch:
        supported["InvestigationScope"].append("1.0.1")
    return CompatibilityRegistry(supported)


def expect_error(test: TestCase, code: str, action: Callable[[], object]) -> ContractValidationError:
    with test.assertRaises(ContractValidationError) as caught:
        action()
    test.assertEqual(code, caught.exception.code)
    return caught.exception


def evidence_contract(**changes: object) -> EvidenceRef:
    raw = valid_mapping("EvidenceRef")
    raw["payload"].update(changes)
    return EvidenceRef.from_mapping(raw)  # type: ignore[return-value]


def actual_finding(evidence: EvidenceRef | None = None) -> ProposedFinding:
    raw = valid_mapping("ProposedFinding")
    if evidence is not None:
        raw["payload"]["supporting_refs"] = [evidence_pointer(evidence)]
        raw["payload"]["scope_id"] = evidence.payload["scope_id"]
    return ProposedFinding.from_mapping(raw)  # type: ignore[return-value]


def run_case(test: TestCase, case_id: str) -> None:
    if case_id.startswith("SER-"):
        schemas = {
            "SER-001": "InvestigationScope", "SER-002": "InvestigationBudget",
            "SER-003": "RetrievalRequest", "SER-004": "AuthorisationDecision",
            "SER-005": "EvidenceRef", "SER-006": "ProposedFinding",
            "SER-007": "VerificationResult", "SER-008": "InvestigationOutcome",
        }
        if case_id == "SER-004":
            request = RetrievalRequest.from_mapping(valid_mapping("RetrievalRequest"))
            decision_raw = valid_mapping("AuthorisationDecision")
            decision_raw["payload"]["request_id"] = request.object_id
            decision_raw["payload"]["request_revision"] = request.revision
            decision_raw["payload"]["request_digest"] = request.digest()
            decision = load_contract(decision_raw)
            validate_authorised_binding(request, decision, now=datetime(2029, 1, 1, tzinfo=timezone.utc))  # type: ignore[arg-type]
            return
        raw = valid_mapping(schemas[case_id])
        contract = load_contract(raw)
        test.assertEqual(contract.to_mapping(), load_contract(json.loads(contract.canonical_bytes())).to_mapping())
        if case_id == "SER-003":
            test.assertIsInstance(contract, RetrievalRequest)
        if case_id == "SER-006":
            test.assertEqual("proposed", contract.payload["lifecycle"])
        if case_id == "SER-007":
            test.assertEqual("supported", contract.payload["outcome"])
        return

    if case_id == "VAL-001":
        raw = valid_mapping("InvestigationScope"); del raw["schema_name"]
        expect_error(test, "REQUIRED_FIELD", lambda: load_contract(raw)); return
    if case_id == "VAL-002":
        raw = valid_mapping("InvestigationScope"); del raw["producer"]["instance_id"]
        expect_error(test, "REQUIRED_FIELD", lambda: load_contract(raw)); return
    if case_id == "VAL-003":
        expect_error(test, "INVALID_JSON", lambda: decode_json('{"schema_name":"a","schema_name":"b"}')); return
    if case_id == "VAL-004":
        expect_error(test, "NON_CANONICAL_VALUE", lambda: canonical_bytes({"value": float("nan")})); return
    if case_id == "VAL-005":
        raw = valid_mapping("InvestigationScope"); raw["payload"]["objective"] = "x" * 70_000
        expect_error(test, "SIZE_LIMIT", lambda: load_contract(raw)); return
    if case_id == "VAL-006":
        raw = valid_mapping("EvidenceRef"); raw["payload"]["expires_at"] = "2029-01-01T00:00:00Z"
        expect_error(test, "INVALID_CHRONOLOGY", lambda: load_contract(raw)); return
    if case_id == "VAL-007":
        raw = valid_mapping("InvestigationScope"); raw["object_id"] = "!" * 140
        expect_error(test, "INVALID_IDENTIFIER", lambda: load_contract(raw)); return
    if case_id == "VAL-008":
        raw = valid_mapping("Hypothesis"); raw["payload"]["state"] = "accepted"
        expect_error(test, "INVALID_ENUM", lambda: load_contract(raw)); return
    if case_id == "VAL-009":
        raw = valid_mapping("ProposedFinding")
        reversed_raw = dict(reversed(list(raw.items())))
        test.assertEqual(canonical_bytes(raw), canonical_bytes(reversed_raw)); return
    if case_id == "VAL-010":
        raw = valid_mapping("InvestigationScope"); raw["payload"]["audience"] = ["reviewer", "reviewer"]
        expect_error(test, "DUPLICATE_MEMBER", lambda: load_contract(raw)); return

    if case_id.startswith("SCP-"):
        scope = InvestigationScope.from_mapping(valid_mapping("InvestigationScope"))
        request_raw = valid_mapping("RetrievalRequest")
        if case_id == "SCP-001":
            request_raw["payload"]["source_id"] = "other-source"
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "SOURCE_OUT_OF_SCOPE", lambda: validate_retrieval_request(req, scope, remaining_budget=10, now=datetime(2029,1,1,tzinfo=timezone.utc))); return
        if case_id == "SCP-002":
            request_raw["payload"]["field_limits"] = ["secret_field"]
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "FIELD_OUT_OF_SCOPE", lambda: validate_retrieval_request(req, scope, remaining_budget=10, now=datetime(2029,1,1,tzinfo=timezone.utc))); return
        if case_id == "SCP-003":
            request_raw["payload"]["parameters"]["period"] = "2027-01"
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "PERIOD_OUT_OF_SCOPE", lambda: validate_retrieval_request(req, scope, remaining_budget=10, now=datetime(2029,1,1,tzinfo=timezone.utc))); return
        if case_id == "SCP-004":
            request_raw["payload"]["parameters"]["sql"] = "select synthetic"
            expect_error(test, "PROHIBITED_PARAMETER", lambda: load_contract(request_raw)); return
        if case_id == "SCP-005":
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "BUDGET_EXCEEDED", lambda: validate_retrieval_request(req, scope, remaining_budget=0, now=datetime(2029,1,1,tzinfo=timezone.utc))); return
        if case_id == "SCP-006":
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "REQUEST_EXPIRED", lambda: validate_retrieval_request(req, scope, remaining_budget=10, now=datetime(2031,1,1,tzinfo=timezone.utc))); return
        if case_id == "SCP-007":
            original = RetrievalRequest.from_mapping(request_raw)
            decision_raw = valid_mapping("AuthorisationDecision")
            decision_raw["payload"].update(request_id=original.object_id, request_revision=original.revision, request_digest=original.digest())
            decision = load_contract(decision_raw)
            changed = copy.deepcopy(request_raw); changed["payload"]["purpose"] = "Changed after authorisation"
            altered = RetrievalRequest.from_mapping(changed)
            expect_error(test, "DECISION_BINDING_MISMATCH", lambda: validate_authorised_binding(altered, decision, now=datetime(2029,1,1,tzinfo=timezone.utc))); return  # type: ignore[arg-type]
        if case_id == "SCP-008":
            raw = valid_mapping("RetrievalResult"); raw["payload"]["status"] = "denied"
            expect_error(test, "EVIDENCE_AFTER_DENIAL", lambda: load_contract(raw)); return

    if case_id == "LIN-001":
        evidence = evidence_contract(); index = EvidenceIndex([evidence])
        pointer = evidence_pointer(evidence); pointer["digest"] = DIGEST_A
        expect_error(test, "DIGEST_MISMATCH", lambda: index.validate_refs([pointer], expected_scope="scope-1")); return
    if case_id == "LIN-002":
        child = evidence_contract(lineage_parents=[evidence_pointer(evidence_id="missing")])
        expect_error(test, "MISSING_PARENT", lambda: EvidenceIndex([child]).validate_lineage(child)); return
    if case_id == "LIN-003":
        b = evidence_contract(evidence_id="evidence-b", lineage_parents=[evidence_pointer(evidence_id="evidence-a")])
        a = evidence_contract(evidence_id="evidence-a", lineage_parents=[evidence_pointer(b)])
        expect_error(test, "LINEAGE_CYCLE", lambda: EvidenceIndex([a, b]).validate_lineage(a)); return
    if case_id == "LIN-004":
        parent = evidence_contract(evidence_id="parent", expires_at="2030-01-01T12:00:00Z")
        child = evidence_contract(evidence_id="child", expires_at="2030-01-02T00:00:00Z", lineage_parents=[evidence_pointer(parent)])
        expect_error(test, "EXPIRY_EXTENSION", lambda: EvidenceIndex([parent, child]).validate_lineage(child)); return
    if case_id == "LIN-005":
        parent = evidence_contract(evidence_id="parent")
        raw = valid_mapping("EvidenceRef"); raw["payload"].update(evidence_id="child", lineage_parents=[evidence_pointer(parent)]); raw["classification"] = "public"
        child = EvidenceRef.from_mapping(raw)
        expect_error(test, "CLASSIFICATION_DOWNGRADE", lambda: EvidenceIndex([parent, child]).validate_lineage(child)); return
    if case_id == "LIN-006":
        evidence = evidence_contract(); pointer = evidence_pointer(evidence); pointer["scope_id"] = "scope-2"
        expect_error(test, "EVIDENCE_SCOPE_MISMATCH", lambda: EvidenceIndex([evidence]).validate_refs([pointer], expected_scope="scope-1")); return
    if case_id == "LIN-007":
        raw = valid_mapping("ProposedFinding"); del raw["producer"]["version"]
        expect_error(test, "REQUIRED_FIELD", lambda: load_contract(raw)); return
    if case_id == "LIN-008":
        outcome = InvestigationOutcome.from_mapping(valid_mapping("InvestigationOutcome"))
        expect_error(test, "INCOMPLETE_PROVENANCE", lambda: validate_outcome_completeness(outcome, known_failure_refs={"failure-1"})); return

    if case_id.startswith("AUT-"):
        if case_id == "AUT-001":
            hypothesis = Hypothesis.from_mapping(valid_mapping("Hypothesis"))
            expect_error(test, "PROHIBITED_PROMOTION", lambda: request_transition(hypothesis, target="accepted_finding", actor_role="engine")); return
        if case_id == "AUT-002":
            raw = valid_mapping("VerificationRequest"); raw["payload"]["verifier_component"] = raw["payload"]["proposer_component"]
            expect_error(test, "SELF_VERIFICATION", lambda: load_contract(raw)); return
        if case_id == "AUT-003":
            raw = valid_mapping("VerificationResult"); raw["producer"]["component"] = raw["payload"]["proposer_component"]; raw["producer"]["instance_id"] = "different-instance"
            expect_error(test, "INDEPENDENCE_FAILURE", lambda: load_contract(raw)); return
        if case_id in {"AUT-004", "AUT-005", "AUT-006"}:
            raw = valid_mapping("VerificationResult")
            raw["payload"]["outcome"] = {"AUT-004":"supported","AUT-005":"not_supported","AUT-006":"unresolved"}[case_id]
            result = VerificationResult.from_mapping(raw)
            target = {"AUT-004":"accepted_finding","AUT-005":"rejected_finding","AUT-006":"unresolved_finding"}[case_id]
            expect_error(test, "PROHIBITED_PROMOTION", lambda: request_transition(result, target=target, actor_role="verifier")); return
        if case_id == "AUT-007":
            finding = actual_finding()
            expect_error(test, "PROHIBITED_PROMOTION", lambda: request_transition(finding, target="canonical_report", actor_role="controller")); return
        if case_id == "AUT-008":
            finding = actual_finding()
            expect_error(test, "PROHIBITED_PROMOTION", lambda: request_transition(finding, target="published", actor_role="operator")); return
        if case_id == "AUT-009":
            raw = valid_mapping("InvestigationScope"); raw["revision"] = 2; raw["payload"]["source_domains"].append("new-source"); raw["producer"]["role"] = "engine"
            scope = InvestigationScope.from_mapping(valid_mapping("InvestigationScope"))
            request_raw = valid_mapping("RetrievalRequest"); request_raw["payload"]["source_id"] = "new-source"
            req = RetrievalRequest.from_mapping(request_raw)
            expect_error(test, "SOURCE_OUT_OF_SCOPE", lambda: validate_retrieval_request(req, scope, remaining_budget=10, now=datetime(2029,1,1,tzinfo=timezone.utc))); return
        if case_id == "AUT-010":
            raw = valid_mapping("BudgetUsage"); raw["payload"]["entries"].append(copy.deepcopy(raw["payload"]["entries"][0]))
            expect_error(test, "DUPLICATE_CHARGE", lambda: load_contract(raw)); return

    if case_id.startswith("VER-"):
        reg = registry()
        if case_id == "VER-001":
            test.assertIsNone(load_contract(valid_mapping("InvestigationScope"), compatibility=reg).transformation); return
        if case_id == "VER-002":
            raw = valid_mapping("RetrievalRequest"); raw["schema_version"] = "0.9.0"
            transformed = load_contract(raw, compatibility=reg)
            test.assertEqual("retrieval-request-0.9-to-1.0", transformed.transformation.transform_id); return  # type: ignore[union-attr]
        if case_id == "VER-003":
            raw = valid_mapping("RetrievalRequest"); raw["schema_version"] = "0.9.0"
            expect_error(test, "UNSUPPORTED_VERSION", lambda: reg.prepare(raw, allow_registered_transform=False)); return
        if case_id == "VER-004":
            raw = valid_mapping("InvestigationScope"); raw["schema_version"] = "1.1.0"
            expect_error(test, "UNSUPPORTED_VERSION", lambda: load_contract(raw, compatibility=reg)); return
        if case_id == "VER-005":
            original = valid_mapping("ProposedFinding"); transformed = copy.deepcopy(original); transformed["payload"]["supporting_refs"] = []
            expect_error(test, "SEMANTIC_LOSS", lambda: validate_transformation_preservation(original, transformed)); return
        if case_id == "VER-006":
            raw = valid_mapping("InvestigationScope"); raw["schema_version"] = "2.0.0"
            expect_error(test, "UNSUPPORTED_MAJOR", lambda: load_contract(raw, compatibility=reg)); return
        if case_id == "VER-007":
            raw = valid_mapping("InvestigationScope"); raw["schema_version"] = "0.9.0"; del raw["payload"]["policy_revision"]
            expect_error(test, "UNSUPPORTED_MAJOR", lambda: load_contract(raw, compatibility=reg)); return
        if case_id == "VER-008":
            original = valid_mapping("EvidenceRef"); transformed = copy.deepcopy(original); del transformed["classification"]
            expect_error(test, "SEMANTIC_LOSS", lambda: validate_transformation_preservation(original, transformed)); return
        if case_id == "VER-009":
            raw = valid_mapping("InvestigationBudget"); raw["schema_version"] = "1.1.0"; raw["payload"]["max_evidence_bytes"] = 4
            expect_error(test, "UNSUPPORTED_VERSION", lambda: load_contract(raw, compatibility=reg)); return
        if case_id == "VER-010":
            raw = valid_mapping("InvestigationScope"); raw["unknown"] = True
            expect_error(test, "UNKNOWN_FIELD", lambda: load_contract(raw)); return
        if case_id == "VER-011":
            raw = valid_mapping("RetrievalRequest"); raw["payload"]["extensions"] = {"owner_note": "synthetic"}
            test.assertIsInstance(load_contract(raw), RetrievalRequest); return
        if case_id == "VER-012":
            raw = valid_mapping("VerificationResult"); raw["payload"]["outcome"] = "probably_supported"
            expect_error(test, "INVALID_ENUM", lambda: load_contract(raw)); return
        if case_id == "VER-013":
            raw = valid_mapping("InvestigationScope"); raw["schema_version"] = "v1"
            expect_error(test, "MALFORMED_VERSION", lambda: load_contract(raw)); return
        if case_id == "VER-014":
            raw = valid_mapping("InvestigationScope"); raw["fallback_versions"] = ["1.0.0"]
            expect_error(test, "NEGOTIATION_BYPASS", lambda: load_contract(raw, compatibility=reg)); return
        if case_id == "VER-015":
            original = valid_mapping("VerificationRequest"); transformed = copy.deepcopy(original); transformed["payload"]["evidence_refs"] = []
            expect_error(test, "SEMANTIC_LOSS", lambda: validate_transformation_preservation(original, transformed)); return
        if case_id == "VER-016":
            raw = valid_mapping("InvestigationScope"); raw["schema_version"] = "1.0.1"
            test.assertEqual("1.0.1", load_contract(raw, compatibility=registry(patch=True), receiver_version="1.0.1").schema_version); return

    if case_id.startswith("SAFE-"):
        if case_id == "SAFE-001":
            secret = "password=synthetic-sentinel"
            error = expect_error(test, "INVALID_JSON", lambda: decode_json('{"bad":' + secret))
            test.assertNotIn(secret, str(error)); return
        if case_id == "SAFE-002":
            raw = valid_mapping("RetrievalResult"); raw["payload"].update(status="timeout", evidence_refs=[], completeness="none", retry_classification="retryable")
            test.assertEqual("timeout", load_contract(raw).payload["status"]); return
        if case_id == "SAFE-003":
            raw = valid_mapping("RetrievalResult"); raw["payload"].update(status="internal_failure", evidence_refs=[], completeness="none", retry_classification="not_retryable", limitations=["internal failure; correlation retained"])
            result = load_contract(raw); test.assertNotIn("Traceback", result.canonical_bytes().decode()); return
        if case_id == "SAFE-004":
            expect_error(test, "NON_CANONICAL_VALUE", lambda: canonical_bytes({"bad": object()})); return
        if case_id == "SAFE-005":
            raw = valid_mapping("InvestigationOutcome"); raw["payload"].update(terminal_status="budget_exhausted", terminal_reason="budget_exhausted", proposal_refs=[], verification_refs=[], unresolved_questions=["evidence unavailable"])
            outcome = load_contract(raw); test.assertEqual("budget_exhausted", outcome.payload["terminal_status"]); return
        if case_id == "SAFE-006":
            raw = valid_mapping("VerificationResult"); raw["payload"].update(outcome="unresolved", rationale="Required evidence expired", limitations=["evidence expired"])
            test.assertEqual("unresolved", load_contract(raw).payload["outcome"]); return
        if case_id == "SAFE-007":
            codes = []
            for _ in range(25):
                try: decode_json('{"broken":')
                except ContractValidationError as exc: codes.append(exc.code)
            test.assertEqual(["INVALID_JSON"] * 25, codes); return
        if case_id == "SAFE-008":
            raw = valid_mapping("InvestigationScope"); raw["validation_policy"] = "disabled"
            expect_error(test, "UNKNOWN_FIELD", lambda: load_contract(raw)); return

    test.fail(f"No executable scenario for frozen case {case_id}")
