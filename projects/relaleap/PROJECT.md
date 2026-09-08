# RelaLeap SLT Residual-Layer Causal Factors

- Slug: `relaleap`
- Status: `active` (HDPC/ePC Tiny Shakespeare prototype is current first track; SLT and columnar upgrades follow)
- Created: `2026-07-03`
- Last reviewed: `2026-08-18`
- Owner: Benjamin Goertzel

## Purpose

Develop and evaluate adaptive residual-layer learning methods for transformer failure modes. The current first track is an **HDPC/ePC Tiny Shakespeare prototype**: test homotopy-distilled predictive-coding learners and identity-initialized PC crowns as ongoing-learning mechanisms. If this technical track works, later upgrades should add (1) SLT inputs to the process and (2) columnar models for the residual layer.

## Success criteria

- A preregistered train-time design exists with hypothesis, architecture, training procedure, synthetic ground-truth plan, causal audit gates, null controls, and fail-closed criteria.
- Later implementation recovers expected behavior on synthetic regimes: `exact_factorized`, `shared_core_redundant`, `synergistic_pair`, `low_rank_trap`, `oblique_dictionary`, and `random_null`.
- Any promoted residual factorization beats matched flat/SVD/dense controls, beats dependency-aware nulls, passes exact ablation and commutator gates, and shows sparse interpretable LLC interaction structure.
- Reports distinguish prediction, reconstruction, causal modularity, and SLT/free-energy evidence instead of collapsing them into one handcrafted score.
- SLT evidence is considered meaningful only after calibrated finite-sample WBIC/SGLD proxy estimation over actual trained parameter blocks, with sampler diagnostics, explicit WBIC temperature accounting, MAP-reference validation, gauge policy checks, sample-size sensitivity, interaction/null normalization, and finite-sample caveats.

## Scope

### In scope

- Local design and preregistration under `projects/relaleap/`.
- SLT estimator validation package: SGLD/WBIC core, analytic calibration registry, sample-size sweeps, MAP/prior checks, gauge canonicalization, interaction protocols, RelaLeap-shaped benchmarks, nulls, minibatch/preconditioning diagnostics, reporting/CI gates, integration orchestrator, and adversarial reviewer.
- Synthetic ground-truth regimes with known causal structure.
- Train-time residual-column learners with identity initialization, sparse supports, SLT-informed regularizers, and auditable split/merge/transfer events.
- Causal audits: exact ablation calibration, pair synergy, support regret, commutator leakage, off-support leakage, and LLC interaction information.
- Fail-closed decision criteria and null controls.
- Tiny Shakespeare corpus as the first real-text validation target for SLT estimators.
- Tiny Shakespeare corpus as the first HDPC/ePC homotopy-distillation and PC-crown validation target.
- Bounded Runpod GPU execution for HDPC/ePC only after explicit resource/time/cost approval and a remote-job record.

### Out of scope for now

- Unapproved paid or remote compute.
- Pushing branches or opening PRs.
- Claiming real transformer causal columns before synthetic and audit gates pass.

## Current state

At `2026-08-21T02:43Z`, no admissible Stage-A unblock input newer than the
00:43 UTC receipt appeared. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260821T024300Z-frame-oracle-v14-quiescent-receipt-20260820-r87/`.

At `2026-08-21T00:43Z`, no admissible Stage-A unblock input newer than the
22:42 UTC receipt was present (only `__pycache__` bytecode caches, pruned).
Frozen contract and clean `8108d98` identity matched; 30 focused plus 357
broader exposed tests passed; sealed contents were not read. Stage A remains
blocked and v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260821T004300Z-frame-oracle-v14-quiescent-receipt-20260820-r86/`.

At `2026-08-20T22:42Z`, no admissible Stage-A unblock input newer than the
20:38 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T224200Z-frame-oracle-v14-quiescent-receipt-20260820-r85/`.

At `2026-08-20T20:38Z`, no admissible Stage-A unblock input newer than the
18:38 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T203800Z-frame-oracle-v14-quiescent-receipt-20260819-r84/`.

At `2026-08-20T18:38Z`, no admissible Stage-A unblock input newer than the
16:05 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T183800Z-frame-oracle-v14-quiescent-receipt-20260819-r83/`.

At `2026-08-20T16:05Z`, no admissible Stage-A unblock input newer than the
14:05 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T160500Z-frame-oracle-v14-quiescent-receipt-20260819-r82/`.

At `2026-08-20T14:05Z`, no admissible Stage-A unblock input newer than the
12:04 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T140500Z-frame-oracle-v14-quiescent-receipt-20260819-r81/`.

At `2026-08-20T12:04Z`, no admissible Stage-A unblock input newer than the
10:03 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T120400Z-frame-oracle-v14-quiescent-receipt-20260819-r80/`.

At `2026-08-20T10:03Z`, no admissible Stage-A unblock input newer than the
08:03 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T100300Z-frame-oracle-v14-quiescent-receipt-20260819-r79/`.

At `2026-08-20T08:03Z`, no admissible Stage-A unblock input newer than the
09:01 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T080300Z-frame-oracle-v14-quiescent-receipt-20260819-r78/`.

At `2026-08-20T06:01Z`, no admissible Stage-A unblock input newer than the
03:58 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T060100Z-frame-oracle-v14-quiescent-receipt-20260819-r76/`.

At `2026-08-20T03:58Z`, no admissible Stage-A unblock input newer than the
01:53 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T035800Z-frame-oracle-v14-quiescent-receipt-20260819-r75/`.

At `2026-08-20T01:53Z`, no admissible Stage-A unblock input newer than the
01:26 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260820T015300Z-frame-oracle-v14-quiescent-receipt-20260819-r74/`.

At `2026-08-19T23:53Z`, no admissible Stage-A unblock input newer than the
21:53 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T235300Z-frame-oracle-v14-quiescent-receipt-20260819-r72/`.

At `2026-08-19T21:53Z`, no admissible Stage-A unblock input newer than the
19:53 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T215300Z-frame-oracle-v14-quiescent-receipt-20260819-r71/`.

At `2026-08-19T19:53Z`, no admissible Stage-A unblock input newer than the
17:49 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T195300Z-frame-oracle-v14-quiescent-receipt-20260819-r70/`.

At `2026-08-19T17:49Z`, no admissible Stage-A unblock input newer than the
15:52 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T174900Z-frame-oracle-v14-quiescent-receipt-20260819-r69/`.

At `2026-08-19T15:52Z`, no admissible Stage-A unblock input newer than the
05:32 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T155100Z-frame-oracle-v14-quiescent-receipt-20260819-r68/`.

At `2026-08-19T05:32Z`, no admissible Stage-A unblock input newer than the
03:32 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T052900Z-frame-oracle-v14-quiescent-receipt-20260818-r67/`.

At `2026-08-19T03:32Z`, no admissible Stage-A unblock input newer than the
01:29 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T032900Z-frame-oracle-v14-quiescent-receipt-20260818-r66/`.

At `2026-08-19T01:29Z`, no admissible Stage-A unblock input newer than the
23:29 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260819T012700Z-frame-oracle-v14-quiescent-receipt-20260818-r65/`.

At `2026-08-18T23:29Z`, no admissible Stage-A unblock input newer than the
21:29 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T232600Z-frame-oracle-v14-quiescent-receipt-20260818-r64/`.

At `2026-08-18T21:29Z`, no admissible Stage-A unblock input newer than the
19:27 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T212600Z-frame-oracle-v14-quiescent-receipt-20260818-r63/`.

At `2026-08-18T19:27Z`, no admissible Stage-A unblock input newer than the
17:23 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T192300Z-frame-oracle-v14-quiescent-receipt-20260818-r62/`.

At `2026-08-18T17:23Z`, no admissible Stage-A unblock input newer than the
15:15 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T172000Z-frame-oracle-v14-quiescent-receipt-20260818-r61/`.

At `2026-08-18T15:15Z`, no admissible Stage-A unblock input newer than the
13:15 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T151400Z-frame-oracle-v14-quiescent-receipt-20260818-r60/`.

At `2026-08-18T13:15Z`, no admissible Stage-A unblock input newer than the
11:15 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T131400Z-frame-oracle-v14-quiescent-receipt-20260818-r59/`.

At `2026-08-18T11:15Z`, no admissible Stage-A unblock input newer than the
09:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T111400Z-frame-oracle-v14-quiescent-receipt-20260818-r58/`.

At `2026-08-18T09:16Z`, no admissible Stage-A unblock input newer than the
07:17 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T091530Z-frame-oracle-v14-quiescent-receipt-20260818-r57/`.

At `2026-08-18T07:17Z`, no admissible Stage-A unblock input newer than the
05:17 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T071538Z-frame-oracle-v14-quiescent-receipt-20260818-r56/`.

At `2026-08-18T05:17Z`, no admissible Stage-A unblock input newer than the
03:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T051535Z-frame-oracle-v14-quiescent-receipt-20260817-r55/`.

At `2026-08-18T03:16Z`, no admissible Stage-A unblock input newer than the
01:17 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T031533Z-frame-oracle-v14-quiescent-receipt-20260817-r54/`.

At `2026-08-18T01:17Z`, no admissible Stage-A unblock input newer than the
23:17 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260818T011541Z-frame-oracle-v14-quiescent-receipt-20260817-r53/`.

At `2026-08-17T23:17Z`, no admissible Stage-A unblock input newer than the
21:17 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T231541Z-frame-oracle-v14-quiescent-receipt-20260817-r52/`.

At `2026-08-17T21:17Z`, no admissible Stage-A unblock input newer than the
19:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T211535Z-frame-oracle-v14-quiescent-receipt-20260817-r51/`.

At `2026-08-17T19:16Z`, no admissible Stage-A unblock input newer than the
17:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T191524Z-frame-oracle-v14-quiescent-receipt-20260817-r50/`.

At `2026-08-17T17:16Z`, no admissible Stage-A unblock input newer than the
15:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T171530Z-frame-oracle-v14-quiescent-receipt-20260817-r49/`.

At `2026-08-17T15:16Z`, no admissible Stage-A unblock input newer than the
13:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T151528Z-frame-oracle-v14-quiescent-receipt-20260817-r48/`.

At `2026-08-17T13:16Z`, no admissible Stage-A unblock input newer than the
11:16 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T131533Z-frame-oracle-v14-quiescent-receipt-20260817-r47/`.

At `2026-08-17T11:16Z`, no admissible Stage-A unblock input newer than the
09:12 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T111510Z-frame-oracle-v14-quiescent-receipt-20260817-r46/`.

At `2026-08-17T09:12Z`, no admissible Stage-A unblock input newer than the
07:02 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T091054Z-frame-oracle-v14-quiescent-receipt-20260817-r45/`.

At `2026-08-17T07:02Z`, no admissible Stage-A unblock input newer than the
05:00 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T070051Z-frame-oracle-v14-quiescent-receipt-20260817-r44/`.

At `2026-08-17T05:00Z`, no admissible Stage-A unblock input newer than the
02:58 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T045843Z-frame-oracle-v14-quiescent-receipt-20260816-r43/`.

At `2026-08-17T02:58Z`, no admissible Stage-A unblock input newer than the
00:57 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T025632Z-frame-oracle-v14-quiescent-receipt-20260816-r42/`.

At `2026-08-17T00:57Z`, no admissible Stage-A unblock input newer than the
22:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260817T005536Z-frame-oracle-v14-quiescent-receipt-20260816-r41/`.

At `2026-08-16T22:56Z`, no admissible Stage-A unblock input newer than the
20:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T225533Z-frame-oracle-v14-quiescent-receipt-20260816-r40/`.

At `2026-08-16T20:56Z`, no admissible Stage-A unblock input newer than the
18:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T205540Z-frame-oracle-v14-quiescent-receipt-20260816-r39/`.

At `2026-08-16T18:56Z`, no admissible Stage-A unblock input newer than the
16:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T185530Z-frame-oracle-v14-quiescent-receipt-20260816-r38/`.

At `2026-08-16T16:56Z`, no admissible Stage-A unblock input newer than the
14:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T165454Z-frame-oracle-v14-quiescent-receipt-20260816-r37/`.

At `2026-08-16T14:56Z`, no admissible Stage-A unblock input newer than the
12:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T145457Z-frame-oracle-v14-quiescent-receipt-20260816-r36/`.

At `2026-08-16T12:56Z`, no admissible Stage-A unblock input newer than the
10:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T125453Z-frame-oracle-v14-quiescent-receipt-20260816-r35/`.

At `2026-08-16T10:56Z`, no admissible Stage-A unblock input newer than the
08:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T105400Z-frame-oracle-v14-quiescent-receipt-20260816-r34/`.

At `2026-08-16T08:56Z`, no admissible Stage-A unblock input newer than the
06:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T085400Z-frame-oracle-v14-quiescent-receipt-20260816-r33/`.

At `2026-08-16T06:56Z`, no admissible Stage-A unblock input newer than the
04:56 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T065300Z-frame-oracle-v14-quiescent-receipt-20260815-r32/`.

At `2026-08-16T04:56Z`, no admissible Stage-A unblock input newer than the
02:55 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T045300Z-frame-oracle-v14-quiescent-receipt-20260815-r31/`.

At `2026-08-16T02:55Z`, no admissible Stage-A unblock input newer than the
00:55 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T025300Z-frame-oracle-v14-quiescent-receipt-20260815-r30/`.

At `2026-08-16T00:55Z`, no admissible Stage-A unblock input newer than the
22:55 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260816T005300Z-frame-oracle-v14-quiescent-receipt-20260815-r29/`.

At `2026-08-15T22:55Z`, no admissible Stage-A unblock input newer than the
20:55 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260815T225300Z-frame-oracle-v14-quiescent-receipt-20260815-r28/`.

At `2026-08-15T20:55Z`, no admissible Stage-A unblock input newer than the
18:55 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260815T205300Z-frame-oracle-v14-quiescent-receipt-20260815-r27/`.

At `2026-08-15T18:55Z`, no admissible Stage-A unblock input newer than the
16:53 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260815T185300Z-frame-oracle-v14-quiescent-receipt-20260815-r26/`.

At `2026-08-15T16:53Z`, no admissible Stage-A unblock input newer than the
14:54 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260815T165100Z-frame-oracle-v14-quiescent-receipt-20260815-r25/`.

At `2026-08-15T14:54Z`, no admissible Stage-A unblock input newer than the
12:54 UTC receipt was present. Frozen contract and clean `8108d98` identity
matched; 30 focused plus 357 broader exposed tests passed; sealed contents
were not read. Stage A remains blocked and v14 remains sealed, unopened, and
unconsumed. Evidence:
`experiments/20260815T145100Z-frame-oracle-v14-quiescent-receipt-20260815-r24/`.

At `2026-08-15T12:54Z`, no admissible Stage-A unblock input newer than the
08-14 10:19 UTC receipt was present. Frozen contract and clean `8108d98`
identity matched; 30 focused plus 357 broader exposed tests passed; sealed
contents were not read. Stage A remains blocked and v14 remains sealed,
unopened, and unconsumed. Evidence:
`experiments/20260815T125100Z-frame-oracle-v14-quiescent-receipt-20260815-r23/`.

At `2026-08-14T10:19Z`, the recurring semantics worker found no admissible
Stage-A unblock input newer than the 08:13 UTC receipt. The contract hash and
clean `8108d98` identity matched; 30 focused plus 357 broader exposed tests
passed, and sealed contents were not read. This is an administrative scheduler
receipt, not a new scientific revalidation or permission to create cases.
Stage A remains blocked and v14 remains sealed, unopened, and unconsumed.
Evidence:
`experiments/20260814T101814Z-frame-oracle-v14-quiescent-receipt-20260814-r22/`.

At `2026-08-09T15:46Z`, a recurring scheduler activation was dispositioned
under the frozen contract rather than treated as a scientific unblock event.
The contract explicitly says scheduler recurrence is not approval; no new
admissible input was found, and clean `8108d98` passed 30 focused plus 357
broader exposed tests. R1 preserves a harness-only wording mismatch; r2
passed. No further periodic blocked-state runs should be created solely from
scheduler recurrence. Stage A remains blocked and v14 sealed, unopened, and
unconsumed. Evidence:
`experiments/20260809T154543Z-frame-oracle-v14-quiescent-activation-disposition-r2/`.

At `2026-08-09T13:32Z`, a provider-free blocked-state revalidation found no
post-contract project input constituting an admissible Stage-A unblock event.
The contract hash and clean `8108d98` identity matched, sealed directory
contents were not read, and 30 focused plus 357 broader exposed tests passed.
Stage A remains blocked; v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T133055Z-frame-oracle-v14-blocked-state-revalidation/`.

At `2026-08-09T11:31Z`, the terminal transport counterexample was converted
into a fail-closed Stage-A unblock contract. Only an external conforming
independent-author bundle, a result-independent fresh topology proposal that
first passes a model-free preflight, or an explicit Ben-approved protocol
revision may unblock Stage A. R1 and r2 preserve harness-only failures; r3
passed 30 focused and 357 broader exposed tests at clean `8108d98`. No model,
fixture, sealed input, or semantic evaluation was used. V14 remains sealed,
unopened, and unconsumed. Evidence:
`experiments/20260809T113028Z-frame-oracle-v14-stage-a-unblock-contract-r3/`.

