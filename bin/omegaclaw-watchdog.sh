#!/usr/bin/env bash
# Watchdog for OmegaClaw Telegram private supervisor.
# Checks if the process is alive; if not, cleans up and restarts.
# Returns 0 if running fine, 0 if restarted successfully, 1 if restart failed.
set -euo pipefail

SUPERVISOR="/home/openclaw/research-agent/projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh"
PID_FILE="/home/openclaw/research-agent/projects/omegaclaw/local/run-state/omegaclaw-telegram-private.pid"

# Check if the process is running
if [[ -f "$PID_FILE" ]]; then
  PID=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
    # Process is alive
    echo "ALREADY_RUNNING pid=$PID"
    exit 0
  fi
fi

# Process is dead or missing — clean up and restart
rm -f "$PID_FILE"

# Restart via supervisor
export HOME=/home/openclaw
export PATH=/home/openclaw/.npm-global/bin:$PATH
"$SUPERVISOR" start 2>&1 || { echo "RESTART_FAILED"; exit 1; }

# Verify it came up
sleep 3
if [[ -f "$PID_FILE" ]]; then
  PID=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
    echo "RESTARTED pid=$PID"
    exit 0
  fi
fi

echo "RESTART_FAILED"
exit 1
