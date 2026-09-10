# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] Prevent boot-time Telegram network races from crashing the OpenClaw gateway.
  Deliverable: a systemd `ExecStartPre` endpoint-readiness gate.
  Acceptance test: installed drop-in is visible in `systemctl cat`,
  the readiness probe passes, the gateway is active, and
  `openclaw channels status --probe` reports Telegram connected.
  Next command:
  `sudo /home/openclaw/research-agent/bin/install-openclaw-telegram-network-gate`.
  Evidence path:
  `projects/openclaw-smoke/systemd/openclaw-agent.service.d/10-telegram-network-readiness.conf`.
- [x] Run local Python smoke test and record result.
- [x] Verify OpenClaw memory index status.
- [x] Write setup report.

## Next

- [x] Install approved Pop!_OS prerequisites after Benjamin authorized sudo apt.
- [x] Authenticate GitHub after `gh` is installed.
- [x] Install and smoke-test QMD semantic search.

## Waiting or blocked

- [ ] Coding-agent doctor warning - no available coding-agent binary in check path - ZeroBot - 2026-06-25
- [ ] Session-log and summarize helpers - missing setup or command - ZeroBot - 2026-06-25
- [ ] Refresh stale setup-era text in `PROJECT.md` and the tiny Python experiment `RUN.md` now that prerequisites, GitHub auth, and QMD are installed - ZeroBot heartbeat - 2026-06-25

## Someday or exploratory

- [ ] Configure Runpod or ASI:Cloud only after explicit approval and cost plan.

## Done recently

- 2026-07-27: Installed and verified the systemd Telegram endpoint-readiness
  gate. `ExecStartPre` completed three stable probes in six seconds; the
  gateway is active and both Telegram and Slack probes pass.
- 2026-06-25: Created project and completed local workspace smoke test.
- 2026-06-25: Installed prerequisites, authenticated GitHub, and installed QMD semantic search.

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.
