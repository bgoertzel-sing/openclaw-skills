# OmegaClaw Core Installation

- Slug: `omegaclaw`
- Status: `active`
- Created: `2026-06-26`
- Last reviewed: `2026-06-26`
- Owner: Benjamin Goertzel

## Purpose

Install and validate OmegaClaw Core locally on the OpenClaw research workstation, then prepare a safe second phase for communication with Benjamin via Telegram, with ZeroBot/OpenClaw, and eventually in a shared Telegram group.

## Success criteria

Initial install success:

- OmegaClaw-Core, PeTTa, and `petta_lib_chromadb` are cloned in a reproducible project layout.
- Required SWI-Prolog/PeTTa/Python dependencies are installed without clobbering system state.
- PeTTa smoke test passes.
- OmegaClaw starts locally in a controlled mock mode without real Telegram/API credentials.
- Install notes and launch environment are recorded.

Second-phase success, not yet attempted:

- Decide a safe communication architecture and auth boundaries.
- Configure OmegaClaw to talk to Benjamin via Telegram.
- Configure controlled OmegaClaw ↔ ZeroBot/OpenClaw communication.
- Configure a Telegram group path if still desired.

## Scope

### In scope

- Local user-space installation where possible.
- Repository inspection before running install logic.
- Local SWI-Prolog build if distro packages are unavailable/too old.
- Python venv under the project tree.
- Mock-channel/mock-provider smoke tests.
- Telegram/channel planning after local runtime is stable.

### Out of scope for now

- Installing real Telegram bot tokens or LLM provider credentials without a separate explicit configuration step.
- Giving OmegaClaw broad filesystem/network authority before policy review.
- Running uncontrolled long-lived loops or self-starting services.
- Paid compute.

## Current state

OmegaClaw is installed enough to run locally in mock mode.

Observed on 2026-06-26:

- Cloned OmegaClaw-Core, PeTTa, and `petta_lib_chromadb`.
- Built local SWI-Prolog `9.3.36` from source because `swipl` was absent and the Pop/Ubuntu apt candidate was SWI `8.4.2`, too old for this stack.
- Rebuilt SWI with PeTTa/OmegaClaw-required libraries: `janus`, `process`, `filesex`, `pcre`, `uuid`.
- Created Python venv and installed `OmegaClaw-Core/requirements.txt`; `janus-swi==1.5.2` built successfully against local SWI.
- Downloaded local embedding model `intfloat/e5-large-v2`; load-tested dimension `1024`.
- PeTTa `examples/fib.metta` smoke test passed.
- OmegaClaw mock startup/loop smoke passed using `projects/omegaclaw/local/run-omegaclaw-mock.sh`; expected timeout exit `124` was treated as success for the continuous loop.
- OpenClaw Gateway `/v1/chat/completions` is active locally and authenticated tiny prompt returned `omega-ok`.
- Added local OmegaClaw `OpenClaw` provider and wrapper `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh`; experiment `projects/omegaclaw/experiments/20260627T063559Z-openclaw-proxy-smoke/` confirmed OmegaClaw can call OpenClaw Gateway (`HTTP/1.1 200 OK`) with mock channel and local embeddings. Timeout exit `124` remains expected for bounded continuous-loop smokes.
- Added local supervisor `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh` with `start|stop|status|log` for OpenClaw-backed mock-channel runs. It is not a Telegram integration and should stay supervised.
- Prepared private/direct Telegram path: local `channels/telegram.py` now supports `TG_ALLOWED_USER_ID(S)`, `TG_PRIVATE_ONLY`, and `TG_SKIP_INITIAL_OFFSET`; added `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`, `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`, and `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh`. Defaults allow only Telegram user/chat `402314199` and private chats. On 2026-06-27 after Benjamin messaged `@protomegabot` and got no reply, diagnosis showed the Telegram supervisor inactive/no-token first, then repeated Telegram polling DNS failures under the local Landlock policy. Root cause was `/etc/resolv.conf` symlinking into `/run/systemd/resolve`, which the policy did not allow. The local policy now grants read-only access to `/run/systemd/resolve`. The runner/validator/supervisor auto-load `/home/openclaw/.openclaw/omegaclaw-telegram.env` if present. Benjamin provided the separate OmegaClaw bot token in chat; it was saved only to the local secret env file with mode `0600`, validated via Telegram `getMe` as username `Protomegabot`, and the private Telegram supervisor was started with user/chat allowlist `402314199`. The Telegram smoke then succeeded: Benjamin reported receiving a reply from `@Protomegabot` / ProtomegaTron. The smoke supervisor was stopped afterward to avoid idle backend calls. Because the token was pasted into chat, it should be rotated in BotFather.
- On 2026-06-28, after `@Protomegabot` could not see Telegram documents posted to the shared group, upgraded the runtime adapter in `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/channels/telegram.py` so document attachments are downloaded, text-like files are inserted into the inbound prompt as untrusted attachment content, and PDFs are extracted with local `pdftotext`. Large extracted attachments are now chunked: the full extraction is saved as `.extracted.txt`, split into `.chunkNNN.txt`, and the prompt receives a first-chunk preview plus chunk paths that ProtomegaTron can inspect via `read-file`. Limits are configurable via `TG_ATTACHMENT_MAX_BYTES` and `TG_ATTACHMENT_MAX_CHARS`; default storage is `/home/openclaw/tmp/omegaclaw-telegram-attachments`. The supervised group run was restarted and verified active.
- Later on 2026-06-28, diagnosed repeated deep-call stalls after Ben asked whether `@Protomegabot` was thinking or stalling. `openclaw status` showed the fixed ProtoMegaTron Gateway `user` session had grown to about `998k/272k` tokens, while fresh/unique-user health checks returned normally. Patched `lib_llm_ext.py` to support per-call Gateway sessions because OmegaClaw already supplies its own prompt/history, to return user-visible `(send ...)` diagnostics for backend failure/timeout/empty output instead of silent `()`, and to preserve more traceback detail. Patched the Telegram runner to use per-call sessions and aligned 900s HTTP/subprocess timeouts. Patched the supervisor so nonzero runner exits no longer kill the supervisor under `set -e`. Verification: Python compile, shell syntax, failed-backend diagnostic smoke, healthy OpenClaw provider smoke, `openclaw status`, and active supervisor restart.

