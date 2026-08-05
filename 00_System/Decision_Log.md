# Decision Log

## Document Status

- Status: Active
- Version: v0.6.0
- Authority: Authoritative record of significant system-level decisions within Yu-AI-OS, subordinate to Human authority and `AI_Constitution.md`
- Activation: Requires Human Acceptance before becoming Active
- Update Frequency: Only when a significant decision is proposed, accepted, rejected, withdrawn, superseded, or factually corrected

`v0.6.0 Active` is the current Human-accepted Decision Log baseline as of 2026-08-05. `DEC-0001` through `DEC-0006` are Accepted.

## Purpose

Yu-AI-OS needs a durable record of significant system-level decisions whose rationale and long-term effects cannot be reconstructed reliably from changed files alone.

This Decision Log preserves what was decided or formally proposed, why it was considered, whether the Human accepted it, what it affects, which material alternatives were considered, and which verifiable evidence supports its status. It also preserves the history of decisions that are rejected, withdrawn, or superseded when that history remains useful.

## One-Sentence Core

The Decision Log records significant Human-reviewed Yu-AI-OS decisions, their rationale, consequences, evidence, and supersession history.

## Responsibilities

The Decision Log is responsible for:

- recording significant system-level decisions and formal proposals;
- distinguishing Human-accepted decisions from proposals, rejections, withdrawals, and superseded decisions;
- preserving the context, rationale, material alternatives, consequences, and affected scope of each recorded decision;
- linking decisions to verifiable Pull Requests, commits, issues, Human Acceptance records, authoritative documents, or other Decision IDs;
- preserving stable Decision IDs and explicit supersession relationships; and
- providing the authoritative long-term record of why a qualifying Yu-AI-OS decision was made.

If this document were removed, Yu-AI-OS would lose its durable source for the rationale, Human Acceptance status, consequences, and supersession history of significant system-level decisions.

## Non-Responsibilities

The Decision Log does not:

- define or weaken the principles and authority boundaries in `AI_Constitution.md`;
- define how work or decisions are proposed, reviewed, approved, implemented, committed, or published; `Workflow.md` owns those procedures;
- define system design principles, document lifecycle rules, or responsibility-design methods; `System_Design_Guide.md` owns those rules;
- replace Git history, a changelog, or a document's Version History;
- record current progress, next actions, temporary context, or handoff state;
- serve as a task list, issue tracker, Daily record, or implementation journal;
- grant permission to implement, publish, merge, or otherwise execute a recorded decision; or
- infer Human Acceptance from silence, technical access, prior authorization, or automated review.

Recording a decision does not make it valid, accepted, or authorized for implementation. Any decision that conflicts with Human authority or `AI_Constitution.md` is invalid even if it appears in this log.

## What Must Be Recorded

A Decision Entry is required when a decision has lasting system-level significance, including:

- a system architecture choice;
- a change to a top-level directory or core module responsibility;
- a change to the authority hierarchy or a Single Source of Truth;
- a change to governance-document responsibility boundaries;
- a change to automation permissions or authorization models;
- a change to document lifecycle or version rules;
- a long-term rule affecting multiple modules;
- a significant security, privacy, credential, or data-boundary decision;
- a high-cost, difficult-to-reverse, or long-constraining choice; or
- a decision whose rationale the Human explicitly requires the system to preserve.

A qualifying entry must identify the decision's scope, Human Acceptance status, rationale, material consequences, and verifiable evidence.

## What Must Not Be Recorded

The following do not qualify by themselves:

- spelling, formatting, or other non-semantic corrections;
- ordinary commits;
- file moves that do not change responsibility or authority;
- Daily tasks, learning plans, or current work progress;
- temporary implementation details;
- ordinary bug fixes without lasting system-level consequences;
- ideas that have not become formal proposals;
- local choices without long-term impact;
- decisions invented only to make the log appear complete; or
- an AI inference that the Human has accepted a decision.

Not every commit or document version creates a Decision Entry. Entries must remain limited to decisions that meet the qualification criteria so this document does not become an unbounded miscellaneous record.

## Decision Statuses

- `Proposed`: A formal proposal exists but has not received explicit Human Acceptance.
- `Accepted`: The Human has explicitly accepted the decision, and the decision is currently valid.
- `Superseded`: A later Decision Entry has replaced the decision.
- `Rejected`: The proposal was reviewed and not accepted.
- `Withdrawn`: The proposer withdrew the proposal before Human Acceptance.

