# Awesome VibeCoding Showcase｜Vibe Coding 优秀应用成果橱窗

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC_BY_4.0-blue.svg)](CONTENT-LICENSING.md)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE)

**Vibe Coding 优秀应用成果橱窗。**这里只收录 AI 实质参与主体开发、可公开体验且源码公开的完整产品。

> A curated showcase of usable, open-source products substantially built through natural-language collaboration with AI.

[English](README.en.md) · 简体中文

## 这是什么

`Awesome-VibeCoding-Showcase` 是一个 GitHub 原生、中文优先并提供关键英文对照的成果库。它关注“做成了什么”，不收集 AI 编程工具、IDE、编辑器、插件或模型。

适合：

- 想快速体验优秀 Vibe Coding 产品，并查看真实源码与开发证据的开发者；
- 想展示成果、说明 AI 协作过程并获得可信曝光的产品作者；
- 想研究技术选择、产品完成度和人机协作方式的团队与社区维护者。

值得 Star 的理由：每个条目都有在线体验、公开源码、AI 实质参与证据、统一的价值说明和最近核验日期；失效或失真的项目会进入复核与下架流程。

## 快速导航

- [收录标准](#收录标准)
- [分类](#分类)
- [项目橱窗](#项目橱窗)
- [提交项目](#提交项目)
- [审核与维护](#审核与维护)
- [贡献与社区](#贡献与社区)

## 收录标准

项目必须同时满足五项标准，缺一不可：

- **C1 — 可体验：**有公众可访问的产品、演示或在线体验；
- **C2 — 源码公开：**有公开可读、与产品主体相符的源码仓库；
- **C3 — AI 实质参与：**核心功能代码主要由 AI 生成并经对话迭代完成，或主体开发由自然语言驱动；
- **C4 — 有成果质量：**具备可验证的完成度、实用性或创新性；
- **C5 — 真实可核验：**产品、源码、作者陈述和开发证据相互一致。

每个正式条目还必须完整展示：解决的问题（D1）、核心功能与实际价值（D2）、主要技术栈（D3）、AI 的工具/深度/协作方式（D4），以及体验和源码地址（D5）。详见[收录标准与证据指南](docs/CRITERIA.md)。

不计入 C3：只用 AI 写文档、生成注释、补测试、修少量 Bug 或制作素材。不开设工具、IDE、插件、模型等类别。

## 分类

每个项目只有一个一级分类和一个二级分类，以用户完成的主要任务为准：

1. 生产力与协作 / Productivity & Collaboration
2. 商业与运营 / Business & Operations
3. 教育与知识 / Education & Knowledge
4. 数据与决策 / Data & Decision
5. 创意与媒体 / Creative & Media
6. 健康与生活 / Health & Lifestyle
7. 社区与公共利益 / Community & Public Good
8. 游戏与娱乐 / Games & Entertainment

完整的二级分类、边界案例和机械排序规则见[分类规则](docs/CATEGORIES.md)。

## 项目橱窗

正式条目由 [`data/projects.json`](data/projects.json) 生成；不要直接手改本节。分类内按收录日期倒序排列，同日按项目 ID 升序排列。

<!-- catalog:start -->
_暂无收录项目。_
<!-- catalog:end -->

首批项目宁缺毋滥。候选只有在 C1–C5 全部人工核验、D1–D5 完整且自动化通过后才会出现在这里。

## 提交项目

1. 先阅读[贡献指南](CONTRIBUTING.md)并自查 C1–C5；
2. 在仓库的 **Issues → New issue** 选择 **项目提交 / Project submission**；
3. 一个 Issue 只提交一个项目，并提供去敏后的公开 AI 开发证据；
4. Issue 获得 `status: approved` 后，再按 PR 模板更新结构化数据和双语展示。

维护者会在 7 天内首次响应，并以材料齐全后 14 天内完成一次完整决定为目标。自动化通过不等于收录获批。

## 审核与维护

- 新提交按[人工审核清单](docs/REVIEW_CHECKLIST.md)逐项验证 C1–C5 和 D1–D5；
- 链接每周自动巡检，维护者每月人工复核至少 10 个条目；
- 普通链接故障会在二次确认后通知作者，并提供 14 天修复窗口；
- 源码关闭、材料失真或安全风险会触发下架审查；
- 收录争议默认在公开 Issue 留痕，行为规范与安全事件使用私密渠道。

完整状态、时限、回避和申诉规则见[治理机制](GOVERNANCE.md)。

## 贡献与社区

- [贡献指南](CONTRIBUTING.md)
- [英文贡献指南 / Contributing in English](CONTRIBUTING.en.md)
- [单项目展示格式](docs/PROJECT_FORMAT.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全政策](SECURITY.md)
- [路线图](ROADMAP.md)
- [运营手册](docs/OPERATIONS.md)

欢迎修复失效链接、改善双语表达、补充可验证证据或参与复核。收录不收费，不接受付费置顶、交换推广或用 Star 数换取优先审核。

## 许可证

- README、项目元数据与说明文档：[`CC BY 4.0`](CONTENT-LICENSING.md)；
- 校验脚本与 GitHub 自动化：[`MIT`](LICENSE)；
- `CODE_OF_CONDUCT*`：`CC BY-SA 4.0`，沿用 Contributor Covenant 3.0 的授权。

路径边界和第三方材料说明见 [`LICENSING.md`](LICENSING.md) 与 [`NOTICE`](NOTICE)。被收录项目仍使用其各自仓库声明的许可证；“源码公开”不等于可任意复用。
