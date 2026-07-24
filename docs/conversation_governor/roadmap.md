# Conversation Governor — Roadmap

Branch: `agent/conversation-governor` (off `agent/chat-room-identity-phase1`)
Source design: Ben Goertzel, "OmegaHive shared conversation governor" design PDF (2026-07-24)
Review corrections folded in from ProtomegaTron's review (2026-07-24).

## Load-bearing principle

The cheapest response is a correctly suppressed invocation, not a shorter one.
Distinguish **essay amplification** (response longer than needed) from
**message amplification** (response generated when none was needed). The
governor targets message amplification first.

## Review corrections (agreed)

1. **Topology fallback.** The design assumes a shared pre-inference boundary
   where both agents' events can be inspected before prompt construction.
   This is contingent on Phase A discovery. If the premise fails: per-agent
   local governors coordinated via a shared ledger.
2. **Governor cost budget.** Novelty-score weights (0.45/0.25/0.20/0.10) are
   unjustified constants; they must be calibrated from Phase 1 shadow data,
   not shipped fixed. Track `governor_tokens / tokens_saved` as a first-class
   metric with an explicit budget.
3. **Ownership hysteresis.** Conversational stickiness: recent-speaker bias
   with a short timeout, broken only by explicit re-addressing. Prevents
   message-by-message owner thrash in fast human dialogue.
4. **Non-semantic-only egress repair.** The control plane may strip
   narration, truncate, reformat — never add or alter claims.

## Phases and test gates

- **Phase 0 — Instrumentation baseline.** Measure from existing session
  logs, no behavior change. Metrics: no-op invocation rate (LLM run whose
  terminal output is NO_REPLY/empty/HEARTBEAT_OK), duplicate public outbound
  rate, token/cost spend per class, heartbeat-triggered share.
  *Gate: baseline report committed; go/no-go thresholds evaluated.*
- **Phase A — Discovery.** Trace real event flow: Telegram ingress → gateway
  → dispatch → router → model call → egress, plus cron worker paths.
  Deliverable: `current_event_flow.md` with module/function names, insertion
  points, and the verdict: does a shared pre-inference boundary exist for
  both bots?
- **Phase 1 — Shadow governor.** Log what *would* be suppressed; suppress
  nothing. Measure false-silence rate against human-labeled samples.
- **Phase 2 — Deterministic suppression, narrowly scoped.** Hard suppression
  only for exact-match classes validated in Phase 1 (literal NO_REPLY
  leakage, exact duplicate outbound, repeated-event coalescing). Scope is
  explicit and enumerable; nothing semantic. (Ben, 2026-07-24: "the hard
  suppression needs to be scoped properly" — this phase is that scoping.)
- **Phase 3+ —** Shared response leases, private review requests, daily
  digest aggregation, multi-channel OmegaHive federation. Each gated on the
  previous phase's metrics holding.

## Go/no-go thresholds (defined in advance)

Leave shadow mode only if:

- no-op invocation rate ≥ 20% of LLM calls **or** duplicate public outbound ≥ 10%
- false-silence rate < 2%
- governor overhead < 5% of tokens saved

If not met: stop and reassess rather than build machinery for a small problem.

## Milestone reporting format

Each phase reports: **Completed / Evidence / Tests / Risks / Next gate.**
