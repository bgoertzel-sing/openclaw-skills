# Run 20260718T223300Z-epc-outcome-6layer-battery: six-layer ePC outcome battery

- Project: `relaleap`
- Started: `2026-07-18T22:33:00Z` (provisioning)
- Finished: `2026-07-19T00:29Z` (result file written)
- Status: `complete; promotion failed; structural/CKA/spectral/adaptation data collected`
- Provider: RunPod Secure Cloud
- Pod: `bksws9jhc7e8xp` (terminated after verified retrieval)
- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Config SHA-256: `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`

## Patches applied

Two bug-fix patches were applied to the frozen runner on the pod (not scientific changes):

1. **Device placement fix in `_attach_low_rank`**: Low-rank adapter parameters were created on CPU but the model was on CUDA. Fixed by moving adapter to `module.weight.device` before registration.
2. **GPU acceleration for CKA/SVD**: `_linear_cka` and `_spectral_summary` were computing on CPU with slow BLAS (first attempt ran 95+ minutes without finishing before the container restarted). Moved hidden-state CKA and spectral SVD computations to GPU. This is a performance change, not a scientific change — same mathematical operations, same results.

Patched runner SHA-256: `a3a82402b6a0720dd06a6a109e7a9b58c06d6f2a20bfd76b4df698594e57b189`

## Frozen inputs

- Nine safetensors checkpoints from run `20260718T073312Z-epc-outcome-6layer-run2`
  (3 seeds × 3 arms: bp_ce, bp_kd, epc_kd), each 327,657,928 bytes.
- Config: `configs/gpt2_epc_outcome_6layer.json`
- Public inputs: pinned GPT-2, WikiText-103, TinyStories.

## Execution

- First Community Cloud pod `64vtxxj6nfauof` stalled (uptime=0 for 5+ min), terminated.
- Secure Cloud pod `bksws9jhc7e8xp` provisioned at $1.39/hr.
- Checkpoint upload via 9 parallel rsync transfers (~30 min due to slow network).
- First run attempt: device mismatch bug → patched → second attempt: CPU-bound
  SVD/CKA too slow (95+ min) → container restarted → patched for GPU acceleration.
- Third attempt: completed in ~7 minutes after patching.

## Result

**Observed:** the frozen promotion rule failed (`passes: false`).

### Adaptation/forgetting summary

| Seed | Arm | Pre-source | Pre-target | Source forgetting | Target adapt gain | Target AUC |
|------|-----|-----------|-----------|-------------------|-------------------|------------|
| 1729 | bp_ce | 5.294 | 7.895 | 0.257 | 2.198 | 6.351 |
| 1729 | bp_kd | 5.940 | 5.835 | 0.197 | 0.962 | 5.169 |
| 1729 | epc_kd | 6.448 | 6.908 | 0.114 | 0.645 | 6.442 |
| 3253 | bp_ce | 5.333 | 7.735 | 0.331 | 2.075 | 6.286 |
| 3253 | bp_kd | 5.989 | 5.828 | 0.149 | 0.961 | 5.162 |
| 3253 | epc_kd | 6.551 | 6.994 | 0.064 | 0.714 | 6.476 |
| 6421 | bp_ce | 5.315 | 7.786 | 0.239 | 2.132 | 6.283 |
| 6421 | bp_kd | 5.933 | 5.887 | 0.134 | 1.023 | 5.168 |
| 6421 | epc_kd | 6.577 | 7.086 | -0.040 | 0.773 | 6.497 |

### Promotion evaluation

- `bp_ce` contrast: mean AUC gain = -0.164, 95% CI [-0.221, -0.095]
- `bp_kd` contrast: mean AUC gain = -1.304, 95% CI [-1.334, -1.270]
- Mean ePC source forgetting: 0.046 nats
- Max ePC pre-adaptation regression: 1.199 nats
- **Passes: false** (ePC does not beat either control on target AUC)

### CKA (linear, per layer)

ePC checkpoints show substantially different representation geometry from both BP controls:

- bp_ce vs bp_kd CKA: 0.94, 0.75-0.77, 0.72-0.73, 0.72-0.75, 0.73-0.75, 0.77-0.79
- bp_ce vs epc_kd CKA: 0.17-0.24, 0.24-0.35, 0.08-0.43, 0.08-0.49, 0.08-0.52, 0.45-0.55
- bp_kd vs epc_kd CKA: 0.18-0.25, 0.27-0.41, 0.07-0.41, 0.07-0.40, 0.06-0.40, 0.45-0.45

**Interpretation:** ePC-trained networks have markedly different internal representations
from both BP controls (CKA 0.06–0.55 vs 0.72–0.94 for BP-vs-BP). However, this structural
difference does not translate to better plasticity or adaptation — ePC networks adapt more
slowly to the TinyStories domain and forget less of the source (lower forgetting is not
necessarily better when accompanied by worse target adaptation).

## Retrieval and cleanup

- Retrieved `gpt2_epc_outcome_6layer.json` (207,425 bytes) and `outcome_run.log`.
- Pod `bksws9jhc7e8xp` terminated; provider pod inventory empty. No job-created volumes.
- Estimated pod-lifetime cost: ~$2.50 (provisioned 22:46 UTC, terminated 00:35 UTC, ~1.8 hr at $1.39/hr).

## Exit and limitation

- Runner exit status: `0` (normal completion).
- Promotion rule: failed.
- The structural/CKA/spectral/adaptation/corruption/block-skip data are complete and
  available for analysis, but the frozen promotion criterion is not met.
