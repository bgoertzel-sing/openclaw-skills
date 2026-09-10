---
name: "multi-provider-quota-cascade-runbook"
description: "Detect, mitigate, and prevent multi-provider model quota cascades across the OpenClaw fleet."
---

# Multi-provider quota-cascade runbook

## Purpose

Use when multiple sessions/cron lanes fail simultaneously with provider
rate-limit or quota errors, or when designing/auditing model routing for the
fleet. Distinguish a hard subscription quota (resets on a schedule) from a
per-minute throttle; the response differs.

## Detection signals

- Cluster of `FallbackSummaryError` / `chain_exhausted` across unrelated cron
  jobs and chat sessions within minutes of each other.
- Provider 429s containing a quota-reset timestamp (e.g. "usage limit. Next
  reset in N hours") rather than a short retry window.
- Gateway log shows a burst of runs at the same second after a gateway
  restart (post-restart catch-up: missed jobs fire together after a flat
  delay, no jitter — observed 2026-08-19, 27 jobs).
- "Model Fallback cleared" messages on sessions whose *primary* model is
  still the exhausted one — clearing a fallback does not change the primary.

## Immediate mitigation (ordered)

1. Identify the exhausted provider and the reset time from the gateway log;
  record both in the daily memory file.
2. Retarget routine cron lanes and affected agents to a *different provider
  family* (e.g. OpenRouter) with a same-family fallback. Batch the edits;
  back up config first (`openclaw.json.bak-<date>-<reason>`).
3. `/reset` stuck chat sessions so they inherit the new gateway default
  chain; clearing the fallback alone is insufficient.
4. If a chat agent is spam-looping from a poisoned context, stop its
  supervisor first, then repair (history excision, loop guards) before
  restart — do not let it keep burning the fallback provider.
5. Verify recovery with one live probe per restored route before declaring
  the incident mitigated.

## Standing prevention policy

- Every fallback chain must span at least two provider families, so one
  provider's quota failure cannot exhaust the whole chain.
- Routine cron/background traffic stays on cheap non-subscription models;
  reserve Codex/Claude subscription models for expert review lanes.
- Cron model pins are a fleet-wide coupling: audit them together (one config
  diff), never one job at a time during an incident.
- Known upstream gap: OpenClaw post-restart catch-up fires all missed jobs
  after a flat delay with no jitter knob. Mitigate by capping concurrent
  cron lanes or filing an upstream feature request for staggered catch-up.

## Restoration checklist (after quota reset)

1. Confirm the reset time passed; run one live probe per previously-exhausted
  route through the real gateway path.
2. Decide explicitly, with the owner, between: (a) restoring the recorded
  pre-incident pins, or (b) adopting the incident-time routing as the new
  standing policy. Do not drift into an undocumented hybrid.
3. When restoring, apply the prevention fix in the same edit
  (provider-family-diverse fallbacks).
4. Check any supervisor/watchdog cron that can restart an agent with a stale
  pinned config.
5. Record the final routing decision in the incident memory entry and the
  affected project records.

## Guardrails

- Never expose API keys or quota-account identifiers while gathering logs.
- Config changes go through the normal backup + review flow unless the owner
  declares an emergency; record either way.
- Do not treat recovery of the provider as evidence the root causes are
  fixed; thundering-herd and monoculture persist until addressed.

## Output

Report: exhausted provider(s) and reset time; affected lanes/agents; config
edits with backup paths; probe evidence; final routing decision and where it
is recorded; remaining prevention gaps.
