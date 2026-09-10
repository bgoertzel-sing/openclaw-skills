# R9 representation battery: Fable/Sol synthesis

Date: 2026-07-21

## Decision frame

Both independent reviews agree that R8 is negative on the outcomes already
measured. ePC's monotone activity energy is an implementation invariant, not a
functional win. The earlier effective-rank result (roughly 2.7--3.8 for ePC
versus 23--42 for BP) is currently more consistent with collapse or brittle
compression than with useful disentanglement.

R9 therefore tests the preregistered hypothesis:

> Relative to paired BP controls, ePC yields factor-selective, causally
> separable representations that improve at least one held-out functional
> outcome under the same post-training rule, without losing usable information
> or concentrating computation into a brittle bottleneck.

A structural difference counts as positive only if it (1) survives
rank/scale/loss controls, (2) has a paired functional benefit, and (3) is not
reproduced by an explicitly rank-collapsed or bottlenecked BP control.

## What must remain distinct

- **Disentanglement:** independently intervenable factors decode with little
  cross-factor leakage, including held-out factor combinations.
- **Modularity:** restricted subspaces have selective causal effects with low
  off-target damage.
- **Sparsity:** few active units or dictionary coefficients; dead units also
  satisfy this, so sparsity alone is not beneficial.
- **Superposition:** more useful features than approximately orthogonal
  directions, demonstrated through interference/polysemanticity rather than
  high dimension alone.
- **Low intrinsic dimension:** a geometric description, not evidence against
  collapse.
- **Collapse:** lost variance/information/sensitivity or merged factors,
  usually coupled to brittleness or compensatory amplification.
- **Redundancy:** substitutable copies of information, demonstrated through
  conditional decoding or lesion recovery.
- **Causal factorization:** targeted interventions change one factor-dependent
  behavior while preserving unrelated behavior; probes alone do not show it.

Report three panels separately: information retained, organization, and
functional consequences. Do not produce a single omnibus disentanglement
score.

## Stage A: checkpoint-only, fail-closed battery

Use all 20 R8 checkpoints. Primary paired contrasts are ePC-original and
ePC-deep against BP+KD within each seed; BP+CE is the secondary control.
Use identical hashed matrices for every checkpoint: WikiText-103 validation,
TinyStories or another disjoint real-language corpus, and a frozen controlled
minimal-pair set. Use at least 4,096 sequences per corpus and split
calibration, probe-test, and causal-test data before analysis. Preserve
documents and token positions; never treat adjacent tokens as independent.

### A0. Instrument calibration

- Float64 linear CKA symmetry error below 1e-10 and feature/Gram agreement
  within 1e-6.
- Known-rank fixtures recover entropy and participation ranks within 5%.
- Orthogonal rotations preserve rotation-invariant metrics; axis-aligned
  scores change when expected.
- Permuted labels give chance probes.
- Identity patching has zero effect; zero/full ablation reproduce endpoints.
- Every arm receives the same examples, masks, rows, seeds, probe capacity,
  and hyperparameter-search budget.

Failure invalidates the affected panel.

### A1. Collapse and conditioning audit (first gate)

At embeddings, every block output, and final normalized output measure:

- centered covariance spectrum; entropy, participation, stable and numerical
  rank; top-1/3/8/16 variance shares;
- raw RMS/norms, anisotropy, pairwise-cosine concentration, dead/saturated
  fractions, and linear reconstruction curves;
- TwoNN and k-NN intrinsic dimension with neighborhood sensitivity;
- factor/frequency-conditioned spectra;
- weight spectral/Frobenius norms and layerwise amplification; optionally
  Jacobian singular-value summaries.

Report raw centered geometry and feature-standardized correlation geometry.
Do not whiten or normalize each example for the primary collapse diagnosis.
Controls: matched-covariance Gaussians, token/block permutations, rotations,
BP projected to ranks 2/4/8/16/32, BP rescaled to ePC RMS, and random equal-size
subspaces.

Preregistered collapse red flag: median layer effective rank below 25% of
paired BP+KD plus either top-1 variance share above 0.70 or conditioning/
amplification above 4x BP. Call collapse supported only if this accompanies at
least 10% relative loss in held-out factor decoding, local sensitivity, or
matched adaptation AUC in at least 4/5 seeds.

### A2. Factor recovery and leakage (primary structural test)

Generate factorial, independently intervenable language factors: subject and
object number, tense, voice, negation, dependency/distractor number, relative-
clause depth, semantic roles, and lexical identity as nuisance. Split by
lexical items and factor combinations, not random tokens. Freeze pooling sites
(pre-inflected-verb state, content-token mean, and final token) in advance.

