# Nearest-neighbor divergence Stage-A calibration v2

- Status: executed once; Stage A passed; Stage B remains unauthorized pending
  a distinct frozen protocol.
- Freeze time: 2026-07-20T18:15:00-07:00 / 2026-07-21T01:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `85667bd0937eef0de8023db8d7462c6d3afc73a5` (clean).
- Protocol: `docs/nearest-neighbor-divergence-calibration-preregistration-v2.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

V2 preserves V1's six fixtures, representations, prefix-only normalization,
Theiler windows, horizon, fit interval, threshold, seeds, and exact all-six
decision rule. Its only correction is a pre-specified runner status for the
exact no-positive-distance-pair condition: zero pairs, null slope, and not
promoted. Any other detector error remains fatal, and a degenerate positive
fails the gate. V1 remains an immutable pre-score protocol failure.

Pre-outcome checks passed: focused pytest 8 tests / 4 subtests; full pytest 282
tests / 84 subtests; stdlib discovery 204 tests; `compileall`; and
`git diff --check`. The focused suite explicitly exercises the end-to-end
degenerate stable schema and verifies that unrelated detector errors propagate.

- Protocol SHA-256: `6d1aa7eb867618709b1a049c1df55444535bbb3564107c9f4a9a1104b44f7047`.
- Benchmark SHA-256: `3222e0c7d89501f80bcd3ef2bb91271de3067a18344a3aa50164594aba010e68`.
- Declaration-test SHA-256: `630dcf06198744b2d44c20cf1ad7a57befe3c474c93a5046ed17f184e3f4efe5`.
- Command SHA-256: `f901c1f2f33825b0b580b87d036c98f0446e90142c597444177e1a8620520dcc`.
- Serialized initial-state SHA-256: Mackey--Glass
  `08423c1ee488176f64566989e4dddd157093b0294c16e0c906f1cbd23bacaa11`;
  Lorenz--96 `63428b686126b3604fb06f29bc662d83b3a09e864a46e277b8c7343749b01947`.
- Shuffle seeds: 842021 and 842022; dynamics have no random seed.
- Decisive command: exactly `bash command.sh` from this directory.

At freeze time neither `run()` nor the decisive command had been executed at
the corrective commit. This can establish only bounded finite-protocol
discrimination, never chaos proof, attractor/source-law identification,
CLA/compression validation, or semantic grammar. No tuning or rescoring of
these fixtures is permitted. Stage B remains prohibited unless the complete
gate passes and a distinct Stage-B protocol is later frozen.

## Execution result

The exact decisive command was executed once on 2026-07-20 at approximately
18:18 PDT and exited 0 after about 77 seconds. Both positives were promoted:
Mackey--Glass slope 0.019656759765072553 and full-state Lorenz--96 slope
0.013052857377956398. Mackey--Glass stable was explicitly reported degenerate
with zero pairs/null slope and not promoted. Mackey--Glass shuffled
(-0.00016819136492626706), Lorenz--96 stable (-0.0002188829856632411), and
Lorenz--96 shuffled (-0.000052087819800855637) were not promoted. The exact
six-fixture rule therefore passed. `stage_b_authorized` remained false.

The command's JSON was transcribed without numeric changes into `results.json`
(SHA-256 `efbd2dea2edb086be3a1a33b61f99a090dfcca0c5f2800cb5e55c4296691e30f`).
This is the first passed bounded Stage-A detector calibration in this lane, not
chaos proof and not CLA/compression, attractor, source-law, or semantic-grammar
evidence. No v2 tuning or rescoring is allowed.
