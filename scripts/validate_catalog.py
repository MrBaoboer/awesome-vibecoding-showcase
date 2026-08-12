#!/usr/bin/env python3
"""Validate the canonical showcase catalog using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from ipaddress import ip_address
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "projects.json"
DEFAULT_SCHEMA = ROOT / "schema" / "projects.schema.json"
SCHEMA_REFERENCE = "../schema/projects.schema.json"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ISO_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
LOCALES = ("zh-CN", "en")
AI_DEPTHS = {
    "core-code-majority-ai",
    "natural-language-driven-core",
}
FEATURE_ITEMS = (2, 4)
TECH_STACK_ITEMS = (3, 8)
EXPECTED_PRIMARY_IDS = (
    "productivity-collaboration",
    "business-operations",
    "education-knowledge",
    "data-decision",
    "creative-media",
    "health-lifestyle",
    "community-public-good",
    "games-entertainment",
)
EXPECTED_SECONDARY_IDS = {
    "productivity-collaboration": (
        "task-workflow",
        "communication-collaboration",
        "personal-productivity",
    ),
    "business-operations": (
        "commerce-sales",
        "finance-administration",
        "customer-service",
    ),
    "education-knowledge": (
        "learning-training",
        "research-reference",
        "knowledge-management",
    ),
    "data-decision": (
        "analytics-visualization",
        "planning-forecasting",
        "decision-support",
    ),
    "creative-media": (
        "writing-publishing",
        "design-visual",
        "audio-video",
    ),
    "health-lifestyle": (
        "health-wellness",
        "home-daily-life",
        "travel-local",
    ),
    "community-public-good": (
        "civic-public-service",
        "accessibility-inclusion",
        "community-nonprofit",
    ),
    "games-entertainment": (
        "games-interactive",
        "social-entertainment",
        "hobbies-fandom",
    ),
}

TOP_LEVEL_FIELDS = {"$schema", "schema_version", "categories", "projects"}
CATEGORY_FIELDS = {"id", "name", "description", "subcategories"}
SUBCATEGORY_FIELDS = {"id", "name", "description"}
PROJECT_FIELDS = {
    "id",
    "kind",
    "name",
    "primary_category",
    "secondary_category",
    "problem",
    "features",
    "value",
    "tech_stack",
    "ai_role",
    "demo_url",
    "source_url",
    "quality_evidence",
    "verification",
    "added_on",
}
AI_ROLE_FIELDS = {"tools", "depth", "workflow", "evidence_urls"}
VERIFICATION_FIELDS = {
    "sources",
    "review_issue_url",
    "submitter_attested",
    "verified_on",
}
SHOWCASE_REPOSITORY_NAME = "Awesome-VibeCoding-Showcase"
GITHUB_ISSUE_PATH = re.compile(
    r"^/(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/"
    r"(?P<repo>Awesome-VibeCoding-Showcase)/issues/"
    r"(?P<number>[1-9][0-9]*)$",
    re.IGNORECASE,
)
LEGACY_IPV4_HOST = re.compile(
    r"^(?:0x[0-9a-f]+|[0-9]+)(?:\.(?:0x[0-9a-f]+|[0-9]+))*$",
    re.IGNORECASE,
)


class CatalogLoadError(ValueError):
    """Raised when a JSON catalog or schema cannot be loaded."""


def load_json(path: Path) -> Any:
    """Load UTF-8 JSON and return a useful error without a Python traceback."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CatalogLoadError(f"{path}: file is missing") from exc
    except json.JSONDecodeError as exc:
        raise CatalogLoadError(
            f"{path}:{exc.lineno}:{exc.colno}: invalid JSON: {exc.msg}"
        ) from exc


def load_catalog(path: Path = DEFAULT_DATA) -> dict[str, Any]:
    """Load a catalog object; structural validation is a separate operation."""
    value = load_json(path)
    if not isinstance(value, dict):
        raise CatalogLoadError(f"{path}: top level must be a JSON object")
    return value


