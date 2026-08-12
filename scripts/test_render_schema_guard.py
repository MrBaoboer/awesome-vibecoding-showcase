#!/usr/bin/env python3
"""Regression tests for evidence-count schema parity."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_catalog import (  # noqa: E402
    DEFAULT_SCHEMA,
    load_json,
    validate_schema_contract,
)


class RenderSchemaGuardTests(unittest.TestCase):
    def test_schema_declares_eight_url_limits(self) -> None:
        schema = load_json(DEFAULT_SCHEMA)
        definitions = schema["$defs"]
        self.assertEqual(
            definitions["aiRole"]["properties"]["evidence_urls"]["maxItems"],
            8,
        )
        self.assertEqual(
            definitions["verification"]["properties"]["sources"]["maxItems"],
            8,
        )
        self.assertEqual(validate_schema_contract(schema), [])

    def test_schema_contract_detects_evidence_limit_drift(self) -> None:
        schema = load_json(DEFAULT_SCHEMA)
        drifted = copy.deepcopy(schema)
        drifted["$defs"]["aiRole"]["properties"]["evidence_urls"][
            "maxItems"
        ] = 9
        errors = validate_schema_contract(drifted)
        self.assertTrue(any("AI evidence URL count" in error for error in errors))

        drifted = copy.deepcopy(schema)
        drifted["$defs"]["verification"]["properties"]["sources"][
            "maxItems"
        ] = 9
        errors = validate_schema_contract(drifted)
        self.assertTrue(
            any("verification source count" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
