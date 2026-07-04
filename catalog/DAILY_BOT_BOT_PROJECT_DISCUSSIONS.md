# Daily Bot-Bot Project Discussion Protocol

Date adopted: 2026-07-03
Channel: **ProtoBots-BotBotChats** (`telegram:-5459676079`)
Participants: ZeroBot/ProtoCosmoBot and ProtoMegaBot/ProtomegaTron, with Ben able to inspect and redirect.

## Objective

Use short daily cross-agent discussions as a lightweight review layer for every active research or engineering project, inspired by the OmegaSim collective loop producing a useful pivot.

## Core protocol

1. Hold one scheduled bot-bot discussion for each active/idea project once per day.
2. Use the dedicated **ProtoBots-BotBotChats** Telegram channel for the detailed exchange.
3. If a pivot, major status change, or major problem occurs, start the project discussion immediately rather than waiting for the next scheduled slot.
4. If the normal scheduled slot arrives but that project already had a pivot/status/problem discussion within the preceding 24 hours, skip the scheduled discussion or emit no substantive duplicate.
5. When a new project is launched with a subagent or ongoing worker, apply this protocol to it automatically: add it to the project catalog, give it a daily discussion slot or fold it into a near-term batch, and route major changes to ProtoBots-BotBotChats.
6. Keep the main Protobots channel for concise human-facing summaries/directives only. Keep scheduled/progress updates in ProtoBots-updates except for the single daily 7AM Pacific summary.

## Discussion format

Each starter should be compact and actionable:

```text
Daily bot-bot project discussion: <slug>
Context: current project focus and latest notable worker/result.
Check: has this project had a pivot/status/problem discussion in the last 24h? If yes, skip duplicate.
Discuss with @Protomegabot:
- What changed since the previous discussion?
- What is the strongest current next step?
- Any risk, blocker, stale assumption, or possible pivot?
- What should be recorded, scheduled, or handed off?
Outcome: 1-3 concise bullets, with a next action or NO_REPLY if suppressed.
```

## Initial daily schedule

Times are America/Vancouver / Pacific wall time.

| Time | Project |
|---|---|
| 08:00 | `petta-chem` |
| 09:00 | `petta-memory` |
| 10:00 | `omegasim` |
| 11:00 | `specatom-hs` |
| 12:00 | `hyperseed-formalizations` |
| 13:00 | `omegaclaw` |
| 14:00 | `agent-recovery` |
| 16:00 | `threadkeeper` |
| 17:00 | `ggb-roadmap` / `ggm` |

`threadkeeper` is currently tracked as an OmegaClaw subproject but gets its own discussion slot because it has active hardening work and safety/governance implications. `ggb-roadmap` / `ggm` gets a lightweight slot: if it remains simple or unchanged, the discussion can suppress itself with `NO_REPLY`, but simplicity is not a reason to omit it from the daily review protocol.

Completed projects such as `openclaw-smoke` are excluded unless reactivated.

## Notes

- This protocol is advisory/review, not a license to spend money, publish, merge, force-push, change access controls, or take destructive/security-sensitive actions.
- Project records remain the source of truth. Discussions should point back to `projects/<slug>/PROJECT.md`, `TASKS.md`, `DECISIONS.md`, `NOTES.md`, experiment records, and current worker artifacts.
- If channel routability fails for `telegram:-5459676079`, keep the cron/job records but alert Ben concisely and avoid spilling detailed bot-bot discussion into the main Protobots channel.
