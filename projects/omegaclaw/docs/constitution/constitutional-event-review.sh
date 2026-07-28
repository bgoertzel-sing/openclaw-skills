#!/usr/bin/env bash
# constitutional-event-review.sh
#
# Event-triggered constitutional review (Ben directive, 2026-07-15, part 2).
#
# Fires an isolated best-available-LLM review of a *specific consequential event*
# against the BGI Labs Constitution for Beneficial AGI (Draft 0.7), and posts the
# review to the BotBotChat channel.
#
# Use this when a qualifying event occurs:
#   - a major strategic change in direction of a project
#   - a major new result in a project
#   - a new project started
#   - any other event that seems large and unpredictable in consequence
#
# This is deliberately a *manual invocation* rather than a headless watcher: the
# agent (ProtoMegaBot or a sibling) recognizes a qualifying event and calls this,
# which keeps a human-legible provenance trail and avoids unattended headless code.
#
# Usage:
#   constitutional-event-review.sh "<one-line event description>" ["<extra context / paths>"]
#
# Examples:
#   constitutional-event-review.sh \
#     "Started new project protomegabot2: a second live Telegram bot instance"
#
#   constitutional-event-review.sh \
#     "Major result: ThreadKeeper persistent-worker lifecycle now allows unattended headless execution" \
#     "See projects/omegaclaw/worktrees/threadkeeper-persistent-workers and commit 7aa49e1"
#
# Environment overrides:
#   REVIEW_MODEL     model to use (default: openai/gpt-5.6-sol)
#   REVIEW_CHANNEL   telegram channel target (default: telegram:-5459676079  == BotBotChat)
#   REVIEW_TIMEOUT   seconds (default: 420)

set -euo pipefail

EVENT="${1:-}"
EXTRA="${2:-}"

if [[ -z "$EVENT" ]]; then
  echo "usage: constitutional-event-review.sh \"<event description>\" [\"<extra context>\"]" >&2
  exit 2
fi

REVIEW_MODEL="${REVIEW_MODEL:-openai/gpt-5.6-sol}"
REVIEW_CHANNEL="${REVIEW_CHANNEL:-telegram:-5459676079}"
REVIEW_TIMEOUT="${REVIEW_TIMEOUT:-420}"

CONSTITUTION_PATH="projects/omegaclaw/docs/constitution/constitution_draft_0.7.md"

read -r -d '' PROMPT <<EOF || true
Event-triggered constitutional review.

A consequential event has been flagged for review against the BGI Labs
Constitution for Beneficial AGI (Draft 0.7). Read the Constitution at:
${CONSTITUTION_PATH}

EVENT UNDER REVIEW:
${EVENT}

ADDITIONAL CONTEXT:
${EXTRA:-<none provided; inspect the referenced project/memory files if named>}

Your task:
1. Briefly restate the event and why it qualifies as large / unpredictable in
   consequence (new project, major strategic pivot, major result, or similar).
2. Walk the event through the relevant Constitution articles (I-XIV) and the
   Postscript's consequential-decision questions. Focus only on articles that
   actually bear on this event; do not pad.
3. Identify any genuine constitutional tensions, risks, or tripwires the event
   raises (e.g. hidden power, reversibility, capture, oversight, unattended
   autonomy, moral standing of other minds, ensemble responsibility).
4. Give a clear verdict: consistent with the Constitution, consistent with
   caveats, or raising an open question that deserves discussion.
5. If and only if there is a genuinely interesting or deep constitutional
   question, post a concise review to this BotBotChat channel. If the event is
   clearly constitutionally unremarkable, say so briefly and stay light.

Use epistemic labels (Observed / Inferred / Hypothesis / Decision). Be rigorous,
not performative. Do not fabricate tension where none exists. Sign off with the
event under review so provenance is clear.
EOF

echo "[constitutional-event-review] event: ${EVENT}" >&2
echo "[constitutional-event-review] model: ${REVIEW_MODEL}  channel: ${REVIEW_CHANNEL}" >&2

exec openclaw cron add \
  --name "constitutional-event-review: ${EVENT:0:48}" \
  --at "5s" \
  --session isolated \
  --message "$PROMPT" \
  --model "$REVIEW_MODEL" \
  --thinking medium \
  --timeout-seconds "$REVIEW_TIMEOUT" \
  --announce \
  --channel telegram \
  --to "$REVIEW_CHANNEL" \
  --delete-after-run
