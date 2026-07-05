# Decision Log

## D-20260704-threadkeeper-async-worker-loop: Add supervised real async worker loop

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `projects/omegaclaw/repos/ThreadKeeper` commit `cc3cd1e` (`Add bounded queued worker loop`) on branch `agent/threadkeeper-hardening-next`; Telegram instruction from Ben: "We definitely want a real async worker loop".

### Context

ThreadKeeper Phase 3 already had queue-only dispatch, atomic queued-worker claim/finish, bounded manual drain, checksum sidecars, strict queued-task validation, cancellation preservation, patch-proposal mode, adjudication-required mode, persistent transcripts, and hash-chain audit. The remaining design question was whether to stop at operator-supervised bounded drains or add a real polling worker loop.

### Decision

Add a real async worker-loop primitive, but keep it explicitly supervised: it must be launched by an operator/supervisor, not self-started from parent `dispatch`.

### Alternatives considered

- Keep only `run_queued_dispatch(queue_path)` and `drain_queued_dispatches(max_tasks=...)` until after live @Protomegabot smoke.
- Add an unbounded daemon/self-scheduling loop immediately.

### Rationale and evidence

Ben explicitly preferred the real async worker loop. The implemented compromise, `subagent.run_queued_worker_loop(...)`, repeatedly polls and claims queued records, but exits on explicit bounds (`max_tasks`, `max_idle_polls`, `max_runtime_s`, or `stop_file`) and uses a best-effort local lock to prevent two local worker loops draining the same queue concurrently. Focused mock tests cover multi-task drain-to-idle, stop-file preservation before worker LLM calls, and concurrent-loop rejection. Verification: `git diff --check`, Python compile, and focused mock pytest (`71 passed`).

### Consequences

ThreadKeeper is closer to staged @Protomegabot pilot use, but the loop still needs a local install/smoke under @Protomegabot config before any live group/channel use. Defaults and supervisor wrapper policy should stay conservative.

### Revisit trigger

Revisit after the first @Protomegabot-config local smoke and controlled private/group smoke, or if the worker loop shows queue starvation, duplicate claims, runaway cost, stop-file failure, or audit gaps.

### Supersedes or superseded by

Supersedes the earlier Phase 3 "only add a live async worker loop if/when Ben explicitly wants supervised live dispatch" open question.

## D-20260705-threadkeeper-smoke-gates: ThreadKeeper supervisor/provider and private OpenClaw smoke

- Date: `2026-07-05`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-provider-smoke/` and `artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/`

### Context

ThreadKeeper branch `agent/threadkeeper-hardening-next` at commit `85145ea` has 82 passing focused mock tests and has progressed through supervisor-boundary, cancellation, env-file, and config smokes. Ben approved the ThreadKeeper smoke in Protobots message 2724 at 2026-07-05 08:48 PDT.

### Decision

Run two controlled non-live smokes: (1) a supervisor/provider-boundary smoke with a local fake Ollama endpoint to exercise the full worker→provider call path without external dependencies, and (2) a private/non-group OpenClaw smoke using the real local OpenClaw Gateway to exercise a genuine worker LLM call with `needs_adjudication` task-contract mode.

### Alternatives considered

- Skip the fake-provider smoke and go directly to live OpenClaw Gateway.
- Skip the private OpenClaw smoke and go directly to Telegram-private integration.

### Rationale and evidence

Both smokes passed. The fake-provider smoke verified the supervisor launches, the worker claims/calls/writes/exits cleanly, and exactly one provider call was made. The private OpenClaw smoke verified a real local Gateway `/v1/chat/completions` call returned HTTP 200, the worker used 16,756 tokens, and the task returned `needs_adjudication` as intended. No Telegram, external provider, secrets, paid compute, daemon, or scheduler was involved.

### Consequences

The next staged gate should adjudicate the private OpenClaw smoke candidate output, then consider staged Telegram-private integration with explicit stop conditions. Alternatively, run a multi-task or multi-persona supervisor smoke.

### Revisit trigger

Revisit if adjudication reveals worker output quality issues, if the Gateway call pattern changes, or before any Telegram-private or group integration.

### Supersedes or superseded by

None.

## D-<YYYYMMDD>-<short-slug>: <Decision title>

- Date: `<YYYY-MM-DD>`
- Status: `proposed | accepted | superseded | rejected`
- Decision owner: Benjamin Goertzel or delegated role
- Related task/run/commit: `<pointer>`

### Context

### Decision

### Alternatives considered

### Rationale and evidence

### Consequences

### Revisit trigger

### Supersedes or superseded by
