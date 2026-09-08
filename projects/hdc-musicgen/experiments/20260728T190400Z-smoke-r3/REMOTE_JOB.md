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

## Completion (2026-07-28 16:44 PDT)

- Two setup failures repaired in-band: PyAV needed `pkg-config`+ffmpeg dev libs (apt); `audiocraft==1.3.0` pins `torch==2.1.0`/`xformers<0.0.23` which are unavailable/incompatible on py3.12 — resolved with `pip install --no-deps audiocraft==1.3.0` plus explicit deps (av, einops, flashy, hydra-core, hydra_colorlog, julius, num2words, sentencepiece, spacy, demucs, librosa, torchmetrics, transformers==4.46.3, xformers==0.0.28.post3) against torch 2.5.1+cu121.
- Run completed exit 0 at 23:41 UTC. All 7 results-file hashes in SHA256SUMS verified locally (audio hashes recorded against manifest, not re-downloaded).
- Results: Stage0 smoke_mode (8 tracks/24 min; full gate needs 20/60 — expected fail-closed). Stage S gate PASS (separation 0.4921; related mean 0.986 vs unrelated 0.494). Stage A gate PASS (related relevance_gain 0.0542; unrelated stratum support insufficient, n=1).
- Pod `xgv04sy1g9a3q8` terminated 2026-07-28 16:44 PDT (`deleted: true`; pod list confirms only RelaLeap pod remains). Estimated spend: ~5.2h × $0.50 ≈ $2.60 (cap $5).
- Artifacts: `artifacts/remote-sync/` (run.log, RESULTS.md, SHA256SUMS, stage JSONs, codes.pt, environment.txt, exit_status).
