# M4 Step 4.1: USAGE/Latency Distribution Analysis + T Recommendation

**Date:** 2026-09-04 21:54 PDT
**Source:** `/home/openclaw/.openclaw/protocosmo2-supervisor.log` (473,544 lines, ~104 MB)
**Span:** 2026-09-02 14:26 → 2026-09-04 21:55 (~55.5 hours)
**Total LLM calls extracted:** 5,640 (via `AFTER LLM` / `USAGE CompletionUsage` line pairing)

## Method

The supervisor log contains `BEFORE LLM` / `AFTER LLM` markers around each
`client.chat.completions.create(...)` call in iter.py (line ~894–916). Each
`AFTER LLM` line includes the full `ChatCompletion` object with a `created=`
Unix timestamp (provider-side completion time) and `USAGE CompletionUsage(`
metadata (token counts, cost, reasoning tokens). Each `USAGE` line is the
standalone print at line ~916.

Inter-call intervals were computed from consecutive `created=` timestamps
within the same model. These intervals represent the **total cycle time**
(tool execution + LLM API latency) per step — not pure LLM latency alone.
However, since the concurrency design's T parameter gates the LLM call
itself (the blocking point before tool dispatch), and the inter-call interval
is the best available proxy from log data alone, the analysis uses this as
the primary metric. The completion-token-stratified split (low vs high token
count) provides a secondary signal separating short-generation calls from
long-generation calls.

## Per-model results

### z-ai/glm-5.2 (current production model)

| Metric | All data (3,276 calls) | Last 24h (2,399 calls) |
|--------|----------------------|----------------------|
| p50 | 22s | 23s |
| p90 | 66s | 67s |
| p95 | 80s | 82s |
| mean | 34.4s | 36.0s |
| Fast (<30s) | 61.1% — p90=24s, p95=27s | 57.9% — p90=25s, p95=27s |
| Slow (≥30s) | 38.9% — p50=53s, p90=85s | 42.1% — p50=52s, p90=86s |
| Valley (30–40s) | 10.0% | 11.8% |
| Total cost | $20.89 | — |

### moonshotai/kimi-k3 (previous model)

| Metric | All data (2,149 calls) |
|--------|----------------------|
| p50 | 26s |
| p90 | 64s |
| p95 | 89s |
| mean | 35.8s |
| Fast (<30s) | 58.3% — p90=27s, p95=28s |
| Slow (≥30s) | 41.7% — p50=48s, p90=95s |
| Valley (30–40s) | 12.7% |
| Total cost | $48.56 |

### z-ai/glm-4.7 (brief test, 9 calls)

| Metric | Value |
|--------|-------|
| p50 | 14s |
| Fast (<30s) | 75.0% |
| Slow (≥30s) | 25.0% |

Too few calls for statistical significance; included for completeness.

## Histogram (z-ai/glm-5.2, all data)

```
  5- 10s:     2
 10- 15s:   246  ######
 15- 20s:   970  ##############################
 20- 25s:   540  ################
 25- 30s:   243  #######
 30- 35s:   163  ####
 35- 40s:   165  ####
 40- 50s:   265  ########
 50- 60s:   239  #######
 60- 90s:   284  ########
 90-120s:    52  ##
120-180s:    23  #
180-300s:     6  #
300+  s:     2  #
```

## Bimodal split assessment

**Partially confirmed.** The distribution shows two modes:

1. **Fast mode** (15–28s): 61.1% of calls, centered ~20s. This is the
   "simple tool call + short reasoning" mode — the model produces a
   tool call with <200 completion tokens and brief reasoning.

2. **Slow mode** (40–90s): 38.9% of calls, centered ~52s. This is the
   "complex reasoning + long generation" mode — the model produces
   200–2500 completion tokens with 100–1000+ reasoning tokens.

**Valley (30–40s):** 10.0% of calls fall in the gap between modes. These
are the "medium complexity" calls — they'd finish at 30–40s if allowed to
run to completion, but at T=30s they'd be promoted to a background thread
after 30s, wasting the initial 30s of compute and requiring a re-issue
in the background branch. This is the threshold misprediction cost
identified in the v3 frontier review.

**Not a clean bimodal distribution** — the valley contains meaningful mass
(10% of calls). However, the fast p95 (27s) is below T=30, so only ~3% of
fast calls would be unnecessarily promoted. The valley cost is real but
tolerable.

