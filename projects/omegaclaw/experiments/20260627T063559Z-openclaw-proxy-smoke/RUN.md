# Run 20260627T063559Z-openclaw-proxy-smoke: openclaw-proxy-smoke

- Project: `omegaclaw`
- Started: `2026-06-27T06:35:59Z`
- Finished: `2026-06-27T06:37:30Z`
- Status: `partial-success` — the OpenClaw provider call succeeded; the continuous OmegaClaw loop was intentionally stopped by timeout (`124`).
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent`

## Question

Can OmegaClaw use the local OpenClaw Gateway OpenAI-compatible `/v1/chat/completions` endpoint as its LLM provider while keeping Telegram/group integration disabled?

## Hypothesis or expected behavior

A local `OpenClaw` provider in `lib_llm_ext.py` plus a supervised wrapper should let OmegaClaw initialize with:

- mock communication channel;
- local Landlock policy;
- local `intfloat/e5-large-v2` embeddings;
- OpenClaw Gateway at `http://127.0.0.1:18789/v1`;
- model target `openclaw/default`;
- Gateway token read from local secret storage, not placed in project files.

Because OmegaClaw is a continuous loop, timeout exit `124` is acceptable if the OpenClaw HTTP call succeeds first.

## Inputs

- Git state: `git.txt` (workspace itself is not a git worktree; relevant repo commits below)
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: none set.
- PeTTa checkout commit at inspection time: `d8d46920269ced70cd6236a5182d4d2409c1e12b`.
- Nested OmegaClaw-Core checkout commit at inspection time: `16d380d9ff32675aa3f19bec7419229b99a7ae12` with local modification adding `OpenClawProvider`.

## Results

- Exit status: `124` from the intentional `timeout` boundary.
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

Observed evidence:

- Local policy loaded: `[FileSystemPolicy.load_file] policy applied`.
- Local embeddings selected and loaded: `Embedding type selected is Local`; stderr loaded `intfloat/e5-large-v2` on CPU.
- OmegaClaw configured `provider=OpenClaw` and `commchannel=mock`.
- OpenClaw provider connected to `http://127.0.0.1:18789/v1`.
- HTTP call succeeded: `HTTP Request: POST http://127.0.0.1:18789/v1/chat/completions "HTTP/1.1 200 OK"`.
- LLM raw log showed OpenClaw response: `provider=OpenClaw model=openclaw/default chars=37 raw='Understood — I won’t re-send or spam.'`.
- OmegaClaw parsed a response form: `(RESPONSE: ((Understood "— I won’t re-send or spam.")))`.

## Interpretation

Observed: the local OpenClaw Gateway path works as an OmegaClaw LLM backend for a bounded smoke run. Telegram was not involved, so Telegram can be added later as a separate communication layer.

Observed caveat: OmegaClaw continued printing idle iterations after `maxNewInputLoops=1`, so the wrapper still needs an external supervisor/timeout for safe short runs. This matches the known continuous-loop behavior.

Observed caveat: the model output was semantically benign but not an executable OmegaClaw skill call, so the run demonstrates provider connectivity and parsing behavior, not useful autonomous task execution.

Security note: Gateway token was read from `~/.openclaw/secrets.json` by the wrapper and was not written into this run record or command line.

## Reproduction

From `/home/openclaw/research-agent`:

```bash
projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh
```

The wrapper defaults to:

```bash
OPENCLAW_GATEWAY_BASE_URL=http://127.0.0.1:18789/v1
OPENCLAW_MODEL=openclaw/default
OPENCLAW_SESSION_USER=omegaclaw-local-smoke
OMEGACLAW_TIMEOUT=90
```

## Follow-up

- Keep the OpenClaw provider and wrapper as local integration scaffolding.
- Add a supervised launch/stop procedure before any longer OmegaClaw run.
- Review whether the OpenClaw backend should be a raw model route rather than a full OpenClaw agent target before allowing more capable OmegaClaw prompts.
- Add Telegram only after deciding token ownership and whether OmegaClaw talks directly to Telegram or through an OpenClaw/ZeroBot bridge.
