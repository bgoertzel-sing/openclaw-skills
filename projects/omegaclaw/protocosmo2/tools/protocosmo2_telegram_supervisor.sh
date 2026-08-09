#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/openclaw/research-agent/projects/omegaclaw
export OMEGACLAW_OUTER_RUNNER="${OMEGACLAW_OUTER_RUNNER:-$ROOT/protocosmo2/tools/phase6_private_canary_runner.py}"
export OMEGACLAW_OUTER_CORE="${OMEGACLAW_OUTER_CORE:-$ROOT/worktrees/protocosmo2-phase6-live}"
export OMEGACLAW_OUTER_TRANSPORT_CORE="${OMEGACLAW_OUTER_TRANSPORT_CORE:-$ROOT/worktrees/protocosmo2-phase6-live}"
export OMEGACLAW_OUTER_PETTA="${OMEGACLAW_OUTER_PETTA:-$ROOT/protocosmo2/phase2-checked-baseline/repos/PeTTa}"
export OMEGACLAW_OUTER_DRIVER="${OMEGACLAW_OUTER_DRIVER:-$ROOT/protocosmo2/tools/phase5_omegaclaw_case.py}"
export OMEGACLAW_OUTER_ENV_FILE="${OMEGACLAW_OUTER_ENV_FILE:-/home/openclaw/.openclaw/protocosmo2.env}"
export OMEGACLAW_OUTER_CONFIG="${OMEGACLAW_OUTER_CONFIG:-/home/openclaw/.openclaw/protocosmo2-canary.json}"
export OMEGACLAW_OUTER_STATE_DIR="${OMEGACLAW_OUTER_STATE_DIR:-/home/openclaw/.openclaw/protocosmo2-canary-state}"
export OMEGACLAW_OUTER_WORKER_STATE_DIR="${OMEGACLAW_OUTER_WORKER_STATE_DIR:-/home/openclaw/.openclaw/protocosmo2-worker-state}"
export OMEGACLAW_OUTER_PID_FILE="${OMEGACLAW_OUTER_PID_FILE:-/home/openclaw/.openclaw/protocosmo2-supervisor.pid}"
export OMEGACLAW_OUTER_START_LOCK="${OMEGACLAW_OUTER_START_LOCK:-/home/openclaw/.openclaw/protocosmo2-supervisor.pid.start.lock}"
export OMEGACLAW_CUTOVER_LOCK="${OMEGACLAW_CUTOVER_LOCK:-$ROOT/local/run-state/protocosmo2-cutover.lock}"
export OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER="${OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER:-/home/openclaw/.openclaw/protocosmo2-deferred-disabled}"
export OMEGACLAW_OUTER_LOG="${OMEGACLAW_OUTER_LOG:-/home/openclaw/.openclaw/protocosmo2-supervisor.log}"
export OMEGACLAW_OUTER_IDENTITY=ProtoCosmo2
export OMEGACLAW_OUTER_BOT_ID=8716054285
export OMEGACLAW_OUTER_BOT_USERNAME=@protocosmo2bot
export OMEGACLAW_OUTER_SESSION_PREFIX=protocosmo2-canary
export OMEGACLAW_OUTER_AGENT_ID=main
export OMEGACLAW_OUTER_MODEL=openai/gpt-5.6-sol
export OMEGACLAW_OUTER_PROVIDER_TIMEOUT=240
export OMEGACLAW_OUTER_POLL_TIMEOUT=15

exec "$ROOT/local/protomega-outer-telegram-supervisor.sh" "$@"
