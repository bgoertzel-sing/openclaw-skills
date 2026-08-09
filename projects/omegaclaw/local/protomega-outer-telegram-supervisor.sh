#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/openclaw/research-agent/projects/omegaclaw
RUNNER="${OMEGACLAW_OUTER_RUNNER:-$ROOT/protocosmo2/tools/phase6_private_canary_runner.py}"
CORE="${OMEGACLAW_OUTER_CORE:-$ROOT/repos/PeTTa/repos/OmegaClaw-Core}"
TRANSPORT_CORE="${OMEGACLAW_OUTER_TRANSPORT_CORE:-$ROOT/worktrees/protocosmo2-phase6-live}"
PETTA="${OMEGACLAW_OUTER_PETTA:-$ROOT/repos/PeTTa}"
DRIVER="${OMEGACLAW_OUTER_DRIVER:-$ROOT/protocosmo2/tools/phase5_omegaclaw_case.py}"
ENV_FILE="${OMEGACLAW_OUTER_ENV_FILE:-/home/openclaw/.openclaw/omegaclaw-telegram.env}"
CONFIG="${OMEGACLAW_OUTER_CONFIG:-/home/openclaw/.openclaw/protomega-outer.json}"
STATE_DIR="${OMEGACLAW_OUTER_STATE_DIR:-/home/openclaw/.openclaw/protomega-outer-state}"
WORKER_STATE_DIR="${OMEGACLAW_OUTER_WORKER_STATE_DIR:-$ROOT/local/protomega-worker-state}"
PID_FILE="${OMEGACLAW_OUTER_PID_FILE:-$ROOT/local/run-state/protomega-outer-telegram.pid}"
PID_IDENTITY_FILE="${PID_FILE}.identity"
START_LOCK="${OMEGACLAW_OUTER_START_LOCK:-${PID_FILE}.start.lock}"
CUTOVER_LOCK="${OMEGACLAW_CUTOVER_LOCK:-$ROOT/local/run-state/protomega-cutover.lock}"
DEFERRED_DISABLE_MARKER="${OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER:-$ROOT/local/run-state/protomega-deferred-disabled}"
IDENTITY="${OMEGACLAW_OUTER_IDENTITY:-ProtomegaTron}"
BOT_ID="${OMEGACLAW_OUTER_BOT_ID:-8562797306}"
BOT_USERNAME="${OMEGACLAW_OUTER_BOT_USERNAME:-@Protomegabot}"
SESSION_PREFIX="${OMEGACLAW_OUTER_SESSION_PREFIX:-protomegatron-live}"
AGENT_ID="${OMEGACLAW_OUTER_AGENT_ID:-protomegabot-opus}"
MODEL="${OMEGACLAW_OUTER_MODEL:-anthropic/claude-opus-4-6}"
PROVIDER_TIMEOUT="${OMEGACLAW_OUTER_PROVIDER_TIMEOUT:-300}"
POLL_TIMEOUT="${OMEGACLAW_OUTER_POLL_TIMEOUT:-15}"

validate_deferred_disable_marker() {
  MARKER_PATH="$DEFERRED_DISABLE_MARKER" python3 - <<'PY'
import os, stat
path = os.environ["MARKER_PATH"]
flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
fd = os.open(path, flags)
try:
    info = os.fstat(fd)
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid():
        raise SystemExit("unsafe deferred-disable marker identity")
    if stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1:
        raise SystemExit("unsafe deferred-disable marker metadata")
finally:
    os.close(fd)
PY
}

create_deferred_disable_marker() {
  mkdir -p "$(dirname "$DEFERRED_DISABLE_MARKER")"
  MARKER_PATH="$DEFERRED_DISABLE_MARKER" python3 - <<'PY'
import errno, os, stat
path = os.environ["MARKER_PATH"]
flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
try:
    fd = os.open(path, flags, 0o600)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
try:
    info = os.fstat(fd)
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid():
        raise SystemExit("unsafe deferred-disable marker identity")
    if stat.S_IMODE(info.st_mode) != 0o600 or info.st_nlink != 1:
        raise SystemExit("unsafe deferred-disable marker metadata")
    os.fsync(fd)
finally:
    os.close(fd)
PY
}

