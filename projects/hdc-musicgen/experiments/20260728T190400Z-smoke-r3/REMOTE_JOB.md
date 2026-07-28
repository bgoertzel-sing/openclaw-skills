# Remote Job: MusicGen smoke-r3

- Project/run: `hdc-musicgen` / `20260728T190400Z-smoke-r3`
- Status: `approved; pre-transfer`
- Owner approval: Ben, Telegram 2026-07-28.

## Authorized scope

- Provider/account: RunPod operator account verified by `runpodctl doctor`.
- Pod: `xgv04sy1g9a3q8`; one RTX 3090 (24 GB), `$0.50/hour`, official
  `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`, 50 GB container disk,
  ephemeral `/workspace`, SSH only; no persistent volume, endpoint, snapshot,
  or unrelated project use.
- Bound: Stage 0/S/A only; maximum 8 wall-clock hours or USD 5.00, whichever
  occurs first. Retrieve artifacts and terminate immediately after a gate
  failure or completion.
- Source: Git archive of `8907d0fcba2897be48d435f49f501661ab4d8f4b`; exclude
  `.git`, local virtual environments, and the pre-existing dirty file.
- Inputs: exactly the eight listed explicit-CC MP3 files from the prior
  verified corpus; no download and no other audio.
- Return: logs, JSON, selected-input hashes, environment record, and checksums
  to `artifacts/`, verify locally, then terminate the pod.

## Scientific boundary

This is the amended eight-track Stage 0/S/A smoke only. It applies the
support-aware NLL rule at commit `8907d0f`; it authorizes neither a full run,
Stage C/D, fine-tuning, nor retries beyond minimal runtime repair.
