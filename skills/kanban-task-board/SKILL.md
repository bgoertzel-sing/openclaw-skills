---
name: "kanban-task-board"
description: "Maintain project Kanban boards and recurring task reviews."
---

# Kanban task board

Use when work spans many one-off or recurring tasks, multiple projects, subagents, or machines, and the user wants a board/status view rather than prose-only summaries.

## Board sources

- Prefer durable project records under `projects/<slug>/` for project-specific tasks.
- Use `catalog/KANBAN.md` as the cross-project board index when present.
- Link out to `projects/<slug>/TASKS.md`, issue/PR IDs, experiment run dirs, and session/job identifiers rather than duplicating long detail.
- Do not treat transient chat summaries as authoritative if project records or repo state disagree.

## Workflow

1. Identify the active scope: global, project, machine, or subagent family.
2. Inspect existing board/project task files before editing.
3. Normalize tasks into lanes:
   - Backlog
   - Ready / Next
   - In Progress
   - Blocked / Needs Ben
   - Waiting / Scheduled
   - Done / Archived
4. For each card, keep a compact record:
   - title
   - project or machine
   - owner/agent if known
   - status lane
   - next concrete action
   - blocker, if any
   - source link/path and last checked date
   - recurrence, if recurring
5. For recurrent tasks, record cadence and the scheduler/job ID if implemented via OpenClaw cron.
6. Before publishing a summary, check visible sessions/subagents, cron jobs, active project records, and relevant repo state for the requested scope.
7. When a summary omits known active projects, say the scope limitation explicitly and fix the board/source query.

## Daily reflection routine

Once per day, review the day’s project work and ask:

- Did repeated friction suggest a new skill, helper script, or tool?
- Did an existing skill need an update?
- Are there recurring tasks that should become scheduler jobs?
- Are any boards stale, duplicated, or missing blockers?

Only propose or queue tool/skill additions by default. Do not install external software, apply skill proposals, start paid compute, or change access/security settings without explicit approval.

## Validation

- Board update has at least one source path/job/session pointer per non-trivial card.
- Recurring tasks have cadence and owner/agent recorded.
- Summary states scope: all machines, local Pop!_OS, MacBook, one project, etc.
- No credentials, tokens, or private environment values are written to board files.