AI may draft a `Proposed` entry but may not mark a decision `Accepted` on its own. Only explicit, verifiable Human Acceptance can establish `Accepted` status.

Human silence, technical access, authorization for a previous task, permission to draft or implement, and a passing automated review do not constitute Human Acceptance.

Document lifecycle status and Decision Entry status are distinct. Human approval to include this file on `main` as a Draft does not constitute acceptance of any `Proposed` Decision Entry.

Merging a Draft Pull Request, creating a commit, placing a file on `main`, or receiving an automated review result does not by itself change a Decision Entry to `Accepted`. Document lifecycle status and Decision Entry status remain independent: only explicit, verifiable Human Acceptance can change a `Proposed` Decision to `Accepted`.

The current Decision Log baseline is `v0.5.0 Active`; `DEC-0001` through `DEC-0005` are Accepted. A future Draft version or newly merged Proposed Decision does not alter those established facts or automatically accept any new proposal.

A `Superseded` entry must remain in the log and identify the replacing Decision ID in `Superseded By`. Rejected and withdrawn entries may be retained when their history can prevent repeated consideration of the same question. A status change must cite verifiable evidence.

## Decision ID Rules

Decision IDs use a stable, continuous, repository-wide sequence:

```text
DEC-0001
DEC-0002
DEC-0003
```

- An assigned ID must never be reused.
- An ID remains reserved if its decision is rejected, withdrawn, or superseded.
- Numbering does not restart by year, version, status, or document section.
- A title may be clarified, but its Decision ID must remain unchanged.
- A superseded decision points to its replacement through `Superseded By`; the new decision points back through `Supersedes`.
- The next ID must be selected by checking the current Decision Log rather than relying on memory.

## Decision Entry Schema

Copy the following template for a new formal proposal:

```markdown
### DEC-0000 — Decision Title

- Status: Proposed
- Proposed Date: YYYY-MM-DD
- Decision Date: Pending
- Accepted By: Pending Human Review
- Scope:
- Related Documents:
- Related Modules:
- Supersedes: None
- Superseded By: None
- Evidence:

#### Context

Explain why this decision is needed.

#### Decision

State the decision being formally proposed or accepted.

#### Rationale

Explain why this option was selected.

#### Alternatives Considered

Identify material alternatives and why they were not selected.

#### Consequences

Describe expected benefits, constraints, costs, and risks.

#### Review and Acceptance

Record the Human review and acceptance state without inferring approval.

#### Notes

Include only supplementary information with long-term value.
```

Evidence may reference a Pull Request, commit SHA, issue, explicit Human Acceptance record, authoritative governance document, or another Decision ID. Evidence must be specific and verifiable.

An AI summary, unsaved chat memory, a vague reference to an earlier discussion, an automated-review result, or Human silence without a defined object must not be the sole evidence for a decision or status change.

## Recording and Update Rules

1. Add each new significant decision as a new Decision Entry.
2. Do not rewrite historical decisions to create the false appearance that the system never changed.
3. A factual error may be corrected, but the entry must retain a dated correction note and evidence for the correction.
4. When a decision changes materially, prefer a new Decision Entry and establish both `Supersedes` and `Superseded By` links.
5. Ordinary wording corrections do not require a new Decision Entry.
6. Every decision-status change requires verifiable evidence.
7. Current progress and follow-up tasks belong in Handoff, an issue, or the responsible task file.
8. The Decision Log is not a task-management system.
9. The Decision Log does not acquire execution authority merely by recording a decision.
10. Recording or accepting a decision does not itself authorize its implementation; implementation requires the authorization and workflow applicable to that action.
11. Historical backfill must be a separately scoped and reviewed task after the Human accepts this document's responsibility and format.

## Relationship to Other Sources

### Git History

Git history records which files changed, who committed a change, and in which commit it occurred. The Decision Log records why a qualifying decision was made, what the Human accepted, and what long-term effect the decision has.

Commits may be evidence for a Decision Entry, but ordinary commits must not be copied automatically into this log.

### Handoff

