# CLA detector provenance audit, 2026-07-16

## Finding

The 2026-07-15 preregistered OmegaSim run recorded the clean OmegaSim
repository at commit `5a6002bd134ffb60e4f20b6c506a1ff6795e7afa`, but its command imported
`chaoslang` from a second repository and did not record that repository's
commit or working-tree status. Therefore the reported `4/5` result is not
promotable replication evidence. It remains a hypothesis-generating result.

## Bounded reconstruction

The dependency repository reflog places commit
`974af31efaf6e3cc239252f78367d20e657ac45c` (the train-fitted k-means
implementation) at 2026-07-15 08:28:16 PDT, before the run began at 08:30:49
PDT. Its next commit, `457d5bcd7d576fcd6b17f891c2e7169c081d3bf4`, was made at 09:09:36 PDT,
after the run finished at 09:02:15 PDT, and adds only report `.tex`/`.pdf`
files. This strongly identifies the committed dependency tree, but cannot
retroactively prove that its working tree was clean during the run.

## Fail-closed repair

Untouched-seed replication must use:

- OmegaSim commit `5a6002bd134ffb60e4f20b6c506a1ff6795e7afa`, clean;
- detached `chaoslang` commit `974af31efaf6e3cc239252f78367d20e657ac45c`, clean;
- the unchanged detector script and thresholds from the original
  preregistration;
- a new experiment record that captures both repositories, file hashes,
  commands, seeds, environment, logs, exit status, timing, and artifact hashes.

No detector behavior may be changed in response to OmegaSim outcomes. The
Mackey--Glass and Lorenz--96 calibration gates remain prerequisites for any
strange-attractor or grammatical-structure claim.
