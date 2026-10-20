"""Versioned foundational investigation contracts for B03-WP01."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar

from .errors import ContractValidationError, fail
from .serialization import canonical_bytes
from .validation import (
    deep_freeze,
    digest,
    enum,
    exact_keys,
    identifier,
    integer,
    mapping,
    sequence,
    string_set,
    text,
    thaw,
    timestamp,
)
from .versioning import CompatibilityRegistry, TransformationRecord, Version

COMMON_REQUIRED = {
    "schema_name", "schema_version", "object_id", "revision", "created_at",
    "producer", "correlation_id", "parent_refs", "classification", "payload",
}
PRODUCER_REQUIRED = {"role", "component", "version", "instance_id"}
PARENT_REQUIRED = {"schema_name", "object_id", "revision", "digest"}
PRODUCER_ROLES = {
    "engine", "controller", "verifier", "provider", "repository", "operator", "policy", "validator",
}


def _validate_producer(value: Any) -> None:
    producer = mapping(value, "$.producer")
    exact_keys(producer, PRODUCER_REQUIRED, set(), "$.producer")
    enum(producer["role"], PRODUCER_ROLES, "$.producer.role")
    identifier(producer["component"], "$.producer.component")
    text(producer["version"], "$.producer.version", max_chars=64)
    identifier(producer["instance_id"], "$.producer.instance_id")


def _validate_parent_refs(value: Any) -> None:
    parents = sequence(value, "$.parent_refs")
    seen: set[tuple[str, str, int]] = set()
    for index, raw in enumerate(parents):
        path = f"$.parent_refs[{index}]"
        parent = mapping(raw, path)
        exact_keys(parent, PARENT_REQUIRED, set(), path)
        schema = text(parent["schema_name"], f"{path}.schema_name", max_chars=64)
        object_id = identifier(parent["object_id"], f"{path}.object_id")
        revision = integer(parent["revision"], f"{path}.revision", minimum=1)
        digest(parent["digest"], f"{path}.digest")
        key = (schema, object_id, revision)
        if key in seen:
            fail("DUPLICATE_MEMBER", path, "Duplicate parent reference")
        seen.add(key)


def _validate_ref_list(value: Any, path: str, *, min_items: int = 0) -> None:
    refs = sequence(value, path, min_items=min_items)
    seen: set[tuple[str, int]] = set()
    for index, raw in enumerate(refs):
        item_path = f"{path}[{index}]"
        ref = mapping(raw, item_path)
        exact_keys(ref, {"evidence_id", "revision", "digest", "scope_id"}, set(), item_path)
        key = (
            identifier(ref["evidence_id"], f"{item_path}.evidence_id"),
            integer(ref["revision"], f"{item_path}.revision", minimum=1),
        )
        digest(ref["digest"], f"{item_path}.digest")
        identifier(ref["scope_id"], f"{item_path}.scope_id")
        if key in seen:
            fail("DUPLICATE_MEMBER", item_path, "Duplicate evidence reference")
        seen.add(key)


@dataclass(frozen=True, slots=True)
class BaseContract:
    schema_name: str
    schema_version: str
    object_id: str
    revision: int
    created_at: str
    producer: Mapping[str, Any]
    correlation_id: str
    parent_refs: tuple[Any, ...]
    classification: str
    payload: Mapping[str, Any]
    transformation: TransformationRecord | None = None

    SCHEMA_NAME: ClassVar[str] = "BaseContract"
    PAYLOAD_REQUIRED: ClassVar[set[str]] = set()
    PAYLOAD_OPTIONAL: ClassVar[set[str]] = set()

    @classmethod
    def from_mapping(
        cls,
        raw: Mapping[str, Any],
        *,
        compatibility: CompatibilityRegistry | None = None,
        receiver_version: str = "1.0.0",
    ) -> "BaseContract":
        prepared = dict(raw)
        transformation = None
        if compatibility is not None:
            prepared, transformation = compatibility.prepare(
                raw, receiver_version=receiver_version
            )
        canonical_bytes(prepared)
        exact_keys(prepared, COMMON_REQUIRED, set(), "$")
        if prepared["schema_name"] != cls.SCHEMA_NAME:
            fail("SCHEMA_MISMATCH", "$.schema_name", "Schema does not match contract type")
        Version.parse(prepared["schema_version"])
        identifier(prepared["object_id"], "$.object_id")
        integer(prepared["revision"], "$.revision", minimum=1)
        timestamp(prepared["created_at"], "$.created_at")
        _validate_producer(prepared["producer"])
        identifier(prepared["correlation_id"], "$.correlation_id")
        _validate_parent_refs(prepared["parent_refs"])
        text(prepared["classification"], "$.classification", max_chars=128)
        payload = mapping(prepared["payload"], "$.payload")
        exact_keys(payload, cls.PAYLOAD_REQUIRED, cls.PAYLOAD_OPTIONAL, "$.payload")
        cls._validate_payload(payload, prepared)
        return cls(
            schema_name=prepared["schema_name"],
            schema_version=prepared["schema_version"],
            object_id=prepared["object_id"],
            revision=prepared["revision"],
            created_at=prepared["created_at"],
            producer=deep_freeze(prepared["producer"]),
            correlation_id=prepared["correlation_id"],
            parent_refs=deep_freeze(prepared["parent_refs"]),
            classification=prepared["classification"],
            payload=deep_freeze(payload),
            transformation=transformation,
        )

    @classmethod
    def _validate_payload(cls, payload: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        del payload, raw

    def to_mapping(self) -> dict[str, Any]:
        return {
            "schema_name": self.schema_name,
            "schema_version": self.schema_version,
            "object_id": self.object_id,
            "revision": self.revision,
            "created_at": self.created_at,
            "producer": thaw(self.producer),
            "correlation_id": self.correlation_id,
            "parent_refs": thaw(self.parent_refs),
            "classification": self.classification,
            "payload": thaw(self.payload),
        }

    def canonical_bytes(self) -> bytes:
        return canonical_bytes(self.to_mapping())

    def digest(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()


class InvestigationScope(BaseContract):
    SCHEMA_NAME = "InvestigationScope"
    PAYLOAD_REQUIRED = {
        "request_ref", "objective", "audience", "entities", "metrics", "populations",
        "periods", "source_domains", "operation_classes", "obligations", "knowledge_snapshot",
        "ambiguities", "status", "policy_revision",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        text(p["request_ref"], "$.payload.request_ref")
        text(p["objective"], "$.payload.objective")
        string_set(p["audience"], "$.payload.audience", min_items=1)
        string_set(p["entities"], "$.payload.entities")
        string_set(p["metrics"], "$.payload.metrics", min_items=1)
        string_set(p["populations"], "$.payload.populations", min_items=1)
        string_set(p["periods"], "$.payload.periods", min_items=1)
        string_set(p["source_domains"], "$.payload.source_domains", min_items=1)
        string_set(p["operation_classes"], "$.payload.operation_classes", min_items=1)
        string_set(p["obligations"], "$.payload.obligations")
        identifier(p["knowledge_snapshot"], "$.payload.knowledge_snapshot")
        string_set(p["ambiguities"], "$.payload.ambiguities")
        enum(p["status"], {"admitted", "clarification_required", "blocked"}, "$.payload.status")
        identifier(p["policy_revision"], "$.payload.policy_revision")


class InvestigationBudget(BaseContract):
    SCHEMA_NAME = "InvestigationBudget"
    PAYLOAD_REQUIRED = {
        "scope_id", "max_rounds", "max_retrievals", "max_evidence_bytes", "max_elapsed_seconds",
        "max_retries", "max_operator_interventions", "effective_at", "expires_at", "policy_revision",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["scope_id"], "$.payload.scope_id")
        for field in ("max_rounds", "max_retrievals", "max_evidence_bytes", "max_elapsed_seconds", "max_retries", "max_operator_interventions"):
            integer(p[field], f"$.payload.{field}")
        if timestamp(p["expires_at"], "$.payload.expires_at") <= timestamp(p["effective_at"], "$.payload.effective_at"):
            fail("INVALID_CHRONOLOGY", "$.payload.expires_at", "Budget expiry must follow effective time")
        identifier(p["policy_revision"], "$.payload.policy_revision")


class BudgetUsage(BaseContract):
    SCHEMA_NAME = "BudgetUsage"
    PAYLOAD_REQUIRED = {"budget_id", "entries", "remaining", "terminal"}

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["budget_id"], "$.payload.budget_id")
        entries = sequence(p["entries"], "$.payload.entries")
        seen: set[str] = set()
        for index, item in enumerate(entries):
            path = f"$.payload.entries[{index}]"
            entry = mapping(item, path)
            exact_keys(entry, {"action_id", "kind", "dimension", "amount", "timestamp"}, set(), path)
            action = identifier(entry["action_id"], f"{path}.action_id")
            enum(entry["kind"], {"reserve", "charge", "release"}, f"{path}.kind")
            text(entry["dimension"], f"{path}.dimension", max_chars=64)
            integer(entry["amount"], f"{path}.amount", minimum=1)
            timestamp(entry["timestamp"], f"{path}.timestamp")
            if entry["kind"] == "charge" and action in seen:
                fail("DUPLICATE_CHARGE", path, "Action has already been charged")
            if entry["kind"] == "charge":
                seen.add(action)
        remaining = mapping(p["remaining"], "$.payload.remaining")
        for key, value in remaining.items():
            text(key, "$.payload.remaining", max_chars=64)
            integer(value, f"$.payload.remaining.{key}")
        if not isinstance(p["terminal"], bool):
            fail("INVALID_TYPE", "$.payload.terminal", "Terminal must be Boolean")


class RetrievalRequest(BaseContract):
    SCHEMA_NAME = "RetrievalRequest"
    PAYLOAD_REQUIRED = {
        "scope_id", "budget_id", "operation", "operation_version", "source_id", "parameters",
        "field_limits", "population_limit", "byte_limit", "evidence_requirement", "purpose",
        "worst_case_charge", "expires_at", "idempotency_key",
    }
    PAYLOAD_OPTIONAL = {"extensions"}

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        for field in ("scope_id", "budget_id", "source_id", "idempotency_key"):
            identifier(p[field], f"$.payload.{field}")
        operation = identifier(p["operation"], "$.payload.operation")
        Version.parse(p["operation_version"])
        params = mapping(p["parameters"], "$.payload.parameters")
        prohibited = {"sql", "url", "expression", "code"} & set(params)
        if prohibited or operation.startswith(("sql.", "url.", "exec.")):
            fail("PROHIBITED_PARAMETER", "$.payload.parameters", "Executable or free-form retrieval input is prohibited")
        string_set(p["field_limits"], "$.payload.field_limits", min_items=1)
        integer(p["population_limit"], "$.payload.population_limit", minimum=1)
        integer(p["byte_limit"], "$.payload.byte_limit", minimum=1)
        text(p["evidence_requirement"], "$.payload.evidence_requirement")
        text(p["purpose"], "$.payload.purpose")
        integer(p["worst_case_charge"], "$.payload.worst_case_charge", minimum=1)
        timestamp(p["expires_at"], "$.payload.expires_at")
        if "extensions" in p:
            ext = mapping(p["extensions"], "$.payload.extensions")
            if any(key in ext for key in ("authority", "state", "evidence", "classification")):
                fail("PROHIBITED_EXTENSION", "$.payload.extensions", "Extension cannot alter governed semantics")


class AuthorisationDecision(BaseContract):
    SCHEMA_NAME = "AuthorisationDecision"
    PAYLOAD_REQUIRED = {
        "request_id", "request_revision", "request_digest", "scope_id", "budget_id", "policy_revision",
        "decision", "constraints", "reason_code", "valid_until",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        for field in ("request_id", "scope_id", "budget_id", "policy_revision", "reason_code"):
            identifier(p[field], f"$.payload.{field}")
        integer(p["request_revision"], "$.payload.request_revision", minimum=1)
        digest(p["request_digest"], "$.payload.request_digest")
        enum(p["decision"], {"allow", "deny"}, "$.payload.decision")
        string_set(p["constraints"], "$.payload.constraints")
        timestamp(p["valid_until"], "$.payload.valid_until")
        if raw["producer"]["role"] != "controller":
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only the controller can issue retrieval decisions")


class RetrievalResult(BaseContract):
    SCHEMA_NAME = "RetrievalResult"
    PAYLOAD_REQUIRED = {
        "request_id", "decision_id", "source_snapshot", "status", "evidence_refs", "completeness",
        "coverage", "actual_charge", "limitations", "retry_classification",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        for field in ("request_id", "decision_id", "source_snapshot"):
            identifier(p[field], f"$.payload.{field}")
        status = enum(p["status"], {"success", "partial", "denied", "unavailable", "timeout", "integrity_failure", "internal_failure", "budget_denied"}, "$.payload.status")
        _validate_ref_list(p["evidence_refs"], "$.payload.evidence_refs")
        text(p["completeness"], "$.payload.completeness", max_chars=128)
        text(p["coverage"], "$.payload.coverage", max_chars=256)
        integer(p["actual_charge"], "$.payload.actual_charge")
        string_set(p["limitations"], "$.payload.limitations")
        enum(p["retry_classification"], {"none", "retryable", "not_retryable"}, "$.payload.retry_classification")
        if status in {"denied", "budget_denied"} and p["evidence_refs"]:
            fail("EVIDENCE_AFTER_DENIAL", "$.payload.evidence_refs", "Denied retrieval cannot emit evidence")
        if status == "success" and not p["evidence_refs"] and p["completeness"] != "authoritative_empty":
            fail("MISSING_EVIDENCE", "$.payload.evidence_refs", "Successful retrieval requires evidence")


class EvidenceRef(BaseContract):
    SCHEMA_NAME = "EvidenceRef"
    PAYLOAD_REQUIRED = {
        "evidence_id", "source_id", "snapshot_id", "record_locator", "evidence_type", "scope_id",
        "acquired_at", "expires_at", "digest", "digest_algorithm", "lineage_parents", "completeness", "access_state",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        for field in ("evidence_id", "source_id", "snapshot_id", "scope_id"):
            identifier(p[field], f"$.payload.{field}")
        text(p["record_locator"], "$.payload.record_locator")
        text(p["evidence_type"], "$.payload.evidence_type", max_chars=128)
        acquired = timestamp(p["acquired_at"], "$.payload.acquired_at")
        expires = timestamp(p["expires_at"], "$.payload.expires_at")
        if expires <= acquired:
            fail("INVALID_CHRONOLOGY", "$.payload.expires_at", "Evidence expiry must follow acquisition")
        digest(p["digest"], "$.payload.digest")
        enum(p["digest_algorithm"], {"sha256"}, "$.payload.digest_algorithm")
        _validate_ref_list(p["lineage_parents"], "$.payload.lineage_parents")
        enum(p["completeness"], {"complete", "partial"}, "$.payload.completeness")
        enum(p["access_state"], {"available", "partial", "expired", "inaccessible", "contradicted", "invalid"}, "$.payload.access_state")
        if raw["producer"]["role"] != "repository":
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only the evidence repository can issue evidence references")


class Hypothesis(BaseContract):
    SCHEMA_NAME = "Hypothesis"
    PAYLOAD_REQUIRED = {
        "scope_id", "statement", "trigger_refs", "predictions", "support_requirements", "falsifiers",
        "confounders", "evidence_gaps", "materiality", "state", "predecessor",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["scope_id"], "$.payload.scope_id")
        text(p["statement"], "$.payload.statement")
        _validate_ref_list(p["trigger_refs"], "$.payload.trigger_refs")
        string_set(p["predictions"], "$.payload.predictions", min_items=1)
        string_set(p["support_requirements"], "$.payload.support_requirements", min_items=1)
        string_set(p["falsifiers"], "$.payload.falsifiers", min_items=1)
        string_set(p["confounders"], "$.payload.confounders")
        string_set(p["evidence_gaps"], "$.payload.evidence_gaps")
        enum(p["materiality"], {"low", "medium", "high", "critical"}, "$.payload.materiality")
        enum(p["state"], {"open", "supported", "weakened", "rejected", "revised", "unresolved"}, "$.payload.state")
        if p["predecessor"] is not None:
            identifier(p["predecessor"], "$.payload.predecessor")


class ProposedFinding(BaseContract):
    SCHEMA_NAME = "ProposedFinding"
    PAYLOAD_REQUIRED = {
        "scope_id", "claim", "materiality", "claim_strength", "supporting_refs", "refuting_refs",
        "calculation_refs", "qualifications", "obligations", "lifecycle",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        forbidden = {"accepted", "published", "disposition", "final_state"} & set(p)
        if forbidden:
            fail("PROHIBITED_STATE", "$.payload", "Final finding state is outside WP01")
        identifier(p["scope_id"], "$.payload.scope_id")
        text(p["claim"], "$.payload.claim")
        enum(p["materiality"], {"low", "medium", "high", "critical"}, "$.payload.materiality")
        enum(p["claim_strength"], {"observation", "association", "qualified_conclusion"}, "$.payload.claim_strength")
        _validate_ref_list(p["supporting_refs"], "$.payload.supporting_refs", min_items=1)
        _validate_ref_list(p["refuting_refs"], "$.payload.refuting_refs")
        string_set(p["calculation_refs"], "$.payload.calculation_refs")
        string_set(p["qualifications"], "$.payload.qualifications", min_items=1)
        string_set(p["obligations"], "$.payload.obligations")
        enum(p["lifecycle"], {"proposed", "verification_pending"}, "$.payload.lifecycle")
        if raw["producer"]["role"] not in {"engine", "operator"}:
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only an engine or authorised operator can propose a finding")


class VerificationRequest(BaseContract):
    SCHEMA_NAME = "VerificationRequest"
    PAYLOAD_REQUIRED = {
        "proposal_id", "proposal_revision", "proposal_digest", "required_checks", "evidence_refs",
        "assumptions", "contradictions", "verifier_policy", "proposer_component", "verifier_component", "deadline",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["proposal_id"], "$.payload.proposal_id")
        integer(p["proposal_revision"], "$.payload.proposal_revision", minimum=1)
        digest(p["proposal_digest"], "$.payload.proposal_digest")
        string_set(p["required_checks"], "$.payload.required_checks", min_items=1)
        _validate_ref_list(p["evidence_refs"], "$.payload.evidence_refs", min_items=1)
        string_set(p["assumptions"], "$.payload.assumptions")
        string_set(p["contradictions"], "$.payload.contradictions")
        identifier(p["verifier_policy"], "$.payload.verifier_policy")
        proposer = identifier(p["proposer_component"], "$.payload.proposer_component")
        verifier = identifier(p["verifier_component"], "$.payload.verifier_component")
        if proposer == verifier:
            fail("SELF_VERIFICATION", "$.payload.verifier_component", "Proposal producer cannot verify its own output")
        timestamp(p["deadline"], "$.payload.deadline")
        if raw["producer"]["role"] != "controller":
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only the controller can request verification")


class VerificationResult(BaseContract):
    SCHEMA_NAME = "VerificationResult"
    PAYLOAD_REQUIRED = {
        "request_id", "proposal_id", "proposal_revision", "proposal_digest", "proposer_component",
        "checked_evidence_refs", "checked_calculations", "contradiction_results", "assumption_results",
        "outcome", "rationale", "limitations",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        for field in ("request_id", "proposal_id", "proposer_component"):
            identifier(p[field], f"$.payload.{field}")
        integer(p["proposal_revision"], "$.payload.proposal_revision", minimum=1)
        digest(p["proposal_digest"], "$.payload.proposal_digest")
        _validate_ref_list(p["checked_evidence_refs"], "$.payload.checked_evidence_refs", min_items=1)
        string_set(p["checked_calculations"], "$.payload.checked_calculations")
        string_set(p["contradiction_results"], "$.payload.contradiction_results")
        string_set(p["assumption_results"], "$.payload.assumption_results")
        enum(p["outcome"], {"supported", "not_supported", "unresolved"}, "$.payload.outcome")
        text(p["rationale"], "$.payload.rationale")
        string_set(p["limitations"], "$.payload.limitations")
        if raw["producer"]["role"] != "verifier":
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only the verifier can issue verification results")
        if raw["producer"]["component"] == p["proposer_component"]:
            fail("INDEPENDENCE_FAILURE", "$.producer.component", "Verifier and proposer components must differ")


class InvestigationOutcome(BaseContract):
    SCHEMA_NAME = "InvestigationOutcome"
    PAYLOAD_REQUIRED = {
        "scope_id", "terminal_status", "terminal_reason", "retrieval_refs", "decision_refs", "evidence_refs",
        "hypothesis_refs", "proposal_refs", "verification_refs", "failure_refs", "budget_usage_id",
        "unresolved_questions", "configuration_versions",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["scope_id"], "$.payload.scope_id")
        enum(p["terminal_status"], {"complete", "partial", "inconclusive", "blocked", "failed", "budget_exhausted", "clarification_required"}, "$.payload.terminal_status")
        identifier(p["terminal_reason"], "$.payload.terminal_reason")
        for field in ("retrieval_refs", "decision_refs", "hypothesis_refs", "proposal_refs", "verification_refs", "failure_refs"):
            string_set(p[field], f"$.payload.{field}")
        _validate_ref_list(p["evidence_refs"], "$.payload.evidence_refs")
        identifier(p["budget_usage_id"], "$.payload.budget_usage_id")
        string_set(p["unresolved_questions"], "$.payload.unresolved_questions")
        versions = mapping(p["configuration_versions"], "$.payload.configuration_versions")
        for key, value in versions.items():
            identifier(key, "$.payload.configuration_versions")
            Version.parse(value)
        if raw["producer"]["role"] != "controller":
            fail("UNAUTHORISED_ACTOR", "$.producer.role", "Only the controller can assemble an investigation outcome")


class ContractFailure(BaseContract):
    SCHEMA_NAME = "ContractFailure"
    PAYLOAD_REQUIRED = {
        "boundary", "related_object_id", "related_digest", "category", "code", "field_path",
        "retryable", "policy_revision", "public_message",
    }

    @classmethod
    def _validate_payload(cls, p: Mapping[str, Any], raw: Mapping[str, Any]) -> None:
        identifier(p["boundary"], "$.payload.boundary")
        if p["related_object_id"] is not None:
            identifier(p["related_object_id"], "$.payload.related_object_id")
        if p["related_digest"] is not None:
            digest(p["related_digest"], "$.payload.related_digest")
        identifier(p["category"], "$.payload.category")
        identifier(p["code"], "$.payload.code")
        text(p["field_path"], "$.payload.field_path", max_chars=256)
        if not isinstance(p["retryable"], bool):
            fail("INVALID_TYPE", "$.payload.retryable", "Retryability must be Boolean")
        identifier(p["policy_revision"], "$.payload.policy_revision")
        message = text(p["public_message"], "$.payload.public_message", max_chars=512)
        if any(marker in message.lower() for marker in ("password=", "secret=", "bearer ", "private key")):
            fail("SENSITIVE_FAILURE_CONTENT", "$.payload.public_message", "Failure message contains prohibited sensitive content")


CONTRACT_TYPES: dict[str, type[BaseContract]] = {
    cls.SCHEMA_NAME: cls
    for cls in (
        InvestigationScope, InvestigationBudget, BudgetUsage, RetrievalRequest,
        AuthorisationDecision, RetrievalResult, EvidenceRef, Hypothesis,
        ProposedFinding, VerificationRequest, VerificationResult,
        InvestigationOutcome, ContractFailure,
    )
}


def load_contract(
    raw: Mapping[str, Any],
    *,
    compatibility: CompatibilityRegistry | None = None,
    receiver_version: str = "1.0.0",
) -> BaseContract:
    name = raw.get("schema_name")
    if name is None:
        fail("REQUIRED_FIELD", "$.schema_name", "Mandatory field is missing")
    contract_type = CONTRACT_TYPES.get(name) if isinstance(name, str) else None
    if contract_type is None:
        fail("UNKNOWN_SCHEMA", "$.schema_name", "Unknown contract schema")
    return contract_type.from_mapping(raw, compatibility=compatibility, receiver_version=receiver_version)


class EvidenceIndex:
    """Exact revision/digest/scope index for validating evidence-bearing claims."""

    def __init__(self, evidence: list[EvidenceRef]) -> None:
        self._items = {
            (item.payload["evidence_id"], item.revision): item for item in evidence
        }

    def validate_refs(self, refs: Any, *, expected_scope: str) -> None:
        _validate_ref_list(refs, "$.evidence_refs")
        for raw in refs:
            key = (raw["evidence_id"], raw["revision"])
            item = self._items.get(key)
            if item is None:
                fail("INVALID_EVIDENCE_REFERENCE", "$.evidence_refs", "Evidence reference does not resolve")
            if item.digest() != raw["digest"]:
                fail("DIGEST_MISMATCH", "$.evidence_refs", "Evidence reference digest does not match")
            if item.payload["scope_id"] != expected_scope or raw["scope_id"] != expected_scope:
                fail("EVIDENCE_SCOPE_MISMATCH", "$.evidence_refs", "Evidence belongs to another scope")
            if item.payload["access_state"] != "available":
                fail("EVIDENCE_UNAVAILABLE", "$.evidence_refs", "Evidence is not currently available")

    def validate_lineage(self, evidence: EvidenceRef) -> None:
        visited: set[tuple[str, int]] = set()

        def visit(item: EvidenceRef, chain: set[tuple[str, int]]) -> None:
            key = (str(item.payload["evidence_id"]), item.revision)
            if key in chain:
                fail("LINEAGE_CYCLE", "$.payload.lineage_parents", "Evidence lineage contains a cycle")
            if key in visited:
                return
            next_chain = set(chain)
            next_chain.add(key)
            child_expiry = timestamp(item.payload["expires_at"], "$.payload.expires_at")
            for raw in item.payload["lineage_parents"]:
                parent_key = (raw["evidence_id"], raw["revision"])
                if parent_key in next_chain:
                    fail("LINEAGE_CYCLE", "$.payload.lineage_parents", "Evidence lineage contains a cycle")
                parent = self._items.get(parent_key)
                if parent is None:
                    fail("MISSING_PARENT", "$.payload.lineage_parents", "Lineage parent does not resolve")
                if parent.digest() != raw["digest"]:
                    fail("DIGEST_MISMATCH", "$.payload.lineage_parents", "Lineage digest does not match")
                if timestamp(parent.payload["expires_at"], "$.payload.expires_at") < child_expiry:
                    fail("EXPIRY_EXTENSION", "$.payload.expires_at", "Derived evidence cannot extend parent expiry")
                if parent.classification != item.classification:
                    fail("CLASSIFICATION_DOWNGRADE", "$.classification", "Derived classification must preserve parent classification")
                visit(parent, next_chain)
            visited.add(key)

        visit(evidence, set())


def validate_outcome_completeness(
    outcome: InvestigationOutcome, *, known_failure_refs: set[str]
) -> None:
    if not known_failure_refs.issubset(set(outcome.payload["failure_refs"])):
        fail("INCOMPLETE_PROVENANCE", "$.payload.failure_refs", "Outcome omits a known failure")
