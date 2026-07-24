# Run 20260724T220707Z-e4-non-label-equivalent-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T22:07:07Z`
- Finished: `2026-07-24T22:11:00Z`
- Status: `succeeded`
- Local or remote: `local CPU`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Which non-label-equivalent symbolic source, if any, recovers more than 20% of
CS task-loss headroom through the direct-logit sink, and which condition
should be frozen for disjoint confirmation?

## Preregistered design

- Protocol: `docs/e4_non_label_equivalent_protocol.md`
- Config: `configs/e4_non_label_constraints_calibration_v1.json`
- Calibration seeds: `24109,25219,26339`
- Reserved disjoint confirmation seeds: `27449,28559,29669,30781,31891`
- Sources: every 1/2/3-factor subset, six pairwise parities, four single
  implication rules, and three-factor constraints at noise
  `p=0,0.1,0.2,0.5`.
- Direct-logit scale: `5x`; 64 steps; step size `0.2`; anchor `1.0`.
- Primary metric: `G_loss=(SC_loss-FF_loss)/(TC_loss-FF_loss)`.
- Eligibility invariant: every emitted message admits at least two classes.

## Provenance

- Base Git commit: `55b5547bf827bc7a6c42a807935b94dd0031e6ce`
- Branch: `agent/e1-guarded-homotopy`
- Dirty state: task-specific implementation plus pre-existing untracked
  `artifacts/`, `configs/e1_homotopy_calibration.json`,
  `scripts/run_e1_calibration_multi.py`, and `src/relaleap.egg-info/`.
- Python: `3.10.12`
- Torch: `2.12.1+cpu`
- Host: Linux `7.0.11-76070011-generic`, x86_64
- CPU: Intel i7-1165G7, 8 logical CPUs
- Focused preflight tests: `12 passed in 1.23s`

## Exact command

See `command.sh`. Standard output, standard error, wall time, and exit status
will be captured beside this record.

## Results

Attempt 1 exited `1` before any seed ran because the project-local venv did
not have the repository's `src` directory on its import path. The failure is
preserved in `stdout.attempt1.log` and `stderr.attempt1.log`. `command.sh` was
corrected to export the explicit repository `src` path before attempt 2.

Attempt 2 exited `0` in `14.78s` wall time with peak RSS `296508 KiB`.
All three seed artifacts and the aggregate are complete.

- FF CS task loss: `0.72812 ± 0.15568`; accuracy: `0.96094`.
- TC CS task loss: `0.71481 ± 0.15165`; accuracy: `0.96354`.
- Best eligible condition: `partial3_123`, which supplies object number,
  tense, and negation but leaves subject number unknown and therefore exactly
  two labels possible.
- `partial3_123` CS loss: `0.67783 ± 0.14687`; accuracy:
  `0.98177 ± 0.01966`.
- Defined-seed CS `G_loss`: `3.48925, 3.36351`; mean `3.42638`.
- Seed `24109` retained raw metrics but its `G` is undefined because
  `|TC_loss-FF_loss|=0.0099586`, just below the frozen `0.01` denominator
  floor.
- Best parity: `parity_23`, mean `G=2.07506`.
- Best implication: `implication_2_1`, mean `G=0.79321`.
- Three-factor noisy curve: `p=0: 3.17058`, `p=0.1: 1.40714`,
  `p=0.2: -0.37365`, `p=0.5: -4.83186`.
- All 28 source conditions passed the runtime non-label-equivalence audit.

Calibration therefore provides strong evidence that label equivalence is not
required by the direct-logit sink. `partial3_123` is frozen as the primary
confirmation condition in
`configs/e4_non_label_constraints_confirmation_frozen_v1.json`; confirmation
remains required for the scientific disposition.

## Artifacts

- `artifacts/seed_24109.json`
- `artifacts/seed_25219.json`
- `artifacts/seed_26339.json`
- `artifacts/result.json`
- Aggregate SHA-256:
  `fa2f0471166883caba781d344eaac738a7e8e76c2a694dbd6c9d54115e7e6872`
- Captured execution: `stdout.log`, `stderr.log`
- Preserved failed launch: `stdout.attempt1.log`, `stderr.attempt1.log`
