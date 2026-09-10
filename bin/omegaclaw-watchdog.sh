#!/usr/bin/env bash
# Watchdog for the accepted Protomega outer Telegram supervisor.
# Legacy is recognized only as an explicit rollback state and is never
# started automatically while outer mode is the production target.
# Returns 0 if running fine, 0 if restarted successfully, 1 if restart failed.
set -euo pipefail

SUPERVISOR="${OMEGACLAW_WATCHDOG_SUPERVISOR:-/home/openclaw/research-agent/projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh}"
OUTER_SUPERVISOR="${OMEGACLAW_WATCHDOG_OUTER_SUPERVISOR:-/home/openclaw/research-agent/projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh}"
PID_FILE="${OMEGACLAW_WATCHDOG_PID_FILE:-/home/openclaw/research-agent/projects/omegaclaw/local/run-state/omegaclaw-telegram-private.pid}"
OUTER_PID_FILE="${OMEGACLAW_WATCHDOG_OUTER_PID_FILE:-/home/openclaw/research-agent/projects/omegaclaw/local/run-state/protomega-outer-telegram.pid}"
OUTER_STATE_DIR="${OMEGACLAW_WATCHDOG_OUTER_STATE_DIR:-/home/openclaw/.openclaw/protomega-outer-state}"
LEASE_FILE="${OMEGACLAW_WATCHDOG_LEASE_FILE:-/home/openclaw/research-agent/projects/omegaclaw/local/run-state/omegaclaw-watchdog.maintenance}"
CUTOVER_LOCK="${OMEGACLAW_WATCHDOG_CUTOVER_LOCK:-/home/openclaw/research-agent/projects/omegaclaw/local/run-state/protomega-cutover.lock}"
MAX_LEASE_SECONDS=900
OUTER_IDENTITY="${OMEGACLAW_WATCHDOG_OUTER_IDENTITY:-ProtomegaTron}"

alive_pid_file() {
  local file="$1" pid
  [[ -f "$file" && ! -L "$file" ]] || return 1
  IFS= read -r pid <"$file" || return 1
  [[ "$pid" =~ ^[1-9][0-9]*$ ]] || return 1
  kill -0 "$pid" 2>/dev/null
}

outer_receiver_count() {
EXPECTED_STATE_DIR="$OUTER_STATE_DIR" EXPECTED_IDENTITY="$OUTER_IDENTITY" python3 - <<'PY'
import os
from pathlib import Path
count = 0
expected_state = os.path.realpath(os.environ['EXPECTED_STATE_DIR'])
expected_identity = os.environ['EXPECTED_IDENTITY']
for cmdline in Path('/proc').glob('[0-9]*/cmdline'):
    try:
        args = [part.decode(errors='replace') for part in cmdline.read_bytes().split(b'\0') if part]
    except (FileNotFoundError, PermissionError, ProcessLookupError):
        continue
    if not any(Path(arg).name == 'phase6_private_canary_runner.py' for arg in args):
        continue
    if any(args[i:i + 2] == ['--identity', expected_identity] for i in range(len(args) - 1)):
        for i in range(len(args) - 1):
            if args[i] == '--state-dir' and os.path.realpath(args[i + 1]) == expected_state:
                count += 1
                break
print(count)
PY
}

lease_until() {
  local line until now
  [[ -f "$LEASE_FILE" && ! -L "$LEASE_FILE" ]] || return 1
  [[ $(wc -c <"$LEASE_FILE") -le 64 ]] || return 1
  IFS= read -r line <"$LEASE_FILE" || return 1
  [[ "$line" =~ ^maintenance_until_epoch=([0-9]{10})$ ]] || return 1
  until="${BASH_REMATCH[1]}"
  now=$(date +%s)
  (( until > now && until <= now + MAX_LEASE_SECONDS )) || return 1
  printf '%s\n' "$until"
}

