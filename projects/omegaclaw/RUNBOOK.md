# OmegaClaw Local Install Runbook

Created: `2026-06-26`

## Local layout

- Project notebook: `projects/omegaclaw/`
- PeTTa checkout: `projects/omegaclaw/repos/PeTTa`
- OmegaClaw nested checkout used by PeTTa: `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core`
- ChromaDB helper checkout: `projects/omegaclaw/repos/PeTTa/repos/petta_lib_chromadb`
- Initial standalone OmegaClaw inspection clone: `projects/omegaclaw/repos/OmegaClaw-Core`
- Local SWI-Prolog install: `projects/omegaclaw/local/swipl-9.3.36`
- Python venv: `projects/omegaclaw/repos/PeTTa/.venv`
- Local HuggingFace/SentenceTransformers caches: `projects/omegaclaw/local/huggingface`, `projects/omegaclaw/local/sentence_transformers`
- Local Landlock policy: `projects/omegaclaw/local/policy.local.yaml`

## What was installed

All successful installation work was local/user-space except normal Git clones and Python package downloads:

- Cloned `https://github.com/asi-alliance/OmegaClaw-Core`.
- Cloned `https://github.com/trueagi-io/PeTTa`.
- Cloned `https://github.com/patham9/petta_lib_chromadb`.
- Built SWI-Prolog `V9.3.36` from source under `projects/omegaclaw/local/swipl-9.3.36`, with packages needed by PeTTa/OmegaClaw: `clib`, `pcre`, `swipy` plus required `sgml`.
- Created Python venv under the PeTTa checkout.
- Installed OmegaClaw Python dependencies from `OmegaClaw-Core/requirements.txt`, including `janus-swi==1.5.2` built against the local SWI.
- Downloaded local embedding model `intfloat/e5-large-v2` into project-local cache; load-tested dimension `1024`.

## Environment for local runs

Use `projects/omegaclaw/local/run-omegaclaw-mock.sh` for a mock-channel/mock-provider smoke run.

Use `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh` for a mock-channel run where OmegaClaw uses the local OpenClaw Gateway OpenAI-compatible endpoint as its LLM backend. The wrapper reads the Gateway bearer token from local OpenClaw secret storage at runtime; do not paste or record that token in project files.

Use `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh start|stop|status|log` for a supervised local OpenClaw-backed mock-channel run. This supervisor writes logs under `projects/omegaclaw/artifacts/openclaw-supervisor/`, stores a pid under `projects/omegaclaw/local/run-state/`, and does **not** configure Telegram.

Use `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh` to validate a separate OmegaClaw Telegram bot token without printing the token. Use `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh start|stop|status|log` for the private/direct Telegram smoke. Defaults:

```text
TG_PRIVATE_ONLY=true
TG_ALLOWED_USER_ID=402314199
TG_CHAT_ID=402314199
TG_POLL_TIMEOUT=3
```

The private Telegram scripts require `OMEGACLAW_TG_BOT_TOKEN` or `TG_BOT_TOKEN` in the local environment and refuse to start without it. They also auto-load `/home/openclaw/.openclaw/omegaclaw-telegram.env` by default, or the file named by `OMEGACLAW_TELEGRAM_ENV`. Prefer `OMEGACLAW_TG_BOT_TOKEN` to avoid confusing this with OpenClaw/ZeroBot's existing Telegram token. Do not paste or save Telegram tokens in project files.

Important variables:

```bash
SWI_PREFIX=/home/openclaw/research-agent/projects/omegaclaw/local/swipl-9.3.36
PATH="$SWI_PREFIX/bin:$PATH"
SWI_HOME_DIR="$SWI_PREFIX/lib/swipl"
LD_LIBRARY_PATH="$SWI_PREFIX/lib/swipl/lib/x86_64-linux:${LD_LIBRARY_PATH:-}"
PYTHONPATH=/home/openclaw/research-agent/projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core:$PYTHONPATH
CHROMA_DB_PATH=/home/openclaw/research-agent/projects/omegaclaw/repos/PeTTa/chroma_db
HF_HOME=/home/openclaw/research-agent/projects/omegaclaw/local/huggingface
SENTENCE_TRANSFORMERS_HOME=/home/openclaw/research-agent/projects/omegaclaw/local/sentence_transformers
```

