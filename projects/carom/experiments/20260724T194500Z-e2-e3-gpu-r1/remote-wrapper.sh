#!/usr/bin/env bash
set -uo pipefail
root=/workspace/carom-e2-e3
date -u +%FT%TZ > "$root/started_at.txt"
timeout --signal=TERM --kill-after=60s 31800s \
  bash "$root/command.sh" > "$root/stdout.log" 2> "$root/stderr.log"
status=$?
printf '%s\n' "$status" > "$root/exit-status.txt"
date -u +%FT%TZ > "$root/finished_at.txt"
find "$root/results" -type f -print0 \
  | sort -z \
  | xargs -0 -r sha256sum > "$root/results-sha256.txt"
exit "$status"
