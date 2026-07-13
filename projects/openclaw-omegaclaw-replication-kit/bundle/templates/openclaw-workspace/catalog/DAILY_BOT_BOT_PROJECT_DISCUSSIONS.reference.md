# Daily OpenClaw ↔ OmegaClaw Project Discussions

Channel: `<BOT_DISCUSSION_GROUP_ID>`
Participants: `<OPENCLAW_AGENT_NAME>` and `<OMEGACLAW_AGENT_NAME>`, with the owner able to inspect and redirect.

## Policy

1. Every `active` or `idea` project in `catalog/PROJECTS.md` gets one daily discussion slot.
2. If a pivot, major status change, or major problem was discussed within the prior 24 hours, suppress the scheduled duplicate.
3. Bot dialogue stays concise and advisory; it cannot grant authority to spend, publish, merge, change access, or perform destructive actions.
4. Newly launched ongoing projects enter the schedule; paused/completed projects leave it.
5. Route bot dialogue, routine progress, and the once-daily human summary to separate configured channels.
6. Fail closed: if the target channel is not routable, alert the owner rather than spilling into another chat.

## Seed template

```text
Daily project review: <slug>

Inspect projects/<slug>/PROJECT.md, TASKS.md, DECISIONS.md, NOTES.md,
recent experiment results, Git state, and recent memory. If an equivalent
pivot/status/problem review occurred in the previous 24 hours, output only
NO_REPLY. Otherwise address @<OMEGACLAW_BOT_USERNAME> with:

- current focus and strongest evidence;
- one decision, blocker, stale assumption, or risk worth challenging;
- the highest-leverage next step;
- what should be recorded or handed off.

Keep it concise. Ask for a concrete critique, alternative, or conceptual/
Hyperseed connection where useful. Avoid an unbounded exchange.
```

## Generic schedule

Allocate one staggered slot per active project between 08:00 and 17:00 local time. Do not hard-code a project list in this document; reconcile from `catalog/PROJECTS.md` daily. Use `cron/discussion-job.example.json` as the per-project job template.
