#!/usr/bin/env bash
set -euo pipefail
ROOT="${RESEARCH_AGENT_ROOT:-$HOME/research-agent}"
SUP="${OMEGACLAW_SUPERVISOR:-$ROOT/projects/omegaclaw/local/omegaclaw-supervisor.sh}"
STATE="${XDG_STATE_HOME:-$HOME/.local/state}/omegaclaw-watchdog"
mkdir -p "$STATE"
now=$(date +%s); window="$STATE/restarts.tsv"; touch "$window"
awk -v n="$now" '$1 > n-3600' "$window" >"$window.tmp" && mv "$window.tmp" "$window"
if "$SUP" health >/dev/null 2>&1; then exit 0; fi
count=$(wc -l <"$window")
if (( count >= 3 )); then echo "OmegaClaw unhealthy; restart ceiling (3/hour) reached"; exit 1; fi
printf '%s\twatchdog\n' "$now" >>"$window"
"$SUP" restart
"$SUP" health
