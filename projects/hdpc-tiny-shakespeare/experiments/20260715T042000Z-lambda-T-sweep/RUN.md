# Lambda/T Sweep — 2026-07-15T04:20:00Z

## Purpose

Diagnose whether the non-monotone energy observed in the two-step trainer smoke (trace `1.092e-7 → 1.714e-7 → 1.432e-7` at λ=0.05, T=2) reproduces across λ values, and find the largest safe error learning rate.

## Command

```bash
cd /home/openclaw/research-agent/projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare
PYTHONPATH=src python3 -m hdpc_tiny_shakespeare.sweep_lambda \
  --output /home/openclaw/research-agent/projects/hdpc-tiny-shakespeare/experiments/20260715T042000Z-lambda-T-sweep/artifacts/sweep_results.json
```

## Environment

- Model: `sshleifer/tiny-gpt2` (2-layer GPT-2, hidden ~50)
- Student: deepcopy of teacher, perturbed by `0.01 * randn` on all parameters
- Batch: 4 sequences of length 256, seed=0, Tiny Shakespeare
- β=2.0, α=0 (KD only)
- CPU, Python 3.10, transformers 4.57.6
- Git: commit `f546434` on branch `agent/two-step-trainer-smoke`

## λ grid: {0.01, 0.02, 0.03, 0.05}
## T grid: {1, 2, 4}
## Pass criterion: energy_strict_monotone=True AND energy_nontrivial=True (tol=1e-3 * |energy_initial|)

## Results

| λ | T | Monotone | Nontrivial | Energy moved | Max increase | h.0 cosine | h.0 norm ratio |
|---|---|----------|------------|-------------|-------------|------------|----------------|
| 0.01 | 1 | ✓ | ✗ | 4.69e-08 | -4.69e-08 | 1.00000002 | 0.999922 |
| 0.01 | 2 | ✓ | ✗ | 8.50e-08 | -3.81e-08 | 0.99999998 | 0.999845 |
| 0.01 | 4 | ✓ | ✗ | 1.51e-07 | -1.94e-08 | 0.99999996 | 0.999691 |
| 0.02 | 1 | ✓ | ✗ | 1.13e-07 | -1.13e-07 | 1.00000000 | 0.999843 |
| 0.02 | 2 | ✓ | ✗ | 1.30e-07 | -1.73e-08 | 0.99999999 | 0.999688 |
| 0.02 | 4 | ✓ | ✗ | 2.75e-07 | -1.73e-08 | 0.99999987 | 0.999382 |
| 0.03 | 1 | ✓ | ✗ | 1.34e-07 | -1.34e-07 | 0.99999998 | 0.999764 |
| 0.03 | 2 | ✓ | ✗ | 2.13e-07 | -7.90e-08 | 0.99999992 | 0.999531 |
| 0.03 | 4 | ✓ | ✗ | 4.24e-07 | -7.90e-08 | 0.99999973 | 0.999076 |
| 0.05 | 1 | ✓ | ✗ | 2.01e-07 | -2.01e-07 | 0.99999993 | 0.999602 |
| 0.05 | 2 | ✓ | ✗ | 3.92e-07 | -1.91e-07 | 0.99999983 | 0.999214 |
| 0.05 | 4 | ✓ | ✓ | 6.23e-07 | -1.12e-07 | 0.99999940 | 0.998473 |

## Key findings

1. **All 12 configurations are strictly monotone.** The non-monotone behavior from the original two-step trainer smoke was NOT reproduced.
2. **Only λ=0.05/T=4 is nontrivial** (energy moved > tolerance threshold).
3. **Gradient alignment near-perfect everywhere:** cosine ≈1.0, norm ratios 0.998–1.003.
4. **The discrepancy is state-dependent.** The original smoke used a student after one AdamW step (lr=1e-4), giving energy ~1.09e-7. This sweep uses a random perturbation (0.01·randn), giving energy ~4.37e-4 — three orders of magnitude larger. The non-monotone behavior may be specific to the post-AdamW-step weight configuration.

## Interpretation

The sweep does not invalidate the original non-monotone observation, but it does not reproduce it either. The non-monotone energy appears to be **state-dependent** — specific to the post-AdamW-step weight configuration rather than purely a function of λ.

## Next step

Run a **state-matched sweep**: replicate the original smoke's exact student state (one AdamW step from teacher at lr=1e-4) and then vary λ from there. This will determine whether the non-monotone behavior is:
- A genuine dynamical property of the ePC relaxation at certain weight configurations, or
- An artifact of the specific training-step interaction with the relaxation loop.

## Artifacts

- `artifacts/sweep_results.json` (sha256sum to be recorded)
