#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/openclaw/research-agent
export OMEGACLAW_WATCHDOG_OUTER_SUPERVISOR="$ROOT/projects/omegaclaw/protocosmo2/tools/protocosmo2_telegram_supervisor.sh"
export OMEGACLAW_WATCHDOG_OUTER_PID_FILE=/home/openclaw/.openclaw/protocosmo2-supervisor.pid
export OMEGACLAW_WATCHDOG_OUTER_STATE_DIR=/home/openclaw/.openclaw/protocosmo2-canary-state
export OMEGACLAW_WATCHDOG_OUTER_IDENTITY=ProtoCosmo2
export OMEGACLAW_WATCHDOG_PID_FILE=/home/openclaw/.openclaw/protocosmo2-legacy-unused.pid
export OMEGACLAW_WATCHDOG_LEASE_FILE=/home/openclaw/.openclaw/protocosmo2-watchdog.maintenance
export OMEGACLAW_WATCHDOG_CUTOVER_LOCK="$ROOT/projects/omegaclaw/local/run-state/protocosmo2-cutover.lock"

exec "$ROOT/bin/omegaclaw-watchdog.sh" "$@"
