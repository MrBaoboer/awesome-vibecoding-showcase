# Maintainers / 维护者

## Current roles / 当前角色

本仓库以一名主维护者启动。由于当前仓库副本没有可核实的远程仓库身份，本文件不虚构个人姓名或邮箱；发布到 GitHub 后，拥有该仓库 Admin 权限并执行发布的仓库所有者账号即为主维护者的可核实身份。

This repository launches with one lead maintainer. Because this repository copy has no verifiable remote identity, this file does not invent a name or email address. Once published on GitHub, the repository-owner account with Admin permission that performs the publication is the verifiable lead maintainer.

| 角色 / Role | 当前席位 / Current seat | 权限与职责 / Authority and duties |
|---|---|---|
| 主维护者 / Lead maintainer | 仓库所有者或其明确指定的 Admin；1 席 / Repository owner or explicitly designated Admin; one seat | 按 GOVERNANCE.md 初审和裁决、合并 PR、管理标签和自动化、执行链接巡检与下架、维护记录。 / Triage and decide under GOVERNANCE.md, merge pull requests, manage labels and automation, act on link checks and removals, and maintain records. |
| 备用行为规范主持人 / Backup conduct moderator | 单人启动期空缺 / Vacant during solo launch | 在涉及主维护者的行为规范报告中独立受理和执行。任命后必须在本表记录 GitHub 用户名。 / Independently handle conduct reports involving the lead maintainer. Once appointed, the GitHub username must be recorded here. |
| 临时复核者 / Ad hoc reviewer | 按个案邀请 / Invited per case | 复核利益冲突或复杂的 C1–C5 争议；仅获处理该事项所需的最小权限。 / Review conflicts of interest or complex C1–C5 disputes with only the minimum access needed. |

备用行为规范主持人空缺期间，如报告涉及唯一维护者，请使用 GitHub 的 Report abuse 功能报告发生在 GitHub 上的行为。仓库不会虚假承诺此时能够提供独立的内部裁决；主维护者必须优先招募无利益关系的备用主持人。

While the backup conduct moderator is vacant, reports concerning the sole maintainer should use GitHub's Report abuse feature for conduct occurring on GitHub. The repository does not falsely promise independent internal adjudication during that gap; recruiting an unrelated backup moderator is a priority.

## Operating rules / 工作规则

- 所有收录、拒绝、更新、下架与申诉必须留下可审计的 Issue 或 PR 记录，并引用相关 C / D 编号。 / Every listing, decline, update, removal, and appeal must leave an auditable issue or pull-request record citing the relevant C / D IDs.
- 自动化结果不等于人工批准，尤其不能替代 C3、C4、C5 判断。 / Automation is not human approval and cannot decide C3, C4, or C5.
- 不接受付费收录、交换推广、礼物或以 Star 数换取优先审核。 / No paid listing, reciprocal promotion, gifts, or priority in exchange for stars.
- 不要求未去敏的完整 AI 对话，不使用 AI 代码检测器推断 C3。 / Do not demand unredacted full AI conversations or infer C3 with AI-code detectors.
- 超过公开 SLA 时更新状态和原因，不静默搁置。 / When an SLA is missed, update the status and reason rather than silently abandoning the item.
- 安全风险可先采取可逆保护措施，但最终结论仍须记录证据。 / Reversible protective action may precede investigation for security risks, but final findings still require recorded evidence.

## Conflicts of interest / 利益冲突

维护者是项目作者、雇员、投资者、赞助方，或与项目有密切协作关系时，必须在相关 Issue 中披露并回避最终决定。由无利益关系的临时复核者决定；暂时找不到复核者时保持待审，不自行批准。

A maintainer who is an author, employee, investor, sponsor, or close collaborator of a project must disclose that relationship in the relevant issue and recuse from the final decision. An unrelated ad hoc reviewer decides the item; if none is available, it remains pending and is not self-approved.

## Adding maintainers / 新增维护者

候选人在最近 90 天内应至少完成以下任意三项：5 次有效提交审核、5 个被合并的内容或治理 PR、10 次有证据的链接复核、或持续参与一次争议处理；同时无未披露利益冲突或有效行为规范处分。主维护者通过公开 PR 提名，列出证据、权限范围和 14 天试用期。试用通过后更新本文件。

Within the preceding 90 days, a candidate should complete any three of: five sound submission reviews, five merged content or governance pull requests, ten evidenced URL reviews, or sustained participation in one dispute review, with no undisclosed conflict or active conduct sanction. The lead maintainer nominates the candidate in a public pull request documenting evidence, scope of access, and a 14-day trial. This file is updated after a successful trial.

行为规范主持人除具备上述判断能力外，还须同意保密、最小披露和回避规则。不得把敏感报告内容用于一般社区评价。

Conduct moderators must also accept confidentiality, minimum-disclosure, and recusal duties. Sensitive report contents must not be reused for general community evaluation.

## Inactivity, removal, and handover / 不活跃、移除与交接

- 连续 60 天无法履行职责时，应公开标记 inactive，并交接在途事项。 / After 60 consecutive days unable to perform duties, mark the role inactive publicly and hand over pending items.
- 连续 90 天无活动且无事先说明，可通过治理 PR 移除维护权限。 / After 90 days without activity or prior notice, access may be removed through a governance pull request.
- 严重安全或行为规范违规可先暂停权限，再由无利益关系的人员复核。 / Serious security or conduct violations may justify immediate suspension pending independent review.
- 交接清单至少包含开放审核、stale 条目、计划中的自动化变更、私密安全事项的最小必要状态和下一次月度复核日期。不得把私密报告复制到公开文档。 / Handover covers open reviews, stale listings, planned automation changes, the minimum necessary status of private security matters, and the next monthly review date. Private reports must not be copied into public documents.

本文件中的角色变更通过 PR 进行；不得在提交历史中写入私人邮箱、密钥或行为规范证据。

Role changes are made by pull request. Private email addresses, secrets, and conduct evidence must not be placed in commit history.
