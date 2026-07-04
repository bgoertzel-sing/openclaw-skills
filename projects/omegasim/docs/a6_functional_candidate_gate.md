# A6 Functional Candidate Gate Preregistration

Date: 2026-07-01
Project: OmegaSim thresholded-appraisal reboot

## Scientific intent

The first A6 smoke sweep showed that role-symbol entropy and nonperiodic macro-role tails are too weak: shuffled controls can look highly active while artifact/risk/provenance-debt dynamics remain nearly flat. This gate tightens the candidate definition before any denser sweep or strange-attractor-like language.

## Model surface

Use the existing dependency-free A6 single-hive thresholded-appraisal model with:

- roles: explore, synth, review, maintain;
- state: motivation, fatigue, adaptive thresholds, artifact maturity, provenance debt, risk, prediction error;
- controls: appraisal, linear, shuffled;
- bounded state variables in [0,1].

No A5 reopening, multi-hive coupling, dashboard, external integration, GPU run, or promotion language is authorized by this gate.

## Candidate criteria

A run is an A6 functional candidate only if all of these hold:

1. bounded state variables;
2. nonperiodic macro-role tail under the current short-period detector;
3. role entropy in a moderate/high range (`role_entropy_bits >= 1.0`);
4. nontrivial but not fully noisy switching (`0.03 <= switch_rate <= 0.85`);
5. functional state movement in the tail:
   - `artifact_range_tail >= 0.03`, and
   - combined tail range over artifact, provenance debt, risk, and prediction error >= 0.12;
6. not obviously risk-collapsed: `risk_mean_tail < 0.95`.

These thresholds are intentionally conservative and smoke-scale. They should be revised only with an explicit result note.

## Comparison rule

Summaries must report candidate counts separately for appraisal, linear, and shuffled controls. If linear or shuffled controls pass at similar or higher rates, the result is not evidence for an appraisal-specific regime; it is a metric failure or model artifact.

## Artifact contract

Write only local files under `projects/omegasim/artifacts/` and an experiment `RUN.md`. Required artifacts:

- command and environment/provenance files;
- per-condition JSON outputs;
- `summary.csv` and `summary.json` with the new functional metrics;
- aggregate notes by control.

## Fail-closed interpretation

Passing this gate does not establish chaos, strange attractors, or OmegaHive cognition. It only authorizes a denser local A6 phase-diagram slice around candidate regions.
