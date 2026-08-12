# Inclusion Criteria and Evidence Standards

[简体中文](CRITERIA.md) · English

This document defines a consistent eligibility test for candidate projects. C1–C5
are cumulative gates: a project is not eligible if any one of them fails. D1–D5
are completeness requirements for each listing: a project cannot enter the
showcase until every field is present.

## Quick Decision Guide

| Outcome | Conditions |
| --- | --- |
| Accept | C1–C5 all pass, D1–D5 are complete, and no scope boundary is violated |
| More information needed | No contrary evidence has been found, but public evidence for one or more requirements is insufficient and the submitter can reasonably provide it |
| Reject | Any C requirement clearly fails, information conflicts, public verification is impossible, or the project is out of scope |

Stars, funding, author reputation, use of a popular AI tool, and promotional
reach never lower the bar.

## Scope Boundaries

- P1: The Showcase itself exists only as a GitHub repository. No standalone
  website will be built for it. Public experience URLs for candidate products
  are not affected by this restriction.
- P2: AI coding tools, IDEs, editors, plugins, and models are not eligible.
- P3: Only strong products genuinely completed with substantial AI coding
  involvement, available for public use, and backed by public source code are
  eligible.
- P4: Simplified Chinese is the primary language, with key content also
  available in English.

Component libraries, SDKs, frameworks, templates, starters, prompt collections,
tutorials, resource lists, and standalone datasets are likewise not considered
"finished, runnable software products."

## C1 | Public Experience

**Pass conditions:**

- A publicly accessible product, online experience, or demo exists.
- A reviewer can access it over the public internet and verify at least one flow
  that represents the product's core value.
- If an account is required, registration must be open and must not depend on a
  private invitation. If the product is paid, a publicly verifiable product demo
  must still be available.

**Evidence to record:**

- The canonical experience URL.
- The verification date.
- The core flow that was tested.
- Any registration, regional, or device restrictions.

**Examples that fail:**

- Only screenshots, a video, a design mockup, or a product landing page is
  available, with no interactive demo.
- The link requires private access approval or has been unavailable for an
  extended period.
- The page loads, but the core flow is entirely unusable and no public demo is
  available as an alternative.

## C2 | Public Source Code

**Pass conditions:**

- A source-code repository is viewable without special authorization.
- The repository contains the primary implementation of the online product or
  demo.
- Its code, project documentation, and build structure provide enough evidence
  to establish that the repository corresponds to the product.

**Evidence to record:**

- The canonical repository URL.
- The verification date and repository visibility.
- An explanation of how the publicly available product version corresponds to
  the source version.
- License status as a factual note only. A missing license does not, by itself,
  determine whether C2 passes.

**Examples that fail:**

- The repository is private or offers only a request-access link.
- The repository contains only a README, marketing page, screenshots, an
  archive, or compiled artifacts.
- The public repository is clearly unrelated to the online product and the
  submitter cannot explain the discrepancy.

## C3 | Substantial AI Involvement

**Pass conditions:**

- Through natural-language collaboration, AI carried out most of the
  implementation of the product's core feature code.
- Development included multiple rounds of conversational iteration around the
  design, implementation, debugging, or refactoring of core features.
- The submitter clearly describes the AI tools used, depth of involvement,
  typical collaboration workflow, and the human developer's main
  responsibilities.
- At least one form of publicly verifiable process evidence exists.

**Acceptable evidence:**

- Development notes, AI collaboration records, or a project retrospective in
  the repository.
- Public issues, pull requests, commit messages, or development logs connected
  to the core implementation.
- Redacted process records that retain context and can be connected to core
  features.
- A specific public account by the author of how the product was developed,
  provided it does not conflict with the source code or project timeline.

**The following do not count as substantial involvement:**

- Using AI only to write documentation, a README, or comments.
- Using AI only to add tests, fix a small number of bugs, or provide local code
  completion.
- Using AI only to generate images, copy, audio, or other assets.
- Calling an AI model at product runtime without evidence that AI participated
  in implementing the primary codebase.
