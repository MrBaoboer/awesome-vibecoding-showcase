# 项目数据维护 / Catalog data maintenance

`projects.json` 是项目条目的唯一事实源。`README.md` 与 `README.en.md` 中 `catalog:start` / `catalog:end` 之间的内容由脚本生成，不得手改。

## 新增或更新条目

1. 确认关联的项目提交 Issue 已获得 `status: approved`；
2. 在 `projects.json` 的 `projects` 数组新增或修改一个对象；
3. 按 `added_on` 倒序、同日按 `id` 升序排列；
4. 生成双语 README；
5. 运行完整本地检查；
6. 提交数据文件和生成后的两个 README。

```powershell
python scripts/render_catalog.py
python scripts/validate_catalog.py
python scripts/validate_repository.py
python scripts/render_catalog.py --check
python -m unittest discover -s scripts -p "test_*.py"
```

本地校验会检查审核链接的结构和唯一性；CI 还会把链接绑定到当前 `${{ github.repository }}`，并通过 GitHub API 确认对应 Issue 真实存在、不是 Pull Request，且同时带有 `submission` 与 `status: approved` / `status: listed`。自动化只验证维护者已经留下的公开决定，不会自行判定 C3–C5 或批准项目。

## 项目对象示意

以下只展示结构，链接使用保留示例域名，不能复制进正式目录。JSON Schema 提供编辑器提示，标准库校验脚本是安全与合并规则的权威实现；CI 会检查 Schema 的枚举和数量声明没有漂移。字段规则见 [`schema/projects.schema.json`](../schema/projects.schema.json) 与校验脚本。

```json
{
  "id": "sample-product",
  "kind": "application",
  "name": {
    "zh-CN": "示例产品",
    "en": "Sample Product"
  },
  "primary_category": "productivity-collaboration",
  "secondary_category": "task-workflow",
  "problem": {
    "zh-CN": "说明目标用户、场景和产品解决的具体问题。",
    "en": "Explain the target user, context, and concrete problem."
  },
  "features": [
    {
      "zh-CN": "已上线的核心功能及其实际作用",
      "en": "A shipped core feature and its practical effect"
    },
    {
      "zh-CN": "第二项已上线功能及其实际价值",
      "en": "A second shipped feature and its practical value"
    }
  ],
  "value": {
    "zh-CN": "说明用户实际获得的价值或可验证创新。",
    "en": "Explain practical user value or verifiable innovation."
  },
  "tech_stack": [
    "TypeScript",
    "React",
    "PostgreSQL"
  ],
  "ai_role": {
    "tools": [
      "AI coding tool used by the author"
    ],
    "depth": "natural-language-driven-core",
    "workflow": {
      "zh-CN": "说明自然语言如何驱动主体设计、实现、测试与迭代。",
      "en": "Explain how natural language drove core design, implementation, testing, and iteration."
    },
    "evidence_urls": [
      "https://example.com/public-redacted-ai-evidence"
    ]
  },
  "demo_url": "https://example.com/live-product",
  "source_url": "https://github.com/OWNER/REPOSITORY",
  "quality_evidence": {
    "zh-CN": "记录人工完成的核心流程与完成度、实用性或创新性依据。",
    "en": "Record the tested core flow and evidence of completeness, utility, or innovation."
  },
  "verification": {
    "sources": [
      "https://example.com/independent-verification-source"
    ],
    "review_issue_url": "https://github.com/OWNER/Awesome-VibeCoding-Showcase/issues/123",
    "submitter_attested": true,
    "verified_on": "2026-08-12"
  },
  "added_on": "2026-08-12"
}
```

## 字段注意事项

- `kind` 只能是 `application`，用于机械阻止工具、IDE、插件和模型进入目录（P2 / P3）；
- `ai_role.depth` 只能是 `core-code-majority-ai` 或 `natural-language-driven-core`（C3 / D4）；
- `verification.sources` 至少有一个不同于体验和源码的公开核验来源（C5）；
- `verification.review_issue_url` 必须指向当前 `Awesome-VibeCoding-Showcase` 仓库中一项一 Issue 的公开审核记录；正式合并前，该 Issue 必须带有 `submission` 与 `status: approved` / `status: listed`（C5）；
- URL 不接受 localhost、私网地址、带账号密码的地址或示例域名；
- `verified_on` 记录最近一次人工复核 C1–C5 的日期；普通文案修改不应伪造核验日期；
- 只有维护者完成审核后才能将 `submitter_attested` 设为 `true`。
