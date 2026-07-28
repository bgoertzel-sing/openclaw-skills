# Run 20260728T201400Z: clean-room transformer ePC multi-step preflight

- Project: `relaleap`
- Status: succeeded locally; no GPU resource started.
- Source: `agent/v4-gpt2-pcstep` commit `6f8cc21f71e09eeb04a60a935c3a4be33abdd839`.

## Question

Can the clean-room GPT-2 PCStep seam execute a fixed multi-update comparison
from identical model/optimizer/RNG state and batch plans, while retaining
exact replay as a hard invariant?

## Frozen experiment contract

`configs/clean_room_epc_multistep_v1.json` specifies three seeds
(`1729, 3253, 6421`), 100 updates, a 64-token batch, the T=1 KD endpoint and
four-settle-step ePC-KD arms, and 16 held-out public WikiText-103 batches.
`scripts/run_cleanroom_epc_multistep_grid.sh` is the sole launcher.

Each seed uses the same initial model/AdamW snapshot and deterministic token
stream for both arms. The settled arm is run a second time from its initial
snapshot and must have identical objective history and serialized final
snapshot. Non-finite objectives/KD, changed settle-time parameters, or a
replay mismatch terminate the run without an efficacy interpretation.

## Local verification

- `pytest -q tests/test_multistep.py tests/test_pcstep_adapter.py tests/test_gpt2_epc.py`: 12 passed.
- `PYTHONPATH=src:. pytest -q`: 156 passed in 15.85 seconds.
- `python3 -m py_compile ...`, `bash -n scripts/run_cleanroom_epc_multistep_grid.sh`, JSON contract validation, and `git diff --check` passed.

## Interpretation boundary

This runner compares a clean-room, KD-only T=1 endpoint to the same
settle-then-global-AdamW scheme at four activity steps. It may report a
three-seed descriptive held-out KD difference. It does not reproduce Mesto's
unpublished transformer-local rules, establish GPT-2 checkpoint compatibility,
or test the separately blocked C4-prime commutator deployment.

## Next step

Create a separate costed RunPod job only after Ben approves the exact resource
and cap. Archive only commit `6f8cc21`, download the pinned public GPT-2 and
WikiText revisions, run the fixed grid in tmux, retrieve all seed JSONs and
summary, verify hashes/invariants, then terminate the pod.
