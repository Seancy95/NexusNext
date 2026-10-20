"""Synthetic-only fixtures for the frozen WP01 conformance matrix."""

from __future__ import annotations

import copy
from typing import Any

from nexus_next.investigation_contracts import EvidenceRef

NOW = "2030-01-01T00:00:00Z"
LATER = "2030-01-02T00:00:00Z"
DIGEST_A = "a" * 64

ROLE_BY_SCHEMA = {
    "InvestigationScope": "controller",
    "InvestigationBudget": "policy",
    "BudgetUsage": "controller",
    "RetrievalRequest": "engine",
    "AuthorisationDecision": "controller",
    "RetrievalResult": "provider",
    "EvidenceRef": "repository",
    "Hypothesis": "engine",
    "ProposedFinding": "engine",
    "VerificationRequest": "controller",
    "VerificationResult": "verifier",
    "InvestigationOutcome": "controller",
    "ContractFailure": "validator",
}


def evidence_pointer(
    evidence: EvidenceRef | None = None,
    *,
    evidence_id: str = "evidence-1",
    scope_id: str = "scope-1",
    digest: str = DIGEST_A,
    revision: int = 1,
) -> dict[str, Any]:
    if evidence is not None:
        return {
            "evidence_id": evidence.payload["evidence_id"],
            "revision": evidence.revision,
            "digest": evidence.digest(),
            "scope_id": evidence.payload["scope_id"],
        }
    return {
        "evidence_id": evidence_id,
        "revision": revision,
        "digest": digest,
        "scope_id": scope_id,
    }


def base(schema: str, payload: dict[str, Any], *, version: str = "1.0.0") -> dict[str, Any]:
    return {
        "schema_name": schema,
        "schema_version": version,
        "object_id": f"{schema.lower()}-1",
        "revision": 1,
        "created_at": NOW,
        "producer": {
            "role": ROLE_BY_SCHEMA[schema],
            "component": f"{ROLE_BY_SCHEMA[schema]}-component",
            "version": "1.0.0",
            "instance_id": f"{ROLE_BY_SCHEMA[schema]}-instance-1",
        },
        "correlation_id": "investigation-1",
        "parent_refs": [],
        "classification": "synthetic",
        "payload": payload,
    }


