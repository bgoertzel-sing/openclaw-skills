---
name: "persistent-subagent-orchestration"
description: "Persistent delegated work with durable approval continuity, bounded execution, evidence, and recovery."
---

# Persistent Subagent Orchestration

## Default operating contract

When a parent delegates a concrete research or engineering task, the child is persistent by default:

1. Complete the current safe, bounded step.
2. Inspect the result and select the next smallest useful step toward the delegated objective.
3. Continue without waiting for a parent prompt.
4. Maintain a durable task/run record with commands, artifacts, tests, findings, and next action.
5. Stop only at a terminal condition, material blocker, required authority decision, explicit budget/quality threshold, or operator cancellation.

Do not stop after preparation, a plan, partial results, or routine review.

## Delegation contract

Record:

- objective and acceptance conditions;
- project/repository and allowed paths;
- permitted external effects;
- current and next steps;
- resource limits and model/provider routing;
- artifacts and verification;
- checkpoint cadence;
- termination and escalation conditions.

Use a durable queue/worker record for multi-turn work. The parent must be able to inspect, pause, resume, cancel, and retrieve concise status.

## Authority continuity and precedence

Treat exact recorded operator approvals as durable capabilities, not one-turn hints.

1. Record the approval source, scope, resource/provider, time and cost bounds, allowed data/effects, stop/cleanup conditions, and whether it is one-shot or ongoing.
2. Revalidate that record at every activation before exercising it.
3. A valid approval remains actionable across scheduler activations and session/model handoffs until:
   - the approved action completes;
   - the operator explicitly revokes or supersedes it;
   - its expiry, resource, time, cost, or usage bound is reached; or
   - observed state makes the approved action unsafe or impossible.
4. Generic safety defaults such as "no paid compute without approval" do not negate a matching recorded approval. Resolve them as conditional guards: no paid compute unless approved.
5. If an activation payload literally contradicts a matching standing approval, do not silently choose the more restrictive text and loop forever. Compare provenance and specificity:
   - a newer explicit operator instruction overrides;
   - an exact standing approval overrides a generic scheduler default;
   - genuinely ambiguous or materially broadened scope is `BLOCKED_AUTHORITY`.
6. Never broaden approval by analogy. Changes to provider, resource class/count, region, image, storage, price, duration, data policy, or external effects require fresh authority unless the recorded envelope expressly permits them.
7. Record consumption and terminal state so completed one-shot authority cannot be reused.

## Step loop

At each checkpoint classify:

- **advance:** perform the next safe step;
- **repair:** diagnose and retry a failed check;
- **branch:** pursue a bounded alternative;
- **escalate-model:** use an approved stronger route;
- **escalate-compute:** propose remote compute or exercise a matching standing approval;
- **block:** report only a material authority/capability blocker;
- **complete:** verify acceptance, record evidence, and hand off.

Updates go to the parent only for milestones, changed risk, budget thresholds, important failures, or completion.

## Remote compute

Use local resources first when adequate. Before unapproved paid compute, invoke the remote-compute guardrail and present provider/account, hardware/image/storage/region, expected and maximum cost/time, transfer plan, stop/termination behavior, and artifact return.

When an exact approval already exists, revalidate its scope and current provider state, create/update the remote-job ledger, then proceed without requesting duplicate approval. Monitor cost and health, retrieve and verify artifacts, and terminate as approved. If capacity is unavailable or the envelope cannot be honored, report the precise mismatch; do not silently substitute.

## Verification and evidence

Before completion:

- run relevant checks;
- inspect outputs and diffs;
- record commands, versions, commits, seeds, artifacts, approval provenance, resource IDs, cost, and cleanup evidence;
- update project/task records, Kanban, and concise daily memory;
- distinguish observed results from interpretation.

## Failure recovery

Classify tool failures as transient or permanent. Retry transient failures with bounded backoff and try an equivalent route. Diagnose and repair permanent failures where possible. Preserve state across infrastructure outages. Never swallow failures or turn one tool error into a terminal blocker while alternatives remain.

## Anti-patterns

Do not:

- stop after a plan when implementation remains;
- ask "continue?" after ordinary steps;
- fabricate progress while idle;
- loop indefinitely on unchanged `BLOCKED_AUTHORITY`;
- discard or ignore a valid standing approval at the next activation;
- reuse completed, expired, revoked, or exhausted authority;
- use paid compute beyond exact approval;
- weaken model/compute requirements silently;
- mutate unrelated worktrees or publish without authority;
- restate the assignment instead of executing;
- treat a single recoverable tool failure as terminal.