`Handoff/Latest.md` records current task state, unfinished work, next actions, and temporary recovery context. The Decision Log records formal proposals and accepted decisions with lasting system-level importance.

Temporary task state must not be stored in the Decision Log.

### Document Version History

A document's Version History records what changed in that document and which version contains the change. The Decision Log records why a qualifying decision affecting system direction, architecture, governance, authority, or responsibility boundaries was made.

An ordinary version increment does not automatically qualify as a system-level decision.

### Workflow

`Workflow.md` defines how work and decisions are proposed, reviewed, approved, implemented, committed, and published. The Decision Log preserves the results and rationale of decisions that meet its recording criteria.

This document does not redefine the complete workflow.

### AI Constitution

`AI_Constitution.md` defines the highest governance principles and authority boundaries within Yu-AI-OS, subordinate only to explicit Human authority. The Decision Log is subordinate to those rules and cannot amend, weaken, bypass, or legitimize a conflict with them.

### System Design Guide

`System_Design_Guide.md` defines system design principles, document responsibility boundaries, lifecycle states, and version rules. The Decision Log records qualifying decisions made within those constraints; it does not replace them.

## Decision Entries

### DEC-0001 — Establish the Yu-AI-OS Decision Log

- Status: Accepted
- Proposed Date: 2026-07-28
- Decision Date: 2026-07-28
- Accepted By: Human — explicit activation decision recorded in Pull Request #16
- Scope: System-level decision governance and durable decision records
- Related Documents: `00_System/AI_Constitution.md`, `00_System/System_Design_Guide.md`, `00_System/Workflow.md`, `00_System/Handoff/Latest.md`
- Related Modules: `00_System`
- Supersedes: None
- Superseded By: None
- Evidence: Draft Pull Request #15; initial commit `b2c35036fbae27faefd4a04948c6f16e3771c74e`; PR #15 Draft merge commit `270cd0aee47c4c387fbf6a88b1e856b510ff7aee`; activation candidate Pull Request #16; Candidate Commit 1 `07bb2fd2ceca87043890801925805c9baf8e08e7`; Candidate Commit 2 `537aed640cae6999928db2e55c06bc12d0aecb4f`; explicit Human Acceptance recorded in PR #16 on 2026-07-28; activation implementation commit `c2625143a6daaf4521e82511f30ad7ced281d633`; separate Human Merge Decision for PR #16 after final diff review; PR #16 Squash Merge Commit `604dcffa9c3b4dd12dbbc1362aff9c9fbbfbba8a`

#### Context

Before `DEC-0001` was accepted, Yu-AI-OS had authoritative sources for constitutional boundaries, system design, workflow, and temporary handoff state, but did not have a dedicated authoritative record for the rationale, Human Acceptance status, consequences, and supersession history of significant system-level decisions.

Git history can show what changed, and Handoff can preserve current task context, but neither source is responsible for explaining why a long-term governance or architecture decision was made.

#### Decision

Establish `00_System/Decision_Log.md` as the authoritative record of significant system-level Yu-AI-OS decisions.

The log will use stable Decision IDs and preserve each qualifying decision's context, rationale, material alternatives, consequences, verifiable evidence, Human Acceptance status, and supersession relationships. It will not serve as a Handoff, changelog, Git history mirror, or task-management system.

#### Rationale

A dedicated Decision Log makes long-term system choices reviewable without assigning decision rationale to sources that have different responsibilities. Stable IDs and explicit evidence allow later documents and decisions to reference the exact decision and its current status without relying on chat memory or inference.

#### Alternatives Considered

- Use Git history alone: rejected for this proposal because commits primarily record file changes and do not consistently preserve Human Acceptance, alternatives, or long-term rationale.
- Use `Handoff/Latest.md`: rejected for this proposal because Handoff is a dated snapshot of current work rather than a durable governance record.
- Use each document's Version History: rejected for this proposal because Version History explains document revisions, not cross-system decision rationale or supersession.
- Create a database or automation runtime: rejected for this proposal because a reviewed Markdown framework is sufficient for the current need and avoids unsupported complexity.

#### Consequences

As accepted, Yu-AI-OS gains a stable location for significant decision rationale, status, evidence, and supersession history. Contributors must apply the qualification criteria and avoid recording ordinary commits or temporary work.

