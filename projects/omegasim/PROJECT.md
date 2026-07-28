# OmegaSim Thresholded Appraisal Simulations

## Purpose

Reboot OmegaSim as a reproducible local simulation project for OmegaHive-like cognitive dynamics. The immediate scientific question is whether structured, bounded, nonperiodic lobe transitions can arise from cognitively meaningful mechanisms--thresholded appraisal, artifact handoff, fatigue, adaptive thresholds, delay, and prediction-error feedback--rather than from arbitrary chaos injection.

## Current focus

- **Restart directed by Ben on 2026-07-10:** resurrect OmegaSim by rerunning the previous best OmegaSim experiments while leveraging the CLA high-dimensional embedding variant to search for strange attractors with interesting grammatical structure.
- Restart path: first re-run/verify the previous A6 matched-excess regions, then attach CLA high-D embedding diagnostics (deeptime/Python TICA/VAMP, k-means microstates, suffix-trie grammar induction, surrogate excess compression, held-out log-loss) as the attractor-grammar detector.
- Previous pause rationale still matters as a guardrail: do not claim OmegaSim has complex grammatical strange-attractor structure until the CLA detector distinguishes known benchmarks and matched controls.

## Repository

- Local prototype: `projects/omegasim/repos/omegasim`
- Remote: none yet.

## Related records

- Design note: `projects/hyperseed-formalizations/repos/hyperseed-formalizations/papers/0004-omegasim-strange-attractor-tuning/`
- Feedback capture: `projects/hyperseed-formalizations/NOTES.md`, section `2026-07-01 - OmegaSim feedback: thresholded appraisal, not arbitrary logistic chaos`.
- OmegaClaw context: `projects/omegaclaw/NOTES.md`, section `2026-07-01 - OmegaSim feedback attachment captured for Hyperseed/OmegaHive design`.

## Status

