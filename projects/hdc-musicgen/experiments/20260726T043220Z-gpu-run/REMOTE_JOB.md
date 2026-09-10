# Frozen remote job: HDC × MusicGen structural-memory GPU run

- Status: `EXECUTED — FAIL-CLOSED AT SMOKE STAGE A; POD TERMINATED`
- Approved hard spend cap: `USD 25`
- Approval owner: Benjamin Goertzel
- Approval recorded: `2026-07-26`; RunPod, one RTX 3090 24 GB, 18-hour
  elapsed-time limit, and USD 25 hard cap.
- Hard cost cap if explicitly approved: `USD 25`
- Project/run label: `hdc-musicgen-20260726-gpu-structural-r1`
- Frozen source commit: `f4506a7094aaf5f549f16f605a8ef0bf808653c0`
  on local branch `agent/stagec-oracle-diagnostic`

## Provider and resource

- Provider/account: RunPod, Ben-approved account context to be confirmed.
- GPU: one RTX 3090 24 GB (runbook-approved A10/3090/4090 class). Secure Cloud
  preferred; Community Cloud acceptable if Ben approves.
- Region: any available region approved by Ben; record actual region.
- Image: RunPod PyTorch image with CUDA 12.1; record immutable template/image
  identifier before creation.
- Storage: 40 GB container disk plus 30 GB temporary volume.
- Network: outbound HTTPS for PyPI, Hugging Face, GitHub, and selected audio
  archive; SSH ingress only if required by the approved workflow.

Official RunPod pricing page, checked 2026-07-25 23:54 PDT:
`https://www.runpod.io/pricing`; RTX 3090 listed at USD 0.46/hr (Secure Cloud)
or USD 0.22/hr (Community Cloud). Estimate 7 GPU-hours = USD 3.22 (secure) or
USD 1.54 (community). Allowing dependency setup, storage, retry margin, and
price/availability variation, terminate at 18 elapsed hours or USD 25 observed
or estimated total, whichever comes first. Re-check the live console price
before provisioning.

## Expected duration

Based on runbook §4 rough budget (30 tracks × 3 min, A10-class):

| Step | Estimate |
|---|---:|
| Provision / install / model download / smoke | 0.75 h |
| Stage 0 (tokenize) | 0.25 h |
| Stage S (chroma structure analysis, CPU-bound) | 0.33 h |
| Stage A (4 conditions × 2 strata, decision point) | 1.0–1.5 h |
| Stage C (optional, no-noise self-test) | 0.17 h |
| Stage D (adapter training, only if stageA gate passes) | 2.0–4.0 h |
| Validation / package / retrieval | 0.3 h |
| Total expected | 5–7 h |

Under one GPU-day. Stage D is conditional on stageA passing its gate; if it
does not, total drops to ~3 h.

## Audio data plan

Use the official MTG-Jamendo Dataset
(`https://mtg.github.io/mtg-jamendo-dataset/`, DOI `10.5281/zenodo.3826813`)
for non-commercial research. It contains full tracks with per-track Creative
Commons license metadata. Before GPU upload:

1. Clone only the metadata repository and pin its commit.
2. Select at least 20 tracks with duration ≥180 s from one downloadable audio
   archive, requiring an explicit per-track CC license in
   `audio_licenses.txt`; exclude unclear/missing entries.
3. Prefer CC0 or CC BY; if CC BY-SA is used, preserve attribution and license
   URL. Do not use NC material outside this non-commercial research run.
4. Download the smallest archive containing the selected tracks using the
   repository's checksum-validating downloader; retain only selected audio.
5. Create `audio_manifest.tsv` containing track ID, artist/title, duration,
   source URL, license identifier/URL, source metadata commit, local SHA-256,
   and download date.
6. Verify ≥20 tracks, each ≥180 s (runbook §3 requires ≥3 min each, ≥60 min
   total).

Privacy classification: public licensed audio and public code only. Upload no
unrelated workspace files, credentials, OpenClaw state, or private sources.

## Transfer and environment

