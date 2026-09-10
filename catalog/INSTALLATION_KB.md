# Installation and Functionality Knowledge Base

- Created: 2026-07-07
- Owner: Ben / ZeroBot
- Purpose: durable lookup record of what has been installed, configured, patched, or added to the OpenClaw/OmegaClaw proto-hive, and what each component does.
- Update rule: whenever software, a runtime service, a toolchain, a plugin, a skill, a cron job, or a major local patch is installed/changed, add or update an entry here and, when practical, in `catalog/install-kb/components.jsonl`.
- Query rule for ZeroBot: before answering questions like "is X installed?", "can you generate Y?", "what does tool Z do?", or "what changed about you/ProtoMegaBot?", consult this file, `catalog/SETUP_REPORT.md`, current config/status, and exact tool checks.

## Quick lookup commands

```bash
# Keyword search this KB
bin/install-kb-search latex
bin/install-kb-search ollama
bin/install-kb-search protomegabot

# Broader source search
rg -n "tectonic|pdflatex|ollama|qwen|ThreadKeeper|intent-model-router" catalog projects memory MEMORY.md
```

## Components

### OpenClaw main runtime

- Status: installed and active.
- Version observed 2026-07-07: `OpenClaw 2026.6.10 (aa69b12)`.
- Binary: `/home/openclaw/.npm-global/bin/openclaw`.
- Role: ZeroBot/ProtoCosmoBot runtime, Gateway, Telegram routing, tools, cron scheduler, sessions, memory/search, and OpenAI-compatible local proxy for OmegaClaw.
- Config: `/home/openclaw/.openclaw/openclaw.json`.
- Workspace: `/home/openclaw/research-agent`.
- Important docs/records: `catalog/SETUP_REPORT.md`, `MEMORY.md`, `AGENTS.md`, `TOOLS.md`.

### OpenClaw Gateway HTTP endpoints

- Status: enabled in config.
- Base URL: `http://127.0.0.1:18789`.
- Endpoints enabled: `/v1/chat/completions`, `/v1/responses`.
- Role: lets OmegaClaw and smoke harnesses call OpenClaw as an authenticated LLM backend.
- Restart note: config changes require restarting `openclaw-agent.service` on this system.
- Known exact restart command for Ben on Pop!_OS laptop:

```bash
sudo systemctl restart openclaw-agent.service
```

### Telegram channel integration

- Status: enabled.
- Role: ZeroBot direct chat with Ben, Protobots group participation, scheduled updates, and BotBotChats coordination.
- Rich messages: disabled for this bot/account; standard Telegram formatting available.
- Important channels:
  - Ben direct: `telegram:402314199`.
  - Scheduled updates: `telegram:-1003983157420`.
  - ProtoBots-BotBotChats: `telegram:-5459676079`.
- Config contains group-specific prompts and routing rules.

### Tectonic LaTeX compiler

- Status: installed and working.
- Version observed 2026-07-07: `Tectonic 0.16.9`.
- Binary: `/home/openclaw/.npm-global/bin/tectonic`.
- Role: compile `.tex` files to PDF when `pdflatex`/`xelatex`/`lualatex` are absent.
- Important correction: on 2026-07-07 ZeroBot initially said PDF compile was blocked because `pdflatex` was missing; this was incomplete. `tectonic` was installed and successfully compiled the requested LaTeX PDF.
- Example command:

```bash
tectonic catalog/proto_hive_functionality_inventory_20260707.tex --outdir catalog
```

- Verified artifact: `catalog/proto_hive_functionality_inventory_20260707.pdf`.

### PDF generation capability

- Status: available via Tectonic.
- Use: for ASCII LaTeX reports and generated papers/notes.
- Fallback if Tectonic fails and MacBook is available: install MacTeX or BasicTeX on macOS and use `pdflatex`/`latexmk` there; but on this Pop!_OS machine, Tectonic is currently the first local route.

### Ollama local LLM runtime

