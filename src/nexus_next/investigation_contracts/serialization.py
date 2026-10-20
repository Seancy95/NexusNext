"""Deterministic JSON profile used by the bounded WP01 contracts."""

from __future__ import annotations

import json
import math
from collections.abc import Mapping, Sequence
from typing import Any

from .errors import ContractValidationError, fail

MAX_SAFE_INTEGER = 9_007_199_254_740_991


def _reject_constant(_: str) -> None:
    fail("NON_CANONICAL_VALUE", "$", "Non-finite numbers are prohibited")


def _pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            fail("INVALID_JSON", "$", "Duplicate JSON keys are prohibited")
        result[key] = value
    return result


def decode_json(data: bytes | str, *, max_bytes: int = 65_536) -> Any:
    raw = data.encode("utf-8") if isinstance(data, str) else data
    if len(raw) > max_bytes:
        fail("SIZE_LIMIT", "$", "Encoded contract exceeds the configured limit")
    try:
        text = raw.decode("utf-8", errors="strict")
        return json.loads(
            text,
            object_pairs_hook=_pairs_no_duplicates,
            parse_constant=_reject_constant,
        )
    except ContractValidationError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractValidationError("INVALID_JSON", "$", "Malformed UTF-8 JSON") from exc


def _normalise(value: Any, path: str = "$") -> Any:
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > MAX_SAFE_INTEGER:
            fail("NON_CANONICAL_VALUE", path, "Integer exceeds the canonical safe range")
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            fail("NON_CANONICAL_VALUE", path, "Non-finite numbers are prohibited")
        fail("NON_CANONICAL_VALUE", path, "Binary floating-point values are prohibited")
    if isinstance(value, Mapping):
        output: dict[str, Any] = {}
        for key in sorted(value):
            if not isinstance(key, str):
                fail("NON_CANONICAL_VALUE", path, "JSON object keys must be strings")
            output[key] = _normalise(value[key], f"{path}.{key}")
        return output
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_normalise(item, f"{path}[{index}]") for index, item in enumerate(value)]
    fail("NON_CANONICAL_VALUE", path, "Unsupported canonical value type")


def canonical_bytes(value: Any, *, max_bytes: int = 65_536) -> bytes:
    try:
        encoded = json.dumps(
            _normalise(value),
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except ContractValidationError:
        raise
    except (UnicodeEncodeError, ValueError) as exc:
        raise ContractValidationError(
            "SERIALIZATION_FAILURE", "$", "Canonical serialization failed"
        ) from exc
    if len(encoded) > max_bytes:
        fail("SIZE_LIMIT", "$", "Canonical contract exceeds the configured limit")
    return encoded
