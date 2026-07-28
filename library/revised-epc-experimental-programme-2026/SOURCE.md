# Source: Revised ePC Experimental Programme

- Type: `PDF`
- Authors/organization: Causal Fibres / Hyperon ePC effort
- Publication/version date: 2026-07-23; working plan v1.0, superseded the same
  date by v1.1
- Retrieved: `2026-07-23`
- Canonical URL or identifier: User-supplied implementation programme; no public identifier stated
- Local source path: `library/revised-epc-experimental-programme-2026/source.pdf`
- Extracted text: `library/revised-epc-experimental-programme-2026/source.txt`
- SHA-256: `5c8516f1c00899ae5923e85af115bf58e275062703670d361ac113d4887f856b`
- Extracted-text SHA-256: `1b455930a84868cfe862234826fde2b152e7d03b1f7a385a7fa05064a53649dc`
- Superseding revision: `v1.1/source.pdf`
- v1.1 SHA-256: `fcf44a4dcf83b3c0bdca3edf67a7ab138f04bf4ad17f531b13b2344e7b40537b`
- v1.1 extracted text: `v1.1/source.txt`
- v1.1 extracted-text SHA-256:
  `f77635e9845c452b430c3967cdb9872d76312de9bbbf566ba39268ae2b63dce4`
- License/access constraints: No license stated; local research use
- Privacy tier: `local-private`
- Tags: `epc`, `causal-fibres`, `homotopy`, `gpt-2`, `mork`, `predictive-coding`, `experimental-programme`
- Related projects: `causal-fibres-ladder`, `relaleap`, `morkql`, `hyperseed-formalizations`

## Summary

This eleven-page implementation programme revises the causal-fibres/ePC
sequence in response to Mesto's provisional GPT-2 homotopy-PC and MORK
results. It promotes guarded homotopy absorption to E1, frontier stability and
fibre emergence to the keystone E2 test, structured versus unstructured
frontier settlement to E3, deployment-honest teacher-free settlement to E4,
and six-layer MORK hosting to E5. It specifies shared invariants, metrics,
controls, branch logic, artifacts, and provisional acceptance criteria.

## Key claims or contents

- E1 compares BP-anchored homotopy against the archived R8/R9 direct-ePC
  pathology at matched seeds and token budget, measuring teacher-free
  fidelity, per-block frontier depth, representation rank, and error-mass
  concentration (pages 4-5, section 3).
- E2 asks whether concentrated settled-error fields contain stable,
  context-indexed and factor-aligned structure. It combines split-half support
  Jaccard, principal-angle stability, robust JBD, do-intervention
  fingerprints, and an observability floor with matched nulls (pages 5-7,
  section 4).
- E3 compares dense, unstructured top-k, fibre-projected, and random-k
  settlement at equal scalar update counts, emphasizing compositional shift,
  routing transfer, and continual drift (pages 7-8, section 5).
- E4 separates feed-forward, teacher-clamped, observed-token,
  symbolic-constraint, and combined teacher-free settlement. Its key measure
  is the fraction of the teacher-clamped gap recovered by deployable symbolic
  constraints (page 8, section 6).
- E5 proposes MORK forward, settlement, sparse incremental writes, fibre
  registration, and explicit cost accounting for the six-layer model
  (pages 8-9, section 7).
- Mandatory controls are a BP residual, dictionary learning on the identical
  error cells, and matched-compute BP fine-tuning (page 9, section 8).

## Methods or implementation details

- Existing six-layer synthetic compositional grammar rig with ground-truth
  context signatures, do-operations, ID and compositional-shift splits.
- Explicit error tensors at all six block outputs; geometric settlement-depth
  schedule from `T=1` toward `T=128`.
- First-class clamped and teacher-free evaluators, per-block reporting,
  matched seeds, immutable versioned configs, runtime frozen-weight
  assertions, and persisted error-field sufficient statistics.
- Phase order: E1 plus shared harness/C1; E2 plus C2; E3/E4; then E5, with
  conditional advancement based on explicit branch results.

## Limitations and uncertainties

- The plan deliberately treats Mesto's external claims as provisional, but
  portions of its motivation still assume that the homotopy and MORK results
  will reproduce. E1 and E5 must remain tests, not inherited facts.
- “Strict envelope over n>=3 replicates” is appropriate for estimating
  variability but cannot serve simultaneously as calibration and confirmatory
  evidence. Calibration replicates and confirmatory seeds must be disjoint,
  with the rule and final bars frozen before confirmatory outcomes are seen.
