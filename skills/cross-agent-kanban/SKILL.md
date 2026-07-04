---
name: "cross-agent-kanban"
description: "Maintain a compact cross-agent Kanban board for recurrent and one-off OpenClaw workstreams."
---

# Cross-Agent Kanban

Use this skill when asked for a global subagent/workstream summary, project-worker status, recurrent-task review, or when a new recurring/one-off lane should remain visible across future OpenClaw/OmegaClaw turns.

## Purpose

Maintain a lightweight Kanban-style source of truth for cross-agent work that may not appear in ordinary `sessions_list` output, especially isolated cron workers and recurrent project lanes.

## Default board

Use `catalog/KANBAN.md` unless the user specifies another board. Project-specific details remain in each project notebook; the board is only the compact cross-lane index.

## Procedure

1. Inspect current state before summarizing or editing:
   - read `catalog/KANBAN.md` if present;
   - list active cron jobs with `cron(action="list")`;
   - use `sessions_list(activeMinutes=1440, includeLastMessage=true)` for recent visible sessions/subagents;
   - for project-specific claims, read the relevant project files or recent memory entries.
2. When summarizing all subagents/workstreams, include both:
   - visible recent sessions/subagents;
   - recurrent cron/project workers listed on the board, even if no recent session is visible.
3. When Ben names a persistent lane, add or update one compact row with:
   - lane name;
   - status: `backlog`, `ready`, `running`, `blocked`, `review`, `done`, or `recurring`;
   - owner/cadence;
   - current focus;
   - source-of-truth path;
   - brief notes.
4. Do not let `catalog/KANBAN.md` become a duplicate project notebook:
   - keep rows short;
   - put detailed results, tests, decisions, and artifacts in the project record;
   - remove or archive stale one-off rows after they are resolved.
5. For daily or recurrent reflection, check whether the day’s work implies a reusable skill/tool/workflow. If yes, create or revise a Skill Workshop proposal with `skill_workshop`; do not manually install live skills unless explicitly approved.
6. Never store secrets, credentials, private tokens, or sensitive operational values in the board.

## Summary checklist

Before claiming “all subagents” have been covered, verify:

- `catalog/KANBAN.md` checked;
- active cron jobs checked;
- recent sessions checked;
- active project records or memory checked for any lane mentioned;
- blockers and Ben-needed decisions separated from ordinary next steps.
