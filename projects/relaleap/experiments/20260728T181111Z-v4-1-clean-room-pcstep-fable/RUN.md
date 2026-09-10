# V4-1 clean-room PCStep adapter — Fable design

- Status: COMPLETE (synthetic clean-room prototype only)
- Created (UTC): 2026-07-28T18:11:11Z
- Project: RelaLeap
- Question: Can a minimal, testable `T=1` PC--GPT-2 settlement/update adapter
  be constructed clean-room from the supplied paper and integrated with the V4
  causal-critic seam without pretending to reproduce unavailable production
  code or checkpoints?
- Source:
  `../../../../library/mesto-homotopy-pc-gpt2-2026/report-2026-07-26.pdf`
- Companion specification:
  `../../../../library/commutator-critic-c4prime-2026/c4prime_implications.pdf`
- Existing V4 seam:
  `../../../omegaclaw/workspace/relaleap-v4/comcrit/comcrit/`

## Frozen scope

Implement only a deterministic synthetic `T=1` adapter and its state
boundaries. Preserve the distinction between paper-derived assumptions,
invented engineering choices, and observed test results. Do not claim
production-checkpoint compatibility, exact reproduction of Mesto's
implementation, transformer-scale validity, policy efficacy, or C4-prime
admission. No remote compute or external writes.

## Acceptance

1. Pure `(theta, optimizer_state, batch, t, gate) -> state` interface.
2. Runtime assertion that parameters do not change during settlement.
3. Exact deterministic snapshot/restore on the synthetic fixture.
4. `T=1` behavior matches an independently expressed reference update.
5. Assumptions and deviations are explicit and reviewable.
6. Focused tests and `git diff --check` pass.

## Result

Implemented a two-layer float64 synthetic `T=1` PCStep with:

- the pure conceptual boundary
  `pc_step(theta, optimizer_state, batch, t, gate) -> StepState`;
- separately named settlement and local-gradient phases, with a runtime
  pre/post weight digest assertion around settlement;
- gated per-layer local gradients and a pure AdamW-style state transition;
- explicit RNG and batch-plan state;
- canonical byte snapshots and exact restore/replay;
- an independently spelled analytic reference update.

The paper-derived assumptions, invented choices, and exclusions are frozen in
`work/ASSUMPTIONS.md`. The adapter mirrors comcrit's R3 module-gradient gate
conceptually but does not import or modify comcrit.

## Execution

Frozen command in `command.sh`:

```bash
python3 -m unittest discover -s work/tests -p 'test_*.py' -v
```

The ledger runner invoked it as `bash command.sh` and captured:

- final exit status: `0` (`exit_status.txt`);
- tests: `5`, all passed (`stderr.txt`; unittest writes verbose output there);
- wall time: `0.12` seconds (`wall_seconds.txt`);
- stdout: empty (`stdout.txt`);
- environment: Python 3.10.12, NumPy 2.2.6, Linux
  7.0.11-76070011-generic x86_64 (`environment.txt`);
- artifact hashes: `sha256.txt`.

`python3 -m py_compile work/pcstep.py work/tests/test_pcstep.py` and scoped
`git diff --check` also passed.

## Attempt history

The initial ledger wrapper tried `./command.sh`, which did not execute because
the pre-existing file mode was not executable (exit 126). That evidence is
preserved as `*.attempt1.txt`. The first actual test execution
(`bash command.sh`) exited 1: three tests passed, one test assertion incorrectly
compared dataclasses containing NumPy arrays, and the independent oracle
differed by `2.07e-25` under different floating-point operation spelling.
That evidence is preserved as `*.attempt2.txt`. The tests were corrected to
compare unchanged arrays individually and allow only roundoff-scale oracle
agreement (`rtol=1e-15`, `atol=1e-18`); the final run passed.

## Interpretation and limitations

The acceptance conditions for the **synthetic clean-room fixture** passed.
This is not Mesto-code reproduction, production asset intake, checkpoint
compatibility, a deep-settle implementation, transformer-scale evidence,
exact Torch optimizer compatibility, exact-D validation, policy evidence, or
C4-prime admission. The required production checkpoints, implementation,
configuration, data identities, telemetry, and licence statement remain
absent, so the production V4-1 asset-intake contract remains unfulfilled.

## Post-completion upstream inspection

After the prototype passed, Ben relayed Mesto's statement that the relevant
implementation is in `https://github.com/MesTTo/metta-on-mork`. Inspection of
the public GPL repository at `main`
`45a0b51dce76fd8d620984e812317f6ed3a01204`, its `master` branch, and visible
history found genuine synthetic PC code under `demos/pcgraph`: a float32
`2-2-2` tanh XOR settle, NumPy/Torch oracles, MORK phase rules, committed
reference artifacts, and end-of-settle/update-every-tick local learning modes.

No committed PC--GPT-2 homotopy training implementation, AdamW state,
production checkpoint, configuration, data identity, or telemetry was found
in either visible branch or the historical object paths. The only
transformer-specific tree artifact is a July 23 report PDF, distinct from the
supplied July 26 report. Accordingly, production-code availability is now
**partially resolved, not presumed absent**: real toy ePC/MORK code is
available and reusable subject to GPL provenance, while the production
PC--GPT-2 substrate remains unidentified.

No upstream code was copied into this clean-room work. Detailed comparison:
`work/UPSTREAM_PROVENANCE.md`. Preserved source record:
`../../../../library/metta-on-mork-2026/SOURCE.md`.

The unchanged focused clean-room suite was rerun after the provenance update:
5 tests passed in 0.026 seconds, exit 0
(`post_inspection_stderr.txt`, `post_inspection_exit_status.txt`). Compilation
and scoped whitespace checks also passed. Updated hashes are in `sha256.txt`.

Relevant Research Rules: 1 (validate with a handwritten oracle), 2 (freeze the
plain-language assumptions/spec first), 5 (capture reproducible evidence), and
7 (keep the gate/state seam modular).
