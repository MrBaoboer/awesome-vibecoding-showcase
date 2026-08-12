## 变更摘要 / Summary

<!-- 说明改了什么、为什么改，以及范围是否只涉及一个目的。 / Explain what changed, why, and whether the PR has one focused purpose. -->

- 关联 Issue / Linked issue:
- 变更类型 / Change type：项目新增 / New project；项目更新 / Project update；下架 / Removal；文档 / Documentation；翻译 / Translation；配置 / Configuration

> 新增项目必须关联带有 `status: approved` 的项目提交 Issue；“无需 Issue”的例外只适用于文档、翻译、配置等非项目变更。
>
> New projects must link to a submission Issue labeled `status: approved`. Only non-project changes such as documentation, translation, or configuration may omit an Issue.

## 项目信息 / Project information

<!-- 纯文档、翻译或仓库配置 PR 可填写“不适用”，并在上方说明原因。涉及项目收录、更新或下架时不得省略。 / For documentation-, translation-, or repository-configuration-only PRs, enter “Not applicable” and explain why above. Do not omit this section for project additions, updates, or removals. -->

| 字段 / Field | 内容 / Details |
| --- | --- |
| 产品名称 / Product name（C5） | <!-- TODO --> |
| 产品解决的问题 / Problem solved（D1） | <!-- TODO --> |
| 核心功能与实际价值 / Core features and real value（C4 / D2） | <!-- TODO --> |
| 主要技术栈 / Main technology stack（D3） | <!-- TODO --> |
| AI 工具、参与深度与典型协作方式 / AI tools, depth, and workflow（C3 / D4） | <!-- TODO --> |
| AI 实质性参与的公开证据 / Public evidence of substantial AI involvement（C3 / C5 / D4） | <!-- TODO --> |
| 在线体验、公开演示或产品地址 / Live product or demo URL（C1 / D5） | <!-- TODO --> |
| 公开源码仓库地址 / Public source repository（C2 / D5） | <!-- TODO --> |
| 完成度、实用性或创新性证据 / Evidence of completeness, utility, or innovation（C4） | <!-- TODO --> |
| 真实性及体验与源码对应关系 / Authenticity and live-to-source mapping（C5） | <!-- TODO --> |
| 一级 / 二级分类 / Primary and secondary category | <!-- TODO --> |

## 收录条件核对 / Eligibility

涉及项目时，请逐项确认 / For project-related changes, confirm each item:

- [ ] 产品、演示或在线体验可公开访问。 / The product or demo is publicly accessible（C1 / D5）。
- [ ] 产品主体源码仓库公开可访问。 / The repository containing the substantive source is public（C2 / D5）。
- [ ] AI 实质性参与核心功能实现，不是只写文档、注释、补测试、修少量 bug 或生成素材。 / AI substantially implemented core features—not merely documentation, comments, tests, minor fixes, or assets（C3 / D4）。
- [ ] 产品具备可验证的完成度、实用性或创新性。 / The product has verifiable completeness, utility, or innovation（C4 / D1 / D2）。
- [ ] 项目信息真实，产品可运行，证据可公开核验。 / Project information is authentic, the product works, and evidence is publicly verifiable（C5）。
- [ ] 展示内容完整说明问题、功能与价值、技术栈、AI 角色及两个地址。 / The listing covers the problem, features and value, stack, AI role, and both URLs（D1–D5）。
- [ ] 条目不是 AI 编程工具、IDE、编辑器、插件或模型。 / The entry is not an AI coding tool, IDE, editor, plugin, or model.

## 变更质量核对 / Change quality

- [ ] 我已阅读 `CONTRIBUTING.md` 与 `docs/CRITERIA.md`。 / I have read `CONTRIBUTING.en.md` and `docs/CRITERIA.en.md`.
- [ ] 分类符合 `docs/CATEGORIES.md`，且一个项目只选择一个主分类和一个二级分类。 / The classification follows `docs/CATEGORIES.en.md`, with exactly one primary and one secondary category.
- [ ] 展示格式符合 `docs/PROJECT_FORMAT.md`。 / The listing follows `docs/PROJECT_FORMAT.md`.
- [ ] 项目数据已更新到 `data/projects.json`，并运行 `python scripts/render_catalog.py` 生成两个 README；未直接手改生成区。 / I updated `data/projects.json`, ran `python scripts/render_catalog.py` to generate both READMEs, and did not edit generated sections directly.
- [ ] 新增或修改的链接可公开访问，且没有提交密钥、账号密码或个人敏感信息。 / New or changed links are public, and no secrets, passwords, or personal data are included.
- [ ] 中文主内容已更新；若变更影响英文关键内容，也已同步英文版本。 / Chinese primary content is updated, and affected key English content is synchronized.
- [ ] 本 PR 不包含与当前目的无关的重构或批量格式化。 / This PR contains no unrelated refactoring or bulk formatting.

## 核验说明 / Verification notes

<!-- 写明实际打开的链接、验证的核心流程，以及仍需维护者人工判断的事项。 / List the links you opened, the core flow you verified, and any questions that still require maintainer judgment. -->
