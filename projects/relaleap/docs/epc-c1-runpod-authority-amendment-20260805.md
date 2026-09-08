# C1 Runpod Authority Amendment — Available A40

Status: approved by Ben in Telegram at `2026-08-05T23:27:11Z`.

This amendment supersedes only the unavailable **US-West** location constraint
in `epc-c1-runpod-authority-proposal-20260805.md`.  All other frozen C1 scope,
input, artifact-return, stop, and cleanup conditions remain unchanged.

## Authorized resource

- Provider/account: existing Runpod Secure Cloud credential store.
- Resource: one NVIDIA A40, 48 GB, in `CA-MTL-1` (Canada).
- Image: the existing digest-bound Runpod PyTorch image.
- Storage/network: 50 GB disposable container disk; SSH and outbound HTTPS
  only; no endpoint, network volume, snapshot, or unrelated transfer.
- Price: observed Secure Cloud rate `$0.44/GPU-hour`.

## Bound

The existing expected 12 GPU-hour / `$5.28` target, 20-hour science stop, 24
hour hard termination, and `$12.00` all-in cap remain in force.  Terminate,
not merely stop, after return/verification or on any frozen stop condition.

## Provenance

Ben's instruction was: “for runpod for epc, just get any machine that works
and is available”.  The A40 in `CA-MTL-1` is chosen because it preserves the
already-reviewed 48 GB CUDA class and the original `$0.44/GPU-hour` cost
assumption while resolving the US-West capacity failure.
