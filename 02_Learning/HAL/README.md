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

## Course Note Workflow

1. Teaching.
2. Lesson completion.
3. Required handoff to the relevant course `Notes.md`.
4. User writes notes.
5. AI reviews notes.
6. AI identifies errors or missing concepts.
7. User corrects notes.

AI-generated summaries are supplementary and must not replace user-authored notes.

## Boundaries

- Current cross-course learning status belongs in `02_Learning/Current.md`.
- Course-specific continuity belongs in each course `Current.md`.
- User-authored course notes belong in each course `Notes.md`.
- Daily school priorities belong in `04_Daily/Today.md`.
- Stable reusable explanations belong in `05_Reference`.