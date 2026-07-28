# Notes

## 2026-07-21 — RunPod heartbeat sensor repair

**Observed failure:** RunPod CLI returned `uptimeSeconds: 0` for healthy pods
that were SSH-reachable and had active GPU/training processes. The prior
natural-language heartbeat rule allowed “zero uptime, no SSH for >15 min” to
justify deletion and led to false alarms plus destructive cleanup.

**Decision:** Provider uptime is advisory only. Readiness comes from successful
SSH. Activity comes from a GPU compute process, GPU utilization >=5%, or a
high-CPU training process. Unreachability is provisional until three
observations span at least 15 minutes. Heartbeat can never start, stop, or
delete a paid resource, regardless of approval state.

**Implementation:** `bin/runpod-heartbeat-sensor.py` is a deterministic,
read-only JSON sensor with persisted unreachability history.
`tests/test_runpod_heartbeat_sensor.py` covers healthy zero-uptime, idle,
CPU-bound preprocessing, stopped, transient/persistent unreachable, state
reset, probe parsing, and RunPod timestamp/cost parsing.

**Reproduced live:** At 2026-07-22 05:36 UTC, both active pods reported provider
uptime zero but classified `ready_active`: CAROM `wsllxvsshf7jf1` was
SSH-reachable with 33% GPU, one compute process, and one high-CPU trainer;
RelaLeap `0i26hl3ls399x4` was SSH-reachable with 31% GPU and the same process
evidence. Validation JSON:
`scratch/runpod-heartbeat-live-validation.json`.

**Limit:** Process/activity evidence establishes liveness, not scientific
progress. A future enhancement may compare checkpoint/log mtimes without
weakening the no-destructive-actions invariant.
