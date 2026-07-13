# 06 — Schedules, health, backup, and cost control

`install-schedules.sh` creates named jobs only if absent. It does not copy machine-specific job IDs. Inspect the script and `openclaw cron add --help` before execution.

## Default local-time schedule

| Time | Workflow |
|---|---|
| 00:20 daily | Kanban refresh |
| 00:45 daily | Scheduler reconciliation/report; no mutation |
| 03:30 daily | Sanitized recovery backup |
| 06:30 daily | Active-project/discussion-job discovery proposal |
| 07:00 daily | One concise human summary |
| 08:00–17:00 | Staggered active-project bot reviews |
| 08:30 daily | Ecosystem health report |
| 10:00 daily | Independent health-report alarm |
| Every 10 min | OmegaClaw bounded watchdog |
| 23:30 daily | Maintenance/skill-improvement reflection |
| Wednesday 14:00 | Rotating frontier-model expert review |
| Monthly/manual | Restore smoke test and memory/index audit |

Adjust to the recipient's timezone and model budget. Keep routine jobs on an economical model. A frontier model is used only for the selected weekly review unless the owner explicitly enables more.

## Health evidence

A useful health report checks:

- OpenClaw status, config validation, channel probe, scheduler failures;
- one Omega worker, zero MTProto bridges, fresh Bot API polling, successful send outcomes;
- correct per-chat routing canaries;
- Kanban/catalog freshness;
- backup manifest/archive readability and last restore test;
- stale uncommitted work, incomplete experiment records, disk pressure;
- unexpected model fallback, throttling, refusal/degradation, and spend telemetry.

Do not interpret process liveness as end-to-end health.

## Backup

`sanitized-recovery-backup.sh` includes policies/context, catalog/templates, skills/plugins/helpers, Markdown memory, and project notebook records. It excludes repositories, databases, caches, models, logs, artifacts, raw sessions/chats, and credentials. It performs a conservative secret-like scan and creates a SHA-256 manifest.

This is a recovery **skeleton**, not a complete data backup. If preserving private repos/artifacts/databases is required, define separate encrypted backups with explicit retention/access policy. Test restore monthly into a disposable location.

## Cost control

- autonomous paid remote-compute budget: USD 0;
- no automatic provider-key activation or frontier escalation;
- configure current pricing/budgets before enabling the optional intent router;
- log model route/usage decisions without prompt content or secrets;
- set scheduler timeouts and output caps;
- review provider invoices independently of local estimates.
