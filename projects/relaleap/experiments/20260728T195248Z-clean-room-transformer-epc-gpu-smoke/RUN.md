# Run 20260728T195248Z: clean-room transformer ePC GPU smoke

- Status: succeeded; remote pod terminated
- Question: does `clean_room_transformer_epc_v1` execute one source-pinned,
  six-layer GPT-2 student / frozen GPT-2 teacher T=1 step on the approved RTX
  4090 while preserving frozen settlement and byte-identical replay?
- Source: `agent/v4-gpt2-pcstep` at `19e1022`, plus the uncommitted smoke
  launcher recorded in this directory before execution.
- Acceptance: remote JSON records `status=passed`, `settlement_frozen=true`,
  `replay_exact=true`, six student layers, and finite objective/memory values.
- Interpretation boundary: engineering smoke only; the update is global
  autograd/AdamW after settlement, not a reproduction of unpublished Mesto
  transformer-local rules and not a training-efficacy result.
- Exact command: `command.sh` after transfer to the pinned source archive.
- Remote record: `REMOTE_JOB.md`.

## Results

**Observed:** the approved RTX 4090 executed the one-step smoke using a
six-layer, GPT-2-width 81,322,752-parameter student and a frozen
124,439,808-parameter GPT-2 teacher. The T=1 objective was `42.68228530883789`;
peak CUDA allocation was 3,141,838,848 bytes. The emitted JSON reports
`settlement_frozen=true` and `replay_exact=true`. Remote and returned hashes
match; see `artifacts/gpu_smoke.json` and `artifacts/run.retry1.log`.

**Interpretation:** this reproduces the local engineering invariants on the
approved GPU and establishes that the stated 24 GB VRAM configuration has
substantial headroom for this one-step configuration. It does not test a
training trajectory, compare ePC with KD, or establish Mesto compatibility.

**Environment note:** the selected image supplied Torch `2.8.0+cu128`; the
smoke pinned Transformers `4.44.2` but deliberately used image Torch rather
than altering the image to the legacy pilot's Torch 2.4 lock. Therefore it is
not a frozen-protocol efficacy run.

**Cleanup:** artifacts were retrieved and verified, then RunPod pod
`i59hyjg2qoglex` was terminated. `runpodctl pod get` returned 404 after
deletion.
