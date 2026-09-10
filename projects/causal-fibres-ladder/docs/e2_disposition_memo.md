# E2 disposition: concentration without recovered structure

- Date: `2026-07-24`
- Frozen criteria: RelaLeap
  `configs/e2_acceptance_v1_1_frozen.json`, criteria version `1.2.0`
- Calibration seeds: `2111, 3253, 4517`
- Confirmation seeds: `6029, 7331, 8641, 9941, 11251`
- Substrate: reduced `ResidualSixBlockStudent`, local CPU
- Decision: **E2-B on both settled-error and adjoint tracks**
- Prediction 2: **failed**
- M0: **not equivalent**

## Why this is E2-B

The confirmation set reproduces concentrated and context-stable fields. The
settled top-5% frontier has exactly `1.000` confirmation-mean mass share in
block 6. The adjoint frontier has mean mass shares
`[0.4850, 0.3058, 0.1389, 0.0572, 0.0131, 0.0000]`, concentrated early.
M1 clears its full frozen gate in settled blocks 3--6 and all adjoint blocks.

Observability is not the binding global failure. Settled block 6 has mean M5
accuracy `0.693` with `+0.191` over shuffled labels. Every adjoint block is
observable: mean accuracies run from `0.746` at block 1 to `0.659` at block 6,
with deltas from `+0.232` to `+0.154`. This rules out joint E2-C, although
settled blocks 1--5 remain individually weak or unobservable.

The structural gates fail:

- No block passes the joint M2 floor. The largest rank-1/rank-2 contrast pair
  is only about `0.259/0.257` on settled block 3, below the frozen
  `0.30/0.15` joint requirement because rank 1 fails. Adjoint rank-1
  contrasts are `0.143`--`0.177`, also below `0.30`.
- No block reaches the frozen M3 mean-MI floor `0.20`. Settled blocks peak at
  `0.111` (block 3); adjoint blocks peak at `0.142` (block 4).
- No block reaches M4's diagonal/off-diagonal ratio `2.0`. Settled blocks peak
  at `1.465` (block 6); adjoint blocks peak at `1.409` (block 5).
- All 36 calibration and 60 confirmation JBD fits converged, so the negative
  structural outcome is not a fit-failure artifact.

M0 has zero equivalent blocks under the frozen per-block joint gate. Cosine
and support agree late, but the magnitude ratios range from effectively zero
upstream through `23.385` at block 6, outside `[0.75, 1.25]`.

## Co-location

Prediction 2 fails on both tracks. Settled M3 peaks at depth block 3 while M4
peaks at home block 6. Adjoint M3 and M4 peak at blocks 4 and 5 rather than
the frozen home blocks 1--2. Since no M3/M4 structure passes the emergence
gate, these are diagnostic peaks, not recovered fibres.

## Programme consequence

Do not select JBD-recovered fibres from this E2 run for E3. Under programme
branch 5.2, the honest scope contracts to supplied-structure applications:
E3 may proceed with supplied fibres as the structured arm, clearly labelled
as imposed structure, and must compare their cost and effect against dense,
top-k, sparsified-gradient, and random-k controls. This result supplies no
evidence that causal fibres emerged from either field substrate.

The negative result is limited to this reduced residual CPU substrate. Neither
local reduced substrate reproduced Mesto's settled depth profile, so this does
not refute emergence in the 124M rig. A renewed emergence claim would require
a separately preregistered substrate/configuration change and fresh disjoint
confirmation, not retrospective relaxation of these thresholds.

## C2 amendment

The mandatory C2 sparse-autoencoder baseline has now run on the identical
hash-verified five-seed confirmation fields. It is positive where JBD is
negative: C2 clears frozen M3/M4 on M5-observable settled block 6 and adjoint
blocks 1--6. Its eligible M3/M4 peaks co-locate with each track's frozen home
blocks. The accurate scientific interpretation is therefore narrower than
the initial memo: **concentration without JBD-recoverable structure, with
positive dictionary structure**. Estimator choice binds.

This does not retrospectively convert the gate to E2-A. E2-A preregistered
robust JBD recovery, and C2 was specified as a rival baseline rather than an
alternative fibre selector. E3 therefore still uses supplied fibres under
branch 5.2. Selecting C2 atoms would require a separately preregistered
selector/transport validation rather than post-hoc promotion.

## Evidence

- Calibration:
  `experiments/20260724T181654Z-e2-calibration-3seed-v1-1-frozen-rerun/`
- Confirmation and machine-readable disposition:
  `experiments/20260724T181805Z-e2-confirmation-5seed-v1-1-frozen/`
- Disposition SHA-256:
  `723674cfa4acd94fd985ae83afcd1d5ccf6d509b209cba63b5e0a564039d6972`
- RelaLeap commits: `93826c6`, `e14dfb3`, `2fe1fb5`
- C2:
  `experiments/20260724T185721Z-e2-c2-dictionary-5seed-v1-1-hungarian/`
