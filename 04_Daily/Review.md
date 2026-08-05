## Purpose
Define the daily review workflow for confirming actual completion and producing the daily summary.

## Read By
Human, ChatGPT, Claude Code, Codex

## Update Frequency
Daily, during the end-of-day review cycle.

## Related Files
- 04_Daily/README.md
- 04_Daily/Today.md
- 04_Daily/Briefing.md
- 02_Learning/Current.md
- 03_Project

# Daily Review

## Scope

Daily review summarizes the user's actual day.

Daily briefing covers external developments and belongs in `04_Daily/Briefing.md`.

## Timezone

- Asia/Tokyo

## 00:00 Confirmation

At `00:00`, the user finishes work and the system initiates confirmation of the day's actual plan completion.

Ask or verify:

- What was actually completed?
- What was not completed?
- What was postponed?
- What was added unexpectedly?

Do not infer completion.

## 00:30 Daily Summary

At `00:30`, an external ChatGPT scheduled workflow produces a mobile-friendly daily review in Chinese.

The repository documents this workflow; it does not automatically schedule ChatGPT notifications.

Include when confirmed data exists:

1. Completed items.
2. Incomplete or postponed items.
3. Learning progress.
4. Project or system progress.
5. Health and energy status.
6. Daily score from 0 to 100.
7. Score explanation.
8. The single most important item for the next day.

## Scoring Rules

- Scoring must be explainable.
- Do not fabricate missing data.
- If the user has not confirmed enough information, mark relevant fields as `Not Confirmed`.
- Do not reward missing data.
- Do not punish missing data.
- Base the score only on confirmed plan, completion, constraints, and context.

## Review Template

### Completed Items

- Not Confirmed

### Incomplete or Postponed Items

- Not Confirmed

### Unexpected Additions

- Not Confirmed

### Learning Progress

- Not Confirmed

### Project or System Progress

- Not Confirmed

### Health and Energy Status

- Not Confirmed

### Daily Score

- Not Confirmed

### Score Explanation

- Not Confirmed

### Single Most Important Item for Tomorrow

- Not Confirmed