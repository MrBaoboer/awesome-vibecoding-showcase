# Governance

This document defines how listings are handled. See the [admission criteria](docs/CRITERIA.en.md); the project form supplies the listing fields. Every project must meet C1-C5, and every listing must contain D1-D5. Automation checks links, structure, and formatting; it does not make admission decisions.

## Responsibilities

| Role | Responsibility |
|---|---|
| Submitter | Provide complete, accurate, and publicly verifiable information; respond to requests for details |
| Automation | Check catalog data, links, formatting, ordering, and duplicates |
| Lead maintainer | Triage, test the product, verify evidence, decide, and merge changes |
| Independent reviewer | Handle projects or disputes in which the lead maintainer has a conflict of interest |

## Admission

| Step | Owner | Target | Basis and result |
|---|---|---:|---|
| Submit the project form | Submitter | N/A | Provide C1-C5 evidence and D1-D5 content |
| First response | Lead maintainer | 7 calendar days | Confirm scope, public access, and source availability (C1 / C2) |
| Full review | Lead maintainer | 14 calendar days after evidence is complete | Mark `status: approved`, `status: needs-info`, or `status: declined` |
| Additional information | Submitter | 14 calendar days | Close if incomplete; reopen when the requested information is supplied |
| Add the listing | Lead maintainer | 7 calendar days after approval | Write the catalog data from the approved issue and regenerate the README |
| Merge checks | Automation | 10 minutes after the change is proposed | Validate the data, review issue, links, and generated output; fix failures before merging |

Submitters only complete the project form; no pull request is required for a new listing. Maintainer-sourced projects follow the same recorded review. New submissions use `status: triage`; incomplete submissions move to `status: needs-info`; accepted submissions then move through `status: approved` and `status: listed`.

## Review

The lead maintainer checks:

1. The public experience works through a core flow (C1 / D5).
2. The public source matches the demonstrated product (C2 / D5).
3. AI performed core implementation work, supported by public and redacted development evidence (C3 / C5 / D4).
4. The product shows verifiable completeness, utility, or innovation (C4 / C5 / D1 / D2).
5. The stack, category, and listing content match the project (C5 / D1-D5).

A request for information or rejection must cite the unmet C / D IDs. Stars, author identity, revenue, and community votes cannot replace any criterion. Maintainers may not accept paid listings, reciprocal promotion, gifts, or priority in exchange for stars.

## Updates

| Action | Owner | Frequency or target | Basis |
|---|---|---:|---|
| Link checks | Automation | Weekly | Check C1, C2, and D5; one failure does not remove a listing |
| Rolling review | Lead maintainer | 10 listings per month | Recheck C1-C5 and update the verification date |
| Information update | Project team or community member | Anytime | Open a general issue with the change and a public source |
| Change handling | Lead maintainer | 7 calendar days | Verify and update D1–D5; recheck C1–C5 after material changes to the experience, source, or AI involvement |

## Removal

| Step | Owner | Target | Basis and result |
|---|---|---:|---|
| Verify the failure | Automation and lead maintainer | 48 hours after the first failure | Retry and rule out rate limits or temporary outages (C1 / C2 / D5) |
| Request a fix | Lead maintainer | 14 calendar days | Mark `status: stale` and cite the unmet C / D IDs |
| Remove | Lead maintainer | 3 calendar days after the grace period | Remove when any C1-C5 criterion remains unmet |
| Hide urgently | Lead maintainer | Immediately after verification | Phishing, malicious redirects, impersonation, or exposed private data |
| Restore | Lead maintainer | 14 calendar days after evidence is complete | Recheck C1-C5 and restore D1-D5 |

Issues, pull requests, and Git history retain the reason for removal.

## Disputes

1. Open a general issue, cite the relevant C / D IDs, and provide new evidence. Use the designated private channel for security or conduct reports.
2. The lead maintainer acknowledges the dispute within 3 calendar days and decides within 14 calendar days after the information is complete.
3. The decision addresses each relevant criterion and remains in the issue. The same evidence is reviewed once.
4. A lead maintainer who is an author, employee, investor, sponsor, or close collaborator of the project must disclose the relationship and recuse. An independent reviewer decides; the project remains pending until one is available.

## Solo-maintainer capacity

Full reviews are capped at three per week, with routine work capped at four hours. Additional complete submissions are queued in order without lowering C1-C5 or D1-D5.
