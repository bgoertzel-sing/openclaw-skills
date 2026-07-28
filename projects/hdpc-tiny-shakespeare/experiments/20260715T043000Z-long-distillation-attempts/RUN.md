# Long-Run Distillation Attempts — 2026-07-15T04:30:00Z and 04:32:00Z

## Purpose

Test whether the λ·T monotonicity boundary from the state-matched sweep holds under sustained training, or whether student drift shifts the boundary.

## Runs

### Run 1: λ=0.01, T=4 (λ·T=0.04, at sweep boundary)

- **Aborted at step 2** (of 300)
- Step 0: energy_init ~3.86e-7, monotone ✓
- Step 1: monotone ✓
- Step 2: energy increase 2.78e-8 exceeded threshold 1.93e-8 (5% of |energy_init|)
- Total time: 10.2s

### Run 2: λ=0.005, T=4 (λ·T=0.02, well inside safe zone)

- **Aborted at step 3** (of 300)
- Step 0: monotone ✓
- Step 1: monotone ✓
- Step 2: monotone ✓
- Step 3: energy increase 4.68e-9 exceeded threshold 1.37e-9 (10% of |energy_init|)
- Total time: 13.6s

## Key finding

**The monotonicity boundary tightens rapidly as the student drifts from the teacher.**

The energy baselines shrink with each AdamW step (3.86e-7 → 1.37e-8 across ~2-3 steps — a 28x decrease). The relative tolerance threshold (5% or 10% of |energy_init|) scales down proportionally, so even λ·T=0.02 (well inside the safe zone from the sweep) fails after 2–3 training steps.

This confirms ProtoMegaBot's hypothesis H2: the safe λ·T boundary decreases as training proceeds. The mechanism is that the student converges toward the teacher (KD loss → 0), shrinking the energy surface. At very small energy scales, any per-step perturbation exceeds a relative threshold.

## Root cause analysis

The problem is structural, not a tuning issue:

1. **tiny-gpt2 has a very flat KD loss surface** — the student barely diverges from teacher after one AdamW step at lr=1e-4
2. **Energy = error_energy + KD_loss** — as KD loss → 0, the energy surface shrinks toward zero
3. **Relative thresholds become meaningless** at very small energy scales — 5% of 1e-8 is 5e-10, which is below the precision of the relaxation dynamics

## Implications

- The λ·T control law from the state-matched sweep is valid for a **fixed weight configuration** but does not transfer across training steps
- An absolute energy threshold for the abort would be more stable, but would mask genuine dynamics at small scales
- **The real issue is that tiny-gpt2 is too small a model for meaningful distillation** — the KD loss surface is too flat, and the student converges to teacher too quickly, leaving no energy for the PC relaxation to work with

## Recommended next steps

1. **Switch to a larger model** — gpt2-small (124M) or a small custom transformer with more capacity, so the KD loss surface has enough structure for sustained distillation
2. **Use an absolute energy threshold** (e.g., abort if energy increase > 1e-6) rather than relative, to avoid the shrinking-baseline problem
3. **Alternatively: use a pre-trained teacher and a randomly-initialized student** (not a copy of teacher), so the KD loss stays large throughout training
4. **Consider a non-trivial task** — tiny-gpt2 on Tiny Shakespeare produces near-uniform-output perplexity (~50K), indicating the model has essentially no task signal to distill

## Artifacts

- `20260715T043000Z-long-distillation-l001-T4/artifacts/results.json`
- `20260715T043200Z-long-distillation-l0005-T4/artifacts/results.json`
