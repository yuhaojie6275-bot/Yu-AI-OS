## Purpose

定义 Yu-AI-OS Pull Request 的确定性基础检查和 Human Review 边界。

## Read By

Human、ChatGPT、Codex、GitHub Actions

## Update Frequency

当检查范围、安全边界或自动化行为发生变化时更新。

## Related Files

- `00_System/AI_Constitution.md`
- `00_System/Workflow.md`
- `00_System/Decision_Log.md`
- `.github/workflows/deterministic-checks.yml`
- `.github/scripts/deterministic_checks.py`

# Deterministic Checks Policy

## 目标

自动化只运行低成本、可复核的确定性检查，不调用 DeepSeek 或其他 LLM，不读取 PR body 生成摘要，不创建或更新 PR 评论。

Codex 的任务报告、Commit / PR 信息以及 GitHub `Files changed` / diff 负责提供变更上下文；本自动化不重复生成执行摘要，也不新增替代摘要系统。

## 权限与决定边界

- Human 拥有最终 Merge 决定权。
- 自动检查结果属于 advisory 信息。
- 自动化不得批准 Pull Request、执行 Merge、启用自动 Merge、修改代码、生成修复 Commit、Push、修改分支保护或仓库设置。
- 检查通过只表示已运行的确定性检查通过，不表示 Human 已审阅或批准 Merge。

## 可信执行边界

Workflow 使用 `pull_request_target`，只执行 `main` 中已受信任的 Workflow 和检查脚本。Pull Request head 仅作为 Git 数据被读取，不 checkout、导入或执行其脚本、依赖、命令或配置。

GitHub 权限仅为：

- `contents: read`

不得增加与确定性检查无关的写权限。技术错误保留在 Actions 日志中。

## 确定性检查

当前检查包括：

- 变更 Python 文件的语法编译；
- `git diff --check`；
- 变更 Markdown 文件的本地链接检查；
- 变更 YAML 文件的基本解析。

没有适用文件时如实报告 `SKIP`，不得伪造通过。未来可按实际价值接入已有 TypeScript、Lint 或测试工具链，但本政策不要求新增低价值工具链。

任何已配置检查失败时，Workflow 必须以非零状态结束；失败不得被描述为 Human Approval 或 Merge Approval。

## 失败行为

- 确定性检查失败：以非零状态结束，并将具体结果保留在 Actions 日志中。
- Git、配置、脚本或解析失败：Workflow 以非零状态结束，具体错误保留在 Actions 日志中。
- 自动化不发布 PR 评论，不调用模型，也不代替 Human 解释或批准变更。
