# 目录数据维护

本文件供维护者使用。项目提交者只需填写项目提交 Issue，不需要编辑数据文件或选择最终分类。

`projects.json` 是项目目录的唯一数据源。两个 README 中 `catalog:start` 与 `catalog:end` 之间的内容由脚本生成，不得手动修改。

## 收录项目

项目 Issue 获得 `status: approved` 后：

1. 依据审核记录选择一级和二级分类；
2. 在 `projects.json` 中录入 D1–D5、C3–C5 证据、审核 Issue 和核验日期；
3. 保留首次收录日期，并按 `added_on` 倒序排列；同日按 `id` 的 ASCII 升序排列；
4. 生成 README 并运行检查；
5. 合并后将 Issue 标记为 `status: listed`。

```powershell
python scripts/render_catalog.py
python scripts/validate_catalog.py
python scripts/validate_repository.py
python scripts/render_catalog.py --check
python -m unittest discover -s scripts -p "test_*.py"
```

CI 还会确认 `review_issue_url` 指向当前仓库中真实的项目提交 Issue，且带有 `submission` 和 `status: approved` 或 `status: listed` 标签。

字段结构和数量限制以 [`schema/projects.schema.json`](../schema/projects.schema.json) 为准。条目只写已上线且可核验的内容，使用直接地址，不使用搜索页或短链；中英文字段表达相同事实，不要求逐字对应。

## 更新项目

- 事实、链接或证据变化时，先在原审核 Issue 或通用 Issue 中留下来源；
- 修改 `projects.json` 后重新生成两个 README；
- 只有重新核验 C1–C5 后才更新 `verified_on`；
- 内容更新不改变 `added_on`。
