"""Shared strict validators for WP01 contracts."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Any

from .errors import fail

IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def exact_keys(mapping: Mapping[str, Any], required: set[str], optional: set[str], path: str) -> None:
    missing = sorted(required - set(mapping))
    if missing:
        fail("REQUIRED_FIELD", f"{path}.{missing[0]}", "Mandatory field is missing")
    unknown = sorted(set(mapping) - required - optional)
    if unknown:
        fail("UNKNOWN_FIELD", f"{path}.{unknown[0]}", "Unknown field is prohibited")


def identifier(value: Any, path: str) -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        fail("INVALID_IDENTIFIER", path, "Identifier has invalid syntax or length")
    return value


def text(value: Any, path: str, *, allow_empty: bool = False, max_chars: int = 8192) -> str:
    if not isinstance(value, str) or len(value) > max_chars or (not allow_empty and not value.strip()):
        fail("INVALID_TEXT", path, "Text is missing, blank or exceeds its bound")
    return value


def integer(value: Any, path: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        fail("INVALID_INTEGER", path, "Integer is outside the permitted range")
    return value


def timestamp(value: Any, path: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        fail("INVALID_TIMESTAMP", path, "Timestamp must be UTC RFC 3339 with Z")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        fail("INVALID_TIMESTAMP", path, "Timestamp is malformed")
        raise AssertionError from exc
    if parsed.tzinfo != timezone.utc:
        fail("INVALID_TIMESTAMP", path, "Timestamp must be UTC")
    return parsed


def digest(value: Any, path: str) -> str:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        fail("INVALID_DIGEST", path, "SHA-256 digest must be lowercase hexadecimal")
    return value


def sequence(value: Any, path: str, *, min_items: int = 0, max_items: int = 256) -> list[Any]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        fail("INVALID_COLLECTION", path, "Expected an array")
    items = list(value)
    if not min_items <= len(items) <= max_items:
        fail("COLLECTION_SIZE", path, "Collection size is outside the permitted range")
    return items


def string_set(value: Any, path: str, *, min_items: int = 0) -> tuple[str, ...]:
    items = sequence(value, path, min_items=min_items)
    checked = tuple(text(item, f"{path}[{index}]", max_chars=256) for index, item in enumerate(items))
    if len(set(checked)) != len(checked):
        fail("DUPLICATE_MEMBER", path, "Semantic set contains a duplicate")
    return tuple(sorted(checked))


def enum(value: Any, allowed: set[str], path: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        fail("INVALID_ENUM", path, "Enumeration value is not supported")
    return value


def mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        fail("INVALID_OBJECT", path, "Expected an object")
    return value


def deep_freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({str(key): deep_freeze(item) for key, item in value.items()})
    if isinstance(value, list | tuple):
        return tuple(deep_freeze(item) for item in value)
    return value


def thaw(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [thaw(item) for item in value]
    return value
