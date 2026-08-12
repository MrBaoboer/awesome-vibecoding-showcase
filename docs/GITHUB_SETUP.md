# GitHub 仓库上线设置

本文件列出本地文件无法自动完成的 GitHub 仓库设置。创建远端后由维护者逐项应用并在首个 Release 前复核。

## Repository details

- Repository name: `Awesome-VibeCoding-Showcase`
- README 中文标题：`Awesome VibeCoding Showcase｜Vibe Coding 优秀应用成果橱窗`
- README English title: `Awesome VibeCoding Showcase`
- 中文名称：`Vibe Coding 优秀应用成果橱窗`
- About（中文优先）：`精选由 AI 实质参与开发、可在线体验且源码公开的 Vibe Coding 产品成果。Chinese-first, bilingual.`
- About (English alternative): `Curated, usable, open-source products substantially built through AI collaboration.`
- Website: 留空（本项目不建设独立官网）
- Topics:
  - `awesome-list`
  - `vibe-coding`
  - `ai-coding`
  - `showcase`
  - `open-source`
  - `applications`
  - `made-with-ai`
  - `bilingual`
  - `chinese`

## 对外文案备选 / Tagline options

- 中文：`看见 Vibe Coding 真正做成的产品。`
- 中文：`可体验、看源码、能验证的 AI 编程成果橱窗。`
- 中文：`从自然语言到可运行产品，展示真实的人机协作成果。`
- English: `See what Vibe Coding actually ships.`
- English: `Usable products, public source, verifiable AI collaboration.`
- English: `From natural language to working products.`

## Features

- 开启 Issues；
- 可在有精力主持时开启 Discussions；
- 关闭 Wikis，避免规则出现第二事实源；
- 不启用 GitHub Pages；
- 开启私密漏洞报告（Private vulnerability reporting）。

## `main` 分支保护

首次推送且两个工作流成功运行后：

- Require a pull request before merging；
- 启动期只有 1 名维护者时，不要求审批人数；
- Require status checks：
  - `Links (C1 / C2 / C5 / D5)`
  - `Format and fields (C1-C5 / D1-D5)`
- Require conversation resolution；
- Block force pushes；
- Block deletions；
- 不启用允许绕过 C1–C5 的自定义例外。

引入第二名维护者后，将 required approvals 设为 1；利益冲突项目由无关联维护者审批。

## Labels

按 [`.github/labels.yml`](../.github/labels.yml) 创建或同步标签。Issue Form 中引用的标签名必须逐字符一致。

## Actions

- Workflow 的默认权限使用 **Read repository contents permission**；
- `Validate content` 仅额外授予 `issues: read`，用于确认目录条目引用的审核 Issue 真实存在，并带有 `submission` 与 `status: approved` / `status: listed` 标签；
- 不允许 Actions 创建或批准 Pull Request；
- 首次推送会自动运行 `Validate content` 与 `Check links`；如首次运行被仓库策略跳过，再从 Actions 页面分别手动触发；
- 只有两项均成功后，才将其设为必需检查。

## 首发检查

- [ ] 仓库可见性为 Public；
- [ ] 默认分支为 `main`；
- [ ] About 与 Topics 已填写；
- [ ] Issues 已开启，项目提交表单可见；
- [ ] 私密漏洞报告已开启；
- [ ] 两项 Actions 已成功运行；
- [ ] 分支保护已启用；
- [ ] `CODE_OF_CONDUCT*` 没有报告渠道占位符；
- [ ] 首批正式条目均有批准 Issue。
