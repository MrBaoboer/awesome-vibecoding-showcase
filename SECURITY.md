# Security Policy / 安全政策

## Supported version / 支持范围

本仓库只支持 GitHub 默认分支的最新版本。历史提交、分叉仓库以及被收录项目自身的代码、部署和服务不在本仓库的安全维护范围内。

Only the latest version on the GitHub default branch is supported. Historical revisions, forks, and the code, deployments, or services of listed projects are outside this repository's security-maintenance scope.

收录不是安全背书。若问题属于某个被收录项目，请同时按照该项目自己的安全政策向其维护者报告；如该项目链接存在钓鱼、恶意跳转、冒充或隐私泄露风险，也请向本仓库报告，以便紧急隐藏条目。

A listing is not a security endorsement. If a vulnerability belongs to a listed project, report it to that project's maintainers under its own policy. Also notify this repository when its listing leads to phishing, a malicious redirect, impersonation, or privacy exposure so the entry can be hidden urgently.

## What to report / 报告范围

- 本仓库脚本、GitHub Actions 或依赖中的可利用漏洞； / exploitable issues in repository scripts, GitHub Actions, or dependencies;
- 可导致令牌、密钥或维护权限泄露的配置； / configurations that may expose tokens, secrets, or maintainer privileges;
- 被收录链接发生的钓鱼、恶意跳转、恶意下载、域名接管或冒充； / phishing, malicious redirects or downloads, domain takeover, or impersonation through a listed URL;
- 仓库中意外提交的个人信息、秘密或其他敏感数据； / personal data, secrets, or other sensitive material accidentally committed here;
- 可绕过审核或篡改收录数据的供应链问题。 / supply-chain issues that can bypass review or alter listing data.

一般链接失效、内容纠错和资格争议不是安全漏洞，请使用普通 Issue。行为规范事件请遵循 CODE_OF_CONDUCT.md；可以使用同一私密入口，但标题应明确为行为规范报告。

Ordinary dead links, copy corrections, and eligibility disputes are not vulnerabilities and belong in a regular issue. Conduct incidents follow CODE_OF_CONDUCT.en.md; they may use the same private entry point but must be clearly titled as a conduct report.

## Private reporting / 私密报告

首选方式是在本仓库 GitHub 页面进入 Security → Advisories，然后选择 Report a vulnerability。请提供：

The preferred route is this repository's GitHub page under Security → Advisories → Report a vulnerability. Please include:

1. 问题类型与受影响文件、工作流或 URL； / issue type and affected file, workflow, or URL;
2. 复现步骤或最小概念验证； / reproduction steps or a minimal proof of concept;
3. 可能影响及已知被利用情况； / potential impact and known exploitation;
4. 建议修复方式（如有）； / suggested remediation, if any;
5. 可以公开致谢的方式，或注明希望匿名。 / preferred public credit, or a request for anonymity.

不要在公开 Issue、PR、Discussion 或提交历史中披露漏洞细节、密钥、个人信息或行为规范证据。

Do not disclose vulnerability details, secrets, personal data, or conduct evidence in a public issue, pull request, discussion, or commit history.

如果 Report a vulnerability 入口尚不可用，可创建标题为 “[Private security report request]” 的公开 Issue，但正文只能请求开启私密通道，不得写受影响目标、人员、复现步骤或证据。维护者将在确认后创建 draft Security Advisory 并邀请报告者继续私密沟通，或启用仓库的私密漏洞报告功能。

If Report a vulnerability is unavailable, open a public issue titled “[Private security report request]”. Its body must only request a private channel and must not identify affected targets, people, reproduction steps, or evidence. After acknowledgment, the maintainer will create a draft Security Advisory and invite the reporter, or enable private vulnerability reporting for the repository.

## Response targets / 响应目标

| 阶段 / Stage | 目标 / Target |
|---|---:|
| 确认收到 / Acknowledgment | 3 个自然日 / 3 calendar days |
| 初步分类与影响判断 / Initial triage and impact assessment | 7 个自然日 / 7 calendar days |
| 已确认恶意链接的临时隐藏 / Temporary hiding of a verified malicious link | 核实后立即，目标 24 小时内 / Immediately after verification, target within 24 hours |
| 修复计划或状态更新 / Remediation plan or status update | 14 个自然日 / 14 calendar days |
| 后续状态更新 / Subsequent status updates | 至少每 14 个自然日 / At least every 14 calendar days |

这些是单维护者项目的响应目标，不是修复完成保证。复杂问题的修复时间取决于风险和上游依赖；维护者会说明下一步和预计时间。

These are response targets for a solo-maintainer project, not guarantees of completed remediation. Complex fixes depend on risk and upstream dependencies; the maintainer will state the next step and expected timeline.

## Disclosure and handling / 披露与处理

- 报告者与维护者在修复或缓解措施可用前协调披露时间。 / Reporter and maintainer coordinate disclosure until a fix or mitigation is available.
- 只向处理问题所必需的人员开放报告，并删除公开位置中的意外泄露。 / Access is limited to people needed for resolution, and accidental public disclosure is removed where possible.
- 不要求报告者提供超出核验需要的个人信息。 / Reporters are not asked for personal information beyond what verification requires.
- 在不增加风险且报告者同意时，于修复说明中致谢；匿名请求会被尊重。 / Credit is provided in remediation notes when safe and agreed; requests for anonymity are respected.
- 本项目目前不提供漏洞赏金，也不授权测试第三方项目、账号或基础设施。 / This project currently offers no bug bounty and does not authorize testing third-party projects, accounts, or infrastructure.

请仅测试你拥有或获明确授权的资源，并避免隐私侵犯、数据破坏、服务中断、社会工程或供应链投毒。

Test only resources you own or are expressly authorized to test, and avoid privacy invasion, data destruction, service disruption, social engineering, or supply-chain poisoning.
