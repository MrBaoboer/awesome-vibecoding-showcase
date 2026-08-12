# Project Classification Rules

[简体中文](CATEGORIES.md) · English

This taxonomy applies only to software products that have already passed
C1–C5. Classification does not change the inclusion bar, and the existence of a
category never makes an otherwise ineligible project acceptable.

## Core Rules

1. Each project receives exactly one primary category and one secondary category
   within that primary category.
2. Classify by the main problem the product solves, its primary target user, and
   its core usage flow—not by programming language, framework, AI tool, or
   deployment platform.
3. Use the product's public homepage, documentation, and runnable flows as
   evidence, not the submitter's preferred placement for greater exposure.
4. If multiple categories appear suitable, compare them in this order:
   1. The primary target user stated in the product's public description.
   2. The core flow required for a user to realize the product's main value.
   3. The first shipped feature presented on the homepage or in the
      documentation.
5. If the choice remains ambiguous, the maintainer selects the narrower, more
   specific category and records the reason in the review record.
6. Within each category, entries are sorted by `added_on` in descending order;
   entries with the same date are sorted by project `id` in ascending ASCII
   order. Later updates do not change the original inclusion date.

## Explicit Exclusions

The following do not belong in any category:

- AI coding tools, IDEs, editors, plugins, or models.
- Component libraries, SDKs, frameworks, templates, starters, prompt
  collections, or resource lists.
- Projects that show only a concept, screenshots, design mockups, or code
  snippets and cannot be experienced publicly.
- Projects with an online experience but no public source for the primary
  implementation, or source code but no public experience.
- Projects where AI was used only for documentation, comments, tests, a small
  number of bug fixes, or asset generation.

Having AI-powered runtime features is not the same as substantial AI involvement
in development. Every product must independently pass C3, regardless of its
category.

## 1. `productivity-collaboration` | Productivity and Collaboration

**Definition:** Products that help individuals or teams organize tasks,
communicate information, or perform everyday knowledge work more effectively.
Their primary value is saving time, reducing coordination costs, or improving
personal workflows.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `task-workflow` | Tasks and workflows | To-do management, project planning, approvals, scheduling, or execution of recurring workflows |
| `communication-collaboration` | Communication and collaboration | Team communication, meeting collaboration, asynchronous work, or collaborative editing |
| `personal-productivity` | Personal productivity | Personal notes, focus, time management, or personal information organization |

**Category boundaries:**

- Workflows for a specific business function such as sales, finance, or customer
  support belong in `business-operations`.
- Products whose main goal is structured learning, teaching, or building a
  searchable knowledge system belong in `education-knowledge`.
- Developer-only tools for coding, debugging, or model management are excluded;
  an appeal to "productivity" does not place them in this category.

## 2. `business-operations` | Business and Operations

**Definition:** Products that support business activity or a specific operating
function. Their primary value maps directly to customer acquisition,
transactions, finance, delivery, or customer support.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `commerce-sales` | Commerce and sales | E-commerce operations, lead management, sales progression, quoting, or transaction workflows |
| `finance-administration` | Finance and administration | Budgeting, accounting, expenses, contracts, procurement, or business administration |
| `customer-service` | Customer service | Support intake, ticketing, self-service, customer success, or after-sales workflows |

**Category boundaries:**

- General team task management belongs in `productivity-collaboration`; use this
  category only when the core flow clearly serves a business function.
- If the core output is analysis, forecasting, or decision support rather than
  execution of a business process, use `data-decision`.
- Noncommercial products primarily serving public-interest work or allocation of
  public resources belong in `community-public-good`.

## 3. `education-knowledge` | Education and Knowledge

**Definition:** Products that help people learn, teach, research, look up, or
retain knowledge. Their primary value is improved understanding, capability, or
reusable knowledge.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `learning-training` | Learning and training | Courses, practice, assessment, tutoring, professional training, or skill development |
| `research-reference` | Research and reference | Literature lookup, source exploration, factual reference, or research-process support |
| `knowledge-management` | Knowledge management | Capturing, organizing, retrieving, connecting, or sharing knowledge within a team |

**Category boundaries:**

- If completing tasks, scheduling, or collaborating is primary and knowledge
  capture is incidental, use `productivity-collaboration`.
- If statistical analysis, forecasting, or choosing among options is primary,
  use `data-decision`.
- If gamification is merely a teaching method and learning outcomes are the main
  value, use `learning-training`; if entertainment is the main value, use
  `games-entertainment`.

## 4. `data-decision` | Data and Decisions

