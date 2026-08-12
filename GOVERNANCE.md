# Governance / 治理

本文件规定 Awesome-VibeCoding-Showcase 的收录、审核和社区决策方式。简体中文是主要工作语言；英文用于帮助全球贡献者参与。两种表述应作同义理解，任何解释均不得降低下述准入标准。

This document defines how Awesome-VibeCoding-Showcase handles listings, reviews, and community decisions. Simplified Chinese is the primary working language; English is provided for global contributors. Both versions are intended to mean the same thing, and no interpretation may weaken the admission criteria below.

## 1. Scope and non-negotiable rules / 范围与不可变规则

- P1：只建设 GitHub 仓库，不建设独立网站。 / Build only the GitHub repository; no standalone website.
- P2：不收录 AI 编程工具、IDE、编辑器、插件或模型。 / Do not list AI coding tools, IDEs, editors, plugins, or models.
- P3：只收录借助 AI 编程真正完成、可公开体验的优秀应用或产品。 / List only strong, publicly usable applications or products genuinely built with substantial AI coding assistance.
- P4：以简体中文为主，关键内容提供英文对照。 / Use Simplified Chinese as the primary language and provide English for key content.

每个项目必须同时满足 C1–C5；任何一项失败都不能以 Star 数、作者知名度、商业收入或社区投票抵消。项目展示必须完整覆盖 D1–D5。

Every project must pass all of C1–C5. Stars, author reputation, revenue, or community votes cannot compensate for a failed criterion. Every listing must also contain D1–D5.

| 编号 / ID | 强制要求 / Mandatory requirement |
|---|---|
| C1 | 有无需私有邀请即可访问的公开产品、演示或下载体验；维护者能完成至少一个核心路径。 / A public product, demo, or downloadable experience is available without a private invitation, and a maintainer can complete at least one core path. |
| C2 | 有无需登录即可查看、且与所展示产品相符的实质源码仓库。 / A publicly viewable repository contains substantive source code corresponding to the demonstrated product. |
| C3 | AI 通过自然语言协作承担大部分核心实现；仅写文档、注释、测试、素材或少量修复不计。 / AI, directed through natural-language collaboration, performed most core implementation; documentation, comments, tests, assets, or minor fixes alone do not qualify. |
| C4 | 产品已能完成非平凡的端到端任务，并在完成度、实用性或创新性中至少一项提供具体证据。 / The product completes a non-trivial end-to-end task and provides concrete evidence of completeness, utility, or innovation. |
| C5 | 产品、源码、描述和 AI 参与声明真实、一致并可由公开证据核验。 / The product, source, description, and AI-participation claim are authentic, consistent, and verifiable through public evidence. |
| D1 | 解决的问题与目标用户。 / Problem solved and target users. |
| D2 | 核心功能及实际价值。 / Core features and practical value. |
| D3 | 主要技术栈。 / Main technology stack. |
| D4 | AI 工具、参与深度、承担的核心工作和典型协作方式。 / AI tools, depth, core work performed, and typical collaboration workflow. |
| D5 | 在线体验与源码仓库地址。 / Live experience and source repository URLs. |

自动化只能检查字段、格式、重复项和链接状态，不能自动判定 C3、C4 或 C5，也不能自动批准项目。

Automation may check fields, formatting, duplicates, and URL status. It cannot decide C3, C4, or C5 and cannot approve a project.

## 2. Roles and decision authority / 角色与决策权

| 角色 / Role | 责任 / Responsibility |
|---|---|
| 提交者 / Submitter | 提供完整、真实、已去敏的 C1–C5 证据和 D1–D5 内容；按时补充材料。 / Provide complete, truthful, redacted C1–C5 evidence and D1–D5 content; respond to requests on time. |
| 自动化 / Automation | 执行非裁决性的链接、结构、格式和重复项检查。 / Run non-decisional URL, structure, formatting, and duplicate checks. |
| 主维护者 / Lead maintainer | 初审、人工体验、证据核对、决定、合并、复核和记录。 / Triage, manually test, verify evidence, decide, merge, recheck, and keep records. |
| 临时复核者 / Ad hoc reviewer | 在利益冲突或复杂争议中提供独立复核；不得与项目存在利益关系。 / Provide independent review for conflicts of interest or complex disputes; must have no interest in the project. |