- Status: repaired and working as of 2026-07-07, pending OpenClaw Gateway restart for config pickup.
- Binary: `/home/openclaw/.local/bin/ollama`.
- Version observed: `ollama version is 0.31.1`.
- API: `http://127.0.0.1:11434`.
- Model installed: `qwen2.5:7b` (4.7 GB), id `845dbda0ea48`.
- Role: local LLM fallback for provider/billing/network failures.
- Problem fixed: `ollama` binary existed but `llama-server` and shared libraries were missing. Installed them from official Ollama v0.31.1 Linux amd64 release tarball into `/home/openclaw/.local/lib/ollama/`.
- Smoke test passed: `ollama run qwen2.5:7b` answered `2 + 2 equals 4`.
- OpenClaw config updated: added provider `ollama` with `baseUrl: http://127.0.0.1:11434` and model `ollama/qwen2.5:7b`; appended it after GLM in fallback list.
- Pending: restart OpenClaw Gateway/service for the running agent to pick up the config.

### Ollama keepalive cron

- Status: active.
- Job id: `b61b7f9a-4062-4d60-addc-71898e9ec239`.
- Schedule: every 5 minutes.
- Role: checks `http://localhost:11434/api/version`; starts `ollama serve > /tmp/ollama.log 2>&1 &` if Ollama is down; reports only repeated failure.
- Caveat: systemd user service could not be enabled from the agent environment because no user DBus/session bus was available; cron keepalive is the current lightweight workaround.

### OpenClaw intent-model-router plugin

- Status: installed locally and extracted to standalone repo.
- Local plugin path: `plugins/intent-model-router`.
- Repo: `projects/openclaw-intent-model-router/repos/openclaw-intent-model-router`.
- Head observed 2026-07-07: `a6c7171 Extract cost-aware OpenClaw intent router`.
- Role: cost/intent-aware model routing; routine work can use GLM, substantive/deep work uses GPT-5.5; OmegaClaw/ProtomegaTron sessions get special detection so complex PeTTa/OmegaClaw prompts avoid weak model misrouting.

### Agent recovery repositories

- Status: active.
- Project: `projects/agent-recovery`.
- Private repos:
  - `bgoertzel-sing/zerobot-recovery`.
  - `bgoertzel-sing/protomegabot-recovery`.
- Role: sanitized disaster recovery snapshots for ZeroBot/OpenClaw and ProtoMegaBot/OmegaClaw.
- Daily cron: `Daily agent recovery GitHub backup`, job id `5ae59dd5-dfe3-4ace-999d-a08ca153325e`, 03:30 America/Vancouver.
- Scripts:
  - `projects/agent-recovery/scripts/backup-zerobot-recovery.sh`
  - `projects/agent-recovery/scripts/backup-protomegabot-recovery.sh`
  - `projects/agent-recovery/scripts/push-recovery-repos.sh`

### Channel watchdog

- Status: active.
- Project: `projects/channel-watchdog`.
- Cron: `Channel watchdog scan`, job id `70cd9d3f-8ed4-4d86-8887-917eb919c6b9`, every 15 minutes.
- Role: scans Telegram bot conversations for dropped continuations, missing attachments, stock acknowledgements, runaway bot-bot chatter, and unsurfaced subagent completions.
- Alerts: scheduled-updates channel.

### ProtoMegaBot / OmegaClaw local runtime

- Status: installed and locally runnable; Telegram runtime supervised/watchdogged.
- Project: `projects/omegaclaw`.
- Important runtime paths:
  - `projects/omegaclaw/local/run-omegaclaw-mock.sh`
  - `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh`
  - `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`
  - `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`
  - `bin/omegaclaw-watchdog.sh`
- Role: PeTTa/OmegaClaw-based ProtoMegaBot / ProtomegaTron, using local SWI/PeTTa/ChromaDB/embedding runtime and OpenClaw as LLM backend.
- Major local additions: Telegram allowlist/private mode, attachment extraction/chunking, continuation protocol, backend diagnostics, per-call OpenClaw sessions, and supervisor hardening.

### OmegaClaw watchdog

- Status: active.
- Cron: `omegaclaw-watchdog`, job id `9df4641e-f89a-4dca-9ed3-d749cf6f075c`, every 10 minutes.
- Script: `bin/omegaclaw-watchdog.sh`.
- Role: checks ProtoMegaBot Telegram supervisor PID and restarts it if down.

### Local SWI-Prolog for OmegaClaw