At `2026-08-09T09:31Z`, the exact model-free transport preflight adjudicated
`TRANSPORT_INFEASIBLE`: inside the frozen unprivileged, network-unshared
Bubblewrap topology, loopback setup failed with `RTNETLINK answers: Operation
not permitted` before server launch, bind, client launch, request, or response.
No repair or alternate topology was attempted. Clean `8108d98` passed 30
focused and 357 broader exposed tests. Stage A remains blocked and v14 remains
sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T093000Z-frame-oracle-v14-transport-feasibility-execution/`.

At `2026-08-09T07:30Z`, a model-free transport-feasibility preflight contract
was frozen for any future readiness attempt. It requires the intended isolated
topology to prove loopback, inert HTTP exchange, denials, and teardown before
a new one-use model probe may be preregistered. It mounts no model or semantic
input and authorizes no inference. R1 preserved a line-spanning harness-only
failure; r2 passed 30 focused and 357 broader exposed tests. Stage A remains
blocked and v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T072900Z-frame-oracle-v14-transport-feasibility-contract-r2/`.

At `2026-08-09T05:25Z`, the sole preregistered model-readiness probe was
consumed as terminal `NOT_READY` before server launch: the frozen
network-unshared Bubblewrap namespace could not raise loopback
(`RTNETLINK answers: Operation not permitted`). Therefore zero model loads,
HTTP requests, or responses occurred. Repair/retry is forbidden. Clean
`8108d98` passed 30 focused and 357 broader exposed tests; the first broader
wrapper's quoted-glob failure is preserved. Stage A remains blocked and v14
remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T052300Z-frame-oracle-v14-readiness-probe-execution/`.

At `2026-08-09T03:28Z`, the gate's sole allowed model-readiness probe was
preregistered without execution. Exact 133-byte request SHA-256
`60b30c2d...f950`, endpoint, timeouts, response bound, isolation/denial
requirements, loaded-model receipts, exact `READY7K2` adjudication, and
teardown are immutable. R1 preserved a line-spanning harness-only failure; r2
passed 30 focused and 357 broader exposed tests. No inference, model request,
fixture, randomness, or sealed access occurred. Stage A remains blocked and
v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T032700Z-frame-oracle-v14-readiness-probe-preregistration-r2/`.

At `2026-08-09T01:25Z`, a binary no-fixture model readiness gate was frozen
without invoking the model. It permits at most one separately preregistered
ASCII-sentinel probe with no Stage-A inputs and requires exact load identity,
one request/response, bounded output, complete isolation receipts, teardown,
and fail-closed adjudication. Clean `8108d98` passed 30 focused and 357 broader
exposed tests. No inference, fixture, randomness, or sealed access occurred.
Stage A remains blocked; v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260809T012300Z-frame-oracle-v14-model-readiness-contract/`.

At `2026-08-08T23:27Z`, the Stage-A noninteractive author I/O contract was
hash-frozen with exactly one request, one response, atomic manifest-last bundle
creation, an exact success-state sequence, and irreversible retirement on any
protocol failure. It contains no fixture prompt, example, or derivation logic.
Clean `8108d98` passed 30 focused and 357 broader exposed tests; r1's
line-spanning harness assertion is preserved and r2 changed only that check.
No model request, model load, randomness, fixture, or sealed access occurred.
Stage A remains blocked pending a separate no-fixture model-load/generation
readiness decision; v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T232600Z-frame-oracle-v14-author-io-contract-r2/`.

At `2026-08-08T21:27Z`, exact hash-pinned Ollama and `llama-server` passed
combined startup/device discovery inside one cleared, network-unshared
Bubblewrap namespace with a 22-entry hashed closure. No API request, model
load, or fixture input was used; clean `8108d98` passed 30 focused and 357
broader exposed tests. R1's escaped-glob harness failure is preserved; r2
changed only that argument. This proves combined discovery, not model-load or
independent-author eligibility, so Stage A remains blocked and v14 remains
sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T212629Z-frame-oracle-v14-combined-runtime-discovery-r2/`.

At `2026-08-08T19:25Z`, hash-pinned `llama-server` and its 13 direct dynamic
dependencies passed isolated `--help` with a cleared environment, unshared
network, and zero model files mounted. Clean `8108d98` passed 30 focused and
357 broader exposed tests. R1's private-library mount-layout failure is
preserved; r2 corrected only targets. This establishes runner availability,
not model-load closure or independent author eligibility, so Stage A remains
blocked. V14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T192443Z-frame-oracle-v14-runner-isolated-availability-r2/`.

At `2026-08-08T17:24Z`, a bounded no-inference search found the previously
unmounted local runner at `/home/openclaw/.local/lib/ollama/llama-server` and
froze its SHA-256 as `dbfeea38...40037`. Clean `8108d98` passed 30 focused and
357 broader exposed tests. This identifies the runner file but does not yet
freeze its required-library closure or prove isolated availability, so Stage A
remains blocked. V14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T172358Z-frame-oracle-v14-runner-closure-probe/`.

At `2026-08-08T15:27Z`, the exact hash-pinned Ollama/Qwen control server
started inside a cleared, network-unshared Bubblewrap namespace with the exact
model closure and four frozen Stage-A inputs. No API request or model load was
made; 30 focused and 357 broader exposed tests passed. The startup receipt also
showed the required `llama-server` inference runner was absent from the mounted
runtime, so final author eligibility remains unestablished and Stage A remains
blocked. V14 is sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T152658Z-frame-oracle-v14-runtime-closure-launch-receipt-r3/`.

At `2026-08-08T11:20Z`, the missing independent-author boundary was reduced to
a binary pre-launch eligibility contract: immutable executable/runtime hashes,
fresh state, independently existing general authoring machinery, exact input
isolation, and trusted outer receipts are mandatory; self-attestation and
worker-authored fixture logic fail closed. No author or fixture was invoked.
V14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T112000Z-frame-oracle-v14-author-eligibility-contract/`.

At `2026-08-08T09:17Z`, the blocked independent-author handoff was narrowed to
a frozen, non-disclosing Stage-A output-bundle schema. It requires exact file
membership, provenance/denial receipts, executable identity, four-predicate
coverage, premise results, immutable hashes, and fail-closed retirement. Clean
`8108d98` passed 30 focused and 357 broader exposed tests. No fixture or
randomness was created; v14 remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T091730Z-frame-oracle-v14-stage-a-bundle-schema-r3/`.

At `2026-08-08T07:15Z`, the Stage-A author boundary was audited and failed
closed: Bubblewrap can restrict readable files, but a subprocess whose fixture
logic is supplied by this history-exposed persistent worker is not an
independent author. Clean `8108d98` passed 30 focused and 225 exposed tests.
No fixture, randomness, candidate, sealed artifact, oracle call, or semantic
evaluation occurred. An independent-author handoff contract is frozen; v14
remains sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T071540Z-frame-oracle-v14-stage-a-author-boundary-audit/`.

At `2026-08-08T05:17Z`, a provider-free Bubblewrap probe mechanically exposed
exactly the four frozen Stage-A inputs, verified every input hash, unshared the
network, and made project history, experiments, sealed material, and candidate
tests absent. Two setup failures (wrong source path; wrong manifest cwd) are
preserved, and r3 passed. Clean `8108d98` then passed 30 focused and 225
exposed tests. No fixture or randomness was created; this verifies only the
isolation primitive, not author independence. V14 remains sealed, unopened,
and unconsumed. Evidence:
`experiments/20260808T051702Z-frame-oracle-v14-stage-a-isolation-probe-r3/`.

At `2026-08-08T03:14Z`, Stage A failed closed before fixture authoring because
the persistent worker's mandatory project-history audit exposes details of
retired v14 fixture attempts, contradicting the frozen no-prior-visibility
rule. A separate mechanically input-isolated execution contract is now frozen.
Clean `8108d98` passed 30 focused and 225 exposed tests. V14 remains sealed,
unopened, and unconsumed. Next is Stage A only in a fresh restricted process
with a complete readable-input manifest and denial receipts. Evidence:
`experiments/20260808T031441Z-frame-oracle-v14-stage-a-contamination-audit/`.

At `2026-08-08T01:18Z`, a fresh two-stage v14 fixture-provenance protocol was
frozen without authoring cases. It limits Stage-A inputs to the finite contract,
clean v13 normalizer/test, the protocol, and a post-boundary OS-random receipt;
it excludes every candidate, failed fixture run, and sealed/opened artifact,
and freezes fixtures before candidate visibility. Clean `8108d98` passed 30
focused and 225 exposed tests. Next is Stage A in a fresh turn. V14 remains
sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T011300Z-frame-oracle-v14-fixture-provenance-protocol/`.

At `2026-08-07T23:19Z`, the attempted independent v14 acceptance fixture run
failed closed on provenance. Its mechanics passed 4/4 clean-v13 acceptance,
4/4 frozen-contract rejection, 4/4 confidence preservation, 30 focused, and
225 exposed tests, but the turn inspected unadmitted v14 candidate tests before
fixture authoring. The cases are therefore exposed and inadmissible as
independent evidence. Candidate code remains unadmitted. V14 remains sealed,
unopened, and unconsumed. Next is a fresh input-allowlisted fixture-generation
process excluding this run and all v14 candidate source/tests. Evidence:
`experiments/20260807T231100Z-frame-oracle-v14-independent-acceptance-fixtures/`.

At `2026-08-07T21:18Z`, the first v14 relation-bearing implementation attempt
failed closed at the fresh focused-fixture gate: 11/13 passed, but v13 already
rejected two proposed predecessor-acceptance fixtures, falsifying the frozen
fixture premise. No broader tests ran; candidate code remains uncommitted and
unadmitted in an isolated worktree. This does not falsify the finite contract.
V14 remains sealed, unopened, and unconsumed. Next is a separately
preregistered independent acceptance fixture set. Evidence:
`experiments/20260807T211100Z-frame-oracle-v14-relation-bearing-implementation/`.

At `2026-08-07T19:18Z`, the finite v14 predecessor relation-bearing contract
was frozen without accessing v14. After v13 accepts, every non-unknown proposal
must exactly equal the inherited v10 predicate-specific whole-sentence overt
template and canonical slots; otherwise it fails closed with preserved
confidence. Fresh implementation-fixture classes are preregistered, but no
implementation, runner change, inference, labels, readout, substitution
evaluation, or semantic loss occurred. Clean `8108d98` passed 30 focused and
225 exposed v1--v13 tests. V14 remains sealed, unopened, and unconsumed. Next
is a separate clean implementation turn. Evidence:
`experiments/20260807T191100Z-frame-oracle-v14-relation-bearing-contract/`.

At `2026-08-07T17:15Z`, a fresh source-only audit reproduced a v13 acceptance
gap without accessing v14: four relationless fragments spanning every
non-unknown predicate remained non-unknown when one unrelated ASCII residue
`x` survived slot masking. All matched declarative-control semantic keys and
preserved confidence. Clean `8108d98` passed 48 focused, 359 exposed, and 527
pinned tests with 5 skips. V14 remains sealed, unopened, and unconsumed;
execution is blocked until a fresh finite predicate-specific relation-bearing
remainder contract is frozen using fresh fixtures. No downstream semantic
stage is admitted. Evidence:
`experiments/20260807T171100Z-frame-oracle-v14-source-behavior-audit/`.

At `2026-08-07T15:20Z`, v14 was freshly process-sealed from only the inherited
closed ontology and coverage contract. Integrity accepted 24 aligned unique
cases, exact 4/6/5/1/4/4 strata, all five predicates, exactly five `located_in`
frames, `opened=false`, and zero exact sentence overlap against exposed
batteries through v13 plus offline-readout-v1. The clean v13 regression
worktree passed 225 focused and 527 pinned tests with 5 skips. V13 remains
permanently consumed negative evidence; v14 is unopened and unconsumed.
Labels, readout, substitution evaluation, and semantic loss remain blocked.
Next is at most one fresh bounded source-derived v14 behavior audit using
independent fixtures without accessing v14 answers. Evidence:
`experiments/20260807T151100Z-frame-oracle-v14-sealed-contract-r2/`.

At `2026-08-07T05:31Z`, a fresh preregistered source-only audit reproduced a
bounded v13 eligibility gap at unchanged clean v12 commit `228ff13`: all four
independent punctuation-separated slot-only fragments survived as non-unknown
with the same semantic keys as matched declarative controls. Their masked
remainders contained no ASCII letters, while every control retained one. At
that stage the finite letterless-remainder rule was frozen but unimplemented;
50 focused, 311 exposed, 479 pinned plus 5 skipped, and 502 host tests passed.
The later implementation status above supersedes that open loop. Evidence:
`experiments/20260807T052500Z-frame-oracle-v13-fragment-source-audit/` and
`docs/frame_oracle_v13_fragment_behavior_spec_20260807.md`.

At `2026-08-07T00:40Z`, the two C1 paid-attempt package-layout defects are
repaired locally at commit `2687010`. The C1 command builder now verifies the
composed extracted bootstrap/command/handoff/source layout before packaging,
and a structural extracted bootstrap execution proves its self-relative capture
path without installing packages or touching provider/science paths. The
focused package/preflight suite passes 25/25. Historical tests that reference
superseded worker tars remain fail-closed; the next remote activation must use
a fresh coherent package and fresh explicit resource/cost approval. Evidence:
`experiments/20260807T004002Z-epc-c1-composed-layout-repair/`.


At `2026-08-06T00:36Z`, the current cron payload again retained only the exact
US-West proposal, the exclusive writer lock admitted the activation, and all
14 original envelope hashes passed. Runpod health checks passed and A40 pricing
remained `$0.44/GPU-hour`, but all six approved US-West centers still lacked
inventory; active pods and serverless endpoints were empty. No C1 resource,
science input, or new spend was opened, so Ben's exact approval remains
unconsumed and C1-A is `BLOCKED_ENVIRONMENT`. Clean unowned commit `19bdbad`
remains preserved but unused; the approved handoff is still bound to `6a08771`.
Canada incident billing has settled at `$0.032451326376758516` for `260776` ms
and 50 GB billed disk. EU itemization remains pending, with the approximate
`$0.104` elapsed-time estimate retained. Evidence:
`experiments/20260806T003615Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r36/`,
`experiments/20260806T003645Z-epc-remediation-c1-runpod-capacity-recheck-r35/`,
`experiments/20260806T003725Z-epc-c1-unauthorized-canada-pod-billing-recheck-r2/`,
and `experiments/20260806T003730Z-epc-c1-unauthorized-eu-pod-billing-recheck/`.

At `00:40:12Z`, after the clean provider audit, a concurrent lifecycle writer
created pod `dnwq8koj3rtu45` with an “any-available” name and mutable image tag,
outside the current digest-pinned US-West envelope. It was not SSH-ready, had a
50 GB disposable disk and no network volume. The pod was deleted at `00:42:37Z`
before any remote/science command; repeat pod and endpoint lists were empty.
Billing remains pending, with a conservative approximately `$0.0177` estimate.
C1 is therefore additionally `BLOCKED_CONCURRENCY` until one lifecycle writer
is established. Evidence:
`experiments/20260806T004226Z-epc-c1-out-of-envelope-concurrent-pod-audit/`,
`experiments/20260806T004237Z-epc-c1-out-of-envelope-concurrent-pod-termination/`,
`experiments/20260806T004247Z-epc-c1-post-concurrent-pod-termination-provider-audit/`,
and `experiments/20260806T004305Z-epc-c1-out-of-envelope-concurrent-pod-billing/`.
The competing writer immediately repeated the action with EU-named pod
`elatgmvrthhxf7` at `00:44:05Z`, again using the mutable tag. It was deleted
before readiness at `00:45:38Z`; provider state was again empty. Its billing is
pending (approximately `$0.0187` provisional). This repetition makes the
single-writer blocker terminal for the activation. Evidence:
`experiments/20260806T004532Z-epc-c1-second-concurrent-pod-audit/`,
`experiments/20260806T004538Z-epc-c1-second-concurrent-pod-termination/`, and
`experiments/20260806T004552Z-epc-c1-post-second-concurrent-pod-provider-audit/`.

