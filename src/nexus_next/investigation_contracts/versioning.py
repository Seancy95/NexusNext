"""Explicit contract-version compatibility with no implicit negotiation."""

from __future__ import annotations

import copy
import re
from dataclasses import dataclass
from typing import Any, Mapping

from .errors import fail
from .serialization import canonical_bytes

SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")


@dataclass(frozen=True, order=True, slots=True)
class Version:
    major: int
    minor: int
    patch: int

    @classmethod
    def parse(cls, value: Any) -> "Version":
        if not isinstance(value, str):
            fail("MALFORMED_VERSION", "$.schema_version", "Version must be a semantic-version string")
        match = SEMVER.fullmatch(value)
        if not match:
            fail("MALFORMED_VERSION", "$.schema_version", "Malformed semantic version")
        return cls(*(int(part) for part in match.groups()))

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


@dataclass(frozen=True, slots=True)
class TransformationRecord:
    transform_id: str
    source_version: str
    target_version: str
    original_digest: str
    transformed_digest: str


class CompatibilityRegistry:
    """Finite registry; callers cannot add fallback versions through payloads."""

    def __init__(self, supported: Mapping[str, tuple[str, ...] | list[str]]) -> None:
        self._supported = {name: tuple(versions) for name, versions in supported.items()}

    def supports(self, contract: str, version: str) -> bool:
        Version.parse(version)
        return version in self._supported.get(contract, ())

    def prepare(
        self,
        mapping: Mapping[str, Any],
        *,
        receiver_version: str = "1.0.0",
        allow_registered_transform: bool = True,
    ) -> tuple[dict[str, Any], TransformationRecord | None]:
        if any(key in mapping for key in ("fallback_versions", "disable_validation", "negotiate")):
            fail("NEGOTIATION_BYPASS", "$", "Payload-directed version negotiation is prohibited")
        name = mapping.get("schema_name")
        incoming_text = mapping.get("schema_version")
        incoming = Version.parse(incoming_text)
        receiver = Version.parse(receiver_version)
        if not isinstance(name, str) or name not in self._supported:
            fail("UNKNOWN_SCHEMA", "$.schema_name", "Unknown contract schema")
        if incoming_text == receiver_version and self.supports(name, incoming_text):
            return copy.deepcopy(dict(mapping)), None
        if name == "RetrievalRequest" and incoming_text == "0.9.0" and receiver_version == "1.0.0":
            if not allow_registered_transform:
                fail("UNSUPPORTED_VERSION", "$.schema_version", "No enabled compatibility transformation")
            import hashlib

            transformed = copy.deepcopy(dict(mapping))
            payload = dict(transformed.get("payload", {}))
            payload.setdefault("extensions", {})
            transformed["payload"] = payload
            transformed["schema_version"] = "1.0.0"
            return transformed, TransformationRecord(
                transform_id="retrieval-request-0.9-to-1.0",
                source_version="0.9.0",
                target_version="1.0.0",
                original_digest=hashlib.sha256(canonical_bytes(mapping)).hexdigest(),
                transformed_digest=hashlib.sha256(canonical_bytes(transformed)).hexdigest(),
            )
        if incoming.major != receiver.major:
            fail("UNSUPPORTED_MAJOR", "$.schema_version", "Unsupported contract major version")
        fail("UNSUPPORTED_VERSION", "$.schema_version", "No registered compatibility transformation")


def validate_transformation_preservation(
    original: Mapping[str, Any], transformed: Mapping[str, Any]
) -> None:
    """Reject compatibility transforms that lose governed meaning or lineage."""

    for field in ("classification", "parent_refs", "object_id", "revision", "correlation_id"):
        if original.get(field) != transformed.get(field):
            fail("SEMANTIC_LOSS", f"$.{field}", "Transformation changed protected contract meaning")
    original_payload = original.get("payload")
    transformed_payload = transformed.get("payload")
    if isinstance(original_payload, Mapping) and isinstance(transformed_payload, Mapping):
        protected = {
            key for key in original_payload
            if "evidence" in key or "classification" in key or "expir" in key or key.endswith("_refs")
        }
        for key in protected:
            if original_payload.get(key) != transformed_payload.get(key):
                fail("SEMANTIC_LOSS", f"$.payload.{key}", "Transformation lost protected evidence semantics")
