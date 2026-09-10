# Iter baseline v3 gate specification

- Date: 2026-08-12
- Status: provider-free implementation complete; factual capture pending
- Capacities: 1.3, 1.5, 2.4, 3.1, 3.4, 4.2, 5.1, 5.2
- Supersedes: v2 as the next capture shape, not its existing test evidence

## Problem found

The v2 contract cannot represent the factual 2026-08-12 capture attempt. The
roadmap requires unresolved facts to remain `unknown`, but v2 requires every
receiver count to equal `1`, every receiver owner to be a nonempty string, and
every commit and routing fingerprint to have a final digest shape. A stopped
or ambiguous deployment therefore cannot produce a valid observation record;
the only choices are to invent facts or emit no machine-checkable evidence.

## Capacity-to-work map

| Capacity lane | Existing work | v3 empirical contribution |
| --- | --- | --- |
| 1.3, 1.5 | OmegaClaw transport and identity records | Separate requested deployment slot, declared runtime identity, and observed receiver state |
| 2.4, 3.1, 3.4 | `petta-memory` evidence packets and ThreadKeeper receipts | Preserve unknown observations explicitly and content-bind the evidence used to resolve them |
| 4.2, 5.1, 5.2 | GoalChainer offline gate and supervised runtime boundaries | Make adapter readiness a derived fail-closed verdict, never an operator assertion |
| 2.3, 4.4, 5.4 | `petta-chem` run-contract patterns | Reuse preregistered observation/result separation without claiming chemistry evidence |

## Frozen v3 shape

Keep v2's exact three ordered deployment slots and all-false authority block.
For each fact currently required as final, encode an observation object:

```json
{"status":"known","value":"content-bound value","evidence_sha256":"64-hex"}
```

or exactly:

```json
{"status":"unknown","reason":"bounded enum","evidence_sha256":"64-hex"}
```

Allowed unknown reasons are `identity_ambiguous`, `receiver_inactive`,
`owner_unobserved`, `source_unresolved`, `rollback_unresolved`, and
`routing_projection_unapproved`. Free-form unknown reasons are rejected.
Receiver state is independently one of `active_single`, `inactive`, or
`ambiguous`; only `active_single` may carry a known owner and count `1`.

The validator computes `adapter_design_ready`; the input must not supply it.
It is true only when all three records have known source/rollback commits,
known approved secret-free routing fingerprints, unambiguous slot/runtime
identity, and `active_single` receiver state with one known owner. A
structurally valid observation with any unknown is recorded as
`capture_valid_adapter_not_ready`.

## Near-term empirical gate

Implement v3 beside v2, then replay these provider-free cases:

1. The 2026-08-12 inactive/ambiguous observation passes as a valid capture and
   derives `adapter_design_ready: false`.
2. One synthetic fully known three-bot record derives readiness true.
3. An asserted readiness field, invented digest, free-form unknown reason,
   unknown value plus known status, inactive receiver with owner/count, wrong
   slot order, duplicate JSON member, secret-like key, or any live authority
   fails closed.
4. Mutating any cited evidence bytes makes its digest check fail.

## Implementation result

Implemented under
`artifacts/ggb-capacity-gates/20260812-iter-three-bot-baseline-v3/`. The
standard-library suite covers valid unknown/not-ready and fully known/ready
records plus fail-closed authority, readiness assertion, unknown-reason,
receiver-consistency, evidence-integrity, slot-order, secret-key, invented-
digest, and duplicate-member cases. Next: encode only the already recorded
secret-free capture evidence as a valid not-ready observation, then request
the unresolved slot/runtime mapping from the runtime owner. Do not restart
receivers merely to make the gate pass.

## Boundaries

This specification grants no adapter design or implementation, runtime
restart/stop/launch, provider call, Telegram action, credential access, state
mutation, GoalChainer integration, memory write, ThreadKeeper PR #1 change,
paid compute, push, or merge. GoalChainer remains an external offline input;
any later use still requires a non-live smoke gate and explicit approval for
runtime behavior changes.