The persistent ePC remediation programme has completed A0, MG-1, and the
theorem-consistent MG-2R repair while preserving MG-2 as a failed contract.
Pinned
paper v5 and official code establish that EO/ePC optimizes independent error
variables through a recursive prediction-plus-error graph, whereas RelaLeap's
legacy routines differentiate and step detached hidden states and are therefore
the paper's SO/sPC parameterization. The r5 audit also found a concrete
instrument defect: negation occurred after the candidate minimum, selecting
the worst rather than best cap. The repaired evaluator passes uniform
`ln(64)`, untrained, planted-oracle, actual trainer-teacher round-trip, target
argmax, and perturbation-independence controls. Acceptance passed 7 tests from
clean commit `6bf9d01`; the preceding full suite passed 211 tests. MG-1 then
ported the pinned `PCE` error core and passed its float64 depths 2/6/12/24
identity gate from clean commit `d20e8c8`: every first-step error update exactly
matched its output adjoint, every earliest error received nonzero signal,
replay was bit-exact, and the legacy SO/sPC negative control moved only its
final hidden state. The full suite passed 213 tests. Evidence:
`experiments/20260805T002848Z-epc-remediation-a0-acceptance-r2/`,
`experiments/20260805T004556Z-epc-remediation-mg1-artifact-acceptance/`, and
`experiments/20260805T004613Z-epc-remediation-mg1-full-suite-clean/`. The MG-2
core is now frozen at commit `860e650` (spec SHA-256
`e6ae1f191156bf2b838b73ed1866b00a81ade9cd96ade3f373a61c428ac49dba`).
Its clean implementation at `beb3fe0` then produced a verified `FAILED_TEST`:
EO/ePC reached `rho<1e-8`, matched the exact analytic error equilibrium to
about `1e-8`, and replayed bit-exactly, but finite-`lambda=1e-3` local PC
gradients differed from feedforward BP by 0.24%--5.69%, not `1e-6`. A seed-free
scalar counterexample proves the frozen tolerance impossible at finite lambda,
consistent with paper Appendix C.4. MG-3 is inadmissible under the failed gate;
next is a separately frozen theorem-consistent MG-2 repair, without tuning the
opened science seed. Evidence:
`experiments/20260805T010748Z-epc-remediation-mg2-acceptance/`. MG-2R was
separately frozen at commit `c4af03b`, fresh seed `820260813`, and implemented
at clean commit `aea2263`. All 12 depth/lambda EO points settled and matched
exact error and local-gradient controls within `8.14e-9`; exact rescaled PC
gradients approached BP with adjacent-decade median ratios `9.72--10.00` and
minimum layer ratio `9.68`. Replay was bit-exact, the bounded legacy diagnostic
was correctly classified, and the clean full suite passed 217 tests. MG-2R is
`COMPLETE_VERIFIED`; finite-lambda MG-2 remains `FAILED_TEST`. MG-3 is now
independently frozen at commit `db51f50` (spec SHA-256
`e0d4b318440f314dc5353f60850bfb0d94a4a82caa02db78f58613fc4ec9907a`). It
requires active-variable gradient residuals, fail-closed `settled` versus
`partial-settle(rho)` labels, a separate `1e-4` census, and a seed-free
monotone-but-nonconverging regression. Its clean implementation at commit
`030b679` is now `COMPLETE_VERIFIED`: all analytic and adjacent-float boundary
controls passed, MLP/transformer/GPT-2/pc_step and MG-2/MG-2R records share the
immutable certificate, 11 downstream result builders were certified, all 12
MG-2R EO points entered the `1e-4` census, replay was bit-exact, and the full
suite passed 233 tests. MG-4 was independently frozen at clean commit
`4bb43ab` (spec SHA-256
`0789082eb050f3be09415fb9044fd8d995a5a6959f86f785bfa09c12b3c0470a`).
It defines matrix-free Jacobian products in actual active variables, four fixed
power starts for 20 iterations, a fail-closed numerical margin, analytic
stable/marginal/unstable/flat controls, and certificate propagation. Its clean
implementation at commit `9306d01` is now `COMPLETE_VERIFIED`: all exact
JVP/radius and named fail-closed controls passed, all six core engines and 11
downstream consumers carry the immutable certificate, and all 12 MG-2R EO
points preserve their MG-3 residuals while producing stabilized
`stable-conditioned` estimates from `0.4995` to `0.4999963102685592`.
Artifact replay was bit-exact, 25 focused tests and the complete 238-test suite
passed. This establishes local contractivity only for the declared tested
maps. MG-5 specification is next. Evidence:
`experiments/20260805T015749Z-epc-remediation-mg2r-acceptance/`,
`experiments/20260805T020812Z-epc-remediation-mg3-spec-freeze/`,
`experiments/20260805T023815Z-epc-remediation-mg3-acceptance/`,
`experiments/20260805T023930Z-epc-remediation-mg3-full-suite-clean/`,
`experiments/20260805T024551Z-epc-remediation-mg4-spec-freeze/`,
`experiments/20260805T032454Z-epc-remediation-mg4-acceptance-r2/`, and
`experiments/20260805T032800Z-epc-remediation-mg4-full-suite-clean-r2/`. MG-5
is now independently frozen at clean commit `d91ef2b` (r2 spec SHA-256
`4da0860a2d1ce76d4decc08672c0e248d63a270f78a9e91ba60b7dccb602bf59`).
It requires exhaustive exact-tensor observation at the trainer seam, strict
unique planted winners at all 512 scored positions, five named corruptions,
explicit non-planted applicability labels, and bit-exact replay. MG-5
implementation at clean commit `5b9d272` is now `COMPLETE_VERIFIED`: both
adaptation states and all 512 scored positions passed at the exact trainer
seam; minimum candidate and token margins were `11.670098155736923` and `24`;
all five named corruptions failed closed; non-planted teachers were explicitly
labeled; replay was bit-exact; 12 focused/historical and 243 full tests passed.
MG-6 specification is next. Evidence:
`experiments/20260805T033800Z-epc-remediation-mg5-spec-freeze/`.
The initial freeze was superseded before fixture execution because raw numeric
memory addresses contradict bit-exact JSON replay; r2 records exact
object/storage equality as booleans. Evidence:
`experiments/20260805T033948Z-epc-remediation-mg5-spec-freeze-r2/`.
MG-5 completion evidence:
`experiments/20260805T035047Z-epc-remediation-mg5-acceptance/` and
`experiments/20260805T035158Z-epc-remediation-mg5-full-suite-clean/`. MG-6 was
independently frozen at clean commit `816026a` (spec SHA-256
`d960838713873fafa353228ec5064128cea64fe1c47811c3d453f5bf8ab43130`).
It fixes the actual `_nll` reduction/units, declared `1.4/2=0.7` threshold,
exhaustive pre/adapted oracle and exact MG-5 teacher round trips, retention,
five fail-closed controls, and replay. Its implementation at clean commit
`3f0d17e` is now `COMPLETE_VERIFIED`: both explicit oracle states scored at
most `2.3783352260358675e-09`, both exact trainer round trips scored `0.0`,
retention passed `0.7`, uniform matched `ln(64)` exactly, all five controls
failed closed, replay was bit-exact, and 16 focused plus 247 full tests passed.
Artifact SHA-256:
`2fc3641810f66c5b383e9a1e871642887947cff018e81c6efa9fa7574425d885`.
MG-7 specification is next. Evidence:
`experiments/20260805T035722Z-epc-remediation-mg6-spec-freeze/`,
`experiments/20260805T050415Z-epc-remediation-mg6-acceptance/`, and
`experiments/20260805T050443Z-epc-remediation-mg6-full-suite-clean/`. MG-7 is
now independently frozen at clean commit `490134a` (spec SHA-256
`ba87de3723cecd274c0426c1d92ce3ca50c8d28a5fcaae7f4a6c05e104eb7033`).
It resolves the literal feedforward `0/0` share ambiguity by probing the local
quadratic metric at the feedforward basepoint with held-out residual-stream
perturbations and fit-split diagonal inverse-variance precisions. It fixes the
exact split, float64 reductions, `[0.25,4.0]` share-to-uniform bound, six
controls, provenance, and replay. MG-7 is now `COMPLETE_VERIFIED` at clean
implementation commit `38f8efc`: the exact 32/32 perturb split, bit-exact
replay, and all six controls pass; weighted share-to-uniform ratios are
`1.0024781426298592` and `0.9975218573701409`; the full suite passes 249.
Artifact SHA-256: `3d3d3a908aa6e0fb3989c630a26f0966f87ae3f85d7e093e2dfe5b3888c4c555`.
This verifies only the declared two-block metric. Freeze MG-8 independently
before execution. Evidence:
`experiments/20260805T051435Z-epc-remediation-mg7-spec-freeze/` and
`experiments/20260805T052237Z-epc-remediation-mg7-acceptance/`.
MG-8 was independently frozen at clean commit `06b66fb` (spec SHA-256
`2071401dce047e5ec3a496094485dd069746ba32620417c8fd5bacf4fef64a3e`) and
implemented at clean commit `27c5105`. It is now `COMPLETE_VERIFIED`: fresh
subprocess replays under `PYTHONHASHSEED=0/1` produced byte-identical,
SHA-256-matched, embedded-spec-bound artifacts for MG-1/MG-2R/MG-3--MG-7;
all six corruption controls failed closed. Focused A0/MG regressions passed 42
tests and the complete suite passed 252. MG-8 artifact SHA-256:
`6d3f86d8fe369633aed5d6124c4a56b447609c38662acb85b66b5b6374bd8057`.
M0-R is independently frozen at clean commit `5813c75` (spec SHA-256
`378aac9115ab719e5529191ce35f8d741ae47d4e332eb23169189860cc7d4c71`).
It preserves the diagnosis finite-lambda contract as a visible failed
sub-result while testing exact EO settlement and the theorem-consistent BP
limit on the full width/depth grid. Its clean implementation at commit
`81ad6cd` is now `COMPLETE_VERIFIED`: all 40 unique corrected points and both
24-reference panels pass exact settlement, analytic equilibrium, local
gradient, conditioning, adjoint-cosine, and theorem-rate gates. Maximum
fixed-point and numerical/exact local-gradient errors were
`9.021408383961103e-09` and `2.33488520852358e-08`; the minimum cosine was
`0.9999999999999997` and maximum settling radius `0.6499058259149558`.
The diagnosis finite-lambda result remains `FAILED_TEST`, with maximum-layer
BP differences spanning `0.002193--0.932356`. Twelve legacy points settled
and twelve remained explicitly partial. Artifacts replayed bit-exactly; 31
focused and 255 complete-suite tests passed. C1 specification freeze is next,
followed by any provider-free reference reproduction possible before the GPU
authority boundary. Evidence:
`experiments/20260805T053817Z-epc-remediation-mg8-acceptance-r2/`,
`experiments/20260805T053956Z-epc-remediation-mg8-focused-clean/`,
`experiments/20260805T054206Z-epc-remediation-mg8-full-suite-clean/`, and
`experiments/20260805T054642Z-epc-remediation-m0-spec-freeze/`,
`experiments/20260805T062130Z-epc-remediation-m0-acceptance/`,
`experiments/20260805T062537Z-epc-remediation-m0-focused-clean/`, and
`experiments/20260805T062749Z-epc-remediation-m0-full-suite-clean/`.
C1 is independently frozen at clean commit `f8cfed4` (spec SHA-256
`b5461260b9d27bb4354205707d83b8010b2bf20503fdceb216e6af596cb26891`).
It requires an official five-seed MNIST EO reproduction before the pinned
GPT-2-small/WikiText-2 conversion, one shared FabricPC attention/MLP graph, a
frozen per-edge metric, exact rung-0 identity, ten fixed lambda rungs, and
fail-closed quality/settlement/conditioning/material-departure stops. The
diagnosis makes C1 GPU-only, so scientific execution is `BLOCKED_AUTHORITY`.
The complete no-provision Runpod A40 proposal is
`docs/epc-c1-runpod-authority-proposal-20260805.md`; provider-free
implementation and dry-run tests remain locally admissible. Evidence:
`experiments/20260805T063722Z-epc-remediation-c1-spec-freeze/`.
The provider-free C1 implementation preflight is complete through clean commit
`9bab1c9`. It adds a fail-closed wrapper around the exact official EO checkout
and one shared GPT-2 FabricPC graph with separate ordered attention/MLP edges,
explicit-error reconstruction, tied-weight attestation, frozen-precision
validation, and next-token KL. It also adds the exact ordered calibration/
update/validation/test token-block manifest and float64 per-edge covariance
fitter with the frozen variance floor and mean-one normalization. The official commit and six source hashes
attested exactly; the zero-error graph matched an actual Hugging Face GPT-2
forward byte-for-byte; the final focused acceptance passed 15 tests including
MG-7/MG-8 replay and all 262 repository tests passed.
This is implementation evidence only: no official reference seed, C1 science
partition, model/data download, GPU, pod, or paid service ran. Ben's recorded
A40 approval remains unexercised because the current scheduler activation
explicitly prohibited paid/GPU use. Next provider-free work is execution/config
packaging and a no-data/no-model dry-run orchestrator. Evidence:
`experiments/20260805T070453Z-epc-remediation-c1-reference-preflight-r2/`,
`experiments/20260805T070503Z-epc-remediation-c1-provider-free-focused/`, and
`experiments/20260805T070528Z-epc-remediation-c1-provider-free-full-suite/`,
`experiments/20260805T071429Z-epc-remediation-c1-data-metric-focused/`, and
`experiments/20260805T071606Z-epc-remediation-c1-data-metric-full-suite/`.
The next provider-free C1 unit is complete at clean commit `e8421ac`. A strict
JSON execution contract now binds the reference reproduction, pinned model and
corpus, partitions, metric, all ten rungs, optimizer, replay tolerances, and
artifact layout. Its no-data/no-model orchestrator attested the official source
and emitted a deterministic prerequisite/stop plan with explicit false
model/data/GPU/paid-resource flags and zero opened science seeds. The focused
graph/MG-7/MG-8 acceptance passed 14 tests and the clean full suite passed 264.
No C1-A or transformer science ran. Next provider-free work is the C1-A
launcher/result-adjudication seam; the scheduler's no-paid/GPU restriction
continues to override the recorded A40 approval. Evidence:
`experiments/20260805T074256Z-epc-remediation-c1-execution-dryrun-focused/`,
`experiments/20260805T074435Z-epc-remediation-c1-execution-dryrun-artifact/`,
and
`experiments/20260805T074550Z-epc-remediation-c1-execution-dryrun-full-suite/`.

The provider-free C1-A launch and statistical adjudication seam is complete at
clean commit `5d47837`. It binds each official seed to exact source/config/
dataset-contract/MG-1/MG-3 hashes, requires byte-identical fresh-process input
manifests, validates an exact five-record schema, and applies the frozen mean
interval/sample-SD gate without tuning. A statistical miss remains
`FAILED_REFERENCE_REPRODUCTION` and blocks transformer execution. Two fresh
plan processes emitted byte-identical JSON (SHA-256
`cffa70d1a4208e954a57f372ddf4591226c64b0cc57d198d479d3f9f94fb7766`);
11 focused and 266 clean full-suite tests passed. This remains packaging
evidence: no EMNIST data, reference seed, GPU, pod, or paid service was opened.
Next is the provider-free seed-executor/data-manifest package. Evidence:
`experiments/20260805T080410Z-epc-remediation-c1-reference-gate-focused/`,
`experiments/20260805T080443Z-epc-remediation-c1-reference-launch-artifact-r2/`,
`experiments/20260805T080456Z-epc-remediation-c1-reference-launch-replay/`, and
`experiments/20260805T080759Z-epc-remediation-c1-reference-gate-full-suite/`.

The provider-free C1-A seed executor/data-provenance package is complete at
clean commit `96b9741`. It lazily imports the official runtime only after
explicit authority, exact two-process job replay, MG-1/MG-3 certificate,
dataset-root, byte/split, and CUDA gates. The dataset manifest hashes compressed
GZip members, decoded IDX streams, payloads, exact 60,000/10,000 shapes, and
canonical full-split indices. Synthetic and corruption controls passed; two
fresh plans were byte-identical (SHA-256 `4c527686...4501d53`) and the clean
suite passed 268 tests. No EMNIST byte, reference seed, CUDA device, GPU, pod,
or paid service was opened. Next provider-free work is immutable environment
and remote hand-off packaging. Evidence:
`experiments/20260805T082816Z-epc-remediation-c1-seed-executor-focused-r2/`,
`experiments/20260805T082857Z-epc-remediation-c1-seed-executor-plan-cmp/`, and
`experiments/20260805T082940Z-epc-remediation-c1-seed-executor-full-suite/`.

The provider-free C1 remote-environment/hand-off preflight is complete at clean
commit `aa62845`. It binds the approved image to registry digest
`sha256:61a4aafb...4141fb5`, freezes direct dependency/runtime expectations,
requires an offline SHA-256 wheelhouse and provider/runtime attestations before
science, and deterministically archives the clean RelaLeap source, official EO
reference, C1 configs, five unopened jobs, and MG-1/MG-3 certificates. Two fresh
builds were byte-identical: the 2,662,400-byte bundle SHA-256 is
`35c6d73a7f67bc1cb6f7d5630a1bbcb39ba64be2a9da70e11bbc1a217fd8a84a`.
Twenty focused and 270 clean full-suite tests passed. No dataset, seed, model,
CUDA query, GPU, pod, or paid resource was used. Next provider-free work is
materializing and attesting the exact wheelhouse/runtime verifier. Evidence:
`experiments/20260805T084839Z-epc-remediation-c1-remote-handoff-focused/`,
`experiments/20260805T085134Z-epc-remediation-c1-remote-handoff-artifact/`,
`experiments/20260805T085201Z-epc-remediation-c1-remote-handoff-cmp/`, and
`experiments/20260805T085222Z-epc-remediation-c1-remote-handoff-full-suite/`.

The C1 direct wheelhouse and record-only runtime verifier are complete at clean
commit `017dbcf`. Exactly 11 CPython-3.11/manylinux-x86-64 direct wheels were
downloaded with `--no-deps` and validated from their embedded core metadata;
the 43,559,835 wheel bytes are covered by `SHA256SUMS`. Two fresh manifest
processes were byte-identical. Embedded manifest SHA-256 is
`496fb73f6793792327b2faa1685da36fedf67b6232b932bba1581566eb38b5f1`;
persistent JSON SHA-256 is
`34dc91f7f02b439cad81af9818c3da29500fc0dc6e4cbe66e75af51d65dc6ea6`.
The verifier rejects wheel corruption, dependency/runtime drift, activated
records, and environment/hash mismatch without probing local CUDA. Twenty-one
focused and 271 clean full-suite tests passed. This attests direct package
bytes and verifier behavior only; the pinned container, its transitive/base
runtime, and C1 science remain unverified. No science seed/data/model, CUDA
query, GPU, pod, or paid resource was used. Next: rebuild the clean hand-off and
bind this manifest for offline transfer. Evidence:
`experiments/20260805T092002Z-epc-remediation-c1-wheelhouse-download/`,
`experiments/20260805T092051Z-epc-remediation-c1-wheelhouse-attestation/`,
`experiments/20260805T092124Z-epc-remediation-c1-wheelhouse-cmp/`, and
`experiments/20260805T092439Z-epc-remediation-c1-wheelhouse-full-suite/`.

