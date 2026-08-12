#!/usr/bin/env python3
"""Small standard-library regression suite for the catalog contract."""

from __future__ import annotations

import copy
import sys
import unittest
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_catalog import (  # noqa: E402
    load_catalog,
    load_json,
    validate_catalog,
    validate_schema_contract,
)
from render_catalog import render_catalog, replace_generated_region  # noqa: E402
from validate_repository import validate_repository  # noqa: E402


TODAY = date(2026, 8, 12)


def localized(zh: str, en: str) -> dict[str, str]:
    return {"zh-CN": zh, "en": en}


def valid_project() -> dict[str, object]:
    """Return synthetic data that is never written into the real catalog."""
    return {
        "id": "contract-test-app",
        "kind": "application",
        "name": localized("契约测试应用", "Contract Test Application"),
        "primary_category": "productivity-collaboration",
        "secondary_category": "task-workflow",
        "problem": localized(
            "帮助测试人员验证目录数据契约能否正确工作。",
            "Helps maintainers verify that the catalog contract works correctly.",
        ),
        "features": [
            localized(
                "执行一条完整的合成测试流程",
                "Runs one complete synthetic test workflow",
            ),
            localized(
                "阻止违反范围与证据规则的目录输入",
                "Rejects catalog input that violates scope or evidence rules",
            ),
        ],
        "value": localized(
            "在不污染正式目录的情况下发现验证规则回归。",
            "Finds validation regressions without polluting the production catalog.",
        ),
        "tech_stack": ["Python", "JSON", "Markdown"],
        "ai_role": {
            "tools": ["Synthetic Test Tool"],
            "depth": "natural-language-driven-core",
            "workflow": localized(
                "自然语言定义测试场景，生成实现后根据失败结果持续迭代。",
                "Natural language defines scenarios and failed checks drive implementation iterations.",
            ),
            "evidence_urls": ["https://github.com/openai/openai-python"],
        },
        "demo_url": "https://www.python.org/",
        "source_url": "https://github.com/python/cpython",
        "quality_evidence": localized(
            "测试数据可以完整通过所有机器可检查规则。",
            "The fixture passes every machine-checkable catalog rule.",
        ),
        "verification": {
            "sources": ["https://docs.python.org/3/"],
            "review_issue_url": (
                "https://github.com/openai/"
                "Awesome-VibeCoding-Showcase/issues/1"
            ),
            "submitter_attested": True,
            "verified_on": "2026-08-12",
        },
        "added_on": "2026-08-12",
    }


class CatalogContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = load_catalog()

    def with_project(self) -> dict[str, object]:
        data = copy.deepcopy(self.catalog)
        data["projects"] = [valid_project()]
        return data

    def assert_has(self, errors: list[str], requirement: str) -> None:
        self.assertTrue(
            any(requirement in error for error in errors),
            f"expected {requirement!r} in {errors!r}",
        )

    def test_empty_production_catalog_is_valid(self) -> None:
        self.assertEqual(validate_catalog(self.catalog, today=TODAY), [])

    def test_complete_application_fixture_is_valid(self) -> None:
        self.assertEqual(validate_catalog(self.with_project(), today=TODAY), [])

    def test_tool_is_rejected_by_scope_rule(self) -> None:
        data = self.with_project()
        data["projects"][0]["kind"] = "tool"
        self.assert_has(validate_catalog(data, today=TODAY), "P2 / P3")

    def test_placeholder_demo_is_rejected(self) -> None:
        data = self.with_project()
        data["projects"][0]["demo_url"] = "https://example.com/demo"
        self.assert_has(validate_catalog(data, today=TODAY), "C1 / D5")

    def test_secondary_category_must_belong_to_primary(self) -> None:
        data = self.with_project()
        data["projects"][0]["secondary_category"] = "commerce-sales"
        self.assert_has(validate_catalog(data, today=TODAY), "C4")

    def test_ai_evidence_is_mandatory(self) -> None:
        data = self.with_project()
        data["projects"][0]["ai_role"]["evidence_urls"] = []
        self.assert_has(validate_catalog(data, today=TODAY), "C3 / C5 / D4")

    def test_verification_needs_independent_source(self) -> None:
        data = self.with_project()
        project = data["projects"][0]
        project["verification"]["sources"] = [project["demo_url"]]
        self.assert_has(validate_catalog(data, today=TODAY), "C5")

    def test_review_record_must_be_a_github_issue(self) -> None:
        data = self.with_project()
        data["projects"][0]["verification"]["review_issue_url"] = (
            "https://github.com/python/cpython/pull/1"
        )
        self.assert_has(validate_catalog(data, today=TODAY), "C5")

    def test_review_record_must_belong_to_showcase_repository(self) -> None:
        data = self.with_project()
        data["projects"][0]["verification"]["review_issue_url"] = (
            "https://github.com/python/cpython/issues/1"
        )
        self.assert_has(validate_catalog(data, today=TODAY), "C5")

    def test_one_review_issue_cannot_approve_multiple_projects(self) -> None:
        data = self.with_project()
        second = copy.deepcopy(data["projects"][0])
        second["id"] = "contract-test-app-two"
        second["name"] = localized("第二个契约应用", "Second Contract Application")
        second["demo_url"] = "https://www.iana.org/"
        second["source_url"] = "https://github.com/psf/requests"
        data["projects"].append(second)
        self.assert_has(validate_catalog(data, today=TODAY), "C5")

    def test_browser_normalized_private_hosts_are_rejected(self) -> None:
        blocked = (
            "http://127.1/",
            "http://2130706433/",
            "http://017700000001/",
            "http://0x7f000001/",
            "http://ⓛocalhost/",
            "http://127。0。0。1/",
            "http://127%2e0%2e0%2e1/",
            "https://ⓔxample.com/",
        )
        for value in blocked:
            with self.subTest(value=value):
                data = self.with_project()
                data["projects"][0]["demo_url"] = value
                self.assert_has(validate_catalog(data, today=TODAY), "C1 / D5")

    def test_fragment_does_not_create_independent_verification_source(self) -> None:
        data = self.with_project()
        project = data["projects"][0]
        project["verification"]["sources"] = [project["source_url"] + "#readme"]
        self.assert_has(validate_catalog(data, today=TODAY), "C5")

    def test_renderer_includes_all_listing_fields(self) -> None:
        data = self.with_project()
        output = render_catalog(data, "en")
        self.assertIn("<!-- project:contract-test-app -->", output)
        self.assertIn("Problem", output)
        self.assertIn("Core features and value", output)
        self.assertIn("Main stack", output)
        self.assertIn("AI involvement", output)
        self.assertIn("Public links", output)
        self.assertIn("Review issue", output)

    def test_renderer_escapes_markdown_in_catalog_text(self) -> None:
        data = self.with_project()
        data["projects"][0]["name"]["en"] = "Unsafe [link](javascript:alert)"
        output = render_catalog(data, "en")
        self.assertIn(r"Unsafe \[link\](javascript:alert)", output)
        self.assertNotIn("[link](javascript:alert)", output.replace(r"\[link\]", ""))

    def test_renderer_omits_category_descriptions(self) -> None:
        data = self.with_project()
        data["categories"][0]["description"]["en"] = "# Injected heading"
        data["categories"][0]["subcategories"][0]["description"]["en"] = (
            "1. Injected list"
        )
        output = render_catalog(data, "en")
        self.assertNotIn("Injected heading", output)
        self.assertNotIn("Injected list", output)

    def test_generated_region_requires_exactly_one_marker_pair(self) -> None:
        with self.assertRaises(ValueError):
            replace_generated_region("# No markers\n", "content", Path("README.md"))

    def test_repository_cross_file_contract_is_valid(self) -> None:
        self.assertEqual(validate_repository(), [])

    def test_json_schema_declarations_match_runtime_contract(self) -> None:
        schema = load_json(SCRIPT_DIR.parent / "schema" / "projects.schema.json")
        self.assertEqual(validate_schema_contract(schema), [])


if __name__ == "__main__":
    unittest.main()
