# GoalChainer ↔ ThreadKeeper Goal/Task-State Contract

**Status:** draft v0.2 (non-live canary)
**Date:** 2026-07-13

## Purpose

Define a fail-closed, auditable mapping from GoalChainer decisions to ThreadKeeper candidate tasks. This contract does not authorize live task claiming, Telegram egress, runtime installation, memory writes, or automatic acceptance.

## Roles and trust boundary

1. `petta-memory` supplies a bounded, immutable, read-only evidence handoff with provenance.
2. GoalChainer appraises candidate actions and emits decisions; it does not claim or execute tasks.
3. A narrow adapter may turn an eligible decision into a ThreadKeeper queued-task candidate.
4. ThreadKeeper enforces task-contract limits and records worker evidence.
5. A separate reviewer/operator adjudicates every canary result.

No component may treat a recommendation as execution authority.

## GoalChainer decision fields

Expected decision fields include:

- `action_id`: non-empty unique string
- `label`: human-readable summary
- `status`: `recommended`, `candidate`, `held`, `weak`, or `blocked`
- `score`: finite number in `[0, 1]`
- `norm_status`: `obliged`, `permitted`, `forbidden`, or `unregulated`
- `norm_reasons`: list of strings
- `evidence`: bounded proof/provenance record
- `satisfied_goals` / `missing_required_goals`: bounded lists

Unknown/malformed status, action, norm, evidence, or score fields fail closed before queue construction.

## ThreadKeeper task-contract fields

A canary queued task contains:

- `objective`: string goal prefixed with the source `action_id`
- `allowed_paths`: narrow workspace-relative path list
- `forbidden_actions`: explicit prohibited effects
- `done_criteria`: bounded proof obligations
- `max_tool_calls`: explicit small cap
- `patch_proposal_only: true`
- `requires_adjudication: true`

The queue record and checksum sidecar remain subject to ThreadKeeper's existing schema, path, quota, cancellation, and audit checks.

## Fail-closed decision mapping

| GoalChainer result | Canary adapter behavior |
|---|---|
| `recommended` + non-forbidden norm | May produce a candidate queue record; always `requires_adjudication: true` |
| `candidate` + non-forbidden norm | May produce a candidate queue record; always `requires_adjudication: true` |
| `held` | Record deferred; do not queue |
| `weak` | Record insufficient evidence; do not queue |
| `blocked` | Record blocked; do not queue |
| any `norm_status == forbidden` | Record forbidden; do not queue, regardless of status or score |
| unknown/malformed/ambiguous result | Fail closed; do not queue |

A blocked/forbidden action is never converted into another task's executable instruction. Its identifier may be copied only into `forbidden_actions` as an audit constraint.

## Canary lifecycle

```text
read-only evidence artifact
        ↓
GoalChainer decisions
        ↓ validate shape, uniqueness, norms, evidence
eligible recommended/candidate decision
        ↓ construct checksum-protected candidate task
ThreadKeeper bounded worker
        ↓ candidate result only
reviewer policy + operator adjudication
        ├─ accepted_offline_evidence
        ├─ rejected
        └─ needs_review
```

There is no canary `auto-accept` transition. `accepted_offline_evidence` means only that the archived candidate passed the named offline gate; it does not authorize posting, applying a patch, claiming a live task, writing memory, or changing runtime behavior.

## Adjudication requirements

The reviewer must check:

1. **Integrity:** source evidence, decision, queue record, result, and checksum pointers match the archived artifacts.
2. **Evidence:** required proof artifacts are present, bounded, and provenance-linked.
3. **Norms:** neither the selected action nor worker output violates a forbidden norm/action.
4. **Goal coverage:** required goals/done criteria are addressed; missing goals remain explicit.
5. **Leak safety:** no secrets, tokens, raw sensitive logs, or PII are exposed.
6. **Non-action boundary:** no Telegram post, provider call, memory write/promotion, queue claim outside the fixture, supervisor launch, or runtime bridge change occurred.
7. **Policy:** the action is explicitly allowlisted for the particular offline gate. The current incident-response fixture allowlists only `publish_redacted_summary`.

Any failed check yields `rejected`; inconclusive or missing evidence yields `needs_review`.

## Empirical conformance gate

A contract-conformance fixture passes only if all of these hold:

- sensitive-data scenario: redacted summary queues as a candidate and can pass offline review;
- forbidden raw-log action is not queued even if its score/status is otherwise favorable;
- every queued `recommended` or `candidate` record has both `patch_proposal_only` and `requires_adjudication` exactly `true`;
- `held`, `weak`, and `blocked` decisions produce no queue task;
- malformed/unknown statuses and duplicate/empty action IDs fail closed;
- a reviewer cannot convert offline acceptance into live egress or workspace application;
- no memory write, inferred-belief promotion, Telegram/provider action, paid compute, or runtime behavior change occurs.

Current evidence: `artifacts/ggb-capacity-gates/20260712-goalchainer-canary-review-boundary/` and `repos/OmegaClaw-GoalChainer/tests/test_threadkeeper_canary_policy.py` cover the first four policy invariants. The malformed/duplicate adapter-input matrix remains the next narrow implementation gate.

## Promotion rule

Moving beyond this non-live contract requires a new decision record and explicit Ben approval defining scope, stop conditions, rollback, target chat/runtime, and whether any result may be applied or emitted. Until then, all outputs remain review-only artifacts.
