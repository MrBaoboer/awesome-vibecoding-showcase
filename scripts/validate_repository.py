#!/usr/bin/env python3
"""Validate cross-file repository contracts without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS = tuple(f"C{index}" for index in range(1, 6)) + tuple(
    f"D{index}" for index in range(1, 6)
)
STATUS_LABELS = {
    "status: triage",
    "status: needs-info",
    "status: approved",
    "status: listed",
    "status: declined",
    "status: stale",
    "status: removed",
}
LEGACY_STATUS_TEXT = {
    "status: needs-triage",
    "status: needs-review",
    "status: rejected",
    "content: remove",
    "status:approved",
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _form_labels(document: str) -> set[str]:
    match = re.search(
        r"^labels:\s*\n(?P<labels>(?:  - [^\n]+\n)+)",
        document,
        flags=re.MULTILINE,
    )
    if not match:
        return set()
    return set(re.findall(r'^  - "([^"]+)"$', match.group("labels"), re.MULTILINE))


def validate_repository() -> list[str]:
    errors: list[str] = []

    for license_path in (
        "LICENSE",
        "LICENSING.md",
        "LICENSING.en.md",
        "CONTENT-LICENSING.md",
    ):
        if not (ROOT / license_path).is_file():
            errors.append(f"required licensing file is missing: {license_path}")
    for legacy_path in ("LICENSE-CODE", "LICENSE-CONTENT"):
        if (ROOT / legacy_path).exists():
            errors.append(
                f"legacy {legacy_path} must be removed; LICENSE-* files cause GitHub "
                "to report an unknown multi-license result"
            )
    mit_license = read("LICENSE") if (ROOT / "LICENSE").is_file() else ""
    for required_text in (
        "MIT License",
        "Permission is hereby granted, free of charge",
        'THE SOFTWARE IS PROVIDED "AS IS"',
    ):
        if required_text not in mit_license:
            errors.append(f"root LICENSE is missing standard MIT text: {required_text!r}")
    readme_license_targets = {
        "README.md": ("LICENSE", "LICENSING.md", "CONTENT-LICENSING.md"),
        "README.en.md": ("LICENSE", "LICENSING.en.md", "CONTENT-LICENSING.md"),
    }
    for readme_path, targets in readme_license_targets.items():
        readme = read(readme_path)
        for target in targets:
            if f"({target})" not in readme:
                errors.append(f"{readme_path} must link to {target}")

    catalog = json.loads(read("data/projects.json"))
    primary_ids = [category["id"] for category in catalog["categories"]]
    category_pairs = [
        f"{category['id']} / {subcategory['id']}"
        for category in catalog["categories"]
        for subcategory in category["subcategories"]
    ]

    submission_url = (
        "https://github.com/MrBaoboer/Awesome-VibeCoding-Showcase/"
        "issues/new?template=project-submission.yml"
    )
    for readme_path in ("README.md", "README.en.md"):
        if submission_url not in read(readme_path):
            errors.append(
                f"{readme_path} must link directly to the project submission form"
            )

    for category_doc_path in ("docs/CATEGORIES.md", "docs/CATEGORIES.en.md"):
        category_doc = read(category_doc_path)
        for category_id in primary_ids:
            if f"`{category_id}`" not in category_doc:
                errors.append(
                    f"{category_doc_path} is missing primary category {category_id}"
                )
        for pair in category_pairs:
            secondary_id = pair.split(" / ", 1)[1]
            if f"`{secondary_id}`" not in category_doc:
                errors.append(
                    f"{category_doc_path} is missing secondary category {secondary_id}"
                )

    labels_text = read(".github/labels.yml")
    declared_labels = set(
        re.findall(r'^- name: "([^"]+)"$', labels_text, flags=re.MULTILINE)
    )
    declared_statuses = {
        label for label in declared_labels if label.startswith("status: ")
    }
    if declared_statuses != STATUS_LABELS:
        missing = sorted(STATUS_LABELS - declared_statuses)
        extra = sorted(declared_statuses - STATUS_LABELS)
        errors.append(f"status label mismatch; missing={missing}, extra={extra}")

    for form_path in (
        ".github/ISSUE_TEMPLATE/project-submission.yml",
        ".github/ISSUE_TEMPLATE/general-issue.yml",
    ):
        referenced = _form_labels(read(form_path))
        missing = sorted(referenced - declared_labels)
        if missing:
            errors.append(f"{form_path} references undeclared labels: {missing}")

    mapped_files = (
        ".github/ISSUE_TEMPLATE/project-submission.yml",
        ".github/ISSUE_TEMPLATE/general-issue.yml",
        ".github/pull_request_template.md",
    )
    for path in mapped_files:
        content = read(path)
        missing = [requirement for requirement in REQUIREMENTS if requirement not in content]
        if missing:
            errors.append(f"{path} is missing requirement mappings: {missing}")

    searchable_paths = (
        "README.md",
        "README.en.md",
        "CONTRIBUTING.md",
        "CONTRIBUTING.en.md",
        "GOVERNANCE.md",
        "GOVERNANCE.en.md",
        "docs/REVIEW_CHECKLIST.md",
        ".github/ISSUE_TEMPLATE/project-submission.yml",
        ".github/ISSUE_TEMPLATE/general-issue.yml",
        ".github/labels.yml",
    )
    for path in searchable_paths:
        content = read(path)
        for legacy in LEGACY_STATUS_TEXT:
            if legacy in content:
                errors.append(f"{path} contains legacy status text {legacy!r}")

    for workflow_path in (
        ".github/workflows/links.yml",
        ".github/workflows/validate.yml",
    ):
        workflow = read(workflow_path)
        if "pull_request_target:" in workflow:
            errors.append(f"{workflow_path} must not use pull_request_target")
        if re.search(r"^\s+[a-z-]+:\s*write\s*$", workflow, flags=re.MULTILINE):
            errors.append(f"{workflow_path} must not grant write permissions")

    links_permissions = re.search(
        r"^permissions:\s*\n(?P<body>(?:  [a-z-]+: [a-z]+\s*\n)+)",
        read(".github/workflows/links.yml"),
        flags=re.MULTILINE,
    )
    if not links_permissions or links_permissions.group("body").split() != [
        "contents:",
        "read",
    ]:
        errors.append("links workflow must declare only contents: read")

    validate_permissions = re.search(
        r"^permissions:\s*\n(?P<body>(?:  [a-z-]+: [a-z]+\s*\n)+)",
        read(".github/workflows/validate.yml"),
        flags=re.MULTILINE,
    )
    expected_validate_permissions = {"contents: read", "issues: read"}
    actual_validate_permissions = (
        {
            line.strip()
            for line in validate_permissions.group("body").splitlines()
            if line.strip()
        }
        if validate_permissions
        else set()
    )
    if actual_validate_permissions != expected_validate_permissions:
        errors.append(
            "validate workflow permissions must be exactly contents: read and issues: read"
        )
    links_workflow = read(".github/workflows/links.yml")
    if "--method get" not in links_workflow:
        errors.append("links workflow must use lychee's supported single GET method")
    if "--exclude-private" not in links_workflow:
        errors.append("links workflow must block requests to private network addresses")

    issue_first_paths = (
        "CONTRIBUTING.md",
        "CONTRIBUTING.en.md",
        ".github/pull_request_template.md",
    )
    for path in issue_first_paths:
        content = read(path)
        if "status: approved" not in content:
            errors.append(f"{path} must require an approved issue for a new listing")

    return errors


def main() -> int:
    try:
        errors = validate_repository()
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
        print(f"::error::{exc}")
        return 1

    for message in errors:
        print(f"::error::{message}")
    if errors:
        print(f"Repository contract failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Repository cross-file contracts are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
