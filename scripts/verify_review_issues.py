#!/usr/bin/env python3
"""Verify that every catalog review record is an approved Issue in this repo."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from validate_catalog import (
    DEFAULT_DATA,
    CatalogLoadError,
    load_catalog,
    parse_repository_full_name,
    parse_review_issue_url,
    validate_catalog,
)


APPROVED_STATUS_LABELS = {"status: approved", "status: listed"}
REQUIRED_SUBMISSION_LABEL = "submission"
API_VERSION = "2022-11-28"


class ReviewIssueAPIError(RuntimeError):
    """Raised when GitHub cannot provide a usable Issue response."""


def _escape_annotation(message: str) -> str:
    return (
        message.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
    )


def fetch_issue_payload(
    repository_full_name: str,
    issue_number: int,
    token: str,
) -> Any:
    """Fetch one Issue from GitHub's REST API using a scoped Actions token."""
    repository = parse_repository_full_name(repository_full_name)
    if repository is None:
        raise ReviewIssueAPIError("invalid repository owner/name")
    owner, repo = repository
    api_url = (
        "https://api.github.com/repos/"
        f"{quote(owner, safe='')}/{quote(repo, safe='')}/issues/{issue_number}"
    )
    request = Request(
        api_url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-vibecoding-showcase-review-verifier",
            "X-GitHub-Api-Version": API_VERSION,
        },
    )
    try:
        with urlopen(request, timeout=20) as response:  # noqa: S310 (fixed host)
            status = getattr(response, "status", 200)
            body = response.read()
    except HTTPError as exc:
        try:
            detail = json.loads(exc.read().decode("utf-8")).get("message", "")
        except (UnicodeDecodeError, json.JSONDecodeError, AttributeError):
            detail = ""
        suffix = f": {detail}" if detail else ""
        raise ReviewIssueAPIError(f"GitHub API returned HTTP {exc.code}{suffix}") from exc
    except URLError as exc:
        raise ReviewIssueAPIError(f"GitHub API request failed: {exc.reason}") from exc

    if status != 200:
        raise ReviewIssueAPIError(f"GitHub API returned unexpected HTTP {status}")
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ReviewIssueAPIError("GitHub API returned invalid JSON") from exc


def verify_issue_payload(payload: Any) -> list[str]:
    """Validate the GitHub Issue shape and its governance labels."""
    if not isinstance(payload, dict):
        return ["GitHub API response must be an object"]
    errors: list[str] = []
    if "pull_request" in payload:
        errors.append("review record is a pull request, not an Issue")

    raw_labels = payload.get("labels")
    label_names: set[str] = set()
    if not isinstance(raw_labels, list):
        errors.append("GitHub API response has no valid labels array")
    else:
        for label in raw_labels:
            if isinstance(label, dict) and isinstance(label.get("name"), str):
                label_names.add(label["name"].strip().casefold())
            elif isinstance(label, str):
                label_names.add(label.strip().casefold())

        if REQUIRED_SUBMISSION_LABEL not in label_names:
            errors.append("Issue is missing the 'submission' label")
        if label_names.isdisjoint(APPROVED_STATUS_LABELS):
            errors.append(
                "Issue must have 'status: approved' or 'status: listed' label"
            )
    return errors


IssueFetcher = Callable[[str, int, str], Any]


def verify_catalog_review_issues(
    data: Any,
    repository_full_name: str,
    token: str | None,
    *,
    fetch_issue: IssueFetcher = fetch_issue_payload,
) -> list[str]:
    """Verify all review Issues, returning readable errors without exceptions."""
    catalog_errors = validate_catalog(
        data,
        repository_full_name=repository_full_name,
    )
    if catalog_errors:
        return [f"catalog: {message}" for message in catalog_errors]

    projects = data.get("projects", [])
    if not projects:
        # The repository intentionally starts empty; no token or API call is needed.
        return []
    if not token or not token.strip():
        return ["GITHUB_TOKEN is required when the catalog contains projects"]

    errors: list[str] = []
    for index, project in enumerate(projects):
        issue_url = project["verification"]["review_issue_url"]
        issue = parse_review_issue_url(issue_url)
        if issue is None:
            # validate_catalog already guarantees this branch cannot normally occur.
            errors.append(f"projects[{index}]: review Issue URL is invalid")
            continue
        issue_number = issue[2]
        try:
            payload = fetch_issue(repository_full_name, issue_number, token.strip())
        except ReviewIssueAPIError as exc:
            errors.append(
                f"projects[{index}] ({project['id']}), Issue #{issue_number}: {exc}"
            )
            continue
        for message in verify_issue_payload(payload):
            errors.append(
                f"projects[{index}] ({project['id']}), Issue #{issue_number}: "
                f"{message}"
            )
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--repository", required=True, metavar="OWNER/REPOSITORY")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        data = load_catalog(args.data)
    except CatalogLoadError as exc:
        print(f"::error::{_escape_annotation(str(exc))}")
        return 1

    errors = verify_catalog_review_issues(
        data,
        args.repository,
        os.environ.get("GITHUB_TOKEN"),
    )
    for message in errors:
        print(f"::error::{_escape_annotation(message)}")
    if errors:
        print(
            f"Review Issue verification failed with {len(errors)} error(s).",
            file=sys.stderr,
        )
        return 1

    print(f"Verified {len(data['projects'])} approved review Issue(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
