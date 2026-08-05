## Purpose
Define the operational specification for the user's daily briefing.

## Read By
Human, ChatGPT, Claude Code, Codex

## Update Frequency
When briefing goals, topics, selection rules, or output rules change.

## Related Files
- 04_Daily/README.md
- 04_Daily/Today.md
- 04_Daily/Review.md
- 02_Learning/Current.md
- 01_Career/Roadmap.md

# Daily Briefing

## Scope

Daily briefing covers external developments, not the user's actual day.

Daily review belongs in `04_Daily/Review.md`.
## Architecture

- `04_Daily/Briefing.md` is the canonical briefing specification.
- The external ChatGPT scheduled daily briefing is the execution mechanism.
- Yu-AI-OS does not contain a second briefing engine.
- This repository does not automatically send briefings or schedule ChatGPT notifications.

## Synchronization Rule

When briefing requirements change, update this specification first, then synchronize the external ChatGPT scheduled task.

## User Goals

The briefing should help the user:

- Discover earning opportunities.
- Discover entrepreneurship opportunities.
- Improve learning efficiency.
- Improve job-search efficiency.
- Understand major changes.
- Discover directly usable tools.

## Priority Topics

- AI
- Programming
- Technology
- Studying in Japan
- HAL-related developments when relevant
- Employment in Japan
- Earning opportunities
- Entrepreneurship opportunities
- Funds and market developments

## Geographic Priority

1. China
2. Japan
3. Global developments only when materially relevant

## Reading Time

- Normal target: about 2 minutes.
- Major news days: about 3 to 4 minutes.
- Exceptional situations: maximum about 5 minutes.

## Output Structure

For important items, answer:

1. What happened?
2. Why does it matter to the user?
3. What can the user do now?

## Selection Rules

- Prioritize material developments.
- Avoid low-value noise.
- Avoid repeating unchanged stories.
- Prefer actionable information.
- Clearly distinguish facts from inference.
- Use current information.
- Verify dates.
- Use reliable sources.
- Prioritize direct relevance to the user's goals.

## Fund and Market Rules

The user is interested in funds, but the briefing should not become a generic market-news dump.

- Highlight only material changes.
- Explain why the change matters.
- Avoid pretending short-term market movements are predictable.
- Distinguish market facts from interpretation.
- Surface risks when relevant.

## Quality Rules

- The briefing shown to the user should be Chinese-first.
- HAL-specific terminology may include Japanese where useful.
- Other AI and technical content does not need Japanese explanations by default.
- Keep the briefing concise and directly useful.
- Do not include filler items just to make the briefing look complete.