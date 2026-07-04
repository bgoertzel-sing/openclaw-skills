#!/usr/bin/env bash
# Read-only status collector for Codex CLI loops on defective-mind-uploader.
set -euo pipefail
HOST="${MAC_CODEX_HOST:-bengoertzel@100.105.177.92}"
ssh -o ConnectTimeout=10 "$HOST" 'set -euo pipefail
ROOT="$HOME/Documents/Codex/2026-06-17/i-want-to-have-you-work"
echo "# Mac Codex status $(date "+%Y-%m-%d %H:%M:%S %Z")"
echo
printf "host: "; hostname
printf "user: "; whoami
echo

echo "## launchd"
launchctl list | egrep "com.bengoertzel.codex.(relaleap|omegasim|git-auto-push)" || true

echo
 echo "## active Codex exec processes"
ps aux | grep "/Applications/Codex.app/Contents/Resources/codex .* exec" | grep -v grep || true

echo
 echo "## locks"
for name in relaleap omegasim; do
  d="/tmp/${name}-cli-loop.lock"
  echo "### $name"
  if [ -d "$d" ]; then
    ls -la "$d"
    if [ -f "$d/pid" ]; then
      pid=$(cat "$d/pid" 2>/dev/null || true)
      echo "lock_pid=$pid"
      [ -n "$pid" ] && ps -p "$pid" -o pid,ppid,stat,etime,command || true
    fi
  else
    echo "no lock"
  fi
done

echo
 echo "## repository summaries"
for repo in relaleap omegasim; do
  echo "### $repo"
  cd "$ROOT/$repo"
  echo "branch=$(git rev-parse --abbrev-ref HEAD)"
  echo "head=$(git log -1 --oneline)"
  echo "status:"
  git status --short || true
  if [ -f AUTOMATION_STATUS.md ]; then
    echo "current_focus_excerpt:"
    awk "/^## Current Focus/{flag=1; count=0; next} /^## Previous Run/{flag=0} flag && count<35 {print; count++}" AUTOMATION_STATUS.md || true
  fi
done

echo
 echo "## recent loop logs"
for name in relaleap omegasim git-auto-push; do
  log="$ROOT/outputs/${name}.log"
  # actual loop log names include -cli-loop for project loops
  [ "$name" = relaleap ] && log="$ROOT/outputs/relaleap-cli-loop.log"
  [ "$name" = omegasim ] && log="$ROOT/outputs/omegasim-cli-loop.log"
  echo "### $name log: $log"
  tail -25 "$log" 2>/dev/null || echo "no log"
done
'
