# runpod-pilot-001 — HDPC Tiny Shakespeare LoRA T={1,2}

## Status

Draft only. No paid resource started.

## Goal

Run the first bounded GPU pilot for HDPC/ePC homotopy distillation on Tiny Shakespeare after local tests pass.

## Approval checklist to fill before launch

- Provider/account: Runpod, account verified by `runpodctl doctor` on 2026-07-09.
- Resource: TBD, likely one 24–48GB GPU (`RTX 4090`, `RTX A6000`, `L40S`, or comparable) depending on current price/availability.
- Region/datacenter: TBD from availability.
- Image/template: TBD; should include CUDA/PyTorch or use a pinned container.
- Storage/network: minimal persistent volume only if needed; no public service exposure.
- Current price source: TBD immediately before approval.
- Expected duration: TBD after local benchmark; initial target should be a short pilot, not full annealing.
- Maximum cost/time cap: TBD; must be explicitly approved.
- Data: Tiny Shakespeare public corpus only; code and configs only, no secrets or unrelated local files.
- Transfer plan: rsync/git clone a clean repo checkout plus config; do not upload `.openclaw`, SSH private keys, tokens, or unrelated files.
- Stop/terminate behavior: terminate pod after artifacts are retrieved and verified unless Ben approves retaining storage.
- Artifact path: `projects/hdpc-tiny-shakespeare/artifacts/runpod-pilot-001/`.

## Required preconditions

- Local tests T1-T7 implemented and passing where applicable.
- Run script captures commit hash, environment, exact commands, logs, metrics, and exit status.
