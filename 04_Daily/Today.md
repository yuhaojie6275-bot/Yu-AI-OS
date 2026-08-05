## Purpose
Provide a lightweight daily execution document for current priorities, constraints, and review.

## Read By
Human, ChatGPT, Claude Code, Codex

## Update Frequency
Daily, or when priorities materially change during the day.

## Related Files
- 04_Daily/README.md
- 04_Daily/Briefing.md
- 04_Daily/Review.md
- 00_System/Strategic_Goals.md
- 02_Learning/Current.md
- 03_Project

# Today

## Daily Direction

- Daily planning must support the Strategic Mission in `00_System/Strategic_Goals.md`.
- The main long-term direction is becoming an AI Full Stack Engineer before March 2028.
- Daily execution should prioritize reusable long-term assets: projects, code, notes, documentation, automation, and reviewable PRs.

## Date / Timezone

- Date: <!-- TODO: Set today's date when using this file. -->
- Timezone: Asia/Tokyo

## Most Important Task

- MIT: <!-- TODO: Set exactly one specific and realistic Most Important Task. -->
- Each day has exactly one Most Important Task.
- MIT means the one core event that makes the day successful if completed.
- MIT does not mean only one task can be done.
- Supporting tasks are allowed after the MIT is clear.

## Top Priorities

- <!-- TODO: Add confirmed top priorities for today. -->

## Hard Deadlines

- <!-- TODO: Add confirmed hard deadlines, if any. -->

## Learning Focus

- <!-- TODO: Add today's confirmed learning focus. -->

## Project Focus

- <!-- TODO: Add today's confirmed project focus, if any. -->

## Health / Energy Check

- <!-- TODO: Add current health, sleep, or energy constraints if relevant. -->

## Optional Tasks

- <!-- TODO: Add optional tasks only after required work is clear. -->

## End-of-Day Note

<!-- TODO: Add a short end-of-day note after real work is done. -->

## Fixed School Times

- Period 1: 09:30-11:00
- Period 2: 11:10-12:40
- Period 3: 12:50-14:20
- Period 4: 14:30-16:00
- Period 5: 16:10-17:40

## Work Shift Notation

- `18-3F` means work starts at 18:00 on 3F.
- `18-2F` means work starts at 18:00 on 2F.
- `18-B1` means work starts at 18:00 on B1.
- `13-B1` means work starts at 13:00 on B1.
- `17-2F` means work starts at 17:00 on 2F.
- Work normally ends at 24:00.
- The user normally gets home around 01:00.

## Commute Rules

### Online Class Day

- No morning school commute.
- If there is work that day, leave home 1 hour before work.

### Offline School Day

- Leave home at 08:30 for school.
- After classes, the user may stay in the school study room or library.
- Leave school 30 minutes before work.

### Friday Transition Note

- Period 5 ends at 17:40 and work may start at 18:00.
- This is feasible because the user can arrive just in time and the manager allows a few minutes of delay.
- Still mark it as a high-pressure transition.

## Late Study Block

- On work days, work continues until 24:00.
- On work days, home arrival is around 01:00.
- Late Study Block: 01:10-02:40.

Allowed Late Study Block tasks:

- school review
- programming practice
- AZ-900 study
- Japanese study
- light fund learning

Forbidden during Late Study Block:

- merging PRs
- modifying `main`
- high-risk Git operations
- major architecture decisions
- complex conflict resolution

## Japanese Usage Rule

- Commute / fragmented time: vocabulary, short phrases, listening, shadowing.
- Quiet study blocks: grammar, reading, interview Japanese, technical Japanese.
- Daily minimum target: 10-15 minutes when realistic.

## AZ-900 Rule

- AZ-900 exam date: July 22.
- Starting level: beginner / zero baseline.
- Goal: pass AZ-900.
- Recommended daily use: 30-60 minutes when possible.
- On heavy days, use part of the Late Study Block.
- AZ-900 must not replace project-based learning.

## Fund Learning Rule

- Starting level: zero.
- Normal day: up to 10 minutes.
- Very busy day: may skip.
- Weekly summary: about 30 minutes when possible.
- Do not make real investment decisions from incomplete understanding.

## Health Rule

- Health is not a default forced daily management item.
- When the user explicitly says they are close to breaking down, exhausted, or cannot continue, health management becomes active.
- In that case, recommend rest, workload reduction, sleep protection, and risk control.

## No Fake Completion

- Unfinished tasks must be recorded as postponed or incomplete.
- Do not pretend unfinished work was completed.
- Do not invent progress.
- Do not invent study mastery.

## Temporary Final-School-Week Planning Note

This schedule is provisional based on the previous week's pattern. Do not treat the work schedule as final.

- Monday: online IH15 / SD15, work starts 18:00 on 3F.
- Tuesday: offline JV15 / JV15 / CS15 / SL12, no work assumed.
- Wednesday: offline WF15 / DB15 / FX12, work starts 18:00 on 2F.
- Thursday: offline CS15 / CS15, work starts 18:00 on B1.
- Friday: offline CT15 / JV15 / unknown period 3 / WF15 / WF15, work starts 18:00 on B1, high-pressure but feasible transition after period 5.
- Saturday: work starts 13:00 on B1.
- Sunday: work starts 17:00 on 2F.

## Prioritization Rule

1. Health or urgent personal constraints.
2. Hard deadlines.
3. HAL coursework and required school work.
4. Current learning bottleneck.
5. Active project work.
6. Yu-AI-OS maintenance.
7. Optional tasks.

Yu-AI-OS maintenance should normally remain below real study and project work unless the system issue is directly blocking them.

## Daily Review Handoff

- At `00:00` Asia/Tokyo, move to `04_Daily/Review.md` and confirm actual completion.
- At `00:30` Asia/Tokyo, the external ChatGPT scheduled workflow uses confirmed review data to prepare the Chinese daily review.
- Do not infer completion from this file alone.
- This repository does not automatically schedule the 00:30 workflow.