## Purpose
定义 Yu-AI-OS Pull Request 执行摘要与确定性基础检查的可信规则。

## Read By
Human、ChatGPT、Codex、GitHub Actions

## Update Frequency
当摘要目标、检查范围、安全边界或自动化行为发生变化时更新。

## Related Files
- `00_System/AI_Constitution.md`
- `00_System/Workflow.md`
- `00_System/Decision_Log.md`
- `.github/workflows/executive-summary.yml`
- `.github/scripts/executive_summary.py`

# Executive Summary Policy

## 目标

自动化只为 Human 提供两项内容：

1. 约 20～30 秒可读完的中文执行摘要；
2. 轻量、确定性的基础检查结果。

自动化不对完整 diff 进行 LLM 审查，不向 DeepSeek 或其他 LLM 发送 Pull Request 内容，也不生成长篇 AI findings。

## 权限与决定边界

- Human 拥有最终 Merge 决定权。
- 执行摘要和自动检查都属于 advisory 信息。
- 自动化不得批准 Pull Request、执行 Merge、启用自动 Merge、修改代码、生成修复 Commit、Push、修改分支保护或仓库设置。
- 检查通过只表示已运行的确定性检查通过，不表示 Human 已审阅或批准 Merge。
- 自动摘要不得伪造 Human Decision、Human Acceptance 或 Merge 授权。

## 可信执行边界

Workflow 使用 `pull_request_target`，只执行 `main` 中已受信任的 Workflow 和摘要脚本。

Pull Request head 仅作为数据被读取。自动化可以读取 Git 对象、PR 标题、PR 正文和元数据，但不得 checkout、导入或执行 PR head 中的脚本、依赖、命令或配置。

GitHub 权限保持为：

- `contents: read`
- `pull-requests: write`

不得增加与本目标无关的写权限。技术错误保留在 Actions 日志中，不写入 Human 摘要。

## 摘要数据来源

允许的数据来源：

- PR 标题和 PR 正文；
- GitHub changed files 数量；
- base SHA、head SHA、分支和 PR 元数据；
- 确定性检查的真实结果。

“本次做了什么”“本次没做什么”“需要 Human 注意”和“下一步”优先从 PR 正文的同名结构化栏目提取。缺少栏目时必须写“PR 正文未提供”，不得根据 diff 或模型猜测内容。

摘要不得默认列出完整 changed files、Payload limits、截断细节、英文基础设施说明、严重性分级或内部实现细节。

## 默认输出

每条摘要必须包含：

- 结论：`✅ 可以进入 Human 审阅` 或 `⚠ 建议修改后再合并`；
- 本次做了什么：最多 5 条；
- 本次没做什么：最多 5 条；
- 自动检查；
- 需要 Human 注意：没有则写“无”，有则最多 3 条；
- 下一步：最多 3 条；
- “自动检查通过不代表 Human 已批准 Merge”的明确说明；
- 预计阅读时间。

## 确定性检查

只运行当前仓库可低成本可靠完成的检查：

- 变更 Python 文件的语法编译；
- 执行摘要脚本自测；
- `git diff --check`；
- 变更 Markdown 文件的本地链接检查；
- 变更 YAML 文件的基本解析。

未来已有 TypeScript、Lint 或测试工具链时，可以按实际价值接入；本任务不为制造绿色勾引入完整新工具链。

任何已配置检查失败时，Workflow 必须失败，摘要结论必须为“建议修改后再合并”。没有适用文件或没有对应工具链时，必须如实写“未配置”，不得伪造通过。

## 评论更新

稳定隐藏标记为：

`<!-- yu-ai-os-automatic-review -->`

每个 Pull Request 只维护一条由 GitHub Actions Bot 创建的标记评论。重跑时更新最新的同标记 Bot 评论，不重复创建摘要。沿用旧标记是为了把现有长篇自动审查评论原位替换为新摘要。

## 失败行为

- 确定性检查失败：先更新摘要，再以非零状态结束 Workflow。
- GitHub API、配置、脚本、自测或评论发布失败：Workflow 以非零状态结束，具体错误保留在 Actions 日志中。
- 任何失败都不得被描述为通过、Human Approval 或 Merge Approval。
