# CAROM GPT-2 controller v5 active-continuation gate

- Status: completed; scientific utility gate failed
- Project: `carom`
- Started: 2026-07-25T16:10:00Z

## Question

Can the distributional selector choose a learning-rate action that improves an
actual state-restored continuation over passive OneCycleLR-scale continuation
on common future batches?

## Frozen corrections

- Decisions occur at updates 600 and 1200, before terminal LR decay.
- Candidate scales: 0.25, 0.5, 1.0, 1.5.
- Eight calibration trajectories of eight updates estimate the mean-gradient
  forecast.
- Four held-out common-random continuations per scale run 32 actual optimizer
  updates from the identical model/AdamW/scheduler checkpoint.
- The informed arm uses the selected scale; passive uses 1.0; oracle is the
  best held-out scale in hindsight.
- The source checkpoint remains immutable and every scale receives identical
  held-out batches.

## Gates

- Operational: exact checkpoint hash before/after all continuations.
- Sensitivity: at least one checkpoint has a nonzero held-out loss range
  exceeding 1e-4 across scales.
- Utility: median informed/passive loss ratio <= 0.999.
- Oracle headroom: median oracle/passive ratio <= 0.999.
- Selection: informed captures at least 25% of oracle improvement when
  headroom is positive.

## Results

Attempt 1 failed before training because the PyTorch 2.8 image enforces PEP
668 and rejected a system-level `pip install transformers`. No GPU training
occurred. The command was corrected to use a system-site-packages virtual
environment; attempt 1 logs are retained.

Attempt 2 completed in 2,406.73 seconds (40.11 minutes).

| Checkpoint | Selected | Passive loss | Informed loss | Oracle scale/loss | Outcome |
|---:|---:|---:|---:|---:|---|
| 600 | 1.5 | 1.825081 | 1.868018 | 0.25 / 1.803257 | selector harmful |
| 1200 | 0.5 | 1.594500 | 1.592587 | 0.5 / 1.592587 | selector matched oracle |

- Operational checkpoint immutability: pass.
- Finite outputs: pass.
- Action sensitivity: pass; maximum held-out range `0.0647608`.
- Utility: **fail**; median informed/passive ratio `1.01116296`.
- Oracle headroom: pass; median oracle/passive ratio `0.993421`.
- Selection: **fail**; mean captured oracle improvement `-0.483665`.
- Final evaluation: accuracy `0.326172`, edge accuracy `0.708998`,
  itinerary tau `0.975260`.

## Interpretation

The corrected design establishes that learning-rate actions materially alter
the continuation and that useful oracle headroom exists. The selector is
miscalibrated near the peak learning rate: it chose 1.5x when 0.25x was best,
worsening held-out continuation loss by about 2.35% versus passive. At the
later low-learning-rate gate it chose the oracle 0.5x action, improving loss
by about 0.12%. Thus v4's passive behavior was not evidence of a useful
controller, and v5 gives a valid negative overall utility result.

## Provenance and cleanup

- Resource: RunPod A100 SXM 80GB at USD 1.49/hour.
- Estimated successful-run cost: USD 0.996, plus negligible failed setup time.
- Artifacts: `artifacts/results.json`, `artifacts/experiment.log`,
  `artifacts/environment.json`, and `artifacts/sha256.txt`.
- Local SHA-256 verification passed for all three result artifacts.
- Pod `7xg450h78qkmj9` was terminated after retrieval; provider inventory was
  confirmed empty.
