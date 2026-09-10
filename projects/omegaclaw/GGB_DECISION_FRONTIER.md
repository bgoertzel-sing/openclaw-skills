# Protobots GGB Decision Frontier

- Updated: `2026-08-11 23:37 UTC`
- Purpose: keep currently blocked empirical gates precise and prevent an
  approval for evidence generation from being interpreted as runtime authority.

## D1 — Capacity 1.1 held-out execution

- Decision owner: Ben
- Requested decision: authorize or decline exactly one reveal and execution of
  sealed cases `A09`--`A12` against the frozen request-to-contract candidate.
- Candidate SHA-256:
  `df182ee8cafab2a7356352375916e06c2b1e39a60aae61378bb918fb39a27126`
- Preflight:
  `artifacts/ggb-capacity-gates/20260810-heldout-authorization-preflight/`
- Latest replay: `2026-08-11 07:36 UTC`; direct checker, all five fail-closed
  unit tests, and Python compilation passed. Authority flags remained false.
- Pass evidence required: all four cases execute through the content-bound v0.6
  Bubblewrap chain; the exact score and per-case results are recorded; candidate,
  commitment, encrypted sealed copy, or sandbox drift fails closed.
- Explicitly not authorized: adopting the harness; editing ThreadKeeper PR #1;
  dispatch; memory writes; GoalChainer wiring; providers; Telegram; or any live
  runtime behavior change.
- If declined or unanswered: keep the sealed bytes encrypted and unexecuted.

## D2 — Capacity 1.2 deterministic materialization

- Decision owner: Ben
- Requested decision: authorize or decline one provider-free execution of the
  reviewed deterministic generator at the already bound `64/32` scope.
- Preflight:
  `artifacts/ggb-capacity-gates/20260729-motivation-score-policy-v02-materialization-preflight/`
- Decision-receipt contract:
  `artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/`
- Latest contract replay: `2026-08-11 23:37 UTC`; all nine fail-closed unit
  tests, compilation, and the five-file GGB fixture checker passed. No receipt
  or dataset was created.
- Pass evidence required: exactly 64 development and 32 confirmation records;
  preregistered split, family, boundary, and uniqueness invariants pass; output
  identities and replay command are recorded.
- Explicitly not authorized: fitting or calibration; changing score parameters;
  memory writes; ThreadKeeper effects; GoalChainer or Protomegabot integration;
  providers; Telegram; or runtime behavior changes.
- If declined or unanswered: do not materialize the dataset.

## Ordering and independence

`D1` is the nearer intelligence gate because it scores the already frozen
Capacity 1.1 candidate. `D2` is independent and may be decided separately; it
only creates offline evidence for later motivation-policy evaluation. Neither
decision implies the other, and neither can authorize deployment.

After a passing D1, the next decision is whether to adopt the candidate/harness
for further non-live evaluation. After a passing D2, the next step is an
independent identity and invariant replay before any analysis or calibration.