**Definition:** Products that turn data into insight, forecasts, plans, or
actionable choices. Their primary value comes from decisions that are more
accurate, faster, or more transparent.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `analytics-visualization` | Analytics and visualization | Metric analysis, exploration, reporting, charts, or data storytelling |
| `planning-forecasting` | Planning and forecasting | Forecasting, scenario simulation, resource planning, or goal planning |
| `decision-support` | Decision support | Comparing options, recommending actions, assessing risk, or making structured trade-offs |

**Category boundaries:**

- If data merely drives sales, finance, or support operations and the core value
  remains process execution, use `business-operations`.
- If the primary output is a creative work such as an article, image, audio, or
  video, use `creative-media`.
- Databases, ETL systems, model services, developer APIs, and visualization
  component libraries are infrastructure tools and are not eligible as product
  outcomes.

## 5. `creative-media` | Creative and Media

**Definition:** Products that help users create, edit, publish, or manage
consumable text, visual, audio, or video content.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `writing-publishing` | Writing and publishing | Long- or short-form writing, editing, layout, publishing, or content operations |
| `design-visual` | Design and visual media | Graphic design, illustration, photo editing, visual storytelling, or brand assets |
| `audio-video` | Audio and video | Music, podcasts, voice, animation, video creation, or post-production |

**Category boundaries:**

- If content primarily serves a course and learning is the main goal, use
  `education-knowledge`.
- If rules, challenges, or an entertainment loop form the main experience, use
  `games-entertainment`.
- AI-generated content assets alone do not satisfy C3. The project must also show
  that AI participated substantially in implementing the product code.

## 6. `health-lifestyle` | Health and Lifestyle

**Definition:** Products for personal health, daily life, household management,
travel, or local experiences. Their primary value is improving real-world life
for individuals or families.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `health-wellness` | Health and wellness | Fitness, sleep, nutrition, habits, mental-health support, or health-information management |
| `home-daily-life` | Home and daily life | Household tasks, belongings, food, family scheduling, or personal daily services |
| `travel-local` | Travel and local experiences | Itineraries, local discovery, location-based services, or travel experiences |

**Category boundaries:**

- Products for healthcare-provider operations, customer support, or
  administrative workflows belong in `business-operations`.
- If public health, accessibility, or broadly inclusive service is the primary
  goal, use `community-public-good`.
- A product that only provides health-education content without supporting
  real-life action belongs in `education-knowledge`.

## 7. `community-public-good` | Community and Public Good

**Definition:** Products that serve community collaboration, civic engagement,
charitable action, accessibility, or public resources. Their primary value
prioritizes social and public benefit.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `civic-public-service` | Civic and public services | Public information, civic participation, community governance, or use of public resources |
| `accessibility-inclusion` | Accessibility and inclusion | Reducing barriers related to ability, language, income, or environment and expanding equal participation |
| `community-nonprofit` | Community and nonprofit | Volunteer coordination, charitable projects, mutual-aid networks, or nonprofit services |

**Category boundaries:**

- If commercial customers are the primary audience and business outcomes are
  the main value, use `business-operations`.
- If social features primarily support leisure, performance, or entertainment,
  use `games-entertainment`.
- A product may have social significance while its core remains personal health
  or family life; use `health-lifestyle` unless public benefit is the primary
  goal.

## 8. `games-entertainment` | Games and Entertainment

**Definition:** Products whose primary value comes from game rules, interactive
experiences, social entertainment, or recreational interests rather than work,
learning, or business tasks.

| Secondary category | Name | Definition |
| --- | --- | --- |
| `games-interactive` | Games and interactive experiences | Defined interaction rules, challenges, narrative choices, or a gameplay loop |
| `social-entertainment` | Social entertainment | Casual interaction, co-viewing, performance, or entertainment-oriented social experiences |
| `hobbies-fandom` | Hobbies and fandom | Collections, hobby activities, fandom, or recreational exploration |

**Category boundaries:**

- If gamified learning primarily serves measurable learning outcomes, use
  `education-knowledge`.
- If a creation tool mainly helps users produce media, use `creative-media`; use
  this category only when the finished product itself is an interactive game.
- Scheduling or collaboration platforms for professional teams belong in
  `productivity-collaboration`, even when their subject matter involves games or
  hobbies.

## Reclassification

If a project's classification appears inaccurate, use the "General issue" form
and provide:

1. The current primary and secondary categories.
2. The proposed new classification.
3. Public evidence of the product's positioning and core flow.
4. The reasoning that follows the boundary rules in this document.

Reclassification does not change the project's original inclusion date.
