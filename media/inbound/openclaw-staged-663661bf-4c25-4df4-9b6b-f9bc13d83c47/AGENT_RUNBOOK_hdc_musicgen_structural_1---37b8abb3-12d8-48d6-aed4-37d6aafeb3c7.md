# AGENT RUNBOOK: structural memory for MusicGen (`hdc_musicgen_structural.py`)

You are a coding agent running a staged experiment on a RunPod GPU. Run the
stages in order, check each against its gate, fix only what blocks
execution, and report the numbers. **A clean null is a successful outcome.**
The only real failure is a corrupted positive.

---

## 1. What is being tested, and what is NOT

MusicGen attends over ~30 s and generates longer audio with a sliding
window, so anything older than the window is discarded: it cannot recall a
motif, return to a theme, or keep key across a 3-minute piece. This
experiment asks whether a **fixed-width hypervector summary of distant
history**, injected through the cross-attention conditioning path, can
restore some of that lost structure.

**This is not a speed experiment.** Do not report or optimize for speedup.
The arithmetic was checked: history compression targets ~19% of per-frame
FLOPs (ceiling ~1.2x end-to-end) and output-interface changes target ~2%,
so the interesting payoff is capability, not latency. If you find yourself
benchmarking tokens/second, you have drifted off task.

Because most spans of music have no long-range dependency, **uniform
sampling would average any real effect into noise.** Every measurement is
therefore stratified into RELATED spans (structurally similar to material
older than the window) and UNRELATED spans, and every comparison is
length-controlled. The RELATED-minus-UNRELATED contrast is the result;
a number that is equally good on both strata is generic conditioning, not
memory.

---

## 2. Environment

```bash
pip install -U pip
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install audiocraft==1.3.0
```

One GPU >= 16 GB (A10/3090/4090 class). `facebook/musicgen-small` is
ungated; first run downloads ~2 GB. If dependency resolution fails, change
the **torch** pin, not the audiocraft pin — the script targets audiocraft
1.3.0 internals.

---

## 3. Data (this gate is strict — a bad corpus guarantees an uninteresting null)

Required: **>= 20 tracks, >= 3 minutes each, with real repetition
structure** — pop, electronic, hip-hop, or classical with recapitulation.

Explicitly unsuitable: ambient, drone, free improvisation, through-composed
material, and any 30-second clip dataset (FMA-small/medium are 30 s clips —
do not use). If the music has no returning material, stageS has nothing to
find and stageA will report a null for reasons that say nothing about the
hypothesis.

**Gate after stage0:** `stage0_persistence.json` must show
`n_tracks >= 20` and `total_minutes >= 60`. Per-codebook persistence should
lie in (0.05, 0.9) and generally decrease from codebook 0 to 3.

**Gate after stageS:** in `stageS_summary.json`, `related_sim_mean` must
exceed `unrelated_sim_mean` by a clear margin (>= 0.15 in cosine). If the
two strata are not separated, the corpus lacks detectable structure — stop
and report; do not proceed to stageA.

---

## 4. Runbook

Smoke test first (everything, tiny):

```bash
python hdc_musicgen_structural.py stage0 --audio_dir $AUDIO --limit 4 --max_seconds 120
python hdc_musicgen_structural.py stageS --spans_per_track 3
python hdc_musicgen_structural.py stageA
python hdc_musicgen_structural.py stageC
python hdc_musicgen_structural.py stageD --adapter_steps 100
```

Then wipe `./hdc_mg_struct` and run for real:

```bash
python hdc_musicgen_structural.py stage0 --audio_dir $AUDIO
python hdc_musicgen_structural.py stageS
python hdc_musicgen_structural.py stageA     # <-- decision point
python hdc_musicgen_structural.py stageC     # optional, ~10 min
python hdc_musicgen_structural.py stageD     # ONLY if stageA gate passes
```

Rough budget (30 tracks x 3 min, A10-class): stage0 ~15 min, stageS ~20 min
(CPU-bound chroma), stageA ~45–90 min, stageC ~10 min, stageD ~2–4 h.
Under one GPU-day total.

---

## 5. Gates and how to read the numbers

### stageA — the decision point (no training involved)

Four conditions per span: `window` (status quo), `matched` (window with the
retrieved returning chunk prepended), `random` (same length, wrong content),
`full` (reference, only where the span starts within the model's own 30 s
window).

The headline is **`relevance_gain = random - matched`** on RELATED spans:
the value of distant context *with sequence length held constant*. Comparing
`matched` against `window` alone would confound relevance with simply having
more tokens; that is why the random control exists and why it must never be
dropped.

**Proceed to stageD only if:** related `relevance_gain` > 0.02 nats/token
AND it clearly exceeds the unrelated `relevance_gain`.

