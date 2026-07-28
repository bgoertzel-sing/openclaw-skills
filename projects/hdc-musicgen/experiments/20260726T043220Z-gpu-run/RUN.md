# Run 20260726T043220Z-gpu-run

- Project: `hdc-musicgen`
- Status: `fail-closed at smoke Stage A sanity gate`
- Provider: RunPod Secure Cloud, pod `qmp6o3dkmvcp8d`
- Image: `runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`
- GPU: one NVIDIA GeForce RTX 3090, 24,576 MiB
- Frozen source: branch `agent/stagec-oracle-diagnostic`, commit
  `f4506a7094aaf5f549f16f605a8ef0bf808653c0`
- Minimal FRAGILE fixes committed after the run:
  `609c9c6d5b8e2941dca76f2884f7270f7f194fa0`
- Pod created: `2026-07-26T07:40:51Z`
- Resumed for this execution: `2026-07-26T14:54:18Z`
- Terminated: `2026-07-26T15:12:15Z`
- Creation-to-termination wall time: 7 h 31 m 24 s
- Price: USD 0.50/hour
- Cost: approximately USD 3.76 from elapsed time at the fixed hourly price;
  RunPod CLI did not expose a final accrued-charge field

## Question and disposition

Can the frozen HDC × MusicGen structural-memory experiment pass its staged
gates on a license-clean real-audio corpus?

**Observed:** environment tests passed and smoke Stages 0/S ran. Smoke Stage S
separated RELATED from UNRELATED material. After two minimal FRAGILE-point
repairs, Stage A returned finite and plausible NLLs, but one UNRELATED smoke
span had absolute NLL below the frozen 1.5 lower sanity bound.

**Decision:** fail closed. The full run was not started. Stage C and Stage D
were not run. No claim about the full corpus, the resonator, or the learned HDC
adapter is supported by this run.

## Data

**Observed:** the official MTG-Jamendo metadata repository was pinned at
`cafd8e20c265ed84f1e61f1c875327971f43a62f`. The selected archive yielded 24
tracks with explicit CC BY 2.0 or CC BY-SA 2.0 metadata. The shortest measured
track was 186.958 seconds and total measured duration was 123.635 minutes.
Every local audio file was present and hashed in `audio_manifest.tsv`.
The generator was corrected after retrieval to include the required explicit
`download_date = 2026-07-26` column; the completed version is preserved as
`artifacts/audio_manifest_with_download_date.tsv`, while
`artifacts/audio_manifest.tsv` remains the byte-identical remote copy.

**Inference:** the prepared corpus satisfies the pre-tokenization licensing,
track-count, per-track-duration, and total-duration requirements. Because the
full Stage 0 command was not authorized by the smoke gate outcome, full-corpus
codec persistence was not measured.

## Environment

| Component | Observed version |
|---|---|
| Python | 3.10.12 |
| torch | 2.1.0+cu121 |
| torchaudio | 2.1.0+cu121 |
| AudioCraft | 1.3.0 |
| librosa | 0.11.0 |
| NumPy | 1.26.4 |
| Transformers | 4.35.2 |
| PyAV | 11.0.0 |
| CUDA runtime reported by torch | 12.1 |
| NVIDIA driver | 610.43.02 |
| FFmpeg | 4.4.2 |

The initial unbounded dependency resolution selected NumPy 2.2.6 and
Transformers 5.14.1. NumPy 2 was binary-incompatible with torch 2.1, while
Transformers 5.14 disabled torch versions below 2.4. Environment-only
compatibility pins changed these to NumPy 1.26.4 and Transformers 4.35.2.
FFmpeg runtime libraries were installed for the built PyAV 11 extension.

## Validation before execution

- **Observed:** `python -m pytest -q` passed all 13 frozen repository tests
  after the environment became importable.
- **Observed:** after the runtime repairs and added NaN-mask regression,
  `python -m pytest -q test_hdc_musicgen_structural.py` passed 7 tests.
- **Observed:** CUDA was available and identified the RTX 3090.
- **Observed:** remote source hashes matched the frozen local files before the
  two recorded FRAGILE fixes.

## Exact staged commands

The named remote tmux session was `hdc-structural-r1`. The commands were:

```bash
export AUDIO=/workspace/audio
export SMOKE=/workspace/results-smoke
python hdc_musicgen_structural.py stage0 --audio_dir "$AUDIO" --out_dir "$SMOKE" --limit 4 --max_seconds 120
python hdc_musicgen_structural.py stageS --out_dir "$SMOKE" --spans_per_track 3
python hdc_musicgen_structural.py stageA --out_dir "$SMOKE"
```

Stage A was rerun after each minimal FRAGILE repair. The following frozen
commands were deliberately not run:

```bash
python hdc_musicgen_structural.py stageC --out_dir "$SMOKE"
python hdc_musicgen_structural.py stageD --out_dir "$SMOKE" --adapter_steps 100
python hdc_musicgen_structural.py stage0 --audio_dir "$AUDIO" --out_dir /workspace/results-full
```