def validate_schema_contract(schema: Any) -> list[str]:
    """Check that the editor-facing Schema mirrors authoritative runtime rules."""
    errors: list[str] = []
    if not isinstance(schema, dict):
        return ["schema: top level must be an object (data contract)"]
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("schema: must declare JSON Schema draft 2020-12 (data contract)")
    try:
        definitions = schema["$defs"]
        project = definitions["project"]
        properties = project["properties"]
        verification = definitions["verification"]
        ai_role = definitions["aiRole"]

        expected_secondary = tuple(
            secondary
            for primary in EXPECTED_PRIMARY_IDS
            for secondary in EXPECTED_SECONDARY_IDS[primary]
        )
        checks = (
            (
                tuple(definitions["primaryCategory"]["properties"]["id"]["enum"]),
                EXPECTED_PRIMARY_IDS,
                "primary category enum",
            ),
            (
                tuple(properties["primary_category"]["enum"]),
                EXPECTED_PRIMARY_IDS,
                "project primary category enum",
            ),
            (
                tuple(definitions["secondaryCategory"]["properties"]["id"]["enum"]),
                expected_secondary,
                "secondary category enum",
            ),
            (
                tuple(properties["secondary_category"]["enum"]),
                expected_secondary,
                "project secondary category enum",
            ),
            (set(project["required"]), PROJECT_FIELDS, "project required fields"),
            (
                set(verification["required"]),
                VERIFICATION_FIELDS,
                "verification required fields",
            ),
            (set(ai_role["properties"]["depth"]["enum"]), AI_DEPTHS, "AI depth enum"),
            (
                (
                    properties["features"]["minItems"],
                    properties["features"]["maxItems"],
                ),
                FEATURE_ITEMS,
                "feature count",
            ),
            (
                (
                    properties["tech_stack"]["minItems"],
                    properties["tech_stack"]["maxItems"],
                ),
                TECH_STACK_ITEMS,
                "technology stack count",
            ),
            (
                (
                    ai_role["properties"]["evidence_urls"]["minItems"],
                    ai_role["properties"]["evidence_urls"]["maxItems"],
                ),
                (1, 8),
                "AI evidence URL count",
            ),
            (
                (
                    verification["properties"]["sources"]["minItems"],
                    verification["properties"]["sources"]["maxItems"],
                ),
                (1, 8),
                "verification source count",
            ),
        )
        for actual, expected, label in checks:
            if actual != expected:
                errors.append(
                    f"schema: {label} differs from runtime contract: "
                    f"expected {expected!r}, found {actual!r}"
                )

        schema_pairs = {}
        for rule in project["allOf"]:
            primary = rule["if"]["properties"]["primary_category"]["const"]
            secondaries = tuple(
                rule["then"]["properties"]["secondary_category"]["enum"]
            )
            schema_pairs[primary] = secondaries
        if schema_pairs != EXPECTED_SECONDARY_IDS:
            errors.append("schema: primary/secondary conditional pairs differ from runtime")
    except (KeyError, TypeError):
        errors.append("schema: required contract declarations are missing or malformed")
    return errors


def _canonical_host(raw_host: str) -> str | None:
    """Return an ASCII host suitable for security checks and comparisons."""
    if "%" in raw_host:
        return None
    normalized = unicodedata.normalize("NFKC", raw_host).rstrip(".").casefold()
    if not normalized:
        return None
    try:
        return ip_address(normalized).compressed.casefold()
    except ValueError:
        pass
    try:
        ascii_host = normalized.encode("idna").decode("ascii").rstrip(".").casefold()
    except UnicodeError:
        return None
    if not ascii_host or LEGACY_IPV4_HOST.fullmatch(ascii_host):
        # Browsers interpret decimal/octal/hex and shortened numeric hosts as IPv4.
        return None
    return ascii_host