## Completion token correlation

Inter-call intervals stratified by completion token count (proxy for
generation time):

| Token range | Count | Interval p50 | Interval p90 | Mean |
|------------|-------|-------------|-------------|------|
| <200 (fast generation) | 1,464 | 16s | 33s | 19.5s |
| ≥200 (slow generation) | 4,174 | 30s | 68s | 38.6s |

Low-token calls cluster tightly at 16s median; high-token calls spread
from 30–68s. This confirms that generation length (and its associated
API time) is the primary driver of the slow mode.

## Reasoning token analysis

95.6% of all calls produced reasoning tokens (mean=398, p50=184, p90=1060).
The model is almost always "thinking" — the reasoning mode is not optional
or occasional. Reasoning token count correlates with inter-call interval
(Slow mode = high reasoning + high completion).

## T recommendation

**T = 30s remains the best default.** Justification:

| Criterion | Value | Assessment |
|-----------|-------|------------|
| Fast p95 | 27s | T=30 captures 95%+ of fast calls ✅ |
| Fast p90 | 24s | T=30 captures 90%+ with 3s margin ✅ |
| Slow p50 | 52s | T=30 reliably promotes slow calls (22s margin) ✅ |
| Valley (30–40s) | 10% of calls | Tolerable misprediction cost ⚠️ |
| Fast mode false promotion rate | ~3% | Acceptable ✅ |
| Slow mode capture rate | ~99% | Near-complete ✅ |

**Alternatives considered:**

| T | Fast capture | Valley cost | Slow blocking | Assessment |
|---|-------------|-------------|--------------|------------|
| 25s | p90 only (~90%) | ~15% valley | 25s on slow | Too aggressive — promotes too many fast calls |
| 28s | p95 (~95%) | ~12% valley | 28s on slow | Marginal improvement over 30s |
| **30s** | **>p95 (~97%)** | **~10% valley** | **30s on slow** | **Best balance** ✅ |
| 35s | >p95 | ~7% valley | 35s on slow | Reduces valley by 30% but extends slow blocking |
| 40s | >p99 | ~3% valley | 40s on slow | Eliminates most valley but blocks 40s on 42% of calls |

**BACKGROUND_DEADLINE** = max(2×30, 300) = 300s is well-calibrated:
slow p90 = 86s, so 300s gives 3.5× headroom. Even the p99 (~120s) is well
within the deadline. No adjustment needed.

## Cost context

- Total cost across all models: $69.55 (5,434 calls with cost data)
- Mean cost per call: $0.0128
- Daily cost (Sep 4): ~$34 for ~2,249 calls
- Implication: each unnecessary promotion (valley call that would finish
  at 30–40s) wastes ~$0.013 in re-issuing the call. At 10% of ~2,400
  calls/day = ~240 valley calls/day × $0.013 = ~$3.12/day in wasted
  promotions. This is a tolerable cost for the responsiveness benefit.

## Limitations

1. **Inter-call intervals include tool execution time.** The actual LLM
   API latency is a subset of the inter-call interval. Without per-line
   timestamps in the supervisor log, pure LLM latency cannot be directly
   measured. The inter-call interval is an upper bound on LLM latency.

2. **Model mix shifted over the period.** kimi-k3 ran Sep 2–3; glm-5.2
   ran Sep 3–4. The per-model breakdown accounts for this, but the
   combined distribution is less clean than either model alone.

3. **No direct BEFORE→AFTER timing.** The log lacks timestamps on
   individual print statements. Adding `time.time()` stamps to the
   `BEFORE LLM` and `AFTER LLM` print statements would enable
   direct LLM latency measurement in future analysis.

4. **Tool execution time is not separated.** Some tool calls (e.g.,
   running Python scripts for ECAN tuning) may take 10–30s,
   contributing to the inter-call interval independently of LLM
   latency. The completion-token stratification partially controls
   for this but does not fully isolate LLM time.

## Conclusion

The bimodal hypothesis is **partially confirmed** — there is a fast mode
(~20s, 61% of calls) and a slow mode (~52s, 39% of calls), but the valley
between them (30–40s, 10% of calls) is not empty. **T=30s is well-calibrated**
for the current model (z-ai/glm-5.2): it sits just above the fast p95 (27s),
reliably captures the slow mode, and the valley misprediction cost (~$3/day,
~10% of calls) is tolerable. **No change to T is recommended.**