Logs preserve wall times and stderr:
`smoke-stage0.log`, `smoke-stageS.log`, `smoke-stageA.log`,
`smoke-stageA-fix1.log`, and `smoke-stageA-fix2.log`.

Core setup and compatibility commands were:

```bash
python3 -m venv /workspace/hdc-venv
source /workspace/hdc-venv/bin/activate
python -m pip install -U pip
python -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
python -m pip install audiocraft==1.3.0 pytest librosa
apt-get update
apt-get install -y ffmpeg tmux rsync
python -m pip install "numpy<2"
python -m pip install "transformers==4.35.2"
python -m pytest -q
```

Retrieval, verification, and cleanup used:

```bash
rsync -avz --no-owner --no-group \
  -e "ssh -i /home/openclaw/.runpod/ssh/runpodctl-ssh-key -p 40109" \
  root@213.192.2.75:/workspace/results-smoke/ artifacts/
sha256sum -c REMOTE_SHA256SUMS
python3 -c 'import glob,json; [json.load(open(p)) for p in glob.glob("artifacts/*.json")]'
runpodctl pod delete qmp6o3dkmvcp8d
runpodctl pod list
runpodctl pod get qmp6o3dkmvcp8d
```

## Stage results and gates

### Smoke Stage 0

**Observed:** four tracks and 8.0 minutes were tokenized, as required by the
tiny command. Per-codebook persistence was
`[0.06964, 0.04413, 0.04209, 0.03476]`. The JSON sets `smoke_mode: true` and
does not pass the full-corpus data gate.

**Inference:** model download, audio decode, resampling, codec execution, and
artifact writing worked. This tiny result is not evidence that the full Stage
0 persistence gate passes.

### Smoke Stage S

**Observed:** 12 RELATED spans and one UNRELATED span were mined.
`related_sim_mean = 0.984184`, `unrelated_sim_mean = 0.493875`, and separation
was `0.490309`, above the required 0.15. The Stage S gate passed.

**Inference:** the detector found sharply separated recurrence strata in the
four-track smoke subset, but the single UNRELATED sample makes smoke-only
downstream estimates fragile.

### Smoke Stage A

The first attempt raised a Float/Half LayerNorm mismatch. After FRAGILE fix 1,
the call completed but all NLL aggregates were NaN. FRAGILE fix 2 yielded:

| Stratum | window | matched | random | full | relevance gain |
|---|---:|---:|---:|---:|---:|
| RELATED (n=12) | 4.08487 | 4.01637 | 4.06844 | 3.05248 | 0.05207 |
| UNRELATED (n=1) | 1.26837 | 1.24421 | 1.24495 | 1.23326 | 0.00074 |

**Observed:** the relevance criterion itself passed: RELATED gain was above
0.02 and exceeded UNRELATED gain by more than 0.01. The absolute-NLL sanity
gate failed because every UNRELATED condition was below 1.5. Values remained
well above the runbook's `<0.5` alignment-bug warning threshold.

**Decision:** the frozen gate is conjunctive; Stage A did not pass. Stop before
Stage C/D and before any full run.

### Stage C and Stage D

**Observed:** no JSON exists because neither stage ran.

## FRAGILE-point fixes

1. `_predictions()` now mirrors AudioCraft's own CUDA generation path by
   entering fp16 autocast around `compute_predictions`. This fixed the
   Float/Half LayerNorm mismatch without changing logits, masks, conditions,
   or teacher-forced scoring semantics.
2. `masked_nll()` now uses `torch.where(score_mask, nll, 0.0)` before
   reduction. AudioCraft intentionally fills invalid pattern positions with
   NaN, and `NaN * False` remains NaN. A regression test demonstrates that
   invalid NaN-filled positions do not contaminate the masked NLL.

No frozen experimental choice was changed.

## Artifacts and integrity

All available remote smoke artifacts, logs, the audio manifest, environment
record, and remote checksum list were retrieved into `artifacts/`.
`REMOTE_SHA256SUMS` verified every retrieved remote file. `LOCAL_SHA256SUMS`
records the local artifact set, including the completed manifest with explicit
download date. All six retrieved JSON files parse with Python's standard
`json` module.

No `results-full` directory existed.

## Cleanup

**Observed:** `runpodctl pod delete qmp6o3dkmvcp8d` returned
`{"deleted": true}` at `2026-07-26T15:12:15Z`. A subsequent
`runpodctl pod list` returned `[]`, and `runpodctl pod get` returned HTTP 404
`pod not found`.

**Inference:** the pod and its temporary attached storage are no longer
billable. No endpoint, snapshot, or separately named persistent volume was
created by this run.

## Remaining uncertainty

**Hypothesis:** the sub-1.5 UNRELATED smoke NLL may reflect one unusually
predictable span rather than broken alignment, since the RELATED values and
all individual outputs are finite and plausible. Testing that hypothesis
would require a revised or explicitly waived smoke sanity policy; this run did
not assume that authority.