The log will require disciplined maintenance when qualifying decisions change. It will not grant execution authority, and any implementation will remain subject to Human authorization, `AI_Constitution.md`, and `Workflow.md`.

#### Review and Acceptance

The Human explicitly accepted `DEC-0001` on 2026-07-28 and formally established and activated the Decision Log as the authoritative record for significant Human Decision rationale, evidence, status, and supersession history. This acceptance does not grant the Decision Log independent normative authority, authorize it to amend other authoritative documents, or automatically authorize future implementation actions.

PR #15 approved only the Draft merge and did not accept `DEC-0001`. The later explicit Human Decision recorded in PR #16 is the acceptance evidence. After that acceptance, the Human separately authorized Merge following final diff review, and PR #16 was published to `main` by Squash Merge Commit `604dcffa9c3b4dd12dbbc1362aff9c9fbbfbba8a`.

#### Notes

The initial Draft did not backfill earlier repository decisions. Historical backfill remains a separately scoped and Human-reviewed task and is not authorized by `DEC-0001`.

### DEC-0002 — Establish and Activate the Yu-AI-OS First-Layer Governance System

- Status: Accepted
- Proposed Date: 2026-07-28
- Decision Date: 2026-07-28
- Accepted By: Human — explicit activation decision recorded in Pull Request #16
- Scope: Responsibilities and unified activation of the seven first-layer core governance documents
- Related Documents: `00_System/AI_Constitution.md`, `00_System/Identity.md`, `00_System/Vision.md`, `00_System/Strategic_Goals.md`, `00_System/System_Design_Guide.md`, `00_System/Workflow.md`, `00_System/Decision_Log.md`
- Related Modules: `00_System`
- Supersedes: None
- Superseded By: None
- Evidence: Activation candidate Pull Request #16; Candidate Commit 1 `07bb2fd2ceca87043890801925805c9baf8e08e7`; Candidate Commit 2 `537aed640cae6999928db2e55c06bc12d0aecb4f`; explicit Human Acceptance recorded in PR #16 on 2026-07-28; activation implementation commit `c2625143a6daaf4521e82511f30ad7ced281d633`; separate Human Merge Decision for PR #16 after final diff review; PR #16 Squash Merge Commit `604dcffa9c3b4dd12dbbc1362aff9c9fbbfbba8a`

#### Context

Before this decision was accepted, Yu-AI-OS had seven Draft core documents that together covered first-layer governance, direction, design, execution, and durable decision evidence. Their responsibility relationship and activation boundary required review as one coherent decision before any of them became Active.

The accepted first layer includes Human Authority; the highest normative role of `AI_Constitution.md`; the direction roles of `Identity.md`, `Vision.md`, and `Strategic_Goals.md`; the design and execution roles of `System_Design_Guide.md` and `Workflow.md`; and the evidence and history role of `Decision_Log.md`.

#### Decision

The Human decided that:

- the seven core documents constitute the Yu-AI-OS first-layer governance system;
- `AI_Constitution.md` remains the highest normative document within Yu-AI-OS, subordinate only to explicit Human authority;
- `Decision_Log.md` is the evidence and historical record of significant Human Decisions, not an independent normative layer;
- current rules are maintained by the authoritative document responsible for each rule; and
- the seven accepted document versions are activated under the explicit Human Activation Decision recorded in Pull Request #16, with activation date 2026-07-28.

This decision was explicitly accepted by the Human on 2026-07-28. Its implementation was prepared in Pull Request #16. After Human Acceptance, the Human made a separate Merge Decision following final diff review, and PR #16 was published to `main` by Squash Merge Commit `604dcffa9c3b4dd12dbbc1362aff9c9fbbfbba8a`. The seven first-layer files thereby became the repository-current Active baseline on `main`.

#### Rationale

A unified activation review allows the Human to evaluate the seven documents as one responsibility system while preserving the distinct authority and Single Source of Truth of each document. It also avoids treating a merged Draft, a recorded proposal, or an automated review result as an implicit activation decision.

The accepted activation package was prepared from the latest `main` containing the AI Constitution and Decision Log Draft merges. Document versions remain independently managed according to the actual changes in each file rather than being forced to a shared version number.

#### Alternatives Considered

