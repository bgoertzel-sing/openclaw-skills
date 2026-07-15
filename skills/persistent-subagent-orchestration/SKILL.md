---
name: "persistent-subagent-orchestration"
description: "Run delegated research tasks persistently with evidence, bounded checkpoints, and explicit model/compute escalation."
---

# Persistent Subagent Orchestration

## Default operating contract

When a parent delegates a concrete research or engineering task, the child is **persistent by default**:

1. Complete the current safe, bounded step.
2. Inspect the result and select the next smallest useful step toward the delegated objective.
3. Continue without waiting for a parent prompt.
4. Maintain a durable task/run record with commands, artifacts, tests, findings, and next action.
5. Stop only at a terminal condition, a material blocker, a required authority decision, an explicit budget/quality threshold, or an operator cancellation.

A subagent must not stop merely because it has completed a preparatory step, created a plan, obtained partial results, or would benefit from an ordinary review.

## Delegation contract

Every persistent delegation records:

- objective and acceptance conditions;
- project/repository and allowed paths;
- permitted external effects;
- current step and next step;
- local-resource limits;
- model/provider routing;
- expected artifacts and verification;
- checkpoint cadence;
- termination and escalation conditions.

Use a durable queue/worker record for work spanning more than one model turn. A parent must have a way to inspect, pause, resume, cancel, and retrieve a concise status.

## Step loop

At each checkpoint, the child classifies the outcome:

- **advance:** perform the next safe step immediately;
- **repair:** diagnose and repair a failed narrow check, then retry;
- **branch:** pursue the highest-value bounded alternative while preserving the failed path;
- **escalate-model:** route one hard reasoning subproblem to an approved stronger model;
- **escalate-compute:** propose remote computation according to the compute policy;
- **block:** report only a material blocker requiring operator authority or unavailable capability;
- **complete:** verify acceptance criteria, record evidence, and hand off.

The parent should receive compact updates only on real milestones, changed risk, budget threshold, important failure, or completion—not a stream of “still working” messages.

## Resource routing

Use local resources first when adequate. If local CPU/RAM/runtime capacity is the limiting factor, evaluate Runpod or another approved remote provider.

Before provisioning paid or remote compute, invoke the remote-compute guardrail and present:

- provider/account context;
- hardware, image, storage, region;
- expected duration and cost estimate;
- data transfer and artifact-return plan;
- stop/termination criteria;
- consequences of stop vs. terminate.

The autonomous spend budget is zero unless the operator has explicitly authorized a concrete remote job. Do not provision, start, resize, or retain paid resources until that authorization exists.

If approved Runpod capacity is insufficient (hardware, availability, network/data policy, cost cap, or required capability), report the specific insufficiency and alternatives. Do not silently downgrade a task’s required model or compute class.

## Model routing

Honor task-specific model preferences. For substantive research writing/reasoning, do not silently fall back to a materially weaker model. If the preferred route is unavailable:

1. retry transient availability failures within bounded backoff;
2. use an explicitly approved fallback hierarchy;
3. otherwise report the blockage and preserve the task for resumption.

## Verification and evidence

Before declaring completion:

- run the narrowest relevant tests/checks;
- inspect outputs and diffs;
- record exact commands, versions, commits, seeds, and artifacts as applicable;
- update project/task records and a concise daily-memory pointer;
- distinguish observed results from interpretation.

## Kanban board visibility

Every persistent subagent must update the cross-project Kanban board (`catalog/KANBAN.md`) when it starts, reaches a milestone, or changes status. This is required for cross-project visibility — project-level `TASKS.md` files are authoritative for project detail, but the Kanban index is how the parent and operator see all active workers at a glance.

On each meaningful state change:
- add or update the subagent's card in the In Progress / Running lane with current status and next action;
- move to Blocked / Needs Ben if blocked;
- move to Done / Archived on completion.

Read the Kanban board at start to check for conflicting or overlapping work before beginning.

## Control commands

The orchestrator exposes durable operations:

- `status <task/run>`
- `pause <task/run>`
- `resume <task/run>`
- `cancel <task/run>`
- `prioritize <task/run>`
- `set-budget <task/run>` (requires explicit authorization for paid compute)
- `handoff <task/run>`

## Tool failure and recovery

When a tool call fails, do not stop and report the failure as a terminal outcome. Instead:

1. **Classify the failure:** transient (timeout, rate-limit, connection-refused, provider-unavailable) vs. permanent (file-not-found, permission-denied, schema-violation, logic-error).
2. **Transient failures:** retry with bounded backoff (e.g., 2s, 5s, 10s, then give up after 3 attempts). If the failure persists, try an alternative tool or approach that achieves the same goal.
3. **Permanent failures:** diagnose the root cause, attempt a repair (fix the file, adjust the command, correct the schema), and retry. If the repair itself fails, escalate to `block` with a precise diagnosis.
4. **Infrastructure outages** (e.g., provider relay unavailable, gateway restarting): record the partial state, wait briefly, and resume from the last checkpoint. Do not declare the task failed unless the outage persists beyond a reasonable bounded wait.
5. Never silently swallow a failure and proceed as if the tool succeeded. Record the failure, the retry attempt, and the outcome.

## Anti-patterns

Do not:

- stop after producing only a plan when implementation/experiment work remains;
- await a parent "continue" after each ordinary step;
- fabricate progress while a worker is idle;
- allow endless looping without bounded checkpoints or cancellation;
- use paid compute without explicit approval;
- silently use a weaker model for a quality-sensitive task;
- mutate unrelated worktrees or publish/push without task authorization;
- **restate your assigned task or objective as your output** — if you find yourself summarizing or repeating the assignment back to the parent, stop immediately and execute the first concrete step instead. The parent already knows the task; they need the result;
- **stop and report a single tool failure as a terminal blocker** when alternative approaches exist — retry, repair, or branch before escalating to `block`;
- **emit a plan-only response when the assignment asks for implementation** — a plan is a preparatory step, not a deliverable. Proceed to implementation unless a material blocker genuinely prevents it.
