# Decision Log

## D-20260727-start-executable-shadow: Begin implementation without enabling suppression

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Evidence: `plugins/conversation-governor/`; focused Node tests

### Decision

Advance immediately from frozen design to the standalone executable shadow
slice. Treat the earlier 48-hour interval as design observation, not measured
shadow operation. Activation of the observer, collection of 48 hours of ledger
data, and any later enforcement remain distinct gates. Active mode is rejected
by the Phase B adapters.

### Rationale

There was no deployed observer from which a 48-hour measurement could have
been obtained. Building the observation-only code is therefore the necessary
next step and does not incur the false-silence risk of enforcement.

### Revisit trigger

The full schema/fixture matrix fails, OpenClaw hook compatibility differs from
the pinned runtime, or ledger review finds privacy or fail-open defects.

## D-20260724-standalone-shadow-plugin: Implement a standalone shadow-first plugin

- Date: `2026-07-24`
- Status: `accepted for implementation planning`
- Decision owner: Benjamin Goertzel
- Evidence: `docs/runtime-discovery.md`; `docs/implementation-plan.md`

### Decision

Implement the first vertical slice at `plugins/conversation-governor/`.
Separate pure policy from OpenClaw hook adapters, in-memory coordination, and
the append-only JSONL audit trail. Keep `intent-model-router` responsible for
model selection. Lock the first slice to shadow observation so it cannot block
inference, cancel delivery, or mutate payloads.

### Rationale

Phase A confirmed all agents share the same gateway and plugin pipeline, so a
single plugin provides the simplest Topology A implementation. A separate
plugin avoids coupling communication policy to model routing, and the pure
core preserves a future Topology B/C adapter seam. Relevant research rules are
Rules 1, 2, 3, and 7.

### Consequences

Phase B creates contracts, fixtures, audit behavior, and tests only. Passing
its gate authorizes replay-corpus work, not live suppression. Gateway config
activation and restart require a later gated step.

### Revisit trigger

The plugin hook contract changes, multi-process deployment invalidates the
in-process atomicity assumption, or replay data shows the proposed decision
surface is insufficient.

## D-20260724-design-corrections: Fold six sharpenings into the governor design before coding

- Date: `2026-07-24`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (via OmegaClaw review)

### Corrections

1. **Placement contingency:** Phase A discovery must verify the shared
   pre-inference seam. If OmegaClaw inbound does not traverse OpenClaw gateway
   pre-inference, fall back to per-agent local governors coordinated via shared
   ledger.
2. **Governor cost budget:** Add a `governor_overhead` metric (governor tokens
   / tokens saved). Novelty-score weights are initial guesses to be calibrated
   from Phase 1 shadow data, not shipped as fixed values.
3. **Ownership hysteresis:** Add conversational stickiness — recent-speaker bias
   with short timeout, broken only by explicit re-addressing — to prevent
   per-event owner thrash in fast dialogue.
4. **Non-semantic egress repair only:** Egress repair is constrained to
   stripping narration, truncating, and reformatting. Adding or altering claims
   is forbidden; the governor must not become an unaccountable co-author.
5. **Pre-registered go/no-go thresholds:** Phase 0 ends with a decision gate.
   Proceed only if measured no-op invocation rate and duplicate outbound rate
   exceed stated thresholds (to be defined before measurement).
6. **Human override grammar:** Add explicit channel commands — "everyone
   answer," "quiet mode," "show suppressed" — as first-class policy inputs.

### Rationale

These six points were identified in OmegaClaw's substantive review of the
governing PDF. Each addresses a real failure mode or missing constraint
without changing the core architecture. Ben's 53-page Revision 2, received
2026-07-24 and preserved in
`library/omegahive-conversation-governor/`, incorporates all six and is now the
current governing specification.

### Revisit trigger

Discovery findings or shadow measurements materially contradict the
 assumptions behind any correction.

## D-20260724-staged-shadow-first: Implement stepwise with a test gate after every phase

- Date: `2026-07-24`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md`; governing PDF section 13 and appendix A

### Context

The current OpenClaw/OmegaClaw proto-hive produces redundant invocations,
parallel answers, visible silence markers, operational narration, and repeated
incident messages. Ben supplied a detailed shared-governor design and directed
that it be implemented step by step with testing at every step.

### Decision

Implement sequentially from discovery and instrumentation through shadow
admission, deterministic suppression, leases, private review, aggregation,
incident coalescing, and finally advisory semantic novelty. Each phase requires
its own replay or canary acceptance evidence. No live suppression or shared
topology change is implied by the implementation mandate; activation requires
the applicable evidence and explicit approval.

### Alternatives considered

- Prompt-only changes: rejected as insufficient for cross-agent idempotency and
  pre-inference savings.
- Immediate enforcement: rejected because false silence is the dominant early
  safety risk.
- Semantic deduplication first: rejected because it is less deterministic and
  should remain advisory until calibrated.

### Rationale and evidence

The governing design distinguishes message creation from verbosity and places
admission before inference. Shadow-first rollout provides counterfactual
measurements without changing human-visible behavior. Relevant research rules
are Rule 2 (plain-language stateful spec), Rule 5 (reproducible reports), and
Rule 7 (modular seams); Rule 1 applies to calibration of the suppression
classifier.

### Consequences

Initial work is local, read-mostly, and non-operative. Every later feature is
independently flaggable and reversible. Replay labels and false-silence
measurements become promotion evidence.

### Revisit trigger

Discovery shows no safe common gateway seam; replay evidence finds unacceptable
false-silence rates; the two-agent topology changes materially; or discovery
findings invalidate any design correction in D-20260724-design-corrections.

### Supersedes or superseded by

None.
