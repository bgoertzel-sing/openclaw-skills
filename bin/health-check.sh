#!/usr/bin/env bash
# Daily health check for Protobots ecosystem
# Writes a dated report to health-reports/ and prints summary for sending
set -euo pipefail

TODAY=$(date +%Y-%m-%d)
REPORT_DIR="$HOME/research-agent/health-reports"
REPORT_FILE="$REPORT_DIR/${TODAY}.md"
mkdir -p "$REPORT_DIR"

# Collect status lines
STATUS_LINES=()
ALERTS=()

# 1. ProtoMegaBot supervisor
PM_STATUS=$(cd "$HOME/research-agent" && projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh status 2>&1 || echo "INACTIVE/ERROR")
# Supervisor reports "owner-active pid ..." (or "active"); treat both as healthy.
if echo "$PM_STATUS" | grep -qE "^(owner-)?active"; then
  STATUS_LINES+=("✅ ProtoMegaBot supervisor: active")
else
  STATUS_LINES+=("❌ ProtoMegaBot supervisor: $PM_STATUS")
  ALERTS+=("ProtoMegaBot supervisor not active")
fi

# 2. OpenClaw/Gateway status
# `openclaw status` renders a wide table; scan the whole output, not just head.
OC_STATUS=$(openclaw status 2>&1 || echo "ERROR")
if echo "$OC_STATUS" | grep -qiE "running|active \(running\)|healthy|Dashboard"; then
  STATUS_LINES+=("✅ OpenClaw Gateway: running")
else
  STATUS_LINES+=("⚠️ OpenClaw Gateway: $OC_STATUS")
  ALERTS+=("OpenClaw Gateway may not be healthy")
fi

# 3. Cron jobs with error status — check via the cron tool
# (This is done by the caller agent, not this script, since it needs the cron tool)

# 4. Kanban freshness
KANBAN_FILE="$HOME/research-agent/catalog/KANBAN.md"
if [ -f "$KANBAN_FILE" ]; then
  KANBAN_DATE=$(grep -oP 'Last updated: \K[0-9-]+' "$KANBAN_FILE" 2>/dev/null || echo "unknown")
  TODAY_EPOCH=$(date -d "$TODAY" +%s 2>/dev/null || date +%s)
  if [ "$KANBAN_DATE" != "unknown" ]; then
    KANBAN_EPOCH=$(date -d "$KANBAN_DATE" +%s 2>/dev/null || echo 0)
    AGE_DAYS=$(( (TODAY_EPOCH - KANBAN_EPOCH) / 86400 ))
    if [ "$AGE_DAYS" -le 1 ]; then
      STATUS_LINES+=("✅ Kanban board: fresh ($KANBAN_DATE, ${AGE_DAYS}d old)")
    elif [ "$AGE_DAYS" -le 3 ]; then
      STATUS_LINES+=("⚠️ Kanban board: stale ($KANBAN_DATE, ${AGE_DAYS}d old)")
      ALERTS+=("Kanban board ${AGE_DAYS}d stale")
    else
      STATUS_LINES+=("❌ Kanban board: very stale ($KANBAN_DATE, ${AGE_DAYS}d old)")
      ALERTS+=("Kanban board ${AGE_DAYS}d stale — needs refresh")
    fi
  else
    STATUS_LINES+=("⚠️ Kanban board: unknown freshness")
    ALERTS+=("Kanban freshness unknown")
  fi
else
  STATUS_LINES+=("❌ Kanban board: file missing")
  ALERTS+=("Kanban file missing")
fi

