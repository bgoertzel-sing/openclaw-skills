# E0 coder calibration v1

- Status: completed; exit 0; integrity controls passed; frozen aggregate rule
  failed.
- Freeze time: 2026-07-26T10:15:00-07:00 /
  2026-07-26T17:15:00Z.
- Repository:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `096cbb11b2d60e4d07a7bbfffb30b808e169dab4` (clean).
- Protocol: `docs/e0-coder-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

This ledger freezes E0's deterministic iid, Markov-1, Markov-3, and periodic
source laws; five seeds; three lengths; six coder arms; analytical entropy
rates; all row and aggregate predicates; and historical canonical-LZ78
continuity artifacts. The separately approved adaptive Markov-3 arm is E0-only.
The declaration tests do not generate any frozen-seed stream or coder score.

- Protocol SHA-256:
  `f9f4200b657844597c53a15cf1d9ca1320eda99c30697aa993ec1882bd399c1d`.
- Runner SHA-256:
  `f00a48b97fc24e18edda5f9db8ef92228f2e4aad0afb1276684f0f36cf70d4f6`.
- Ledger manifest SHA-256:
  `ae03b8ae0ed2b4093e70ca6e6d20c1d0fff0b678ffbb1b4802b97a9baae86bb8`.
- Wrapper SHA-256:
  `0e1fbe08fc1e52d94451649036f8bf7d7d00b4f31f02518562fff8c8a8657850`.
- Frozen command SHA-256:
  `b6e60a1d2596e7d2983b62d7a001232d860506f3bfc01b90e98622699b87ef79`.
- Declaration-test SHA-256:
  `0d3463bacffcbacc2035c832ba2b80d936a7aa2ef209a8457ab4dd55538fd13d`.
- Pre-outcome checks: ledger declaration tests passed 4/4; runner focused
  tests passed 4/4; required stdlib discovery passed 283/283; compileall and
  both repository diff checks passed. No frozen-seed fixture or score was
  generated.

The sole decisive command, after this ledger is acceptance-tested and committed
cleanly, is exactly `bash command.sh` from this directory. It may execute once.
No result may be tuned or rescored under this v1 gate.

This is coder calibration only. It supplies no evidence of chaos, attractor
recovery, hierarchical generativity, semantic grammar, or superiority over
CSSR on positive-entropy sofic regimes. E3 remains binding and OmegaSim remains
paused until E7 resolves and E8a passes.

## Results

The exact `bash command.sh` invocation ran once and exited 0 with empty stderr
in 15:40.45 wall time, using 369,844 KiB maximum RSS. All matching-coder
entropy-convergence predicates passed for all five seeds, every CTW sanity
band passed, both Markov-source M2 comparisons passed, and the iid M2
comparisons passed for vocabulary sizes 2 and 4 and for Zipf-v16. Historical
manifest/result provenance and all four canonical-LZ78 bit, reconstruction,
and byte-stability checks passed.

The aggregate E0 rule nevertheless failed because all five 100,000-symbol
`iid-uniform-v16` rows exceeded the frozen adaptive-Markov-2 redundancy
allowance:

| seed | excess beyond frozen allowance (bits) |
| ---: | ---: |
| 26072601 | 274.625 |
| 26072602 | 317.872 |
| 26072603 | 318.820 |
| 26072604 | 417.373 |
| 26072605 | 438.455 |

No threshold, implementation, source, seed, or result was tuned or rescored.
This v1 gate is closed as failed. Its narrow failure localizes to the
high-cardinality iid Markov-2 redundancy predicate; it does not revise the
passed coder checks or authorize E1.

Post-run focused E0 tests passed 4/4; required stdlib discovery passed 283/283;
compileall and `git diff --check` passed. Artifact SHA-256 values:

- `results.json`:
  `3f3b68b39425628f43e28f75758a7f722aba048a9d74aa4a254890dac8942f85`.
- empty `stderr.txt`:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`:
  `98d695bb1383860d29d9642a3210c56989c4e2bceedf7acaf30ef9c6006c60d9`.
- `exit-status.txt`:
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