def valid_mapping(schema: str) -> dict[str, Any]:
    ref = evidence_pointer()
    payloads: dict[str, dict[str, Any]] = {
        "InvestigationScope": {
            "request_ref": "local:question-1",
            "objective": "Compare September with August",
            "audience": ["reviewer"],
            "entities": ["ticket_id"],
            "metrics": ["sla_attainment"],
            "populations": ["resolved_tickets"],
            "periods": ["2026-08", "2026-09"],
            "source_domains": ["synthetic-service-desk"],
            "operation_classes": ["retrieve.summary"],
            "obligations": ["show_denominator"],
            "knowledge_snapshot": "knowledge-1",
            "ambiguities": [],
            "status": "admitted",
            "policy_revision": "policy-1",
        },
        "InvestigationBudget": {
            "scope_id": "scope-1",
            "max_rounds": 3,
            "max_retrievals": 4,
            "max_evidence_bytes": 4096,
            "max_elapsed_seconds": 60,
            "max_retries": 1,
            "max_operator_interventions": 0,
            "effective_at": NOW,
            "expires_at": LATER,
            "policy_revision": "policy-1",
        },
        "BudgetUsage": {
            "budget_id": "budget-1",
            "entries": [{"action_id": "action-1", "kind": "charge", "dimension": "retrievals", "amount": 1, "timestamp": NOW}],
            "remaining": {"retrievals": 3},
            "terminal": False,
        },
        "RetrievalRequest": {
            "scope_id": "investigationscope-1",
            "budget_id": "budget-1",
            "operation": "retrieve.summary",
            "operation_version": "1.0.0",
            "source_id": "synthetic-service-desk",
            "parameters": {"period": "2026-09"},
            "field_limits": ["sla_attainment", "ticket_id"],
            "population_limit": 100,
            "byte_limit": 4096,
            "evidence_requirement": "period summary",
            "purpose": "Compare periods",
            "worst_case_charge": 1,
            "expires_at": LATER,
            "idempotency_key": "request-key-1",
        },
        "AuthorisationDecision": {
            "request_id": "retrievalrequest-1",
            "request_revision": 1,
            "request_digest": DIGEST_A,
            "scope_id": "investigationscope-1",
            "budget_id": "budget-1",
            "policy_revision": "policy-1",
            "decision": "allow",
            "constraints": ["synthetic_only"],
            "reason_code": "within_scope",
            "valid_until": LATER,
        },
        "RetrievalResult": {
            "request_id": "retrievalrequest-1",
            "decision_id": "authorisationdecision-1",
            "source_snapshot": "snapshot-1",
            "status": "success",
            "evidence_refs": [ref],
            "completeness": "complete",
            "coverage": "all synthetic rows",
            "actual_charge": 1,
            "limitations": [],
            "retry_classification": "none",
        },
        "EvidenceRef": {
            "evidence_id": "evidence-1",
            "source_id": "synthetic-service-desk",
            "snapshot_id": "snapshot-1",
            "record_locator": "summary:2026-09",
            "evidence_type": "synthetic_summary",
            "scope_id": "scope-1",
            "acquired_at": NOW,
            "expires_at": LATER,
            "digest": DIGEST_A,
            "digest_algorithm": "sha256",
            "lineage_parents": [],
            "completeness": "complete",
            "access_state": "available",
        },
        "Hypothesis": {
            "scope_id": "scope-1",
            "statement": "September attainment is lower",
            "trigger_refs": [ref],
            "predictions": ["September rate is below August"],
            "support_requirements": ["two period summaries"],
            "falsifiers": ["September rate is not below August"],
            "confounders": ["population definition change"],
            "evidence_gaps": [],
            "materiality": "medium",
            "state": "open",
            "predecessor": None,
        },
        "ProposedFinding": {
            "scope_id": "scope-1",
            "claim": "September SLA attainment was lower than August",
            "materiality": "medium",
            "claim_strength": "observation",
            "supporting_refs": [ref],
            "refuting_refs": [],
            "calculation_refs": ["calculation-1"],
            "qualifications": ["synthetic fixture only"],
            "obligations": ["show denominator"],
            "lifecycle": "proposed",
        },
        "VerificationRequest": {
            "proposal_id": "proposedfinding-1",
            "proposal_revision": 1,
            "proposal_digest": DIGEST_A,
            "required_checks": ["recalculate"],
            "evidence_refs": [ref],
            "assumptions": [],
            "contradictions": [],
            "verifier_policy": "verifier-policy-1",
            "proposer_component": "engine-component",
            "verifier_component": "verifier-component",
            "deadline": LATER,
        },
        "VerificationResult": {
            "request_id": "verificationrequest-1",
            "proposal_id": "proposedfinding-1",
            "proposal_revision": 1,
            "proposal_digest": DIGEST_A,
            "proposer_component": "engine-component",
            "checked_evidence_refs": [ref],
            "checked_calculations": ["calculation-1"],
            "contradiction_results": [],
            "assumption_results": [],
            "outcome": "supported",
            "rationale": "Synthetic values recalculate",
            "limitations": ["not a final finding disposition"],
        },
        "InvestigationOutcome": {
            "scope_id": "scope-1",
            "terminal_status": "partial",
            "terminal_reason": "bounded_fixture_complete",
            "retrieval_refs": ["retrievalresult-1"],
            "decision_refs": ["authorisationdecision-1"],
            "evidence_refs": [ref],
            "hypothesis_refs": ["hypothesis-1"],
            "proposal_refs": ["proposedfinding-1"],
            "verification_refs": ["verificationresult-1"],
            "failure_refs": [],
            "budget_usage_id": "budgetusage-1",
            "unresolved_questions": ["final disposition authority"],
            "configuration_versions": {"contract_registry": "1.0.0"},
        },
        "ContractFailure": {
            "boundary": "contract-validator",
            "related_object_id": None,
            "related_digest": None,
            "category": "validation",
            "code": "INVALID_INPUT",
            "field_path": "$.payload",
            "retryable": False,
            "policy_revision": "policy-1",
            "public_message": "Synthetic contract validation failed",
        },
    }
    return copy.deepcopy(base(schema, payloads[schema]))