## Verification already run

### SWI library check

```bash
swipl -q -g "use_module(library(janus)),use_module(library(process)),use_module(library(filesex)),use_module(library(pcre)),use_module(library(uuid)),halt."
```

Result: passed.

### PeTTa smoke test

```bash
sh run.sh ./examples/fib.metta
```

Result: passed; output included `is 832040, should 832040. ✅`.

### Python/Janus imports

Python venv import check passed for `torch`, `chromadb`, `janus_swi`, `openai`, and `yaml`.

### OmegaClaw mock startup

Ran OmegaClaw with:

- mock communication channel;
- mock/Test LLM controller;
- local Landlock policy;
- local embedding model;
- no real API keys;
- no Telegram/Mattermost/Slack adapter;
- `timeout 15` so the infinite loop is intentionally interrupted.

Result: initialized policy, memory, knowledge bypass, mock channel, entered repeated iterations, and exited by timeout code `124`. This is expected for a continuous-loop smoke test.

### OmegaClaw via local OpenClaw Gateway

Added a local `OpenClaw` provider in `repos/PeTTa/repos/OmegaClaw-Core/lib_llm_ext.py` using:

```text
OPENCLAW_GATEWAY_BASE_URL=http://127.0.0.1:18789/v1
OPENCLAW_MODEL=openclaw/default
OPENCLAW_SESSION_USER=omegaclaw-local-smoke
```

Ran:

```bash
projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh
```

Result: partial success; local policy and local embeddings initialized, mock channel stayed in use, OpenClaw Gateway returned `HTTP/1.1 200 OK`, and OmegaClaw logged raw OpenClaw response `Understood — I won’t re-send or spam.` The run exited by timeout code `124`, which is expected for the continuous loop. Full record: `projects/omegaclaw/experiments/20260627T063559Z-openclaw-proxy-smoke/RUN.md`.

### Private Telegram smoke

Private/direct Telegram smoke has been live-tested with the separate `@Protomegabot` / ProtomegaTron bot. Local changes/checks:

- `channels/telegram.py` accepts `TG_ALLOWED_USER_ID`, `TG_ALLOWED_USER_IDS`, `TG_PRIVATE_ONLY`, and `TG_SKIP_INITIAL_OFFSET`.
- `TG_PRIVATE_ONLY=true` rejects group/supergroup/channel updates before binding.
- `TG_ALLOWED_USER_ID=402314199` rejects other Telegram senders before binding.
- `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh` runs Telegram private/direct mode with OpenClaw backend and loads `/home/openclaw/.openclaw/omegaclaw-telegram.env` if present.
- `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh` supervises the private Telegram run and loads `/home/openclaw/.openclaw/omegaclaw-telegram.env` if present.
- `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh` validates `getMe` without printing the token and loads `/home/openclaw/.openclaw/omegaclaw-telegram.env` if present.

Checks passed: Python syntax compile, shell syntax checks, allowlist behavior test, supervisor `status`/`stop`, `start` refuses when no token is present, token validator succeeds without printing the token, and a private Telegram message was received and answered by OmegaClaw through Telegram.

Important operational notes:

- Use `TG_SKIP_INITIAL_OFFSET=true` when restarting during diagnostics if pending Telegram updates must be preserved instead of discarded at startup.
- The local Landlock policy must allow read-only access to `/run/systemd/resolve` because `/etc/resolv.conf` symlinks there on this Pop!_OS machine; otherwise Telegram polling fails with DNS `Name or service not known` under policy even though host DNS works.
- The smoke supervisor should be stopped after tests until idle/no-input looping is tuned, because the current OmegaClaw loop can call the OpenClaw backend repeatedly while waiting.
- The current bot token was pasted in chat during setup. Rotation remains recommended, but Ben explicitly accepted skipping rotation on 2026-06-27, so it is not a blocker for supervised testing.

