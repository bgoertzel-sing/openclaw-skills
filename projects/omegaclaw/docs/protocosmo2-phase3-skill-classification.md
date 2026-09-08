# ProtoCosmo2 Phase 3 skill classification

- Date: 2026-08-03
- Scope: every `skills/*/SKILL.md` package in the ZeroBot workspace (19 total)
- Target baseline: isolated ProtoCosmo2 OmegaClaw tree

OmegaClaw skills are prompt-catalog entries plus MeTTa definitions, optionally
bridged to Python or Prolog; it does not load OpenClaw `SKILL.md` packages as
executables (`protocosmo2/OmegaClaw-Core/docs/tutorial-03-writing-a-custom-skill.md`).
Here, **portable-unchanged** means the behavioral prose can be embedded without
semantic changes, not that its package format loads unchanged.

| Skill | Class | One-line justification |
|---|---|---|
| `cross-agent-kanban` | deferred | Requires cron and session/subagent enumeration, neither present in the catalogued OmegaClaw surface (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `daily-bot-bot-project-discussions` | deferred | Requires scheduled jobs, named-channel routing, and safe bot-to-bot exchange; OmegaClaw exposes only the active channel's `send` (`protocosmo2/OmegaClaw-Core/src/channels.metta`). |
| `experiment-ledger` | portable-with-adapter | Ledger discipline is valid, but helper scripts, tmux, and durable writes must be mediated through bounded shell/file operations (`protocosmo2/OmegaClaw-Core/docs/reference-skills-io.md`). |
| `follow-through-contract` | portable-with-adapter | The policy is valid, but durable obligation reload/closure needs file conventions because `pin` is rolling history only (`protocosmo2/OmegaClaw-Core/docs/reference-skills-memory.md`). |
| `google-drive` | deferred | No Drive/OAuth skill exists in the catalogued surface; shell/network/package/credential availability is `[unverified]` (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `hyperon-workbench` | portable-with-adapter | MeTTa and shell primitives cover minimal local work, subject to the five-second shell limit and filesystem policy (`protocosmo2/OmegaClaw-Core/src/skills.metta`; `protocosmo2/OmegaClaw-Core/src/skills.pl`). |
| `kanban-task-board` | portable-with-adapter | File-backed boards are possible, but cron/session/job discovery has no OmegaClaw equivalent (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `knowledge-curation` | portable-with-adapter | File placement rules port, while semantic recall uses non-deduplicating embedding memory and needs provenance wrappers (`protocosmo2/OmegaClaw-Core/docs/reference-skills-memory.md`). |
| `persistent-subagent-orchestration` | portable-with-adapter | Adapter commit `5c64918` adds bounded durable task/event state, status/pause/resume/cancel/checkpoint controls, and read-only standing-approval adjudication. V1 records orchestration only and intentionally does not spawn, schedule, execute, or consume authority (`docs/protocosmo2-persistent-worker-adapter-v1.md`). |
| `plain-spec-governor` | reference-only | Plain templates and review criteria remain useful, but its mandatory persistent `PlainSpecReviewer` cannot execute on the observed generic skill surface (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `playwright` | deferred | No browser or screenshot skill is catalogued; Python package/browser installation and policy access are `[unverified]` (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `recurring-project-progress-worker` | deferred | Depends on OpenClaw cron, isolated agent turns, run history, and routed updates; only periodic wake-loop parameters are observed (`protocosmo2/OmegaClaw-Core/docs/reference-configuration.md`). |
| `remote-compute-guardrails` | portable-unchanged | The zero-spend approval policy is behavioral and remains enforceable by refusing execution; shell existence does not grant spend authority (`protocosmo2/OmegaClaw-Core/docs/reference-skills-io.md`). |
| `repository-operations` | portable-with-adapter | Git can be invoked through shell, but `gh`, authentication, long commands, and remote-write confirmation support are `[unverified]` (`protocosmo2/OmegaClaw-Core/src/skills.pl`). |
| `research-library` | portable-with-adapter | Sidecar/provenance discipline ports, while QMD, PDF/image inspection, hashing tools, and web preservation require verified shell adapters (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `research-projects` | portable-with-adapter | File-backed project records port, but workspace paths, helper commands, Git state, and memory indexing need instance-specific adapters (`protocosmo2/OmegaClaw-Core/docs/reference-skills-io.md`). |
| `research-rules-checklist` | portable-unchanged | It is epistemic prompt guidance and needs only file reading, which OmegaClaw supports (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `subagent-execution-contract` | reference-only | Its evidence/status vocabulary is useful, but dispatch and parent verification assume a generic subagent API not present in `getSkills` (`protocosmo2/OmegaClaw-Core/src/skills.metta`). |
| `telegram-channel-registry` | deferred | The target supports one active/bound Telegram chat, not named multi-channel lookup/send/sync (`protocosmo2/OmegaClaw-Core/channels/telegram.py`; `protocosmo2/OmegaClaw-Core/src/channels.metta`). |

## Counts and baseline rule

- portable-unchanged: 2
- portable-with-adapter: 9
- reference-only: 2
- deferred: 6
- total: 19

Nothing in this matrix authorizes installing dependencies, enabling a provider,
starting Telegram, enabling wake loops, dispatching a remote agent, or writing
long-term memory. Each adapter needs a provider-free positive test and a
refusal/boundary test before activation.
