# Run 20260716T204500Z-cla-roles8-bitwise-replay

- Project: `omegasim`
- Started: `2026-07-16T20:48:17Z`
- Finished: `2026-07-16T20:55:46Z`
- Status: `succeeded; exact replay equality passed`
- Local or remote: `local CPU`

## Question

Can the exact pinned untouched-seed replication be replayed in a fully captured
environment with byte-identical CSV rows and semantically identical JSON,
without overwriting or reinterpreting the original untouched artifacts?

## Expected behavior

The replay must fail before measurement if either repository identity, clean
state, or frozen implementation hash differs. A successful replay requires an
exact CSV match and an exact JSON match after removing only the output-path
field, which necessarily differs between ledger directories.

## Inputs

- OmegaSim commit: `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d` (detector parent `5a6002bd134ffb60e4f20b6c506a1ff6795e7afa`).
- chaoslang commit: `974af31efaf6e3cc239252f78367d20e657ac45c`.
- Frozen detector SHA-256: `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.
- A6 model SHA-256: `2b788fb95be7021bd875ce273d3530488e7ec9432edb4b278d48de7ab8e0db3d`.
- Seeds: `101,103,107,109,113`; gain `5.0`; coupling `0.60`; delay `3`; exact appraisal/linear/shuffled controls; all detector defaults unchanged.
- Original JSON SHA-256: `020d9adc7d7bbf1ef423e3e82b398eb86f227b5476b161aa880db9c66b615ccc`.
- Original CSV SHA-256: `6b7ad6c2edc6e3828be1781e6eb2ff0804b3e13eb492c798e13c40ff39bfe45b`.
- Exact command: `command.sh`; environment: `env.txt`; repository capture: `git.txt`.
- Command SHA-256: `b34921fd3fa1894209d9b95072cc547aa9b75d6935ada93d097f2341b094e060`.
- Environment-capture SHA-256: `eb9cb482623caf70255e1e0600a0d18fb73fafa247adb546d50a4c30ea5f9b30`.
- Pre-run checks: 8 tests plus 2 subtests passed; `py_compile`, both clean-tree gates, and `git diff --check` passed. An initial test invocation from the workspace root failed collection because `scripts` was not importable there; the same frozen tests passed from the pinned repository root before measurement.

## Results

- Exit status: 0; elapsed: 449 seconds.
- All 45 CSV rows were byte-identical to the untouched run (CSV SHA-256
  `6b7ad6c2edc6e3828be1781e6eb2ff0804b3e13eb492c798e13c40ff39bfe45b`).
- JSON was exactly equal after removing only `config.output`; the replay JSON
  SHA-256 is `4ef2789a60fbd795f44bfc2930701d3c2982a75f11ada8b4c2240cedabd61608`.
- Confirmatory `roles8` remained 4/5. Operational byproducts remained
  `core4=3/5` and `full20=5/5`; neither changes the preregistered conclusion.
- `stderr.log` was empty. Both pinned worktrees remained clean.
- Raw artifacts: `artifacts/`.
- Logs: `stdout.log`, `stderr.log`, `status.json`.

## Interpretation

Direct observation: a captured local environment reproduced every CSV byte and
all normalized JSON values from the untouched run. This closes the practical
replayability gap caused by the original ledger's missing `env.txt`, although
it cannot retroactively prove every runtime version present at 16:49 UTC.

Inference: the untouched result is reproducible under the recorded environment.
The replay is not an independent seed replication and cannot unlock chaos,
strange-attractor, or semantic-grammar claims.

## Reproduction

From this directory, run `bash command.sh` after reviewing its fail-closed
identity and hash preflight.

## Follow-up

Mackey--Glass and Lorenz--96 calibration of the same frozen proxy path remains
open. The independent CLA lane's held-out coding null and subsequent
`greedy_or_representation_blindness` diagnostic remain unchanged; detector
changes belong to that lane and must not respond to OmegaSim outcomes.
