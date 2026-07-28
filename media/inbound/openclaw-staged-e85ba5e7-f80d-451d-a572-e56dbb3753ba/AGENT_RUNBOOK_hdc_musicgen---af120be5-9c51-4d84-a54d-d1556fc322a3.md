# AGENT RUNBOOK: HDC x MusicGen experiments (`hdc_musicgen_experiments.py`)

You are a coding agent executing a staged scientific experiment on a RunPod
GPU. Your job is to **run the stages in order, validate each against its
gate, fix only what blocks execution, and report the numbers** — not to
improve, refactor, or extend the science. Both positive and negative results
are valuable; a cleanly-measured null is a success. A silently-corrupted
positive is the only real failure.

---

## 1. Mission

The script tests whether hyperdimensional-computing (HDC) machinery can make
autoregressive music generation cheaper/faster, using a frozen pretrained
MusicGen as the testbed. Four independent hypotheses, one stage each:

| Stage | Hypothesis | Success looks like | Failure is still informative because |
|---|---|---|---|
| A | Long context has measurable NLL value that saturates, leaving a bounded gap a compressed memory could recover | NLL decreases with context then flattens; nonzero gap between window-W and full | A near-zero gap means the *teacher* underuses long context (try `--model facebook/musicgen-medium`) |
| B | One linear bundle-head projection can match K independent softmax heads on identical inputs/targets | bundle exact-accuracy within ~1–2 pts of multi-head | A large gap means sign-bundle targets lose information at this D → report the D at which parity returns |
| C | Previous-frame warm start gives resonator basin entry at real product-space scale (~1.8e13) | warm >> cold at moderate SNR; cold ~0 is EXPECTED | If warm also fails, real music token dynamics don't provide basin entry → kills the product-state channel |
| D | A fixed-width HDC summary of distant history, injected via the text cross-attention path, recovers part of the truncated-vs-full NLL gap | `fraction_recovered_by_HDC_summary` meaningfully > 0 | 0% recovery with a healthy stage-A gap means this summary construction is inadequate (report, do not iterate beyond §6 knobs) |

Do not reorder stages: A's output tells you whether D is worth running, and
stage0's cache feeds everything.

---

## 2. Environment

- GPU: one card, >= 16 GB (A10 / 3090 / 4090 class). musicgen-small: ~4 GB
  inference; stageD training: ~10–14 GB.
- Install exactly:

```bash
pip install -U pip
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install audiocraft==1.3.0
```

- `facebook/musicgen-small` is ungated; no HF token needed. First run
  downloads ~2 GB of weights.
- If `audiocraft==1.3.0` fails to resolve against your torch version,
  prefer changing the **torch** pin, not the audiocraft pin. The script is
  written against audiocraft 1.3.0 internals.

---

## 3. Data

Requirement: **>= 20 music tracks of >= 120 s each** (more and longer is
better; the long-context stages are meaningless on short clips). Any genre;
mono/stereo/mp3/wav/flac all fine.

- If the operator supplied a directory, use it.
- If you must source audio yourself, use a license-clean source of
  full-length tracks (e.g. Creative Commons collections; note that
  FMA-*small/medium* are 30 s clips — unsuitable; you need full tracks).
- Gate before proceeding: after `stage0`, open `codes_meta.json` and verify
  `sum(frames) >= 20 * 120 * 50` (i.e. >= 120,000 frames total) and that at
  least 15 tracks have `frames >= 6000`. If not, get more/longer audio.

---

## 4. Execution runbook

Always smoke-test the full pipeline first:

```bash
python hdc_musicgen_experiments.py stage0 --audio_dir $AUDIO --limit 4 --max_seconds 40
python hdc_musicgen_experiments.py stageA --contexts 1,2,5 --eval_seconds 2
python hdc_musicgen_experiments.py stageB --probe_steps 200
python hdc_musicgen_experiments.py stageC
python hdc_musicgen_experiments.py stageD --adapter_steps 200 --adapter_window 5
```

Every stage must complete and write its JSON before you scale up. Then wipe
`./hdc_mg_out` and run for real:

```bash
python hdc_musicgen_experiments.py stage0 --audio_dir $AUDIO
python hdc_musicgen_experiments.py stageA
python hdc_musicgen_experiments.py stageB
python hdc_musicgen_experiments.py stageC
python hdc_musicgen_experiments.py stageD
```

Approximate budgets (A10-class, 30 tracks x 3 min): stage0 ~10 min;
stageA ~30–60 min (dominated by the `full` condition on long tracks);
stageB ~20–30 min; stageC ~10 min; stageD ~2–4 h. Total well under one
GPU-day. If stageA's `full` condition is intolerably slow, cap tracks with
`--max_seconds 120` — but then also cap `--contexts` at 60 and say so in the
report.

Artifacts after a full run (all in `--out_dir`, default `./hdc_mg_out`):
`codes.pt`, `codes_meta.json`, `stage0_persistence.json`,
`stageA_context_curve.json`, `stageB_heads.json`, `stageC_resonator.json`,
`stageD_adapter.json`.

---

## 5. Validation gates (check after each stage; do not proceed on failure)

**stage0**
- Persistence values in `stage0_persistence.json` should be in (0.05, 0.9)
  per codebook and typically decreasing from codebook 0 to 3. Values ~0 or
  ~1 across the board indicate a tokenization bug.

**stageA**
- Mean NLL must be **monotone non-increasing** in context length (small
  non-monotonic wiggles < 0.02 nats are noise; large violations mean the
  eval-span alignment is broken — see §7).
