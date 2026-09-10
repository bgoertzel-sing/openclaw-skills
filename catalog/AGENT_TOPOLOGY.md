# Agent and System Topology

Last updated: 2026-07-12

This is a durable reference for the identity, location, processes, and
relationships of all agents and key software entities on the Pop!_OS
research workstation. Update when topology changes.

## Host

- **Machine:** Pop!_OS laptop (hostname `pop-os`, 192.168.1.83)
- **OS:** Linux 7.0.11-76070011-generic (x64)
- **Primary user:** openclaw
- **Workspace:** `/home/openclaw/research-agent`

## Agents

### ZeroBot / ProtoCosmoBot

- **Real identity:** OpenClaw agent `main` on this host.
- **Telegram handle:** `@Protocosmobot` (also called ZeroBot in some contexts).
- **Runtime:** OpenClaw Gateway, systemd user service (pid tracked by systemd).
  - Gateway: `ws://127.0.0.1:18789`, local loopback.
  - Config: `~/.openclaw/agents/main/`.
  - Default model: `openai/gpt-5.6-terra` (200k ctx).
  - Heartbeat: 1h.
- **Role:** Ben's persistent research prototyping collaborator. Manages all
  projects under `~/research-agent/projects/`, runs experiments, maintains
  memory, and participates in Telegram group chats.
- **Source:** OpenClaw (`~/.npm-global/lib/node_modules/openclaw`).
- **Disaster recovery:** private GitHub repo `bgoertzel-sing/zerobot-recovery`,
  daily backup cron at 03:30 America/Vancouver.

### ProtoMegaBot / ProtomegaTron

- **Real identity:** OmegaClaw agent running locally on the same Pop!_OS host.
- **Telegram handle:** `@Protomegabot`.
- **Runtime:** Supervised OmegaClaw process (SWI-Prolog-based), NOT an OpenClaw
  agent. Runs under a bash supervisor script that auto-restarts on exit.
  - Supervisor script: `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`
  - Runner: `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`
  - OmegaClaw source: `projects/omegaclaw/repos/PeTTa/`
  - SWI-Prolog process with `run.metta` entry point.
  - Provider: OpenClaw (chat completions through the local Gateway).
  - PID state file: `projects/omegaclaw/local/run-state/omegaclaw-telegram-private.pid`
  - Logs: `projects/omegaclaw/artifacts/telegram-private-supervisor/`
  - Env file (secrets): `~/.openclaw/omegaclaw-telegram.env` (0600, not committed).
- **Current binding:** Multi-chat mode (`TG_PRIVATE_ONLY=false`). Listening
  on Ben's private chat (`402314199`) and all known group chats:
  `protobot-updates` (`-1003983157420`), `ProtoBots-BotBotChats`
  (`-5459676079`), and the main Protobots group (`-5437945421`).
- **Role:** Hyperseed-extension research agent; formalization, continual
  thinking, and Telegram interaction. Maintained by ZeroBot/OpenClaw.
- **Prompt:** `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/memory/prompt_OpenClaw.txt`
- **Disaster recovery:** private GitHub repo `bgoertzel-sing/protomegabot-recovery`,
  daily backup cron at 03:30 America/Vancouver.

### @zariuq

- **External human collaborator** (not a bot). Referenced in Protobots
  group context. Math-formalization discussions typically go 1:1 with Zar
  or in a dedicated channel.

### @Oruzibot

- **External bot** in the Protobots ecosystem. ZeroBot may interact with it
  directly when useful, but keep bot-bot back-and-forth selective.

## Key Software Entities

### OpenClaw Gateway

- **Process:** systemd user service, pid 1020731 on host `pop-os`.
- **Listen:** `ws://127.0.0.1:18789` (local loopback only).
- **Config:** `~/.openclaw/agents/main/agent.yaml` and related.
- **Role:** Manages ZeroBot's agent sessions, tool routing, Telegram channel,
  memory, cron, and model routing. Also acts as the LLM provider backend for
  OmegaClaw/ProtomegaTron.

### OmegaClaw

- **Source:** `projects/omegaclaw/repos/PeTTa/` (MeTTa-based agent framework
  running on SWI-Prolog).
- **Role:** ProtomegaTron's runtime. Uses OpenClaw Gateway as its
  chat-completion provider. Has its own Telegram adapter
  (`channels/telegram.py`) and loop logic (`src/loop.metta`).
- **Key subsystems:** GoalChainer, ThreadKeeper, petta-memory integration
  (read-only handoff packets by default).

### PeTTa / petta-memory

- **Repo:** `projects/petta-memory/repos/petta-memory`
- **Role:** PLN-based inference and memory layer for OmegaClaw. ZeroBot
  implements wrapper-only inference-control mechanisms (context selection,
  probabilistic filtering, chained pipeline) without touching the live
  OmegaClaw path.

## Telegram Channels

| Channel | Chat ID | Purpose |
|---------|---------|---------|
| Protobots main group | (Ben's main group) | General Protobots discussion |
| Protobot-updates | `telegram:-1003983157420` | Scheduled updates and progress |
| ProtoBots-BotBotChats | `telegram:-5459676079` | Bot-bot project discussions |

## Relationships

```
Ben (402314199)
├── ZeroBot / @Protocosmobot (OpenClaw agent main)
│   ├── Manages all research projects
│   ├── Maintains ProtoMegaBot/OmegaClaw
│   ├── Daily recovery backups to GitHub
│   └── Participates in Telegram groups
├── ProtoMegaBot / @Protomegabot (OmegaClaw on same host)
│   ├── Uses OpenClaw Gateway as LLM provider
│   ├── Currently bound to Ben's private chat only
│   ├── Prompt and runtime maintained by ZeroBot
│   └── Recovery backup to GitHub
└── External collaborators: @zariuq, @Oruzibot
```

## Maintenance Notes

- ZeroBot is responsible for starting, stopping, and reconfiguring
  ProtoMegaBot/OmegaClaw.
- The OmegaClaw supervisor auto-restarts the runner on exit with a 5-second
  delay.
- ProtoMegaBot's Telegram binding needs explicit reconfiguration to join
  group chats (currently private-chat-only).
- Token rotation for @Protomegabot was deferred per Ben's instruction
  (2026-06-27); treat as recommended hygiene, not a blocker.
