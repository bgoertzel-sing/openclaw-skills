# OpenClaw + OmegaClaw Replication Kit

- Slug: `openclaw-omegaclaw-replication-kit`
- Status: ready-for-fresh-host-test
- Created: `2026-07-13`
- Last reviewed: `2026-07-13`
- Owner: Benjamin Goertzel

## Purpose

Produce a sanitized, portable bundle that lets trusted colleagues reproduce the two-agent OpenClaw + OmegaClaw/ProtoMegaBot operating pattern on their own Linux/macOS machine and Telegram groups, while substituting their own identity, projects, credentials, model providers, and chat IDs.

## Success criteria

- A ZIP archive contains a concrete installation/configuration recipe and all non-public support files needed for the workflow.
- It covers OpenClaw, OmegaClaw, Telegram Bot API 10 bot-to-bot mode, prompts, reusable skills, memory/project records, Kanban, scheduled project discussions, health/recovery checks, experiment discipline, and optional frontier-model expert review.
- Public dependencies are fetched by documented pinned commands rather than copied unnecessarily.
- No credentials, private chat/session data, Ben-specific project content, machine identifiers, or secret-bearing state are included.
- Bundle scripts pass shell/Python syntax checks; internal links and expected files validate; a secret-pattern scan and archive inspection pass.

## Scope

### In scope

- Parameterized workspace/context templates preserving the current research-engineering operating style.
- Reusable local skills, project templates, helper scripts, scheduler job templates, and sanitized configuration examples.
- OmegaClaw patch series and prompt templates required to reproduce the current Bot API polling and OpenClaw-backed runtime behavior.
- Setup, verification, security, backup, customization, and troubleshooting documentation.

### Out of scope for now

- Ben's actual research repositories, memories, chats, credentials, Telegram IDs, provider tokens, model caches, databases, and generated artifacts.
- Paid compute provisioning or automatic provider-account configuration.
- Redistribution of public dependencies when a pinned download/clone procedure is sufficient.
- Fully unattended cross-platform installation; the first release targets a reviewable, operator-driven Linux/macOS setup.

## Current state

Version 1.0.0 was assembled and validated on 2026-07-13. The downloadable ZIP and SHA-256 sidecar are under `artifacts/`. The live two-bot Telegram loop was validated using Bot API 10 bot-to-bot mode, plain Bot API polling for OmegaClaw, and explicit loop-prevention safeguards. Remaining acceptance work is a fresh-host deployment with newly issued credentials/IDs.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| OpenClaw | https://github.com/openclaw/openclaw | installed package/docs | stable/latest | record at packaging time |
| PeTTa | https://github.com/trueagi-io/PeTTa | `projects/omegaclaw/repos/PeTTa` | local checkout | record in bundle manifest |
| OmegaClaw-Core | https://github.com/asi-alliance/OmegaClaw-Core | `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core` | `agent/telegram-runtime-mods-checkpoint` | record in bundle manifest + patch series |

## Environments

The reference host is Linux with Node 24, Python, Git, SWI-Prolog/Janus, Telegram bots, and OpenClaw Gateway. Exact detected versions and source commits will be written to the bundle manifest.

## Key results

- 2026-07-13: genuine bot-originated Telegram discussions succeeded after enabling Bot-to-Bot Communication in the BotFather MiniApp for both bots and using Bot API polling.
- OmegaClaw runtime commits `361fd6a`, `4c6794c`, and `db192e5` fix silent outbound suppression, retire MTProto receive, and add bot-loop safeguards.
- 2026-07-13: built `artifacts/openclaw-omegaclaw-replication-kit-v1.0.0.zip` (SHA-256 `b68e06fa767d8f1042daa04ed391947948463de08ac33adcc7e86b17b7bad9c5`). Archive has 79 files, internal manifest verification passes, patch applies to the pinned OmegaClaw base, 29 targeted Omega runtime tests pass, and shell/Python/plugin/secret/archive checks pass.

## Open questions

- Fresh-host behavior across recipient Linux distributions and model providers.
- Whether to split the large OmegaClaw overlay into focused upstream PRs after the private kit is exercised.
- Whether to publish the kit as a public repository after Ben reviews the private ZIP.

## Related projects and concepts

- `omegaclaw`, `agent-recovery`, `openclaw-intent-model-router`, `research-agent-setup`
- Hyperseed formalization, cross-agent Kanban, experiment ledger, durable memory, cost-aware expert review

## Risks

- Secret/session leakage if live OpenClaw/OmegaClaw state is copied rather than templated.
- Stale upstream APIs or dependency versions.
- Telegram bot loops without rate/depth/mention controls.
- Model-cost surprises if optional expert reviews or autonomous workers are enabled without budgets.
- Licensing/provenance mistakes when packaging upstream code; prefer patches and fetch instructions.

## Research rules emphasized

Rules 2, 3, 5, and 7: specify behavior and invariants before implementation, reuse OpenClaw/OmegaClaw rather than rebuilding, make the recipe reproducible, and retain replaceable seams for Telegram, models, schedulers, and memory backends.