# 5. Agent-recovery backup freshness
RECOVERY_DIR="$HOME/research-agent/projects/agent-recovery"
if [ -d "$RECOVERY_DIR" ]; then
  # Freshness = most recent git commit across the recovery repos (the backup
  # pushes commits). Sampling loose *.json/RUN.md files reported stale content
  # mtimes (e.g. a 07-06 persona file) even when today's backup succeeded.
  BACKUP_MTIME=0
  for RECOVERY_REPO in "$RECOVERY_DIR"/repos/*/; do
    if [ -d "$RECOVERY_REPO/.git" ]; then
      REPO_COMMIT_TS=$(cd "$RECOVERY_REPO" && git log -1 --format=%ct 2>/dev/null || echo 0)
      if [ "$REPO_COMMIT_TS" -gt "$BACKUP_MTIME" ]; then
        BACKUP_MTIME=$REPO_COMMIT_TS
      fi
    fi
  done
  if [ "$BACKUP_MTIME" -gt 0 ]; then
    NOW=$(date +%s)
    BACKUP_AGE_H=$(( (NOW - BACKUP_MTIME) / 3600 ))
    if [ "$BACKUP_AGE_H" -le 30 ]; then
      STATUS_LINES+=("✅ Agent recovery: recent activity (${BACKUP_AGE_H}h ago)")
    else
      STATUS_LINES+=("⚠️ Agent recovery: last activity ${BACKUP_AGE_H}h ago")
      ALERTS+=("Agent recovery backup ${BACKUP_AGE_H}h old")
    fi
  fi
fi

# 6. Uncommitted work older than 1 day in key repos
for REPO in \
  "$HOME/research-agent/projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core" \
  "$HOME/research-agent/projects/specatom-hs/repos/specatom-hs" \
  "$HOME/research-agent/projects/petta-chem/repos/petta-chem" \
  "$HOME/research-agent/projects/petta-memory/repos/petta-memory" \
  "$HOME/research-agent/projects/relaleap/worktrees/slt-integration"; do
  if [ -d "$REPO/.git" ]; then
    REPO_NAME=$(basename "$REPO")
    DIFF_COUNT=$(cd "$REPO" && git status --porcelain 2>/dev/null | wc -l || echo 0)
    if [ "$DIFF_COUNT" -gt 0 ]; then
      # Check oldest uncommitted file age
      OLDEST_FILE=$(cd "$REPO" && git status --porcelain 2>/dev/null | awk '{print $2}' | head -1)
      if [ -n "$OLDEST_FILE" ] && [ -f "$REPO/$OLDEST_FILE" ]; then
        FILE_MTIME=$(stat -c %Y "$REPO/$OLDEST_FILE" 2>/dev/null || echo 0)
        NOW=$(date +%s)
        FILE_AGE_H=$(( (NOW - FILE_MTIME) / 3600 ))
        if [ "$FILE_AGE_H" -ge 24 ]; then
          STATUS_LINES+=("⚠️ $REPO_NAME: $DIFF_COUNT uncommitted files, oldest ${FILE_AGE_H}h")
          ALERTS+=("$REPO_NAME has uncommitted work older than 24h")
        fi
      fi
    fi
  fi
done

# 7. ProtoMegaBot log freshness (last log line within 10 min)
PM_LOG="$HOME/research-agent/projects/omegaclaw/artifacts/telegram-private-supervisor/omegaclaw-telegram-private.log"
if [ -f "$PM_LOG" ]; then
  LOG_MTIME=$(stat -c %Y "$PM_LOG" 2>/dev/null || echo 0)
  NOW=$(date +%s)
  LOG_AGE_M=$(( (NOW - LOG_MTIME) / 60 ))
  if [ "$LOG_AGE_M" -le 10 ]; then
    STATUS_LINES+=("✅ ProtoMegaBot log: active (${LOG_AGE_M}m ago)")
  elif [ "$LOG_AGE_M" -le 60 ]; then
    STATUS_LINES+=("⚠️ ProtoMegaBot log: ${LOG_AGE_M}m since last write")
  else
    STATUS_LINES+=("❌ ProtoMegaBot log: ${LOG_AGE_M}m since last write")
    ALERTS+=("ProtoMegaBot log inactive for ${LOG_AGE_M}m")
  fi
fi

# 7b. Previous day's alarm verification
#     The alarm cron (b2b7d564) should have run yesterday at 10:00 Pacific.
#     It always writes an 'alarm-ran' marker; if it found the health report
#     missing, it also writes an 'alarm-fired' sentinel and alerts BotBotChats.
YESTERDAY=$(date -d "$TODAY - 1 day" +%Y-%m-%d 2>/dev/null || date -v-1d +%Y-%m-%d 2>/dev/null || echo "")
YESTERDAY_REPORT="$REPORT_DIR/${YESTERDAY}.md"
ALARM_RAN_MARKER="$REPORT_DIR/${YESTERDAY}-alarm-ran.txt"
ALARM_FIRED_SENTINEL="$REPORT_DIR/${YESTERDAY}-alarm-fired.txt"
if [ -n "$YESTERDAY" ]; then
  # Check yesterday's health report
  if [ ! -f "$YESTERDAY_REPORT" ]; then
    STATUS_LINES+=("❌ Yesterday ($YESTERDAY) health report missing — health checker failed yesterday")
    ALERTS+=("Yesterday's health check did not run (report file missing)")
  fi
  # Check that the alarm cron itself ran
  if [ -f "$ALARM_RAN_MARKER" ]; then
    if [ -f "$ALARM_FIRED_SENTINEL" ]; then
      STATUS_LINES+=("⚠️ Yesterday ($YESTERDAY) alarm ran AND fired — health checker was broken yesterday")
      ALERTS+=("Yesterday's alarm fired (health checker was down)")
    else
      STATUS_LINES+=("✅ Yesterday ($YESTERDAY) alarm: ran clean (no issues detected)")
    fi
  else
    STATUS_LINES+=("❌ Yesterday ($YESTERDAY) alarm did not run — alarm cron itself failed")
    ALERTS+=("Yesterday's alarm cron did not execute (no alarm-ran marker found)")
  fi
fi

# Write report
{
  echo "# Daily Health Report — $TODAY"
  echo ""
  echo "Generated: $(date -Iseconds)"
  echo ""
  echo "## Status"
  for line in "${STATUS_LINES[@]}"; do
    echo "- $line"
  done
  echo ""
  if [ ${#ALERTS[@]} -gt 0 ]; then
    echo "## ⚠️ Alerts"
    for alert in "${ALERTS[@]}"; do
      echo "- $alert"
    done
  else
    echo "## ✅ No alerts"
  fi
  echo ""
  echo "## Cron job status"
  echo "(Checked separately by agent via cron tool)"
} > "$REPORT_FILE"

# Print summary for the agent to relay
if [ ${#ALERTS[@]} -gt 0 ]; then
  echo "HEALTH_CHECK: $TODAY — ${#ALERTS[@]} alert(s): ${ALERTS[*]}"
else
  echo "HEALTH_CHECK: $TODAY — all systems nominal"
fi
echo "REPORT_FILE: $REPORT_FILE"