Transfer the repository at the frozen commit plus selected audio and manifest
using `rsync`; exclude `.git` credentials, `.venv`, caches, and all unrelated
projects. On the pod:

```bash
python3 -m venv /workspace/hdc-venv
source /workspace/hdc-venv/bin/activate
python -m pip install -U pip
python -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
python -m pip install audiocraft==1.3.0 pytest librosa
cd /workspace/hdc-musicgen
python -m pytest -q
```

Record `nvidia-smi`, Python, torch, torchaudio, AudioCraft, librosa, CUDA
versions, image ID, GPU model, repository commit, and clean Git status.

## Exact staged commands

Smoke test first (everything, tiny):

```bash
export AUDIO=/workspace/audio
export SMOKE=/workspace/results-smoke
python hdc_musicgen_structural.py stage0 --audio_dir "$AUDIO" --out_dir "$SMOKE" --limit 4 --max_seconds 120
python hdc_musicgen_structural.py stageS --out_dir "$SMOKE" --spans_per_track 3
python hdc_musicgen_structural.py stageA --out_dir "$SMOKE"
python hdc_musicgen_structural.py stageC --out_dir "$SMOKE"
python hdc_musicgen_structural.py stageD --out_dir "$SMOKE" --adapter_steps 100
```

Only after every smoke JSON exists and its applicable gate passes, wipe
`$SMOKE` and run for real:

```bash
export FULL=/workspace/results-full
python hdc_musicgen_structural.py stage0 --audio_dir "$AUDIO" --out_dir "$FULL"
python hdc_musicgen_structural.py stageS --out_dir "$FULL"
python hdc_musicgen_structural.py stageA --out_dir "$FULL"     # <-- decision point
python hdc_musicgen_structural.py stageC --out_dir "$FULL"     # optional, ~10 min
python hdc_musicgen_structural.py stageD --out_dir "$FULL"     # ONLY if stageA gate passes
```

Use a named `tmux` session and capture stdout/stderr per stage.

## Frozen choices (never change)

- The frozen backbone — no fine-tuning of `lm` parameters, ever.
- The RELATED/UNRELATED stratification, or the length-matched random control.
- The stageA condition set (`window`, `matched`, `random`, `full`), or the
  eval-span accounting (`eval_from`).
- Scoring as teacher-forced NLL in nats/token over masked positions.

## Allowed knobs (with a one-line note in the report)

- `--batch`, `--max_seconds`, `--limit` for memory and wall-clock.
- `--adapter_steps`, learning rate (halve on divergence).
- `--window` (default 10 s) — if stageA's within-window `full` reference
  suggests a different truncation is more informative.
- `--hdc_D` (8192 → 16384) and `--adapter_tokens` in {8, 16, 32}; run both
  and report both if the first shows a marginal effect.
- `--block_seconds`, `--spans_per_track` for structure-analysis resolution.

## Validation gates (check after each stage; do not proceed on failure)

**Stage 0**: `stage0_persistence.json` must show `n_tracks >= 20` and
`total_minutes >= 60`. Per-codebook persistence should lie in (0.05, 0.9) and
generally decrease from codebook 0 to 3.

**Stage S**: in `stageS_summary.json`, `related_sim_mean` must exceed
`unrelated_sim_mean` by ≥ 0.15 cosine. If the two strata are not separated,
the corpus lacks detectable structure — stop and report; do not proceed to
stageA.

**Stage A** (decision point): four conditions × two strata. Headline is
`relevance_gain = random_nll - matched_nll` on RELATED spans.
- Proceed to stageD only if: related `relevance_gain > 0.02` nats/token AND
  it clearly exceeds the unrelated `relevance_gain`.
- If related gain ~0: stop and report a null — the pretrained model cannot
  exploit returning material even when handed it directly.
- If related and unrelated gains are equal and both positive: report as
  generic conditioning, not structure; do not proceed.
- Sanity band: absolute NLL in 1.5–6.0 nats/token. Below 0.5 = alignment bug.
  Above 8 = conditioning broken.

