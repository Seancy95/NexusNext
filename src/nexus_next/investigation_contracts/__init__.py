"""B03-WP01 foundational contracts.

This package validates data and permitted contract transitions. It does not
authenticate runtime callers, implement investigative reasoning, or accept
findings.
"""

from .authority import (
    TransitionDecision,
    request_transition,
    validate_authorised_binding,
    validate_retrieval_request,
)
from .errors import ContractValidationError
from .models import (
    AuthorisationDecision,
    BaseContract,
    BudgetUsage,
    ContractFailure,
    EvidenceIndex,
    EvidenceRef,
    Hypothesis,
    InvestigationBudget,
    InvestigationOutcome,
    InvestigationScope,
    ProposedFinding,
    RetrievalRequest,
    RetrievalResult,
    VerificationRequest,
    VerificationResult,
    load_contract,
    validate_outcome_completeness,
)
from .serialization import canonical_bytes, decode_json
from .versioning import (
    CompatibilityRegistry,
    TransformationRecord,
    Version,
    validate_transformation_preservation,
)

__all__ = [
    "AuthorisationDecision", "BaseContract", "BudgetUsage", "CompatibilityRegistry",
    "ContractFailure", "ContractValidationError", "EvidenceIndex", "EvidenceRef",
    "Hypothesis", "InvestigationBudget", "InvestigationOutcome", "InvestigationScope",
    "ProposedFinding", "RetrievalRequest", "RetrievalResult", "TransformationRecord",
    "TransitionDecision", "VerificationRequest", "VerificationResult", "Version",
    "canonical_bytes", "decode_json", "load_contract", "request_transition",
    "validate_authorised_binding", "validate_outcome_completeness",
    "validate_retrieval_request", "validate_transformation_preservation",
]
