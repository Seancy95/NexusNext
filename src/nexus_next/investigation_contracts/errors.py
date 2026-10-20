"""Typed, bounded failures for the WP01 contract boundary."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ContractValidationError(ValueError):
    """A public-safe validation failure that never embeds the rejected value."""

    code: str
    path: str = "$"
    message: str = "Contract validation failed"
    retryable: bool = False

    def __str__(self) -> str:
        return f"{self.code} at {self.path}: {self.message}"


def fail(code: str, path: str = "$", message: str = "Contract validation failed") -> None:
    raise ContractValidationError(code=code, path=path, message=message)
