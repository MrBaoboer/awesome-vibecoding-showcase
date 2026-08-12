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
    "status: in-review",
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


def _form_block(document: str, field_id: str) -> str:
    match = re.search(
        rf"^  - type: [^\n]+\n    id: {re.escape(field_id)}\n"
        rf"(?P<body>.*?)(?=^  - type: |\Z)",
        document,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else ""


def _quoted_options(block: str) -> list[str]:
    return re.findall(r'^\s+- "([^"]+)"\s*$', block, flags=re.MULTILINE)


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

    for license_path in ("LICENSE", "LICENSING.md", "LICENSE-CONTENT"):
        if not (ROOT / license_path).is_file():
            errors.append(f"required licensing file is missing: {license_path}")
    if (ROOT / "LICENSE-CODE").exists():
        errors.append("legacy LICENSE-CODE must be removed; the standard MIT text belongs in LICENSE")
    mit_license = read("LICENSE") if (ROOT / "LICENSE").is_file() else ""
    for required_text in (
        "MIT License",
        "Permission is hereby granted, free of charge",
        'THE SOFTWARE IS PROVIDED "AS IS"',
    ):
        if required_text not in mit_license:
            errors.append(f"root LICENSE is missing standard MIT text: {required_text!r}")
    for readme_path in ("README.md", "README.en.md"):
        readme = read(readme_path)
        for target in ("LICENSE", "LICENSING.md", "LICENSE-CONTENT"):
            if f"({target})" not in readme:
                errors.append(f"{readme_path} must link to {target}")

    catalog = json.loads(read("data/projects.json"))
    primary_ids = [category["id"] for category in catalog["categories"]]
    category_pairs = [
        f"{category['id']} / {subcategory['id']}"
        for category in catalog["categories"]
        for subcategory in category["subcategories"]
    ]

    submission = read(".github/ISSUE_TEMPLATE/project-submission.yml")
    submission_name_match = re.search(r'^name: "([^"]+)"$', submission, re.MULTILINE)
    submission_name = submission_name_match.group(1) if submission_name_match else ""
    for readme_path in ("README.md", "README.en.md"):
        if f"**{submission_name}**" not in read(readme_path):
            errors.append(
                f"{readme_path} must use the exact project Issue Form name {submission_name!r}"
            )
    form_pairs = _quoted_options(_form_block(submission, "category_pair"))
    if form_pairs != category_pairs:
        errors.append("project submission secondary categories differ from catalog order")

    category_doc = read("docs/CATEGORIES.md")
    zh_readme = read("README.md")
    en_readme = read("README.en.md")
    for category_id in primary_ids:
        if f"`{category_id}`" not in category_doc:
            errors.append(f"docs/CATEGORIES.md is missing primary category {category_id}")
    for category in catalog["categories"]:
        if category["name"]["zh-CN"] not in zh_readme:
            errors.append(
                f"README.md is missing category name {category['name']['zh-CN']!r}"
            )
        if category["name"]["en"] not in en_readme:
            errors.append(
                f"README.en.md is missing category name {category['name']['en']!r}"
            )
    for pair in category_pairs:
        secondary_id = pair.split(" / ", 1)[1]
        if f"`{secondary_id}`" not in category_doc:
            errors.append(f"docs/CATEGORIES.md is missing secondary category {secondary_id}")

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
