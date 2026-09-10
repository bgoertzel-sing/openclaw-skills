# RelaLeap GPT-2-small ePC resumed pilot — remote job record

- Status: `superseded; subsequent r2 aborted on source/protocol drift`
- Provider/account: RunPod / Ben Goertzel account (`runpodctl doctor` passed)
- Purpose: execute the unchanged frozen GPT-2-small ePC pilot at the corrected
  local runner commit, after the prior retry chain was retired without an
  accepted scientific result.

## Authorization and bound

Ben explicitly directed: “Please resume it now!” in the Protobots Telegram
group. This authorizes this replacement job only.

- GPU: one secure-cloud A100 SXM 80 GB in CA-MTL-4. The initial EU-SE-1 volume
  request was rejected before resource creation because that region does not
  support network volumes; CA-MTL-4 is in RunPod's returned supported-region
  list. CA-MTL-4 then rejected the A100 SXM allocation before creating a pod;
  one same-region secure A100 PCIe 80 GB fallback is authorized because it
  preserves the 80 GB resource class, image, storage, deadline, and cap. No
  further fallback GPU, second pod, or retry is authorized by this record.
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04@sha256:61a4aafb0094cd773f11eefa378929d5a687bd775febeb78eac62fc824141fb5`
  (Docker Registry manifest digest checked 2026-07-17T04:46Z).
- Storage: a new 80 GB network volume mounted at `/workspace`; no unrelated
  existing volume may be attached or modified.
- Runtime/cost bound: provider-side automatic termination at
  `2026-07-17T10:46:53Z`; do not continue if the allocated rate exceeds
  USD 1.39/hour. The GPU cap is USD 8.34 at that ceiling; the total target cap,
  including storage, is USD 10.
- Upload/privacy: clean archive of public research code only. The model,
  tokenizer, and WikiText-103 data are pinned public artifacts. No credentials
  or private research data are uploaded.

## Pinned scientific inputs

- Source commit: `d400c15353c99c8882cd5f948526f6bb328103ab`
- Source worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Frozen protocol: `configs/gpt2_small_epc_pilot.json`, SHA-256
  `ba89ac189a5e8635806157794f4d66c87b2ca6d011ead39dd3505a98b9a473ab`
- GPU dependency lock SHA-256:
  `62a560ea55bcab9c3917f08ac1c143f90d600b85d72b327f1bf0e1981dd46374`
- Launch script SHA-256:
  `a46456ef2724fa149001d56ef8608bddba63fc1d77446255d404f462d616084e`
- Frozen primary arms: `bp_ce`, update-matched `bp_kd`, `epc_kd`, then
  wall-clock-matched `bp_kd`; seeds `1729,3253,6421`.

## Execution and stop conditions

1. Create the dedicated volume, then one pod with the automatic termination
   deadline; capture the returned pod ID, region, GPU, and actual rate.
2. Reject and immediately delete the pod if it differs from the specified GPU,
   image, region, or rate ceiling.
3. Transfer a `git archive` from the pinned commit; run hash/model/data/GPU
   preflight before scientific execution.
4. Run one GPU smoke update and project the full duration. Stop and retrieve
   diagnostics if the full run cannot finish within the bound.
5. Write each completed arm immediately to the network volume. Pull and hash
   those artifacts locally after each completed seed.
6. Stop immediately on source/protocol/data hash mismatch, non-finite metrics,
   non-monotone activity energy, OOM, failed retrieval, or cap breach.
7. Retrieve and verify all artifacts, terminate the pod, delete the dedicated
   volume, and verify both are absent before any result interpretation.

No previous partial output is eligible evidence. The job remains implementation
and pilot evidence unless the frozen evaluator and every invariant pass.

## Allocation outcome

- `2026-07-17T04:49Z`: RunPod created dedicated volume `2ergq54df4` in
  CA-MTL-4. The requested secure A100 SXM allocation was rejected as out of
  stock before a pod was created.
- The one allowed same-region secure A100 PCIe fallback was also rejected as
  out of stock before a pod was created.
- The dedicated volume was deleted immediately. Final provider check must show
  no RelaLeap pod or volume; unrelated pre-existing resources are untouched.
- No GPU time, code transfer, public-data download, or scientific run occurred.
  A further attempt needs a new provider/region/resource decision and a fresh
  bounded record.
- A later controller path provisioned a Community Cloud A100 r2 attempt outside
  this record's allocation outcome. Heartbeat terminated it after retrieved
  artifacts self-reported the wrong source commit and protocol hash. Evidence:
  `../20260717T045700Z-gpt2-small-r2/RUN.md`.
