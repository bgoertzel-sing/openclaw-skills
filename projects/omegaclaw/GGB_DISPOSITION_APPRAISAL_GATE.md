# Handoff-Blocked Disposition Appraisal Gate

- Status: passed offline; non-live only
- Date: 2026-07-17
- GGB capacities: 1.2 memory use; 2.1/2.2 appraisal and uncertainty; 3.2/3.5 goal maintenance and recovery; 4.1/4.3 bounded action selection; 5.2/5.4 audit and safety

## Purpose

Test a narrow intelligence layer above ThreadKeeper's passed missing-handoff
operator-disposition mechanism (`f09c621`). GoalChainer may rank the four
already-bounded dispositions using immutable, read-only `petta-memory`
evidence, but it must return a recommendation artifact only. It cannot record
a disposition, create a handoff, enqueue work, or change task state.

This separates appraisal from effects:

`pinned task/checkpoint + selected memory evidence -> appraisal recommendation -> explicit operator review -> existing ThreadKeeper validator/effect`

## Existing anchors

- ThreadKeeper `f09c621`: immutable `hold`, `request_cancel`, `fail_terminal`,
  and `expire` records; exact task/manifest/checkpoint binding; no requeue.
- Restart-stability gate `8c106b6`: repeated supervisor passes remain
  `handoff_required` with zero enqueue effects.
- `petta-memory` EvidenceSnapshot v2 / PiChart and admitted handoff contracts:
  immutable packet identity, bounded provenance, read-only replay.
- GoalChainer heuristic-memory bridge and reviewer thresholds: ranked,
  proof-bearing appraisal without live task claiming.
- `docs/GOAL_TASK_STATE_CONTRACT.md`: recommendation is evidence, not
  execution authority.

## Fixture matrix

| Fixture | Evidence/appraisal condition | Required recommendation | Required non-effect |
|---|---|---|---|
| transient dependency | recent, credible evidence that required input is expected inside a bounded window | `hold` with an explicit review deadline | task remains `FAILED_RETRYABLE`; zero enqueue/state effects |
| operator-requested stop | authenticated reviewed stop intent bound to this task version | `request_cancel` | no cancellation record or lifecycle transition before explicit review |
| irrecoverable invariant failure | pinned evidence that the task's done criteria cannot be met without forbidden action | `fail_terminal` | no terminal event before explicit review |
| stale objective | task age/goal record exceeds a preregistered expiry rule | `expire` | no expiry event before explicit review |
| ambiguous/conflicting evidence | no disposition clears the confidence/margin threshold | `hold` plus `needs_adjudication` | no synthesized handoff, older-checkpoint reuse, or queue effect |

## Pass gate

Archive one provider-free replay bundle containing pinned hashes, the exact
four-action vocabulary, bounded selected evidence IDs, per-action scores,
proof/evidence pointers, threshold policy, and a recommendation checksum.
Replaying identical inputs must produce identical ordering and digest.

Negative tests must reject a changed task version, manifest/checkpoint digest,
unknown disposition, unselected or content-mutated memory packet, stale snapshot/chart, missing
review deadline for `hold`, and any output that requests a direct effect. The
ThreadKeeper persistent root and source checkout hashes must be unchanged by
the appraisal run.

## Result and next implementation task

Passed at
`artifacts/ggb-capacity-gates/20260717-threadkeeper-disposition-appraisal/`.
Five synthetic fixtures and the fail-closed matrix now include per-packet
content-digest binding, so evidence strength/support/proof cannot change under
an unchanged snapshot admission record. A canary remains a separate decision:
ask Ben whether to approve an operator-reviewed recommendation path; do not add
a runtime bridge without that approval.

Threshold follow-on evidence is archived at
`artifacts/ggb-capacity-gates/20260718-disposition-threshold-counterexamples/`.
Five exact/adjacent edge cases pass, and an unsafe confidence-only rule shrinks
deterministically to a checksummed two-score margin counterexample. This does
not alter the appraisal runtime or grant disposition authority.

Bounded perturbation evidence is archived at
`artifacts/ggb-capacity-gates/20260718-disposition-perturbation-calibration/`.
The preregistered `{-0.03, 0, +0.03}^4` grid exercises 405 samples across four
clear and one ambiguous synthetic admitted-evidence archetype. All clear
recommendations remain stable; the ambiguous case adjudicates in 72/81 samples
and otherwise resolves only to its nominal top action. No decisive action
jumps directly to another decisive action. This is synthetic robustness
evidence, not calibration on operational evidence or canary authority.

The operational-evidence step is now preregistered at
`artifacts/ggb-capacity-gates/20260718-disposition-corpus-preregistration/`.
Its provider-free contract admits synthetic records only, requires immutable
task/checkpoint/evidence digests, independent two-reviewer plus adjudicator
labels, and a completed redaction audit, while prohibiting raw text,
identifiers, secrets, model scores, and model-produced labels. Passing it does
not authorize operational corpus collection or a canary.

The follow-on split preregistration is archived at
`artifacts/ggb-capacity-gates/20260719-disposition-split-preregistration/`.
It freezes label-blind, order-invariant 60/20/20 assignment from a scoped seed
and immutable task-version digest before any reviewed corpus exists. This is a
synthetic protocol check only and grants no collection or runtime authority.

## Explicit non-actions

No provider or Telegram call; no queue/supervisor launch; no memory write or
promotion; no disposition/lifecycle record; no ProtoMegaBot runtime change;
no secret/access change; no paid compute; no push or merge.
