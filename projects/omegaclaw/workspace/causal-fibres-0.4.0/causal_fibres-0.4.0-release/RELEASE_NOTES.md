# Release notes: 0.4.0

Version 0.4 is a critique-driven revision that broadens `causal-fibres` from an
orthogonal-fibre-first package into a comparative structural-adaptation
framework.

## Major changes

- Added dense, sparse-autoencoder, grouped-overcomplete, orthogonal-fibre, and
  context-conditioned bundle representation classes.
- Added reconstruction and teacher-residual representation contests.
- Added a mandatory SAE + steering baseline and dependency-free LoRA tools.
- Added frozen-read observability probes, layerwise audits, and teacher-gap
  capacity curves.
- Added controlled low-rank substrate co-adaptation, anchor trust regions, and
  alternating residual/base training.
- Changed the conservative credit default to exact autograd plus responsibility
  gating (`oracle_gated`).
- Added soft responsibility gradient gates over disjoint parameter groups.
- Added explicit predictor-only, free, constrained, and teacher-clamped
  settlement evaluation modes.
- Added matched-compute and finite curriculum-order evaluators.
- Added held-out-context routing metrics.
- Added overcomplete dictionary-coordinate operator audits.
- Added a conservative module certification ladder and underidentification
  status.
- Added revised staged Transformer configurations in which learned highways and
  symbolic caps occur only after earlier gates pass.
- Added five new runnable examples and extensive critique-driven documentation.

## Compatibility

Existing 0.3 terminal sidecars, solvers, JBD tools, interventions, checkpoints,
and symbolic-store APIs remain available. `FibreStatus.CAUSAL` is retained as a
backward-compatible alias for `CAUSALLY_IDENTIFIED`.

## Scientific default

The new safe default is:

```text
dense representation + frozen base + exact gradients + no settlement
+ mandatory observability and SAE controls
```

Every stronger structural claim must now earn its place through explicit stage
gates.