process_running() {
  local pid="$1" state
  kill -0 "$pid" 2>/dev/null || return 1
  state=$(awk '{print $3}' "/proc/$pid/stat" 2>/dev/null) || return 1
  [[ "$state" != Z ]]
}
LOG="${OMEGACLAW_OUTER_LOG:-$ROOT/artifacts/telegram-private-supervisor/protomega-outer-telegram.log}"

alive() {
  local pid recorded_pid recorded_start recorded_hash current_start current_hash
  [[ -f "$PID_FILE" && ! -L "$PID_FILE" && -f "$PID_IDENTITY_FILE" && ! -L "$PID_IDENTITY_FILE" ]] || return 1
  IFS= read -r pid <"$PID_FILE" || return 1
  read -r recorded_pid recorded_start recorded_hash <"$PID_IDENTITY_FILE" || return 1
  [[ "$pid" =~ ^[1-9][0-9]*$ && "$recorded_pid" == "$pid" && "$recorded_start" =~ ^[0-9]+$ && "$recorded_hash" =~ ^[0-9a-f]{64}$ ]] || return 1
  process_running "$pid" || return 1
  current_start=$(awk '{print $22}' "/proc/$pid/stat" 2>/dev/null) || return 1
  [[ "$current_start" == "$recorded_start" ]] || return 1
  current_hash=$(sha256sum "/proc/$pid/cmdline" 2>/dev/null | awk '{print $1}') || return 1
  [[ "$current_hash" == "$recorded_hash" ]] || return 1
  EXPECTED_SCRIPT="$(realpath "$0")" TARGET_PID="$pid" python3 - <<'PY'
import os
from pathlib import Path
args = [a.decode() for a in Path(f'/proc/{os.environ["TARGET_PID"]}/cmdline').read_bytes().split(b'\0') if a]
expected = os.environ['EXPECTED_SCRIPT']
for index, arg in enumerate(args[:-1]):
    if os.path.realpath(arg) == expected and args[index + 1] == 'run':
        raise SystemExit(0)
raise SystemExit(1)
PY
}

child_count() {
  local owner_pid="$1"
  ps -eo ppid=,args= | awk -v owner="$owner_pid" '
    $1 == owner && /phase6_private_canary_runner\.py/ {count++}
    END {print count + 0}
  '
}