**Stage C** (optional): `snr99` (noiseless) must be ~1.000 for both cold and
warm — that is the self-test. Expect cold collapse at lower SNR while
`warm_prev` holds up. Feasibility footnote only, never a headline.

**Stage D**: expect `window >= summary` (adapter can at worst be neutral).
If `summary` worse than `window` by > 0.02 nats, halve LR and rerun once.
Report `summary_gain` per stratum, the RELATED-minus-UNRELATED contrast, and
`fraction_of_oracle_recovered`.

## Fragile points (audiocraft internals)

Three places are marked FRAGILE in the source. Fix minimally, verify against
the sanity band, and record every change.

1. `null_condition_tensors()` — builds "no text" conditioning. If it raises,
   read `audiocraft/models/lm.py` and `audiocraft/modules/conditioners.py`.
2. `_predictions()` — the `compute_predictions` signature. Keep semantics:
   logits `(B,K,T,card)` aligned with input `codes`, plus boolean mask.
3. `cond_from()` in stageD — injects adapter output where text conditioning
   goes. If the LM rejects the shape, print a real text-conditioned
   `condition_tensors` object and match shape/dtype/mask exactly.

Plumbing sanity check (recommended before trusting any null): run stageA with
`--model facebook/musicgen-melody`. That checkpoint accepts chromagram
conditioning through the same cross-attention path stageD injects into,
confirming the channel can carry structural information.

If a fix attempt fails twice, stop and write up what you tried. Do not thrash.

## Stop conditions

Stop and report (partial results are fine) if:
- The data or stageS separation gates cannot be met.
- StageA's NLL sanity band cannot be reached after FRAGILE-point fixes.
- StageA's gate fails — **do not run stageD to "see what happens"**.
- Cumulative GPU time exceeds ~1.5 GPU-days.
- A fix would require changing anything in the frozen list.

## Retrieval, verification, cleanup

Retrieve all JSON artifacts, `RESULTS.md`, manifest, environment record,
commands, and logs into this run directory's `artifacts/`. Generate local
SHA-256 checksums before transfer and verify them after retrieval. Confirm
JSON parses and rerun the gate checker. Then terminate the pod (not merely
stop it), confirm no billable volume, endpoint, or snapshot remains, query
provider state again, and record resource ID, final observed cost, termination
timestamp, and cleanup evidence.

Ben explicitly approved RunPod, one RTX 3090 24 GB, an 18-hour timeout, and a
USD 25 hard cap on 2026-07-26. The live price, actual region/image, and provider
resource identifiers must be recorded below before and immediately after
provisioning.

## Execution record

- Provider account: `bengoertzel@gmail.com` (verified by `runpodctl doctor`;
  no credential material recorded)
- Preflight: `runpodctl doctor` healthy; local/cloud SSH key registered
- Live offer selected: RunPod legacy cloud listing showed RTX 3090 at USD
  0.22/hour before creation; the selected Secure Cloud pod creation response
  reported USD 0.50/hour. The latter is the authoritative run price.
- Pod ID: `qmp6o3dkmvcp8d`
- Region: `CZ` (Secure Cloud)
- Image: `runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`
  via official template `runpod-torch-v220`
- GPU / price: one RTX 3090 24 GB at USD 0.50/hour
- Storage: 40 GB container disk plus 30 GB temporary `/workspace` volume
- Started: `2026-07-26T07:40:51Z`
- Provider-side auto-termination: 18 hours after creation
- Terminated: `2026-07-26T15:12:15Z`; deletion confirmed, pod list empty,
  subsequent lookup returned 404.
- Final cost: approximately `USD 3.76` from 7 h 31 m 24 s
  creation-to-termination elapsed time at `USD 0.50/hour`. The CLI did not
  expose a final accrued-charge field.
- Outcome: smoke Stage S passed, but Stage A failed the frozen absolute-NLL
  sanity gate after two minimal FRAGILE fixes. Full run and Stages C/D were not
  executed. See `RUN.md`.
