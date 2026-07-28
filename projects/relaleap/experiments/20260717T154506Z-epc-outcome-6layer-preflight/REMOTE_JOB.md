# RelaLeap six-layer ePC outcome gate — approval request

- Status: `fresh expanded-region approval consumed; stalled pod terminated`
- Outcome: The initial scoped region attempts failed for lack of capacity.
  Ben then explicitly approved expanded regions at 2026-07-17 21:26 UTC.
  Pod `lop52u56xugpxk` allocated within the remaining GPU/rate/image/storage
  bounds but never became ready (`uptimeSeconds: 0`, no SSH) and was terminated
  after about 52 minutes. No transfer, GPU runtime, scientific execution, or
  job-created volume occurred. See
  `../20260717T155300Z-epc-outcome-6layer-run1/RUN.md`.
- Provider/account: RunPod / configured Ben Goertzel account (`runpodctl doctor`
  passed 2026-07-17)
- Purpose: train fresh matched six-layer GPT-2-width BP+CE, BP+KD, and ePC+KD
  students, preserve every checkpoint, then run the frozen structural and
  WikiText-103 to TinyStories adaptation/forgetting battery.

## Requested resource and cost bound

- GPU: one Community Cloud NVIDIA A100 PCIe 80 GB.
- Regions: try `CA-MTL-3`; if unavailable, one allocation attempt in
  `EU-RO-1`. No other GPU, region, second simultaneous pod, or retry chain.
- Live price checked 2026-07-17: USD 1.19/hour; reject any allocation above
  this rate.
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` pinned to
  registry digest
  `sha256:61a4aafb0094cd773f11eefa378929d5a687bd775febeb78eac62fc824141fb5`.
- Storage: 80 GB ephemeral container storage; no network volume and no existing
  user volume may be attached or modified.
- Expected duration: 3.5 hours, based on the prior one-seed forensic timing
  (~50 minutes for all four training controls) plus three-seed probe overhead.
- Hard termination: 5 hours after provisioning. Expected GPU charge USD 4.17;
  maximum GPU charge USD 5.95. Total job cap USD 7.00 including incidental
  ephemeral storage charges.

## Frozen scientific and source inputs

- Clean source commit:
  `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`.
- Source transfer: a `git archive` of exactly that commit, with a separate
  `SOURCE_COMMIT` marker; no working-tree copy.
- Distillation protocol: `configs/gpt2_small_epc_pilot.json`, SHA-256
  `ba89ac189a5e8635806157794f4d66c87b2ca6d011ead39dd3505a98b9a473ab`.
- Outcome protocol: `configs/gpt2_epc_outcome_6layer.json`, SHA-256
  `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`.
- Dependency lock: `requirements-gpu.lock.txt`, SHA-256
  `62a560ea55bcab9c3917f08ac1c143f90d600b85d72b327f1bf0e1981dd46374`.
- Training runner SHA-256:
  `0add268dc78381503aca24702aef46820920b19c2a35e355ee9bb293bca9c7e0`.
- Outcome runner SHA-256:
  `68e7c67350aec0042a06f6facc11f3a59c45b1d022f71fe8dfe15a990a7b3ef3`.
- Public inputs only: pinned GPT-2 model/tokenizer, WikiText-103 source, and
  TinyStories target at revision
  `f54c09fd23315a6f9c86f9dc80f725de7d8f9c64`.

## Execution, transfer, and termination contract

1. Allocate at most one pod with provider-side five-hour termination, verify
   GPU, rate, image digest, region, storage, and empty resource state.
2. Upload only the clean source archive and frozen public-data specifications.
   No credentials, private data, unrelated files, or full workspace transfer.
3. Install the pinned lock, cache and hash the public artifacts, then enable
   offline mode for both scientific runners.
4. Verify the source marker and both config hashes before a one-update GPU
   smoke. Abort if the smoke or projected runtime cannot fit the cap.
5. Execute the three frozen seeds and four matched training records per seed;
   checkpoint every BP/KD/ePC arm with safetensors plus SHA-256 manifest.
6. Run the frozen common low-rank adaptation battery and two-level paired
   seed/segment bootstrap. Do not change seeds, horizons, domains, thresholds,
   or adaptation settings after observing output.
7. Pull metrics, logs, environment record, source/config hashes, and all nine
   final checkpoints to
   `projects/relaleap/experiments/<remote-run-id>/artifacts/`; verify hashes.
8. Terminate (not merely stop) the pod after successful retrieval or any hard
   stop. Termination deletes ephemeral storage; stopping would retain a
   billable resource and is not permitted. Verify no job-created pod or volume
   remains.

Immediate hard stops: source/config/image/data drift; unexpected existing
output; missing arm/checkpoint; non-finite metric; non-monotone ePC energy;
OOM; failed artifact retrieval; price/cost/time breach; or any unapproved
fallback. A stopped/failed job yields implementation diagnostics only and does
not authorize another allocation.
