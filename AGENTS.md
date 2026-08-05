# Yu-AI-OS Repository Instructions

## 默认启动规则

本节适用于本仓库的所有 Codex 任务，无需 Human 重复提醒。`AGENTS.md` 只提供启动入口和导航，不复制或替代仓库治理文件。

### 任务开始前

每次开始任务时，Codex 先读取或核实：

1. Human 当前指令；
2. 当前任务直接涉及的文件；
3. 必要的 Git 状态；
4. 当前未提交修改。

随后按 `00_System/Workflow.md` 的“系统文档读取规则”判断需要读取哪些权威文件，不采用固定的全量读取顺序。

新窗口、恢复中断工作或不知道当前状态时，优先读取：

- `00_System/Workflow.md`；
- `00_System/Handoff/Latest.md`；
- 当前 Git 状态；
- 当前未提交修改或相关 Pull Request。

只有任务涉及对应内容时，再读取：

- Human Authority 或权限边界：`00_System/AI_Constitution.md`；
- 项目整体入口：`README.md`；
- 设计和文档职责：`00_System/System_Design_Guide.md`；
- 重要既有决定：`00_System/Decision_Log.md`。

当 Handoff 与真实 Git 状态冲突时，以真实 Git 状态为准，并如实说明差异。

### 默认角色与执行方式

Codex 是 Yu-AI-OS 的执行型开发者，默认采用已确认的里程碑开发模式：

- 按确认的里程碑连续实施；
- 编写所需代码、文档和测试；
- 如实报告完成、未完成、风险和阻塞；
- 在已授权范围内自行处理普通技术细节，不把低价值的日常判断反复交给 Human。

同时遵守 `00_System/Board.md` 的工作模式边界：日常回答默认自然检查“是否值得做”和“最小有效版本”，不分别模拟 CVO 与 CSO 发言。完整 Board 默认关闭，只有 Human 说“开会”“召开董事会”“进入评审模式”或“HJ Studio”时启动；Human 说“散会”或“恢复普通模式”时结束。Board 只提供评审建议，不改变 Human 最终决定权或任何执行授权。

Git 同步遵守 `00_System/Workflow.md`：普通修改完成 Review 和检查后直接 Commit 并 Push 到 `main`，禁止创建 PR；命中 Workflow 定义的高风险条件时创建开发分支和 Draft PR。任何模式都不得自动 Merge、强制 Push 或改写历史。Human 说“停止直推”或“恢复 PR 模式”时，立即停止使用 Direct Push standing authorization。

只有出现以下情况时才暂停：

- 里程碑完成；
- 缺少无法从仓库确认的关键事实；
- 范围发生实质扩大；
- 授权发生冲突；
- 存在数据损失或不可逆风险；
- 操作超出 Direct Push 或高风险 PR standing authorization，或需要 Merge 授权。

### 权限边界

- Human 决定产品方向和最终结果；
- ChatGPT 担任 Tech Lead；
- Codex 担任执行型开发者；
- 不得虚构 Human Decision；
- 不得自行 Merge；
- 不得自行改变已接受的治理规则；
- 不得执行未授权的破坏性 Git 操作。

### 默认报告格式

- 完成了什么
- 没完成什么
- 测试结果
- 当前状态
- 风险
- 下一步
- Git 状态

## Handoff 快捷指令

### 触发条件

只有当用户明确发送以下口令之一时，才执行本节的 Handoff 收尾流程：

- `更新 Handoff`
- `更新handoff`
- `更新交接`
- `今天收尾`

口令可以附带用户明确提供的补充信息，例如：

`更新 Handoff，下一步先做 Daily 模块。`

此类消息仍视为快捷指令，并且用户明确指定的 Result、Next 或 Risk 优先于自动判断。普通开发任务结束、阶段完成或其他未包含上述明确口令的消息，不得自动更新 Handoff。

### 执行前判断

1. 检查当前对话中实际完成的仓库工作。
2. 以只读方式检查真实仓库状态，包括：
   - 当前分支和 HEAD；
   - `git status` 和 `git diff`；
   - 实际修改文件；
   - 最近 Commit；
   - 当前对话中有证据表明确实执行过的验证。
3. 仅总结本阶段的重要结果，不把普通小改动写成流水账。
4. 不得虚构测试、Commit、Push、PR、Merge 或完成状态。无法确认的信息写 `Unknown`。
5. 如果没有发现实际完成且值得恢复记录的阶段性仓库工作，不运行脚本、不改写 Handoff，并报告：

   `没有发现需要记录的阶段性工作，Handoff 未更新。`

### 自动总结

有可记录工作时，根据当前对话、Git 状态和用户补充内容生成：

- `Result`：本阶段真正完成的重要内容；
- `Next`：下一步最重要的一个动作；
- `Risk`：已确认的当前风险；没有已确认风险时使用 `None identified`。

用户明确提供的内容优先，不要求用户重新解释已经能从当前对话和仓库证据确认的信息。

### 本地执行

仅在上述触发和判断条件均满足时运行：

```powershell
.\scripts\finish_task.ps1 `
  -Result "<自动总结的实际结果>" `
  -Next "<自动判断或用户指定的下一步>" `
  -Risk "<已确认风险或 None identified>"
```

运行后必须检查：

- `00_System/Handoff/Latest.md` 已成功更新；
- 文件为覆盖更新，不是重复追加；
- 内容与真实仓库状态和当前对话证据一致。

### 严格边界

Handoff 快捷指令只允许本地更新 `00_System/Handoff/Latest.md`。执行时不得：

- Commit 或 Push；
- 创建或修改 PR；
- 将 PR 标记为 Ready；
- Merge；
- 删除、处理或切换分支；
- 修改七个第一层核心治理文件；
- 修改 Review Policy 或自动审查机制；
- 将普通小改动全部写入 Handoff。

### 回复格式

执行快捷指令后只使用以下格式回复：

```text
Handoff：已更新 / 未更新
本阶段完成：
当前风险：
下一步：
未提交文件：
远端操作：无
```
