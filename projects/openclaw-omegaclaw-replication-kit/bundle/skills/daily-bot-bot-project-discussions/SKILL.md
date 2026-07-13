---
name: "daily-bot-bot-project-discussions"
description: "Protocol for daily cross-agent project discussions: scheduled bot-bot review of each active project with skip-on-pivot and channel routing rules."
---

# Daily Bot-Bot Project Discussion Protocol

## Purpose

Active research projects ownerefit from a lightweight daily cross-agent review: the OpenClaw agent and the OmegaClaw agent briefly discuss each active project's direction, risks, and next steps. This skill standardizes that protocol so new projects get automatic discussion slots and the pattern is reusable.

## When to use

- Multiple active research/engineering projects with recurring workers or ongoing work.
- Two or more agents can exchange short structured discussions in a shared channel.
- A dedicated discussion channel exists (e.g., the dedicated bot-to-bot channel).

## Prerequisites

- A dedicated Telegram channel for bot-bot discussions (e.g., `telegram:<BOT_DISCUSSION_GROUP_ID>`).
- Both participating agents have channel read/write access configured.
- A project catalog (`catalog/PROJECTS.md`) listing active projects.
- A schedule file (e.g., `catalog/DAILY_BOT_BOT_PROJECT_DISCUSSIONS.md`) recording time slots.

## Protocol

### 1. Scheduled discussion seed

For each active project, one daily cron job triggers at the assigned time slot:

1. Read `projects/<slug>/PROJECT.md`, `TASKS.md`, `DECISIONS.md`, `NOTES.md`, and recent memory.
2. Check if a pivot/major-status/major-problem discussion already occurred for this project within the last 24 hours. If yes, reply `NO_REPLY` and skip.
3. Otherwise, post a concise discussion starter to the bot-bot channel addressed to the other agent:
   - Current focus and latest notable worker/result
   - Strongest current next step
   - Risks, blockers, stale assumptions, or possible pivot
   - Desired outcome

### 2. Discussion format

```text
Daily bot-bot project discussion: <slug>
Context: <current focus and latest result>
Discuss with @<other-agent>:
- What changed since the previous discussion?
- What is the strongest current next step?
- Any risk, blocker, stale assumption, or possible pivot?
- What should be recorded, scheduled, or handed off?
Outcome: 1-3 concise bullets, with a next action or NO_REPLY if suppressed.
```

### 3. Immediate discussion on pivots

If a pivot, major status change, or major problem occurs outside the scheduled slot, start the project discussion immediately in the bot-bot channel rather than waiting for the next slot. The scheduled slot should then suppress itself if the immediate discussion happened within 24 hours.

### 4. Auto-discovery

A daily auto-discovery cron job (e.g., 6:30AM) should:
1. Scan `catalog/PROJECTS.md` for new active projects.
2. Assign them a discussion time slot.
3. Create the corresponding cron job.
4. Disable discussion jobs for projects that are completed or paused.

### 5. Channel routing

- **Bot-bot discussions**: dedicated channel (e.g., `telegram:<BOT_DISCUSSION_GROUP_ID>`).
- **Scheduled progress updates**: scheduled-updates channel (e.g., `telegram:<SCHEDULED_UPDATES_GROUP_ID>`).
- **Daily human-facing summary**: human summary channel (e.g., `telegram:<HUMAN_SUMMARY_GROUP_ID>`), once daily at 7AM Pacific.
- Do not spill detailed bot-bot discussion into the main human summary channel.
- If channel routability fails, alert the owner concisely and avoid spilling into wrong channels.

## Guardrails

- This protocol is advisory/review, not a license to spend money, publish, merge, force-push, change access controls, or take destructive/security-sensitive actions.
- Project records remain the source of truth. Discussions should point back to `projects/<slug>/` files.
- Keep bot-bot back-and-forth selective — if extended discussion is needed, suggest moving to a dedicated subchannel.

## Onboarding a new project

1. Add the project to `catalog/PROJECTS.md`.
2. Assign a daily discussion time slot in `catalog/DAILY_BOT_BOT_PROJECT_DISCUSSIONS.md`.
3. Create a cron job for that slot using the standard template.
4. Add the project to the auto-discovery scan list.
5. If the project has a progress worker, ensure the discussion complements rather than duplicates it.

## Relationship to other protocols

- **Recurring project progress workers**: workers advance work; daily discussions review direction. Complementary.
- **Collective experiment loop** (OmegaSim-style): the discussion protocol generalizes the collective-loop discussion step for any project.
- **Scheduled updates channel**: progress workers report there; daily discussions happen in the bot-bot channel.
