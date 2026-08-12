#!/usr/bin/env python3
"""Render the canonical catalog into generated regions of both README files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote

from validate_catalog import (
    CatalogLoadError,
    DEFAULT_DATA,
    ROOT,
    load_catalog,
    validate_catalog,
)


START_MARKER = "<!-- catalog:start -->"
END_MARKER = "<!-- catalog:end -->"
DEFAULT_ZH_README = ROOT / "README.md"
DEFAULT_EN_README = ROOT / "README.en.md"
LOCALE_CONFIG = {
    "zh-CN": {
        "empty": "_暂无收录项目。_",
        "problem": "解决的问题（D1）",
        "features": "核心功能（D2）",
        "value": "实际价值（C4 / D2）",
        "stack": "主要技术栈（D3）",
        "ai": "AI 开发角色（C3 / D4）",
        "quality": "完成度与质量证据（C4）",
        "links": "公开地址（C1 / C2 / D5）",
        "verify": "真实性核验（C5）",
        "added": "收录日期",
        "demo": "在线体验",
        "source": "源码仓库",
        "ai_evidence": "AI 证据",
        "verification_source": "核验来源",
        "review_issue": "审核记录",
        "verified_on": "核验于",
        "tools": "工具",
        "depth": "参与深度",
        "workflow": "协作方式",
        "separator": "；",
    },
    "en": {
        "empty": "_No projects have been listed yet._",
        "problem": "Problem (D1)",
        "features": "Core features (D2)",
        "value": "Practical value (C4 / D2)",
        "stack": "Main stack (D3)",
        "ai": "AI development role (C3 / D4)",
        "quality": "Completion and quality evidence (C4)",
        "links": "Public links (C1 / C2 / D5)",
        "verify": "Verification (C5)",
        "added": "Listed on",
        "demo": "Live demo",
        "source": "Source repository",
        "ai_evidence": "AI evidence",
        "verification_source": "Verification source",
        "review_issue": "Review issue",
        "verified_on": "verified on",
        "tools": "tools",
        "depth": "depth",
        "workflow": "workflow",
        "separator": "; ",
    },
}
DEPTH_LABELS = {
    "core-code-majority-ai": {
        "zh-CN": "核心功能代码主要由 AI 生成并迭代",
        "en": "AI generated and iterated most core feature code",
    },
    "natural-language-driven-core": {
        "zh-CN": "以自然语言驱动完成主体开发",
        "en": "Natural-language-driven implementation of the core product",
    },
}


def _inline(value: str) -> str:
    """Escape untrusted data for a single Markdown text line."""
    compact = " ".join(value.split())
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", compact)


def _block_text(value: str) -> str:
    """Escape Markdown constructs when catalog text occupies its own line."""
    safe = _inline(value)
    if re.match(r"^(?:#{1,6}|[-+])(?:\s|$)", safe):
        return "\\" + safe
    if re.fullmatch(r"(?:-\s*){3,}", safe):
        return "\\" + safe
    if re.match(r"^~{3,}", safe) or re.fullmatch(r"={3,}", safe):
        return "\\" + safe
    return re.sub(r"^(\d+)([.)])(\s)", r"\1\\\2\3", safe)


def _code_span(value: str) -> str:
    compact = " ".join(value.split())
    runs = [len(match.group(0)) for match in re.finditer(r"`+", compact)]
    fence = "`" * (max(runs, default=0) + 1)
    padding = " " if compact.startswith("`") or compact.endswith("`") else ""
    return f"{fence}{padding}{compact}{padding}{fence}"


def _link(label: str, url: str) -> str:
    safe_url = quote(url, safe=":/?#@!$&'*+,;=%")
    return f"[{_inline(label)}]({safe_url})"


def _numbered_links(prefix: str, urls: list[str]) -> str:
    return " · ".join(
        _link(f"{prefix} {index}", url)
        for index, url in enumerate(urls, start=1)
    )


def _localized(value: dict[str, str], locale: str) -> str:
    return _inline(value[locale])


def _render_project(project: dict[str, Any], locale: str) -> list[str]:
    labels = LOCALE_CONFIG[locale]
    separator = labels["separator"]
    features = separator.join(
        _localized(feature, locale) for feature in project["features"]
    )
    stack = ", ".join(_code_span(item) for item in project["tech_stack"])
    tools = ", ".join(_code_span(item) for item in project["ai_role"]["tools"])
    depth = _inline(DEPTH_LABELS[project["ai_role"]["depth"]][locale])
    evidence = _numbered_links(
        labels["ai_evidence"],
        project["ai_role"]["evidence_urls"],
    )
    public_links = " · ".join(
        (
            _link(labels["demo"], project["demo_url"]),
            _link(labels["source"], project["source_url"]),
        )
    )
    verification_links = _numbered_links(
        labels["verification_source"],
        project["verification"]["sources"],
    )
    review_issue = _link(
        labels["review_issue"],
        project["verification"]["review_issue_url"],
    )
    verified_on = _inline(project["verification"]["verified_on"])

    return [
        f"<!-- project:{project['id']} -->",
        f"##### {_localized(project['name'], locale)}",
        "",
        f"- **{labels['problem']}：** {_localized(project['problem'], locale)}"
        if locale == "zh-CN"
        else f"- **{labels['problem']}:** {_localized(project['problem'], locale)}",
        f"- **{labels['features']}：** {features}"
        if locale == "zh-CN"
        else f"- **{labels['features']}:** {features}",
        f"- **{labels['value']}：** {_localized(project['value'], locale)}"
        if locale == "zh-CN"
        else f"- **{labels['value']}:** {_localized(project['value'], locale)}",
        f"- **{labels['stack']}：** {stack}"
        if locale == "zh-CN"
        else f"- **{labels['stack']}:** {stack}",
        (
            f"- **{labels['ai']}：** {labels['tools']}：{tools}；"
            f"{labels['depth']}：{depth}；{labels['workflow']}："
            f"{_localized(project['ai_role']['workflow'], locale)}；{evidence}"
            if locale == "zh-CN"
            else f"- **{labels['ai']}:** {labels['tools']}: {tools}; "
            f"{labels['depth']}: {depth}; {labels['workflow']}: "
            f"{_localized(project['ai_role']['workflow'], locale)}; {evidence}"
        ),
        f"- **{labels['quality']}：** {_localized(project['quality_evidence'], locale)}"
        if locale == "zh-CN"
        else f"- **{labels['quality']}:** {_localized(project['quality_evidence'], locale)}",
        f"- **{labels['links']}：** {public_links}"
        if locale == "zh-CN"
        else f"- **{labels['links']}:** {public_links}",
        (
            f"- **{labels['verify']}：** {verification_links} · {review_issue}；"
            f"{labels['verified_on']} {verified_on}"
            if locale == "zh-CN"
            else f"- **{labels['verify']}:** {verification_links} · {review_issue}; "
            f"{labels['verified_on']} {verified_on}"
        ),
        f"- **{labels['added']}：** {_inline(project['added_on'])}"
        if locale == "zh-CN"
        else f"- **{labels['added']}:** {_inline(project['added_on'])}",
    ]


def render_catalog(data: dict[str, Any], locale: str) -> str:
    """Render only accepted projects; empty catalogs produce a stable placeholder."""
    projects = data["projects"]
    if not projects:
        return LOCALE_CONFIG[locale]["empty"]

    lines: list[str] = []
    for category in data["categories"]:
        category_projects = [
            project
            for project in projects
            if project["primary_category"] == category["id"]
        ]
        if not category_projects:
            continue
        if lines:
            lines.append("")
        lines.extend(
            (
                f"### {_localized(category['name'], locale)}",
                "",
                _block_text(category["description"][locale]),
            )
        )

        for subcategory in category["subcategories"]:
            subcategory_projects = [
                project
                for project in category_projects
                if project["secondary_category"] == subcategory["id"]
            ]
            if not subcategory_projects:
                continue
            lines.extend(
                (
                    "",
                    f"#### {_localized(subcategory['name'], locale)}",
                    "",
                    _block_text(subcategory["description"][locale]),
                )
            )
            for project in subcategory_projects:
                lines.append("")
                lines.extend(_render_project(project, locale))

    return "\n".join(lines).rstrip()


def replace_generated_region(document: str, generated: str, path: Path) -> str:
    """Replace exactly one catalog region while preserving all authored content."""
    start_count = document.count(START_MARKER)
    end_count = document.count(END_MARKER)
    if start_count != 1 or end_count != 1:
        raise ValueError(
            f"{path}: expected exactly one {START_MARKER!r} and one "
            f"{END_MARKER!r}; found {start_count} and {end_count}"
        )

    start = document.index(START_MARKER)
    content_start = start + len(START_MARKER)
    end = document.index(END_MARKER)
    if end < content_start:
        raise ValueError(f"{path}: catalog end marker appears before start marker")

    return (
        document[:content_start]
        + "\n"
        + generated.rstrip()
        + "\n"
        + document[end:]
    )


def _read_readme(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ValueError(f"{path}: file is missing") from exc


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if README output is stale")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--zh-readme", type=Path, default=DEFAULT_ZH_README)
    parser.add_argument("--en-readme", type=Path, default=DEFAULT_EN_README)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        data = load_catalog(args.data)
    except CatalogLoadError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    errors = validate_catalog(data)
    if errors:
        for message in errors:
            print(f"error: {message}", file=sys.stderr)
        print("Refusing to render an invalid catalog.", file=sys.stderr)
        return 1

    targets = (
        (args.zh_readme, "zh-CN"),
        (args.en_readme, "en"),
    )
    planned: list[tuple[Path, str, str]] = []
    try:
        for path, locale in targets:
            current = _read_readme(path)
            desired = replace_generated_region(
                current,
                render_catalog(data, locale),
                path,
            )
            planned.append((path, current, desired))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    stale = [path for path, current, desired in planned if current != desired]
    if args.check:
        if stale:
            for path in stale:
                print(f"error: {path} has a stale generated catalog region", file=sys.stderr)
            print("Run: python scripts/render_catalog.py", file=sys.stderr)
            return 1
        print("README catalog regions are up to date.")
        return 0

    for path, current, desired in planned:
        if current != desired:
            path.write_text(desired, encoding="utf-8", newline="\n")
            print(f"Updated {path.relative_to(ROOT)}")
        else:
            print(f"Already up to date: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
