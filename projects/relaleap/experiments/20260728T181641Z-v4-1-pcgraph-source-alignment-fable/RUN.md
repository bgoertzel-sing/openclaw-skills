# V4-1 PCStep alignment with Mesto's public pcgraph

- Status: COMPLETE (bounded XOR source alignment; not GPT-2 production)
- Created (UTC): 2026-07-28T18:16:41Z
- Project: RelaLeap
- Source repository: `../../repos/metta-on-mork/`
- Source commit: `45a0b51dce76fd8d620984e812317f6ed3a01204`
- Source licence: GPL-2.0-or-later; preserve attribution and avoid unmarked
  source copying
- Prior synthetic scaffold:
  `../20260728T181111Z-v4-1-clean-room-pcstep-fable/`

## Question

Can the synthetic pure-state PCStep seam be aligned to the executable
one-tick settlement and local-update semantics in Mesto's public
`demos/pcgraph` code and checked oracle artifacts, while keeping the
commutator-critic state/gate boundary explicit?

## Acceptance

1. Map `pcgraph` state cells, signs, error variables, settlement, and local
   update into the adapter contract with source locations.
2. Match the public one-tick reference and local update within its stated fp32
   tolerance.
3. Preserve the frozen-weight settlement assertion and exact deterministic
   state snapshot/restore.
4. Keep licence/provenance boundaries explicit.
5. List the precise remaining gap between `pcgraph` and the claimed GPT-2
   homotopy production substrate.
6. Focused tests and scoped `git diff --check` pass.

## Result

Implemented `work/pcgraph_adapter.py`, a pure fp32 adapter around the pinned
pcgraph jpc-native XOR semantics. It maps public state/error/gradient cells,
executes frozen-weight settle ticks, applies the m1 local outer-product update
after settlement, and exposes a comcrit-compatible module gate immediately
before the additive fold. Canonical snapshots cover weights, outer-step state,
RNG, batch plan, settled errors, and named cells.

Five tests passed: one tick and one 16-tick m1 local update agree with
`xor_jpc_reference.npz`; settlement is frozen and the step pure; snapshot,
restore, and continuation are byte-exact; invalid gates/plans fail closed.
Tolerance (`rtol=2.4e-6`, `atol=6e-8`) conservatively covers the largest fp32
discrepancies reported in `oracle/jpc_report.json`.

Attempt 2 exited 0 in 0.174110 seconds. Attempt 1 is preserved and exited 1:
it compared the m1 training update (which uses `x_train[0]`) against the
separate `x_single` settle fixture. The corrected test explicitly distinguishes
those checked artifact inputs.

## Source and environment

- Remote/commit: `https://github.com/MesTTo/metta-on-mork.git`,
  `45a0b51dce76fd8d620984e812317f6ed3a01204` (`main`)
- Source worktree: clean before and after; no source edits
- Licence: GPL-2.0-or-later; equations are attributed and independently
  structured in `work/SOURCE_ALIGNMENT.md`; tests load the NPZ in place
- Runtime: Python 3.10.12, NumPy 2.2.6,
  Linux 7.0.11-76070011-generic x86_64
- Remote resources/external writes: none
- Relevant research rules: 0, 2, 5, 6, and 10

## Frozen command and evidence

`command.sh` was frozen before attempt 1 and unchanged between attempts. It
runs unittest discovery, `py_compile`, scoped `git diff --no-index --check`,
and a narrow credential-pattern scan. Successful raw evidence is in
`stdout.txt`, `stderr.txt`, `exit_status.txt`, and `wall_seconds.txt`; the
failed run is in the corresponding `*.attempt1.txt` files. Environment and
artifact hashes are recorded in `environment.txt` and `sha256.txt`.

## Interpretation and limitations

This establishes only the public fixed 2-2-2 XOR seam. Repository inspection
found no executable GPT-2 homotopy trainer; trained PC GPT-2 model,
optimizer/RNG/batch-plan checkpoints; production config/model manifest;
tokenizer/data pipeline; homotopy/settlement schedule; transformer
attention/MLP/layer-norm local-update implementation; or training telemetry.
The verified MORK binary is described as an ignored external build, not a
checked artifact. No GPT-2 reproduction, checkpoint compatibility,
transformer-scale result, exact-D admission, or C4-prime production claim
follows. Precise adapted-versus-invented boundaries and source locations are
in `work/SOURCE_ALIGNMENT.md`.
