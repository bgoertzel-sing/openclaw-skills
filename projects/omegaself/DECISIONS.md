# OmegaSelf — Decisions

## D1: Test on ProtoMegaBot2 canary before any live ProtoMegaBot change
**Date:** 2026-07-15
**Rationale:** ProtoMegaBot is live and useful. All OmegaSelf integration must be validated on the isolated ProtoMegaBot2 canary first.
**Alternatives:** Direct ProtoMegaBot deployment — rejected, too risky for a governance-layer change.

## D2: Follow the coding-agent-pack's 15-task sequence
**Date:** 2026-07-15
**Rationale:** The pack defines a disciplined shadow-mode-first approach: record-only observations before behavior changes, reasoner SPI before backend migration, signed policy before capability dispatch.
**Source:** `OMEGASELF_CODING_AGENT_QUICKSTART.md`

## D3: Persistent subagent for implementation
**Date:** 2026-07-15
**Rationale:** OmegaSelf is a multi-phase integration requiring sustained context across sessions. A persistent subagent following the persistent-subagent-orchestration skill with Kanban updates is the right execution model.

## D4: Record-only bridge is default-off and fail-isolated
**Date:** 2026-07-15
**Rationale:** Importing an optional governance layer must not jeopardize ProtoMegaBot's existing channel connection. The bridge imports the OmegaSelf runtime lazily, catches observation failures, changes no dispatch result, and activates only under `OMEGASELF_RECORD_ONLY`. Raw message, parsed-call, result, and error bodies are hashed rather than copied into this initial ledger.
**Authority boundary:** Records use `runtime:unattested`; no current-identity or Allow authority is inferred.

## D5: Develop against an isolated canary worktree
**Date:** 2026-07-15
**Rationale:** The ProtoMegaBot2 canary path is also carrying the active Machintel lane. OmegaSelf is isolated on `agent/omegaself-record-only` from the same pinned canary commit so both sets of work remain reviewable and no runtime history is overwritten.

## D6: Queue OMERA after OmegaSelf, provisionally over PeTTa Memory
**Date:** 2026-07-20
**Decision:** Do not begin OMERA implementation until OmegaSelf is implemented and validated. Treat the likely stack as PeTTa Memory/PLN substrate -> OmegaSelf evidence, prediction, policy, and receipt layer -> OMERA affective modulation and emotion regimes -> governed OmegaClaw actuation.
**Rationale:** OMERA depends directly on stable OmegaSelf records and its single governance choke point. Implementing the affect layer earlier would either duplicate those interfaces or weaken replay and authority guarantees.
**Uncertainty:** “On top of PeTTa Memory” is presently an architectural assumption, not a frozen interface decision; confirm it from the implemented OmegaSelf–PeTTa integration before OMERA WP0.
**Source:** Ben, Telegram message 10383, 2026-07-20; accompanying OMERA paper and implementation-plan attachments in messages 10378–10379.