1. Continue leaving all seven documents Draft: this would have remained the safe fallback if Human review had not been completed, but it would not have established an operational first layer.
2. Activate the seven documents separately: not selected because partial activation could leave unclear or inconsistent responsibility boundaries.
3. Add the Decision Log to the numbered Authority Hierarchy: not selected because the log records decision evidence and history rather than serving as an independent normative layer.
4. Use the old `docs/activate-first-layer-foundation` branch directly: not selected because it predates PR #14 and PR #15 and therefore does not represent the latest governance baseline.
5. Upgrade every document to `v1.0.0` on first activation: not selected because versions should reflect each document's actual independent change history.

The accepted decision therefore uses a new activation package based on latest `main`, completes activation only after unified Human Review, keeps the Decision Log outside the numbered normative hierarchy, and manages versions per document.

#### Consequences

As accepted, this decision establishes the first-layer responsibility and authority model.

The Active lifecycle changes were implemented in Pull Request #16 with activation date 2026-07-28 and became the repository-current versions on `main` after the separately authorized Squash Merge.

Positive effects:

- the first-layer governance system becomes formally usable;
- authority sources and document responsibilities become clearer;
- AI and automation gain stable governance boundaries; and
- significant decisions can be traced over the long term.

Constraints and costs:

- all later modules must comply with the first layer;
- changes to core governance require stricter review;
- the Decision Log requires ongoing maintenance; and
- automatic review remains limited by truncation when reviewing long files.

These are the recorded consequences of the accepted decision and its authorized activation implementation.

#### Review and Acceptance

The Human explicitly accepted `DEC-0002` on 2026-07-28, confirmed the seven-document responsibility system, accepted the Constitution's highest normative position and the Decision Log's non-normative evidence and history responsibility, and authorized activation of the seven accepted versions in PR #16.

This acceptance is established by the explicit Human Decision, not by the existence of PR #16, a commit, or an automated review result. At the time of Human Acceptance, PR #16 remained unmerged; the Human later gave separate Merge authorization after final diff review, and the PR was Squash Merged to `main`.

#### Notes

The Human activation date is 2026-07-28. Automated review remains advisory and is not the acceptance evidence. Repository publication is recorded by PR #16 and Squash Merge Commit `604dcffa9c3b4dd12dbbc1362aff9c9fbbfbba8a`.

### DEC-0003 — Establish Risk-Proportional Yu-AI-OS Work Modes

- Status: Accepted
- Proposed Date: 2026-07-28
- Decision Date: 2026-07-28
- Accepted By: Human — explicit acceptance and local activation decision provided on 2026-07-28
- Scope: Yu-AI-OS task execution and Git authorization efficiency model
- Related Documents: `00_System/AI_Constitution.md`, `00_System/Workflow.md`, `00_System/System_Design_Guide.md`, `00_System/Handoff/Latest.md`
- Related Modules: system-wide
- Supersedes: None
- Superseded By: None
- Evidence: Local `Workflow.md` `v0.3.0 Draft` and `Decision_Log.md` `v0.3.0 Draft` candidate changes dated 2026-07-28; explicit Human Decision on 2026-07-28 accepting `DEC-0003`, the three work modes, and Human-triggered Handoff; explicit authorization in the same Human Decision to activate locally `AI_Constitution.md` `v0.2.1`, `Identity.md` `v0.0.4`, `Workflow.md` `v0.3.0`, and `Decision_Log.md` `v0.3.0`; no Commit, Push, PR, or Merge was performed as part of that local activation; a later Human instruction on 2026-07-29 authorized unified Stage Sync to the existing Draft PR #17, with the resulting Commit and PR state to be verified from Git and GitHub after execution

#### Context

Existing Yu-AI-OS rules already require workflow complexity to remain proportional to risk. In practice, ordinary README, Handoff, navigation, and local maintenance work has sometimes been split into repeated PR, review, and authorization steps. That overhead slows progress toward a practically usable system without adding proportional protection.

A clearer work-mode model is needed to reduce low-value process cost while preserving Human Authority, truthful reporting, scope control, independent Merge authorization, and full review for consequential governance changes.

#### Decision

Establish three work modes:

1. Local Work Mode, the default for authorized local edits, checks, and tests without Git or external writes.
2. Stage Sync Mode, in which one scope-specific Human instruction may authorize all or part of `git add`, Commit, Push, and creation of a Draft PR as a coordinated stage operation.
3. Governance Change Mode, which retains full authoritative-file reading, candidate-version identification, Human Review, explicit Human Acceptance, and separate Activation and Merge authorization for high-risk governance work.

