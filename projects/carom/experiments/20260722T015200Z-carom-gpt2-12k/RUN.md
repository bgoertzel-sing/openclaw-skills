# CAROM frozen-GPT-2 higher-accuracy run

- Status: `COMPLETE — artifacts verified; pod terminated`
- Question: Does tripling the training-example budget raise frozen-GPT-2 CAROM
  in-distribution accuracy while preserving or strengthening causal trajectory
  evidence and improving held-out L5 behavior?

## Frozen protocol

- Seed: 0
- Frozen base: GPT-2-small, 124M parameters, final hidden layer, width 768
- CAROM architecture/losses: unchanged from the completed 4,000-step arm
- Training updates: 12,000
- Batch size: 64 (768,000 examples total)
- Optimizer: AdamW, LR 0.002, weight decay 0.0001
- Schedule: OneCycleLR defined over all 12,000 updates
- Gradient clipping: 1.0
- Checkpoints: step 0 and every 1,000 updates through 12,000
- Frozen evaluation: L2--4 corpus seed 1234, n=256; L5 seed 5678, n=128
- Interventions: natural, forced, shuffled, smeared at every checkpoint
- L5 budgets: S=72, 100, 120

## Acceptance and interpretation

- Primary optimization target: final L2--4 accuracy >0.55.
- Strong target: final L2--4 accuracy >=0.65.
- Required mechanism panel: coverage, exact order, tau,
  natural-minus-shuffled, forced/shuffled/smeared endpoints.
- Required extrapolation panel: L5 accuracy at S=72/100/120.
- A higher endpoint with weaker mechanism measures is reported as an endpoint
  optimization improvement, not stronger evidence for compiled execution.
- No claim of learned commutation is permitted without the separately repaired
  and controlled nonlinear swap/JVP commutator probes.

## Evidence paths

- Exact command: `command.sh`
- Runner: `source/r9_carom_gpt2_12k.py`
- Raw outputs: `artifacts/results/`, `artifacts/checkpoints/`, and `artifacts/logs/`
- Verification: 13 checkpoints and 13 result rows (steps 0--12,000 by 1,000),
  complete intervention/budget records, and a 31-file SHA-256 manifest

## Outcome

- Training completed 12,000 updates in 10,582 seconds (2h56m22s).
- Best frozen L2--4 accuracy was 0.3268 at step 3,000; final accuracy was
  0.1888. The preregistered >0.55 and >=0.65 targets were not met.
- At the best checkpoint: tau 0.9870, coverage 0.7275, exact order 0.3320,
  natural-minus-shuffled 0.0801, and L5 accuracy 0.2617.
- At the final checkpoint: tau 0.3281, coverage 0.4704, exact order 0.0938,
  natural-minus-shuffled 0.0221, and L5 accuracy 0.1589.
- Edge accuracy stayed near 0.70 while endpoint and itinerary measures
  collapsed, separating graph prediction from successful execution.
- The OneCycleLR schedule reached maximum LR near step 3,600. Failure begins
  between steps 3,000 and 4,000 at LR approximately 0.00187--0.00199. This
  temporal match supports, but does not prove, LR-induced destabilization.
- The automatic intervention pass inherited an older corpus-unpacking bug.
  The tested repaired runner then evaluated all checkpoints without retraining.
- Pod `wsllxvsshf7jf1` was terminated after retrieval and verification.

## Stop conditions

- Non-finite loss, OOM, missing checkpoints, repeated process failure,
  three elapsed hours, or USD 4.47 compute cap.
- Retrieve and verify artifacts immediately on completion or failure, then
  terminate the pod and re-query provider inventory.
