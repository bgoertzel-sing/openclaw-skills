# 04 — OmegaClaw installation and runtime

## Public sources and patch

`install-omegaclaw.sh` fetches:

- PeTTa fork commit `4ce1d0e...` (includes runtime fixes used by the reference setup)
- OmegaClaw upstream base `16d380d...`
- `petta_lib_chromadb`

It applies `patches/omegaclaw/omega-runtime-botapi10.patch`, a sanitized diff from the pinned OmegaClaw base to the tested local runtime. The patch includes Telegram routing/mention fixes, per-message envelopes, send-result/deduplication changes, health/event instrumentation, Bot API polling, and bot-loop guards. Historical MTProto diagnostic code may remain in the patch/test history, but **the live recipe disables MTProto and does not start its bridge**.

Review the patch before applying. The installer refuses if it cannot apply cleanly. It creates a dedicated venv and installs pinned OmegaClaw requirements. Dependency downloads are large.

## Prompt and stores

Customize `memory/prompt_OpenClaw.txt` after installation. It preserves the two-agent relationship, provenance/uncertainty requirements, bounded communication, optional Hyperseed work, and strict approval boundaries. Replace all `<...>` placeholders. Disable the public-writing background task if not wanted.

OmegaClaw creates its own stores under the PeTTa/Omega directories, including Chroma/vector data and MeTTa history/episodes. These are recipient-specific runtime state. Back them up separately only after deciding what private model/chat content they contain; never redistribute them as part of a setup kit.

## Gateway provider

The `OpenClaw` provider targets the local Gateway endpoint. Required runtime values:

- `OPENCLAW_GATEWAY_BASE_URL=http://127.0.0.1:18789/v1`
- `OPENCLAW_GATEWAY_TOKEN` from protected runtime configuration
- `OPENCLAW_MODEL=openclaw/default`
- `OPENCLAW_SESSION_PER_CALL=true`

The token must never be placed in Git, a prompt, cron payload, command argument, or shared archive.

## Start and inspect

```bash
chmod 600 ~/.openclaw/omegaclaw-telegram.env
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh start
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh status
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh health
```

Expected topology: `workers=1 mtproto_bridges=0`. If another poller is using the token, stop and identify it; do not add another bridge or worker.

## Service persistence

First validate manually. Then create a user-level service appropriate to the OS (for Linux, a systemd **user** unit) whose `ExecStart` calls the runner and whose protected environment supplies secrets. Do not put secrets directly in a world-readable unit. Use one restart policy with bounded backoff; do not stack systemd, cron, and multiple shell supervisors all restarting the same process.

The included 10-minute watchdog is optional. If systemd already provides monitored bounded restart, disable the redundant restart action and retain only health alerting.
