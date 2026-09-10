# Run 20260725T001224Z-e4-cmcp-ledger-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T00:12:24Z`
- Finished: `2026-07-25T00:13:01Z`
- Status: `failed before scientific execution`
- Operator/agent: ZeroBot
- Local or remote: local CPU

## Question

Can a provenance-first CMCP conditional-information ledger suppress duplicate
and deterministically derived symbolic E4 constraint packets while preserving
useful independent repeated evidence on the confirmed text-like substrate?

## Hypothesis or expected behavior

CMCP should match the oracle effective precision on exact duplicates and
deterministic descendants, assign nonzero information to an independent repeat,
remain invariant after known rotated-frame alignment, and avoid worse mean CS
loss than naive repeated injection on redundant streams. Direction-only
novelty is expected to suppress both redundant and independent repeats.

## Inputs

- Repository branch: `agent/e1-guarded-homotopy`
- Base commit: `154e5cfb604ffeeca314b22429e34d26b490a61c`
- Dirty state: CMCP protocol/source/tests/scripts plus pre-existing unrelated
  untracked calibration artifacts; exact status will be captured in `git.txt`.
- Configuration: `configs/e4_cmcp_ledger_calibration_v1.json`
- Seeds: `51001, 52103, 53209`
- Protocol: `docs/e4_cmcp_ledger_protocol.md`

## Environment

- Host: local Intel i7-1165G7 CPU
- Python/Torch versions captured in `env.txt`

## Command

See `command.sh`.

## Results

- Exit status: `1`
- Metrics: none; no seed started
- Artifacts: none
- Logs: `stdout.log`, `stderr.log`

## Interpretation

The launch wrapper did not expose repository `src/` on `PYTHONPATH`, so the
runner failed importing `relaleap`. This is an operational guard failure, not
scientific evidence.

## Reproduction

Run `command.sh` from the recorded repository and environment.

## Follow-up

Relaunch under a new run ID after adding only `PYTHONPATH=src`. Freeze
confirmation tolerances only if constructed tests and calibration estimator
invariants pass.