主维护者拥有日常合并权，但必须依据本文件并在拒绝、下架或争议结论中引用具体 C / D 编号。社区反馈是证据来源，不是按票数裁决。

The lead maintainer has routine merge authority, but must follow this document and cite specific C / D IDs when declining, removing, or resolving disputes. Community feedback is evidence, not a vote.

## 3. Status model / 状态模型

标准状态为：triage → needs-info 或 in-review → approved → listed。已收录项目可进入 stale → removed；不符合条件的提交进入 declined。

The standard states are: triage → needs-info or in-review → approved → listed. A listed project may move through stale → removed; an ineligible submission moves to declined.

needs-info 表示材料不足而非已经判定失败。补齐后可在原 Issue 中继续审核。一个提交 Issue 或 PR 只处理一个项目；新增项目 PR 必须关联已经 approved 的提交 Issue。维护者主动发现的项目也必须建立同样的审核记录。

needs-info means insufficient evidence, not a final failure. Review may continue in the same issue once evidence is supplied. One submission issue or pull request handles one project only. A new-listing pull request must link an approved submission issue. Maintainer-sourced projects receive the same recorded review.

## 4. Inclusion process / 收录流程

| 步骤 / Step | 责任人 / Owner | SLA | 依据与输出 / Basis and output |
|---|---|---:|---|
| 1. 提交项目表单 / Submit project form | 提交者 / Submitter | 即时 / Immediate | 完整填写 C1–C5、D1–D5，并确认符合 P1–P4。 / Complete C1–C5 and D1–D5; confirm P1–P4. |
| 2. 机械预检 / Mechanical precheck | 自动化 / Automation | 启用后 10 分钟内 / Within 10 minutes when enabled | 检查必填字段、URL 结构、重复仓库与格式；失败进入 needs-info，不自动拒绝。 / Check required fields, URL shape, duplicates, and format; failures become needs-info, never automatic rejection. |
| 3. 范围初审 / Scope triage | 主维护者 / Lead maintainer | 7 个自然日 / 7 calendar days | 核对 P1–P4、C1、C2；记录不适用或缺失项目。 / Check P1–P4, C1, and C2; record out-of-scope or missing items. |
| 4. 完整审核 / Full review | 主维护者 / Lead maintainer | 材料齐全后 14 个自然日 / 14 calendar days after evidence is complete | 按第 5 节逐项得出 approved、needs-info 或 declined。 / Apply section 5 and return approved, needs-info, or declined. |
| 5. 补充材料 / Supply evidence | 提交者 / Submitter | 14 个自然日 / 14 calendar days | 超时关闭为材料不完整；补齐后可请求重开。 / Close as incomplete after the deadline; reopening may be requested with the missing evidence. |
| 6. 条目 PR / Listing PR | 提交者；必要时维护者代办 / Submitter; maintainer if needed | 批准后 7 个自然日 / 7 calendar days after approval | 使用标准格式并关联 approved Issue；完整覆盖 D1–D5。 / Use the standard format, link the approved issue, and include D1–D5. |
| 7. 合并与登记 / Merge and record | 主维护者 / Lead maintainer | PR 通过后 7 个自然日 / 7 calendar days after PR passes | 记录收录日期、最近核验日期、分类和机械排序位置。 / Record added date, last-verified date, category, and deterministic ordering position. |

## 5. Review process / 审核流程

