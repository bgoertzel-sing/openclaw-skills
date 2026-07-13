#!/usr/bin/env bash
set -euo pipefail
ROOT="${RESEARCH_AGENT_ROOT:-$HOME/research-agent}"
PROJECT_ROOT="${OMEGACLAW_PROJECT_ROOT:-$ROOT/projects/omegaclaw}"
RUNNER="${OMEGACLAW_RUNNER:-$PROJECT_ROOT/local/run-omegaclaw-telegram.sh}"
LOG_DIR="${OMEGACLAW_LOG_DIR:-$PROJECT_ROOT/artifacts/telegram-supervisor}"
PID_FILE="$LOG_DIR/omegaclaw.pid"
OUT_LOG="$LOG_DIR/omegaclaw.log"
SUP_LOG="$LOG_DIR/supervisor.log"
LOCK_FILE="$LOG_DIR/supervisor.lock"
mkdir -p "$LOG_DIR"

pid_live() { [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; }
topology() {
  local workers mtproto
  workers="$(pgrep -af 'sh run.sh run.metta.*commchannel=telegram' | grep -v grep | wc -l | tr -d ' ')"
  mtproto="$(pgrep -af 'telegram_mtproto_bridge.py' | grep -v grep | wc -l | tr -d ' ')"
  printf 'workers=%s mtproto_bridges=%s\n' "$workers" "$mtproto"
  [[ "$workers" -eq 1 && "$mtproto" -eq 0 ]]
}
start() {
  exec 9>"$LOCK_FILE"
  flock -n 9 || { echo "Another supervisor action is running" >&2; exit 1; }
  if pid_live; then echo "already running pid=$(cat "$PID_FILE")"; topology; return; fi
  [[ -x "$RUNNER" ]] || { echo "Missing executable runner: $RUNNER" >&2; exit 2; }
  nohup "$RUNNER" >>"$OUT_LOG" 2>&1 & echo $! >"$PID_FILE"
  sleep 2
  if pid_live; then echo "started pid=$(cat "$PID_FILE")" | tee -a "$SUP_LOG"; topology || true
  else echo "failed to start; inspect $OUT_LOG" >&2; exit 1; fi
}
stop() {
  if pid_live; then
    pid="$(cat "$PID_FILE")"; kill "$pid"; for _ in {1..20}; do kill -0 "$pid" 2>/dev/null || break; sleep 0.25; done
    kill -0 "$pid" 2>/dev/null && kill -KILL "$pid" || true
  fi
  rm -f "$PID_FILE"; echo stopped
}
status() {
  if pid_live; then echo "running pid=$(cat "$PID_FILE")"; topology
  else echo stopped; rm -f "$PID_FILE"; return 1; fi
}
health() {
  pid_live && topology && grep -qE '\[Telegram\]|HUMAN-MSG|Polling' "$OUT_LOG"
}
case "${1:-status}" in start) start;; stop) stop;; restart) stop; start;; status) status;; health) health;; *) echo "usage: $0 {start|stop|restart|status|health}" >&2; exit 2;; esac
