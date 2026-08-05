## Purpose
Define the repository-level handoff mechanism for passing concise execution context between Human and AI collaborators.

## Read By
Human, ChatGPT, Claude Code, Codex

## Update Frequency
When handoff rules, ownership, or required fields change.

## Related Files
- 00_System/Handoff/Latest.md
- 00_System/Workflow.md
- 00_System/Vision.md

# Handoff

## Handoff Rules

1. Record facts only.
2. Do not invent validation.
3. Do not claim tests were run if they were not run.
4. Do not claim commit or push if they did not happen.
5. Keep the latest handoff concise.
6. The Human remains the final decision-maker.

## Required Fields

- Task
- Executor
- Date
- Changes
- Files Created
- Files Modified
- Tests / Validation
- Conflicts
- Risks
- Recommendations
- Commit Status
- Next Reviewer
- Next Suggested Action

## Ownership

- The current executor updates `00_System/Handoff/Latest.md` after meaningful repository work.
- The Human owns final approval and priority decisions.
- The next AI reviewer may use the handoff as context, but must still verify facts when necessary.

## Limitations

- This is a repository-level handoff record.
- This file does not automatically inject context into a specific ChatGPT conversation.
- This mechanism does not replace direct user confirmation.
- This mechanism does not create commits, push changes, or run scheduled workflows.