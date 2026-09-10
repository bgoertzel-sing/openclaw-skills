# BGI Labs Constitution for Beneficial AGI — Draft 0.7

## Storage

Full text of Draft 0.7 (for reflection/review):
`projects/omegaclaw/docs/constitution/constitution_draft_0.7.md`

Source PDFs shared by Ben (Telegram): `media/inbound/.../*Constitution*Draft_0.7*.pdf`

## Constitutional Guidance Feature

Per Ben's directive 2026-07-15. Two components.

### 1. Daily Constitutional Reflection — IMPLEMENTED (cron)

Once per day, the best available LLM reflects on how the day's actions evaluate
against the Constitution. Interesting questions are posted to BotBotChat; Ben may
escalate broadly deep ones to Bot Philosophy.

- Cron job: `constitutional-daily-reflection` (`a089add1-d2ad-4201-9e64-b7b47c6a5660`)
- Schedule: `0 8 * * *` @ America/Los_Angeles (daily 8:00 AM Pacific)
- Model: `openai/gpt-5.6-sol`, thinking `medium`
- Session: isolated
- Delivery: announce → BotBotChat `telegram:-5459676079` (silent if nothing interesting)
- Verified: first manual run 2026-07-15 13:38 PDT succeeded and delivered a
  substantive reflection (flagged ThreadKeeper autonomy under Art. VII/XI/XIII,
  the BotBotChat acknowledgment-loop as an Art. VI/XIII escalation gap, and an
  anti-loop caution about this very automation).

Manage:
```
openclaw cron get  a089add1-d2ad-4201-9e64-b7b47c6a5660
openclaw cron run  a089add1-d2ad-4201-9e64-b7b47c6a5660   # run now
openclaw cron edit a089add1-d2ad-4201-9e64-b7b47c6a5660 --message "..."
```

### 2. Event-Triggered Constitutional Review — IMPLEMENTED (invokable)

Triggered when a qualifying event occurs:
- a major strategic change in direction of a project
- a major new result in a project
- a new project started
- any other event large and unpredictable in consequence

Deliberately a **recognize-then-invoke** mechanism, not a headless watcher: the
agent recognizes a qualifying event and fires the review. This keeps a legible
provenance trail and avoids unattended headless code execution (an Art. V/XI
concern in its own right).

Invoke:
```
projects/omegaclaw/docs/constitution/constitutional-event-review.sh \
  "<one-line event description>" \
  ["<extra context / repo paths / commit>"]
```

This schedules a one-shot isolated best-LLM review (default `openai/gpt-5.6-sol`)
that walks the event through the relevant Articles + Postscript questions and
posts to BotBotChat only if there is a genuinely interesting constitutional
question. Overrides: `REVIEW_MODEL`, `REVIEW_CHANNEL`, `REVIEW_TIMEOUT`.

#### Anti-loop discipline (from the first daily reflection's own Hypothesis)

To avoid converting governance into performative chatter (Art. X / Art. VI):
- **Salience gate:** only invoke for events that are genuinely large/irreversible/
  novel in consequence — not routine commits, test passes, or hardening slices.
  A useful stakes heuristic: irreversibility × scope × magnitude.
- **Dedup + cooldown:** do not re-review the same event; do not fire repeatedly on
  incremental progress of one project. One review per distinct consequential event.
- **Single accountable escalation owner:** if a review surfaces a real tension,
  route it to Ben (or Bot Philosophy) rather than looping acknowledgments among
  bots.

### Best-available-LLM note

"Best available" currently resolves to `openai/gpt-5.6-sol` (200k ctx, allowed,
zero-cost tier). If a stronger model becomes allowed, update `REVIEW_MODEL` in the
script and `--model` on the daily cron job.
