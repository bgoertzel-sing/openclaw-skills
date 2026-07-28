# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-28 - P1B calibration target layer

The frozen §6.7 target-code realization is now executable: grid validation,
canonical atoms, both hierarchy arms, full lexical/frame binding, and
per-arm ridge replay are covered by 24 tests. A reduced replay is
byte-identical at SHA-256 `b2a6ee25...719e8`. It is deliberately marked
gate-ineligible. Remote launch stays fail-closed until the full trainer,
controls, raw arrays/manifest, metrics, and criteria-freezing path pass.

## 2026-07-28 - P1B calibration runner core

Nested commit `6a807b1` adds the frozen training/early-stop loop, deterministic
residual/readout execution, core feature and closure metrics, hashed raw-array
artifact verification, and seed/criteria fail-closed guards. The reduced
replay passes 26 tests and refuses a confirmation seed. This is not yet a
remote-ready smoke: per-H metrics, representation and shuffled-label controls,
coherence, and peak GPU memory remain required.

## 2026-07-28 - P1A completion and P1B CPU gate

The P1A calibration payload completed and is recorded at
`experiments/20260728T002900Z-p1a-full-grid/`. Calibration monotonicity is
weaker than the frozen threshold on 31/60 assumption-matched curves; do not
alter criteria or call this a confirmation failure.

P1B local smoke passed at nested commit `b4593f4`. The exact full manifest has
36,864 samples and replays byte-identically. Remote launch remains conditional
on an exact live RunPod offer at no more than USD 1/hour and a fully concrete
`REMOTE_JOB.md`; the five confirmation seeds remain sealed.

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
# 2026-07-28 — P1B remote-launch source audit

**Observed:** The P1B source at nested commit `b4593f4` supplies a deterministic
manifest, six-layer decoder, residual extraction, ridge primitive, and a
one-update CPU smoke, but no three-seed calibration runner or raw-artifact
writer. The live RunPod Community RTX 3090 offer at USD 0.22/hour satisfied
the approved cost/resource limit, yet no P1B pod was created because the
artifact-schema precondition was not met.

**Observed:** Specification §6.4 requires a fresh readout for each `D` and
names independent-atom and planted-path-composite code arms, but §6 does not
name the P1B dimension set nor give the exact role/binding target-code recipe.
P1A's grid applies to its cleanup fixtures (§5.1) and cannot be silently
borrowed for P1B.

**Decision:** Fail closed until Ben supplies this narrow P1B amendment. The
implementation may not choose those scientific parameters on its own.

**Resolution (2026-07-28):** Ben authorized either a direct choice or a
ProtoMega consultation. ProtoMega's concrete proposal was reviewed against
the existing Eq. 4 and F3 rules and accepted as §6.7 / decision
`D-20260728-p1b-code-realization`. The implementation blocker is resolved;
the separate missing-runner/artifact implementation work remains.
