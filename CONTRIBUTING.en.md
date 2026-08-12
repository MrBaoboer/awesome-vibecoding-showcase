# Contributing

Thank you for helping build `Awesome-VibeCoding-Showcase`. This repository showcases working software products whose core implementation was substantially created through natural-language collaboration with AI, and that have both a public experience and public source code.

Simplified Chinese is the primary maintenance language. English contributions are welcome, and key English guidance is maintained in this file.

## 1. Confirm the scope first

This showcase is built entirely within its GitHub repository; no separate website will be developed for the showcase. Candidate products may, and must, provide their own public experience URLs.

You may submit:

- a working software product that the public can try;
- a public repository containing the product's substantive source code;
- a product whose core features were largely implemented through natural-language collaboration with AI;
- truthful information supported by enough public evidence for independent review.

Do not submit:

- AI coding tools, IDEs, editors, plugins, or models;
- component libraries, templates, starters, prompt collections, tutorials, or resource lists;
- screenshots, designs, concepts, or promotional videos without a publicly accessible product or demo;
- projects without public source, or repositories containing only a landing page, documentation, or build artifacts;
- projects where AI was used only for documentation, comments, test completion, minor bug fixes, or asset generation.

## 2. Eligibility criteria

All five criteria are mandatory:

| ID | Mandatory condition | Minimum review evidence |
| --- | --- | --- |
| C1 | A publicly accessible product, demo, or online experience exists | A URL that a reviewer can open and use to verify the core flow |
| C2 | A public source repository exists | A repository URL exposing the substantive product implementation without special authorization |
| C3 | AI substantially participated in implementation | AI tools, depth of involvement, a typical collaboration method, and at least one public process artifact |
| C4 | The product has meaningful completeness, utility, or innovation | A reproducible core flow and evidence supporting at least one quality dimension |
| C5 | Information is truthful and verifiable | The product, source, submitter's explanation, and evidence corroborate one another |

See `docs/CRITERIA.en.md` for detailed interpretation and rejection examples.

## 3. Required project information

| ID | Display field | Requirement |
| --- | --- | --- |
| D1 | Problem solved | Identify the target user, context, and concrete problem |
| D2 | Core features and practical value | Describe only working features and explain their actual value |
| D3 | Main technology stack | List the main frontend, backend, data, and deployment technologies used by the product |
| D4 | AI's development role | State the tools, depth, typical natural-language workflow, and public evidence |
| D5 | Public experience and source URLs | Provide both URLs and keep them publicly accessible |

See `docs/PROJECT_FORMAT.md` for the display format.

## 4. Ways to contribute

### 4.1 Nominate a new project

1. Search existing entries and open issues to avoid duplicates.
2. Read `docs/CRITERIA.en.md` and `docs/CATEGORIES.en.md`.
3. Open the “Project submission” Issue Form.
4. Complete C1–C5 and D1–D5; do not paste marketing copy as the full submission.
5. Subscribe to the issue and add evidence in the same thread if it receives `status: needs-info`.

Do not open a PR for a new project before initial review. Once eligibility and display content are confirmed, the maintainer can create or invite the corresponding content PR.

### 4.2 Report an error, broken link, or removal concern

1. Use the “General issue” form.
2. Select the issue type and provide the project name, entry location, and public evidence.
3. For a factual project change, provide the applicable C1–C5 / D1–D5 information again.
4. Do not publish exploit details for a security issue. Identify the affected entry and use the repository's private security-reporting channel when available.

### 4.3 Update an existing project

Authors and community members may suggest updates, but factual changes need public sources. Please report:

- changes to the public experience or source URL (C1 / C2 / D5);
- changes to core features, value, or technology stack (D1–D3);
- stronger public evidence for AI participation (C3 / C5 / D4);
- a product going offline, source becoming private, or information being disproved (C1 / C2 / C5).

### 4.4 Open a pull request

1. Keep one PR focused on one purpose.
2. A new listing must link a project-submission issue carrying `status: approved`; documentation, translation, configuration, and other non-listing changes may explain why no issue is needed.
3. Use the PR template and complete C1–C5 / D1–D5 for project-related changes.
4. Select exactly one primary and one secondary category from `docs/CATEGORIES.en.md`, then maintain the listing in the canonical `data/projects.json`; do not edit generated README catalog regions directly.
5. Run `python scripts/render_catalog.py` and include the generated `README.md` and `README.en.md` changes.
6. Open the experience and source URLs yourself and record the core flow you verified.
7. Update the affected Chinese source content and key English content together.
8. Run the local checks below. Avoid unrelated reordering, mass formatting, or dependency changes.

```powershell
python scripts/validate_catalog.py
python scripts/validate_repository.py
python scripts/render_catalog.py --check
python -m unittest discover -s scripts -p "test_*.py"
```

Local checks validate fields, formatting, and review-Issue URL structure. CI on the real pull request also binds that URL to this repository and confirms that the Issue exists with an approval label.

See `data/README.md` for structured fields and an example; rendered output must follow `docs/PROJECT_FORMAT.md`.

## 5. Evidence

Acceptable public evidence includes:

- development notes or AI-collaboration records in the project repository;
- public issues, pull requests, or commit descriptions tied to core feature implementation;
- a public development log, technical retrospective, or redacted process record;
- reproducible product steps, public documentation, and release notes.

The following cannot prove C3 or C5 on their own:

- a claim that a product was “built with AI”;
- a list of AI tool names;
- code that merely looks AI-generated;
- unattributed screenshots, user counts, stars, or marketing claims;
- private chats or evidence available only after joining a private group.

Redact API keys, tokens, account details, private conversations, and personal information before sharing process evidence.

## 6. Classification

- Classify by the primary problem solved, not by technology or AI tool.
- Select one primary category and one of its three secondary categories.
- For a multi-purpose product, use the primary target user and core flow stated in public product documentation.
- Resolve edge cases with the category-specific rules in `docs/CATEGORIES.en.md` and record the reason in the issue.

## 7. Chinese and English synchronization

- Chinese is the source of truth for current facts and governance rules.
- A change to positioning, criteria, submission instructions, or required project fields must update the English counterpart in the same PR.
- If a contributor cannot provide the English update, the PR must say so and receive the `i18n` label. Unreviewed machine translation should not be copied in as final text.
- Do not translate product names, URLs, code, labels, or category slugs.

## 8. Review outcomes

The maintainer records decisions with `docs/REVIEW_CHECKLIST.md`. The state flow is `triage → needs-info | in-review → approved → listed`; an existing listing may move through `stale → removed`. Key outcomes are:

- `status: approved`: all C1–C5 pass and D1–D5 are complete;
- `status: needs-info`: evidence is incomplete but can reasonably be supplied;
- `status: declined`: at least one mandatory criterion fails or remains unverifiable;
- `status: removed`: an existing entry was removed after re-review.

Passing automation means only that no link, format, or required-field problem was detected. It does not replace human judgment for C3–C5.

## 9. Collaboration expectations

- Use reviewable evidence rather than author prominence, commercial relationships, or popularity.
- Disclose authorship, employment, investment, or promotional relationships with a candidate project.
- Accept consistency edits to descriptions, classification, and wording.
- Do not spam, repeatedly pressure maintainers, or offer payment, gifts, or cross-promotion for inclusion.

By contributing, you confirm that you may publish the submitted material and agree to its distribution under the repository's license.
