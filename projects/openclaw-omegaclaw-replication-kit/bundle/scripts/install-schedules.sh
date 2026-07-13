#!/usr/bin/env bash
set -euo pipefail
: "${BOT_DISCUSSION_CHAT_ID:?Set BOT_DISCUSSION_CHAT_ID (numeric Telegram group ID)}"
: "${SCHEDULED_UPDATES_CHAT_ID:?Set SCHEDULED_UPDATES_CHAT_ID}"
: "${HUMAN_SUMMARY_CHAT_ID:?Set HUMAN_SUMMARY_CHAT_ID}"
TZ_NAME="${LOCAL_TIMEZONE:-UTC}"
WORKSPACE="${WORKSPACE:-$HOME/research-agent}"
ROUTINE_MODEL="${ROUTINE_MODEL:-openrouter/auto}"
EXPERT_MODEL="${EXPERT_MODEL:-openrouter/auto}"
OMEGA_BOT_USERNAME="${OMEGA_BOT_USERNAME:?Set OMEGA_BOT_USERNAME without @}"

existing="$(openclaw cron list --json 2>/dev/null || printf '{}')"
add() {
  local name="$1"; shift
  if printf '%s' "$existing" | grep -Eq '"name"[[:space:]]*:[[:space:]]*"'"$name"'"'; then echo "skip existing: $name"; return; fi
  echo "add: $name"; openclaw cron add --name "$name" "$@"
}

add 'replica-kanban-refresh' --cron '20 0 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --no-deliver --message \
"Refresh $WORKSPACE/catalog/KANBAN.md from catalog/PROJECTS.md and each active project's TASKS.md/PROJECT.md. Keep project files authoritative, use pointers, preserve owner-needed blockers, and write only if content changes."

add 'replica-scheduler-reconciliation' --cron '45 0 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Audit this agent's cron jobs for missing, duplicate, obsolete, disabled, or repeatedly failing jobs. Compare against $WORKSPACE/cron/replication-schedule.md if present and active projects. Report only actionable discrepancies; do not mutate the scheduler unless explicitly authorized."

add 'replica-recovery-backup' --cron '30 3 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Run $WORKSPACE/bin/sanitized-recovery-backup.sh if present. Verify manifest, secret-scan result, and archive readability. Be silent on unchanged success; report failures or leakage concerns. Never back up credentials, runtime sessions, caches, raw chats, private cloned repositories, or tokens."

add 'replica-project-discovery' --cron '30 6 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Compare $WORKSPACE/catalog/PROJECTS.md with daily project-discussion jobs. Propose jobs for active/idea projects and retirement for paused/completed projects. Do not alter cron automatically. Suppress if no changes are needed."

add 'replica-daily-human-summary' --cron '0 7 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$HUMAN_SUMMARY_CHAT_ID" --best-effort-deliver --message \
"Produce one concise daily summary: completed evidence, active work, failures/risks, owner decisions needed, and today's highest-leverage next steps. Link project/experiment records; do not paste bot-to-bot dialogue."

add 'replica-omegaclaw-watchdog' --every '10m' --command "$WORKSPACE/bin/omegaclaw-watchdog.sh" --command-cwd "$WORKSPACE" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver

add 'replica-ecosystem-health' --cron '30 8 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Run a read-only ecosystem health review: openclaw status/config validation, failed scheduler runs, OmegaClaw supervisor health and one-worker/zero-MTProto topology, Kanban freshness, backup evidence, stale uncommitted work, unfinished experiment records, and disk pressure. Write a dated report under $WORKSPACE/health-reports. Announce only actionable failures/risks."

add 'replica-health-alarm' --cron '0 10 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Verify today's ecosystem health report exists and contains a completed status. Alert if absent/stale or if the health checker itself failed; otherwise output NO_REPLY."

add 'replica-maintenance-reflection' --cron '30 23 * * *' --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --no-deliver --message \
"Review today's recurring friction and failures. Propose reusable workflow/skill improvements with evidence, but do not install, apply, publish, or widen permissions automatically. Record useful proposals in project notes or Skill Workshop."

add 'replica-weekly-frontier-review' --cron '0 14 * * 3' --tz "$TZ_NAME" --session isolated --model "$EXPERT_MODEL" --thinking high --timeout-seconds 3600 --announce --channel telegram --to "$SCHEDULED_UPDATES_CHAT_ID" --best-effort-deliver --message \
"Select the active project least recently expert-reviewed. Independently review its exact commit/run evidence for correctness/invariants, complexity/resources, research design/confounders, security/privacy, and operational boundaries. Store a dated artifact with ranked findings, falsification tests, and disposition. Do not modify code, merge, publish, or spend money."

# Add one daily review job per catalog slug. Stagger from 08:00 onward.
mapfile -t slugs < <(awk -F'|' '/^\|[[:space:]]*[a-z0-9][a-z0-9-]*[[:space:]]*\|/ {gsub(/^[ \t]+|[ \t]+$/,"",$2); gsub(/^[ \t]+|[ \t]+$/,"",$4); if ($4=="active" || $4=="idea") print $2}' "$WORKSPACE/catalog/PROJECTS.md" 2>/dev/null || true)
for i in "${!slugs[@]}"; do
  slug="${slugs[$i]}"; hour=$((8 + i / 2)); minute=$(( (i % 2) * 30 )); (( hour > 17 )) && hour=$((8 + i % 10))
  add "project-bot-discussion-$slug" --cron "$minute $hour * * *" --tz "$TZ_NAME" --session isolated --model "$ROUTINE_MODEL" --timeout-seconds 900 --announce --channel telegram --to "$BOT_DISCUSSION_CHAT_ID" --best-effort-deliver --message \
"Scheduled daily bot-to-bot project review for $slug. Follow the daily-bot-bot-project-discussions skill. Inspect $WORKSPACE/projects/$slug records, experiments, Git state, and recent memory. If an equivalent pivot/status/problem discussion occurred in the previous 24h, output only NO_REPLY. Otherwise post a concise evidence-grounded starter addressed to @$OMEGA_BOT_USERNAME: current focus, one decision/risk/stale assumption, strongest next step, and a request for concrete critique or a Hyperseed/conceptual connection. Keep the exchange advisory and loop-bounded."
done

echo 'Schedules installed. Review with: openclaw cron list --json'