Stage Sync Mode never includes Merge. Governance Change Mode preserves complete review. Handoff is manually triggered by the Human and generated semi-automatically through the local script; it is not updated after every task.

#### Rationale

The proposed model reduces low-value process cost, concentrates risk controls on genuinely consequential operations, accelerates Yu-AI-OS toward practical use, and preserves Human Authority and traceability.

#### Alternatives Considered

1. Require the complete PR workflow for every task: not selected because it imposes disproportionate cost on low-risk local work.
2. Automatically Commit and Push all ordinary work: not selected because it creates excessive authorization and repository-noise risk.
3. Automatically update Handoff after every task: not selected because it encourages redundant, low-value activity logs.
4. Use Human-triggered Handoff with script-generated content: selected as the proposed approach because it combines deliberate timing with efficient and evidence-based generation.
5. Remove governance review entirely: not selected because it violates first-layer principles and Human Authority.

#### Consequences

Positive effects:

- ordinary work can proceed faster;
- Handoff remains more concise;
- repeated authorization requests are reduced; and
- high-risk governance work remains isolated.

Constraints:

- AI must select the correct mode;
- expanded scope or risk requires renewed authorization and mode assessment;
- Stage Sync Mode cannot authorize Merge; and
- the Human may narrow, revoke, or terminate authorization at any time.

#### Review and Acceptance

The Human explicitly accepted `DEC-0003` on 2026-07-28 after reviewing the final candidate. The accepted decision establishes Local Work Mode, Stage Sync Mode, and Governance Change Mode, together with Human-triggered, script-assisted Handoff generation.

The Human authorized only local Activation of the four reviewed candidate versions in this decision. This acceptance and local Activation do not authorize Commit, Push, creation or modification of a PR, or Merge. Merge continues to require a separate, explicit Human Decision.

#### Notes

The local Activation established the accepted versions in the working tree. A later Human instruction on 2026-07-29 separately authorized the milestone Stage Sync to Draft PR #17. Durable Git and remote evidence must be taken from the operations that actually complete; no nonexistent Commit SHA, Push result, or Merge is claimed here.

### DEC-0004 — Establish and Activate Board V1.0

- Status: Accepted
- Proposed Date: 2026-08-04
- Decision Date: 2026-08-04
- Accepted By: Human — explicit acceptance and local activation authorization provided on 2026-08-04
- Scope: Board V1.0 organization, role responsibilities, daily lightweight checks, and full Board activation boundary
- Related Documents: `00_System/Board.md`, `00_System/ChatGPT_Project_Instructions.md`, `AGENTS.md`, `README.md`
- Related Modules: system-wide
- Supersedes: None
- Superseded By: None
- Evidence: Explicit Human Decision on 2026-08-04 accepting the reviewed `00_System/Board.md` V1.0 content and authorizing its local activation; local `Board.md` v1.0.0 Active implementation; no Commit, Push, PR, or Merge was authorized or performed as part of this decision

#### Context

Yu-AI-OS needed a clear decision-review structure that separates Human final authority, lightweight daily value and simplification checks, full multi-role review, and execution responsibilities without introducing a meeting runtime or automated decision system.

#### Decision

The Human accepted Board V1.0 and authorized local activation of `00_System/Board.md` v1.0.0. Daily mode uses CVO and CSO only as lightweight checks. Full Board review starts only when the Human uses a documented activation phrase. All roles remain advisory, and the Human retains final decision authority.

#### Rationale

One concise Board document makes role boundaries and review modes available across the system while avoiding duplicated role files, unnecessary meeting machinery, and changes to existing constitutional or workflow authority.

#### Alternatives Considered

1. Keep Board V1.0 as Draft: not selected because the Human reviewed and explicitly accepted the current content.
2. Expand immediately into a complete meeting mechanism or runtime system: not selected because it is outside V1.0 scope and would add unproven complexity.
3. Split every role into a separate file: not selected because one file remains clear and easier to maintain.

#### Consequences

