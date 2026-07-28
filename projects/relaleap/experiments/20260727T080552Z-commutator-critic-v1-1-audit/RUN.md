# Run 20260727T080552Z-commutator-critic-v1-1-audit: supplied V4 package audit

- Project: `relaleap`
- Started: `2026-07-27T08:05:52Z`
- Finished: `2026-07-27T08:12:40Z`
- Status: `inconclusive`
- Operator/agent: `ZeroBot`
- Local or remote: `local`

## Question

Do the supplied quadratic sandbox and patched `comcrit` package reproduce
their available CPU claims, and what remains unverified without JAX?

## Hypothesis or expected behavior

The NumPy quadratic demo should reproduce its checked-in JSON within numerical
tolerance. The package's non-JAX tests and PyTorch optimizer-replica admission
gate should pass. JAX-specific nonlinear and batching claims may remain
unreproduced because JAX is absent from the base environment.

## Inputs

- Repository and commit: supplied archive, not a Git repository; RelaLeap
  comparison worktree `agent/colearned-causal-critic-v1` at `9be8222`
- Dirty patch or uncommitted state: none in the comparison worktree
- Data identifiers and hashes: source hashes in
  `../../../library/commutator-critic-v1-1/SHA256SUMS`
- Configuration: commands in `command.sh`
- Random seeds: embedded in supplied scripts

## Environment

- Host/GPU: `pop-os`, CPU only
- OS/container image: Pop!_OS host, Linux `7.0.11-76070011-generic`
- Language and dependency versions: Python 3.10; NumPy 2.2.6; Torch
  2.12.1+cpu; pytest 9.1.1; JAX absent
- Environment capture: `env.txt`

## Command

See `command.sh`.

## Results

- Exit status: `1` (package admission gate failed)
- Quadratic demo: independently reproduced; output JSON is byte-identical to
  the supplied checked-in result (`SHA-256
  52093cc8167072cb44969d9c5b33537c47544d066ac0575bddd7e693c45bc023`).
- Quadratic mechanisms reproduced: rollout/closed-form maximum relative error
  up to `2.6119e-8`; backbone Spearman `0.9945--0.999997`; planted synergy
  effect `8.73--22.15x` the measured noise floor; aligned-null false beneficials
  `0`; no-signal fraction grew from `0.00` to `1.00`.
- Built-in `comcrit.selftest()`: passed its NumPy checks; JAX test skipped.
- Packaged tests: `5 passed, 4 failed, 1 skipped`. All four failures are the
  PyTorch functional optimizer replica's declared bit-exact admission tests
  (AdamW with weight decay `0`/`.01`; SGD with momentum/weight decay
  `0`/`0` and `.9`/`.01`) on Torch `2.12.1+cpu`.
- A one-step diagnostic found discrepancies at last-bit scale in simple cases
  (e.g. SGD maximum absolute difference `3.47e-18`), but the package contract
  is explicitly bit-exact, so this does not waive the gate.
- Both supplied unified diffs dry-run cleanly against the skeleton using
  `patch -p0`; the already-patched v0.1.1 tarball contains the acceptance tests.
- Artifacts: `artifacts/results_quadratic-reproduced.json`
- Logs: `stdout.log`, `stderr.log`

## Interpretation

**Reproduced:** the quadratic identity/backbone/failure-demonstration bundle
is internally consistent and deterministic in this environment. This is real
support for replacing fixed declared orderings with per-state truth and a
measured no-signal regime.

**Not reproduced:** the nonlinear MLP/Adam exact-D results, tangent-column
batching equivalence/performance, and JAX decomposition tests; JAX is absent.

**Blocked:** the supplied PyTorch backend is not admitted on the target host
under its own bit-exactness criterion. The numerical deviations may be harmless
rounding/order differences, but exact-D science requires either a replica that
matches the chosen Torch implementation or a newly justified tolerance plus
an end-to-end tangent-equivalence test. No existing RelaLeap code was changed.

## Reproduction

Run `command.sh` from the workspace root. It uses a temporary extraction
directory and does not modify the existing RelaLeap worktree.

## Follow-up

1. Diagnose and repair/version-gate the PyTorch optimizer replicas before any
   RelaLeap integration.
2. If Ben requests continued execution, create a reviewed isolated JAX
   environment and reproduce the nonlinear exact-D and batching claims.
3. Only then transplant a minimal C0 backbone/fixture slice into a fresh
   RelaLeap branch; do not open C2 or policy work yet.
