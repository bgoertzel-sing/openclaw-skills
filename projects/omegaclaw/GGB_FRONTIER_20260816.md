# GGB empirical frontier — 2026-08-16

Purpose: concise execution view over `GGB_CAPACITIES_ROADMAP.md`. This record
grants no runtime, VM2, provider, Telegram, memory-write, task-claim,
ThreadKeeper PR #1, held-out reveal, or motivation-materialization authority.

## Capacity-to-work map

| Lane | GGB capacities | Existing anchor | Current empirical gate | Next small task | State |
|---|---|---|---|---|---|
| Request → bounded contract | 1.1, 2.1, 2.2, 3.1, 5.3, 5.4 | Frozen zero-effect classifier and v0.6 sandbox | `artifacts/ggb-capacity-gates/20260811-heldout-decision-receipt-contract/` | If Ben authorizes D1, bind the exact decision receipt; only afterward build a separate one-shot A09–A12 runner | blocked on D1 |
| Memory → appraisal → motivation | 1.2, 2.2, 2.5, 4.3, 5.5 | Read-only `petta-memory` handoff, GoalChainer heuristic PLN/deontic path, MetaMo score-policy fixtures | `artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/` | If Ben authorizes D2, bind the exact decision receipt before running the reviewed deterministic 64/32 materializer | blocked on D2 |
| Delegation and durable work | 1.3, 3.2, 3.3, 4.1, 4.5, 5.2 | ThreadKeeper draft PR #1 and persistent-worker records | PR #1 safety-floor ancestry; latest parent-binding checks recorded in `PROJECT.md` | Coordinate with PR #1; add work only for a concrete failing fixture or review finding | wait / coordinate |
| Scientific reasoning | 2.3, 4.4, 5.2, 5.4 | `petta-chem` run contracts and completed exp07 rich-pool records | `artifacts/ggb-capacity-gates/20260814-petta-chem-structural-transfer-prereg/` | After the priority pause is explicitly lifted, implement the preregistered read-only digest-bound evaluator; do not touch incomplete graph-seed-1003 or shared PeTTa state | preregistered; paused |
| Conversation and delayed reasoning | 1.5, 2.4, 3.1, 3.4, 4.2, 5.1, 5.2 | Addressed Omega loop, durable request origin, pinned memory, rollback closure | `experiments/20260816T072000Z-protomega-deterministic-delayed-live-fixture/` plus restoration evidence in `experiments/20260816T034500Z-protocosmo2-protomega2-restoration/` | Preserve the accepted one-owner/receiver baseline; make no further live change from this roadmap | gate passed; hold |
| Post-VM2 agentic staging | 1.3, 2.4, 3.1, 3.2, 3.4, 4.1, 4.3, 5.1–5.5 | Iter planning, Protomega2 staging identity, `petta-memory` task boundary | `GGB_VM2_AGENTIC_ADMISSION.md`: complete, digest-bound evidence for every target bot | After that prerequisite is evidenced, first freeze a provider-free Iter loop contract for Protomega2; separately define ProtoCosmo2's bounded `petta-memory` task acceptance/rollback record | blocked on VM2 acceptance |

## Near-term order

1. Preserve the restored three-identity production baseline; this roadmap does
   not authorize another canary, restart, or runtime modification.
2. Wait for evidence that all target bots are ported to and accepted on VM2.
   Only then start the Iter/Protomega2 contract gate; keep ProtoCosmo2's
   `petta-memory` task as a separate promotion decision.
3. Preserve the D1 and D2 receipt seams without interpreting silence as
   approval.
4. Preserve the `petta-chem` preregistration until its priority pause is
   explicitly lifted.
5. Coordinate all ThreadKeeper work with draft PR #1 and require a concrete
   failing fixture or review finding.

## First post-VM2 non-live gate

Freeze one report-only Protomega2 Iter-loop contract containing:

- an accepted VM2 deployment-evidence digest and exact runtime identity;
- one bounded input, immutable request/origin ID, and fixed candidate actions;
- read-only memory evidence IDs with source and snapshot digests;
- explicit appraisal output separated from selection output;
- one forbidden action and one ambiguity case that must abstain;
- bounded iteration/tool budgets, rollback identity, and effect `none`;
- a negative fixture each for deployment drift, foreign completion, duplicate
  completion, memory-evidence drift, forbidden-action selection, and missing
  appraisal provenance.

Acceptance is deterministic replay with no skill loading, task claim, memory
write, provider call, Telegram access, supervisor launch, or ThreadKeeper
change. Passing it may support a later staging proposal; it does not authorize
one.

## Snapshot checks

Run from the repository root:

```sh
test -f projects/omegaclaw/GGB_CAPACITIES_ROADMAP.md
test -f projects/omegaclaw/GGB_DECISION_FRONTIER.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260811-heldout-decision-receipt-contract/RUN.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/RUN.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260814-petta-chem-structural-transfer-prereg/RUN.md
test -f projects/omegaclaw/experiments/20260816T072000Z-protomega-deterministic-delayed-live-fixture/RUN.md
git diff --check -- projects/omegaclaw/GGB_FRONTIER_20260816.md
```
