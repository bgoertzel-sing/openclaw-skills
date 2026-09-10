#!/usr/bin/env bash
# Phase 0 instrumentation: measure no-op invocation rate, duplicate outbound
# rate, and token/cost baselines from OpenClaw session logs. Read-only.
#
# Usage: measure_baseline.sh <agentId> [sessions_dir]
# Emits run-level JSONL to stdout; aggregate with aggregate_baseline.py.
set -euo pipefail

AGENT_ID="${1:?agentId required}"
SESSION_DIR="${2:-${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/agents/$AGENT_ID/sessions}"

find "$SESSION_DIR" -maxdepth 1 -type f \
  \( -name '*.jsonl' -o -name '*.jsonl.reset.*Z' -o -name '*.jsonl.deleted.*Z' \) -print0 |
while IFS= read -r -d '' f; do
  jq -cn --arg file "$(basename "$f")" '
    # A "run" = assistant LLM calls following one user message, up to the next
    # user message. Terminal text = text of the last non-toolUse assistant
    # message in the run (what the user would actually see).
    reduce (inputs | select(.type == "message")) as $m
      ({runs: [], cur: null};
        if $m.message.role == "user" then
          (if .cur then .runs += [.cur] else . end)
          | .cur = {
              calls: 0, cost: 0.0, tok: 0, text: "",
              ts: ($m.timestamp // ""),
              trig: ([$m.message.content[]? | select(.type == "text") | .text]
                     | join(" ") | .[0:300])
            }
        elif $m.message.role == "assistant" and .cur then
          .cur.calls += 1
          | .cur.cost += ($m.message.usage.cost.total // 0)
          | .cur.tok  += ($m.message.usage.totalTokens // 0)
          | (if ($m.message.stopReason // "") != "toolUse" then
               .cur.text = ([$m.message.content[]? | select(.type == "text") | .text]
                            | join(" "))
             else . end)
        else . end)
    | (if .cur then .runs += [.cur] else . end)
    | .runs[] | select(.calls > 0)
    | {file: $file, ts, calls, cost, tok,
       text: (.text | gsub("\\s+"; " ") | .[0:200]),
       trig_hb: (.trig | test("heartbeat"; "i"))}
  ' "$f" 2>/dev/null
done