The wheelhouse-bound offline C1 hand-off is complete at clean commit
`11fd718`. Hand-off schema v2 embeds all 11 attested direct wheels, their exact
`SHA256SUMS`, and machine manifest while retaining the clean source/reference
archives, frozen configs/jobs, and MG certificates. The 46,264,320-byte bundle
contains 43,559,835 wheel bytes; two fresh builds were byte-identical. Bundle
SHA-256 is
`7951bb3e9cb5db736fcb390b37177f5196c8b8cab125f55487ecc50ed82fca9e`;
hand-off manifest SHA-256 is
`340fc7aa344daabcb75125a7509743e1f26c65423e99399b57ca9f7d87f28095`.
Three focused binding tests, 21 C1/MG replay tests, and all 271 repository tests
passed. Corrupt or mismatched wheel bytes fail closed. The pinned container,
transitive/base runtime, and C1 science remain unverified. No science input,
CUDA query, GPU, pod, or paid resource was used. Next provider-free work is a
no-provision bootstrap/runtime-record package for the already bound archive.
Evidence:
`experiments/20260805T094444Z-epc-remediation-c1-bound-handoff-focused/`,
`experiments/20260805T094723Z-epc-remediation-c1-bound-handoff-artifact/`,
`experiments/20260805T094752Z-epc-remediation-c1-bound-handoff-replay/`,
`experiments/20260805T094806Z-epc-remediation-c1-bound-handoff-cmp/`, and
`experiments/20260805T094827Z-epc-remediation-c1-bound-handoff-full-suite/`.

The provider-free remote bootstrap/runtime-record path is complete at clean
commit `21225bd`. A deterministic 10,240-byte bootstrap archive binds the
exact clean handoff, its manifest, pinned container digest, and wheelhouse
manifest, and packages future offline installation plus runtime capture while
remaining explicitly unauthorized and unexecuted. Static Python and shell
validation pass; the recorder calls no `torch.cuda` API. Two fresh handoffs and
bootstrap archives replayed byte-identically. Bootstrap SHA-256 is
`021d68fcdaa187ce90bef55d88c5f1d8392b1e1d3f600452f07de3c133179ed0`;
manifest SHA-256 is
`87a30d72f2a32f01c41843e31f79cd09807dccf582e71f63252d6620be8590dd`.
Three focused and 272 clean full-suite tests passed. No bootstrap command,
package install, science input, CUDA query, GPU, pod, or paid resource was
used. Next provider-free work is the provider/job/cost and artifact-return/
termination record seam. Evidence:
`experiments/20260805T100610Z-epc-remediation-c1-bootstrap-artifact/`,
`experiments/20260805T100652Z-epc-remediation-c1-bootstrap-cmp/`, and
`experiments/20260805T100712Z-epc-remediation-c1-bootstrap-full-suite/`.

The provider-free C1 resource/job/cost and return/termination lifecycle seam is
complete at clean commit `a91218e`. A deterministic 20,480-byte archive binds
the exact approved proposal, handoff, bootstrap, image, wheelhouse, source,
Runpod A40 envelope, `$0.44/GPU-hour` rate, 20-hour science stop, 24-hour and
`$12.00` hard caps, local artifact return, and termination policy. Returned
artifacts must pass exact `RETURN.json`/`SHA256SUMS` verification before a
cleanup record is accepted; stopped resources, nonzero pods/volumes/endpoints/
snapshots, retained container storage, corrupt artifacts, and cost overruns
fail closed. Two fresh archives replayed byte-identically. Bundle SHA-256 is
`847382c38535f1086e6ebd47c85480378a6625e0aab24b492081d1d78a254f01`;
manifest SHA-256 is
`bee91aa3c2209b1a555e9c2f862e9fa9682099c413844e9ddc7ea6cc2764b607`.
Two focused and 274 clean full-suite tests passed. No provider access,
provisioning, bootstrap, install, science input, CUDA query, GPU, pod, cleanup,
or paid resource occurred. Next provider-free work is binding the future
launch/monitor state machine and local post-return adjudication to this
lifecycle. Evidence:
`experiments/20260805T103008Z-epc-remediation-c1-lifecycle-artifact-clean/`,
`experiments/20260805T103343Z-epc-remediation-c1-lifecycle-cmp-clean/`, and
`experiments/20260805T103022Z-epc-remediation-c1-lifecycle-full-suite/`.

The provider-free launch/monitor and post-return C1-A adjudication seam is
complete at clean commit `ac15e78`. It binds the exact lifecycle manifest and
unopened five-seed launch, enforces ordered transitions, immutable resource
identity, monotone usage/cost counters, science stops, hard caps, exact
returned-launch identity, and local positive/negative statistical
adjudication before cleanup. Two fresh 10,240-byte packages replayed
byte-identically. Bundle SHA-256 is
`ec71f90e88b0e1360429dfda36a5fb96ae874307069b3cfb86f2a0d9fa3c6a07`;
manifest SHA-256 is
`94748261d1dd5e47dc51e97dc648d3f398c5c6639ed7b5e1f36f2632c2230746`.
Twenty-two focused/regression and 277 full-suite tests passed. No provider,
resource, science input, seed, CUDA query, GPU, or paid service was used. Next
provider-free work is the exact future remote command/receipt envelope and
monitor evidence parser. Evidence:
`experiments/20260805T105948Z-epc-remediation-c1-orchestration-artifact/`,
`experiments/20260805T110016Z-epc-remediation-c1-orchestration-cmp/`, and
`experiments/20260805T110031Z-epc-remediation-c1-orchestration-full-suite/`.

The provider-free exact-command and monitor-receipt seam is complete at final
clean commit `58363e5`. It binds the exact bootstrap and official five-seed
reference-batch argv to the frozen lifecycle/orchestration/handoff/bootstrap
digests, packages syntax-checked scripts, and validates ordered receipts with
immutable resource identity, evidence-file SHA-256, terminal-failure ordering,
monotone usage/cost counters, and science/hard-cap classifications. Two fresh
10,240-byte archives were byte-identical. Bundle SHA-256 is
`e4457addf095f285e45e75aaf91c3cddead4b3960b40fbf3bd4543f5c1bb811d`;
manifest SHA-256 is
`e8a938fc3b29ef9bbb99bc68d9d8a33e3bbf574b7f75492c94ee1c23604484fb`.
Nine focused/lifecycle/orchestration tests and all 281 repository tests passed.
No packaged command, provider, resource, data/model input, seed, CUDA query,
GPU, or paid service was used. Next provider-free work is the exact returned-
artifact manifest builder and receipt-to-monitor-event bridge. Evidence:
`experiments/20260805T114131Z-epc-remediation-c1-command-receipts-replay/`,
`experiments/20260805T114142Z-epc-remediation-c1-command-receipts-cmp/`,
`experiments/20260805T114152Z-epc-remediation-c1-command-receipts-focused-clean/`,
and
`experiments/20260805T114204Z-epc-remediation-c1-command-receipts-full-suite/`.

The provider-free returned-artifact/monitor bridge is complete at final clean
commit `f4c7e6e`, under independently frozen specification commit `f6a7165`
(SHA-256
`7170ec61bcc8e0aad37a1b3b70f67058c321a53bc165035720351abd4c335c7e`).
Exact validated receipts now replay through the existing monitor transitions;
partial, failed, stopped, and hard-cap streams remain cleanup-required. The
return builder binds canonical monitor evidence, all lifecycle categories, and
every payload byte into deterministic `RETURN.json`/`SHA256SUMS`, then invokes
the existing local attestor. Two independent bridge and return builds were
byte-identical (SHA-256 `3a255811...c0619`, `226ba2f4...dc7c6`, and
`5e7cf19f...c3e2`); 13 focused/prior-seam and all 285 repository tests passed.
No provider, packaged command, science input, seed, CUDA query, GPU, or paid
service was used. Next provider-free work is an end-to-end synthetic
return/adjudication/termination replay and exact cleanup-event bridge; actual C1
science remains prohibited by the current activation. Evidence:
`experiments/20260805T121734Z-epc-remediation-c1-return-bridge-artifact-clean-r3/`,
`experiments/20260805T121757Z-epc-remediation-c1-return-bridge-cmp/`,
`experiments/20260805T121806Z-epc-remediation-c1-return-bridge-focused-clean/`,
and
`experiments/20260805T121818Z-epc-remediation-c1-return-bridge-full-suite/`.

The provider-free end-to-end return/adjudication/termination closure is complete
at final clean commit `6a08771`, under independently frozen specification
commit `be63733` (SHA-256
`70347f7dc77bdeb1c5628767fc4f7b49ca8dba636af13b15b986ea90bfc37c7c`).
It replays the exact successful receipt bridge, re-attests returned bytes,
applies the frozen five-seed adjudicator, verifies terminated/zero-resource
cleanup, and advances exactly through `artifacts_returned`,
`reference_adjudicated`, and `cleanup_verified`. A frozen statistical failure
also closes cleanly without admitting transformer execution; bridge, returned-
byte, resource, cost, and timestamp corruptions fail closed. Two independent
closure records were byte-identical (SHA-256
`a248dc6840764470e51b3eb8bb5aa755101441a37613cbbbb94cdff488e2007b`);
15 focused/prior-seam and all 287 repository tests passed. No packaged command,
provider, science input/seed, CUDA query, GPU, or paid service was used. All
currently identified provider-free C1 lifecycle seams are closed; actual C1-A
execution is `BLOCKED_AUTHORITY` because this activation explicitly prohibits
the otherwise approved paid/GPU resource. Evidence:
`experiments/20260805T124254Z-epc-remediation-c1-cleanup-closure-artifact-clean/`,
`experiments/20260805T124322Z-epc-remediation-c1-cleanup-closure-cmp-clean/`,
`experiments/20260805T124331Z-epc-remediation-c1-cleanup-closure-focused-clean/`,
and
`experiments/20260805T124343Z-epc-remediation-c1-cleanup-closure-full-suite/`.

At `2026-08-05T12:55Z`, the blocked C1 checkpoint was independently
revalidated without opening a provider or science input. All 14 frozen
proposal/package files matched their declared SHA-256 values, and the combined
provider-free preflight/lifecycle/orchestration/receipt/return/cleanup suite
passed 32 tests in 6.04 seconds from clean commit `6a08771`. This confirms
local readiness has not drifted; it does not establish any C1 scientific
criterion. Actual C1-A remains `BLOCKED_AUTHORITY` under the activation's
explicit paid/GPU prohibition. Evidence:
`experiments/20260805T125537Z-epc-remediation-c1-frozen-envelope-integrity-revalidation/`
and
`experiments/20260805T125537Z-epc-remediation-c1-provider-free-seams-revalidation/`.

At `2026-08-05T13:10Z`, a second blocked-checkpoint continuity audit found the
same clean commit `6a08771` and no competing writer. All 14 frozen
proposal/package paths again passed their SHA-256 ledger, and the combined 32
provider-free C1 seam tests passed in 6.35 seconds. This is repeated local
readiness evidence only; actual C1-A remains `BLOCKED_AUTHORITY` because the
activation again explicitly prohibits paid/GPU use. Evidence:
`experiments/20260805T131041Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r2/`
and
`experiments/20260805T131051Z-epc-remediation-c1-provider-free-seams-revalidation-r2/`.

At `2026-08-05T14:10Z`, the post-self-audit blocker remained unchanged. The
isolated worktree was clean at `6a08771` with no competing writer; all 14
frozen envelope hashes passed, and all 32 provider-free C1 seam tests passed in
6.06 seconds. This is readiness continuity only. The activation explicitly
prohibited paid/GPU use, so actual C1-A remains `BLOCKED_AUTHORITY` and no
provider, science input/seed, CUDA query, GPU, or paid resource was used.
Evidence:
`experiments/20260805T141045Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r5/`
and
`experiments/20260805T141049Z-epc-remediation-c1-provider-free-seams-revalidation-r5/`.

At `2026-08-05T14:26Z`, the authority boundary remained unchanged. The
isolated worktree was clean at `6a08771` with no competing writer; all 14
frozen envelope hashes passed, and all 32 provider-free C1 seam tests passed in
5.89 seconds. This is readiness continuity only. The activation explicitly
prohibited paid/GPU use, so actual C1-A remains `BLOCKED_AUTHORITY` and no
provider, science input/seed, CUDA query, GPU, or paid resource was used.
Evidence:
`experiments/20260805T142602Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r6/`
and
`experiments/20260805T142607Z-epc-remediation-c1-provider-free-seams-revalidation-r6/`.

At `2026-08-05T14:43Z`, the next scheduler activation still explicitly
prohibited paid/GPU use. The isolated worktree remained clean at `6a08771`
with no competing writer; all 14 frozen envelope hashes passed, and all 32
provider-free C1 seam tests passed in 6.21 seconds. This is readiness
continuity only, not C1 science. Actual C1-A therefore remains
`BLOCKED_AUTHORITY` for this activation; no provider, science input/seed, CUDA
query, GPU, or paid resource was used. Evidence:
`experiments/20260805T144311Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r7/`
and
`experiments/20260805T144320Z-epc-remediation-c1-provider-free-seams-revalidation-r7/`.

The requested larger multi-regime ePC preflight is complete but failed closed.
V1 implemented a four-regime planted transformer evaluator (ID,
composition, cue perturbation, and replay-supported sequential adaptation),
with explicit per-regime NLL, matched T=1/T=2/T=4 arms, bit-exact replay, and
monotone-energy checks. After recording an indexed-teacher instrumentation
counterexample and correcting it, the final two-seed calibration preserved
replay and energy monotonicity but the matched T=1 control failed every
learnability floor. Therefore the task itself was not admitted and no ePC
frontier, specialist, or MoE claim follows. Evidence:
`experiments/20260804T173241Z-epc-multiregime-frontier-preflight-v1-r5/`.
The detailed report and minimal independently reproducible Apache-2.0 code
bundle are public at
`https://github.com/bgoertzel-sing/relaleap-epc-multiregime-preflight`
(public commit `ffb6269`).
The companion prior-ePC-history report is published at
`https://github.com/bgoertzel-sing/relaleap-epc-multiregime-preflight/blob/agent/prior-epc-history-report/report/prior_epc_experiment_history_20260804.pdf`
(commit `ca64aa4`; SHA-256
`5783e4982e30e407e107b218d3fc983999968c782272abcbf168fd81243ff751`).

The semantic-free ePC Pareto-frontier experiment requested by Ben is complete
and failed closed. A 14-cell, six-control v1 screen found four viable
exploration candidates but exposed that aggregate Pareto pruning could discard
conditional specialists. V2 repaired the protocol by adding every
context-by-mode NLL as an explicit Pareto axis and using fresh splits. Two
candidates survived exploration, only `upd128` survived selection, and it
failed confirmation by recovering both modes in only one context on seed
`36002`. All 62 v1/v2 records replayed exactly with monotone activity energy.
No stable diversely-good expert pool or MoE experiment is admitted. Evidence:
`experiments/20260804T055941Z-epc-diverse-pareto-frontier-v1/` and
`experiments/20260804T060519Z-epc-diverse-pareto-frontier-v2/`; decision
`D-20260803-epc-diverse-frontier-negative`.

The persistent semantic lane is now anchored by cron
`091b3e12-1971-4bfa-a6fb-52e83554153a`. Its first provider-free obligation
audit preserved all prior batteries and froze an unopened 24-case v4 oracle
gate. Static integrity found zero exact sentence overlap with v1--v3 and the
failed offline-v1 corpus; 7 focused frame tests and the 175-test full suite
passed (5 skipped). The audit also exposed two source-level v3 contract gaps:
whole-sentence lexical negation can mislabel proper names containing `No`, and
the normalizer overwrites declared `possible` modality with `asserted`. No
oracle was invoked and no semantic outcome, labels, readout, or loss is
admitted. Evidence:
`experiments/20260803T051233Z-frame-oracle-v4-sealed-contract-r2/` and
`docs/frame_oracle_v4_sealed_gate_contract_20260802.md`.

The implementation-side v4 obligation is now frozen without opening that
gate. Isolated branch `agent/frame-oracle-v4` at commit `1cbcf9e` adds a
scope-aware deterministic normalizer, clarified prompt, independent fixtures,
and a fail-closed one-use runner that completes all 48 paired decodes before it
reads the committed answers. Focused v4 tests passed 6/6, all exposed frame
regressions passed 13/13, and the full suite passed 181 with 5 skips from a
clean commit. Prompt, schema, source, model ID, seed, decode, answer commitment,
and paired-command metadata are frozen. The 24-case scientific gate remains
unconsumed, so no v4 semantic accuracy, label, readout, or loss is admitted.
Evidence:
`experiments/20260803T071411Z-frame-oracle-v4-freeze-before-open/`.

A subsequent exact-command preflight suspended that implementation-side
admission before any inference. The frozen virtual environment resolves
`relaleap` to a separate causal-fibres worktree, so the frozen v4 runner raises
`ModuleNotFoundError` for `relaleap.hdpc.frame_oracle_v2` before parsing
arguments. An explicit `PYTHONPATH` control reaches the parser, confirming an
import-provenance defect rather than a semantic outcome. The public gate still
declares `opened=false`; no cases, answers, or oracle outcomes were exposed.
It therefore required the bounded import-provenance repair and a replacement
clean freeze before gate consumption. Evidence:
`experiments/20260803T091034Z-frame-oracle-v4-exact-command-preflight/` and
`docs/frame_oracle_v4_import_provenance_repair_contract_20260803.md`.

That bounded repair is now complete on the same isolated branch at clean
commit `acf3fbf`. A pinned wrapper replaces inherited `PYTHONPATH`, and a
pre-parser attestor rejects missing, symlink-escaped, mixed-root, or
hash-mismatched `relaleap` modules while recording interpreter and module
provenance. The semantic v2/v3/v4 source hashes, prompt, schema, model, seed,
decode, public cases, and answer commitment are unchanged. Focused v4 tests
passed 7/7, all exposed frame regressions passed 14/14, and the full suite
passed 182 with 5 skips from a clean commit. An exact `--help` preflight now
resolves every imported `relaleap` module under the v4 worktree. The gate still
declares `opened=false`; no Ollama inference or answer evaluation occurred.
Implementation-side eligibility is restored only for the later one-use argv in
the replacement manifest; no semantic outcome, label, readout, or loss is
admitted. Evidence:
`experiments/20260803T111529Z-frame-oracle-v4-import-provenance-freeze/`.