- The provisional `no block >50%` frontier-depth and `>=0.8x` teacher-rank
  bars need justification from positive/pathology controls or explicit
  scientific loss, not merely a replicate envelope.
- The source says the current rig has `F=4`, whereas prior causal-fibres H0
  smoke used five binary factors. The harness must obtain factor names and
  counts from the actual frozen protocol and reject mismatches.
- R8/R9 used a GPT-2-small-based six-layer student protocol whose source is at
  commit `ecf2f79` on `agent/epc-outcome-probes`; the revised programme's
  wording “six-layer teacher” must be reconciled against that code and its
  actual teacher/student identities before config freeze.
- E3's online top-k condition needs an implementation-level compute
  definition. If dense errors must be computed before selecting top-k, scalar
  update count alone understates its true evaluation cost.
- Storing per-sample error cells can be large. The ledger must bound probe
  count, dtype, and storage before any full run while retaining sufficient
  statistics for split-half and intervention analyses.
- E5 is a separate engineering workstream and must not become a prerequisite
  for interpreting E1/E2 neural evidence.

## Relevance to current work

The plan is accepted as the current strategic programme for
`projects/causal-fibres-ladder`, superseding the earlier linear progression
that treated target-scope H0 as a blocker before any absorption revisit.
The standing BP-residual H0 test is retained as control C1. Immediate work is
Phase 1: reconcile the archived R8/R9 source/config, write shared harness
invariants and versioned acceptance files, run reduced deterministic controls,
and estimate full-campaign storage/runtime. Paid compute remains unapproved.

Research Rules 1, 2, 3, 5, 6, and 7 are especially relevant: validate JBD and
frontier estimators on constructed controls; freeze a plain-language and
machine-readable spec; reuse causal-fibres and archived R8/R9 machinery;
retain exact provenance; preserve the H0-H6 conceptual mapping; and keep
PyTorch/MORK and dense/top-k/fibre interfaces modular.

## Revision note: v1.1

Ben supplied v1.1 at 23:05 PDT on 2026-07-23. It supersedes v1.0 prospectively
but explicitly preserves completed and in-flight v1.0 work.

The principal interpretive correction is that Mesto's fidelity measurements
were teacher-free feedforward evaluations and the reported rising ratio was a
gradient-alignment statistic, not a state-space error ratio. Mesto reports the
terminal settled ePC field as nearly identical to the BP adjoint: global L2
`5.6e-4`, per-block gradient cosine at least `0.998`, and PC/BP gradient-norm
ratio approaching `0.98`. These remain supplied external measurements pending
reproduction on the local six-layer rig.

Consequent programme changes:

- E1's scientific priority shifts to cheap post-hoc P1 depth-profile and P2/M0
  settled-field-versus-adjoint checks. E1b is optional and low priority.
- E2 becomes dual-substrate: the same M1--M5 battery runs on settled error
  fields and plain teacher-free CE adjoint fields.
- Prediction 2 must be frozen before E2 fingerprints are unblinded:
  factor-aligned structure should co-locate with the measured frontier blocks.
- E3 adds DGC-style gradient sparsification with residual accumulation and a
  settle-versus-raw-BP proximal ablation.
- E4 drops the amortization-gap framing. Feedforward is the deployed default;
  test-time settlement is useful only if new observed or symbolic information
  improves on it.
- E5 frontier writes are benchmarked as sparsified-gradient maintenance.

The source's statement that “E1 is complete” refers to the programme status
assumed by its authors. It does not upgrade the local 12-update operational
smoke into a scientific E1 result.

## Quotations or excerpts

> “A run that trips a guard or fails acceptance is a result, not a discard.”

> “The teacher-clamped settle cannot be the deployed object.”

## Follow-up questions

1. Which disjoint seeds form the calibration and confirmatory sets for E1?
2. What positive and pathology controls justify the frontier-depth and
   effective-rank bars?
3. Which exact R8/R9 commit/config is canonical after the archived run's
   source-commit discrepancy (`9ccb151` in the command versus `ecf2f79` in the
   final run ledger)?
4. What storage budget preserves split-half/intervention evidence without
   saving an impractical dense error tensor corpus?
5. For E3, does matched budget include dense frontier discovery, or only
   applied scalar updates?
