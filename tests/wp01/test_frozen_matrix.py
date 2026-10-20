"""One independently reported unittest method for each frozen matrix row."""

from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

from .matrix_cases import run_case

MATRIX = Path(__file__).parents[2] / "docs/B03-WP01-READINESS/synthetic_conformance_matrix.csv"


class FrozenMatrixTests(unittest.TestCase):
    pass


def _install_tests() -> None:
    with MATRIX.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 68:
        raise RuntimeError(f"Frozen matrix must contain 68 cases, found {len(rows)}")
    for row in rows:
        case_id = row["test_id"]
        method_name = "test_matrix_" + re.sub(r"[^a-z0-9]+", "_", case_id.lower()).strip("_")

        def test_method(self: FrozenMatrixTests, frozen_id: str = case_id) -> None:
            run_case(self, frozen_id)

        test_method.__name__ = method_name
        test_method.__doc__ = f"Frozen prospective case {case_id}."
        setattr(FrozenMatrixTests, method_name, test_method)


_install_tests()


if __name__ == "__main__":
    unittest.main()
