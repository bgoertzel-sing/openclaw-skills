# Run 20260725T095200Z-gpt2-controller-v4-rerun

- Project: `carom`
- Started: `2026-07-25T09:52:00Z`
- Finished: `2026-07-25T10:25:00Z`
- Status: `complete; pod terminated`
- Operator/agent: `ZeroBot`
- Local or remote: `RunPod Secure Cloud; pod ziwbsaw4tn71hc (A100 SXM4 80GB), deleted after retrieval`
- Elapsed: 1967s (32.8 min)
- Estimated cost: ~USD 0.82 (32.8 min × $1.49/hr)

## Question

Does CAROM's distributional controller choose useful learning-rate actions on
the frozen-GPT-2-small compiled-channel task?

## Fix from prior failure

The prior v4 run (20260724T082409Z) failed because `branch_trajectory` and
`mean_gradient_trajectory` called `scheduler.step()` on a parent OneCycleLR
that had already reached its `total_steps` limit. Fix: branches now use a
constant LR (parent's current LR × scale) with NO scheduler.step(). Regression
tests in `test_v4_scheduler_fix.py`.

## Frozen protocol

- Frozen GPT-2-small 124M span encoder; only CAROM modules train
- AdamW, base LR 2e-3, OneCycleLR, 2000 total steps
- Batch 64, clip 1.0
- Gate checkpoints at steps 500, 1000, 2000
- 16 calibration branches + 8 held-out branches × 3 LR scales {0.5, 1.0, 1.5}
- 8 branch updates each

## Results

### Final evaluation
- Task accuracy: 0.3516
- Edge accuracy: 0.7173
- Itinerary tau: 0.9323

### Gate results

| Gate | Pass | Details |
|---|---|---|
| loss_reduction | ✅ | median ratio 1.0 (informed ≤ passive) |
| no_destabilization | ✅ | all finite |
| oracle_gap | ✅ | median ratio 0.9995, controller matched oracle 1/3 checkpoints |
| variance_gated | ❌ | median ratio 1.0020 (> 1.0 threshold) |
| operational | ✅ | parent unchanged at all 3 checkpoints |

### Per-checkpoint summary

| Step | Controller scale | Passive loss | Informed loss | Oracle loss | Oracle scale |
|---|---|---|---|---|---|
| 500 | 1.0 | 1.9802 | 1.9802 | 1.9802 | 1.0 |
| 1000 | 1.0 | 1.7234 | 1.7234 | 1.7129 | 0.5 |
| 2000 | 1.0 | 1.5881 | 1.5881 | 1.5874 | 1.5 |

## Interpretation

**Observed:**
- The controller chose scale=1.0 (passive) at all three checkpoints.
- At step 500, all scales performed identically (early training, no LR sensitivity).
- At step 1000, the oracle (scale=0.5) would have achieved 1.7129 vs passive 1.7234 — a 0.6% improvement the controller missed.
- At step 2000, the oracle (scale=1.5) would have achieved 1.5874 vs passive 1.5881 — a 0.04% improvement.
- The variance-gated rule failed: it picked scale=0.5 at step 2000 which performed worse (1.5918).

**Inferred:**
- The distributional controller has very little action headroom on this task at these checkpoints. The mean-gradient forecast correctly predicted scale=1.0 as best at steps 500 and 2000, but missed the small oracle advantage at step 1000.
- The LR scale {0.5, 1.0, 1.5} range may be too narrow to show controller benefit. The prior v3 toy task also had almost no headroom.
- The variance-gated heuristic is not useful here — it amplified noise rather than improving on passive.

**Hypothesis:**
- A wider LR scale range or a different controller signal (e.g., gradient norm or loss curvature) might reveal more headroom. The mean-gradient forecast is accurate but the optimal action is almost always "don't change LR."

## Artifacts

- `artifacts/results.json` — SHA-256 `1b8188a3fdccf97ed907afb46d1ebbf53e49f3b1a1cf76ac11448b2bf41968fe`
- `artifacts/experiment.log` — SHA-256 `54dd1dbc692bf8aceba7715ff949556dcb36ac1f8de48cbfece00f61a16a4c15`
- Pod `ziwbsaw4tn71hc` deleted; provider inventory empty.

## Budget

- $10 max (Ben approved 2026-07-25)
- Actual cost: ~$0.82 (32.8 min × $1.49/hr)
- Well within budget.
