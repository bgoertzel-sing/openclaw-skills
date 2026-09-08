#!/usr/bin/env bash
# Bounded Phase-7 group canary launcher for ProtoCosmo2.
#
# Fixes from the 2026-08-06 orphaned-responder failure (run
# 20260806T194326Z-protocosmo2-phase7-group-canary-20260806):
#  - The launcher owns the runner for the whole canary; an EXIT trap always
#    terminates it, so the runner/responder can never be orphaned.
#  - A durable pending_inbound state is treated as normal progress, never as
#    a launch failure.
#  - Success requires exactly one NEW delivered group reply of kind "reply";
#    a fixed visible-failure reply is reported as a distinct failure verdict.
set -uo pipefail

RUNNER=/home/openclaw/research-agent/projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py
CORE=/home/openclaw/research-agent/projects/omegaclaw/worktrees/protocosmo2-phase6-live
PETTA=/home/openclaw/research-agent/projects/omegaclaw/protocosmo2/phase2-checked-baseline/repos/PeTTa
DRIVER=/home/openclaw/research-agent/projects/omegaclaw/protocosmo2/tools/phase5_omegaclaw_case.py
CONFIG=/home/openclaw/.openclaw/protocosmo2-canary.json
STATE_DIR=/home/openclaw/.openclaw/protocosmo2-canary-state
STATE="$STATE_DIR/state.json"
LOG=/home/openclaw/.openclaw/protocosmo2-canary.log
GROUP_CHAT_ID=-1003983157420
WAIT_SECONDS="${1:-600}"

verdict() { # $1=verdict $2=optional reason
  if [ -n "${2:-}" ]; then
    jq -nc --arg v "$1" --arg r "$2" '{verdict:$v, reason:$r}'
  else
    jq -nc --arg v "$1" '{verdict:$v}'
  fi
}

runner_pid=""
cleanup() {
  if [ -n "$runner_pid" ]; then
    kill -TERM "$runner_pid" 2>/dev/null
    for _ in $(seq 1 20); do
      kill -0 "$runner_pid" 2>/dev/null || break
      sleep 0.5
    done
    kill -KILL "$runner_pid" 2>/dev/null
    wait "$runner_pid" 2>/dev/null
  fi
}
trap cleanup EXIT

# Preflight
[ "$(stat -c %a "$CONFIG")" = 600 ] || { verdict fail "config mode not 0600"; exit 1; }
[ "$(stat -c %a "$STATE_DIR")" = 700 ] || { verdict fail "state dir mode not 0700"; exit 1; }
if pgrep -f "[p]hase6_private_canary_runner" >/dev/null; then
  verdict fail "runner already active"; exit 1
fi
jq -e '.pending_inbound == null' "$STATE" >/dev/null || { verdict fail "dirty pending_inbound before start"; exit 1; }
before=$(jq '.outbox | length' "$STATE")

python3 "$RUNNER" --core "$CORE" --petta "$PETTA" --driver "$DRIVER" </dev/null >>"$LOG" 2>&1 &
runner_pid=$!

# Wait for the runner's started event.
started=0
for _ in $(seq 1 30); do
  kill -0 "$runner_pid" 2>/dev/null || { verdict fail "runner exited during startup"; exit 1; }
  if tail -n 50 "$LOG" | grep -q '"event": "started"'; then started=1; break; fi
  sleep 1
done
[ "$started" = 1 ] || { verdict fail "no started event within 30s"; exit 1; }
jq -nc --argjson pid "$runner_pid" --argjson before "$before" '{verdict:"started", pid:$pid, outbox_before:$before}'

# Wait for exactly one new delivered group reply.
deadline=$(( $(date +%s) + WAIT_SECONDS ))
while [ "$(date +%s)" -lt "$deadline" ]; do
  kill -0 "$runner_pid" 2>/dev/null || { verdict fail "runner died while waiting"; exit 1; }
  new_count=$(jq --argjson before "$before" '[.outbox[$before:][] | select(.delivery != null)] | length' "$STATE")
  pending_clear=$(jq -r '.pending_inbound == null' "$STATE")
  if [ "$new_count" -ge 1 ] && [ "$pending_clear" = "true" ]; then
    kinds=$(jq -c --argjson before "$before" '[.outbox[$before:][] | .kind]' "$STATE")
    receipts=$(jq -c --argjson before "$before" '[.outbox[$before:][] | .delivery.receipt]' "$STATE")
    chats=$(jq -c --argjson before "$before" '[.outbox[$before:][] | .chat_id] | unique' "$STATE")
    if [ "$new_count" -gt 1 ]; then
      verdict fail "duplicate deliveries: $new_count"; exit 1
    fi
    if [ "$chats" != "[$GROUP_CHAT_ID]" ]; then
      verdict fail "delivery to unexpected chat: $chats"; exit 1
    fi
    case "$kinds" in
      '["reply"]')
        jq -nc --argjson receipts "$receipts" '{verdict:"delivered", receipts:$receipts}'
        exit 0
        ;;
      *)
        verdict fail "fixed failure path used instead of model reply: $kinds"; exit 1
        ;;
    esac
  fi
  sleep 2
done
verdict timeout "no delivered group reply within ${WAIT_SECONDS}s"
exit 1