- Status: installed under project local path.
- Path: `projects/omegaclaw/local/swipl-9.3.36`.
- Role: required by PeTTa/OmegaClaw stack because distro SWI candidate was too old.
- Required libraries built: Janus, process, filesex, pcre, uuid.

### PeTTa / OmegaClaw / ChromaDB stack

- Status: installed under `projects/omegaclaw/repos/`.
- Repos include: OmegaClaw-Core, PeTTa, nested OmegaClaw-Core runtime tree, `petta_lib_chromadb`, ThreadKeeper, OmegaClaw-GoalChainer.
- Role: symbolic/MeTTa/OmegaClaw runtime, local embeddings, memory/ChromaDB, subagent delegation, GoalChainer experiments.

### ThreadKeeper subagent system

- Status: active development/hardening.
- Repo: `projects/omegaclaw/repos/ThreadKeeper`.
- Branch/head observed 2026-07-07: `agent/threadkeeper-hardening-next`, `52a9bc9 Require string final emits`.
- Role: OmegaClaw-side subagent, queued task, worker, and audit infrastructure.
- Important functions added/hardened: typed tool args/final emits, bounded raw responses, bounded transcript fields/summaries, audit/index read caps, queue metadata, shell workspace cwd, output caps, non-finite env rejection, hash-chain index rotation.

### GoalChainer / deontic/directive runtime

- Status: non-live integration and gates active.
- Paths: `projects/omegaclaw/repos/OmegaClaw-GoalChainer`, OmegaClaw-Core skill surface, petta-memory bridge artifacts.
- Role: norm/goal/task decision layer using deontic/directive runtime and heuristic PLN-style belief grading.
- Important boundary: used through non-live smoke/gate artifacts before any live Telegram/OmegaClaw/ZeroBot bridge changes.

### QMD / semantic memory search

- Status: was installed/indexed in initial setup report; current PATH check on 2026-07-07 returned missing, so exact executable path should be rechecked before relying on CLI.
- Role: local semantic search layer for memory/projects/library/catalog.
- Source: `catalog/SETUP_REPORT.md` records qmd 2.5.3 and indexed collections during initial setup.
- Current OpenClaw `memory_search` remains available through agent tools.

### Rust / rustup toolchain

- Status: installed and working (2026-07-13).
- rustup: `~/.cargo/bin/rustup`, version 1.29.0.
- Default toolchain: `nightly-x86_64-unknown-linux-gnu`, rustc 1.99.0-nightly (77cf889bc 2026-07-12), cargo 1.99.0-nightly.
- PATH: `~/.cargo/bin` added to `.bashrc` and `.profile` via `~/.cargo/env`.
- Role: required by MORK (edition 2024, nightly features) and PathMap (edition 2024, nightly features). MORK release build verified, `mork test` smoke passes.
- Installed via official `https://sh.rustup.rs` installer with `--default-toolchain nightly --profile default`.

### Core CLI/tooling prerequisites

Observed installed tools 2026-07-07:

```text
git: /usr/bin/git, version 2.34.1
gh: /usr/bin/gh, version 2.4.0+dfsg1
python3: /usr/bin/python3, version 3.10.12
node: /usr/bin/node, v24.18.0
npm: /usr/bin/npm, 11.16.0
jq: /usr/bin/jq, 1.6
rg: /usr/bin/rg, 13.0.0
cmake: /usr/bin/cmake, 3.22.1
gcc: /usr/bin/gcc, 11.4.0
shellcheck: /usr/bin/shellcheck
tmux: /usr/bin/tmux
```

Observed missing from current PATH 2026-07-07:

```text
pdflatex, xelatex, lualatex, latexmk, typst, pandoc, fd, qmd
```

Note: `fdfind` may exist even if `fd` does not; check before concluding absent.

## Maintenance checklist

When installing or changing something:

1. Add or update the Markdown component entry above.
2. Add or update a compact JSONL entry in `catalog/install-kb/components.jsonl` when useful.
3. Add a daily memory note if the change is operationally important.
4. If the component affects recovery, ensure `projects/agent-recovery` snapshots will include enough restore instructions but no secrets.
5. If it affects running OpenClaw config, record whether a Gateway/service restart is required.
