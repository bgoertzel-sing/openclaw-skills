# OpenClaw + OmegaClaw Two-Agent Replication Kit

A sanitized, operator-driven recipe for reproducing the **working pattern** of a persistent OpenClaw research agent plus an OmegaClaw/PeTTa sibling agent, including:

- research-oriented prompts, project/memory/library stores, skills, and templates;
- Telegram Bot API 10 bot-to-bot discussion through a dedicated group;
- a patched OmegaClaw Bot API polling path with self/loop guards and delivery logging;
- project launch rules, experiment ledgers, Kanban, health checks, backups, daily discussions, and frontier-model expert reviews;
- optional Hyperseed-oriented conceptual work;
- conservative permissions, local-first execution, and zero autonomous paid-compute budget.

It intentionally contains **no credentials, personal memory, private chat/session state, cloned research repositories, project data, model caches, databases, or real Telegram IDs**. Public dependencies are fetched from pinned repositories/versions.

## Tested reference

- OpenClaw `2026.6.10`
- Node `24.18.0` (OpenClaw supports Node 22.19+ at this release)
- Python `3.10.12`
- Git `2.34.1`
- SWI-Prolog `9.3.36`
- Linux x86-64 (Pop!_OS/Ubuntu family)
- OmegaClaw base `16d380d9ff32675aa3f19bec7419229b99a7ae12` plus `patches/omegaclaw/omega-runtime-botapi10.patch`
- PeTTa `4ce1d0ea58855abb772b911278312c8846e5cc08`

OpenClaw itself supports macOS. This exact native OmegaClaw dependency set is Linux-tested; on macOS use a Linux VM/container unless you independently resolve/test `py-landlock`, SWI/Janus, and Torch compatibility.

## Quick start

Read the numbered documents first; do not run scripts blindly.

1. `docs/00-architecture-and-threat-model.md`
2. `docs/01-prerequisites.md`
3. Create two Telegram bots and three groups/channels as described in `docs/02-telegram-bot-api-10.md`.
4. Install OpenClaw and bootstrap the workspace:

```bash
npm install -g openclaw@2026.6.10
openclaw onboard --install-daemon
OWNER_NAME='Your Name' OWNER_SHORT_NAME='Your Name' \
  OPENCLAW_AGENT_NAME='YourOpenClawBot' OMEGACLAW_AGENT_NAME='YourOmegaBot' \
  TIMEZONE='America/New_York' ./scripts/bootstrap-workspace.sh
```

5. Customize `templates/openclaw-config/openclaw.example.json5`, **merge** it into the generated config (do not overwrite unknown working settings), configure SecretRefs, then:

```bash
openclaw config validate
openclaw secrets audit
openclaw gateway status
openclaw channels status --probe
```

6. Install OmegaClaw on the Linux host:

```bash
./scripts/install-omegaclaw.sh
```

Customize the copied prompt, create `~/.openclaw/omegaclaw-telegram.env` from the example with mode `0600`, expose a protected `OPENCLAW_GATEWAY_TOKEN` to the runner, and start:

```bash
~/research-agent/projects/omegaclaw/local/omegaclaw-supervisor.sh start
```

7. Run offline verification, then the live canaries in `docs/07-validation-and-troubleshooting.md`.
8. Only after canaries pass, install schedules:

```bash
BOT_DISCUSSION_CHAT_ID='-100...' SCHEDULED_UPDATES_CHAT_ID='-100...' \
HUMAN_SUMMARY_CHAT_ID='-100...' OMEGA_BOT_USERNAME='YourOmegaBot' \
LOCAL_TIMEZONE='America/New_York' ROUTINE_MODEL='your/routine-model' \
EXPERT_MODEL='your/frontier-review-model' ./scripts/install-schedules.sh
```

## Critical operational invariant

Exactly one OmegaClaw worker and exactly one Bot API `getUpdates` consumer may own the Omega bot token. The expected topology is:

```text
OpenClaw bot: Telegram long poll → OpenClaw agent
Omega bot:    Telegram long poll → OmegaClaw/PeTTa → local OpenClaw Gateway model endpoint
MTProto bridges: 0
```

Bot-generated `(send ...)` text is not delivery evidence. Require a successful Telegram `sendMessage` log/result and a visible message in the intended chat.

## What to customize

Search the extracted kit for `<...>` placeholders. At minimum set owner/agent names, model routes, timezone, Telegram user/chat IDs, bot usernames, public writing URL (or disable that background task), repository policy, and backup destination. Review every prompt as executable policy.

## Licenses and provenance

This kit's original glue/docs are supplied under MIT (`LICENSE`). Copied skills/plugins and fetched upstream projects retain their own notices/licenses. See `THIRD_PARTY.md` and `MANIFEST.sha256`.
