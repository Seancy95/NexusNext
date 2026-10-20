"""Registry/configuration conformance for the bounded WP01 surface."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from nexus_next.investigation_contracts import load_contract
from nexus_next.investigation_contracts.models import CONTRACT_TYPES


class RegistryTests(unittest.TestCase):
    def test_registry_has_exact_contract_set_and_disables_post_wp01_authority(self):
        path = Path(__file__).parents[2] / "config/wp01_contract_registry.json"
        registry = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(set(CONTRACT_TYPES), set(registry["contracts"]))
        self.assertEqual(13, len(registry["contracts"]))
        self.assertTrue(all(value is False for value in registry["authority"].values()))

    def test_materialized_synthetic_fixture_set_validates(self):
        path = Path(__file__).parent / "fixtures/v1/valid_contracts.json"
        fixtures = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(set(CONTRACT_TYPES), set(fixtures))
        for name, raw in fixtures.items():
            with self.subTest(contract=name):
                self.assertEqual(name, load_contract(raw).schema_name)


if __name__ == "__main__":
    unittest.main()
