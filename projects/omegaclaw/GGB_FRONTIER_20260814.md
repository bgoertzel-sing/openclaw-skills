# GGB empirical frontier — 2026-08-14

Purpose: a concise, current execution view over the longer
`GGB_CAPACITIES_ROADMAP.md`. This is a planning artifact only; it grants no
runtime, provider, Telegram, memory-write, ThreadKeeper PR #1, or held-out
reveal authority.

## Capacity-to-work map

| Lane | GGB capacities | Existing anchor | Current empirical gate | Next small task | State |
|---|---|---|---|---|---|
| Request → bounded contract | 1.1, 2.1, 2.2, 3.1, 5.3, 5.4 | Project records and the zero-effect request classifier | `artifacts/ggb-capacity-gates/20260811-heldout-decision-receipt-contract/` | After Ben explicitly authorizes D1, bind that exact source decision in a receipt; only then build a separate one-shot A09–A12 runner | blocked on decision |
| Memory → appraisal → motivation | 1.2, 2.2, 2.5, 4.3, 5.5 | `petta-memory` handoff cache, GoalChainer heuristic PLN/deontic pipeline, MetaMo score-policy work | `artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/` | After Ben explicitly authorizes D2, bind the exact source decision before any deterministic 64/32 materializer | blocked on decision |
| Delegation and durable work | 1.3, 3.2, 3.3, 4.1, 4.5, 5.2 | ThreadKeeper draft PR #1 and persistent-worker records | PR #1 safety-floor ancestry plus the archived provider-free worker gates | Coordinate review/update posture; do not add another parser micro-gate without a concrete failing fixture | wait / coordinate |
| Scientific reasoning | 2.3, 4.4, 5.2, 5.4 | `petta-chem` run contracts and completed exp07 rich-pool records | `artifacts/ggb-capacity-gates/20260814-petta-chem-structural-transfer-prereg/` freezes cohort, metric, threshold, shuffled control, and claim boundary | After the Omega-recovery priority pause ends, build a read-only digest-bound evaluator; do not touch incomplete graph-seed-1003 or the shared PeTTa tree | preregistered; evaluation paused |
| Conversation and cross-system behavior | 1.5, 2.4, 3.1, 3.4, 4.2, 5.1, 5.2 | OmegaClaw transports, three-bot Iter schema, conversational-memory validator, preserved/re-embedded Protomega memory | `experiments/20260814T205300Z-protomega-history-byte-threshold/` failed acceptance: identical 4,346-byte input disagreed, and seven corrected reruns crashed at both 4,201- and 4,396-byte controls | Instrument one disposable 4,201-byte replay to timestamp turn ACK, history serialization, SWI/Janus evaluation return, and teardown; report only | NO-GO; threshold hypothesis rejected |

## Near-term order

1. Preserve the completed scientific-reasoning preregistration. Evaluation is
   paused with `petta-chem`; a later evaluator must be read-only and digest-bound.
2. Preserve the D1 and D2 decision seams without fabricating approval.
3. Instrument the production-free conversational-loop lifecycle at the now-
   failing 4,201-byte control; do not resume canaries or cutover.
4. Resume ThreadKeeper implementation only from a concrete PR #1 review
   finding or failing fixture.

## Gate for the next worker

After the explicit `petta-chem` priority pause is lifted, create a read-only
evaluator for the frozen structural-transfer preregistration with:

- SHA-256 bindings for all three frozen source files;
- exact extraction of full-cycle and full-cycle-ablation RAF-positive counts;
- the already frozen per-arm drop threshold and shuffled positive control;
- a replay command that uses no network, paid compute, or PeTTa execution;
- separate observation, inference, and excluded-claim fields.

Acceptance is limited to evidence that the selected structural statistic
transfers across the preregistered local runs. It must not claim general
chemical emergence, modify `petta-chem`, fit a model, write memory, dispatch a
worker, or affect any Omega runtime.

## Snapshot checks

Run from the repository root:

```sh
test -f projects/omegaclaw/GGB_CAPACITIES_ROADMAP.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260811-heldout-decision-receipt-contract/RUN.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/RUN.md
test -f projects/omegaclaw/artifacts/ggb-capacity-gates/20260814-post-recovery-canary-admission/RUN.md
test -d projects/petta-chem
git diff --check -- projects/omegaclaw/GGB_FRONTIER_20260814.md
```
