---
name: "active-agent-upgrades-and-repairs"
description: "Add identity isolation, descendant containment, and stale-controller retirement gates for live bot repairs."
---

# Active Agent Upgrades and Repairs

Use for changes to an agent, bot, gateway route, channel adapter, supervisor, provider path, prompt/action protocol, or other live runtime.

## Core rule

Treat a running agent as a routed stateful system, not merely a code checkout. A unit test, healthy PID, or successful manual API call is not end-to-end evidence.

## Admin exception path

These safeguards are the default, not an excuse to abandon a necessary repair. If a required policy, invariant, or acceptance condition is genuinely infeasible or would materially block progress in a specific case, stop before bypassing it. Ask a human administrator for a bounded exception that states the exact invariant, why it cannot be met, the concrete risk and scope, safer alternatives, the minimum waiver and expiry, rollback/stop conditions, and closure evidence. Proceed only after explicit approval and record its limits.

## Workflow

1. Record the obligation: deliverable, exact acceptance test, next command, evidence path.
2. Identify production and staging identities, repositories, commits, configs, supervisors, scheduled recovery/heartbeat jobs, mutable state, credentials, chats, provider routes, and rollback targets.
3. Before starting staging, resolve each effective messaging/provider identity from non-secret runtime metadata and prove it differs from every production identity. Naming or config-file separation alone is insufficient.
4. Capture a read-only production baseline: PID/start time, raw process topology, controller-reported status, repository commit/dirty state, non-secret effective configuration, cursor/queue state, and recent correlated ingress/inference/egress evidence.
5. State the failure as an exact routed trace: external event -> transport acquisition -> authorization/addressing -> queue -> agent loop -> provider/action -> delivery receipt.
6. Distinguish observed facts from hypotheses. Do not claim a root cause from process health alone.
7. Preserve the smallest real failing input as a provider-free regression where possible.
8. Inspect idle-state reachability. Prove the receiver can acquire the first message when queues are empty.
9. Make the smallest reversible change in an isolated staging runtime first. Never repoint staging into production mutable paths.
10. Before any live staging start, run a lifecycle-containment preflight. Enumerate expected child processes/groups and prove stop, timeout, and rollback terminate the complete descendant tree. Treat daemonization, new sessions, containers, and separately supervised children as explicit containment boundaries.
11. Keep credentials outside repositories, logs, commands, transcripts, and evidence.
12. Use a frontier model for nontrivial diagnosis/design and an independent review before production changes to routing, concurrency, identity, credentials, or side effects.
13. Run narrow deterministic tests, staging integration tests, then a genuine externally initiated end-to-end test.
14. Use explicit chat/session destinations; never rely on mutable last-active-channel state.
15. Deploy only after staging passes and rollback is identified. Restart through the owning supervisor; verify exactly one intended worker and no competing receiver.
16. Observe a fresh production event. Bind update/message/chat IDs, invocation, action, and delivery receipt.
17. Reconcile controller truth with raw topology: controller status must agree with live PIDs, ownership, descendants, and PID files. A controller reporting stopped while owned processes remain is a failed lifecycle/status gate.
18. Before declaring acceptance, enumerate all recovery, heartbeat, canary, watchdog, and rollback automation that can still mutate this runtime. Disable or retarget superseded controllers through the authorized scheduler owner, then prove none can stop, restart, or leak internal diagnostics into the accepted runtime/channel.
19. If acceptance fails, roll back immediately. Continue experimentation in staging.

## Required invariants

- Every inbound event retains an immutable origin/routing envelope through reply delivery.
- Cross-chat reads do not mutate the default send destination.
- One live identity has one owning receiver unless explicitly documented.
- Staging and production identities and credentials are distinct unless a bounded admin exception exists.
- Idle operation can acquire the next external event.
- A human-addressed event produces its correlated effect or a visible bounded failure.
- Manual API actions remain labeled transport-only diagnostics.
- Attachment delivery uses the native bounded document action.
- File actions accept only allowed types, sizes, regular files, and configured roots.
- Raw topology and controller-reported state agree.
- The owning controller can stop the full descendant tree.
- No superseded recovery/heartbeat/canary controller retains mutation authority after acceptance.
- Internal diagnostic notes are never delivered to production user channels as a side effect of maintenance.
- Staging and production do not share mutable history, queues, cursors, attachments, vector stores, sessions, logs, or PID files.
- Production is not modified merely to improve staging.

## Acceptance evidence

A repair is complete only when evidence contains:

- exact repository commit and dirty-state note;
- non-secret effective configuration and identity-isolation proof;
- exact test commands/results;
- raw and controller-reported topology with agreement proof;
- lifecycle failure-injection/stop test and post-stop absence evidence;
- inventory and disposition of all scheduled/standing controllers that can mutate the runtime;
- a fresh externally initiated event with correlated ingress, action, and egress identifiers;
- observed artifact/reply at the intended destination;
- proof production isolation held;
- rollback status, remaining limitations, and any approved exception.

## Failure discipline

Report contradictions promptly. Never convert provisional inference into fixed. Keep noisy diagnostics in staging. After one failed production canary, restore baseline. If identity separation or lifecycle containment fails, stop, preserve evidence, and revoke acceptance. Invoke the admin exception path rather than silently weakening safeguards.

## Handoff

Update project/task/experiment records and a concise daily memory pointer. Leave acceptance open unless the external trace, topology-truth, and stale-controller-retirement gates all pass.