case "${1:-check}" in
  enter-maintenance)
    duration="${2:-300}"
    [[ "$duration" =~ ^[1-9][0-9]*$ ]] || { echo "INVALID_DURATION" >&2; exit 2; }
    (( duration <= MAX_LEASE_SECONDS )) || { echo "DURATION_EXCEEDS_MAX" >&2; exit 2; }
    mkdir -p "$(dirname "$LEASE_FILE")"
    [[ ! -L "$LEASE_FILE" ]] || { echo "UNSAFE_LEASE_FILE" >&2; exit 2; }
    umask 077
    tmp=$(mktemp "$(dirname "$LEASE_FILE")/.omegaclaw-watchdog.maintenance.XXXXXX")
    trap 'rm -f "$tmp"' EXIT
    printf 'maintenance_until_epoch=%s\n' "$(( $(date +%s) + duration ))" >"$tmp"
    mv -f "$tmp" "$LEASE_FILE"
    trap - EXIT
    echo "MAINTENANCE_ENTERED duration=$duration"
    exit 0
    ;;
  clear-maintenance)
    [[ ! -L "$LEASE_FILE" ]] || { echo "UNSAFE_LEASE_FILE" >&2; exit 2; }
    rm -f "$LEASE_FILE"
    echo "MAINTENANCE_CLEARED"
    exit 0
    ;;
  maintenance-status)
    if until=$(lease_until); then echo "MAINTENANCE_ACTIVE until=$until"; exit 0; fi
    echo "MAINTENANCE_INACTIVE"
    exit 1
    ;;
  check) ;;
  *) echo "usage: $0 {check|enter-maintenance [1-$MAX_LEASE_SECONDS]|clear-maintenance|maintenance-status}" >&2; exit 2 ;;
esac

mkdir -p "$(dirname "$CUTOVER_LOCK")"
[[ ! -L "$CUTOVER_LOCK" ]] || { echo "UNSAFE_CUTOVER_LOCK" >&2; exit 2; }
exec 9>"$CUTOVER_LOCK"
if ! flock -n 9; then
  echo "CUTOVER_IN_PROGRESS"
  exit 0
fi

if alive_pid_file "$OUTER_PID_FILE" && "$OUTER_SUPERVISOR" owner-alive >/dev/null 2>&1; then
  echo "OUTER_OWNER_RUNNING pid=$(cat "$OUTER_PID_FILE")"
  exit 0
fi

# A live process referenced by an invalid outer identity is ambiguous. Never
# erase its ownership files or launch a possible competing receiver.
if alive_pid_file "$OUTER_PID_FILE"; then
  echo "OUTER_STATE_UNSAFE pid=$(cat "$OUTER_PID_FILE")" >&2
  exit 1
fi

if until=$(lease_until); then
  echo "MAINTENANCE_ACTIVE until=$until"
  exit 0
fi

# Check if the process is running
if [[ -f "$PID_FILE" ]]; then
  PID=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if alive_pid_file "$PID_FILE" && "$SUPERVISOR" status >/dev/null 2>&1; then
    # Process is alive
    echo "LEGACY_ROLLBACK_RUNNING pid=$PID"
    exit 0
  fi
  if alive_pid_file "$PID_FILE"; then
    echo "LEGACY_STATE_UNSAFE pid=$PID" >&2
    exit 1
  fi
fi

# Neither accepted outer nor explicit legacy rollback owns the receiver.
# A parent-death SIGTERM may take one bounded long poll to unwind. Wait for the
# old receiver to disappear before launching its replacement; never overlap.
for _ in $(seq 1 100); do
  [[ "$(outer_receiver_count)" -eq 0 ]] && break
  sleep 0.25
done
if [[ "$(outer_receiver_count)" -ne 0 ]]; then
  echo "OUTER_RECEIVER_DRAIN_TIMEOUT" >&2
  exit 1
fi

# Remove only stale outer identity state; the outer supervisor independently
# validates identity and preserves cursor/outbox state under STATE_DIR.
rm -f "$OUTER_PID_FILE" "${OUTER_PID_FILE}.identity"

# Restart the accepted outer production target via its owning supervisor.
export HOME=/home/openclaw
export PATH=/home/openclaw/.npm-global/bin:$PATH
OMEGACLAW_CUTOVER_LOCK_HELD=1 "$OUTER_SUPERVISOR" start 2>&1 || { echo "OUTER_RESTART_FAILED"; exit 1; }

# Verify it came up
sleep 3
if alive_pid_file "$OUTER_PID_FILE" \
  && "$OUTER_SUPERVISOR" owner-alive >/dev/null 2>&1 \
  && "$OUTER_SUPERVISOR" status >/dev/null 2>&1; then
  PID=$(cat "$OUTER_PID_FILE")
  echo "OUTER_RESTARTED pid=$PID"
  exit 0
fi

echo "OUTER_RESTART_FAILED"
exit 1
