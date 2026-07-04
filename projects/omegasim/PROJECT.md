# OmegaSim Thresholded Appraisal Simulations

## Purpose

Reboot OmegaSim as a reproducible local simulation project for OmegaHive-like cognitive dynamics. The immediate scientific question is whether structured, bounded, nonperiodic lobe transitions can arise from cognitively meaningful mechanisms--thresholded appraisal, artifact handoff, fatigue, adaptive thresholds, delay, and prediction-error feedback--rather than from arbitrary chaos injection.

## Current focus

- **Paused by Ben on 2026-07-03 pending CLA.** OmegaSim should restart after CLA or a similar grammar-of-attractors detector can robustly recognize complex strange-attractor structure in known systems and OmegaSim-scale traces. Routine OmegaSim scheduled/progress updates are also paused until restart; answer only direct OmegaSim-specific requests meanwhile.
- Previous focus: A6 single-hive role-coupled motivational/appraisal model and detector calibration.

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

## Risks and open questions

- The first A6 model is intentionally minimal; it demonstrates the experimental harness and order parameters, not a validated cognitive theory.
- Need refine exact-tuple matched excess scoring into amplitude/variance-nearest matching and add residual/lobe metrics beyond macro-role strings.
- Need decide whether to create/push a public GitHub repo or fold the prototype into an existing OmegaSim repository if Ben/Protocosmobot has one elsewhere.

- 2026-07-03: Paused by Ben pending CLA. Rationale: OmegaSim cannot sensibly judge whether simulated OmegaHive dynamics have complex strange-attractor structure until CLA or an equivalent detector is robust.
