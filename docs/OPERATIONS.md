# 运营手册 / Operations Playbook

## 一人维护周节奏

| 动作 | 频率 | 时间预算 | 验收方式 |
|---|---:|---:|---|
| 新提交分诊 | 每周 2 次 | 30 分钟 | 7 天内首次响应率 ≥ 90% |
| 完整审核 | 每周最多 5 个 | 120 分钟 | 每个 Issue 留下 C1–C5 / D1–D5 结论 |
| 链接故障复核 | 每周 1 次 | 20 分钟 | 自动失败经重试和人工确认后才建 Issue |
| 双语与数据同步 | 每周 1 次 | 20 分钟 | `render_catalog.py --check` 通过 |
| 社区回复与发布 | 每周 1 次 | 30 分钟 | 问题有状态标签，发布记录可追溯 |
| 机动缓冲 | 每周 | 40 分钟 | 总投入控制在 3–4 小时 |

当完整审核积压超过 10 个时，停止主动征集一周，先清理队列；不降低 C1–C5 标准换取吞吐。

## 冷启动候选池

首轮只建立 20–50 个候选，不直接视为收录。来源按周轮换：

- GitHub：相关 Topic、README 开发日志、公开源码仓库；
- Product Hunt：AI、productivity、developer-built 等产品发布页；
- Hacker News：Show HN；
- Indie Hackers：产品发布和 Build in Public；
- Reddit：r/SideProject、r/webdev、r/LocalLLaMA 中的产品展示帖；
- Cursor Forum：Built with Cursor；
- Replit Gallery、v0 Templates、Lovable Customer Stories：仅作为发现入口；
- DEV Community、Hashnode、掘金、少数派、V2EX 分享创造板块；
- GitHub Trending 与 Awesome 列表：只提取最终应用候选，先排除工具类。

筛选顺序固定如下：

1. 排除工具、IDE、编辑器、插件、模型和纯概念（P2 / P3）；
2. 匿名窗口打开体验并完成一个核心流程（C1）；
3. 打开源码并确认含产品主体实现（C2）；
4. 查找公开、去敏的 AI 工具、核心承担、深度和迭代证据（C3）；
5. 记录可复现的完成度、实用性或创新证据（C4）；
6. 交叉核对作者、产品、源码、时间线和陈述（C5）；
7. 去重后邀请作者通过 Issue 确认事实，不替作者编造 D1–D5。

## 发布节奏

- GitHub Release：每月 1 次，列出新增、更新、下架和规则变更；
- GitHub Discussions：每月 1 个精选主题；只有仓库已启用 Discussions 时执行；
- X / Mastodon / Bluesky：每次月度 Release 后各发 1 条双语摘要；
- Reddit r/SideProject、Indie Hackers：首次达到 15 个项目时发布 1 次，此后仅在季度里程碑发布；
- Hacker News Show HN：仓库达到 30 个合格项目且规则运行满 60 天后发布 1 次；
- V2EX、掘金、少数派：首次公开发布及每季度总结各 1 次，内容必须包含审核标准和贡献入口；
- Cursor Forum、Replit、Lovable 等来源社区：仅在新增项目作者同意且符合社区规则时回帖，不批量营销。

所有外部发布都链接回 GitHub 仓库，不建设独立官网。不得把“被收录”暗示为官方背书。

## 国际化同步

- `README.md` 是规则叙述的中文主版，`README.en.md` 提供关键内容的完整英文对应；
- 项目结构化数据同时保存 `zh` 和 `en` 字段，由同一脚本渲染；
- 影响收录资格的规则变更必须在同一 PR 更新中英文关键段落；
- 每月 Release 前运行一次人工语义差异检查；
- 若两种语言冲突，以较严格的 C1–C5 解释临时执行，并在 7 天内修正文档。

## 贡献者激励

- 每月 Release 按“提交、核验、修复、翻译”四类感谢贡献者；
- 连续完成 3 次准确复核的贡献者可获 `reviewer-candidate` 记录，并接受一次维护者复核培训；
- 每月最多标记 3 个边界清晰的 `good first issue`；
- 不设置付费优先级、竞价排名或以社交热度换审核结果的激励。

## 月度复盘指标

记录在当月 Release：候选数、提交数、通过数、拒绝数、补证数、首次响应中位数、完整决定中位数、链接健康率、人工复核数、外部贡献者数。Star 数可作传播观察值，但不是质量验收指标。
