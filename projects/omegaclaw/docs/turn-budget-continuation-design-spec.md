# Turn-Budget Continuation: Requirements and Design Spec

## Problem

ProtoCosmo2's Iter agent loop (`iter.py`) has a bounded step budget
(`MAX_FAST_STEPS = 50`). When a task exceeds this budget without the agent
calling `send`, the outer transport emits a generic "could not complete this
message safely" failure message. The agent's in-progress work is lost from
the user's perspective, and the failure message is indistinguishable from a
crash or safety violation.

The interim watchdog (implemented above) mitigates this by nudging the agent
to `send` a progress summary at step 45. This spec addresses the deeper
structural fix.

## Requirements

### R1: Graceful checkpoint at turn exhaustion
When the agent reaches `MAX_FAST_STEPS` without calling `send`, it must
automatically emit a structured checkpoint containing:
- what it accomplished this turn
- what remains unfinished
- current test/build state (if applicable)
- the next concrete command to resume with

### R2: Continuation across turns
A subsequent user message (or automatic re-prompt) must be able to resume
the task with full context of the prior turn's work, without re-reading
the entire experience log. The checkpoint must be durable and queryable.

### R3: No false-alarm failure message
The outer transport's "could not complete safely" message must never appear
for turn-budget exhaustion. It must be reserved for actual runtime failures
(provider errors, crashes, authentication failures). Turn-budget exhaustion
is a normal operating condition, not a safety failure.

### R4: Backward compatibility
The checkpoint/continuation mechanism must not change the existing `send`
semantics, tool invocation protocol, or experience-log format in a way that
breaks running agents.

### R5: Bounded overhead
Checkpoint persistence and continuation must add negligible latency (< 1s)
and minimal memory overhead. Checkpoint data should be compact (target:
< 2KB).

## Design

### Checkpoint format

When the turn budget is exhausted without a `send`, the loop writes a
structured checkpoint file before transitioning:

```json
{
  "schema_version": 1,
  "session_id": "<uuid>",
  "created_at": "<ISO-8601>",
  "prompt_sha256": "<hash of originating user prompt>",
  "accomplished": "<brief summary of work done this turn>",
  "remaining": "<brief description of unfinished work>",
  "test_state": "<pass/fail counts or 'not run'>",
  "next_command": "<single concrete command to resume>",
  "experience_size": <int>
}
```

Location: `checkpoints/<session_id>/<timestamp>.json` relative to the iter
working directory.

### Loop changes

1. **Checkpoint detection**: At `autonomous_steps >= MAX_FAST_STEPS`, if no
   `send` was called this turn, invoke a `generate_checkpoint` step:
   - Send one final LLM call with a forced `send` containing the checkpoint
     summary, using a constrained prompt that requests the structured fields.
   - The `send` content IS the user-visible checkpoint message (not a
     separate sidecar), so the user sees real progress, not a wrapper
     failure.

2. **Durable storage**: After the checkpoint `send` completes, write the
   structured checkpoint file. This enables future automatic resume.

3. **Transport message**: The outer transport
   (`phase6_private_canary_runner.py` / `private_canary.py`) must distinguish
   turn-budget exhaustion from runtime failure. Options:
   - Add a distinct exit code or stdout marker from `iter.py` (e.g., `{"status":
     "checkpoint", ...}`) that the transport recognizes as success-with-more-work.
   - Alternatively, since the agent already called `send`, the transport sees
     a normal reply and does not trigger the failure path at all. This is the
     preferred design — the checkpoint is just a regular `send`.

### Continuation

When a new user message arrives and a recent checkpoint exists for the same
session:
- Inject the checkpoint's `accomplished`, `remaining`, and `next_command`
  into the system prompt context (not the experience log) so the agent
  resumes with awareness of its prior progress.
- The user's new message takes priority; the checkpoint is supplementary
  context, not a directive.

For automatic resume (no user message needed):
- Configurable via a `--auto-resume` flag on the iter loop.
- On startup, if a checkpoint younger than N minutes exists, the loop
  injects the checkpoint as a synthetic user message: "Resume the previous
  task: <remaining>. Start with: <next_command>."
- N defaults to 300 (5 minutes); configurable via env var.

### Transport changes (phase6_private_canary_runner.py)

No change needed if the checkpoint is delivered via a normal `send` call.
The transport already treats a successful `send` as a completed turn.
The "could not complete safely" message only fires when no `send` was
captured, which the checkpoint prevents.

If we later want a distinct transport-level signal (e.g., for logging or
metrics), add an optional `{"status": "checkpoint"}` marker in the iter
stdout alongside the existing `{"status": "ok"}` format.

### What the interim watchdog does vs. this spec

The interim watchdog (just implemented) injects a text reminder at step 45
telling the agent to call `send` with a progress summary. This is a
prompt-level nudge with no structured storage.

This spec adds:
1. A *guaranteed* checkpoint at step 50 (not a nudge at 45).
2. Structured durable storage of the checkpoint.
3. Automatic continuation context injection on the next turn.
4. Optional auto-resume without user prompting.

## Open questions

1. Should the checkpoint `send` count against `max_outbound_messages` in the
   canary config? (Preference: no — it's a system-generated safety send, not
   a user-initiated message.)

2. Should auto-resume be enabled by default or require explicit opt-in?
   (Preference: opt-in initially, enable by default after validation.)

3. Should the checkpoint include a truncated experience tail (last N
   messages) for richer continuation context, or is the summary sufficient?
   (Preference: summary only initially; measure continuation quality before
   adding bulk.)

## Implementation phases

**Phase 1** (this session): Interim watchdog — step 45 text nudge. ✅ Done.

**Phase 2**: Structured checkpoint at step 50 with guaranteed `send` +
durable file. ~2-3 hours.

**Phase 3**: Continuation context injection on new user message. ~1-2 hours.

**Phase 4**: Auto-resume mode with configurable threshold. ~1-2 hours.

**Phase 5**: Validation — run a long coding task end-to-end, verify
checkpoint fires, continuation works, no false-alarm messages. ~1 hour.