- 2026-07-01: Created local project and dependency-free Python A6 prototype. Smoke tests pass. First sweep experiment `experiments/20260702T012924Z-a6-smoke-sweep/` ran 243 local conditions. It found 18 bounded appraisal candidate regimes by naive macro-role criteria, but controls showed those criteria needed tightening around functional artifact/risk/debt dynamics.
- 2026-07-01: Added preregistered A6 functional candidate gate and reran the same 243-condition local sweep. The stricter metric reduces shuffled-control false positives (2/81) but linear controls still pass more often than appraisal controls (37/81 versus 24/81), so the result remains fail-closed for appraisal-specific claims.
- 2026-07-02: Added matched excess-over-control scoring against exact seed/gain/delay/coupling linear and shuffled controls. Experiment `experiments/20260702T100000Z-a6-matched-excess-scoring/` found 7/81 appraisal rows exceeding matched controls, localized at `gain=5.0`, `coupling in {0.35,0.60}`, `delay in {0,3}`. Broad appraisal-specific claims remain fail-closed; next step is denser local sweeps plus residual/lobe structure metrics.
- 2026-07-15: Executed the fresh frozen CLA-detector preregistration locally (180 rows, five seeds, three independent strata). One of 12 cells promoted: `coupling=0.60`, `delay=3`, `roles8`, with appraisal beating both exact-tuple controls in four of five seeds. This is bounded proxy evidence only; untouched replication and Mackey--Glass/Lorenz--96 calibration remain required. Evidence: `experiments/20260715T153049Z-cla-detector-preregistered/RUN.md`.
- 2026-07-16: A provenance audit found that the discovery ledger omitted the external `chaoslang` repository identity/dirty state, so the original 4/5 is hypothesis-generating rather than promotable evidence. A repaired, fully pinned untouched-seed replication then met the frozen `roles8` criterion at 4/5 seeds. This remains proxy evidence only; Mackey--Glass/Lorenz--96 calibration still gates attractor/grammar claims. Evidence: `docs/cla_detector_provenance_audit_20260716.md` and `experiments/20260716T164500Z-cla-roles8-untouched-replication/RUN.md`.
- 2026-07-16: A fully captured bitwise replay repaired the untouched ledger's missing environment capture without overwriting its artifacts. All 45 CSV rows were byte-identical and normalized JSON was exact under clean OmegaSim `18c7408` / chaoslang `974af31`; this supports reproducibility but is not a second independent replication. Evidence: `experiments/20260716T204500Z-cla-roles8-bitwise-replay/RUN.md`.
- 2026-07-16: The independent CLA lane completed a preregistered frozen held-out Mackey--Glass/Lorenz--96 x0 benchmark at clean commit `c8e9e91`. Integrity gates passed, but CLA lost aggregate total coding length to the unigram baseline (`65,976.621` versus `6,588.443` bits). This is a calibration failure, not a claim about either attractor. It also exercised a stricter held-out coding path rather than OmegaSim's frozen proxy path, so the OmegaSim benchmark prerequisite remains open. Evidence: `../chaos-language-algorithm/experiments/20260716T172310Z-frozen-heldout-calibration-v1/RUN.md`.
- 2026-07-16: The exact frozen OmegaSim proxy passed a preregistered same-path temporal-order calibration on Mackey--Glass and Lorenz--96, with 5/5 ordered-versus-joint-time-shuffle wins for each system. This closes the same-path sensitivity prerequisite without changing the detector, but does not rescue the independent stricter held-out coding failure or unlock strong attractor/grammar claims. Evidence: `experiments/20260716T224635Z-cla-same-path-external-calibration/RUN.md`.
- 2026-07-16: A local frozen-detector dynamics exploration produced 486 observed readouts over the five-seed A6 tight region plus a balanced 12-point/two-seed broader sample. Four tight cells met the matched proxy rule, but every grammar had exactly two productions and zero categories, and every appraisal and linear row was detector-positive. This supports temporal-order sensitivity while failing to resolve distinct grammatical regimes; attractor/grammar claims remain gated by the stricter held-out coding failure. Evidence: `experiments/20260717T000000Z-cla-dynamics-exploration/RUN.md`.
- 2026-07-17: Stratified re-sweep batches 01--03 added 48 full-grid roles-specific cells (24 parameter triples), each with three seeds and exact controls. All 432 grammars were trivial (one or two productions, zero categories). Batch 01 had two quantitative 5/6 matched-control triples, batch 02 had no triple above 1/6, and batch 03 had two triples at 4/6. This is an expanding informative negative grammar result, not an attractor claim. Evidence: `experiments/20260717T164500Z-a6-stratified-cla-resweep-01/`, `experiments/20260717T184500Z-a6-stratified-cla-resweep-02/`, and `experiments/20260717T204500Z-a6-stratified-cla-resweep-03/`.
- 2026-07-17: Batch 04 expanded coverage to 64/120 roles-specific cells. All 144 new grammars remained trivial; `(5,.80,3)` reached 6/6 and `(2,.15,3)` reached 5/6 exploratory joint matched-control wins. Evidence: `experiments/20260717T224500Z-a6-stratified-cla-resweep-04/`.
- 2026-07-17: Successful batch 07 expanded coverage to 80/120 roles-specific cells after preserving two non-result setup ledgers. All 144 new grammars remained trivial; `(1,.35,5)` and `(2,.15,5)` reached 4/6 exploratory joint matched-control wins. Evidence: `experiments/20260718T024700Z-a6-stratified-cla-resweep-07/`.
- 2026-07-17: Batch 08 expanded successful coverage to 96/120 roles-specific cells. All 144 new grammars remained trivial; `(2,.15,0)` reached 6/6 exploratory joint matched-control wins. Evidence: `experiments/20260718T044500Z-a6-stratified-cla-resweep-08/`.
- 2026-07-17: Batch 09 completed the eight remaining non-tight triples, bringing the stratified series plus separately frozen tight roles8 cells to 116/120 planned roles-specific cells. All 144 new grammars again had two productions and zero categories. Only the four tight-region roles4 cells remain before full-grid closure. Evidence: `experiments/20260718T064500Z-a6-stratified-cla-resweep-09/`.
- 2026-07-18: Batch 10 completed the four remaining tight-region roles4 cells, closing all 120 planned roles-specific grid cells. All 36 new grammars had two productions and zero categories; across the completed stratified sweep, every grammar remained trivial. This is an informative full-grid negative under the frozen detector, not an attractor or simplicity claim. Evidence: `experiments/20260718T084500Z-a6-stratified-cla-resweep-10/`.

## Risks and open questions

- The first A6 model is intentionally minimal; it demonstrates the experimental harness and order parameters, not a validated cognitive theory.
- Need refine exact-tuple matched excess scoring into amplitude/variance-nearest matching and add residual/lobe metrics beyond macro-role strings.
- Need decide whether to create/push a public GitHub repo or fold the prototype into an existing OmegaSim repository if Ben/Protocosmobot has one elsewhere.

- 2026-07-03: Paused by Ben pending CLA. Rationale: OmegaSim cannot sensibly judge whether simulated OmegaHive dynamics have complex strange-attractor structure until CLA or an equivalent detector is robust.
