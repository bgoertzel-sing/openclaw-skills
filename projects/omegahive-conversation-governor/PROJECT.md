# OmegaHive Conversation Governor

- Slug: `omegahive-conversation-governor`
- Status: `active`
- Created: `2026-07-24`
- Last reviewed: `2026-07-27`
- Owner: Benjamin Goertzel

## Purpose

Implement a shared conversation control plane for OpenClaw, OmegaClaw, and a
future OmegaHive. The governor should reduce unnecessary model invocations and
public bot-to-bot noise while preserving useful execution, review, disagreement,
and explicitly requested multi-agent responses.

## Success criteria

- Every phase has a preregistered replay or canary acceptance gate.
- Exact duplicates, own-message echoes, visible silence markers, routine
  unchanged updates, and parallel public answers can be prevented before model
  inference where deterministic evidence permits.
- One public response owner is selected by default, while bounded private
  review remains possible.
- False-silence and duplicate-response rates are measured against a
  transcript-derived replay corpus before activation.
- Live behavior changes occur only behind feature flags after shadow evidence
  and explicit approval.

## Scope

### In scope

- Event/provenance envelope and durable decision ledger.
- Transcript-derived replay corpus with privacy-preserving fixtures.
- Shadow admission decisions and metrics.
- Deterministic no-op suppression, response leases, private review,
  aggregation, incident coalescing, and semantic deduplication in gated phases.
- Integration seams for the existing OpenClaw router and OmegaClaw gateway.

### Out of scope for now

- Live suppression before shadow validation.
- Replacing agent cognition, personalities, or model routers.
- Paid compute, broad gateway topology changes, or production activation
  without separate authorization.
- Semantic deduplication as an early hard gate.

## Current state

Ben approved stepwise implementation on 2026-07-24. The current 53-page
Revision 2 governing design and its original 43-page predecessor are preserved
under `library/omegahive-conversation-governor/`. Revision 2 incorporates
topology fallbacks, governor-cost accounting, ownership hysteresis, a semantic
egress firewall, predeclared activation gates, and human overrides. Local
discovery found OpenClaw 2026.7.1 (`2d2ddc4`), confirmed centralized Topology
A, and identified the existing `plugins/intent-model-router` integration seam.
The Phase B event/ledger contract and implementation/test plan are frozen. On
2026-07-27 the first standalone shadow-only executable slice was added at
`plugins/conversation-governor/`: deterministic normalization/IDs, duplicate,
loopback and sibling counterfactual decisions, exact structured-silence egress,
private JSONL audit, and hook adapters that reject non-shadow mode. Six focused
tests pass. The previously discussed “48 hours” was design observation, not
live shadow telemetry; the measurement clock starts only after safe plugin
activation. Six schema artifacts and ten canonical fixtures are now present,
with the focused plugin suite passing 8/8. The plugin is installed globally and
enabled in `openclaw.json`, still hard-locked to shadow mode. Gateway loading
is pending an operator restart because `openclaw-agent.service` is a
system-scope unit. No live suppression is authorized.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| OpenClaw runtime | upstream package | `/home/openclaw/.npm-global/lib/node_modules/openclaw` | installed package | `2026.7.1 (2d2ddc4)` |
| Existing router integration | local workspace plugin | `plugins/intent-model-router` | `agent/chat-room-identity-phase1` workspace branch | inspect before modification |
| Governor implementation | TBD after discovery | `projects/omegahive-conversation-governor/repos/` or a focused workspace plugin | TBD | none |

## Environments

Local Pop!_OS host; OpenClaw 2026.7.1. No remote resources or paid compute are
authorized or required for the initial phases.

## Key results

- Governing design Revision 2: `library/omegahive-conversation-governor/SOURCE.md`
- Approval and staged-rollout decision: `DECISIONS.md`
- Runtime/topology evidence: `docs/runtime-discovery.md`
- Frozen schemas and fixtures: `docs/event-ledger-contract.md`
- Module plan and named test matrix: `docs/implementation-plan.md`

## Open questions

- Which available transcript export provides the smallest sufficient replay
  corpus without retaining unrelated private content.
- Quantitative false-silence threshold required before each enforcement phase.

## Related projects and concepts

- `projects/openclaw-intent-model-router`: current local action/model routing seam.
- `projects/omegaclaw`: reflective agent and gateway integration target.
- `projects/channel-watchdog`: adjacent channel observability work.
- `projects/plain-spec-governor`: related spec-governance method, not the same runtime component.

## Risks

- False silence suppresses useful or safety-relevant responses.
- Split-brain leases or stale state permit duplicate public answers.
- Replay fixtures may leak private conversation content unless minimized and
  sanitized.
- Semantic deduplication can collapse legitimate disagreement.
- Gateway integration can affect all channels; initial work must remain
  shadow-only and feature-flagged.
- Existing workspace files are heavily modified; implementation must isolate
  its diff and preserve unrelated work.