def _normalized_url(value: str) -> str:
    """Normalize URLs for identity checks; fragments never create a new source."""
    parsed = urlsplit(value.strip())
    host = _canonical_host(parsed.hostname or "") or (parsed.hostname or "").casefold()
    host_for_netloc = f"[{host}]" if ":" in host else host
    port = parsed.port
    if port is not None and not (
        (parsed.scheme.casefold() == "http" and port == 80)
        or (parsed.scheme.casefold() == "https" and port == 443)
    ):
        host_for_netloc += f":{port}"
    return urlunsplit(
        (
            parsed.scheme.casefold(),
            host_for_netloc,
            parsed.path.rstrip("/"),
            parsed.query,
            "",
        )
    )


def _is_public_http_url(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    if any(character.isspace() for character in value):
        return False

    try:
        parsed = urlsplit(value.strip())
        host = _canonical_host(parsed.hostname or "")
        _ = parsed.port
    except (AttributeError, ValueError):
        return False

    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.netloc
        or parsed.username
        or parsed.password
        or host is None
    ):
        return False

    if (
        host == "localhost"
        or host.endswith(
            (
                ".localhost",
                ".local",
                ".internal",
                ".test",
                ".invalid",
                ".example",
            )
        )
        or host in {"example.com", "example.net", "example.org"}
    ):
        return False

    try:
        if not ip_address(host).is_global:
            return False
    except ValueError:
        pass

    return True


def parse_repository_full_name(value: str) -> tuple[str, str] | None:
    """Parse GitHub's ``owner/repository`` identifier without URL semantics."""
    if not isinstance(value, str) or value != value.strip():
        return None
    parts = value.split("/")
    if len(parts) != 2 or not all(parts):
        return None
    owner, repo = parts
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})", owner):
        return None
    if not re.fullmatch(r"[A-Za-z0-9._-]+", repo):
        return None
    return owner, repo


def parse_review_issue_url(value: Any) -> tuple[str, str, int] | None:
    """Return a canonical, case-insensitive GitHub review Issue identity."""
    if not isinstance(value, str) or value != value.strip():
        return None
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except (AttributeError, ValueError):
        return None
    if (
        parsed.scheme.casefold() != "https"
        or _canonical_host(parsed.hostname or "") != "github.com"
        or parsed.username
        or parsed.password
        or port not in (None, 443)
        or parsed.query
        or parsed.fragment
    ):
        return None
    match = GITHUB_ISSUE_PATH.fullmatch(parsed.path)
    if match is None:
        return None
    return (
        match.group("owner").casefold(),
        match.group("repo").casefold(),
        int(match.group("number")),
    )


