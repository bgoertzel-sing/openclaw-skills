# Run 20260717T022106Z: GPT-2 post-attempt runner audit

- Project: `relaleap`
- Started: `2026-07-17T02:21:06Z`
- Finished: `2026-07-17T02:24Z`
- Status: `local validation passed; remote execution blocked`
- Local or remote: `local CPU tests only`
- Source commit: `d400c15353c99c8882cd5f948526f6bb328103ab`

## Question

Do the post-attempt runner changes preserve the frozen protocol and the
fail-closed matched-control/evaluation contract before another GPU request?

## Findings and changes

- Blocking defect: wall-clock-matched BP+KD used an elapsed-time stop check but
  its loop and data iterator were still capped at the frozen 1,000 updates.
  Since BP is expected to be faster than ePC, this could silently reduce the
  wall-clock control to the update-matched control.
- Corrected the wall-clock arm to consume a deterministic unbounded batch
  stream until the ePC elapsed budget, completing but not starting an update
  across the bound. Update-matched arms remain exactly 1,000 updates.
- Restored local-only model/tokenizer loading for scientific execution after
  the launch preflight downloads and verifies pinned hashes; the launch command
  sets Hugging Face Hub and Datasets offline modes.
- Added per-seed evaluation chunk indices and a canonical SHA-256 to every
  record. Expanded fail-closed checks to non-finite matched-control metrics,
  training loss, ePC activity energy, and final ePC objective.

## Verification

```text
PYTHONPATH=src python3 -m pytest -q tests/test_gpt2_epc.py tests/test_gpt2_pilot_gpu_runner.py
11 passed in 2.61s

PYTHONPATH=src python3 -m pytest -q
129 passed in 15.40s

bash -n launch_runpod.sh
python3 -m py_compile scripts/run_gpt2_pilot_gpu.py src/relaleap/hdpc/gpt2_adapter.py src/relaleap/hdpc/gpt2_epc.py
git diff --check
all passed
```

## Interpretation and gate

This is implementation and local validation evidence, not a GPU smoke or
promotion result. The prior explicit approval was consumed by the aborted
experiment `20260717T003032Z-gpt2-small-runpod-pilot`; it does not authorize
the corrected commit. No paid or remote compute was used in this audit. Before
another pod: prepare a replacement `REMOTE_JOB.md` with immutable image,
commit `d400c15`, fresh runtime/cost bounds and cleanup plan, present it to Ben,
and obtain explicit bounded approval.

## Cleanup exception discovered

At 2026-07-17 02:26 UTC, a read-only guardrail check found an additional live
out-of-contract pod: `jnjc7d7y80pxx5`, name `relaleap-gpt2-epc-try7`, image
`runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`, advertised rate
$1.39/hour, desired status `RUNNING`. It was deleted immediately and
`runpodctl pod list` returned `[]`. A stale local delayed SSH monitor process
for that pod was killed; a repeat provider/process check was empty. The pod and
any unverified outputs are not scientific evidence. Deletion is not reversible;
it was required to stop unauthorized spend under the retired job record.
