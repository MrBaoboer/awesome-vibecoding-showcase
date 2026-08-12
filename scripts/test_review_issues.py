#!/usr/bin/env python3
"""Regression tests for repository-bound review Issue verification."""

from __future__ import annotations

import copy
import sys
import unittest
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from test_catalog import load_catalog, localized, valid_project  # noqa: E402
from validate_catalog import parse_review_issue_url, validate_catalog  # noqa: E402
from verify_review_issues import (  # noqa: E402
    ReviewIssueAPIError,
    verify_catalog_review_issues,
    verify_issue_payload,
)


TODAY = date(2026, 8, 12)
CURRENT_REPOSITORY = "openai/Awesome-VibeCoding-Showcase"


class ReviewIssueGuardTests(unittest.TestCase):
    def with_project(self) -> dict[str, object]:
        data = copy.deepcopy(load_catalog())
        data["projects"] = [valid_project()]
        return data

    def test_review_issue_parser_returns_casefolded_identity(self) -> None:
        self.assertEqual(
            parse_review_issue_url(
                "https://GITHUB.com:443/OpenAI/"
                "awesome-vibecoding-showcase/issues/42"
            ),
            ("openai", "awesome-vibecoding-showcase", 42),
        )

    def test_catalog_binds_review_issue_to_current_repository(self) -> None:
        data = self.with_project()
        self.assertEqual(
            validate_catalog(
                data,
                today=TODAY,
                repository_full_name=CURRENT_REPOSITORY,
            ),
            [],
        )
        errors = validate_catalog(
            data,
            today=TODAY,
            repository_full_name="attacker/Awesome-VibeCoding-Showcase",
        )
        self.assertTrue(any("must belong to the current repository" in e for e in errors))

    def test_review_issue_uniqueness_is_case_insensitive(self) -> None:
        data = self.with_project()
        second = copy.deepcopy(data["projects"][0])
        second["id"] = "contract-test-app-two"
        second["name"] = localized("第二个契约应用", "Second Contract Application")
        second["demo_url"] = "https://www.iana.org/"
        second["source_url"] = "https://github.com/psf/requests"
        second["verification"]["review_issue_url"] = (
            "https://github.com/OPENAI/"
            "awesome-vibecoding-showcase/issues/1"
        )
        data["projects"].append(second)
        errors = validate_catalog(data, today=TODAY)
        self.assertTrue(any("duplicates another project's" in e for e in errors))

    def test_approved_issue_payload_passes(self) -> None:
        payload = {
            "labels": [
                {"name": "submission"},
                {"name": "status: approved"},
            ]
        }
        self.assertEqual(verify_issue_payload(payload), [])

    def test_listed_issue_payload_passes_case_insensitively(self) -> None:
        payload = {"labels": ["Submission", {"name": "Status: Listed"}]}
        self.assertEqual(verify_issue_payload(payload), [])

    def test_pull_request_and_missing_labels_are_rejected(self) -> None:
        errors = verify_issue_payload({"pull_request": {}, "labels": []})
        self.assertTrue(any("pull request" in error for error in errors))
        self.assertTrue(any("submission" in error for error in errors))
        self.assertTrue(any("approved" in error for error in errors))

    def test_empty_catalog_passes_without_token_or_network(self) -> None:
        data = load_catalog()

        def unexpected_fetch(*_args: object) -> object:
            self.fail("empty catalog attempted a network request")

        self.assertEqual(
            verify_catalog_review_issues(
                data,
                CURRENT_REPOSITORY,
                None,
                fetch_issue=unexpected_fetch,
            ),
            [],
        )

    def test_nonempty_catalog_requires_actions_token(self) -> None:
        errors = verify_catalog_review_issues(
            self.with_project(),
            CURRENT_REPOSITORY,
            None,
        )
        self.assertEqual(errors, ["GITHUB_TOKEN is required when the catalog contains projects"])

    def test_verifier_fetches_current_issue_and_checks_labels(self) -> None:
        calls: list[tuple[str, int, str]] = []

        def fake_fetch(repository: str, number: int, token: str) -> object:
            calls.append((repository, number, token))
            return {
                "labels": [
                    {"name": "submission"},
                    {"name": "status: listed"},
                ]
            }

        errors = verify_catalog_review_issues(
            self.with_project(),
            CURRENT_REPOSITORY,
            "test-token",
            fetch_issue=fake_fetch,
        )
        self.assertEqual(errors, [])
        self.assertEqual(calls, [(CURRENT_REPOSITORY, 1, "test-token")])

    def test_api_failure_is_reported_with_project_and_issue(self) -> None:
        def failed_fetch(_repository: str, _number: int, _token: str) -> object:
            raise ReviewIssueAPIError("GitHub API returned HTTP 404")

        errors = verify_catalog_review_issues(
            self.with_project(),
            CURRENT_REPOSITORY,
            "test-token",
            fetch_issue=failed_fetch,
        )
        self.assertEqual(len(errors), 1)
        self.assertIn("contract-test-app", errors[0])
        self.assertIn("Issue #1", errors[0])
        self.assertIn("HTTP 404", errors[0])


if __name__ == "__main__":
    unittest.main()
