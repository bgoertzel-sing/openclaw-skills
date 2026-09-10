# pcgraph source-alignment boundary

## Provenance and licence

The observed source is `metta-on-mork` commit
`45a0b51dce76fd8d620984e812317f6ed3a01204`, licensed GPL-2.0-or-later.
`pcgraph_adapter.py` is a small, independently structured Python translation
for validation, with this explicit attribution. It does not copy source text,
rules, comments, or artifacts. Tests read the checked NPZ in place; they do
not redistribute it.

## Adapted semantics

- `README.md:5-11` selects jpc-native ePC (hidden and output errors) as the
  primary path and distinguishes it from the paper-error and iPC variants.
- `oracle/common.py:14-24` supplies fp32 hyperparameters (`K=16`,
  error LR `.1`, local LR `.01`); lines 112-141 and 186-206 define the tick.
- State mapping: `pcw` -> `Weights`; `pcin x/y` -> `Batch.x/y`; `pce h/y` ->
  `SettleState.e_h/e_y`; `pcs h/y`, `pcb h`, and `pcg h/y` -> named
  `SettleState.cells`. Public schemas are documented at `README.md:13-27`.
- Signs are source-exact: hidden state is `pre_h + e_h`; output state is
  `pre_y - e_y`; output residual/gradient cell is `target - pcs_y`; error
  cells advance as `e - error_lr * pcg`. See `oracle/common.py:194-205` and
  `rules/xor_tick.mm2:106-210,252-288`.
- m1 is one outer update (`t=1`) after 16 frozen-weight settle ticks. Its
  `d_wxh = e_h_after.T @ x`, `d_why = residual.T @ phi_h`, and additive
  LR-scaled fold are defined at `oracle/common.py:244-259,261-276` and
  summarized at `README.md:29-34`. The checked oracle is
  `oracle/xor_jpc_reference.npz`; its `local_m1_after_one_*` record uses the
  first `x_train/y_train` row, while `settle_*` uses the separate `x_single`.
- The tolerance is taken conservatively from `oracle/jpc_report.json`:
  maximum reported fp32 relative discrepancy `2.3404048666378795e-06` and
  maximum absolute discrepancy `5.960464477539063e-08`.

## Invented adapter mechanics

The immutable dataclasses, pure R3 signature, `xh`/`hy` scalar module gates,
batch-plan cursor, deliberate one-draw RNG transition, canonical JSON snapshot,
and exact restore/replay protocol are adapter mechanics. They are not pcgraph
claims. pcgraph's local m1 update is a direct additive fold, not AdamW, so the
prior synthetic AdamW moments were intentionally removed. The gate multiplies
each local delta immediately before that fold; gate=1 is the source-equivalent
path. `t` counts outer local updates, while inner settlement uses `settle_ticks`.

## Missing GPT-2 homotopy production substrate

The pinned tree contains the technical-report PDF and README claims about a
12-layer GPT-2/store forward, but observed executable pcgraph assets are only
the fixed 2-2-2 XOR demo. Repository-wide filename/content inspection found no
GPT-2 trainer or homotopy-training program, no trained PC GPT-2 checkpoints or
optimizer/RNG/batch-plan checkpoint state, no production model/config manifest,
no tokenizer or training/evaluation dataset pipeline, no schedule/config for
homotopy coefficients and layerwise settlement, no attention/MLP/layer-norm
local-update adapter, and no training telemetry/seed/run ledger. The MORK
binary/config used for the verified pcgraph run is also not checked in:
`README.md:67-78` describes an external build and ignored copied binary.

Therefore this artifact validates only the public XOR numerical seam. It
cannot run or audit GPT-2 homotopy training, restore its states, or establish
checkpoint compatibility or C4-prime production admission.
