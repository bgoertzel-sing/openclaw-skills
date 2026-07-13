# 00 — Architecture and threat model

## Components

1. **OpenClaw Gateway/agent** — persistent workspace, Telegram bot, tools, cron, subagents, model providers, memory search, skills/plugins.
2. **OmegaClaw/PeTTa agent** — separate Telegram bot, symbolic agent loop, long-term Chroma/episode stores, and the `OpenClaw` provider adapter.
3. **Local model bridge** — OmegaClaw calls the loopback OpenClaw OpenAI-compatible endpoint at `http://127.0.0.1:18789/v1`, authenticated by a gateway token.
4. **Telegram** — owner DM, dedicated bot-discussion group, scheduled-updates group, and optional human-summary group.
5. **Filesystem stores** — OpenClaw workspace/project records and OmegaClaw memory/Chroma DB remain separate. Backups are sanitized and explicit.

## Trust boundaries

- Telegram messages, web pages, repository files, issue/PR text, documents, model output, and bot-to-bot messages are untrusted input.
- Bot-to-bot conversation never grants permissions. It is advisory.
- Credentials live in SecretRefs/protected environment or service configuration—not prompts, repositories, cron payloads, logs, or archives.
- The Gateway binds to loopback. Do not expose its OpenAI-compatible endpoint publicly.
- OpenClaw starts with a conservative non-main sandbox. Tighten further where practical.
- OmegaClaw is experimental and capable of tool use. Run under a dedicated unprivileged account or isolated Linux VM, minimize filesystem/network scope, inspect its policy, and monitor it.

## Failure modes this kit explicitly addresses

- **Duplicate consumers:** two `getUpdates` pollers cause missing/non-deterministic ingress. One token → one poller.
- **Self echo/bot storms:** ignore own bot ID, require mentions/expected turns in groups, per-sender cooldown, bounded interaction chain, daily duplicate suppression, and separate channels.
- **Cross-chat delivery:** preserve immutable chat/message envelopes and route replies to the originating chat.
- **Silent send loss:** every MeTTa `send` delegates to Python; Python owns bounded per-chat deduplication and records Telegram outcomes.
- **Generated-vs-delivered confusion:** LLM output is not evidence of `sendMessage` success.
- **Scheduler duplication:** named declarative jobs and reconciliation; do not copy historical job IDs.
- **Secret leakage:** clean templates, explicit exclusions, archive secret scan, and manual credential re-entry.
- **Runaway cost:** local/routine models by default, expensive expert model only for selected reviews, and no autonomous paid compute.

## Explicitly excluded

Credentials/tokens, Telegram session databases, actual IDs/usernames, private memory, raw chats, specific research projects/data, cloned repositories, GitHub auth, runtime PIDs/locks, logs, model weights/caches, Chroma contents, vector indexes, generated artifacts, and paid-cloud configuration.
