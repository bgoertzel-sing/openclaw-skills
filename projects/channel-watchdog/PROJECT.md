# Channel Watchdog

## Purpose

Monitor Telegram channels where OpenClaw-based bots (ZeroBot, ProtoCosmoBot, ProtoMegaBot) operate. Detect interaction bugs, dropped continuations, stale status contradictions, routing errors, and other perversities. Post concise alerts so the responsible bot or Ben can fix them.

## Status

- Created: 2026-07-07
- Owner: Benjamin Goertzel
- Active: yes
- 2026-07-21: RunPod alarm sensing hardened. The deterministic read-only sensor
  treats `uptimeSeconds` as advisory, fuses SSH/GPU/process evidence, requires
  three unreachable observations spanning at least 15 minutes, calculates
  elapsed cost from `createdAt`, and exposes no mutation operation. Eight
  regressions plus a two-live-pod validation pass. `HEARTBEAT.md` now forbids
  all resource start/stop/delete actions from heartbeat.

## Detection patterns

1. **Dropped continuation**: bot says "doing it now" / "compiling now" / "I'll report back" / "working on it" and no result appears within 15 minutes.
2. **Stale status contradiction**: project/Kanban files say blocked, but branches/subagents/commits exist showing active work.
3. **Routing bugs**: reply appears in wrong channel or thread (e.g., ProtoBots-BotBotChats content in main updates channel).
4. **Completion not surfaced**: subagent finishes but parent does not summarize within 10 minutes.
5. **Attachment promise not fulfilled**: bot says PDF/file/media ready but no MEDIA: attachment follows within 5 minutes.
6. **Looping or stock acknowledgements**: repeated "working on it carefully" / "I'll get back to you" without substantive progress across 2+ messages.
7. **Bot-bot chatter runaway**: extended bot-bot discussion in main updates channel that should move to BotBotChats (>3 bot-bot exchanges).
8. **Remote-compute alarm integrity**: fuse provider state with SSH/GPU/process
   evidence; never infer readiness from RunPod's advisory uptime field, and
   never perform destructive provider actions from heartbeat.

## Alert routing

- Alerts go to the **scheduled-updates channel** (`telegram:-1003983157420`) until Ben creates a dedicated watchdog channel.
- Alerts are prefixed with `🔍 Watchdog:` for easy filtering.
- Conservative: only high-confidence detections. No automatic intervention except posting the alert.
- Paid-resource checks are strictly observational. A heartbeat may never start,
  stop, or delete a pod.

## Cron job

- Schedule: every 15 minutes
- Session target: isolated agentTurn
- Job ID: TBD (created at setup)