- Absolute NLL sanity band: roughly **1.5–6.0 nats/token** for music tokens
  under musicgen-small. NLL < 0.5 → you are probably scoring positions the
  model was given as input (alignment bug). NLL > 8 → conditioning is
  probably broken (model effectively scoring noise).

**stageB**
- Multi-head exact accuracy must be far above chance (chance for exact
  4-tuple is ~(1/2048)^4 ~ 0; per-codebook chance 0.0005). If per-codebook
  accuracy < 0.05, the hidden-state hook is mis-wired (see §7).
- Compare interfaces only if both trained to convergence: if the last 10%
  of steps still moved loss > 5%, double `--probe_steps` once and rerun.

**stageC**
- `warm_prev` >= `cold` at every SNR, and cold should collapse toward 0 at
  low SNR. If warm ~ cold ~ 0 even at 20 dB, atom/product bookkeeping is
  buggy (test: at infinite SNR — no noise — warm and cold must both be ~1.0;
  add that check manually if in doubt).

**stageD**
- Expected ordering: `nll_truncated >= nll_truncated_plus_HDC_adapter >=
  nll_full_context` (adapter can at worst be neutral; if adapter is *worse*
  than truncated by > 0.02 nats, training diverged — see §6).
- Only interpret `fraction_recovered_by_HDC_summary` if
  `long_context_gap > 0.03` nats/token. Below that, report "gap too small
  to measure recovery" and stop.

---

## 6. Allowed knobs vs frozen choices

You MAY adjust, with a note in the report:
- batch size, sequence/segment lengths, `--limit`, `--max_seconds` (OOM and
  wall-clock management);
- learning rates and step counts (if divergence: halve lr, add
  `torch.nn.utils.clip_grad_norm_(adapter.parameters(), 1.0)` before
  `opt.step()` in stageD);
- `--hdc_D` and `--bundle_D` upward (8192 → 16384) if stageB parity fails
  or stageC warm-start underperforms — run both D values and report both;
- `--adapter_window` (default 10 s) to match wherever stageA shows the
  curve still rising;
- `--adapter_tokens` in {8, 16, 32}.

You MUST NOT change (these define the experiment):
- the frozen backbone (no fine-tuning of `lm` parameters, ever);
- identical inputs/targets for the two stageB interfaces;
- the stageC noise model and cold/warm comparison structure;
- the stageD evaluation triple (truncated / truncated+adapter / full) and
  the eval-span accounting;
- scoring: teacher-forced NLL in nats/token over masked positions.

---

## 7. Known fragile points and fix protocol

The script marks two audiocraft-API-dependent helpers as FRAGILE. If
anything breaks, it will almost certainly be here. Fix minimally; verify
with the sanity bands in §5; record every change in the report.

1. **`null_condition_tensors()`** — builds the "no text" conditioning.
   If it raises: read `audiocraft/models/lm.py` and
   `audiocraft/modules/conditioners.py` in your installed version; the goal
   is whatever object `lm.compute_predictions` expects as
   `condition_tensors` representing a null text prompt (this is the same
   path classifier-free guidance uses for its unconditional branch). A
   correct fix reproduces the §5 stageA NLL sanity band.

2. **`teacher_nll()` / `compute_predictions` signature** — if the signature
   drifted, adapt the call but keep the semantics: logits `(B,K,T,card)`
   aligned with input `codes` and a boolean mask of valid scoring
   positions. Beware the delay-pattern special token: `codes` values must
   all be `< card` at gather time; if you see device-side asserts from
   `gather`, clamp-and-mask rather than filtering silently, and check
   whether your audiocraft version pads codes with a special token id.

3. **Hidden-state hook (`lm.out_norm`)** in stageB — if absent in your
   version, hook the output of the final transformer block instead. Verify:
   multi-head probe accuracy clears the §5 gate.

4. **stageD condition injection** (`{"description": (emb, mask)}`) — if the
   LM rejects the shape, print one real text-conditioned
   `condition_tensors` object from helper (1) and match your injected
   tensor's shape/dtype/mask convention to it exactly.

5. **OOM** — first reduce `--batch`, then `seg_frames` (stageB) /
   `--max_seconds`, then move stageA `full` condition to fp16 via
   `torch.autocast`. Do not silently drop the `full` condition.

If a fix attempt fails twice, stop and write up what you tried; do not
thrash.

---

## 8. Report format

Produce `RESULTS.md` in the out_dir containing:

1. Environment: GPU, torch/audiocraft versions, model checkpoint, data
   summary (n tracks, total minutes, source).
2. Any deviations from defaults or fixes applied (§6/§7), each in one line.
3. The four headline numbers, each with its one-sentence interpretation:
   - stageA: NLL-vs-context table + the gap at the chosen window;
   - stageB: exact accuracy multi-head vs bundle, decode ms/frame, head
     parameter counts;
   - stageC: warm vs cold exact-frame recovery at each SNR;
   - stageD: the NLL triple and `fraction_recovered_by_HDC_summary`.
4. Gate outcomes: which §5 gates passed/failed.
5. One paragraph: given these numbers, which of the four hypotheses
   survived, and what single follow-up run would be most informative
   (e.g. musicgen-medium for a bigger stage-A gap; larger D for stageB/C;
   longer `--adapter_window` for stageD).

Attach all five JSON artifacts verbatim at the end.

---

## 9. Stop conditions

Stop and report early (partial results are fine) if:
- the §3 data gate cannot be met;
- stageA's sanity band cannot be reached after §7 fixes (everything
  downstream would be uninterpretable);
- cumulative GPU time exceeds ~1.5 GPU-days;
- any fix would require modifying frozen-choice items in §6.
