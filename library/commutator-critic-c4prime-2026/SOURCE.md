# Source: A Function-Pinned Testbed for the Commutator Critic

- Type: `PDF companion note / proposed experimental specification`
- Authors/organization: author not stated in PDF metadata; supplied by Benjamin Goertzel; AI acknowledgement names Claude Fable 5
- Publication/version date: `July 2026`
- Retrieved: `2026-07-27`
- Canonical URL or identifier: user-supplied document; none stated
- Local source: `c4prime_implications.pdf`
- Searchable text: `c4prime_implications.txt`
- SHA-256: `fb56d41d95dec31cbbc525fb4597f822e56ef6b19073566ce6fd053817d29dc6`
- Extracted-text SHA-256: `c21744e70e8dd3cf37aea8a21fc8c9ef6ee376f2dde24d1d67cf898bb7381367`
- License/access constraints: no license stated; preserve locally and quote sparingly
- Privacy tier: `local-private`
- Tags: `RelaLeap`, `commutator critic`, `comcrit`, `predictive coding`, `GPT-2`, `homotopy distillation`, `continual learning`, `C4-prime`
- Related projects: `relaleap`, `causal-fibres-ladder`, `morkql`

## Summary

This companion note composes the proposed RelaLeap V4 commutator critic with
Mesto's reported homotopy-distilled PC--GPT-2 substrate. Its central proposal
is to measure learning-rule-dependent commutator and trajectory-response
quantities across a reportedly function-preserving homotopy, thereby reducing
the usual confound between model function and learning rule.

The engineering half proposes a `PCStepAdapter`, continuation-validated
unrolled/IFT tangents, a frontier-based pair sparsifier behind an empirical
admission gate, a one-page CCL preregistration, and a GPU stage named C4′.
The document is a specification and argument, not an execution result.

## Key claims and proposed tests

- The homotopy is treated as a function-pinned family because Mesto reports
  prompt KL near `1e-5` at every rung (Sections 1--2, pages 2--3).
- Per-block PC/BP cosine `>=0.998` is argued to be an `h=1` statistic that
  cannot determine horizon-dependent counterfactual response; C4′ therefore
  measures exact propagated tangents and paired rollouts (Section 3, page 4).
- Validation of the equilibrium/IFT branch is proposed by continuation from
  the trusted `T=1` anchor, with unrolled-vs-IFT agreement at a crossover rung
  (Section 4, page 4).
- The reported top-5% error-mass frontier is proposed both as a pair-action
  sparsifier and as a falsifiable predictor of per-block intervention effects
  (Section 5, page 5).
- C4′ freezes three homotopy rungs, 12 blocks plus head, 3 matched seeds,
  80 decision states per rung, horizons `{1,5,10,25}`, CRN paired truth,
  tangent-mode admission bands, noise floors, and a 45-A100-hour programme
  ceiling (Section 8, pages 7--9).

## Assessment

**Conceptually strong:** function pinning makes the proposed comparison much
cleaner than separately trained BP and PC models. The distinction between
instantaneous gradient geometry and trajectory response is aligned with the
already reproduced quadratic V4 sandbox. Freezing weight-step gating while
deferring settle-side gating is also a useful identifiability choice.

**Not yet executable:** the workspace does not contain Mesto's production
checkpoints or settle implementation. The July 26 revision reports a
completed 50-million-token run but still provides no raw telemetry or
checkpoint hashes. In addition, the
local audit of `comcrit` v0.1.1 found four failures in its own bit-exact
Torch optimizer-replica gate, and JAX exact-D claims remain unreproduced.

**Budget uncertainty:** the 8/12/20 A100-hour rung estimates are proposals,
not measured profiles. They should not become a paid-compute request until an
anchor microprofile records memory, JVP cost, action-column batching, and
artifact size on the actual substrate.

**Statistical caution:** the note's `>=0.6` frontier-effect Spearman and other
numeric gates are preregistration candidates, not source-derived constants.
The strict-envelope and 5-sigma rules are sensible, but their calibration must
occur without opening the final confirmation outcomes.

**Visual inspection:** pages 1 and 8 were rendered from the preserved PDF.
The inspected C4′ action/truth/gate notation matches the extracted text; no
figure or table supplies additional empirical evidence.

## Required prerequisites before C4′

1. Obtain and hash the exact Mesto checkpoints, settle code, configs, data
   identifiers, production telemetry, and license/access terms.
2. Repair or explicitly version/tolerance-gate the functional optimizer
   replicas, then reproduce the nonlinear exact-D and tangent-column tests in
   an isolated environment.
3. Implement and unit-test `PCStepAdapter` at `T=1`; reproduce the C4-class
   anchor gate locally or on a tightly bounded GPU microprofile.
4. Freeze the task pair, estimand, `K_mn(tau)` estimator, floors, deviations,
   and budget-cut rule in a separate preregistration before any E-line result
   is opened.
5. Produce a measured remote-compute proposal; the PDF's 45 A100-hours are
   not authorization.

## Provenance relationships

- Mesto report: `../mesto-homotopy-pc-gpt2-2026/SOURCE.md`
- V4 source package: `../commutator-critic-v1-1/SOURCE.md`
- Local V4 audit:
  `../../projects/relaleap/experiments/20260727T080552Z-commutator-critic-v1-1-audit/RUN.md`
