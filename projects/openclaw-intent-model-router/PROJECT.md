# OpenClaw Intent Model Router

- Slug: `openclaw-intent-model-router`
- Status: `active`
- Created: `2026-07-04`
- Owner: Benjamin Goertzel

## Purpose

Package the local OpenClaw `intent-model-router` plugin as a reusable GitHub repository for cost-aware routing across Claw agents: cheap routine model, default/deep model for substantive work, optional Claude Fable escalation, and fail-closed per-day Fable budget accounting.

## Success criteria

- Standalone repository contains the router code, tests, plugin metadata, and practical usage/security docs.
- No secrets, usage ledgers, local OpenClaw config, or private runtime state are included.
- Tests and syntax checks pass from the standalone repository.
- Public GitHub repository is available for other Claw agents after Ben's repo-name/visibility approval.

## Scope

### In scope

- OpenClaw plugin code from `plugins/intent-model-router/`.
- Cost-accounting and budget-override docs.
- Test coverage for routing, budget, override, and schema behavior.
- Project record links back to OmegaClaw, where the plugin originated.

### Out of scope

- Provider API keys or Anthropic/Fable credentials.
- Gateway restart or live provider calls.
- OpenClaw core changes.
- npm package publication.

## Current state

Initial standalone repository prepared under `projects/openclaw-intent-model-router/repos/openclaw-intent-model-router` from the local enabled plugin. The package includes README, USAGE, SECURITY, plugin metadata, router source, tests, and Plain/spec review artifacts.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Public reusable router repo | `https://github.com/bgoertzel-sing/openclaw-intent-model-router` | `projects/openclaw-intent-model-router/repos/openclaw-intent-model-router` | `main` | initial extracted plugin commit |
| Originating local plugin | local only | `plugins/intent-model-router` | n/a | 2026-07-04 daily-budget implementation |

## Related projects

- `omegaclaw`: originating deployment need for ProtomegaTron/OmegaClaw routing and Fable budget control.
- `agent-recovery`: separate backup/recovery concern; this repository is a reusable plugin, not an agent recovery bundle.

## Risks

- **Soft budget guard:** local ledger accounting can lag final provider billing and is not a substitute for provider billing limits.
- **Classifier overreach:** `auto` Fable mode may route more aggressively than desired; default is fail-closed/off.
- **Version drift:** OpenClaw plugin API/model refs may change; docs should record tested OpenClaw versions.
- **Licensing:** no permissive license has been selected yet, so public reuse remains legally limited until Ben chooses one.