- Merely claiming "100% AI-built" or naming tools without explaining the depth
  of involvement and providing process evidence.

Do not infer C3 from code style. Automation may check that required fields and
evidence links exist, but the final decision must be made by a maintainer.

## C4 | Completeness, Utility, or Innovation

**Pass conditions:**

The product must first meet a minimum level of completeness:

- Its core flow works in practice.
- It is more than a landing page, login screen, empty dashboard, or collection
  of nonfunctional buttons.
- Known limitations do not prevent a reviewer from understanding and verifying
  its main value.

Beyond that minimum, the product must satisfy at least one of the following,
with evidence:

- **Utility:** It solves a real problem for a clearly identified user and use
  case.
- **Innovation:** It demonstrates a meaningful idea in its interaction design,
  workflow, technical combination, or service model.
- **Completeness:** Its core features form a coherent experience, with content,
  error handling, and basic usability suitable for continued public display.

**Examples that fail:**

- A concept only, course placeholder, hackathon shell, or product whose core
  flow cannot be completed.
- A value proposition consisting only of unverifiable claims such as "smarter"
  or "industry-disrupting."
- Primary features that materially contradict the public description.

C4 does not impose a minimum number of Stars, users, or revenue. New projects
must not be excluded merely because they have not yet attracted attention.

## C5 | Authentic and Verifiable Information

**Pass conditions:**

- The product name, experience URL, source repository, author statements, and
  supporting evidence are mutually consistent.
- Material claims have public sources and can be reproduced at the time of
  review.
- The submitter discloses any authorship, employment, investment, or promotional
  relationship with the project.
- There is no impersonation, fabricated metric, false attribution, or concealed
  material access restriction.

**Verification actions:**

- Open the experience and source URLs rather than relying only on screenshots.
- Compare product names, features, and version information.
- Confirm that the AI-involvement evidence describes the core implementation of
  this product.
- Mark information that cannot be verified as "unverified"; do not rewrite it
  as fact.

**Examples that fail:**

- Project information conflicts and no reasonable explanation is available.
- Someone else's product or source code is presented as the submitter's own
  work.
- A material claim is supported only by an untraceable screenshot or marketing
  copy.
- Verification would require a reviewer to join a private group, sign an NDA,
  or receive private files.

## D1–D5 | Listing Fields

| ID | Required content | Acceptable | Not acceptable |
| --- | --- | --- | --- |
| D1 | Problem the product solves | Identifies the target user, context, and problem | "An AI product that will change the future" |
| D2 | Core features and real value | Describes 2–4 shipped core features and the value of each | Lists every planned feature or gives only slogans |
| D3 | Primary technology stack | Names 3–8 primary technologies used by the product | Provides a full dependency dump or omits a critical layer |
| D4 | AI's role in development | Gives the tools, depth, typical workflow, and evidence | "Built with AI" |
| D5 | Online experience and source URLs | Provides two public, direct, canonical URLs | Gives a search-results page, a shortened link, or only one of the two URLs |

## Evidence Safety

- Do not submit API keys, access tokens, passwords, private-repository content,
  or complete private conversations.
- Redact personal identifiers, customer data, and third-party secrets before
  sharing screenshots or development records.
- Maintainers must not be asked to download executable files from unknown
  sources.
- Submitters must have the right to publish all evidence they provide.

## Re-review Triggers

Recheck the relevant criteria when any of the following occurs after a project
has been listed:

- The experience repeatedly becomes unavailable or its core flow stops working
  (C1).
- The source repository becomes private, is deleted, or no longer contains the
  primary implementation (C2).
- AI-involvement evidence is withdrawn, disproved, or no longer corresponds to
  the project (C3 / C5).
- The product regresses to a concept page or its value cannot be verified over
  an extended period (C4).
- Impersonation, false attribution, fabricated metrics, or material factual
  conflicts are discovered (C5).
- Project changes make any of D1–D5 inaccurate or incomplete.
