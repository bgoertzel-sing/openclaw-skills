# Source: MesTTo/metta-on-mork

- Type: public Git repository
- Author/organization: MesTTo / Ahmad Mesto
- Canonical URL: `https://github.com/MesTTo/metta-on-mork`
- Retrieved: 2026-07-28
- Local preservation: `repo/`
- Default branch: `main`
- Pinned commit: `45a0b51dce76fd8d620984e812317f6ed3a01204`
- Other visible branch: `master` at
  `f1094e47590f49ea0399601fecf2fd51356257c7`
- Default-tree listing SHA-256:
  `830b6a369cfac568bc257322b350079e3e1508f4b4dbd67a0e333fc0aeeab712`
- License: repository metadata says GPL-2.0; `Cargo.toml` says
  GPL-2.0-or-later; inspect per-file history/notices before redistribution
- Privacy tier: public
- Tags: `MORK`, `MeTTa`, `predictive coding`, `ePC`, `GPT-2`, `RelaLeap`
- Related project: `relaleap`

## Inspection result

The repository contains reusable actual predictive-coding code, but the
committed implementation found at the pinned revision is a synthetic
`2-2-2` tanh XOR demonstrator, not the reported production PC--GPT-2
homotopy implementation.

Actual committed code includes:

- `demos/pcgraph/oracle/common.py`: NumPy float32 ePC settle, separate
  `jpc-native` and paper-error modes, local outer-product weight updates, and
  deterministic fixture constants;
- `demos/pcgraph/oracle/epc_ref.py`: a Torch oracle for the toy settle and
  weight updates;
- `demos/pcgraph/driver.py`, `derive_rules.py`, and `rules/xor_tick.mm2`:
  MORK execution of the toy settle and two local-update schedules;
- committed NPZ/JSON oracle artifacts and a cell-by-cell checker.

The repository's own documentation scopes this to a fixed `2-2-2` XOR chain,
`K=16`, squared loss, and float32 (`demos/pcgraph/README.md`, lines 5--11).
It distinguishes end-of-settle ePC (`m1`) from update-every-tick iPC (`m2`)
(lines 29--34). The code uses direct local learning-rate folds, not AdamW.

The README links the transformer programme and claims an in-store GPT-2
forward result, but the default tree and both visible branch trees contain no
committed GPT-2 model/training code, homotopy scheduler, AdamW optimizer state,
production checkpoints, tokenizer/data plan, or production settle telemetry.
The only transformer-specific file in the tree is the July 23 technical-report
PDF. Its SHA-256 is
`b7ce36a4327278bde1935669b309030f3f4ae4ae1fc95b4d259ec0f906a8ff35`;
it differs from the separately supplied July 26 PDF.

The complete visible Git object-path and `-S` history search found no deleted
GPT-2/homotopy code. `main` is 67 commits ahead of `master`; `master` contains
none of the pcgraph or transformer-report paths.

## Relevance and reuse boundary

The pcgraph implementation is a real upstream reference that could support a
separate, licence-aware synthetic adapter or MORK integration test. It is not
a drop-in source for the V4-1 production `PCStepAdapter`: its topology, error
semantics, optimizer, dtype, settle depth, state boundary, and artifact format
differ. No upstream code was copied into the clean-room experiment.

Further production-asset intake should ask Mesto for the exact branch/path or
commit containing the GPT-2 settle/local-update implementation and the
checkpoint/config/data/telemetry bundle. The repository URL alone does not
identify those assets in the visible history as of the pinned revision.
