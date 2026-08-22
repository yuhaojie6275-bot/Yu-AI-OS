## Purpose
Define how HAL coursework learning state should be organized and maintained.

## Read By
Human, ChatGPT, Claude Code, Codex

## Update Frequency
When HAL coursework status, course boundaries, or study rules change.

## Related Files
- 02_Learning/README.md
- 02_Learning/Current.md
- 02_Learning/HAL/WF15/README.md
- 02_Learning/HAL/JV15/README.md
- 02_Learning/HAL/CS15/README.md
- 02_Learning/HAL/DB15/README.md
- 04_Daily/Today.md

# HAL Learning

## Module Responsibility

- Track HAL course-specific learning state.
- Preserve confirmed coursework context.
- Help AI collaborators continue explanations from the correct level.
- Keep school learning connected to daily execution when needed.
- Support user-authored course notes and AI review.

## Operating Rules

- HAL course-specific learning state belongs here.
- Japanese terminology may be preserved when useful for HAL coursework.
- Explanations for the user should remain Chinese-first.
- Course-specific folders are allowed for confirmed active HAL courses.
- Do not create speculative courses that have not been confirmed.
- Avoid duplicating the same knowledge across multiple courses.
- Do not mark coursework complete unless completion is confirmed.
- Do not infer completion, prerequisites, teacher requirements, textbook structure, or lesson content.
- Use `Confirmed`, `In Progress`, `Not Started`, `Not Confirmed`, or `Unknown` when status clarity is needed.
- Previously encountered topics may be recorded as exposure or study activity, not assumed mastery.
- Accuracy is more important than completeness.
- Acceptable evidence includes explicit user confirmation, repository evidence, actual lesson records, provided course materials, provided screenshots, and provided recordings or transcripts.
- Each course may use a different file structure according to its actual maintenance needs.
- The course README is the authoritative entry point for that course's teaching approach and directory structure.

## Course Continuity and Notes

Each course README defines whether and how continuity or notes are maintained. No course is required to contain `Current.md` or `Notes.md`; user-authored notes may remain outside the repository.

AI-generated summaries are supplementary and must not replace user-authored notes.

## Boundaries

- Current cross-course learning status belongs in `02_Learning/Current.md`.
- Course-specific continuity and directory structure belong in each course README.
- User-authored course notes follow the storage and handoff rules defined by that course; no fixed filename is required.
- Daily school priorities belong in `04_Daily/Today.md`.
- Stable reusable explanations belong in `05_Reference`.