Immediate next step: adjudicate the private OpenClaw smoke candidate output, then consider staged Telegram-private integration with explicit stop conditions. Alternatively, run a multi-task or multi-persona supervisor smoke.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| OmegaClaw Core inspection clone | `https://github.com/asi-alliance/OmegaClaw-Core` | `projects/omegaclaw/repos/OmegaClaw-Core` | upstream default | inspect clone |
| PeTTa runtime checkout | `https://github.com/trueagi-io/PeTTa` | `projects/omegaclaw/repos/PeTTa` | upstream default | recorded by git in clone |
| OmegaClaw nested runtime checkout | `https://github.com/asi-alliance/OmegaClaw-Core` | `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core` | upstream default | recorded by git in clone |
| ChromaDB helper | `https://github.com/patham9/petta_lib_chromadb` | `projects/omegaclaw/repos/PeTTa/repos/petta_lib_chromadb` | upstream default | recorded by git in clone |

## Environments

- Local SWI-Prolog: `projects/omegaclaw/local/swipl-9.3.36`
- Python venv: `projects/omegaclaw/repos/PeTTa/.venv`
- Local Landlock policy: `projects/omegaclaw/local/policy.local.yaml`
- Local run wrapper: `projects/omegaclaw/local/run-omegaclaw-mock.sh`
- Local OpenClaw-backed smoke wrapper: `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh`
- Local OpenClaw-backed supervisor: `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh`
- Local private Telegram wrapper: `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`
- Local private Telegram supervisor: `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`
- Local Telegram token validator: `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh`
- Default local OmegaClaw Telegram secret env file: `/home/openclaw/.openclaw/omegaclaw-telegram.env`
- Local embedding cache: `projects/omegaclaw/local/huggingface`, `projects/omegaclaw/local/sentence_transformers`
- Chroma DB path: `projects/omegaclaw/repos/PeTTa/chroma_db`

See `projects/omegaclaw/RUNBOOK.md` for exact commands and environment variables.

## Key results

- PeTTa smoke result: `examples/fib.metta` reported `is 832040, should 832040. ✅`.
- SWI library import check passed for `janus`, `process`, `filesex`, `pcre`, and `uuid`.
- Python import check passed for `torch`, `chromadb`, `janus_swi`, `openai`, and `yaml`.
- OmegaClaw mock startup initialized policy, memory, local embeddings, knowledge bypass, mock channel, and loop iterations; wrapper verification passed with expected timeout.
- OpenClaw-backed OmegaClaw smoke initialized policy/local embeddings/mock channel, posted to `http://127.0.0.1:18789/v1/chat/completions`, received `200 OK`, and logged raw response `Understood — I won’t re-send or spam.` See `experiments/20260627T063559Z-openclaw-proxy-smoke/RUN.md`.
- Telegram-private scaffolding checks passed: Python syntax compile, shell syntax checks, allowlist unit check (`402314199` private allowed; group and other user ignored), start path refuses without a token, and token/env validator correctly exits `2` when no token is available.
- Token validation on 2026-06-27 succeeded for bot username `Protomegabot`; private Telegram supervisor initialized OmegaClaw with OpenClaw backend. End-to-end private Telegram smoke succeeded after fixing Landlock DNS resolver access and wrapping natural-language responses to `send` for fresh human messages. Benjamin reported receiving a reply in the `@Protomegabot` / ProtomegaTron chat. Supervisor was stopped after the smoke.

## Open questions

- For near-term local operation, OpenClaw proxy works as an LLM backend; before longer runs decide whether it should remain a full OpenClaw agent target or be replaced by a raw-model route.
- Preferred near-term topology is a separate OmegaClaw Telegram bot token/account for private/direct smoke. A token is currently stored only in the local secret env file, but because it was pasted into chat it should be rotated in BotFather before any longer run.
- How should OmegaClaw communicate with ZeroBot/OpenClaw: Telegram group, direct OpenClaw session bridge, local IPC, webhook, or no direct link initially?
- What filesystem/network policy should be used for real runs beyond the current local mock policy?

## Related projects and concepts

- `petta-chem`: separate PeTTa-native algorithmic chemistry project; overlaps in PeTTa/SWI runtime concerns but should remain distinct.
- PeTTa, MeTTa, SWI-Prolog Janus, ChromaDB, Telegram bot adapters.

## Risks

- **Credential exposure:** Telegram/API tokens must not be committed or placed in memory files.
- **Overbroad agency/channel permissions:** OmegaClaw should not be allowed to message groups or agents until auth boundaries are explicit.
- **Filesystem policy mismatch:** upstream Docker policy used `/PeTTa/...`; local path policy must be maintained if running outside Docker.
- **Infinite-loop behavior:** OmegaClaw is a continuous agent loop; run under explicit process/session management and stop smoke supervisors after tests.
- **Provider cost/unintended calls:** mock mode avoids real LLM calls; real provider use needs explicit credentials and monitoring. Current Telegram private mode still needs idle/no-input tuning before long-lived operation.
