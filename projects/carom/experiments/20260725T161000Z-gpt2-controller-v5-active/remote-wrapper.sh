#!/usr/bin/env bash
set -uo pipefail
run_root=/workspace/carom-gpt2-v5
date -u +%FT%TZ > "$run_root/started_at.txt"
timeout --signal=TERM --kill-after=60s 6900s \
  bash "$run_root/command.sh" > "$run_root/stdout.log" 2> "$run_root/stderr.log"
run_status=$?
printf '%s\n' "$run_status" > "$run_root/exit-status.txt"
date -u +%FT%TZ > "$run_root/finished_at.txt"
exit "$run_status"
