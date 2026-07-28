# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-27 - P1A metrics pipeline

Implemented the frozen full-grid runner and metric layer: one-sided Wilson
failure bounds, authoritative grid D-star and censoring, deterministic
binomial logistic interpolation, monotonicity diagnostics, isotonic
deviation, WLS law coefficients, coherence alpha, and F3 all-distance
bipolar/linear geometry. Reduced replay evidence is
`experiments/20260727T235800Z-p1a-metrics-smoke/`. The reduced values are
resource/wiring evidence only and cannot freeze thresholds.

## 2026-07-26 - P0/P1 specification and theorem audit

Research Rules 1, 2, 3, 5, 6, and 7 govern the initial instrument phase:
validate the estimator, freeze the software/measurement contract before code,
reuse only sound abstraction seams, preserve raw reproducible evidence,
separate theorem from conjecture, and keep algebra/fixture/model/artifact
components replaceable.

The five supplied manuscripts are preserved with PDFs, extracted text, and
SHA-256 provenance at
`../../library/hdc-cgcct-source-manuscripts-2026/SOURCE.md`. The July synthesis
quotes a coherence-aware cleanup law that is absent from the supplied June 3
HDC manuscript. The matching conditional lemma and near-duplicate analysis
are in the separately preserved July 25 HDC manuscript at
`../../library/resonator-factored-hierarchical-hypervector-embeddings/`.

Audit disposition:

- independent and coherence-aware cleanup bounds are source-established only
  under random-atom/concentration, isometric-binding, finite-dictionary, and
  crosstalk-independence assumptions;
- the sign `k^(3/2)` and linear `k^2` near-duplicate regimes are conditional on
  a constituent-sharing construction and normalization assumptions;
- the claim that implicational hierarchies induce that geometry is explicitly
  Conjecture 1 and is not implied by the closure theorem or Eq. 4 with
  independent feature atoms;
- CGCCT Theorem 7.3 assumes delta-calibrated probes but does not define the
  empirical delta. HDC cleanup does not control learned residual-to-frame
  readout error, so oracle-code and learned-`K` measurements must remain
  separate.

The execution contract is `docs/p0-p1-spec.md`. It adds independent,
near-duplicate, assumption-violating, and hierarchy-distance fixtures;
disjoint 3/5 calibration/confirmation seeds; exact metrics and gates; a
fail-closed artifact schema; and a planted-PCFG next-token fixture.

Reusable-infrastructure inspection found that causal-fibres provides useful
canonical hashing, sample IDs, deterministic seed/replay tests, a six-block
interface, and mature experiment discipline. Its `SyntheticGrammar` is a
four-binary-factor vector classifier, not the required PCFG, and its
`TokenMixingSixBlockStudent` is not an autoregressive token transformer.
Focused validation at nested RelaLeap worktree commit
`4ca1b5ee337934c9cf8b349adbd3716dc7baa221` passed:

```text
python3 -m pytest -q tests/test_e1_homotopy.py
11 passed in 2.26s
```

No GPU, remote resource, paid compute, or unrelated worktree modification was
performed.
# 2026-07-27 — Authorized P0-v2 resolution-grid outcome

Ben authorized the harder-fixture option after P0-v1's ceiling saturation.
V2 retained P0-G1, seed, trial count, atom distribution, scoring, and exact
CPU replay; it changed only the grid to `D={32,64,128,256,512,1024}`,
`k={32,64,128}`, `M={32,256}`. 13/13 tests passed, two full payloads were
byte-identical (`96f3a7142111828cffa458a59ac35699c6ce0077748a14361063ecc4b4dd14f7`),
and every curve Spearman was 1.0. P0-G1 now passes. Preserve v1 as the
documented saturation result; begin P1A preflight only.
