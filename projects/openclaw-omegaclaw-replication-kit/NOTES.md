# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.
# 2026-08-10

- Ben requested a detailed guide for the administrator provisioning the remote
  host and a separate multi-step port document for ProtoCosmo/ProtoCosmo2 and
  the ProtoMega family.
- Added `docs/remote-server-provisioning-guide-2026-08-10.md`, covering host
  capacity, security/networking, required and optional software, per-agent
  isolation, secrets, OpenClaw/OmegaClaw requirements, supervision, backups,
  acceptance checks, and the administrator handback record.
- Added `docs/multi-agent-remote-port-runbook-2026-08-10.md`, covering frozen
  baselines, sanitized manifests, offline/shadow/live gates, idempotent memory
  import, one-token-at-a-time cutover, dual operation, rollback, and old-host
  retirement. ZeroBot is recommended as the final migration so it remains an
  independent recovery peer while OmegaClaw-family agents stabilize.
- Documentation checks: both files end in a newline, contain no tabs/trailing
  whitespace/NULs, conservative secret-value scan found no matches,
  potentially hazardous-command review found only the explicitly
  administrator-run package installation and a warning against `curl | sh`,
  and `git diff --check` passed.
