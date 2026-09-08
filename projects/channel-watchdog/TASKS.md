# Tasks

## Now

- [x] Suppress public `attachment promise not fulfilled` alerts. Deliverable:
  keep this heuristic out of watchdog channel output while preserving other
  alert classes. Acceptance: a provider-free regression produces `NO_REPLY`
  for an unfulfilled attachment promise and still emits a dropped-continuation
  alert. Next command: run the focused watchdog tests. Evidence:
  `tests/test_channel_watchdog.py`.
  Completed 2026-08-07: 2/2 focused tests pass and a live local invocation
  returned `NO_REPLY` despite the previously detected canary findings.

- [x] Create project notebook (2026-07-07).
- [x] Repair RunPod heartbeat alarm sensing after false zero-uptime alarms and
  destructive cleanup. Deliverable: deterministic read-only evidence fusion,
  repeated-unreachability threshold, absolute no-destructive-actions heartbeat
  policy, regression controls, and live-pod validation. Acceptance: healthy
  zero-uptime/SSH-active, reachable-idle, CPU-preprocessing, stopped, transient
  unreachable, and persistently unreachable fixtures pass; live active pods
  classify `ready_active`; heartbeat policy contains no zero-uptime deletion
  path. Next command: run focused tests and the sensor against current pods.
  Evidence: `bin/runpod-heartbeat-sensor.py`,
  `tests/test_runpod_heartbeat_sensor.py`, and `HEARTBEAT.md`.
  Completed 2026-07-21: eight regression tests pass; live validation classified
  both provider-uptime-zero pods as `ready_active` from SSH/GPU/process evidence.
  Heartbeat is now absolutely prohibited from provider mutations.
- [ ] Set up recurring cron job for 15-minute channel monitoring.
- [ ] First run: verify detection and alert posting works end-to-end.

## Next

- [ ] Ben creates a dedicated watchdog Telegram channel and adds the bot; update alert routing.
- [ ] Add stale-status-contradiction detection (read project/Kanban files vs actual repo/branch state).
- [ ] Add completion-not-surfaced detection (check subagent list vs parent session recent messages).
- [ ] Tune detection thresholds after first week of alerts.

## Someday

- [ ] Automatic task creation for detected issues.
- [ ] Cross-channel correlation (e.g., message routed to wrong channel detection).
- [ ] Weekly summary of detected issues and resolution status.
