"""Narrow regressions for defects exposed by the first frozen-matrix run."""

from __future__ import annotations

import unittest

from nexus_next.investigation_contracts import (
    CompatibilityRegistry,
    ContractValidationError,
    RetrievalRequest,
    canonical_bytes,
    load_contract,
)
from nexus_next.investigation_contracts.models import CONTRACT_TYPES

from .fixture_factory import valid_mapping


class MatrixDefectRegressions(unittest.TestCase):
    def test_reg_001_typed_canonical_error_is_not_wrapped(self):
        with self.assertRaises(ContractValidationError) as caught:
            canonical_bytes({"value": float("nan")})
        self.assertEqual("NON_CANONICAL_VALUE", caught.exception.code)

    def test_reg_002_registered_cross_major_transform_runs_before_default_rejection(self):
        raw = valid_mapping("RetrievalRequest")
        raw["schema_version"] = "0.9.0"
        registry = CompatibilityRegistry({name: ["1.0.0"] for name in CONTRACT_TYPES})
        contract = load_contract(raw, compatibility=registry)
        self.assertIsInstance(contract, RetrievalRequest)
        self.assertEqual("retrieval-request-0.9-to-1.0", contract.transformation.transform_id)


if __name__ == "__main__":
    unittest.main()
