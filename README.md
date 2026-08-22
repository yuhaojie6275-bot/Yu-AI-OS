# Yu-AI-OS

Yu-AI-OS 是 Human 与 AI 协作建设的个人操作系统。它用稳定的治理、身份、方向、工作流程和决策记录，为长期开发提供一致的责任边界和可信事实来源。Human 始终拥有最终决定权。

## 当前状态

第一层核心治理已经完成，七个核心治理文件均为 Active。Pull Request 默认运行确定性基础检查；自动化结果仅为 advisory，不能代替 Human Review 或 Merge Approval。Codex 任务报告和 GitHub diff 提供变更摘要，不再运行重复的 AI 执行摘要层。

第一层完成不代表后续功能系统已经实现。下一里程碑是 **Skill Framework**。

## 角色与开发方式

- **Human**：提出需求、决定产品方向、进行重要授权并作出最终 Merge 决定。
- **ChatGPT**：担任 Tech Lead，拆解需求、定义里程碑、指导 Codex 并向 Human 集中汇报。
- **Codex**：担任执行型开发者，连续完成里程碑所需的代码、文档、测试和自检。

默认采用里程碑开发模式，不为单个文件或普通小调整制造低价值中断。Git 写入、Push、PR 和 Merge 仍必须遵守 [Workflow](00_System/Workflow.md) 的明确授权边界。

## 重要入口

- [AI Constitution](00_System/AI_Constitution.md)：最高治理原则、Human Authority 和权限边界。
- [System Design Guide](00_System/System_Design_Guide.md)：系统结构、文档职责和生命周期规则。
- [Workflow](00_System/Workflow.md)：协作模式、里程碑开发、审核和 Git 授权流程。
- [Board](00_System/Board.md)：决策评审层、角色职责、日常轻量检查和完整 Board 启停边界。
- [Decision Log](00_System/Decision_Log.md)：重要 Human Decision 的理由、证据和状态。
- [Latest Handoff](00_System/Handoff/Latest.md)：用于恢复工作的 dated snapshot，不是治理权威。
- [Deterministic Checks Policy](00_System/Review/Policy.md)：确定性检查和 advisory 边界。
- [ChatGPT Project Instructions](00_System/ChatGPT_Project_Instructions.md)：可复制到 ChatGPT Project 的 Tech Lead 启动说明，不是治理权威。

## 下一阶段

下一里程碑是 **Skill Framework**。Skill Router、Memory System、Decision Engine 等能力尚未开始，不应描述为已经完成。
