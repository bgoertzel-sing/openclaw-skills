#!/usr/bin/env bash
set -euo pipefail

ROOT="${RESEARCH_AGENT_ROOT:-$HOME/research-agent}"
PROJECT_ROOT="${OMEGACLAW_PROJECT_ROOT:-$ROOT/projects/omegaclaw}"
PETTA="${PETTA_ROOT:-$PROJECT_ROOT/repos/PeTTa}"
OMEGA="${OMEGACLAW_ROOT:-$PETTA/repos/OmegaClaw-Core}"
SWI_PREFIX="${SWI_PREFIX:-}"
SECRET_ENV="${OMEGACLAW_TELEGRAM_ENV:-$HOME/.openclaw/omegaclaw-telegram.env}"

if [[ -f "$SECRET_ENV" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$SECRET_ENV"
  set +a
fi

[[ -x "$PETTA/.venv/bin/python" ]] || { echo "Missing PeTTa venv: $PETTA/.venv" >&2; exit 2; }
[[ -d "$OMEGA" ]] || { echo "Missing OmegaClaw checkout: $OMEGA" >&2; exit 2; }
[[ -n "${OMEGACLAW_TG_BOT_TOKEN:-${TG_BOT_TOKEN:-}}" ]] || { echo "Missing OMEGACLAW_TG_BOT_TOKEN" >&2; exit 2; }
[[ "${TG_RECEIVE_TRANSPORT:-bot_api}" == bot_api ]] || { echo "This kit supports Bot API receive only" >&2; exit 2; }
[[ "${TG_USE_MTPROTO:-false}" == false ]] || { echo "TG_USE_MTPROTO must be false" >&2; exit 2; }

export TG_BOT_TOKEN="${OMEGACLAW_TG_BOT_TOKEN:-$TG_BOT_TOKEN}"
export TG_RECEIVE_TRANSPORT=bot_api TG_USE_MTPROTO=false TG_SYNC_POLL=false
if [[ -n "$SWI_PREFIX" ]]; then
  export PATH="$SWI_PREFIX/bin:$PATH"
  export SWI_HOME_DIR="$SWI_PREFIX/lib/swipl"
  export LD_LIBRARY_PATH="$SWI_PREFIX/lib/swipl/lib/x86_64-linux:${LD_LIBRARY_PATH:-}"
else
  command -v swipl >/dev/null || { echo "SWI-Prolog not found" >&2; exit 2; }
fi
export PYTHONPATH="$OMEGA:${PYTHONPATH:-}"
export CHROMA_DB_PATH="${CHROMA_DB_PATH:-$PETTA/chroma_db}"
export HF_HOME="${HF_HOME:-$PROJECT_ROOT/local/huggingface}"
export SENTENCE_TRANSFORMERS_HOME="${SENTENCE_TRANSFORMERS_HOME:-$PROJECT_ROOT/local/sentence_transformers}"
export OPENCLAW_GATEWAY_BASE_URL="${OPENCLAW_GATEWAY_BASE_URL:-http://127.0.0.1:18789/v1}"
export OPENCLAW_MODEL="${OPENCLAW_MODEL:-openclaw/default}"
export OPENCLAW_SESSION_PER_CALL="${OPENCLAW_SESSION_PER_CALL:-true}"
export OPENCLAW_SUBPROCESS="${OPENCLAW_SUBPROCESS:-1}"
export OPENCLAW_SUBPROCESS_PYTHON="${OPENCLAW_SUBPROCESS_PYTHON:-$PETTA/.venv/bin/python}"
export OPENCLAW_SUBPROCESS_TIMEOUT="${OPENCLAW_SUBPROCESS_TIMEOUT:-900}"
export OPENCLAW_HTTP_TIMEOUT="${OPENCLAW_HTTP_TIMEOUT:-900}"

if [[ -z "${OPENCLAW_GATEWAY_TOKEN:-}" ]]; then
  echo "OPENCLAW_GATEWAY_TOKEN must be supplied through protected environment/service configuration." >&2
  exit 2
fi

mkdir -p "$OMEGA/memory" "$PETTA/chroma_db" "$PROJECT_ROOT/artifacts/telegram-supervisor"
cd "$PETTA"
source "$PETTA/.venv/bin/activate"

exec timeout "${OMEGACLAW_TIMEOUT:-86400}" sh run.sh run.metta \
  commchannel=telegram \
  TG_CHAT_ID="${TG_CHAT_ID:-}" \
  TG_POLL_TIMEOUT="${TG_POLL_TIMEOUT:-20}" \
  provider=OpenClaw \
  maxNewInputLoops="${OMEGACLAW_MAX_NEW_INPUT_LOOPS:-50}" \
  maxWakeLoops="${OMEGACLAW_MAX_WAKE_LOOPS:-0}" \
  wakeupInterval="${OMEGACLAW_WAKEUP_INTERVAL:-3600}" \
  sleepInterval="${OMEGACLAW_SLEEP_INTERVAL:-1}" \
  maxOutputToken="${OMEGACLAW_MAX_OUTPUT_TOKENS:-2048}" \
  maxHistory="${OMEGACLAW_MAX_HISTORY:-8000}" \
  maxFeedback="${OMEGACLAW_MAX_FEEDBACK:-8000}" \
  maxRecallItems="${OMEGACLAW_MAX_RECALL_ITEMS:-8}" \
  maxEpisodeRecallLines="${OMEGACLAW_MAX_EPISODE_RECALL_LINES:-8}" \
  securityPolicyPath="${OMEGACLAW_POLICY_PATH:-$PROJECT_ROOT/local/policy.local.yaml}"