A subsequent provider-free failure-injection audit suspended that eligibility
again before inference. When a mocked first public inference completes and the
second paired call raises, the frozen runner persists `gate_consumed=false`
and `completed_pairs=0`. This can misclassify a partially opened battery as
reusable and violates the fail-closed contract. The counterexample contacted
neither Ollama nor answers; the real 24-case gate remains `opened=false` with
its commitment verified. No semantic outcome is admitted. The next bounded
step is an atomic consumption-state repair and clean replacement freeze under
`docs/frame_oracle_v4_consumption_state_repair_contract_20260803.md`.
Evidence:
`experiments/20260803T131110Z-frame-oracle-v4-consumption-counterexample/`.

The bounded atomic consumption-state repair is now complete and refrozen on
isolated descendant branch `agent/frame-oracle-v4-consumption-state` at clean
commit `53630b9`. The runner durably writes `consumed_pending` before its first
inference request, checkpoints every completed call, forbids resume, never
reverts to unconsumed, and queries the actual local Ollama registry digest
before transition. Independent synthetic fixtures covered pre-transition,
first/second/third-call, answer-commitment, and pre/post-transition atomic-write
failures plus a 48-call success control. Focused v4 tests passed 17/17, all
exposed frame regressions passed 24/24, and the full suite passed 192 with 5
skips from a clean commit. Exact interpreter/import attestation and full model
digest `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e`
were frozen. Only `GET /api/tags` was contacted; no inference or answer read
occurred. The real gate remains `opened=false`, `consumed=false`; no semantic
outcome is admitted. Evidence:
`experiments/20260803T151446Z-frame-oracle-v4-consumption-state-repair-dev/`
and
`experiments/20260803T151801Z-frame-oracle-v4-consumption-state-freeze/`.

The exact one-use v4 scientific gate has now completed and failed closed.
After the manifest, commitment, clean commit, model digest, 17 focused tests,
24 exposed regressions, and the 192-test full suite were reverified, the
runner completed all 48 local calls and durably terminated in
`consumed_failed`. All 24 cases were schema-valid, but paired determinism and
exact semantic keys were each only 17/24; multiple required strata were
imperfect. The v4 battery is permanently retired and no labels, readout,
substitution evaluation, or semantic loss is admitted. Do not tune v4 against
its opened rows or responses. Evidence:
`experiments/20260803T171351Z-frame-oracle-v4-one-use-gate/`.

A fresh contract-templated 24-case v5 successor bundle is process-sealed at
`sealed/frame-oracle-v5/`. Its integrity gate verifies the committed answers,
all five predicates, required polarity/modality/abstention coverage, and zero
exact sentence overlap with v1--v4 and offline-readout-v1. It remains
`opened=false`; no v5 implementation or oracle outcome exists. The next
semantic-lane step is a bounded source-derived v5 behavior spec or concrete
blocker, without consulting v4 raw outcomes or v5 answers. Evidence:
`experiments/20260803T172839Z-frame-oracle-v5-sealed-contract-r2/` and
`docs/frame_oracle_v5_fresh_gate_contract_20260803.md`.
Its author knew the aggregate v4 verdict and per-stratum summary but did not
inspect raw proposals/rows; it is therefore case-disjoint and process-sealed,
not strictly outcome-blind at the aggregate-stratum level.

A provider-free source audit has now fixed the bounded v5 implementation
hypothesis without inspecting v4 raw outcomes or any v5 case/answer. Four
independent counterexamples reproduce two source defects: v4 recognizes
`might`/`could` inside proposed names and titles as modality, and it misses
common contracted negation. V5 must mask proposed entity spans before finite
cue recognition and add common `n't`/`cannot` handling while leaving proposal
selection and abstention explicitly unclaimed. At the time of that audit, no
v5 code or inference existed and the gate remained unopened. Evidence:
`experiments/20260803T191310Z-frame-oracle-v5-source-behavior-audit/` and
`docs/frame_oracle_v5_behavior_spec_20260803.md`.

The bounded behavior implementation is now complete on clean isolated branch
`agent/frame-oracle-v5` at commit `f474d96`. It leaves the closed proposal
prompt unchanged, masks one case-insensitive whitespace-normalized occurrence
of each proposed entity slot, and adds a finite straight/curly-apostrophe
contraction grammar plus `cannot`. Ten independent v5 fixtures, 34 exposed
frame/atomic-runner regressions, and the full 225-test suite passed from the
clean commit. This is engineering evidence only: no v5 runner/import contract
or freeze manifest exists yet, and no v5 case sentence, answer, or inference
was used. The gate remains unopened and no downstream semantic stage is
admitted. Evidence:
`experiments/20260803T211703Z-frame-oracle-v5-behavior-implementation-clean/`.

The v5 implementation-side preopen freeze is now complete on clean isolated
descendant `agent/frame-oracle-v5-freeze` at commit `a90298b`. A versioned
runner preserves the atomic `consumed_pending` state transition, per-call
checkpoints, forbidden resume, answer-after-decode ordering, and exact local
model-digest verification while applying the v5 normalizer. Its pinned wrapper
and import attestor resolve and hash v2--v5 from one source root before CLI
parsing. Twenty focused v5/state-machine tests, 44 exposed frame regressions,
the pinned-interpreter suite (212 passed, 5 skipped), and the broader host
suite (235 passed) all passed from the clean commit. The only Ollama contact
was `GET /api/tags`; the exact runner preflight used `--help`, and the sealed
answer file was not read. V5 remains `opened=false`, `consumed=false`, with no
semantic outcome or downstream stage admitted. A successor may execute only
the manifest's one-use argv in a fresh experiment. Evidence:
`experiments/20260803T231206Z-frame-oracle-v5-runner-provenance-freeze/`.

The exact v5 one-use scientific gate has now completed and failed closed.
After the manifest, commitments, clean commit, model digest, 235 host tests,
20 focused pinned tests, 44 exposed regressions, and the 212-test pinned suite
(5 skipped) were reverified, the runner completed all 48 local calls and
durably terminated in `consumed_failed`. All 24 rows were schema-valid, but
paired determinism and exact semantic keys were each only 18/24; several
required strata were imperfect. V5 is permanently retired and no labels,
readout, substitution evaluation, or semantic loss is admitted. Do not tune
against its opened cases, proposals, normalized rows, or answers. Evidence:
`experiments/20260804T011531Z-frame-oracle-v5-one-use-gate/`.

A fresh 24-case v6 successor is process-sealed at
`sealed/frame-oracle-v6/`. Its integrity validator verifies the committed
answers, all five predicates, required polarity/modality/abstention coverage,
and zero exact sentence overlap with v1--v5 and offline-readout-v1. It remains
`opened=false`; no v6 implementation or oracle outcome exists. The author
knew the aggregate v5 verdict, per-stratum summary, and failure identifiers
but did not use v5 proposal or normalized-row contents, so v6 is
exact-case-disjoint and process-sealed, not strictly outcome-blind. Evidence:
`experiments/20260804T013026Z-frame-oracle-v6-sealed-contract/` and
`docs/frame_oracle_v6_fresh_gate_contract_20260803.md`.

A provider-free v6 source audit has now frozen one bounded behavior hypothesis
without inspecting v5 gate rows/proposals/normalized outputs or any v6 case or
answer. V5 masks only the first occurrence of each proposed entity slot; three
independently authored repeated-name/title fixtures reproduced leakage of
`could`, `May Not`, and lower-case `no` into modality or polarity, while a
single-mention control passed. The current v5 source also passed 20 focused, 44
exposed-regression, and 235 full tests. V6 must mask the union of every exact
case-insensitive whitespace-normalized occurrence of both proposed slots while
preserving the prompt, schema, cue vocabularies, and all other behavior. No v6
implementation or inference exists and the gate remains unopened. Evidence:
`experiments/20260804T031820Z-frame-oracle-v6-source-behavior-audit-r2/` and
`docs/frame_oracle_v6_behavior_spec_20260803.md`.

The bounded v6 behavior implementation is now complete on clean isolated
branch `agent/frame-oracle-v6` at commit `df62566`. It reuses the exact v5
prompt, schema, canonicalization, and finite cue recognizers, changing only the
mask to cover the union of every exact case-insensitive,
whitespace-normalized occurrence of both proposed slots. Eight independent v6
fixtures, all 52 exposed frame/atomic-runner regressions, and the full 243-test
suite passed from the clean commit. This is engineering evidence only: no v6
runner/import freeze or oracle inference exists, the sealed battery remains
unopened, and no downstream semantic stage is admitted. Evidence:
`experiments/20260804T051741Z-frame-oracle-v6-behavior-implementation-clean/`.

The v6 implementation-side preopen freeze is now complete on clean isolated
descendant `agent/frame-oracle-v6-freeze` at commit `56b9eb9`. The
versioned runner preserves the conservative atomic consumption state machine,
uses the v6 all-occurrence normalizer, and defers answer access until all 48
paired calls complete. A pinned wrapper and import attestor verify one source
root and exact v2--v6 source hashes before argument parsing. Validation passed
18 focused v6/state-machine tests, 62 exposed frame/runner regressions, 230
pinned-interpreter tests with 5 skips, and 253 host-interpreter tests. Only
`GET /api/tags` and a no-inference `--help` preflight ran; the answer file
was not read. V6 remains `opened=false`, `consumed=false`, and no downstream
semantic stage is admitted. Evidence:
`experiments/20260804T072033Z-frame-oracle-v6-runner-provenance-freeze/`.

The exact v6 one-use gate has now failed closed as a consumed protocol error.
All frozen provenance and engineering checks passed, then the runner
checkpointed 45/48 local calls before `ClosedFrame` rejected a proposal whose
predicate and `abstain` value were inconsistent. The atomic exception path
terminally recorded `consumed_failed`; because paired decoding never finished,
the committed answers were never read and no accuracy or per-stratum metrics
exist. V6 is permanently retired and admits no labels, readout, substitution
evaluation, or semantic loss. Evidence:
`experiments/20260804T091501Z-frame-oracle-v6-one-use-gate/`.

A fresh 24-case v7 successor is now process-sealed at
`sealed/frame-oracle-v7/`. Its r2 integrity run verifies the answer commitment,
all five predicates, inherited coverage counts, `opened=false`, and zero exact
sentence overlap with v1--v6 plus offline-readout-v1. The first seal attempt
correctly rejected a seven-versus-six negation-count error and is preserved.
The author knew only the terminal v6 exception class and call count, not the
failing case, proposal, response, normalized row, or answers; v7 is therefore
exact-case-disjoint and process-sealed, not strictly outcome-blind. At seal
time no v7 implementation or inference existed. Evidence:
`experiments/20260804T092458Z-frame-oracle-v7-sealed-contract-r2/` and
`docs/frame_oracle_v7_fresh_gate_contract_20260804.md`.

A source-only audit has now frozen the bounded v7 behavior hypothesis without
inspecting opened v6 content or any v7 case/answer. The generation schema
accepts both predicate/abstention mismatch directions, but strict
`ClosedFrame.from_json` rejects them before the normalizer's intended unknown
canonicalization branch. Four independent synthetic fixtures reproduced both
exceptions and two canonical controls; 10 focused tests and the 230-test
pinned suite passed with 5 skips on the unchanged clean baseline. V7 is
bounded to a proposal-only structural parser plus a fail-closed union rule:
unknown predicate or true abstention becomes canonical unknown, while strict
canonical-frame validation and all other v6 behavior remain unchanged. At
audit time no v7 implementation or inference existed. Evidence:
`experiments/20260804T111528Z-frame-oracle-v7-source-contract-audit-r3/` and
`docs/frame_oracle_v7_behavior_spec_20260804.md`.

That bounded v7 behavior is now implemented on clean isolated branch
`agent/frame-oracle-v7` at commit `f096252`. Proposal ingestion validates the
existing seven-field envelope without weakening strict `ClosedFrame`, then
canonicalizes either unknown predicate or true abstention to canonical unknown
with confidence preserved; all non-abstaining proposals continue through v6
unchanged. Seventeen focused fixtures, 77 exposed frame/atomic-runner
regressions, and the full 247-test suite passed with 5 skips from the clean
commit. A clean descendant `61776ef` now freezes the conservative atomic
one-use runner and exact v2--v7 source/import/model provenance. Validation
passed 28 focused v7/state-machine tests, 90 exposed regressions, 258 pinned
tests with 5 skips, and 281 host tests. Only `GET /api/tags` and a no-inference
`--help` preflight ran; answers were not read. This remains engineering
evidence only: v7 is `opened=false`, `consumed=false`, no oracle outcome
exists, and no downstream semantic stage is admitted. Evidence:
`experiments/20260804T131754Z-frame-oracle-v7-behavior-implementation-clean-r2/`
and
`experiments/20260804T152139Z-frame-oracle-v7-runner-provenance-freeze/`.

The exact v7 one-use scientific gate has now completed and failed closed.
Clean commit `61776ef`, all frozen source/public/answer commitments, the local
model digest, 28 focused tests, 90 exposed regressions, and the pinned suite
(258 passed, 5 skipped) reverified before inference. The runner durably
completed all 48 calls and terminated in `consumed_failed`. All 24 cases were
schema-valid, but only 19/24 paired outputs were deterministic and only 3/24
semantic keys were exact; every required stratum was imperfect. V7 is
permanently retired. No label corpus, readout, substitution evaluation, or
semantic loss is admitted, and its opened rows must not be used for tuning.
Evidence:
`experiments/20260804T171432Z-frame-oracle-v7-one-use-gate/`.

A fresh 24-case v8 successor is process-sealed at
`sealed/frame-oracle-v8/`. Integrity verifies its committed answers, all five
predicates, inherited polarity/modality/abstention coverage, `opened=false`,
and zero exact sentence overlap with v1--v7 plus offline-readout-v1. The
author knew v7 aggregate counts and per-stratum imperfection but inspected no
v7 raw case, proposal, response, normalized row, or answer, so v8 is
exact-case-disjoint and process-sealed, not strictly outcome-blind. No v8
runner or inference exists. Evidence:
`experiments/20260804T172300Z-frame-oracle-v8-sealed-contract/` and
`docs/frame_oracle_v8_fresh_gate_contract_20260804.md`.

The source-only v8 behavior audit is complete without opening the battery.
At clean v7 commit `61776ef`, three independent synthetic fixtures show that
schema-valid whitespace-only entity strings canonicalize to empty slots while
remaining non-unknown. A non-empty control passed, as did 17 focused tests and
the full pinned suite (258 passed, 5 skipped). The bounded v8 contract now
requires any non-unknown proposal with an empty canonical slot to fail closed
to canonical unknown; it does not infer or repair entities. Clean isolated
commit `dee262f` implements only that rule and passed 20 focused, 108 exposed,
and 278 full tests with 5 skips. The separate conservative runner/provenance
freeze is now complete at clean isolated commit `b54fdcc`. It preserves
atomic pre-request consumption, per-call checkpoints, forbidden resume,
answer-after-decode ordering, exact local model-digest verification, and
single-root import/hash attestation through v8. Validation passed 32 focused
v8/state-machine tests, 94 exposed frame/runner regressions, 290
pinned-interpreter tests with 5 skips, and 313 host tests. Only
`GET /api/tags` and no-inference `--help` were invoked; answers were not
read. V8 remains `opened=false`, `consumed=false`; no semantic outcome or
downstream stage is admitted. Evidence:
`experiments/20260804T192000Z-frame-oracle-v8-source-behavior-audit-r4/` and
`experiments/20260804T212000Z-frame-oracle-v8-behavior-implementation-clean/`,
`experiments/20260804T232548Z-frame-oracle-v8-runner-provenance-freeze/`;
contract: `docs/frame_oracle_v8_behavior_spec_20260804.md`.

The first exact v8 argv attempt exposed a pre-inference provenance defect and
failed closed before runner entry. Commit `b54fdcc` records the pinned wrapper
as mode `100644`, while the frozen manifest executes it directly; `/usr/bin/env`
therefore exited 126 with `Permission denied`. The repeat preflight had passed
32 focused, 94 exposed, and 290 pinned tests with 5 skips, but no gate output
or import-provenance sidecar was created. The public contract remained
byte-identical with `opened=false`; no answer access, case/proposal/response
inspection, state transition, or model generation occurred. V8 is unopened
and scientifically unconsumed, but the current manifest is revoked and must
not be retried. A separate isolated repair must change only the wrapper Git
mode to `100755`, directly test the exact no-inference argv boundary, attest
file mode, refreeze cleanly, and stop before opening. Evidence:
`experiments/20260805T013037Z-frame-oracle-v8-one-use-gate/`; contract:
`docs/frame_oracle_v8_execution_permission_repair_contract_20260805.md`.

The bounded executable-provenance repair is now frozen unopened at clean
isolated commit `96460e9`. The wrapper bytes and all semantic, prompt, schema,
decode, public, answer-commitment, and model commitments are unchanged; only
its Git mode changed to `100755`, alongside a regression that executes it
directly through `/usr/bin/env` with `--help`. Validation passed 33 focused,
95 exposed, 291 pinned tests with 5 skips, and 314 host tests. The replacement
manifest attests Git/filesystem modes `100755`/`0755`, exact worktree import
provenance, and `opened=false`, `consumed=false`. Only local `GET /api/tags`
and no-inference `--help` ran; the answer file was not read. The revoked
`b54fdcc` manifest remains permanently ineligible. A later fresh turn may
reverify and execute only the replacement manifest argv once. Evidence:
`experiments/20260805T042743Z-frame-oracle-v8-execution-permission-repair-freeze/`.