case "${1:-status}" in
  run)
    [[ ! -L "$PID_FILE" ]] || { echo "UNSAFE_PID_FILE" >&2; exit 2; }
    umask 077
    pid_tmp=$(mktemp "$(dirname "$PID_FILE")/.protomega-outer.pid.XXXXXX")
    identity_tmp=$(mktemp "$(dirname "$PID_FILE")/.protomega-outer.identity.XXXXXX")
    trap 'rm -f "$pid_tmp" "$identity_tmp"' EXIT
    printf '%s\n' "$$" >"$pid_tmp"
    printf '%s %s %s\n' "$$" "$(awk '{print $22}' "/proc/$$/stat")" "$(sha256sum "/proc/$$/cmdline" | awk '{print $1}')" >"$identity_tmp"
    mv -f "$identity_tmp" "$PID_IDENTITY_FILE"
    mv -f "$pid_tmp" "$PID_FILE"
    trap - EXIT
    child_pid=""
    terminate() {
      if [[ -n "$child_pid" ]]; then
        kill -TERM "$child_pid" 2>/dev/null || true
        wait "$child_pid" 2>/dev/null || true
      fi
      if [[ "$(cat "$PID_FILE" 2>/dev/null || true)" == "$$" ]]; then rm -f "$PID_FILE" "$PID_IDENTITY_FILE"; fi
      exit 0
    }
    trap terminate TERM INT
    while true; do
      deferred_args=()
      if [[ -e "$DEFERRED_DISABLE_MARKER" || -L "$DEFERRED_DISABLE_MARKER" ]]; then
        validate_deferred_disable_marker
        deferred_args+=(--disable-deferred-jobs)
      fi
      OMEGACLAW_EXPECTED_PARENT_PID="$$" python3 "$RUNNER" \
        --env "$ENV_FILE" --config "$CONFIG" --state-dir "$STATE_DIR" \
        --worker-state-dir "$WORKER_STATE_DIR" --core "$CORE" \
        --transport-core "$TRANSPORT_CORE" --petta "$PETTA" --driver "$DRIVER" \
        --identity "$IDENTITY" --bot-id "$BOT_ID" --bot-username "$BOT_USERNAME" \
        --session-prefix "$SESSION_PREFIX" --agent-id "$AGENT_ID" --model "$MODEL" \
        --provider-timeout "$PROVIDER_TIMEOUT" --poll-timeout "$POLL_TIMEOUT" \
        "${deferred_args[@]}" </dev/null >>"$LOG" 2>&1 &
      child_pid=$!
      wait "$child_pid" || true
      child_pid=""
      sleep 5
    done
    ;;
  start)
    if [[ "${OMEGACLAW_CUTOVER_LOCK_HELD:-0}" != 1 ]]; then
      [[ ! -L "$CUTOVER_LOCK" ]] || { echo "UNSAFE_CUTOVER_LOCK" >&2; exit 2; }
      mkdir -p "$(dirname "$CUTOVER_LOCK")"
      exec 9>"$CUTOVER_LOCK"
      flock -n 9 || { echo "cutover in progress" >&2; exit 1; }
    fi
    [[ ! -L "$START_LOCK" ]] || { echo "UNSAFE_START_LOCK" >&2; exit 2; }
    mkdir -p "$(dirname "$START_LOCK")"
    exec 8>"$START_LOCK"
    flock -n 8 || { echo "start already in progress" >&2; exit 1; }
    if alive; then echo "active pid $(cat "$PID_FILE")"; exit 0; fi
    [[ -f "$ENV_FILE" && -f "$CONFIG" ]]
    mkdir -p "$(dirname "$PID_FILE")" "$(dirname "$LOG")"
    rm -f "$PID_FILE" "$PID_IDENTITY_FILE"
    # Never let the long-lived owner inherit the coordinator's topology lock.
    setsid -f "$0" run 8>&- 9>&- </dev/null >>"$LOG" 2>&1
    for _ in $(seq 1 20); do alive && break; sleep 0.25; done
    alive
    echo "started pid $(cat "$PID_FILE")"
    ;;
  stop)
    if [[ "${OMEGACLAW_CUTOVER_LOCK_HELD:-0}" != 1 ]]; then
      [[ ! -L "$CUTOVER_LOCK" ]] || { echo "UNSAFE_CUTOVER_LOCK" >&2; exit 2; }
      mkdir -p "$(dirname "$CUTOVER_LOCK")"
      exec 9>"$CUTOVER_LOCK"
      flock -n 9 || { echo "cutover in progress" >&2; exit 1; }
    fi
    if alive; then
      pid=$(cat "$PID_FILE")
      kill -TERM "-$pid" 2>/dev/null || kill -TERM "$pid"
      for _ in $(seq 1 40); do process_running "$pid" || break; sleep 0.25; done
      if process_running "$pid"; then
        kill -KILL "-$pid" 2>/dev/null || kill -KILL "$pid" 2>/dev/null || true
        for _ in $(seq 1 20); do process_running "$pid" || break; sleep 0.1; done
      fi
      if process_running "$pid"; then
        echo "stop failed after escalation: owner still active pid $pid" >&2
        exit 1
      fi
    fi
    rm -f "$PID_FILE" "$PID_IDENTITY_FILE"
    echo stopped
    ;;
  status)
    if alive; then
      pid=$(cat "$PID_FILE")
      children=$(child_count "$pid")
      echo "active pid $pid children=$children"
      [[ "$children" -eq 1 ]] || { echo "readiness=failed expected_children=1" >&2; exit 1; }
      echo "readiness=process-topology-ok (end-to-end Telegram delivery not proven)"
    else
      echo inactive
      exit 1
    fi
    ;;
  owner-alive)
    if alive; then echo "owner-active pid $(cat "$PID_FILE")"; else echo inactive; exit 1; fi
    ;;
  enable-sync-rollback)
    create_deferred_disable_marker
    validate_deferred_disable_marker
    echo "sync rollback enabled"
    ;;
  validate-sync-rollback)
    validate_deferred_disable_marker
    echo "sync rollback marker valid"
    ;;
  *) echo "usage: $0 {start|stop|status|run|enable-sync-rollback|validate-sync-rollback}" >&2; exit 2 ;;
esac
