# OmegaClaw ↔ ZeroBot/OpenClaw topology decision note

- Date: 2026-07-07
- Status: accepted by Benjamin Goertzel on 2026-07-15
- Scope: near-term bridge among `@Protomegabot`/OmegaClaw, ThreadKeeper, `petta-memory`, GoalChainer, and OpenClaw/ZeroBot-style agents.

## Recommendation

Use a **supervised, queue-mediated bridge** before any live bidirectional chat bridge:

1. **Ingress:** Telegram/OmegaClaw may create bounded task records only after allowlist/channel checks and explicit operator-approved scopes.
2. **Triage:** optional GoalChainer runs as a non-live/local decision tool over the bounded task text plus selected read-only `petta-memory` evidence packets. It may propose task state (`ready`, `blocked`, `backlog`) and rationale, but it must not send messages or mutate runtime state directly.
3. **Delegation:** ThreadKeeper owns worker execution via queue-only records, checksum sidecars, task contracts, quotas, transcript records, adjudication mode, and bounded worker loops.
4. **Egress:** accepted/adjudicated summaries may be returned to OmegaClaw/Telegram. Raw worker outputs, memory dumps, and GoalChainer proofs stay artifact-local unless explicitly selected and redacted.

The existing ProtomegaTron Telegram service remains a distinct bot/account and
uses the local OpenClaw Gateway only as its model provider. Its configured chat
targets are explicit allowlists. Acceptance of this topology does **not** create
an unrestricted agent-to-agent session bridge or grant silent cross-session
authority.

## Topology options considered

| Option | Shape | Pros | Primary risks | Near-term decision |
|---|---|---|---|---|
| A. Direct Telegram group bridge | OmegaClaw and ZeroBot/OpenClaw talk in a shared group | Fast human-visible collaboration | cross-agent loops, group spam, unclear authority, hard-to-bound memory/context exposure | Defer |
| B. Direct local API bridge | OmegaClaw calls OpenClaw/ZeroBot sessions directly | Low latency; avoids Telegram noise | session growth, hidden recursive agency, hard stop conditions | Use only for bounded smoke gates |
| C. Queue-mediated bridge | OmegaClaw writes task records; ThreadKeeper drains under contracts; operator/adjudicator accepts outputs | Best auditability, explicit stop conditions, aligns with existing ThreadKeeper PR #1 work | More latency and ceremony | Recommended |
| D. Read-only decision sidecar | GoalChainer/petta-memory only annotate choices; no delegation or messaging | Safest first GoalChainer integration boundary | Does not by itself improve execution | First GoalChainer runtime-adjacent step |

## Safety boundaries

- No GoalChainer live import into the running Telegram/OmegaClaw loop without explicit approval.
- No direct `petta-memory` live writes from GoalChainer; use selected read-only handoff packets only.
- No ThreadKeeper worker daemon/scheduler install by default; use supervised bounded runs with max-task/max-runtime caps.
- No automatic egress to Telegram from worker candidates until adjudication status is accepted.
- Preserve current token/channel allowlists and Landlock policy; this note does not change secrets/access/security settings.

## Small empirical gates before live use

1. **Read-only decision sidecar gate:** run GoalChainer over one captured/private task fixture plus one `petta-memory` handoff fixture; verify decision JSON and no runtime messages.
2. **Queue-mediated dry-run gate:** OmegaClaw-style input creates a ThreadKeeper queue task with contract/checksum; drain with fake worker; verify transcript/index/adjudication fields.
3. **Bounded local-provider gate:** one task drains through local OpenClaw provider with `requires_adjudication=true`; verify token accounting, result sidecars, and no Telegram egress.
4. **Private Telegram opt-in gate:** only after Ben approval and explicit stop conditions; one accepted/adjudicated summary returned to private chat, not group.

Ben approved this staged topology on 2026-07-15. Gates 1--3 already have durable
passing records under `artifacts/ggb-capacity-gates/`. The live Telegram service
already operates as the separate allowlisted bot, but the queue/GoalChainer
sidecar remains candidate-only and adjudication-gated. No unrestricted direct
OmegaClaw--ZeroBot bridge was enabled by the approval.

## GGB capacity mapping

- 2.2: separates claims/evidence/provenance by keeping GoalChainer proofs and `petta-memory` packets artifact-local.
- 2.5: provides a concrete architecture proposal with staged gates.
- 3.1: narrows multi-step planning to queue records and adjudicated task states.
- 4.3: coordinates shared memory via read-only handoff packets, not live writes.
- 4.5/5.2: preserves ThreadKeeper task contracts, transcripts, hash-chain/index checks, quotas, and adjudication.
- 5.1/5.5: keeps goal/motivation reasoning advisory until operator-approved runtime behavior changes.
