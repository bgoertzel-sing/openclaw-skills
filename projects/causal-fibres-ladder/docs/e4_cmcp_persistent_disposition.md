# E4/CMCP Persistent-Ledger Disposition

## Result

The corrected stable-cohort persistent-ledger experiment passed all nine
frozen confirmation checks on five disjoint seeds.

At episode 8:

- CMCP effective precision was `8.89433`, close to oracle `9.0`; naive
  accumulation reached `26.0`.
- CMCP versus naive mean accuracy was `0.83281` versus `0.74844`.
- CMCP versus naive mean task loss was `0.43899` versus `0.59725`.
- CMCP versus naive mean 10-bin ECE was `0.07797` versus `0.12309`.
- CMCP versus naive mean multiclass Brier was `0.22596` versus `0.32489`.

CMCP was presentation-order invariant under the tested ordering, and model
parameters remained unchanged.

## Protocol correction

The initial one-seed smoke accumulated row-aligned evidence from unrelated
batches. That makes old row indices refer to different examples and can create
artificial interference. It is retained as implementation history only.

Calibration and confirmation instead reused one hash-identified cohort while
performing freshly seeded extractions each episode. This tests repeated
evidence accounting for the same cases.

## Interpretation boundary

The result establishes a practical same-cohort calibration and precision
advantage over naive duplicate accumulation. It does not establish
continual-learning retention or forgetting prevention: the model is frozen
and no evidence is transferred across unrelated examples.

The next implementation step is a typed persistent store carrying cohort and
example identities, packet provenance, innovation identity, and precision.
Only after those identities are enforced should a parameter-learning or MORK
retention experiment be attempted.

## Evidence

- Calibration:
  `experiments/20260725T015720Z-e4-cmcp-persistent-calibration/`
- Frozen confirmation:
  `experiments/20260725T015835Z-e4-cmcp-persistent-confirmation/`
- Protocol:
  `docs/e4_cmcp_persistent_protocol.md`
