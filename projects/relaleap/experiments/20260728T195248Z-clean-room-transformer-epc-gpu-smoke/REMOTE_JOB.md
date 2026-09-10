# Remote job: clean-room transformer ePC GPU smoke

- Project/run: `relaleap` / `20260728T195248Z-clean-room-transformer-epc-gpu-smoke`
- Status: completed and terminated.
- Approval: Ben, Telegram, 2026-07-28: separate RelaLeap pod and hard cap of
  8 hours / USD 5.
- Provider/account: RunPod account verified by `runpodctl doctor` as Ben's
  account (only account identity verified; no credential recorded here).
- Resource: pod `i59hyjg2qoglex` (`urban_brown_owl`), one RTX 4090 (24,564
  MiB observed), 16 vCPU, 50 GB container disk, no volume. Image:
  `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`; Ubuntu 24.04 observed.
- Price: USD 0.69/hour, reported by `runpodctl pod get` at 2026-07-28T19:52Z.
  Eight hours would be USD 5.52, so the binding financial guard is USD 5;
  terminate by 7h 14m after pod creation, and earlier if smoke completes.
- Network/data: SSH only. Upload a git archive at commit `19e1022` plus this
  run command; the smoke downloads only pinned public Hugging Face GPT-2
  revision `607a30d783dfa663caf39e06633721c8d4cfcd7e`. No local datasets,
  credentials, private keys, OpenClaw state, or RelaLeap-unrelated material.
- Execution: named tmux session `relaleap-cleanroom-epc-smoke`; install only
  pinned Transformers stack needed by the smoke, execute one T=1 six-layer
  student / frozen GPT-2 teacher step and exact snapshot/replay check.
- Stop/termination: retrieve JSON, log, package hash, and GPU report; verify
  the JSON status/replay/frozen-weight invariants locally; terminate pod after
  artifacts are retrieved. A stopped pod is not adequate because it can retain
  billable resources.

## Completion

- Started: 2026-07-28T20:00:27Z (first environment attempt); successful retry
  started 2026-07-28T20:06:17Z.
- Result: `gpu_smoke.json` reports `status=passed`, one T=1 objective of
  `42.68228530883789`, frozen settlement, and byte-identical replay. The
  six-layer student has 81,322,752 parameters; teacher has 124,439,808;
  observed peak CUDA allocation was 3,141,838,848 bytes.
- Environment deviation: the selected image provided Torch `2.8.0+cu128`;
  the isolated environment used that image Torch and pinned Transformers
  `4.44.2` rather than installing the old `torch==2.4.0` pilot lock. This is
  an engineering smoke only, not a frozen pilot outcome.
- Artifact return: remote/local SHA-256 matched for `gpu_smoke.json`
  (`b8e699e2196c16b55de640468e822624ec5c10fd0f8f36c7850f108f514d7011`)
  and `run.retry1.log`
  (`0a11bec2ee3f234f04f72e35cca264a9d0a7d5a2e371aa5e5134b7d7a7ed10b5`).
- Cleanup: `runpodctl pod delete i59hyjg2qoglex` returned `deleted: true`;
  subsequent `pod get` returned 404, observed at 2026-07-28T20:08Z.