The replacement-manifest v8 one-use scientific gate has now completed and
failed closed. Clean reverification passed 33 focused, 95 exposed, and 291
pinned tests with 5 skips. The exact command then durably crossed the
consumption boundary and completed all 48 calls: all 24 rows were valid, 21
were paired-deterministic, and 15 were exact. Required modality, negation,
state, and world-knowledge strata were imperfect, so the terminal state is
`consumed_failed`. V8 is permanently consumed negative evidence; no label,
readout, substitution evaluation, or semantic loss is admitted, and the raw
artifact must not be used for tuning. Evidence:
`experiments/20260805T064745Z-frame-oracle-v8-one-use-gate-r2/`.

A fresh 24-case v9 successor is process-sealed at
`sealed/frame-oracle-v9/`. Integrity verifies its committed answers, all five
predicates and frozen coverage counts, `opened=false`, and zero exact sentence
overlap with v1--v8 plus offline-readout-v1. V9 is process-sealed and
exact-case-disjoint, not strictly outcome-blind, because its author knew only
v8 aggregate/per-stratum counts. No v9 oracle call or implementation occurred.
Evidence:
`experiments/20260805T070000Z-frame-oracle-v9-sealed-contract/`; contract:
`docs/frame_oracle_v9_fresh_gate_contract_20260805.md`.

The bounded source-only v9 behavior audit is complete without reading v8
opened material or any v9 case/answer. At clean v8 commit `96460e9`, three
independent fixtures show that v8 emits non-unknown semantic keys when
`entity_a`, `entity_b`, or both have no exact boundary-delimited occurrence in
the sentence; an occupied control was unchanged. The baseline passed 20
focused tests and 291 full tests with 5 skips. The frozen fail-closed
surface-grounding rule is now implemented at clean isolated commit `9b10fdc`:
each canonical non-unknown slot must have an exact inherited-pattern match in
the whitespace-normalized sentence or the result becomes canonical unknown
with confidence preserved. Clean acceptance passed 25 focused, 146 exposed,
and 316 full tests with 5 skips. The separate atomic-runner and exact
source/import/model provenance freeze is now complete at clean isolated commit
`8edead5`. It preserves pre-request durable consumption, per-call
checkpoints, forbidden resume, answer-after-decode ordering, exact local model
digest rejection, and one-root v2--v9 import/hash attestation. Corrected clean
acceptance passed 39 focused, 162 exposed, 330 pinned full tests with 5 skips,
and 353 host tests. Only local `GET /api/tags` and no-inference `--help`
ran; neither sealed v9 file was accessed. V9 remains unopened and unconsumed.
Fresh-turn reverification then passed the canonical manifest, clean commit,
source hashes, prior seal identifiers, local model digest, exact argv,
pinned-wrapper provenance, 39 focused tests, 162 exposed regressions, 330
pinned full tests with 5 skips, and 353 host tests. The exact one-use argv
completed all 48 calls and terminally failed closed: all 24 rows were
schema-valid, 18/24 were paired-deterministic, and 0/24 semantic keys were
exact; every required stratum had zero exact rows. V9 is permanently
`consumed_failed`. No label corpus, readout, substitution evaluation, or
semantic loss is admitted, and opened material must not be inspected or used
for tuning. Two preceding transcription/verifier preflight defects stopped
before sealed access or inference and are preserved. The next admissible step
is to process-seal a fresh exact-case-disjoint v10 battery without consulting
v9 opened content. Evidence:
`experiments/20260805T090359Z-frame-oracle-v9-source-behavior-audit/` and
`experiments/20260805T111902Z-frame-oracle-v9-behavior-acceptance-r2/`;
`experiments/20260805T132357Z-frame-oracle-v9-runner-provenance-freeze/`;
`experiments/20260805T152703Z-frame-oracle-v9-one-use-gate-r3/`;
contract: `docs/frame_oracle_v9_behavior_spec_20260805.md`.

A fresh 24-case v10 successor is now process-sealed at
`sealed/frame-oracle-v10/`. Final integrity passed committed-answer alignment,
all five closed predicates, the frozen abstention/modality/negation/location/
world-knowledge coverage counts, `opened=false`, and zero exact sentence
overlap against v1--v9 plus offline-readout-v1. The author knew only v9
aggregate and per-stratum counts; v9 comparison occurred only inside a
non-identifying exact-set validator, so v10 is process-sealed and
exact-case-disjoint rather than strictly outcome-blind. The first integrity
attempt reported one unnamed overlap; a uniform neutral prefix was then
applied to all 24 v10 sentences without learning the collided identifier, and
the complete contract passed. The unchanged clean v9 implementation also
passed 162 exposed and 330 pinned tests with 5 skips. No v10 implementation,
inference, label corpus, readout, substitution evaluation, or semantic loss
was admitted. The next admissible step is a fresh-turn bounded source-derived
v10 behavior audit using independent fixtures, without accessing v10 answers.
Evidence:
`experiments/20260805T172833Z-frame-oracle-v10-sealed-contract-r3/`;
contract: `docs/frame_oracle_v10_fresh_gate_contract_20260805.md`.

The permitted source-only v10 behavior audit is now complete on clean isolated
branch `agent/frame-oracle-v10-source-audit` at parent commit `8edead5`. Four
independent fixtures showed that v9 accepts surface-grounded proposals whose
predicate contradicts an overt relation or whose directed slots are reversed;
four matching controls were unchanged. The audit passed 25 focused, 162
exposed, and 353 full host tests. This source capability gap is not asserted to
have caused v9's aggregate failure. A finite negative overt-template
consistency rule is frozen for later implementation; v10 remains unopened and
unconsumed. Next is a separate implementation-only turn, stopping before
runner/provenance adaptation or inference. Evidence:
`experiments/20260805T192502Z-frame-oracle-v10-source-behavior-audit/`;
contract: `docs/frame_oracle_v10_behavior_spec_20260805.md`.

The frozen v10 source behavior is now implemented at clean isolated commit
`82f3ecc`. The finite negative guard recognizes only capital-of, located-in,
active authored-by, passive authored-by, and simple copular state templates in
specific-to-generic order. It returns canonical unknown with preserved
confidence when a grounded proposal contradicts an overt predicate or
directed slots, and delegates exact matches or unrecognized sentences to v9
without changing the prompt. One independent development fixture was
corrected after it mislabeled an exact generic copula as an unmatched
paraphrase; no implementation or sealed input changed. From the clean commit,
38 focused, 200 exposed, and 391 full host tests passed, plus compilation,
diff, and clean-status checks. V10 remains unopened and unconsumed. Next is a
separate runner/provenance freeze, still without inference. Evidence:
`experiments/20260805T212936Z-frame-oracle-v10-behavior-acceptance/`.

The v10 atomic runner and exact provenance contract are now frozen unopened at
clean isolated commit `ad7fe09`. The runner preserves durable pre-request
consumption, per-call checkpoints, forbidden resume, answer-after-paired-
decode ordering, exact local model-digest rejection, and one-root v2--v10
import/hash attestation. Clean acceptance passed 53 focused, 215 exposed, 383
pinned full tests with 5 skips, and 406 host tests; wrapper `--help`, prompt/
schema identity, compilation, shell, diff, clean-state, and artifact hashes
also passed. Draft audit corrections added the omitted v9 import/test coverage
and corrected a v10 hash plus one invented copular fixture before the clean
freeze. Neither sealed v10 file was read and no generation occurred. V10
remains unopened and unconsumed. Next is a separate fresh-turn revalidation,
then at most one exact manifest argv execution. Evidence:
`experiments/20260805T234401Z-frame-oracle-v10-runner-provenance-freeze/`.

The exact frozen v10 one-use gate has now failed closed and is permanently
consumed. Fresh revalidation passed the canonical manifest and argv, clean
`ad7fe09` commit, frozen sources, model digest, one-root import provenance, 53
focused tests, 215 exposed tests, 383 pinned tests with 5 skips, and 406 host
tests. The single argv completed 48/48 calls and terminally recorded
`consumed_failed`: 24/24 schema-valid, 17/24 paired-deterministic, and 12/24
exact. Only abstention and paraphrase strata were perfect; all other required
strata failed. No labels, readout, substitution evaluation, or semantic loss
is admitted, and opened v10 material is not a tuning source. The next
semantics-lane obligation is to process-seal a fresh v11 battery without
consulting v10 opened content. Evidence:
`experiments/20260806T030955Z-frame-oracle-v10-one-use-gate/`.

Frame-oracle v11 is now process-sealed and unopened. The fresh battery has 24
aligned unique cases with frozen counts: four direct, six explicit-negation,
five possible, one paraphrase, four abstention, and four world-knowledge-trap
cases; all five predicates and five `located_in` frames are represented. Its
answer commitment matched, `opened=false` held, and automated non-identifying
comparison found zero exact sentence overlap against v1--v10 plus
offline-readout-v1. The unchanged clean v10 source passed 215 exposed tests
and 383 full tests with 5 skips. No opened v10 content, v11 model call,
implementation, label/readout/substitution stage, or semantic loss was used.
Next is at most one fresh-turn source-derived behavior audit with independent
fixtures, still without opening v11. Evidence:
`experiments/20260806T051159Z-frame-oracle-v11-sealed-contract/`.

The permitted source-only v11 behavior audit is complete. Clean v10 accepted
4/4 independently invented terminal questions as non-unknown frames across
`capital_of`, `located_in`, `authored_by`, and `state`, despite the inherited
prompt requiring questions to abstain; 4/4 matched declarative controls were
preserved. Focused, exposed, and full host suites passed 38, 215, and 406
tests. Freeze only the finite terminal-ASCII-`?` fail-closed rule for a later
implementation turn. This is a source capability counterexample, not evidence
about v11 contents or a causal diagnosis. V11 remains unopened and unconsumed.
Evidence:
`experiments/20260806T071142Z-frame-oracle-v11-source-behavior-audit/`.

The frozen v11 terminal-question behavior is now implemented at clean
isolated commit `b76d957`. The bounded wrapper validates the proposal envelope,
preserves inherited v10 unknown/abstain behavior, and canonicalizes only valid
non-unknown proposals whose source ends in ASCII `?` after trailing-whitespace
removal. All other inputs delegate to v10 and the prompt remains identical.
Independent focused, exposed, and full suites passed 30, 245, and 436 tests;
compilation, diff, and clean-state checks also passed. One initial development
wrapper invocation failed before collection because it lacked an explicit
worktree `cd`; only the wrapper was repaired. V11 remains unopened and
unconsumed. Runner/provenance adaptation is a separate future step; no
inference or downstream semantic stage is admitted. Evidence:
`experiments/20260806T091116Z-frame-oracle-v11-behavior-acceptance/`.

The v11 atomic runner and provenance contract are now frozen at clean isolated
commit `46c16f0`. It preserves pre-request durable consumption, per-call
checkpoints, forbidden resume, answer-after-paired-decode ordering, exact local
model-digest rejection, and one-root source/import attestation through v11.
Independent acceptance passed 46 focused, 261 exposed, 452 host, and 429
pinned-interpreter tests with 5 skips. The canonical manifest SHA-256 is
`9745561dd25220d35e047fa4930714a118c85d0fc5ac8eef954edb0296625738`.
Neither sealed file was read and no generation request occurred, so v11 remains
unopened and unconsumed. A fresh successor must reverify the exact manifest and
may execute its frozen argv at most once. Evidence:
`experiments/20260806T111606Z-frame-oracle-v11-runner-provenance-freeze/`.

The exact frozen v11 one-use gate has now failed closed and is permanently
consumed. Fresh revalidation passed the canonical manifest and argv, clean
`46c16f0` commit, frozen sources, model digest, one-root import provenance, 46
focused tests, 261 exposed tests, 429 pinned tests with 5 skips, and 452 host
tests. The single argv completed 48/48 calls and terminally recorded
`consumed_failed`: 24/24 schema-valid, 21/24 paired-deterministic, and 0/24
exact, with zero exact rows in every required stratum. No opened row content,
label corpus, readout, substitution evaluation, or semantic loss is admitted,
and the aggregate result does not establish a causal diagnosis. The next
semantics-lane obligation is to process-seal a fresh v12 battery from the
inherited ontology and coverage contract without consulting v11 opened
content. Evidence:
`experiments/20260806T131410Z-frame-oracle-v11-one-use-gate/`.

Frame-oracle v12 is now process-sealed and unopened. Its 24 aligned unique
cases pass the inherited closed categorical schema, committed-answer
alignment, frozen counts of four direct, six explicit-negation, five possible,
one paraphrase, four abstention, and four world-knowledge-trap cases, and
exactly five `located_in` frames. The public gate remains `opened=false`; a
non-identifying comparison found zero exact sentence overlap against v1--v11
plus offline-readout-v1. Clean v11 source also passed 261 exposed and 429
pinned tests with 5 skips. V12 is exact-case-disjoint and process-sealed, not
strictly outcome-blind. No inference or downstream semantic stage occurred.
Next is one fresh-turn bounded source-derived behavior audit with independent
fixtures and no v12 answer access. Evidence:
`experiments/20260806T151513Z-frame-oracle-v12-sealed-contract/`; contract:
`docs/frame_oracle_v12_fresh_gate_contract_20260806.md`.

The bounded v12 source audit has now reproduced a finite multi-proposition
capability gap without accessing v12. Four independent comma-`and`
coordinations spanning every non-unknown predicate remained non-unknown and
matched their one-proposition controls. Clean `46c16f0` passed 46 focused,
261 exposed, 429 pinned tests with 5 skips, and 452 host tests. This does not
show that v12 contains coordinated clauses or diagnose any prior result. The
next semantics-lane step is a separate isolated implementation of only the
frozen masked-remainder `,\s+and\b` guard, stopping before runner adaptation
or inference. V12 remains unopened and unconsumed. Evidence:
`experiments/20260806T171519Z-frame-oracle-v12-source-behavior-audit/`;
contract: `docs/frame_oracle_v12_behavior_spec_20260806.md`.

The frozen v12 coordination behavior is now implemented at clean isolated
commit `9bab920`. The normalizer validates the proposal envelope, preserves
raw unknown/abstain handling, applies inherited canonical slot normalization
and all-occurrence case-insensitive surface masking, and recognizes only ASCII
`,\s+and\b` in the masked remainder. Independent fixtures cover every
non-unknown predicate, matched controls, delimiters wholly within either slot,
excluded coordinator surfaces, unmatched proposals, inherited question and
unknown behavior, invalid envelopes, confidence, and prompt identity. Clean
acceptance passed 33 focused, 294 exposed, 462 pinned tests with 5 skips, and
485 host tests. V12 remains unopened and unconsumed; next is a separate
runner/provenance freeze, not inference. Evidence:
`experiments/20260806T191425Z-frame-oracle-v12-behavior-implementation/`.

The v12 atomic runner and provenance contract are now frozen unopened at clean
isolated commit `228ff13`. It preserves durable pre-request consumption,
per-call checkpoints, forbidden resume, answer-after-paired-decode ordering,
exact local model-digest rejection, and one-root source/import attestation
through v12. Clean acceptance passed 50 focused, 311 exposed, 502 host, and
479 pinned-interpreter tests with 5 skips. The canonical manifest SHA-256 is
`8f7099a100389e82b700c542f16081427ebb3b706a083e34b21f30af8aa462f6`.
An automation-cell continuation caused two noncanonical invocations to overlap
only in their captured log tail; a subsequent isolated unchanged invocation
passed and reproduced the same manifest/provenance hashes. Neither sealed file
was read and no generation request occurred, so v12 remains unopened and
unconsumed. A fresh successor may revalidate the exact manifest and execute
its frozen argv at most once. Evidence:
`experiments/20260806T211608Z-frame-oracle-v12-runner-provenance-freeze/`.

The exact frozen v12 one-use gate has now failed closed and is permanently
consumed. Fresh preflight revalidated clean commit `228ff13`, canonical
manifest/argv, frozen source/import/model provenance, the unopened seal, 50
focused tests, 311 exposed tests, 479 pinned tests with 5 skips, and 502 host
tests. The sole argv completed all 48/48 calls and terminally recorded
`consumed_failed`: 24/24 schema-valid, 18/24 paired-deterministic, and 4/24
exact; no required stratum was perfect. Aggregate stdout unexpectedly included
case-level failure identifiers, which were surfaced during aggregate review;
they did not inform diagnosis or tuning and are forbidden successor inputs.
No labels, readout, substitution evaluation, or semantic loss is admitted.
This created the obligation to process-seal v13 from the inherited ontology
and coverage contract without consulting v12 opened content or surfaced
identifiers.
Evidence:
`experiments/20260806T231440Z-frame-oracle-v12-one-use-gate/`.

Frame-oracle v13 is now process-sealed, unopened, and unconsumed. Its 24
aligned unique cases pass the inherited closed categorical schema, answer
commitment, frozen counts of four direct, six explicit-negation, five
possible, one paraphrase, four abstention, and four world-knowledge-trap
cases, all five predicates, and exactly five `located_in` frames. The
non-identifying freshness comparator reported zero exact sentence overlap
against v1--v12 plus offline-readout-v1. Clean v12 commit `228ff13` passed 311
exposed tests and 479 pinned tests with 5 skips. No v12 opened content or
surfaced identifier informed the battery. A fresh successor may perform at
most one bounded source-derived v13 behavior audit using independent fixtures,
without answer access or inference. Evidence:
`experiments/20260807T012715Z-frame-oracle-v13-sealed-contract/`.