Yu-AI-OS gains an Active source for Board organization, role boundaries, daily CVO and CSO checks, and Human-triggered full review. This does not add voting, multi-Agent behavior, Skill routing, memory, a Decision Engine, or implementation authority. Existing Constitution and Workflow rules continue to govern Human Authority and execution permissions.

#### Review and Acceptance

The Human explicitly accepted the reviewed Board V1.0 content and authorized its local activation on 2026-08-04. This acceptance also explicitly excludes scope expansion, complete meeting-mechanism design, voting, multi-Agent implementation, Skill Router, Memory System, Decision Engine, complete Skill Framework, and Merge.

#### Notes

No Commit, Push, PR, or Merge evidence is claimed. Any later expansion of Board responsibilities or meeting mechanisms requires separate scope and review.

### DEC-0005 — Replace Long-Form AI Review with a Concise Executive Summary

- Status: Accepted
- Proposed Date: 2026-08-04
- Decision Date: 2026-08-04
- Accepted By: Human — explicit direction and implementation authorization provided on 2026-08-04
- Scope: Pull Request decision support and deterministic automatic checks
- Related Documents: `00_System/Review/Policy.md`, `00_System/Workflow.md`, `README.md`
- Related Modules: `.github/workflows`, `.github/scripts`, `00_System/Review`
- Supersedes: None
- Superseded By: None
- Evidence: Explicit Human instruction on 2026-08-04 accepting removal of the long DeepSeek AI Review and replacement with a concise Chinese Executive Summary plus useful deterministic checks; implementation prepared on `agent/simplify-review-summary`; Commit, Draft PR, and Merge evidence must be recorded from operations that actually complete

#### Context

The existing DeepSeek review produced long English-heavy and implementation-heavy comments that the Human did not read and that did not effectively support Merge decisions. Its prompt construction, diff payload handling, redaction, retry, model-output validation, severity grouping, and long comment formatting created ongoing complexity without proportional Human value.

#### Decision

Remove the long-form DeepSeek review and stop sending Pull Request content to DeepSeek or any other LLM. Replace it with one short Chinese Executive Summary based on structured PR text, GitHub metadata, and real deterministic check results.

The summary must remain readable in about 20–30 seconds, update one stable marker comment, state missing PR sections without guessing, and keep Human Review and Merge authorization separate from automated check results.

#### Rationale

The concise summary directly supports the Human's actual decision task while deterministic checks provide more reliable evidence than model guesses for syntax, formatting, links, and basic file validity. Removing unused model infrastructure also reduces cost, secret exposure surface, failure modes, and maintenance burden.

#### Alternatives Considered

1. Keep DeepSeek and shorten only its prompt: not selected because the model call and its supporting complexity would remain despite low Human value.
2. Keep the old reviewer behind a compatibility flag: not selected because it would create an unused zombie system.
3. Remove all automation: not selected because a short summary and a small set of deterministic checks provide useful decision support at low cost.

#### Consequences

Pull Requests no longer receive AI findings or severity categories. They receive a concise Chinese summary and deterministic check results instead. The `DEEPSEEK_API_KEY` is no longer referenced by repository code or workflow and may be removed from repository settings by the Human when convenient.

Automation remains advisory and cannot approve or merge a Pull Request. Missing structured PR sections become visible rather than being inferred.

#### Review and Acceptance

The Human explicitly accepted this direction and authorized its implementation, Commit, Push, and Draft PR creation on 2026-08-04. This acceptance does not authorize Ready for Review or Merge. Merge remains a separate Human Decision after reviewing the actual Draft PR.

#### Notes

No Merge evidence is claimed. Commit and Draft PR evidence must be taken from the operations that actually complete.

### DEC-0006 — Establish Risk-Based Direct Push and Pull Request Routing

- Status: Accepted
- Proposed Date: 2026-08-05
- Decision Date: 2026-08-05
- Accepted By: Human — explicit standing authorization and revocation boundary confirmed on 2026-08-05
- Scope: Git add, Commit, Push, branch, and Draft Pull Request routing for `yuhaojie6275-bot/Yu-AI-OS`
- Related Documents: `00_System/AI_Constitution.md`, `00_System/Workflow.md`, `00_System/ChatGPT_Project_Instructions.md`, `AGENTS.md`, `.github/workflows/executive-summary.yml`
- Related Modules: system-wide
- Supersedes: None
- Superseded By: None
- Evidence: Explicit Human instruction on 2026-08-05 defining ordinary Direct Push, seven high-risk PR triggers, meaningful Commit Messages, and post-Push reporting; subsequent explicit Human confirmation that the authorization remains valid until “停止直推” or “恢复 PR 模式”, while Merge, force push, history rewriting, and destructive operations remain separately authorized

