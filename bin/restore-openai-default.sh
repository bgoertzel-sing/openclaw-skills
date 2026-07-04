#!/usr/bin/env bash
set -euo pipefail

# Restore ZeroBot / main OpenClaw agent to the known-good OpenAI default route.
# Intended to be run from the ben account if an OpenRouter/other provider switch or
# intent-router plugin change breaks replies.

OPENCLAW_HOME="/home/openclaw"
OPENCLAW_BIN="/home/openclaw/.npm-global/bin/openclaw"
MODEL_JSON='{"primary":"openai/gpt-5.5","fallbacks":["openai/gpt-5.5"]}'

run_as_openclaw() {
  sudo -u openclaw -H env HOME="$OPENCLAW_HOME" PATH="/home/openclaw/.npm-global/bin:$PATH" "$@"
}

echo "Restoring OpenClaw main-agent model route to: $MODEL_JSON"
run_as_openclaw "$OPENCLAW_BIN" config set agents.defaults.model "$MODEL_JSON" --strict-json

if run_as_openclaw "$OPENCLAW_BIN" config get plugins.entries.intent-model-router --json >/dev/null 2>&1; then
  echo "Disabling intent-model-router plugin for recovery..."
  run_as_openclaw "$OPENCLAW_BIN" config set plugins.entries.intent-model-router.enabled false --strict-json || true
fi

echo "Restarting OpenClaw gateway so the restored config is active..."
if ! run_as_openclaw "$OPENCLAW_BIN" gateway restart; then
  echo "Normal gateway restart failed. If this is a system service, run:"
  echo "  sudo systemctl restart openclaw-agent.service"
  exit 1
fi

echo "Current model status:"
run_as_openclaw "$OPENCLAW_BIN" models status

echo "Done. If Telegram still does not respond, wait ~10 seconds and send: ping"
