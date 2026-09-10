# Heartbeat Tasks

## Daily Kanban Refresh
- Run `directive-board project-plan.metta` to get current board state
- Check for stale tasks (no movement in >3 days) and blocked items
- Update task statuses if completions have occurred since last refresh
- Send compact summary to Ben only if there are actionable changes or stale items
- Last refresh: (track in memory/heartbeat-state.json)

## Periodic Checks (rotate through, 2-4x/day)
- Email: urgent unread messages
- Calendar: events in next 24-48h
- Weather: if Ben might go out