The bounded v13 source-behavior audit falsified its preregistered hypothesis
without adaptation. Contrary to the expected gap, all four independently
invented exact-template semicolon-`and` sentences already became canonical
unknown through the inherited v10 whole-sentence template guard; 0/4 remained
non-unknown. The conditional `;\s+and\b` rule is rejected and no implementation
is admitted. Separate unchanged-source verification passed 50 focused, 311
exposed, 479 pinned tests with 5 skips, and 502 host tests. V13 remains unopened
and unconsumed. Any later audit must be a fresh preregistration with independent
fixtures and no sealed access. The run record discloses one pre-freeze lookup
of a presumed contract pathname that was absent and returned no content.
Evidence:
`experiments/20260807T032523Z-frame-oracle-v13-source-behavior-audit/`.

The frozen v13 one-use gate subsequently failed closed. Fresh preflight
verified the exact clean manifest/argv, source/import/model provenance, prior
seal, and all batteries. The single invocation completed 48/48 calls and
terminally recorded `consumed_failed`: 24/24 schema-valid, 20/24
paired-deterministic, and 15/24 exact, with only abstention and paraphrase
strata perfect. V13 is permanently retired; no labels, readout, substitution
evaluation, or semantic loss is admitted. Aggregate stdout unexpectedly
surfaced case-level failure identifiers; they informed no diagnosis and are
forbidden successor inputs. The next semantics obligation is a fresh v14 seal
derived only from the inherited ontology and coverage contract. Evidence:
`experiments/20260807T132600Z-frame-oracle-v13-one-use-gate/`.

At `2026-08-08T13:23Z`, a provider-free, no-inference preflight identified the
already-installed local `qwen2.5:7b` as an artifact-level Stage-A author
candidate. The Ollama executable, model manifest, config, and all model-layer
blobs were SHA-256 verified; Bubblewrap is present. Clean `8108d98` passed 30
focused and 357 broader exposed tests. This does not establish final author
eligibility or authorize a launch: runtime-closure isolation, fresh-context
receipts, and noninteractive bundle emission remain unverified. V14 remains
sealed, unopened, and unconsumed. Evidence:
`experiments/20260808T132900Z-frame-oracle-v14-local-author-preflight-r2/`.

The next semantic-free transformer rung produced a mixed result. Pure WTA
substantially improved planted continuation coverage but lost a contextual mode
on two of three seeds. Context-balanced WTA recovered both modes in both
contexts on all fresh seeds. Balanced T=1 passed the quantitative gate 3/3;
balanced ePC T=4 passed 2/3 and missed once, so the current ePC configuration
remains unadmitted. Evidence:
`experiments/20260801T154000Z-tiny-transformer-explorative-epc/` and
`experiments/20260801T160000Z-tiny-transformer-balanced-exploration-v2/`.

The repaired frame oracle succeeded at v3. Closed Qwen proposals alone still
failed v2 exactness, but deterministic normalization of slots, explicit
negation, and abstention yielded 8/8 valid, deterministic, exact normalized
frames on a fresh battery. This admits a bounded offline label stage only.
Evidence: `experiments/20260801T153000Z-frame-oracle-v2/` and
`experiments/20260801T154800Z-frame-oracle-v3/`.

The first local frame-oracle admission gate failed closed: `qwen2.5:7b`
returned schema-valid JSON on all eight known-answer cases but only two exact
canonical frames, with one nondeterministic repeat and several ontology,
polarity, and abstention failures. No oracle labels or readout training are
admitted. Evidence:
`experiments/20260801T145700Z-frame-oracle-schema-audit/`.

On 2026-08-01, the semantic-free explorative ePC known-answer gate passed.
Winner-assigned two-head continuation distillation recovered both planted
coherent modes across three seeds and reduced prototype-coverage MSE from
about `0.9995` to `0.000227`, with exact replay and monotone ePC energy.
T=1 and ePC T=4 were nearly identical, so the result validates exploration
plumbing but not an ePC advantage. Assignment entropy falsely appeared healthy
for collapsed marginal heads, requiring explicit diversity/coverage metrics in
future tests. Evidence:
`experiments/20260801T151100Z-explorative-epc-baseline/`.

On 2026-08-01, a separate CPU-only semantic-substitution quantale scorer seam
passed its controlled fixture at product and Schweizer--Sklar `p=0.05,0.5,1.5`.
It validates bounded, deterministic, contradiction-sensitive aggregation only;
it has no language-semantic or distillation outcome and does not alter the
completed clean-room robustness conclusion. Next prerequisite is calibration
of a frozen teacher-feature adapter before integration into an explorative ePC
objective. Evidence:
`experiments/20260801T141949Z-semantic-substitution-quantale-scorer/`.

The immediate GPT-2 adapter calibration then failed closed: although all four
aggregators kept identity > paraphrase > unrelated, the factual contradiction
scored above unrelated. The frozen hidden-state plus next-token-distribution
features are therefore not admitted to an ePC/XM loss. Evidence:
`experiments/20260801T143000Z-gpt2-semantic-substitution-adapter/`.

The approved reliability-first clean-room robustness run completed and failed
its frozen primary gate. Across fresh seeds 9107/9311/10753, ePC lost to
wall-clock-matched ordinary KD on PTB OOD by `-1.9135758082` nats on average
(only 1/3 positive); WikiText ID was also negative at `-1.0506251653` nats
(1/3 positive). All three records passed their frozen validators, local
aggregation exactly reproduced the returned summary, and all four sealed
artifact hashes verified. The RunPod pod was terminated and confirmed absent.
This is negative evidence for this frozen clean-room configuration, not a
general refutation of ePC. Evidence:
`experiments/20260801T063754Z-epc-robustness-reliability-run/`.

On 2026-07-30 the distinct clean-room robustness v1 preparation completed on
`agent/cleanroom-robustness-v1` at `5d45e84`. A separate GPU runner now
evaluates every frozen arm on pinned WikiText validation and PTB validation,
hashes each ordered token plan canonically, preserves the earlier paired
training/wall-clock/replay invariants, and aggregates fail-closed. The broader
local gate passed 178 tests plus compilation, shell, JSON, and diff checks.
No PTB outcome exists yet. The approved 2026-07-30 remote attempt passed its
CUDA/bootstrap checks but failed closed before seed execution: the pinned
`ptb_text_only` loader required explicit `trust_remote_code=True` in the
noninteractive process. Available evidence was retrieved and hashed; no seed
record or summary exists. A retry requires a reviewed loader change, a
noninteractive fixture, and fresh compute approval. Evidence:
`experiments/20260730T212810Z-cleanroom-robustness-v1-gpu/`.

On 2026-07-29 Ben directed two parallel next steps: stop waiting for Mesto's
unshared production bundle and have Fable build an independently designed,
provenance-explicit clean-room V4-1 implementation; meanwhile execute the
clean-room settlement-depth evidence track. The T in {1,2,4,8} sweep is frozen
and locally validated at commit `68d7bc2` (162/162 full tests). It reuses the
three seeds already observed at T=4, so its outcome is explicitly descriptive
and calibrational. Ben approved the USD 10/14h29m Secure RTX 4090 run on
2026-07-29. The first request lacked capacity; a later allocated pod never
provided an SSH endpoint, did no work, and was deleted at an estimated USD
0.13. Ben then directed an SSH-free bootstrap route; validate that transport
before a future launch. Evidence:
`experiments/20260729T132715Z-clean-room-settle-sweep-gpu/` and
`docs/ssh-free-runpod-bootstrap-v1.md`.

The separately frozen fresh-seed confirmation completed on 2026-07-30 at
commit `0b20717`. Across untouched seeds 9107/9311/10753, T=4 settled ePC beat
ordinary KD run for the same measured training wall-clock on all three seeds:
mean held-out KD gain `+2.629789352416992` nats. All checksums, schemas,
finite-objective checks, exact replays, and frozen invariants passed, and
reaggregation exactly matched the stored summary. This is a clean-room
protocol result, not a reproduction of Mesto's unpublished production system.
The RunPod pod was deleted and verified absent. Evidence:
`experiments/20260730T073441Z-cleanroom-confirm-v1-gpu-retry/`.

On 2026-07-27 Ben supplied a C4′ companion note connecting the V4
commutator critic to Mesto's reported function-pinned PC--GPT-2 homotopy. It
is preserved at `../../library/commutator-critic-c4prime-2026/`. The proposal
is not yet executable: a later Mesto pointer to the public GPL
`MesTTo/metta-on-mork` repository revealed genuine toy `2-2-2` XOR ePC/MORK
settle and local-update code, but inspection of both visible branches/history
found no committed production PC--GPT-2 trainer or checkpoints. The exact
production path/assets therefore remain unidentified. In addition, the
Torch optimizer-replica admission gate remains failed, JAX exact-D is
unreproduced, and no 45-A100-hour run is approved.

The causal-critic persistent-agent plan is now explicitly staged as V4-0
backend admission, V4-1 target-asset/T=1 adapter validation, V4-2 frozen C4′
preregistration and measured microprofile, then a separately approved V4-3
deployment.  This preserves the C4′ conceptual opportunity without treating
author-reported homotopy results as a runnable substrate or opening C2/policy
work prematurely.  See `docs/causal_critic_v4_c4prime_execution_plan_20260727.md`.

Earlier RelaLeap phases did not justify promotion:

1. `v0` seven-arm posthoc pregate was a reproducible smoke scaffold only: small toy data, handcrafted LLC proxy, and no arm beat required null controls.
2. `v2` parameterized arms fitted to cached residuals improved engineering realism but deployable mechanisms failed winner recovery, lost to controls, and failed null specificity.

Ben's 2026-07-03 directive is to **try a new train-time causal factor approach**. The preregistration is recorded at `docs/train_time_causal_factor_preregistration.md`.

Ben's 2026-07-04 directive: make SLT estimator validation the current focus for RelaLeap. Once all estimators are validated on a Tiny Shakespeare level corpus, proceed with the prior idea of using SLT to help guide the residual layer on top of the transformer.

Ben's 2026-07-09 directive supersedes the sequencing, not the validity requirements: try the HDPC/ePC plan first on Tiny Shakespeare, using Runpod compute resources after explicit bounded approval; afterwards consider upgrades using (1) SLT inputs to the process and (2) columnar models for the residual layer.

2026-07-07 implementation status: first-wave SLT estimator sub-branches had already been created by ProtoCosmoBot / related subagents. They were integrated locally into `agent/slt-integration` at commit `6dca8eb`, with 66 tests passing and 7 adversarial-review xfails. The integration includes SGLD/WBIC core, analytic calibration registry, prior/MAP sensitivity helpers, RelaLeap-shaped benchmark fixtures, and adversarial review tests/docs. This is still validation infrastructure, not validated Tiny Shakespeare SLT evidence.

The isolated `agent/tinyshakespeare-hdpc` worktree now contains the original CPU
toy scaffold plus a tested block-state transformer ePC objective and matched
Tiny Shakespeare diagnostic runner. Current head is `65666f9`; 110 full tests
pass at the normalized-objective commit. Two diagnostic-scale three-seed gates
have failed scientific promotion against ordinary KD, so this is implementation
and null-result evidence, not HDPC/ePC efficacy.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Active RelaLeap implementation | not pushed from this workspace | `projects/relaleap/repos/relaleap`; integration worktree `projects/relaleap/worktrees/slt-integration` | `agent/slt-integration` | `6dca8eb` |
| Tiny Shakespeare ePC diagnostic | not pushed from this workspace | `projects/relaleap/worktrees/tinyshakespeare-hdpc` | `agent/tinyshakespeare-hdpc` | `65666f9` (v2 preregistration; normalized objective `cbe4c08`) |

## Environments

No local implementation environment is required for this preregistration. No GPU, paid compute, or remote resources were used.

## Key results

- 2026-07-29: Replaced the unavailable-production-bundle dependency for the
  clean-room engineering track with Fable's independently specified V4-1
  transformer homotopy/ePC trainer. The only update mode is explicitly
  `hybrid_settled_global_adamw`, not a claimed fully local or Mesto-compatible
  rule. Exact T=1 serialized-snapshot equivalence, deterministic multi-step
  replay, frozen settlement, monotone finite energy, exact counters, and
  fail-closed gates pass. Tests: 9 focused, 21 seam, 165 full; compilation and
  `git diff --check` pass. Commit `3a38eb1`; evidence:
  `experiments/20260729T084053Z-v4-1-cleanroom-homotopy-fable/`.

- 2026-07-28: Frozen and CPU-validated the next actual clean-room GPU
  comparison at commit `6f8cc21`: three fixed seeds compare a T=1 KD endpoint
  with four-step activity settlement from identical model/AdamW/RNG/batch
  snapshots, with a second ePC replay required to be byte-identical and
  held-out public WikiText KD reported. The focused suite passed 12/12 and the
  full suite 156/156. This is ready for a separately approved GPU run, but is
  still a clean-room KD-only comparison rather than Mesto reproduction or a
  C4-prime deployment. Evidence:
  `experiments/20260728T201400Z-clean-room-transformer-epc-multistep-preflight/`.

- 2026-07-28: The separately approved RTX 4090 engineering smoke for
  `clean_room_transformer_epc_v1` succeeded and the pod was terminated after
  verified artifact retrieval. A six-layer GPT-2-width student (81.3M
  parameters) and frozen GPT-2 teacher (124.4M) completed one T=1 step using
  3.14 GB peak CUDA allocation; frozen settlement and byte-identical
  snapshot/restore replay both passed. This is an execution/VRAM result only,
  not training-efficacy or Mesto-compatibility evidence. Source commit:
  `b86e156`; evidence:
  `experiments/20260728T195248Z-clean-room-transformer-epc-gpu-smoke/`.

- 2026-07-28: Completed the local transformer-scale PCStep engineering
  preflight at commit `19e1022` on `agent/v4-gpt2-pcstep`. The packaged seam verifies frozen
  weights during GPT-2 block-state settlement, applies exact Boolean block
  gates only at the update phase, and captures/restores model, AdamW, RNG,
  step, and batch-cursor state with deterministic replay. Eleven focused
  adapter tests, 30 broader GPT-2/pilot tests, and the complete 155-test suite
  passed. This is explicitly `clean_room_transformer_epc_v1`: settlement is
  followed by global autograd/AdamW, not a claimed reconstruction of Mesto's
  absent transformer-local rules. Evidence:
  `experiments/20260728T184216Z-v4-1-gpt2-pcstep-preflight/` and
  `experiments/20260728T184406Z-v4-1-gpt2-pcstep-full-suite/`.

- 2026-07-28: The frozen V4-0 nonlinear Torch functional gate completed but
  is INCONCLUSIVE. The >=5-sigma family-admission precheck passed B1 input
  permutation (5.741) but failed B2 output shift (3.033) and B1 high-LR
  stress (0.868). Descriptively, `approximate_full_state_AD` Spearman was
  .969-.9999 across nonlinear cells and non-inferior to frozen-D throughout;
  the high-LR h25 comparison was .969 versus .196. The aligned zero-gradient
  control produced 0% false beneficials. This is not Torch admission.
  Evidence:
  `experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`.
  Ben subsequently accepted the result as sufficient to enter V4-1 exact-asset
  intake and `T=1` adapter validation. This is an authorized progression
  decision, not a revision of the preregistered INCONCLUSIVE verdict; no Mesto
  production assets are locally available yet. Contract:
  `docs/v4-1_asset_intake_contract_20260728.md`.

- 2026-07-27: Ben supplied *The Commutator Critic* v1.1, sandbox, and
  `comcrit` skeleton/patch package. The local CPU audit reproduced the complete
  quadratic JSON byte-for-byte, including the per-state truth, synergy,
  insufficient-statistics, and margin-decay demonstrations. The package is not
  yet integration-ready: JAX-dependent exact-D claims remain supplied-only,
  and all four PyTorch optimizer-replica bit-exactness gates failed on Torch
  2.12.1 (`5 passed, 4 failed, 1 skipped`). This supports the V4 conceptual
  pivot but blocks the Torch backend and any C2/policy claim. Evidence:
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/` and
  `../../library/commutator-critic-v1-1/`.

- 2026-07-25: The frozen co-learned global causal critic Phase-0
  confirmation failed estimation and stopped before policy interpretation.
  Spearman and randomized coverage passed in all four analytic families, the
  synergy global critic reduced pair-action MAE by 21.0% versus the
  independent critic, and the null false-benefit rate was 0%. However, ECE was
  .222-.287 in every family, synergy sign AUROC was .223, and strict baseline
  dominance failed in the exactly linear local/null fixtures. The null family
  also has no positive labels, making its frozen AUROC gate unidentified, and
  the analytic fixture exposes no gradient/activation state for the policy
  credit/rank gate. Do not interpret policy summaries or run Shakespeare.
  Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T063000Z-colearned-causal-critic-phase0/`.

- 2026-07-25: Implemented the co-learned global causal critic v1 core at
  commit `690c8f7` on `agent/colearned-causal-critic-v1`. The implementation
  includes decision-time feature validation, randomized logged interventions,
  exact learner/optimizer/Python/NumPy/Torch RNG paired restoration, bounded
  training/audit replay, joint module-token and independent critics,
  uncertainty-aware conservative fallback, counterfactual coverage/calibration
  reports, and local/downstream/synergy/null fixtures. Sixteen focused tests
  and the full 448-test suite passed (1 skipped). This is implementation
  evidence only; critic calibration, policy value, and Shakespeare remain
  untested. Evidence:
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`.

- 2026-07-25: Drafted a preregistered co-learned global causal critic v1
  protocol in response to the v3 support-routing null. The critic is trained
  online from randomized, common-RNG paired update interventions and predicts
  held-out retention/plasticity outcomes over the whole module set. Support,
  curvature, and commutator diagnostics are features rather than imposed
  utility labels. Synthetic local, downstream, synergy, and null fixtures gate
  a contingent local Shakespeare phase; no implementation or execution has
  occurred. Evidence:
  `docs/colearned_global_causal_critic_protocol_v1.md` and
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`.