def validate_catalog(
    data: Any,
    *,
    today: date | None = None,
    repository_full_name: str | None = None,
) -> list[str]:
    """Return all catalog errors; an empty project list is intentionally valid."""
    errors: list[str] = []
    current_date = today or date.today()
    expected_repository: tuple[str, str] | None = None

    if repository_full_name is not None:
        parsed_repository = parse_repository_full_name(repository_full_name)
        if parsed_repository is None:
            errors.append(
                "repository: must be a valid GitHub owner/repository name "
                "(workflow configuration)"
            )
        else:
            expected_repository = tuple(part.casefold() for part in parsed_repository)
            if expected_repository[1] != SHOWCASE_REPOSITORY_NAME.casefold():
                errors.append(
                    "repository: repository name must be "
                    f"{SHOWCASE_REPOSITORY_NAME!r} (workflow configuration)"
                )

    def add(path: str, message: str, requirement: str) -> None:
        errors.append(f"{path}: {message} ({requirement})")

    def check_fields(
        value: Any,
        expected: set[str],
        path: str,
        requirement: str,
    ) -> bool:
        if not isinstance(value, dict):
            add(path, "must be an object", requirement)
            return False
        missing = sorted(expected - set(value))
        unknown = sorted(set(value) - expected)
        if missing:
            add(path, f"missing fields: {', '.join(missing)}", requirement)
        if unknown:
            add(path, f"unknown fields: {', '.join(unknown)}", requirement)
        return not missing

    def check_slug(value: Any, path: str, requirement: str) -> str | None:
        if not isinstance(value, str) or not SLUG.fullmatch(value):
            add(path, "must be a lowercase kebab-case ID", requirement)
            return None
        return value

    def check_text(
        value: Any,
        path: str,
        minimum: int,
        requirement: str,
    ) -> str | None:
        if not isinstance(value, str) or len(value.strip()) < minimum:
            add(
                path,
                f"must be a non-blank string of at least {minimum} characters",
                requirement,
            )
            return None
        if "\n" in value or "\r" in value:
            add(path, "must be a single-line string", requirement)
            return None
        return value.strip()

    def check_localized(
        value: Any,
        path: str,
        minimum: int,
        requirement: str,
    ) -> dict[str, str] | None:
        if not isinstance(value, dict):
            add(path, "must be an object with zh-CN and en", requirement)
            return None
        keys = set(value)
        if keys != set(LOCALES):
            add(path, "must contain exactly zh-CN and en", requirement)
        result: dict[str, str] = {}
        for locale in LOCALES:
            checked = check_text(
                value.get(locale),
                f"{path}.{locale}",
                minimum,
                requirement,
            )
            if checked is not None:
                result[locale] = checked
        return result if len(result) == len(LOCALES) else None

    def check_string_list(
        value: Any,
        path: str,
        minimum_items: int,
        maximum_items: int,
        minimum_length: int,
        requirement: str,
    ) -> list[str]:
        if not isinstance(value, list) or not (
            minimum_items <= len(value) <= maximum_items
        ):
            add(
                path,
                f"must contain {minimum_items}-{maximum_items} items",
                requirement,
            )
            return []
        result: list[str] = []
        for index, item in enumerate(value):
            checked = check_text(
                item,
                f"{path}[{index}]",
                minimum_length,
                requirement,
            )
            if checked is not None:
                result.append(checked)
        if len({item.casefold() for item in result}) != len(result):
            add(path, "must not contain duplicate values", requirement)
        return result

    def check_url(value: Any, path: str, requirement: str) -> str | None:
        if not _is_public_http_url(value):
            add(
                path,
                "must be a public http(s) URL without credentials or placeholders",
                requirement,
            )
            return None
        return value.strip()

    def check_url_list(
        value: Any,
        path: str,
        minimum_items: int,
        maximum_items: int,
        requirement: str,
    ) -> list[str]:
        if not isinstance(value, list) or not (
            minimum_items <= len(value) <= maximum_items
        ):
            add(
                path,
                f"must contain {minimum_items}-{maximum_items} URLs",
                requirement,
            )
            return []
        result: list[str] = []
        for index, item in enumerate(value):
            checked = check_url(item, f"{path}[{index}]", requirement)
            if checked is not None:
                result.append(checked)
        normalized = [_normalized_url(item) for item in result]
        if len(set(normalized)) != len(normalized):
            add(path, "must not contain duplicate URLs", requirement)
        return result

    def check_date(value: Any, path: str, requirement: str) -> date | None:
        if not isinstance(value, str) or not ISO_DATE.fullmatch(value):
            add(path, "must use YYYY-MM-DD", requirement)
            return None
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            add(path, "must be a real calendar date", requirement)
            return None
        if parsed > current_date:
            add(path, "cannot be in the future", requirement)
        return parsed

    if not check_fields(data, TOP_LEVEL_FIELDS, "$", "C1-C5 / D1-D5"):
        return errors
    if data.get("$schema") != SCHEMA_REFERENCE:
        add("$.$schema", f"must equal {SCHEMA_REFERENCE!r}", "data contract")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        add("$.schema_version", "must equal integer 1", "data contract")

    categories = data.get("categories")
    category_pairs: set[tuple[str, str]] = set()
    primary_ids: list[str] = []
    secondary_ids: set[str] = set()
    category_names = {locale: set() for locale in LOCALES}
    subcategory_names = {locale: set() for locale in LOCALES}

    if not isinstance(categories, list):
        add("$.categories", "must be an array", "classification")
        categories = []
    elif len(categories) != len(EXPECTED_PRIMARY_IDS):
        add(
            "$.categories",
            f"must contain exactly {len(EXPECTED_PRIMARY_IDS)} primary categories",
            "classification",
        )

    for category_index, category in enumerate(categories):
        path = f"$.categories[{category_index}]"
        if not check_fields(category, CATEGORY_FIELDS, path, "classification"):
            continue
        primary_id = check_slug(category.get("id"), f"{path}.id", "classification")
        if primary_id is not None:
            primary_ids.append(primary_id)

        names = check_localized(category.get("name"), f"{path}.name", 2, "classification")
        check_localized(
            category.get("description"),
            f"{path}.description",
            8,
            "classification",
        )
        if names:
            for locale, name in names.items():
                key = name.casefold()
                if key in category_names[locale]:
                    add(f"{path}.name.{locale}", "duplicates another name", "classification")
                category_names[locale].add(key)

        subcategories = category.get("subcategories")
        if not isinstance(subcategories, list) or len(subcategories) != 3:
            add(
                f"{path}.subcategories",
                "must contain exactly 3 secondary categories",
                "classification",
            )
            continue

        local_secondary_ids: list[str] = []
        for subcategory_index, subcategory in enumerate(subcategories):
            subpath = f"{path}.subcategories[{subcategory_index}]"
            if not check_fields(
                subcategory,
                SUBCATEGORY_FIELDS,
                subpath,
                "classification",
            ):
                continue
            secondary_id = check_slug(
                subcategory.get("id"),
                f"{subpath}.id",
                "classification",
            )
            subnames = check_localized(
                subcategory.get("name"),
                f"{subpath}.name",
                2,
                "classification",
            )
            check_localized(
                subcategory.get("description"),
                f"{subpath}.description",
                8,
                "classification",
            )
            if secondary_id is not None:
                local_secondary_ids.append(secondary_id)
                if secondary_id in secondary_ids:
                    add(f"{subpath}.id", "duplicates another ID", "classification")
                secondary_ids.add(secondary_id)
                if primary_id is not None:
                    category_pairs.add((primary_id, secondary_id))
            if subnames:
                for locale, name in subnames.items():
                    key = name.casefold()
                    if key in subcategory_names[locale]:
                        add(
                            f"{subpath}.name.{locale}",
                            "duplicates another name",
                            "classification",
                        )
                    subcategory_names[locale].add(key)

        if (
            primary_id in EXPECTED_SECONDARY_IDS
            and tuple(local_secondary_ids) != EXPECTED_SECONDARY_IDS[primary_id]
        ):
            add(
                f"{path}.subcategories",
                "secondary IDs and order must be: "
                + ", ".join(EXPECTED_SECONDARY_IDS[primary_id]),
                "classification",
            )

    if tuple(primary_ids) != EXPECTED_PRIMARY_IDS:
        add(
            "$.categories",
            "primary IDs and order must be: " + ", ".join(EXPECTED_PRIMARY_IDS),
            "classification",
        )

    projects = data.get("projects")
    if not isinstance(projects, list):
        add("$.projects", "must be an array", "C1-C5 / D1-D5")
        projects = []

    seen_ids: set[str] = set()
    seen_demo_urls: set[str] = set()
    seen_source_urls: set[str] = set()
    seen_review_issues: set[tuple[str, str, int]] = set()
    project_names = {locale: set() for locale in LOCALES}
    sortable: list[tuple[int, int, str]] = []

    for project_index, project in enumerate(projects):
        path = f"$.projects[{project_index}]"
        if not check_fields(project, PROJECT_FIELDS, path, "C1-C5 / D1-D5"):
            continue

        project_id = check_slug(project.get("id"), f"{path}.id", "C5")
        if project_id is not None:
            if project_id in seen_ids:
                add(f"{path}.id", "duplicates another project ID", "C5")
            seen_ids.add(project_id)

        if project.get("kind") != "application":
            add(
                f"{path}.kind",
                "must equal 'application'; tools, IDEs, plugins, and models are excluded",
                "P2 / P3",
            )

        names = check_localized(project.get("name"), f"{path}.name", 2, "C5")
        if names:
            for locale, name in names.items():
                key = name.casefold()
                if key in project_names[locale]:
                    add(f"{path}.name.{locale}", "duplicates another name", "C5")
                project_names[locale].add(key)

        primary_id = check_slug(
            project.get("primary_category"),
            f"{path}.primary_category",
            "C4",
        )
        secondary_id = check_slug(
            project.get("secondary_category"),
            f"{path}.secondary_category",
            "C4",
        )
        if (
            primary_id is not None
            and secondary_id is not None
            and (primary_id, secondary_id) not in category_pairs
        ):
            add(
                f"{path}.secondary_category",
                "does not belong to the selected primary category",
                "C4",
            )

        check_localized(project.get("problem"), f"{path}.problem", 12, "D1")

        features = project.get("features")
        if not isinstance(features, list) or not (
            FEATURE_ITEMS[0] <= len(features) <= FEATURE_ITEMS[1]
        ):
            add(
                f"{path}.features",
                f"must contain {FEATURE_ITEMS[0]}-{FEATURE_ITEMS[1]} items",
                "D2",
            )
        else:
            localized_features: dict[str, set[str]] = {
                locale: set() for locale in LOCALES
            }
            for feature_index, feature in enumerate(features):
                feature_path = f"{path}.features[{feature_index}]"
                checked = check_localized(feature, feature_path, 4, "D2")
                if checked:
                    for locale, text_value in checked.items():
                        key = text_value.casefold()
                        if key in localized_features[locale]:
                            add(
                                f"{feature_path}.{locale}",
                                "duplicates another feature",
                                "D2",
                            )
                        localized_features[locale].add(key)

        check_localized(project.get("value"), f"{path}.value", 12, "C4 / D2")
        check_string_list(
            project.get("tech_stack"),
            f"{path}.tech_stack",
            TECH_STACK_ITEMS[0],
            TECH_STACK_ITEMS[1],
            1,
            "D3",
        )

        ai_role = project.get("ai_role")
        if check_fields(ai_role, AI_ROLE_FIELDS, f"{path}.ai_role", "C3 / D4"):
            check_string_list(
                ai_role.get("tools"),
                f"{path}.ai_role.tools",
                1,
                8,
                1,
                "D4",
            )
            if ai_role.get("depth") not in AI_DEPTHS:
                add(
                    f"{path}.ai_role.depth",
                    "must be one of: " + ", ".join(sorted(AI_DEPTHS)),
                    "C3 / D4",
                )
            check_localized(
                ai_role.get("workflow"),
                f"{path}.ai_role.workflow",
                20,
                "C3 / D4",
            )
            check_url_list(
                ai_role.get("evidence_urls"),
                f"{path}.ai_role.evidence_urls",
                1,
                8,
                "C3 / C5 / D4",
            )

        demo_url = check_url(project.get("demo_url"), f"{path}.demo_url", "C1 / D5")
        source_url = check_url(
            project.get("source_url"),
            f"{path}.source_url",
            "C2 / D5",
        )
        if demo_url:
            normalized = _normalized_url(demo_url)
            if normalized in seen_demo_urls:
                add(f"{path}.demo_url", "duplicates another project", "C1 / C5 / D5")
            seen_demo_urls.add(normalized)
        if source_url:
            normalized = _normalized_url(source_url)
            if normalized in seen_source_urls:
                add(
                    f"{path}.source_url",
                    "duplicates another project",
                    "C2 / C5 / D5",
                )
            seen_source_urls.add(normalized)
        if (
            demo_url
            and source_url
            and _normalized_url(demo_url) == _normalized_url(source_url)
        ):
            add(
                f"{path}.demo_url",
                "must differ from source_url",
                "C1 / C2 / D5",
            )

        check_localized(
            project.get("quality_evidence"),
            f"{path}.quality_evidence",
            12,
            "C4",
        )

        verification = project.get("verification")
        if check_fields(
            verification,
            VERIFICATION_FIELDS,
            f"{path}.verification",
            "C5",
        ):
            verification_urls = check_url_list(
                verification.get("sources"),
                f"{path}.verification.sources",
                1,
                8,
                "C5",
            )
            review_issue_url = check_url(
                verification.get("review_issue_url"),
                f"{path}.verification.review_issue_url",
                "C5",
            )
            if review_issue_url is not None:
                review_issue = parse_review_issue_url(review_issue_url)
                if review_issue is None:
                    add(
                        f"{path}.verification.review_issue_url",
                        "must match https://github.com/OWNER/"
                        "Awesome-VibeCoding-Showcase/issues/NUMBER",
                        "C5",
                    )
                else:
                    issue_repository = review_issue[:2]
                    if (
                        expected_repository is not None
                        and issue_repository != expected_repository
                    ):
                        add(
                            f"{path}.verification.review_issue_url",
                            "must belong to the current repository "
                            f"{repository_full_name}",
                            "C5",
                        )
                    if review_issue in seen_review_issues:
                        add(
                            f"{path}.verification.review_issue_url",
                            "duplicates another project's one-project review issue",
                            "C5",
                        )
                    seen_review_issues.add(review_issue)
            known_urls = {
                _normalized_url(item)
                for item in (demo_url, source_url)
                if item is not None
            }
            if verification_urls and not any(
                _normalized_url(item) not in known_urls
                for item in verification_urls
            ):
                add(
                    f"{path}.verification.sources",
                    "needs at least one source beyond demo_url and source_url",
                    "C5",
                )
            if verification.get("submitter_attested") is not True:
                add(
                    f"{path}.verification.submitter_attested",
                    "must be true",
                    "C3 / C5",
                )
            check_date(
                verification.get("verified_on"),
                f"{path}.verification.verified_on",
                "C5",
            )

        added_on = check_date(project.get("added_on"), f"{path}.added_on", "C5")
        if added_on is not None and project_id is not None:
            sortable.append((project_index, added_on.toordinal(), project_id))

    if len(sortable) == len(projects):
        current_order = [item[0] for item in sortable]
        expected_order = [
            item[0]
            for item in sorted(sortable, key=lambda item: (-item[1], item[2]))
        ]
        if current_order != expected_order:
            add(
                "$.projects",
                "must be sorted by added_on descending, then id ascending",
                "display order",
            )

    return errors


def _escape_annotation(message: str) -> str:
    return (
        message.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument(
        "--repository",
        metavar="OWNER/REPOSITORY",
        help="bind review Issue URLs to this GitHub repository",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        schema = load_json(args.schema)
        data = load_catalog(args.data)
    except CatalogLoadError as exc:
        print(f"::error::{_escape_annotation(str(exc))}")
        return 1

    errors = validate_schema_contract(schema)
    errors.extend(validate_catalog(data, repository_full_name=args.repository))

    for message in errors:
        print(f"::error::{_escape_annotation(message)}")
    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Validated {len(data['categories'])} primary categories and "
        f"{len(data['projects'])} project(s); all machine-checkable rules pass."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