Measure regularized linear-probe learning curves, held-out-combination
accuracy, conditional cross-factor leakage, DCI/SAP as descriptive supplements,
conditional HSIC, and principal angles between factor subspaces. MIG is
secondary because its coordinate/discretization assumptions are ill-suited to
arbitrary rotations. Repeat after rotation and after rank-matching BP.

Useful factorization requires retained or improved target decoding together
with reduced leakage; easy decoding caused by lower rank is not sufficient.

### A3. Causal selectivity and functional linkage

For the best preregistered layers/factor subspaces, run activation patching,
low-rank steering, and equal-norm/equal-dimensional ablations. Report on-target
effect, off-target damage, selectivity ratio, and whether two interventions
compose approximately. Compare with random and rank-matched subspaces.

Then apply one identical bounded post-training rule per checkpoint and measure
learning-curve AUC, held-out factor recombination, OOD invariance, calibration,
and forgetting/interference. Structural superiority is not established unless
at least one frozen functional endpoint improves.

### A4. Optional exploratory panel

Only after A1--A3: sparse autoencoders with reconstruction-matched controls,
dictionary coherence/polysemanticity, gradient cosine/interference matrices,
task-vector composition, Fisher/Jacobian block structure, and redundancy via
lesion recovery. These are hypothesis generators, not promotion metrics.

## Statistics

Compute arm differences on identical examples within each seed. Report all
five differences, their mean, paired standardized effect, and hierarchical
bootstrap intervals resampling seeds then documents/factor tuples. Use family-
wise max-T adjustment. With five seeds, a two-sided exact sign-flip test cannot
reach p<.05 (minimum 0.0625); do not manufacture significance by pooling tokens.
A directional test reaches 0.03125 only if all five seeds favor ePC and the
direction was frozen in advance.

## Gates

### Stage A -> B

Advance only if at least 4/5 seeds show both:

1. reduced conditional factor leakage or improved causal selectivity by at
   least 20% relative to paired BP+KD; and
2. no collapse red flag and no more than 5% relative loss in held-out target
   decoding.

At least one matched functional endpoint must improve by 10% relative (or by a
preregistered practically meaningful absolute margin) before calling the
representation superior.

### Stage B: one-seed mechanism screen

If Stage A passes, train one frozen seed on an identifiable compositional
grammar in which number, tense, voice, negation, roles, depth, and lexical
identity vary factorially. Hold out lexical items and joint factor
combinations. Compare BP+KD, ePC-original, ePC-deep, and a BP rank-bottleneck
control from common initialization and batches. Save checkpoints at
0/10/50/100/200 updates plus optimizer, gradient, and relaxation traces.

Advance only if ePC beats both ordinary BP and the collapsed BP control on
causal selectivity plus held-out recombination/adaptation, without the Stage-A
collapse signature.

### Stage C: confirmation

Freeze metrics, layers, pooling, thresholds, grammar, probes, and analysis code;
then repeat across five seeds. Confirm only with sign-consistent structural and
functional benefits in at least 4/5 seeds. Keep validation loss and runtime in
the report even if the representation endpoints pass.

## Minimum R9 table

| Stage | Arms | Required evidence | New training |
|---|---|---|---|
| A | 5 seeds x BP+CE, BP+KD, ePC-T4, ePC-T12 | collapse audit; factor decoding/leakage; causal selectivity; one matched functional endpoint | No base training; frozen probes and bounded adaptation only |
| B | 1 seed x BP+KD, ePC-T4, ePC-T12, rank-bottleneck BP | known-factor recovery, interventions, held-out combinations, learning/forgetting curves | Yes, small synthetic mechanism screen |
| C | same frozen Stage-B arms, 5 seeds | preregistered replication and uncertainty | Yes, only after B passes |

## Resource envelope

Stage A can use the existing 20 checkpoints. Its main cost is activation
extraction/storage; streaming covariance and factor summaries should keep the
durable output to tens of GB rather than retaining every token activation.
Frozen probes and causal forwards are modest relative to R8 training. Stage B
is approximately one small four-arm synthetic training run. Stage C is the
only material new multi-seed compute and requires separate cost approval.

## Top recommendations

1. Run collapse/conditioning calibration before any disentanglement claim.
2. Make conditional factor leakage plus causal intervention selectivity the
   structural core, using rank-matched and deliberately collapsed BP controls.
3. Require paired functional benefit under an identical adaptation rule; if
   Stage A fails, record R9 as no demonstrated ePC representational advantage
   and do not spend on new training.

## Provenance

This synthesis reconciles two independent reviews requested with the same
frozen R8 brief. The prompt is preserved at
`2026-07-21-r9-representation-battery-prompt.md`. Reviewer responses are
preserved in their OpenClaw session records and summarized here; neither
reviewer result is itself experimental evidence.