| 检查 / Check | 责任人 / Owner | 建议用时 / Target effort | 通过依据 / Passing basis |
|---|---|---:|---|
| 体验与仓库 / Experience and repository | 自动化 + 主维护者 / Automation + lead maintainer | 10 分钟 / 10 min | D5 两个地址可达；人工完成核心路径（C1），确认仓库含对应实质源码（C2）。 / Both D5 URLs resolve; manually complete a core path (C1) and confirm corresponding substantive source (C2). |
| AI 参与 / AI participation | 主维护者 / Lead maintainer | 5–10 分钟 / 5–10 min | D4 写明工具、核心承担、深度、典型自然语言迭代方式，并有至少一项公开、去敏证据（C3 / C5）。不得使用 AI 代码检测器代替证据。 / D4 identifies tools, core work, depth, typical natural-language iteration, and at least one public redacted artifact (C3 / C5). AI-code detectors are not evidence. |
| 产品质量 / Product quality | 主维护者 / Lead maintainer | 10 分钟 / 10 min | D1、D2 与实际体验一致，产品完成非平凡流程并有完成度、实用性或创新性证据（C4 / C5）。 / D1 and D2 match the experience; a non-trivial flow works and evidence supports completeness, utility, or innovation (C4 / C5). |
| 技术与一致性 / Technology and consistency | 主维护者 / Lead maintainer | 5 分钟 / 5 min | D3 与源码相符，Demo、源码、说明和项目身份相互一致（C5）。 / D3 matches source; demo, source, claims, and identity are mutually consistent (C5). |
| 展示完整度 / Listing completeness | 自动化 + 主维护者 / Automation + lead maintainer | 5 分钟 / 5 min | D1–D5 均完整，中英文关键内容齐备，分类与排序符合规则。 / D1–D5 are complete, key content is bilingual, and classification and ordering follow the rules. |

接受的 C3 证据包括公开开发日志、去敏对话片段、带上下文的 commit 或 PR、公开文章或视频。不得要求完整私人对话、密钥、个人信息或未经授权的第三方内容。

Acceptable C3 evidence includes public development logs, redacted conversation excerpts, contextual commits or pull requests, and public articles or videos. Full private conversations, secrets, personal data, or unauthorized third-party content must not be requested.

## 6. Update process / 更新流程

| 动作 / Action | 责任人 / Owner | 频率或 SLA / Frequency or SLA | 依据 / Basis |
|---|---|---:|---|
| 链接巡检 / URL scan | 自动化 / Automation | 每周 / Weekly | 检查 C1、C2、D5；单次失败不触发下架。 / Check C1, C2, and D5; one failure never triggers removal. |
| 滚动人工复核 / Rolling manual review | 主维护者 / Lead maintainer | 每月 10 个项目 / 10 projects monthly | 重新核对 C1–C5；更新最近核验日期。 / Recheck C1–C5 and update the last-verified date. |
| 信息更新 / Information update | 项目方或社区 / Project team or community | 随时 / Anytime | 通过关联原审核 Issue 的 PR 更新 D1–D5。 / Update D1–D5 by pull request linked to the original review issue. |
| 变更审核 / Change review | 主维护者 / Lead maintainer | 7 个自然日 / 7 calendar days | 文案或技术栈变更核对对应 D 项；Demo、源码或 AI 声明变化时重审全部 C1–C5。 / Check affected D fields for copy or stack changes; re-review all C1–C5 when demo, source, or AI claims change. |

## 7. Removal process / 下架流程

| 步骤 / Step | 责任人 / Owner | SLA | 依据与动作 / Basis and action |
|---|---|---:|---|
| 1. 异常复核 / Verify anomaly | 自动化 + 主维护者 / Automation + lead maintainer | 首次失败 48 小时后重试并人工确认 / Retry 48 hours after first failure, then verify manually | 区分真实失效与限流、WAF 或临时宕机（C1 / C2 / D5）。 / Distinguish real failure from rate limiting, WAF, or temporary outage (C1 / C2 / D5). |
| 2. 修复通知 / Remediation notice | 主维护者通知原提交者 / Lead maintainer notifies original submitter | 14 个自然日 / 14 calendar days | 标记 stale，并明确未满足的 C / D 编号。 / Mark stale and cite the failed C / D IDs. |
| 3. 下架决定 / Removal decision | 主维护者 / Lead maintainer | 宽限期结束后 3 个自然日 / 3 calendar days after grace period | 任一 C1–C5 持续失败即通过关联证据 Issue 的 PR 下架。 / Remove by an evidence-linked pull request if any C1–C5 remains failed. |
| 4. 紧急处置 / Emergency action | 主维护者 / Lead maintainer | 核实钓鱼、恶意跳转、冒充或隐私泄露后立即 / Immediately after verifying phishing, malicious redirects, impersonation, or privacy exposure | 先隐藏条目以保护访问者，再私下调查；不得把临时隐藏表述为最终定罪（C5）。 / Hide first to protect visitors, then investigate privately; do not present a temporary action as a final finding (C5). |
| 5. 恢复 / Reinstatement | 项目方提交证据；主维护者审核 / Project team submits; lead maintainer reviews | 材料齐全后 14 个自然日 / 14 calendar days after evidence is complete | 重新通过全部 C1–C5 并补齐 D1–D5。 / Re-pass all C1–C5 and restore D1–D5. |