#### Context

The previous workflow required operation-specific Git authorization and commonly used branch-and-PR publication even for ordinary changes. The repository has no Action or script that creates Pull Requests automatically, and `main` currently has no branch protection or ruleset requiring PRs.

#### Decision

For this repository, ordinary reviewed and validated changes use a bounded standing authorization for scoped `git add`, meaningful Commit, and Push directly to `main`, without a Pull Request. Database schema changes, deletion of more than 10 files, GitHub Actions or CI/CD changes, dependency manifest or lockfile changes, system Prompt or core/security rule changes, changes exceeding 30 files, and explicit Human PR or Review requests use a development branch and Draft PR. Merge is never automatic.

The standing authorization remains valid until the Human says “停止直推” or “恢复 PR 模式”. Force push, Amend, Rebase, Reset, history rewriting, Merge, destructive operations, repository-setting changes, and work outside the current task remain outside this authorization.

#### Rationale

Direct Push removes low-value PR overhead for ordinary work, while objective high-risk triggers preserve review where mistakes have larger technical, dependency, automation, governance, or change-scope impact.

#### Alternatives Considered

1. Require a PR for every change: not selected because it adds disproportionate process cost to ordinary work.
2. Direct Push every change: not selected because database, CI/CD, dependency, governance, destructive, and large-scope changes require stronger review.
3. Add a new automation service to route changes: not selected because clear repository instructions are sufficient and avoid unnecessary runtime complexity.

#### Consequences

Ordinary changes no longer create PRs and are reported after a successful Push. High-risk changes automatically create Draft PRs but still require a separate Human Merge decision. Correct risk classification, clean scope checks, meaningful Commit Messages, and truthful validation reports remain mandatory.

#### Review and Acceptance

The Human explicitly defined the routing rules and then confirmed the standing authorization and its revocation phrases on 2026-08-05. This decision does not authorize Merge, force push, history rewriting, destructive operations, or unrelated repository changes.

#### Notes

The GitHub Actions Executive Summary workflow still supports Pull Requests when the high-risk path is used. Its Chinese display names do not change permissions, triggers, trusted-base behavior, or deterministic check logic.

## Version History

| Version | Status | Summary |
| --- | --- | --- |
| v0.1.0 | Draft | Initial Human-reviewable Decision Log framework with one proposed establishment decision. |
| v0.2.0 | Draft | Added the proposed DEC-0002 activation decision and PR #15 merge evidence; DEC-0001 and DEC-0002 remain Proposed, and the Decision Log remains unactivated. |
| v0.2.0 | Active | Activated on 2026-07-28 by explicit Human Acceptance recorded in PR #16; DEC-0001 and DEC-0002 were accepted, AI or automated review received no final decision authority, and the separately authorized PR #16 Squash Merge published the version to `main`. |
| v0.3.0 | Draft | Human Review candidate that corrects PR #16 post-publication facts, keeps DEC-0001 and DEC-0002 Accepted, and adds DEC-0003 as Proposed; no Human Acceptance or Activation is claimed for this candidate. |
| v0.3.0 | Active | Activated locally on 2026-07-28 by explicit Human Acceptance; corrects PR #16 publication history, accepts DEC-0003, and activates the risk-proportional work modes without claiming Commit, Push, PR, or Merge evidence. |
| v0.4.0 | Active | Updated locally on 2026-08-04 under explicit Human Decision; adds accepted DEC-0004 and records Board V1.0 local activation without claiming Commit, Push, PR, or Merge evidence. |
| v0.5.0 | Active | Updated under explicit Human Decision on 2026-08-04; adds accepted DEC-0005 replacing long-form DeepSeek review with a concise Chinese Executive Summary and deterministic checks, while keeping Merge separately authorized. |
| v0.6.0 | Active | Updated on 2026-08-05 under explicit Human Decision; adds accepted DEC-0006 and records risk-based Direct Push and Draft PR routing with explicit revocation and preserved Merge boundaries. |
