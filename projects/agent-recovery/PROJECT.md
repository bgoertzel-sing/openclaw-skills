# Agent Disaster Recovery Repositories

- Slug: `agent-recovery`
- Status: `active`
- Created: `2026-06-28`
- Owner: Benjamin Goertzel

## Purpose

Create private GitHub-backed disaster-recovery repositories for reconstructing Benjamin's OpenClaw-based agents on another machine if the local laptop fails.

This project covers two separate recovery targets:

1. `zerobot-recovery`: ZeroBot / OpenClaw research-agent context, curated memory, project notebooks, and restoration instructions.
2. `protomegabot-recovery`: Protomegabot / OmegaClaw / ProtomegaTron operational context, safe runtime notes, non-secret local patches/manifests, and restoration instructions.

## Success criteria

- Private GitHub repositories exist for each recovery target, with Benjamin-confirmed owner/name/visibility.
- Each repository has a clear `README.md`, `RESTORE.md`, `MANIFEST.md`, `.gitignore`, and backup script.
- Daily automated updates run locally and push sanitized changes.
- Secrets, tokens, SSH keys, provider credentials, local OpenClaw state, and bulky/generated runtime artifacts are excluded.
- Restoration instructions are sufficient to rebuild a functional agent context on a new machine, subject to separately re-entering credentials.

## Scope

### In scope

- Curated prompt/persona/context files.
- Durable memory files and project notebooks.
- Non-secret runbooks, wrappers, manifests, and patches needed to reconstruct local behavior.
- Secret-exclusion policy and lightweight secret scanning before commit.
- Daily scheduling after repository creation.

### Out of scope unless explicitly approved

- Storing `~/.openclaw` state, provider tokens, Telegram bot tokens, SSH keys, or recovery codes.
- Public repositories.
- Full raw chat/session logs unless separately curated and sanitized.
- Large cloned repositories under `projects/*/repos/`.
- Large experiment artifacts or model caches.
- Running paid compute or changing provider resources.

## Current state

- Local planning scaffold created on 2026-06-28 under `projects/agent-recovery/`.
- GitHub CLI is authenticated as `bgoertzel-sing`.
- `/home/openclaw/research-agent` itself is not currently a Git repository.
- Private recovery repositories exist and are active:
  - `bgoertzel-sing/zerobot-recovery`
  - `bgoertzel-sing/protomegabot-recovery`
- Daily OpenClaw cron job `Daily agent recovery GitHub backup` (`5ae59dd5-dfe3-4ace-999d-a08ca153325e`) runs at 03:30 America/Vancouver with no success announcement and failure alerts to the scheduled-updates channel.
- 2026-07-07 repair: tightened the backup secret scanner so hyphenated internal IDs such as `sk-board-...` no longer false-positive as OpenAI-style keys, added venv exclusion/deletion for Protomegabot local snapshots, added fetch/rebase-before-push handling, and successfully pushed fresh snapshots (`zerobot-recovery` `2ef932d`, `protomegabot-recovery` `25c8b3c`).
- 2026-07-15 scheduler repair: the backup script and synchronization were healthy,
  but the isolated cron was marked failed when its agent produced no final
  response after tool success. The job now pins a valid model and must return
  `NO_REPLY` after exact clean/divergence checks. A forced run completed `ok`.

## Repository names

| Recovery target | Repo | Visibility | Notes |
|---|---|---|---|
| ZeroBot/OpenClaw | `bgoertzel-sing/zerobot-recovery` | private | Main OpenClaw research-agent recovery context. |
| Protomegabot/OmegaClaw | `bgoertzel-sing/protomegabot-recovery` | private | Separate bot/runtime recovery; excludes bot token and provider credentials. |

## Risks

- **Credential leakage:** never commit tokens, keys, `.env` files, `~/.openclaw`, credential helper files, or command output containing secrets.
- **Over-broad backup:** backing up raw repos/caches/artifacts can leak private data or create huge repositories.
- **Stale restoration instructions:** daily backups should preserve context but restore docs must be periodically smoke-checked.
- **Identity conflation:** ZeroBot and Protomegabot should remain separate recovery targets with separate manifests.
