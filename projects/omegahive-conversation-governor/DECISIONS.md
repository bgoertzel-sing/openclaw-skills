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

## D-20260806-shadow-deployment-approved — shadow-mode deployment approved

- Date: 2026-08-06 (23:09 PDT, protobots-updates, Ben)
- Status: accepted

### Decision

Deploy the Conversation Governor in shadow ingress mode. The governor observes
real traffic and records counterfactual admission/egress recommendations for
roughly one day; the recommendations are then reviewed for sense before any
activation step is even proposed. No live suppression, mutation, or inference
blocking is authorized by this decision. On the OpenClaw side this means
completing frozen task B5: restart `openclaw-agent.service` so the installed,
shadow-locked `plugins/conversation-governor` observer loads, then capture one
synthetic ledger entry, then accumulate ~24h of shadow telemetry before review.
The OmegaClaw-side Phase D shadow shim (ProtoCosmo2) proceeds in parallel under
the same constraint: recommendations only.

### Evidence and rationale

Ben's explicit instruction in protobots-updates, 2026-08-06 23:09 PDT:
"yes let's deploy the governor in shadow ingress mode, i.e. have it make
recommendations for a day or so and make sure they make sense." Triggering
incident: five near-identical channel-watchdog alert messages in one minute,
caused by missing cross-run dedup in `bin/channel-watchdog.py` (fixed same
evening; 12 tests pass) — the governor would not have seen these because they
traverse the cron announce delivery path, not the conversational pipeline.

### Consequences

A ~24h shadow-observation review checkpoint is scheduled. Activation remains a
separate future decision requiring the replay/canary gates plus explicit
approval.

## D-20260806-direct-post-subagent-scope — governor scope extended to direct-posting subagents

- Date: 2026-08-06 (23:09 PDT, protobots-updates, Ben)
- Status: accepted

### Decision

Governor coverage is extended in scope to subagents and scheduled jobs that are
registered as able to post directly on Telegram channels (OpenClaw cron
`announce` deliveries, isolated agentTurn outputs, and similar direct-post
paths), not only interactive conversational replies.

### Evidence and rationale

Ben: "maybe the governor SHOULD be extended to handle subagents that are
registered as able to post directly on TG channels." Same-evening evidence:
the `Channel watchdog scan` cron job (isolated agentTurn, announce delivery to
telegram:-1003983157420) emitted five near-identical alerts; this path bypasses
both the OmegaClaw egress pipeline and the conversational ingress/egress seams
the Phase B design instruments. First implementation step is a seam audit:
determine whether the OpenClaw plugin hook surface observes cron/announce
deliveries; if not, add a delivery-level observation seam in shadow mode.

### Revisit trigger

The seam audit shows cron/announce deliveries already pass an instrumentable
hook; or the delivery path changes materially in an OpenClaw upgrade.
## D-20260807-squelch-attachment-watchdog-noise

### Decision

Treat `attachment promise not fulfilled` watchdog diagnostics as deterministic
egress noise: suppress them at the watchdog source immediately and classify
raw and Telegram-rendered equivalents as `SUPPRESS` in the governor. Keep
other watchdog alert classes unaffected. Governor enforcement remains
shadow-only until its separately authorized active-mode gate.

### Evidence and rationale

Ben explicitly requested both layers after repeated ProtoCosmo2 canary alerts
added no useful information to the shared updates channel. Provider-free tests
cover the source filter, both governor text forms, and preservation of an
unrelated watchdog alert.
