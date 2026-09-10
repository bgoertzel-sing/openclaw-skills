# Remote job: clean-room transformer ePC multi-step comparison

- Project/run: `relaleap` / `20260728T204354Z-clean-room-transformer-epc-multistep`
- Status: completed, retrieved, verified, and terminated.
- Approval: Ben, Telegram, 2026-07-28, for the frozen three-seed grid after
  local preflight; hard cap USD 5 / eight hours. The binding time guard at the
  observed USD 0.69/h price is seven hours 14 minutes.
- Provider/account: RunPod account verified by `runpodctl doctor`.
- Resource: pod `hzv1q665pe5qf3` (`combined_bronze_impala`), one RTX 4090
  (24,564 MiB observed), 16 vCPU, 50 GB container disk, no persistent volume;
  image `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`, Ubuntu 24.04.
- Price source: `runpodctl pod get` at 2026-07-28T20:44Z: USD 0.69/hour.
- Transfer plan: archive only source commit `6f8cc21f71e09eeb04a60a935c3a4be33abdd839`.
  The pod may download the pinned public GPT-2 revision and public WikiText-103
  revision named in `configs/clean_room_epc_multistep_v1.json`. No credentials,
  private keys, OpenClaw state, or local datasets are transferred.
- Execution: one named tmux session, `relaleap-cleanroom-epc-multistep`, runs
  the frozen three-seed launcher. Stop on any non-finite metric, frozen-settle
  invariant failure, or non-identical replay.
- Artifact return: retrieve seed JSONs, summary, logs, source archive hash,
  and GPU report to this experiment directory; verify returned SHA-256 and
  required JSON invariants locally.
- Cleanup: after retrieval/verification terminate (not merely stop) the pod.

## Completion evidence (2026-07-29 UTC)

- All three returned seed records (`1729`, `3253`, `6421`) have
  `status=passed`, `replay_exact=true`, finite objectives, and finite held-out
  KD gains. The summary reports `status=completed`, exact replays, and mean
  held-out KD gain `6.588154157002767` nats.
- Returned local SHA-256 values exactly match the pod for all three seed JSONs,
  `summary.json`, and `grid.log`; see `artifacts/`.
- `runpodctl pod delete hzv1q665pe5qf3` returned `deleted: true`; the
  immediately subsequent account pod list was empty.