If related gain is ~0: the pretrained model cannot exploit returning
material even when handed it directly. No summary can beat that, so **stop
and report a null** — this is a real, publishable finding about the model,
not a failure of the run.

If related and unrelated gains are equal and both positive: the model is
benefiting from extra context generically, not from structure. Report as
such; do not proceed.

Sanity band: absolute NLL should sit roughly in **1.5–6.0 nats/token**.
Below 0.5 means you are scoring positions the model was given as input
(alignment bug). Above 8 means conditioning is broken.

### stageC (optional)

`snr99` (noiseless) must be ~1.000 for both cold and warm — that is the
self-test. Expect cold start to collapse at lower SNR while `warm_prev`
holds up; that contrast is the whole point. Feasibility footnote only,
never a headline.

### stageD

Expect `window >= summary` (the adapter can at worst be neutral). If
`summary` is worse than `window` by > 0.02 nats, training diverged: halve
the learning rate and rerun once.

The result to report is **`summary_gain` on RELATED spans minus
`summary_gain` on UNRELATED spans**. `fraction_of_oracle_recovered` tells
you how much of the retrieval ceiling a fixed-width summary captures.

---

## 6. Frozen choices vs allowed knobs

**Never change** (these define the experiment):
- the frozen backbone — no fine-tuning of `lm` parameters, ever;
- the RELATED/UNRELATED stratification, or the length-matched random
  control;
- the stageA condition set, or the eval-span accounting (`eval_from`);
- scoring as teacher-forced NLL in nats/token over masked positions.

**May change, with a one-line note in the report:**
- `--batch`, `--max_seconds`, `--limit` for memory and wall-clock;
- `--adapter_steps`, learning rate (halve on divergence);
- `--window` (default 10 s) — if stageA's within-window `full` reference
  suggests a different truncation is more informative;
- `--hdc_D` (8192 -> 16384) and `--adapter_tokens` in {8, 16, 32}; run both
  and report both if the first shows a marginal effect;
- `--block_seconds`, `--spans_per_track` for structure-analysis resolution.

---

## 7. Fragile points (audiocraft internals) and fix protocol

Three places are marked FRAGILE in the source. Fix minimally, verify against
the §5 sanity band, and record every change.

1. **`null_condition_tensors()`** — builds "no text" conditioning (the same
   path CFG uses for its unconditional branch). If it raises, read
   `audiocraft/models/lm.py` and `audiocraft/modules/conditioners.py` in the
   installed version and adapt.
2. **`_predictions()`** — the `compute_predictions` signature. Keep the
   semantics: logits `(B,K,T,card)` aligned with input `codes`, plus a
   boolean mask of valid scoring positions. If `gather` throws device-side
   asserts, check whether your version pads codes with a special token id
   >= card; clamp and mask rather than silently filtering.
3. **`cond_from()` in stageD** — injects the adapter output where text
   conditioning goes. If the LM rejects the shape, print a real
   text-conditioned `condition_tensors` object from helper (1) and match
   shape, dtype, and mask convention exactly.

**Plumbing sanity check (recommended before trusting any null):** run
stageA with `--model facebook/musicgen-melody`. That checkpoint accepts
chromagram conditioning through the same cross-attention path stageD
injects into, so it confirms the channel can carry structural information.

If a fix attempt fails twice, stop and write up what you tried. Do not
thrash.

---

## 8. Report `RESULTS.md` in out_dir

1. Environment: GPU, torch/audiocraft versions, checkpoint, and a data
   summary (n tracks, total minutes, genres, source).
2. Deviations and fixes (§6/§7), one line each.
3. stageS: related vs unrelated similarity means; did the separation gate
   pass?
4. stageA table: all four conditions x both strata, plus the headline
   length-controlled `relevance_gain` per stratum. State plainly whether the
   gate passed.
5. stageC (if run): the noiseless self-test plus warm-vs-cold by SNR.
6. stageD (if run): the four conditions x both strata, `summary_gain` per
   stratum, the RELATED-minus-UNRELATED contrast, and
   `fraction_of_oracle_recovered`.
7. One paragraph: did the pretrained model show usable long-range
   structural value; did a fixed-width summary capture any of it; and what
   single follow-up would be most informative (e.g. `musicgen-medium` for a
   stronger teacher, larger `--hdc_D`, longer `--window`, or a
   structure-richer corpus).

Attach all JSON artifacts verbatim.

---

## 9. Stop conditions

Stop and report (partial results are fine) if:
- the §3 data or stageS separation gates cannot be met;
- stageA's NLL sanity band cannot be reached after §7 fixes;
- stageA's gate fails — **do not run stageD to "see what happens"**;
- cumulative GPU time exceeds ~1.5 GPU-days;
- a fix would require changing anything in the frozen list (§6).
