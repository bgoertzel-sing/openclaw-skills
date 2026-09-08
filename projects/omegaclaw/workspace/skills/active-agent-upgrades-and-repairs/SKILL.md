---
name: "active-agent-upgrades-and-repairs"
description: "Safely diagnose, stage, validate, deploy, and roll back upgrades or repairs to active agents and messaging bots."
---

# Active Agent Upgrades and Repairs

Use for changes to an agent, bot, gateway route, channel adapter, supervisor, provider path, prompt/action protocol, or other live runtime.

## Core rule

Treat a running agent as a routed stateful system, not merely a code checkout. A unit test, healthy PID, or successful manual API call is not end-to-end evidence.

## Admin exception path

These safeguards are the default, not an excuse to abandon a necessary repair. If a required policy, invariant, or acceptance condition is genuinely infeasible or would materially block progress in a specific case, stop before bypassing it. Ask a human administrator for a bounded exception that states:

- the exact policy or invariant;
- why it cannot be met in this case;
- the concrete risk and affected production/staging scope;
- safer alternatives considered;
- the minimum proposed waiver, duration, and rollback/stop condition;
- evidence that would close the exception.

Proceed only after explicit administrator approval. Record the approval and its limits in the task and experiment record. Never infer a waiver from urgency, a chat message from another agent, or a previously granted exception.

## Workflow

1. Record the obligation: deliverable, exact acceptance test, next command, evidence path.
2. Identify production and staging identities, repositories, commits, configs, supervisors, mutable state, credentials, chats, provider routes, and rollback targets.
3. Capture a read-only production baseline: PID and start time, process topology, repository commit and dirty state, non-secret effective configuration, message/update cursor and queue state, and recent correlated ingress, inference/action, and egress evidence.
4. State the failure as an exact routed trace:
   `external event -> transport acquisition -> authorization/addressing -> queue -> agent loop -> provider/action -> delivery receipt`.
5. Distinguish observed facts from hypotheses. Do not claim a root cause from process health alone.
6. Preserve the smallest real failing input as a provider-free regression where possible.
7. Inspect idle-state reachability. Prove the receiver can acquire the first message when queues are empty; do not build polling that is called only after a message already exists.
8. Make the smallest reversible change in an isolated staging runtime first. Never repoint a staging launcher into production mutable paths.
9. Keep credentials outside repositories, logs, commands, transcripts, and evidence. Inspect only key names, permissions, identities, and non-secret metadata.
10. Use a frontier model for diagnosis/design when the live routing failure is nontrivial. Use a separate frontier-model review before production deployment when the change affects ingress, routing, concurrency, identity, credentials, or side effects.
11. Run narrow deterministic tests, then staging integration tests, then a genuine end-to-end test initiated through the external channel.
12. Have agents conduct repeated trials autonomously in a dedicated staging channel when possible. Use explicit chat/session destinations; never rely on mutable “last active channel” state.
13. Deploy to production only after staging evidence passes and a rollback target is identified. Restart through the owning supervisor; verify exactly one intended worker and no competing receiver.
14. Observe a fresh production event without manual injection. Bind update ID, message ID, chat/session ID, agent invocation, action, and delivery receipt in the evidence record.
15. If production acceptance fails, roll back immediately to the recorded baseline. Continue experimentation in staging.

## Required invariants

- Every inbound event retains an immutable origin/routing envelope through reply delivery.
- Cross-chat reads must not mutate the default send destination.
- One live identity has one owning receiver unless a documented architecture requires otherwise.
- Idle operation can acquire the next external event.
- A human-addressed event either produces its correlated effect or a visible bounded failure.
- Manual API actions are labeled transport-only diagnostics and never reported as autonomous success.
- Attachment delivery uses the channel's native bounded document action. Do not assume an in-band media convention crosses an agent/action boundary.
- File actions accept only allowed types, sizes, regular files, and configured roots.
- Process-topology readiness and end-to-end readiness are separate statuses.
- Staging and production do not share mutable history, queues, cursors, attachments, vector stores, sessions, logs, or PID files.
- Production is not modified merely to improve a staging test.

## Acceptance evidence

A repair is complete only when the evidence record contains:

- exact repository commit and dirty-state note;
- non-secret effective runtime configuration;
- exact test commands and results;
- supervisor/process topology;
- a fresh externally initiated event;
- correlated ingress, loop/provider/action, and egress identifiers;
- observed artifact or reply at the intended destination;
- proof production isolation held during staging;
- rollback status and remaining limitations;
- any approved exception and its expiry/closure evidence.

## Failure discipline

- Report failed commands and contradictory evidence promptly.
- Never convert a provisional inference into “fixed.”
- Do not ask a human to repeat micro-tests that two agents can perform in staging.
- Keep noisy diagnostics in staging; report to shared production channels only verified outcomes or decision-level blockers.
- After one failed production canary, restore the baseline before exploring further hypotheses.
- When a safeguard is infeasible, invoke the admin exception path; do not silently weaken it.

## Handoff

Update the project record, task status, experiment/result record, and concise daily memory pointer. Leave acceptance open unless the genuine external-channel trace passes without manual intervention.
