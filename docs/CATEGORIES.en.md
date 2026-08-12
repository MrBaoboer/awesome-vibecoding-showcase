# Project Categories

[Chinese version](CATEGORIES.md)

This document is for maintainers assigning categories. Submitters only need to describe their product; they do not choose the final category. Eligibility is defined by the [inclusion criteria](CRITERIA.en.md).

## Primary Categories

Each project receives one primary category and one secondary category within it.

| Primary category | Use for |
| --- | --- |
| `productivity-collaboration` — Productivity & Collaboration | General task organization, communication, collaboration, and personal workflows |
| `business-operations` — Business & Operations | Sales, commerce, finance, administration, and customer-support processes |
| `education-knowledge` — Education & Knowledge | Learning, teaching, research, reference, and knowledge retention |
| `data-decision` — Data & Decision | Turning data into analysis, forecasts, plans, or choices |
| `creative-media` — Creative & Media | Creating, editing, or publishing text, visual, audio, or video content |
| `health-lifestyle` — Health & Lifestyle | Personal health, home life, daily activities, travel, and local experiences |
| `community-public-good` — Community & Public Good | Public services, accessibility, community collaboration, and nonprofit work |
| `games-entertainment` — Games & Entertainment | Gameplay, interactive entertainment, social leisure, and hobbies |

## Secondary Categories

| Primary category | Secondary category | Use for |
| --- | --- | --- |
| `productivity-collaboration` | `task-workflow` — Task & Workflow | To-dos, project plans, approvals, schedules, or recurring workflows |
| `productivity-collaboration` | `communication-collaboration` — Communication & Collaboration | Team communication, meetings, asynchronous work, or collaborative editing |
| `productivity-collaboration` | `personal-productivity` — Personal Productivity | Personal notes, focus, time, or information management |
| `business-operations` | `commerce-sales` — Commerce & Sales | E-commerce, leads, sales progression, quotes, or transactions |
| `business-operations` | `finance-administration` — Finance & Administration | Budgets, accounting, expenses, contracts, procurement, or administration |
| `business-operations` | `customer-service` — Customer Service | Support intake, tickets, self-service, customer success, or after-sales work |
| `education-knowledge` | `learning-training` — Learning & Training | Courses, practice, assessment, tutoring, or skill development |
| `education-knowledge` | `research-reference` — Research & Reference | Literature, sources, factual reference, or research support |
| `education-knowledge` | `knowledge-management` — Knowledge Management | Capturing, organizing, retrieving, connecting, or sharing knowledge |
| `data-decision` | `analytics-visualization` — Analytics & Visualization | Metrics, exploration, reports, charts, or data storytelling |
| `data-decision` | `planning-forecasting` — Planning & Forecasting | Forecasts, scenarios, resource planning, or goal planning |
| `data-decision` | `decision-support` — Decision Support | Comparing options, recommending actions, assessing risk, or making trade-offs |
| `creative-media` | `writing-publishing` — Writing & Publishing | Writing, editing, layout, publishing, or content operations |
| `creative-media` | `design-visual` — Design & Visual | Graphics, illustration, photo editing, visual storytelling, or brand assets |
| `creative-media` | `audio-video` — Audio & Video | Music, podcasts, voice, animation, video, or post-production |
| `health-lifestyle` | `health-wellness` — Health & Wellness | Fitness, sleep, nutrition, habits, or health-information management |
| `health-lifestyle` | `home-daily-life` — Home & Daily Life | Household tasks, belongings, food, family scheduling, or daily services |
| `health-lifestyle` | `travel-local` — Travel & Local | Itineraries, local discovery, location services, or travel experiences |
| `community-public-good` | `civic-public-service` — Civic & Public Service | Public information, civic participation, community governance, or public resources |
| `community-public-good` | `accessibility-inclusion` — Accessibility & Inclusion | Reducing ability, language, economic, or environmental barriers |
| `community-public-good` | `community-nonprofit` — Community & Nonprofit | Volunteer work, public-interest projects, mutual aid, or nonprofit services |
| `games-entertainment` | `games-interactive` — Games & Interactive Experiences | Experiences with rules, challenges, narrative choices, or gameplay loops |
| `games-entertainment` | `social-entertainment` — Social Entertainment | Casual interaction, shared viewing, performance, or social entertainment |
| `games-entertainment` | `hobbies-fandom` — Hobbies & Fandom | Collections, hobby activities, fandom, or leisure exploration |

## Assignment Rules

1. Classify by the primary outcome of the core user flow, not by technology, AI tool, or marketing theme.
2. A workflow for a specific business function belongs in Business & Operations; general work management belongs in Productivity & Collaboration.
3. Use Education & Knowledge when learning or skill development is the main outcome; use Games & Entertainment when leisure is the main outcome.
4. Use Data & Decision when the main outcome is analysis, forecasting, or choosing among options; use Business & Operations when data only supports process execution.
5. Use Creative & Media when the main outcome is media content; use Games & Entertainment when the finished product is itself an interactive game.
6. Use Health & Lifestyle for individual or household outcomes; use Community & Public Good when public benefit is the primary outcome.
7. When several categories fit, compare the public positioning, core flow, and first shipped feature in that order. Choose the narrower category and record the reason in the review issue.

## Ordering

Within each category, sort by `added_on` in descending order, then by project `id` in ascending ASCII order. Updates do not change the original listing date.