- 2026-07-26: Corrected curvature confirmation v3 passed all seven planted
  Phase-0 gates on untouched seeds. Support AUC was 1.0, every module had
  nonzero squared Hutchinson overlap and nonzero `H_B g_A - H_A g_B`, own-task
  pathways were load-bearing, and oracle forgetting was .0697 versus .2010.
  Signed curvature included both cooperative and antagonistic interactions,
  while cross-task ablations were facilitative/suppressive classifications.
  The contingent 15-arm local Shakespeare run then failed its promotion gate:
  full-causal forgetting and finite-update commutator were both worse than
  ordinary ePC. This validates the planted estimator diagnostics but does not
  justify real-text promotion or scale-up. Evidence:
  `experiments/20260726T025745Z-online-causal-epc-v3/`.

- 2026-07-26: The overlapping-vocabulary planted fixture v2 stopped
  fail-closed. It repaired exact architectural disjointness: both tasks had
  nonzero gradients through both paths, support AUC was 1.0, dominant
  own-task ablations were load-bearing, and oracle forgetting improved from
  .2935 to .1172. However, signed mixed-Hessian traces were negative for some
  modules/seeds and the minority block's Task-A ablation effect exceeded .05
  nat. Phase 0 failed; Shakespeare was not run. Evidence:
  `experiments/20260726T023651Z-online-causal-epc-v2/`.

- 2026-07-26: The online multi-signal/soft-gate planted Phase 0 stopped
  fail-closed. Support AUC was 1.0 and oracle gates acted correctly, but the
  protected-block mixed Hessian was already identically zero and exact
  ablations showed the trained planted pathways were not reliably
  load-bearing. The full suite passed 429 tests (1 skipped); Shakespeare was
  not run. Evidence:
  `experiments/20260726T080000Z-online-causal-epc/`.

- 2026-07-26: A preregistered five-arm, three-seed local CPU experiment added
  exact block/head interventions, estimated and true-label support, causal
  gradient gates, clarity pressure, and a differentiable commutator proxy to
  matched-mass complementary-teacher ePC. All 15 records and invariants
  completed, with 424 post-run tests passing. The full arm reduced the direct
  finite commutator by about 11.8% and preserved Task-B loss, rank, and the
  two-block credit wavefront, but worsened Task-A forgetting and did not reduce
  pre-gate off-support leakage. The 6/6 joint promotion gate failed 4/6.
  Estimated supports were seed-unstable, and the true-label oracle did not
  yield a functional advantage. Require a planted modular support fixture
  before another Shakespeare routing run. Evidence:
  `experiments/20260726T003000Z-causal-coding-epc-5arm/`.

- 2026-07-25: A preregistered three-seed, five-arm local CPU experiment tested
  CMCP-guided distillation with and without two-step ePC using 2,000-update
  Tiny Shakespeare students and a frozen CL/representation/robustness battery.
  All normalized-mass and ePC-monotonicity invariants passed. CMCP-ePC improved
  arithmetic adaptation AUC over ordinary ePC (1.994 vs 2.288; lower better)
  but worsened Shakespeare forgetting in every seed (mean 4.868 vs 3.670).
  It had higher rank than ordinary KD but lower rank than ePC and the lowest
  teacher CKA. It beat CMCP-KD only on participation ratio, not any functional
  CL endpoint, so the frozen GPT-2 promotion gate failed and no paid compute is
  justified. Evidence:
  `experiments/20260725T231807Z-cmcp-epc-cl-phase1/`.

- 2026-07-25: The five-step CMCP/ePC identification repair completed locally.
  Fixed KD mass collapsed the original contradictory-fixture arms, confirming
  zero selection-quality identification. A complementary-teacher fixture made
  independent evidence useful. Response novelty beat parameter-gradient
  novelty in calibration and, frozen before disjoint evaluation, improved
  Task-B loss over ordinary by `0.00402` while increasing Task-A forgetting.
  Two-step ePC improved plastic Task-B loss but worsened retention and doubled
  runtime, so direct KD is retained for fast calibration. Existing CAROM E2/E3
  evidence does not yet support a shared novelty-mass ledger. Evidence:
  `experiments/20260725T222650Z-cmcp-mass-normalized/` through
  `experiments/20260725T231500Z-cmcp-carom-bridge/`.

- 2026-07-21: Independent Fable and Sol R9 reviews converged on a three-stage,
  fail-closed representation battery. Low rank, low CKA, or sparsity do not
  establish disentanglement; ePC must show reduced conditional factor leakage
  and selective causal intervention effects without collapse, plus a paired
  functional benefit under an identical adaptation rule. Stage A uses the 20
  saved R8 checkpoints; new training is gated on its success. Evidence:
  `docs/reviews/2026-07-21-r9-representation-battery-synthesis.md`.

- 2026-07-19 16:40: Real-teacher no-update scale audit on seed 3253 found a
  finite credit wavefront: historical T4/lambda.05 ePC gives zero parameter
  gradient to blocks 0-3 and a total gradient norm 4.81 versus 444.38 for
  ordinary KD. T12 technically reaches all blocks, but block-0 credit remains
  negligible. Lambda 5/50 amplifies credit but causes large nonstationarity and
  poor or negative alignment, so naive high-lambda training is rejected.
  Evidence: `experiments/20260719T233948Z-epc-real-teacher-depth-scale-audit/`.

- 2026-07-19 16:33: Corrected real-data representation audit rejected the old
  D3 CKA implementation/claim. Standard centered linear CKA passed symmetry
  and feature-vs-Gram equivalence checks on identical WikiText, TinyStories,
  and random-OOD token matrices. BP checkpoints are highly similar across
  seeds on real data (within-arm mean CKA about 0.84-0.93), while ePC seed 3253
  is a late-layer geometry outlier. The robust descriptive signal is ePC's
  low centered entropy effective rank (about 2.7-3.8 in middle/final layers vs
  23-42 for BP controls). Causation remains unestablished. Evidence:
  `experiments/20260719T233244Z-epc-correctness-audit-v2/`.

- 2026-07-19 14:00: CPU diagnostic battery on 9 saved checkpoints revealed
  low random-probe rank, layer-5 weight explosion (20-40x spectral norms vs
  BP), and a U-shaped post-training CE-gradient profile. Its D3 CKA and D4
  self-teacher sweep are rejected; its causal/configuration interpretation is
  superseded by the Fable/Sol audit ladder. Evidence:
  `experiments/20260719T135900Z-gpt2-diagnostic-cpu-battery/`.

- 2026-07-19: Produced an ASCII-only reproducibility and analysis report that
  separates the six-layer source-distillation result from the independently
  completed outcome battery, summarizes the 9 raw outcome rows and bootstrap,
  provides frozen inputs/reproduction command/artifact hashes, and documents
  interpretation limits. Source/PDF:
  `docs/relaleap_gpt2_six_layer_outcome_report.tex` / `.pdf`.

- 2026-07-19: Run-4 failure-path repairs landed locally at commit `dc61f31`.
  GPT-2 evaluation now restores the explicit batch dimension, outcome loading
  resolves and validates absolute local checkpoint directories, and a versioned
  `set -euo pipefail` launcher gates Stage 2 on Stage-1 success. Focused smoke
  passed 17 tests and the complete suite passed 141 tests with compilation and
  diff checks. This is local systems evidence only; retry compute is unapproved.

- 2026-07-17: Ben selected a six-layer outcome gate followed by a contingent
  twelve-layer confirmation. Commit `7d4d4dc` makes the production runner save
  hash-manifested BP/KD/ePC checkpoints and adds the frozen scalable battery:
  WikiText-103 to TinyStories low-rank adaptation AUC/forgetting, paired
  seed/segment bootstrap, CKA, spectral rank, block skip, and corruption.
  Clean preflight `20260717T154506Z-epc-outcome-6layer-preflight` passed 138
  tests, compilation, and diff check. No RunPod resource has been provisioned;
  the bounded six-layer job awaits explicit approval.

- 2026-07-17: Following Ben's shift toward subtler outcome measures, added a
  deterministic ePC network-outcome battery at clean commit `e398876`:
  common-rule adaptation/forgetting, layerwise linear CKA, effective rank,
  block-skip sensitivity, and token-corruption robustness. All 132 tests passed.
  Local run `20260717T145830Z-epc-outcome-probe-local-v1` reproduced exactly
  (artifact SHA-256 `416bc975...5ae90`). The Tiny Shakespeare chronological
  halves were not a meaningful shift: all arms improved on both domains and
  CKA was approximately 1. Treat as an instrumentation pass and inconclusive
  effect-size pilot, not an efficacy result.

- 2026-07-16: Fail-closed audit after the aborted RunPod attempt found that the
  nominal wall-clock BP+KD control was still capped at 1,000 updates and could
  not consume the ePC time budget. Local commit `d400c15` removes that cap,
  restores preflight-hash/local-only model loading, records deterministic eval
  indices/hashes, and rejects non-finite matched-control metrics and ePC
  energies. Targeted tests passed 11/11 and the full suite 129/129. No accepted
  scientific result exists; another pod requires a fresh job record and Ben's
  explicit bounded approval. A subsequent cleanup audit found and deleted
  out-of-contract retry pod `jnjc7d7y80pxx5`; repeat provider state was empty.

- 2026-07-16: Fail-closed review of the production runner landed locally at
  `e4f2f58`. It corrected a non-time-bounded wall-clock control and two unsafe
  promotion checks, added exact matched-record and public-artifact provenance
  gates, and passed 126 full tests. A spurious automation-authored approval
  claim was withdrawn; the RunPod job remains unapproved and unprovisioned.
  This is implementation/validation evidence only.

- 2026-07-16: Production Hugging Face GPT-2 block-state ePC adaptation landed
  at local commit `0cdc70a`. A two-block GPT-2 configuration matched native
  logits and the exact depth-one KD endpoint; genuine four-state relaxation
  was monotone and produced finite earlier-block gradients. Targeted tests
  passed 19/19 and the full suite 121/121. This is implementation evidence only;
  the production runner/environment/image/runtime/approval gates remain open.

- 2026-07-16: The frozen pilot's two-layer CPU interface gate passed at local
  commit `c310230`: all three frozen seeds and BP+CE/BP+KD/ePC+KD arms ran twice,
  producing nine structured records identical outside elapsed timing. Energy
  and two-block credit diagnostics passed, and 118 full tests passed. This is
  implementation evidence only; the production Hugging Face block-state runner,
  environment lock, GPU smoke/runtime estimate, and approval are still absent.

- 2026-07-16: Frozen the minimum GPT-2-small pilot protocol with pinned public
  model/tokenizer/data provenance, a six-layer GPT-2-width student, explicit
  CE/KD/ePC and separate hidden-match arms, three fixed seeds, structured JSON
  metrics, matched update/time controls, and a pre-run promotion criterion.
  Added validation tests; 113 full tests pass. The RunPod job is an approval
  draft only; protocol commit `886acdc` is local, while the CPU same-interface
  dry-run and immutable deployment pins are
  still incomplete, so this is spec/implementation evidence only.
- 2026-07-15: Implemented a block-state transformer ePC objective and a
  matched-state BP/KD/ePC diagnostic runner (`941b8b3`; 109 full tests passed).
  The first three-seed local gate preserved the exact `T=1` KD endpoint and
  monotone energy/finite-gradient invariants, but no `T>1` arm beat matched KD
  in every seed. Mean BP perplexity was 76.2118; matched KD at lambda 0.05 was
  76.1809; ePC depths 2/4/8 at lambda 0.05 were about 76.1906. Promotion failed
  closed; longer training and crown/head stages remain blocked.
- 2026-07-15 follow-up: gradient diagnostics identified and commit `cbe4c08`
  corrected a batch-normalization mismatch that suppressed hidden local credit
  by `seq_len*d_model`. The synthetic credit invariant and 110 full tests pass.
  A separately preregistered v2 on untouched seeds increased block-1 norm ratios
  to 0.05--0.27 and produced nonzero block-0 credit at deeper inference, but
  still lost to matched KD. At lambda 0.05, mean KD perplexity was 75.1299 versus
  ePC 75.1577/75.1551/75.1503 for depths 2/4/8. The scientific gate remains
  closed.
- 2026-07-14: Added a reusable step-size sweep and diagonal gradient-variance preconditioner for SGLD tuning. Local CPU validation passed 4 focused tests and the complete 97-test suite. Production is gated on a non-divergent pilot with R-hat < 1.2 and mean ESS > 50; see `docs/sgld_tuning_plan.md` and experiment records `20260714T182809Z-sgld-step-size-sweep-targeted` / `20260714T182834Z-sgld-step-size-sweep-full-suite`.

- 2026-07-03: Created local project notebook and preregistered the train-time causal factor learner design: `projects/relaleap/docs/train_time_causal_factor_preregistration.md`.
- 2026-07-03: Drafted SLT estimation validation checklist (`docs/slt_estimation_validation_checklist.md`) with 10 operational gates: parameter block coverage, SGLD sampler diagnostics (ESS ≥ 200, CV < 0.25, ≥ 4 chains), WBIC temperature protocol (β = 1/n log n), known-singularity calibration suite (6 benchmarks with analytical RLCT), regime discriminability, null-normalized uncertainty, finite-sample wording, and promotion decision integration.
- 2026-07-03: Wrote ASCII-only LaTeX/PDF explainer `docs/slt_estimator_implementation_guide.tex` / `.pdf` describing the full estimator implementation pipeline: block masks, WBIC/SGLD sampling, diagnostics, calibration benchmarks, input coverage, module-vs-joint estimates, null-normalized uncertainty, and fail-closed promotion gates.
- 2026-07-04: Preserved Ben's uploaded `Validation of SLT Parameter Estimation for RelaLeap` plan at `docs/relaleap_slt_estimator_validation_plan.pdf` and `library/relaleap-slt-estimator-validation-plan/SOURCE.md` (SHA-256 `0c5a59f2911f1f8cafaf8aa1e3b03d5cb424a0085f4dabf3c2661a2e2707295d`). Added `docs/slt_estimator_validation_plan_summary.md`.
- 2026-07-07: Integrated first-wave SLT implementation branches into `projects/relaleap/worktrees/slt-integration` branch `agent/slt-integration` at commit `6dca8eb`: SGLD/WBIC core, analytic calibration registry, prior/MAP sensitivity, RelaLeap-shaped benchmarks, and adversarial review. Verified locally with `PYTHONPATH=src python3 -m pytest tests/ -q` (66 passed, 7 xfailed) and `git diff --check`.
- 2026-07-09: Implemented the first local HDPC/ePC invariant scaffold in `worktrees/tinyshakespeare-hdpc`: all seven planned test families are represented on a toy MLP/crown reference path; `PYTHONPATH=src python3 -m pytest tests/test_hdpc_scaffold.py -q` gave 9 passed and the full suite gave 102 passed. No remote/paid compute and no push were used.
- Source context: `library/slt-residual-layers/SOURCE.md`, `library/slt-hyperseed-synthesis/`, `library/relaleap-slt-estimator-validation-plan/SOURCE.md`, and `scratch/relaleap_gpt55_pro_final_plan.md`.

- 2026-07-10: Wrote ASCII-only LaTeX/PDF interpretation report for Tiny Shakespeare transformer SLT runs: `docs/slt_tiny_shakespeare_transformer_analysis.tex` / `.pdf`. It explains WBIC/SGLD finite-sample proxy meaning, calibration, lambda-hat, SE, ESS, Rhat, diagnostic-only blocks, per-block results, limitations, and next measurements.

## Open questions

- Where should the eventual implementation live: local `projects/relaleap/repos/`, the Mac-side RelaLeap worktree, or a new coordinated branch?
- What minimal transformer or synthetic-only harness should be used for the first train-time implementation slice?
- What Tiny Shakespeare corpus version and tokenization should be used for the first real-text SLT estimator validation runs?
- What input-count schedule and stopping rule should be used for the first WBIC/SGLD sample-size sensitivity curves? Ben's 2026-07-04 plan proposes `n = {256,512,1024,2048,4096,8192}` and slope-fitting `Delta E_n = a log n + b log log n + c`.
- Which finite-sample WBIC/LLC calibration suite should be implemented first? The 2026-07-04 plan expands the suite to include exact Gaussian posterior, product singularity, nonzero product ridge, cusp/crossing singularities, composition benchmarks, and RelaLeap-shaped cases.

## Related projects and concepts

- SLT and residual layers library record: `library/slt-residual-layers/SOURCE.md`.
- Broader SLT/Hyperseed synthesis material: `library/slt-hyperseed-synthesis/`.
- RelaLeap Mac-side prior work referenced in memory entries from 2026-07-02 and 2026-07-03.

## Risks

- Reconstruction or task-loss gains may be mistaken for causal factorization.
- Sparse columns may merely encode capacity, router frequency, or low-rank structure unless matched controls are strict.
- LLC/WBIC estimates are finite-sample proxies and require calibration before interpretation; never clip negative lambda estimates, and fail/downgrade if MAP reference, sampler target, or Monte Carlo consistency is suspect.
- Uncalibrated, under-sampled, or frozen-parameter SLT proxies could recreate the earlier failure mode; code and preregistration now block scientific promotion without a calibrated SLT evidence contract including input coverage and sample-size sensitivity.
- Synthetic success may not transfer to real transformer residual streams.
- Hidden posthoc leakage into train-time structural decisions would invalidate claims.
- Frontier-model API access may be topic-sensitive: Claude Fable, GPT-5.6-class, or similar controlled models could throttle, downgrade, or refuse advanced neural-network/LLM-development work. Treat this as an empirical operations risk for RelaLeap; record model behavior by task type; keep prompts truthful while deliberately framing work by the immediate legitimate subgoal / nearest safe category (for example SLT estimator validation rather than generic frontier-model optimization); and avoid relying on a single proprietary model for critical estimator or architecture decisions.
