# VM2 ProtoCosmo Retry Checklist

- Updated: 2026-08-20 18:22 PDT / 2026-08-21 01:22 UTC
- Scope: concise checklist for the next VM2 ProtoCosmo cutover attempt
- Constraint: VM2 must remain inert until Ben authorizes an attended cutover

## Current accepted hashes (updated 2026-08-20 10:59 PDT)

| Component | SHA-256 (prefix) | Status |
|-----------|-----------------|--------|
| Boundary operator | `2cf20985...f352` | changed from `7d8879d2...119` at 10:59 PDT; fixes: (1) `rsync_retry()` 6-attempt bounded retry for SSH transport drops (addresses 06:47/16:25/17:17 UTC arm failures), (2) `--exclude='*.jsonl.lock'` for sessions rsync (transient locks caused rsync non-zero exit), (3) prefix-match for gateway comm in receipt gate (kernel truncates `openclaw-gatewa` to 15 chars, caused #5 arm rollback of healthy container); regressions pass 2026-08-20 10:59 PDT |
| Boundary rollback | `cf9acd39...c4e` | unchanged |
| Worker (agent_worker.py) | `e8b7d7db...cc7b` | unchanged |
| Supervisor (hive_supervisor.py) | `c17993cd...a382` | unchanged |
| Entrypoint | `2078d88e...3469` | unchanged |
| Live Compose | `c80c79eb...b308` | unchanged; pids_limit=512 |
| Inert Compose | `eb70ccf8...d4b7` | unchanged; network_mode=none |
| Boundary contract test | `56b94d5d...2010` | unchanged |
| Worker stability test | `5bf76d07...f8f6` | unchanged |
| Healthcheck | `d775717c...fe79` | unchanged |

## Regression gate (passed 2026-08-20 18:47 UTC — re-run due to operator hash change at 10:59 PDT)

1. Bash syntax: 3/3 scripts pass (operator, rollback, vm2-admin)
2. ShellCheck: pass (exit 0, no warnings at --severity=warning)
3. Python contract test: `operator_boundary_contract=pass stale_state_guards=pass post_dropin_rollback_trap=pass activation_after_laptop_stop=pass network=disabled`
4. Rollback regression: `rollback_disposable_test=pass vm2_cleanup_success=pass vm2_unreachable_laptop_restore=pass evidence_before_removal=pass redaction=pass production_mutations=0`
5. Worker stability: `agent_worker_stability=pass final_interval_recheck=pass polls=46 network=disabled`
6. Config audit: container-scoped paths confirmed — secrets at `/hive/protocosmo/secrets/secrets.json`, state at `/hive/protocosmo/state/`, config at `/opt/proto-hive-runtime/protocosmo/config/openclaw.json`

## VM2 container audit (2026-08-20 18:22 PDT — fresh re-verification)

VM2 is **fully inert**: 0 running containers, 0 stopped containers, 0
activation markers, 0 compose projects. The 8 stopped containers observed
at 10:55 PDT have been pruned (likely by Ben). No `docker container prune`
is needed before cutover.

Docker images present: `proto-hive:vm2-one-hive-final` (2476333839b3)
and `proto-hive:vm2-one-hive` (c21d481bd2f6). No new
`protocosmo-startup-failure` logs since 10:39 PDT.

Runtime tree verified: all required directories present (state,
sessions, media inbound/outbound, agent, workspace). Secrets file
present. Config file present. Docker images: `proto-hive:vm2-one-hive-final`
and `proto-hive:vm2-one-hive`. No new `protocosmo-startup-failure` logs.

## Laptop gateway state (2026-08-20 10:40 PDT)

| Field | Value |
|------|-------|
| PID | 2456108 (restarted 11:36 PDT — Protomega crash-loop recovery, not VM2-related) |
| Restart | always |
| KillMode | control-group |
| NoNewPrivileges | yes |
| Boundary drop-in (`90-vm2-protocosmo-boundary.conf`) | absent (correct) |
| Rollback timer | inactive |
| Telegram connections | 3 ESTAB to 149.154.166.110:443 (≥2 threshold met) |

Note: Gateway PID 2456108 since 11:36 PDT restart (Protomega crash-loop
recovery, not VM2-related; journal confirms no arm/boundary evidence).
No `protocosmo-startup-failure` logs since the 10:27 PDT fix. Previous
four root-owned failure logs (06:47Z, 16:25Z, 17:11Z, 17:17Z) correlated
with four failed `--arm` attempts — first three at line 183 (missing
`|| true` on `tg_conns_after`), fourth at line 230 (same bug on
`tg_conns_after_vm2`). Both now fixed at 10:27 PDT. VM2 inert at 10:55
PDT: 0 running containers, 0 markers, 0 compose projects. 8 stopped
containers (remnants) should be pruned before cutover.
All file hashes verified unchanged at 18:50 UTC: operator `2cf20985...f352`,
rollback `cf9acd39...c4e`, worker `e8b7d7db...cc7b`, supervisor
`c17993cd...a382`, entrypoint `2078d88e...3469`, live Compose
`c80c79eb...b308`, inert Compose `eb70ccf8...d4b7`, healthcheck
`d775717c...fe79`.

## State layout (source → destination)

| Laptop source | VM2 host path | Container path |
|---------------|---------------|----------------|
| `/home/openclaw/.openclaw/state/` | `/opt/proto-hive-runtime/protocosmo/state/state/` | `/hive/protocosmo/state/state/` |
| `/home/openclaw/.openclaw/agents/main/sessions/` | `/opt/proto-hive-runtime/protocosmo/state/agents/main/sessions/` | `/hive/protocosmo/state/agents/main/sessions/` |
| `/home/openclaw/.openclaw/media/inbound/` | `/opt/proto-hive-runtime/protocosmo/state/media/inbound/` | `/hive/protocosmo/state/media/inbound/` |
| `/home/openclaw/.openclaw/media/outbound/` | `/opt/proto-hive-runtime/protocosmo/state/media/outbound/` | `/hive/protocosmo/state/media/outbound/` |

- Config: `/opt/proto-hive-runtime/protocosmo/config/openclaw.json`
- Secrets: `/opt/proto-hive-runtime/protocosmo/secrets/secrets.json`
- Workspace: `/hive/protocosmo/workspace`
- Agent dirs: `/hive/protocosmo/state/agents/{identity}/agent`

## Readiness soak

- Status: VM2 inertness re-verified 2026-08-20 10:55 PDT via read-only SSH.
  Full readiness soak (network-disabled cloned-state startup) remains retired
  per Ben's Telegram 19973. No new soak has been run for the current operator
  hash `2cf20985...f352`; the previous proof path is closed. A fresh soak
  requires Ben to authorize a new test design or re-open the retired path.
- Local regression gate (Python contract, worker stability, bash syntax,
  ShellCheck, rollback regression): all pass for current hashes at
  2026-08-20 18:47 UTC — operator hash changed at 10:59 PDT, regressions re-run.
- Five root-owned `protocosmo-startup-failure` logs appeared today
  (06:47Z, 16:25Z, 17:11Z, 17:17Z, 17:39Z UTC) — unreadable from cron (root:root)
- Root cause of first three failures (06:47Z, 16:25Z, 17:11Z): missing `|| true`
  guard on `tg_conns_after` pipeline (line 183) — `grep` exits 1 when zero
  connections match after gateway stop, `pipefail`+`set -e` aborts before rsync
- Root cause of fourth failure (17:17Z): same missing `|| true` guard on
  `tg_conns_after_vm2` pipeline (line 230) — the 10:14 fix applied the guard to
  line 183 but not line 230. Gateway restarted at 10:17:30 PDT (13s after
  failure log), consistent with rollback timer firing after the script aborted
- Fix applied 10:27 PDT: added `|| true` to line 230, matching the existing
  fix at line 183. Operator hash changed to `7d8879d2...119`
- Second fix applied 10:59 PDT: operator hash changed to `2cf20985...f352`.
  Added `rsync_retry()` with 6-attempt bounded retry for SSH transport drops
  (addresses 06:47/16:25/17:17 UTC failures where `rsync rc=255` aborted the
  arm). Added `--exclude='*.jsonl.lock'` for sessions rsync (transient lock
  files vanished during rsync walk, causing non-zero exit). Changed receipt
  gate to prefix-match `openclaw` instead of exact match (kernel truncates
  comm field to 15 chars: `openclaw-gatewa`, which caused the #5 arm to roll
  back a healthy container). All regressions re-run and pass.
- Root-owned receipt `protocosmo-boundary-20260820T180502Z.receipt` (391 bytes,
  11:05 AM PDT) — unreadable from cron, likely Ben's `--check` run
- VM2 is inert (containers=0, activation_markers=0, gateway=inert)
- Ben's next action: (1) confirm VM2 inertness (stop/remove any test container),
  (2) run `sudo bash .../protocosmo-boundary-operator.sh --check` from an
  independent root terminal, (3) if it passes, decide whether to proceed to
  an attended `--arm` cutover
- Previous network-disabled startup proof retired per Ben's Telegram 19973
- Root cause of prior outage identified: PID exhaustion (128→512 fix applied and validated)

## Expected preflight receipt (--check)

```
preflight=pass main_pid=<PID> gateway_telegram_connections=<N> tmux_pid=<PID> \
boundary_dropin=absent rollback_timer=inactive \
unit_sha256=<hash> readiness_sha256=<hash> \
worker_sha256=e8b7d7db...cc7b \
operator_sha256=2cf20985...f352 \
rollback_sha256=cf9acd39...c4e \
config_sha256=<hash>
mode=check local_no_changes=pass vm2_inert=pass compose=pass
```

## Expected arm receipt (--arm, attended only)

```
boundary=armed old_main_pid=<PID> laptop_telegram_connections=0 tmux_owner=alive
rollback_timer=active unit_sha256=<hash> readiness_sha256=<hash> next=human_canary_then_commit
```

## Acceptance criteria

1. Fresh human-authored Telegram message correlated through ingress → agent loop → egress
2. Exactly one ProtoCosmo receiver on VM2
3. PID usage monitored (must stay well under 512)
4. No overlapping five-minute cron on the VM2 container
5. Rollback trap armed until canary accepted
6. Evidence captured before any container removal

## Hard prohibitions

- Never run `--arm` from cron
- Never create activation markers from cron
- Never stop the laptop gateway from cron
- Never invoke authenticated Telegram/provider actions from cron
- Never mutate production state from cron
- Keep VM2 inert until Ben directs an attended cutover
