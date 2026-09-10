# Phase 0 Baseline — Instrumentation Report

Date: 2026-07-24
Agent measured: `protomegabot-opus` (ProtomegaTron, OpenClaw side)
Data: full local session-log history, 2026-07-14 → 2026-07-24
(1054 active transcripts + archived `.reset`/`.deleted` variants, 107M)
Instrument: `measure_baseline.sh` + `aggregate_baseline.py` (read-only; no
behavior change). Raw run-level data: `/tmp/phase0_runs.jsonl` (2989 runs).

## Definitions

- **Run**: the assistant LLM calls following one inbound user/event message,
  up to the next inbound message. Terminal text = last non-toolUse assistant
  text — what the channel would actually see.
- **No-op run**: terminal text ∈ {empty, `NO_REPLY`, `HEARTBEAT_OK`}
  (whitespace/case normalized).
- **Duplicate outbound**: consecutive runs in one session with identical
  non-noop terminal text.

## Headline numbers

| Metric | Value |
|---|---|
| Runs | 2,989 |
| LLM calls | 5,309 |
| Total cost | $54.43 |
| Total tokens | 199.6M |
| **No-op runs** | **1,281 (42.86%)** |
| **No-op LLM calls** | **1,368 (25.77%)** |
| No-op cost | $2.59 (4.75%) |
| No-op tokens | 18.93% |
| No-op kinds | `no_reply` ×1213, empty ×68 |
| Heartbeat-triggered runs | 0 (heartbeat file is comments-only; heartbeats skipped) |
| Duplicate outbound runs | 0 (0.00%) |

## Interpretation

- **Observed:** 42.9% of invocations produce nothing user-visible; they
  consume 18.9% of tokens (~25.8% of calls). This is the message-
  amplification budget the governor exists to recover — the waste is not
  the silent reply itself (often correct behavior in group channels) but
  the full LLM invocation required to decide on silence. Admission before
  inference is the right target.
- **Observed:** no-op runs are cheap per-run (4.75% of cost) — output
  tokens are tiny; the spend is context/input. A governor with semantic
  pre-filtering must therefore beat ~19% token savings to pay for itself;
  per correction #2 its own overhead is budgeted at <5% of tokens saved.
- **Observed:** zero consecutive duplicates and zero heartbeat invocations
  in this dataset. The duplicate-outbound leg of the go/no-go gate is not
  supported by my logs; the bot-bot channel duplication problem likely
  lives in the OmegaClaw/PeTTa side or in ZeroBot's logs, not here.

## Go/no-go gate evaluation (thresholds from roadmap)

- No-op invocation ≥ 20% of LLM calls: **MET (25.77%)** → proceed.
- Duplicate outbound ≥ 10%: not met (0%) — not needed, either leg suffices.
- False-silence < 2%: measurable only in Phase 1 (shadow mode).
- Governor overhead < 5% of tokens saved: measurable only in Phase 1+.

**Verdict: proceed to Phase A (discovery) and Phase 1 (shadow mode).**

## Limitations and next measurements

1. Single-agent coverage. The shared-channel noise problem involves three
   runtimes: this agent (measured), ZeroBot/OpenClaw, and the OmegaClaw
   PeTTa Telegram bot. Equivalent instruments should be run on the other
   two before Phase 2 scoping; ZeroBot-side measurement is ZeroBot's to
   run or explicitly delegate.
2. NO_REPLY intent is ambiguous from logs alone — some no-op runs are
   *correct* silences (lurking in group chats). Phase 1 shadow mode must
   sample and human-label to separate correct silence from wasted
   invocation that a cheap classifier could have preempted.
3. No channel-type breakdown yet: sessions.json mapping should be used to
   split group-channel vs DM runs; the governor matters most for groups.

## Provenance

- Trigger: Ben Goertzel, 2026-07-24 — "please start on phase 0 yes",
  following the OmegaHive conversation-governor design PDF review.
- Raw summary JSON: `/tmp/phase0_summary.json`.
