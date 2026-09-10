# E1 Guarded Homotopy Protocol

- Status: `smoke_implemented_acceptance_not_frozen`
- Date: `2026-07-23`
- Programme source:
  `../../../library/revised-epc-experimental-programme-2026/SOURCE.md`
- Historical R8 design commit:
  `9ccb151cc396dc73ce9c4ba9b2c9eb63de88d543`
- Historical R8 completed-run commit:
  `ecf2f79db00365a3921152c19a06c1b54ee34771`
- Autonomous paid-compute authorization: `none`

## Question

On one frozen six-layer synthetic-grammar protocol, does a BP-anchored
geometric homotopy avoid the teacher-free fidelity loss, late-block update
concentration, and representation-rank collapse of direct ePC while preserving
the same task/data/model/optimizer exposure?

This protocol distinguishes that causal comparison from reproduction of the
historical R8 WikiText pathology.

## Experiment identities

### E1-SG: paired synthetic-grammar mechanism test

All primary arms share:

- the same frozen teacher identity;
- the same six-layer student architecture and initialization per seed;
- the same training examples and order per seed;
- the same tokenizer and factor schema;
- the same token and optimizer-update budget;
- the same evaluation examples;
- the same checkpoint milestones.

Required arms:

1. `bp_kd`: ordinary backpropagation distillation control;
2. `direct_epc`: direct fixed-depth/energy-monotone ePC pathology control;
3. `homotopy_epc`: geometric `T={1,2,4,...,Tmax}` with convergence holds,
   step subdivision, and divergence guard;
4. `homotopy_objective_control`: same schedule and exposure but with the
   local settled-target coupling ablated or replaced by the closest
   implementable ordinary-KD control.

The fourth arm separates benefit of the homotopy schedule from benefit of the
coupled local objective. Its exact parameterization must be fixed after a
reduced gradient/identity test and before calibration runs.

### R8-WT: historical pathology reproduction anchor

This is not pooled with E1-SG and cannot serve as its paired causal control.
It uses the archived R8 WikiText-103 protocol and final crash-fix commit
`ecf2f79`. It verifies that the retained late-block/collapse phenotype remains
reproducible under the historical data/model identity. If retained artifacts
and code checks are sufficient, do not spend compute merely to duplicate it.

## Factor and split contract

The current R9 generator defines four binary factors:

- `subj_num`;
- `obj_num`;
- `tense`;
- `negation`.

E1 code must read factor names/count from the frozen protocol and fail before
training if the generator, evaluator, and acceptance file disagree.

Split identities:

- `train`: excludes the frozen compositional combinations;
- `id_validation`: same combination support, disjoint lexical realizations;
- `compositional_shift`: frozen held-out combinations and disjoint lexical
  realizations;
- `intervention_probe`: paired examples differing in exactly one declared
  factor, with automated generator validation.

No split is regenerated after outcomes are inspected.

## Calibration and confirmation

Calibration and confirmation are disjoint.

- `calibration`: at least three seeds, used only to estimate numerical
  variability, guard multipliers, and storage/runtime.
- `confirmation`: at least five separately frozen seeds, used for the stated
  E1 disposition.

Seed lists and their derivation are stored in the versioned acceptance JSON
before any calibration run. Confirmation outcomes never modify bars. If a bar
must change, the current campaign is closed as exploratory and a new version
with new confirmation seeds is preregistered.

All A/B comparisons use identical seeds and sample orders. Inference/activity
RNGs are separate from data-order and evaluation RNGs.

## Settlement and locality contract

- Error tensors at each of six block outputs are the only inference leaves.
- Model weights are frozen throughout every settle and checked by before/after
  content hashes.
- `clamped` settlement may access the frozen teacher loss and is an oracle
  diagnostic.
- `teacher_free_ff` uses `epsilon=0`, performs no settle, and cannot import,
  hold, or call a teacher module.
- Any future teacher-free settle is E4, not E1.
- The implementation reports whether settlement uses global autograd through
  the downstream graph; block-local weight updates do not by themselves
  establish local settlement compute.

## Primary measurements

At every milestone and terminal state, report by seed and arm:

1. clamped prompt KL and task metric;
2. teacher-free feed-forward prompt KL and ID/CS task metrics;
3. pooled and per-block squared error/update-mass concentration curves;
4. top-1%, top-5%, and top-20% frontier depth histograms;
5. per-block participation-ratio effective rank for feed-forward and settled
   states;
6. per-block cosine and error-norm ratio;
7. per-factor counterfactual closure and spill;
8. wall clock, applied scalar updates, dense frontier-discovery work,
   activation/error storage, and peak memory.

The primary fidelity result is teacher-free. Clamped fidelity is only a ceiling.

## Provisional confirmatory gates

Final numerical values live only in
`configs/e1_homotopy_acceptance_v1.json`. Before confirmation:

- teacher-free homotopy fidelity must stay inside a calibration-derived bound
  frozen before confirmatory outcomes;
- no single block may hold more than the preregistered share of top-5% mass;
- each block's participation ratio must remain above the preregistered
  teacher-relative floor;
- homotopy must improve at least one collapse/frontier primary over
  `direct_epc` with a paired interval excluding the failure region, while
  remaining noninferior on teacher-free task fidelity;
- all operational invariants must pass for every launched run.

The provisional `50%` frontier and `0.8x` rank values from programme v1.0 are
not final until calibrated against constructed positive, direct-ePC pathology,
and shuffled/random controls.

## Required preflight tests

1. Frozen weights remain byte-identical through settlement.
2. Teacher-free evaluator fails if a teacher object is supplied or touched.
3. Same seed produces exact batches, initialization, and milestone hashes.
4. Paired arms consume identical training/evaluation identities.
5. Factor-schema mismatch fails before training.
6. Pooled error mass equals the sum of per-block mass within tolerance.
7. Frontier histograms recompute from persisted sufficient statistics.
8. Known-rank, late-block-collapse, uniform-frontier, and sparse-unstructured
   fixtures recover their intended diagnostics.
9. Guard-triggered runs retain artifacts and count among launched runs.
10. Reduced CPU smoke produces finite JSONL, immutable config hashes, and
    deterministic artifact hashes.

## Resource gate

Before any paid run, a reduced smoke records:

- bytes per stored probe example by artifact class;
- projected full E1-SG storage;
- updates/second and settle evaluations/second;
- projected GPU type, hours, and cost for calibration and confirmation
  separately;
- stop conditions and artifact-return path.

No paid resource is currently authorized.

## Branches

- `E1-A homotopy clean`: teacher-free fidelity, depth distribution, and rank
  pass; advance whole-model E2.
- `E1-B pathology in slow motion`: fidelity passes but depth/rank fails;
  retain sidecar as the E2 substrate.
- `E1-C clamped only`: clamped passes and teacher-free fails; promote E4
  immediately and make no deployment claim.
- `E1-D no paired pathology`: `direct_epc` does not reproduce pathology on
  E1-SG; the data/regime changed the phenomenon, so E1 cannot attribute a
  homotopy rescue. Report the regime interaction and redesign before E2.

## Evidence paths

- Implementation branch: `agent/e1-guarded-homotopy`, commit `dd1a6e9`
- Implementation worktree:
  `../../relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`
- Machine-readable acceptance: `../configs/e1_homotopy_acceptance_v1.json`
- Reduced smoke ledger:
  `../experiments/20260724T001351Z-e1-homotopy-smoke-complete/RUN.md`
- Full campaign: requires a separate approved ledger