下架记录保留在 Issue、PR 和 Git 历史中；不维护羞辱性黑名单。

Removal records remain in issues, pull requests, and Git history. The project does not maintain a shaming blacklist.

## 8. Dispute process / 争议处理

| 步骤 / Step | 责任人 / Owner | SLA | 规则 / Rule |
|---|---|---:|---|
| 1. 提出 / Raise | 项目方或社区成员 / Project team or community member | 随时 / Anytime | 使用通用 Issue，引用具体 C / D 编号并提供新证据。行为规范或敏感安全事件必须走私密渠道。 / Use the general issue form, cite C / D IDs, and provide new evidence. Conduct or sensitive security incidents must use a private channel. |
| 2. 确认 / Acknowledge | 主维护者 / Lead maintainer | 3 个自然日 / 3 calendar days | 分类为资格、分类、更新或下架申诉。 / Classify as eligibility, categorization, update, or removal appeal. |
| 3. 证据期 / Evidence window | 各方 / All parties | 7 个自然日 / 7 calendar days | 只讨论可验证事实，不公开个人或敏感资料。 / Discuss verifiable facts only; do not expose personal or sensitive material. |
| 4. 复核决定 / Review decision | 主维护者；有冲突时由临时复核者 / Lead maintainer; ad hoc reviewer on conflict | 受理后 14 个自然日 / 14 calendar days after acknowledgment | 逐项回应 C / D；不得因人气、赞助或舆论豁免标准。 / Answer each relevant C / D item; popularity, sponsorship, or pressure grants no exception. |
| 5. 再审 / Re-review | 主维护者 / Lead maintainer | 有实质新证据时 / When material new evidence exists | 相同证据只审一次；新证据可重开。 / The same evidence is reviewed once; material new evidence permits reopening. |

维护者与项目存在作者、雇佣、投资、赞助或密切协作关系时必须披露并回避最终决定。单人启动期若暂时没有合格复核者，项目保持待审，直至找到无利益关系的临时复核者，不得自行豁免。

A maintainer with authorship, employment, investment, sponsorship, or close collaboration ties must disclose the conflict and recuse from the final decision. During the solo-maintainer phase, if no qualified independent reviewer is available, the item remains pending rather than receiving a self-approved exception.

## 9. Solo-maintainer capacity / 单维护者容量

以每周 3 个新提交估算：初审约 15 分钟，完整审核约 60–75 分钟，PR 检查与合并约 25–30 分钟，链接异常和滚动复核约 45–60 分钟，社区回复与记录约 20–30 分钟，合计约 3 小时/周，峰值不超过 4 小时/周。

At three new submissions per week, estimate 15 minutes for triage, 60–75 minutes for full reviews, 25–30 minutes for pull-request checks and merges, 45–60 minutes for URL exceptions and rolling reviews, and 20–30 minutes for communication and records: about 3 hours per week, with a 4-hour peak.

在途完整审核上限为每周 5 个。超出部分按材料齐全时间顺延，并公开保留状态；不得为了追赶队列降低 C1–C5 或 D1–D5 要求。

Full reviews are capped at five per week. Excess complete submissions roll forward in order while retaining a visible status; the C1–C5 or D1–D5 bar must never be lowered to clear a queue.

## 10. Governance changes / 治理变更

治理规则变更必须通过 PR，说明原因、受影响的 C / D 项、迁移方式和生效日期，并至少开放 7 个自然日供社区评论。安全修复或明显文字错误可立即合并，但须在 PR 中记录原因。规则变化适用于所有条目；如需迁移期，应使用统一期限，不设置永久“祖父条款”。

Governance changes require a pull request stating the rationale, affected C / D items, migration method, and effective date, with at least seven calendar days for community comment. Security fixes and obvious editorial corrections may merge immediately with a recorded rationale. Rule changes apply to every listing; any transition period must be uniform, with no permanent grandfathering.
