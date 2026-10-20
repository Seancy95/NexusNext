"""Contract-level authority denials for the bounded WP01 interface."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from .errors import fail
from .models import (
    AuthorisationDecision,
    BaseContract,
    EvidenceIndex,
    Hypothesis,
    InvestigationScope,
    ProposedFinding,
    RetrievalRequest,
    VerificationResult,
)
from .validation import timestamp

PROHIBITED_TARGETS = {
    "accepted_finding",
    "rejected_finding",
    "unresolved_finding",
    "canonical_report",
    "published",
    "artifact_validated",
}


@dataclass(frozen=True, slots=True)
class TransitionDecision:
    contract_id: str
    from_state: str
    to_state: str
    authorised_by: str
    asserted_actor_role: str
    effective_actor_role: str


def validate_retrieval_request(
    request: RetrievalRequest,
    scope: InvestigationScope,
    *,
    remaining_budget: int,
    now: datetime | None = None,
) -> None:
    """Fail closed when a proposed retrieval exceeds the admitted scope or budget."""

    now = now or datetime.now(timezone.utc)
    payload = request.payload
    scope_payload = scope.payload
    if payload["scope_id"] != scope.object_id:
        fail("SCOPE_MISMATCH", "$.payload.scope_id", "Request does not reference the admitted scope")
    if payload["source_id"] not in scope_payload["source_domains"]:
        fail("SOURCE_OUT_OF_SCOPE", "$.payload.source_id", "Source is outside the admitted scope")
    approved_fields = set(scope_payload["metrics"]) | set(scope_payload["entities"])
    if not set(payload["field_limits"]).issubset(approved_fields):
        fail("FIELD_OUT_OF_SCOPE", "$.payload.field_limits", "Field is outside the admitted scope")
    period = payload["parameters"].get("period")
    if period is not None and period not in scope_payload["periods"]:
        fail("PERIOD_OUT_OF_SCOPE", "$.payload.parameters.period", "Period is outside the admitted scope")
    if payload["worst_case_charge"] > remaining_budget:
        fail("BUDGET_EXCEEDED", "$.payload.worst_case_charge", "Request exceeds remaining budget")
    if timestamp(payload["expires_at"], "$.payload.expires_at") <= now:
        fail("REQUEST_EXPIRED", "$.payload.expires_at", "Request has expired")


def validate_authorised_binding(
    request: RetrievalRequest,
    decision: AuthorisationDecision,
    *,
    now: datetime | None = None,
) -> None:
    now = now or datetime.now(timezone.utc)
    payload = decision.payload
    if payload["decision"] != "allow":
        fail("REQUEST_DENIED", "$.payload.decision", "Denied request cannot execute")
    if (
        payload["request_id"] != request.object_id
        or payload["request_revision"] != request.revision
        or payload["request_digest"] != request.digest()
    ):
        fail("DECISION_BINDING_MISMATCH", "$.payload.request_digest", "Decision does not bind this request")
    if timestamp(payload["valid_until"], "$.payload.valid_until") <= now:
        fail("DECISION_EXPIRED", "$.payload.valid_until", "Authorisation decision has expired")


def current_state(contract: BaseContract) -> str:
    if isinstance(contract, Hypothesis):
        return str(contract.payload["state"])
    if isinstance(contract, ProposedFinding):
        return str(contract.payload["lifecycle"])
    if isinstance(contract, VerificationResult):
        return str(contract.payload["outcome"])
    return contract.schema_name


def request_transition(
    contract: BaseContract,
    *,
    target: str,
    actor_role: str,
    actor_claim: str | None = None,
    evidence_index: EvidenceIndex | None = None,
) -> TransitionDecision:
    """Validate only WP01-permitted transitions; caller claims never grant authority."""

    del actor_claim  # An untrusted declaration is never an authority source.
    source = current_state(contract)
    if target in PROHIBITED_TARGETS:
        fail("PROHIBITED_PROMOTION", "$.target", "Final finding/report transition is outside WP01")
    if isinstance(contract, Hypothesis):
        allowed = {"open", "supported", "weakened", "rejected", "revised", "unresolved"}
        if target not in allowed:
            fail("PROHIBITED_STATE", "$.target", "Hypothesis target state is invalid")
        if actor_role not in {"engine", "operator", "controller"}:
            fail("UNAUTHORISED_ACTOR", "$.actor_role", "Actor cannot revise a hypothesis")
    elif isinstance(contract, ProposedFinding):
        if target != "verification_pending":
            fail("PROHIBITED_PROMOTION", "$.target", "WP01 proposal can only await verification")
        if actor_role != "controller":
            fail("UNAUTHORISED_ACTOR", "$.actor_role", "Only controller can request verification")
        if evidence_index is None:
            fail("INVALID_EVIDENCE_REFERENCE", "$.evidence_refs", "Evidence index is required")
        evidence_index.validate_refs(
            contract.payload["supporting_refs"], expected_scope=str(contract.payload["scope_id"])
        )
    elif isinstance(contract, VerificationResult):
        fail("PROHIBITED_PROMOTION", "$.target", "Verification support is not finding disposition")
    else:
        fail("OUT_OF_SCOPE_TRANSITION", "$.target", "Contract has no WP01 transition interface")
    return TransitionDecision(
        contract_id=contract.object_id,
        from_state=source,
        to_state=target,
        authorised_by=actor_role,
        asserted_actor_role=actor_role,
        effective_actor_role=actor_role,
    )
