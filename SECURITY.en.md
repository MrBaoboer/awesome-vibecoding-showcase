# Security Policy

## Supported scope

Only the latest version on the GitHub default branch is maintained. Reportable issues include:

- exploitable vulnerabilities in scripts, GitHub Actions, or dependencies;
- configurations that may expose tokens, secrets, personal data, or maintainer access;
- supply-chain issues that can bypass review or alter catalog data;
- phishing, malicious redirects or downloads, domain takeover, or impersonation through a listed link.

The code, deployment, and service of each listed project remain the responsibility of its maintainers. Use a general issue for ordinary dead links, copy corrections, or eligibility disputes. See the [Code of Conduct](CODE_OF_CONDUCT.en.md) for conduct reports.

## Private reporting

On the repository's GitHub page, open **Security**, then **Advisories**, then **Report a vulnerability**, and include:

1. the affected file, workflow, or link;
2. reproduction steps or a minimal verification method;
3. potential impact and any known exploitation;
4. a suggested mitigation or fix, if available.

Do not publish vulnerability details, secrets, or personal data in an issue, pull request, discussion, or commit.

If private reporting is unavailable, open a public issue titled **[Private security report request]**. The body must only request a private channel; do not include the affected target, reproduction steps, or evidence. The maintainer will create a private security advisory and invite the reporter to continue there.

## Response targets

| Stage | Target |
|---|---:|
| Acknowledgment | 3 calendar days |
| Initial assessment | 7 calendar days |
| Hide a confirmed malicious link | Immediately after verification, with a 24-hour target |
| Remediation plan or status update | 14 calendar days |
| Further status updates | At least every 14 calendar days |

## Handling

- Reports are shared only with people needed to resolve the issue.
- The maintainer and reporter coordinate disclosure until a fix or mitigation is available.
- Credit is given when safe and agreed; requests for anonymity are respected.
- This project offers no bug bounty and does not authorize testing of third-party projects, accounts, or infrastructure.

Test only resources you own or are expressly authorized to test.
