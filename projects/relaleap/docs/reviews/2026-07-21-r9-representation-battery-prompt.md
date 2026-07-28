# R9 representation-battery review prompt

Sent independently to Claude Fable 5 and GPT-5.6 Sol on 2026-07-21.

## Brief

Propose a scientifically decisive RelaLeap R9 battery to test whether
ePC-trained networks have superior properties beyond raw validation perplexity,
especially whether their internal representations are less excessively
entangled, while rigorously distinguishing useful modularity/disentanglement
from low-rank collapse.

### R8 evidence

- Five seeds by five arms completed.
- Mean validation loss: BP+CE `6.261±0.060`; BP+KD `7.039±0.056`;
  ePC-original T=4 `6.781±0.146`; ePC-deep T=12 `6.754±0.131`;
  wall-clock BP+KD `5.785±0.135`.
- The first four arms used 200 updates; wall-clock BP+KD averaged 1,334.
- All 10/10 ePC records had `activity_energy_monotone=true`.
- Mean KD gaps: BP+CE 1,161; BP+KD 824; ePC-original 978; ePC-deep 961;
  wall-clock BP+KD 470.
- Twenty checkpoints exist: BP+CE, BP+KD, ePC-original, and ePC-deep for every
  seed. Wall-clock BP+KD has metrics but no checkpoint.
- Preserve the negative result: ePC loses on raw validation performance at
  equal updates and wall time.

### Prior caveat

A corrected real-data audit on earlier checkpoints found ePC centered-entropy
effective rank about 2.7--3.8 in middle/final layers versus 23--42 for BP,
plus a late-layer geometry outlier and earlier large last-layer spectral norms.
This may be collapse/brittleness rather than disentanglement. Prior outcome work
also showed poor adaptation for an earlier ePC configuration. New similarity
metrics require paired identical token matrices and explicit invariants.

### Requested analysis

1. Operationally distinguish disentanglement, modularity, sparsity,
   superposition, low intrinsic dimension, collapse, redundancy, and causal
   factorization.
2. Rank checkpoint-only probes. For each specify estimator, data, layer/token
   pooling, normalization, controls/nulls, calibration, signatures under useful
   disentanglement versus collapse versus BP-like distributed coding, and
   paired five-seed statistics.
3. Critically assess factor-labelled synthetic/compositional data, cross-factor
   probes, DCI/SAP/MIG, HSIC/conditional dependence, covariance spectra,
   principal angles, sparse autoencoders/dictionary coherence, activation
   patching/causal ablation selectivity, gradient interference, task-vector
   composition, Jacobian/Fisher structure, OOD invariance, continual-learning
   interference, and systematic compositional generalization.
4. Require functional linkage: structural differences count as superior only
   with paired benefits in sample efficiency, few-shot transfer, compositional
   recombination, robustness, calibration, selective forgetting, or adaptation
   under matched post-training rules.
5. Address confounds including worse baseline loss, rank collapse, scale/norm
   differences, arbitrary rotations, probe capacity, token autocorrelation,
   teacher/student mismatch, checkpoint selection, and wall-clock/update
   mismatch.
6. Give a minimum decisive versus optional exploratory battery in three stages:
   checkpoint-only, one-seed mechanism screen if needed, and multi-seed
   confirmation only after frozen gates.
7. State preregistered thresholds and falsifiers for useful disentanglement,
   merely different representations, collapse masquerading as disentanglement,
   and no ePC advantage.
8. Recommend an identifiable factor-labelled synthetic task plus real-language
   confirmation.
9. Estimate relative compute/storage and identify which R8 artifacts suffice
   versus which new traces/checkpoints are required.
10. End with a compact R9 arm/metric table and top three recommendations.

Low CKA, low rank, sparsity, or low corruption delta must not be treated as
automatically beneficial.