## Known issues / notes

- Default OmegaClaw policy is Docker-oriented and hardcodes `/PeTTa/...`; local non-Docker runs need `projects/omegaclaw/local/policy.local.yaml` or equivalent.
- `maxNewInputLoops=0` exposes an OmegaClaw edge-case bug: `&nextWakeAt` is not initialized before the idle branch. Workaround for smoke: run one loop with the Test provider or patch upstream later.
- Full private Telegram receive/respond smoke is live-tested, but longer unattended Telegram operation is not ready until idle/no-input backend calls are reduced.
- No system `sudo apt` install was completed; admin elevation was unavailable from this Telegram runtime.

## OpenClaw Gateway proxy attempt

On 2026-06-26, OpenClaw's local Gateway was configured to enable its OpenAI-compatible HTTP endpoints:

```text
gateway.http.endpoints.chatCompletions.enabled = true
gateway.http.endpoints.responses.enabled = true
```

`openclaw config validate` passed with only pre-existing stale web-search plugin warnings.

Runtime status:

- Running Gateway URL from `openclaw status`: `ws://127.0.0.1:18789`; HTTP probe `http://127.0.0.1:18789/ready` returns ready.
- After restart, `/v1/chat/completions` is active. An authenticated tiny local request with `model=openclaw/default` returned `omega-ok`.
- Older note: before restart, the endpoint returned `Not Found`; the blocker is now resolved.

OmegaClaw's upstream `GATEWAY_URL` convention appends provider subpaths incompatible with OpenClaw's endpoint shape, so this project currently uses the explicit local `OpenClaw` provider/wrapper instead of `GATEWAY_URL`.

## Next phase

- Decide whether OpenClaw should be used as a full agent target or whether a raw-model route is safer for OmegaClaw's backend prompts.
- Optional/recommended: rotate the current OmegaClaw Telegram bot token in BotFather, update the local secret env file, and validate with `check-omegaclaw-telegram-token.sh`. Ben accepted skipping rotation on 2026-06-27; still keep the private Telegram supervisor limited to supervised testing until idle behavior is tuned.
- Define how OmegaClaw should communicate with OpenClaw/ZeroBot: via Telegram group, via OpenClaw session bridge, or another explicit IPC/API boundary.

## ProtomegaTron prompt customization

For the current Telegram/OpenClaw-backed run, OmegaClaw uses provider `OpenClaw`. Prompt selection in `src/memory.metta` prefers `memory/prompt_OpenClaw.txt` when present, otherwise falls back to `memory/prompt.txt`.

The local ProtomegaTron mandate prompt is:

- `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/memory/prompt_OpenClaw.txt`

Smoke note from 2026-06-27: a bounded run confirmed this prompt was loaded, but `TG_SKIP_INITIAL_OFFSET=true` caused an older pending direct-message update to be processed. For ordinary fresh smoke tests, prefer leaving `TG_SKIP_INITIAL_OFFSET` false so stale messages are discarded at startup.

## Idle/no-input loop behavior

As of 2026-06-27, the local `src/loop.metta` patch starts the Telegram loop quietly with `&loops=0`. Fresh Telegram messages reset the loop budget to `maxNewInputLoops`. Autonomous wake loops only occur when `maxWakeLoops > 0`. This keeps ProtomegaTron active as a Telegram listener without repeatedly calling the OpenClaw backend while merely waiting for input.

## Shared Telegram group setup

For shared Ben + ZeroBot + ProtomegaTron testing, use the runner's `TG_CHAT_AUTO_BIND=true` mode with `TG_CHAT_ID` empty, `TG_PRIVATE_ONLY=false`, and `TG_ALLOWED_USER_IDS=402314199`. On the first fresh allowed message in the new group, the Telegram adapter binds to that group chat id. After discovery, record the group chat id in local secret/config state rather than project files if it is considered private.

To let ProtomegaTron see ordinary group messages, disable BotFather privacy for `@Protomegabot`; otherwise it will only see commands/mentions/replies that Telegram delivers to the bot.
