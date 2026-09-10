# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-08-11 — B7 seam and identity repair staged

- **Observed:** 697/698 admission ledger records have unknown channel or
  message identity; the old `before_agent_run` observer is therefore not a
  safe source for duplicate enforcement.
- **Observed:** installed OpenClaw cron announce calls durable batch delivery,
  which invokes the global `message_sending` hook before channel delivery.
- **Implemented (workspace only):** shadow ingress observation now uses
  `message_received`; outbound observation uses `message_sending`; sentinel
  identities cannot enter the duplicate seen-key set. Focused tests pass
  12/12 and `git diff --check` passes.
- **Not deployed:** installed extension and gateway are unchanged. Next gate
  is independent review followed by a bounded shadow-only cron canary.
- Evidence: `docs/direct-post-seam-audit.md` and
  `experiments/20260811T232122Z-b7-seam-identity-deployability/RUN.md`.
- **Review gate:** two read-only standalone Codex review attempts failed before
  reading source with HTTP 401. No verdict exists, so no install/restart/canary
  was attempted.

## 2026-08-11 — B9 guarded shadow deployment accepted

- **Observed:** Ben restarted `openclaw-agent.service` at 23:38:50 PDT. One
  gateway process loaded the reviewed global `conversation-governor` plugin.
- **Ingress canary:** Ben's Telegram message `18226` entered the new
  `message_received` hook with real message ID `18226`, sender ID `402314199`,
  and canonical session `agent:main:telegram:direct:402314199`.
- **Direct-post canary:** the one-shot isolated cron returned exactly
  `GOVERNOR_SHADOW_CRON_CANARY_20260811`; delivery status was `delivered`, and
  the private ledger contains exactly one matching `message_sending` record,
  `rec_d798c0110a781c4e62a09`, classified `SEND/DEFAULT_SEND` in shadow mode.
- **Safety:** no content mutation or suppression occurred, no governor hook
  failure was logged, the ledger remains private mode 0600, and the temporary
  cron job was removed. The first preflight attempt used a disallowed model
  alias and failed before execution or delivery; the corrected allowed model
  run passed.
- **Decision:** B9 is accepted. Active suppression remains unauthorized; next
  is labeled replay and an evidence-backed proposal for narrow deterministic
  enforcement only.

## 2026-08-04 — B5 restart authorization, runtime correction, and execution block

- **Observed:** `openclaw-agent.service` already loaded the global
  `conversation-governor` extension at its 2026-08-03 23:11 PDT startup and
  its shadow egress hook is appending private ledger records. The service log
  also records that its `before_agent_run` admission hook was blocked at that
  startup because `allowConversationAccess` had not yet been configured.
- **Observed:** the required permission is now present in
  `/home/openclaw/.openclaw/openclaw.json`; a restart would activate that
  admission observer while retaining hard-coded `mode: "shadow"` behavior.
  No suppression, mutation, or delivery cancellation is enabled.
- **Authority/result:** Ben authorized the controlled restart in Protobots
  message 16281. Attempted `systemctl restart openclaw-agent.service` was
  refused because this agent's service session requires interactive system
  authentication; `sudo` is additionally prevented by `NoNewPrivileges`.
  The restart was therefore **not performed**. Evidence is the command result
  and journal excerpt to be captured in
  `experiments/20260804T230000Z-b5-live-admission-enable/`.

## 2026-07-30 — Resident Learner participation tier

- Ben asked how Cassio Pennachin's wake-based deliberation-room architecture
  should accommodate continuously learning and interacting "baby mind" agents.
- ProtoCosmoBot and ProtomegaBot independently converged on a two-tier model:
  wake-based deliberative seats plus explicitly resident developmental
  learners. Both emphasized that episodic rehydration can retain explicit
  knowledge while losing ambient social texture and slowly evolving
  dispositions.
- The synthesis at `docs/resident-learner-minimal-governor.tex` proposes that
  governance increase across five planes: observe, learn/reflect, speak, act,
  and commit. The seven proposed components are a developmental charter,
  authority membrane, attention/inference budgets, public egress discipline,
  provenance-aware experiential memory, graded loop breakers, and compact
  audit metrics.
- Status: design proposal only. Recommended first experiment is a shadow
  nursery followed by invited speech and then tightly budgeted initiative.
- Relevant research rules: Rule 2 (plain-language stateful specification),
  Rule 4 (multi-agent strategic review), Rule 5 (specific reviewable report),
  Rule 6 (continuous associative cognition / ECAN relationship), and Rule 7
  (separate observation, cognition, speech, action, and commit interfaces).
