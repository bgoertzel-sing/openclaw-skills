# OmegaClaw GoalChainer integration map

- Date: 2026-07-02
- Source repo: `https://github.com/MesTTo/OmegaClaw-GoalChainer`
- Local inspection clone: `projects/omegaclaw/repos/OmegaClaw-GoalChainer`
- Inspected commit: `23f49515b1556ce04981f74bde4b56ee0a4375c6`
- Status: external exploratory source only; no live Protomegabot/OmegaClaw runtime integration has been made. A topology boundary note now recommends queue-mediated/adjudicated integration before any live bridge changes.

## What GoalChainer appears to provide

GoalChainer is a goal-aware decision layer for OmegaClaw-like agents. Its advertised pipeline is:

1. parse a natural-language request into evidence signals / Semantic-Hypergraph-style propositions;
2. derive deontic status for candidate actions (`forbidden`, `obligated`, `permitted`);
3. grade action acceptability through PeTTaChainer/PLN-style evidence;
4. apply SNARS-style subjective-logic verdicts and proof/provenance;
5. reconcile individual and collective goal pressures with a MetaMo/OpenPsi/MAGUS motivation layer;
6. expose the selected action as an OmegaClaw directive / claimable task.

The concrete demo domain is incident response: choose between publishing raw logs, publishing a redacted summary, or holding updates. The intended safe recommendation is the redacted summary when sensitive data is present.

## Interfaces relevant to Protomegabot

| Interface | Repo location | Candidate Protomegabot use | Integration posture |
|---|---|---|---|
| Python CLI / library | `src/goal_chainer/cli.py`, `pipeline.py`, `omegaclaw_skill.py` | Non-live decision experiments over bounded text requests | Safe to run as local tests only |
| OmegaClaw skill surface | `integrations/omegaclaw/goalchainer_skill.metta`, `run_in_omegaclaw.metta` | Future `goalchainer-decision`, `goalchainer-motivation`, `goalchainer-directive` tools | Do not load into live Protomegabot without explicit approval |
| PeTTa runtime bridge | `src/goal_chainer/petta_runtime.py` | Reuse local PeTTa/SWI paths already present under `projects/omegaclaw/` | Needs path/env hardening and bounded timeouts before live use |
| PeTTaChainer bridge | `src/goal_chainer/evidence_chainer.py` | Potential bridge from `petta-memory` EvidencePacket/STV exports into acceptability queries | Currently hits the same compile/add stack bottleneck seen in `petta-memory` profiling |
| MetaMo motivation | `src/goal_chainer/motivation.py`, `docs/metamo-integration-plan.md` | Model individual/collective drives and appraisal before task claiming | Useful design pattern; first gate should be one-shot/non-live |
| Directive mapping | `src/goal_chainer/directive.py`, `integrations/prolog/gc_directive.pl` | Turn deontic status into ready/blocked/backlog task state | One local test currently fails; needs diagnosis before adoption |

## Relationship to existing work

- **GGB roadmap:** maps most directly to capacities 2.2 claim/evidence separation, 2.5 architecture proposal, 3.1 multi-step planning, 4.3 shared memory coordination, 5.1 governance boundaries, and 5.5 self-improvement loop governance.
- **`petta-memory`:** can supply bounded, provenance-carrying evidence packets and prompt/index views; GoalChainer could consume selected promoted facts as appraisal/evidence inputs rather than reading live memory directly.
- **PeTTaChainer bottleneck:** local tests with `GOALCHAINER_PETTACHAINER_DIR=projects/petta-memory/repos/PeTTaChainer` reproduce a PeTTaChainer `compileadd` 8 GB stack-limit failure on a small four-rule GoalChainer query, matching the current `petta-memory` profiling concern.
- **OmegaClaw/ThreadKeeper:** GoalChainer's directive output is a candidate upstream task-claim signal, but ThreadKeeper should remain the bounded delegation/record layer; do not let GoalChainer bypass task contracts, allowed paths, quotas, or transcript records.
- **MetaMo/Hyperseed motivation analysis:** GoalChainer fits the suggested separation between appraisal/evidence/context update and decision/task selection, with a bounded feedback law between them. The first implementation should be a crude PLN/heuristic gate, not rigorous self-modification verification.

## Non-live smoke gate proposal

Goal: prove a bounded request can produce a decision payload without touching live Telegram/OmegaClaw runtime state.

1. Pin repo commit and runtime paths.
2. Run offline/unit tests and record pass/fail split.
3. Configure local PeTTa/SWI and PeTTaChainer paths explicitly.
4. Run one demo request through `goalchainer-decision` or equivalent Python API under a timeout.
5. Confirm output includes: ranked actions, deontic status, motivation summary, evidence/proof pointer, and directive/task-state mapping.
6. Feed at most one hand-picked `petta-memory` fixture/export as read-only evidence; no live memory writes.
7. Archive a GGB gate record before any runtime integration discussion.

## Current gate result (updated 2026-07-07 03:34 UTC)

Full pipeline now runs end-to-end with heuristic PLN fallback, including through the OmegaClaw MeTTa skill surface, and now bridges `petta-memory` promoted evidence packets into the heuristic belief grader:

- Clone/inspection succeeded at commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`.
- `omegaclaw-deontic` package cloned and installed; deontic and directive layers work correctly.
- `derive_deontic` returns correct statuses; `register_directive` returns correct task states and claims.
- Heuristic PLN belief grader (`heuristic_beliefs.py`) bypasses the PeTTaChainer `compileadd` bottleneck using subjective-logic fusion on the same PLN rule semantics.
- Full `solve_incident` pipeline runs end-to-end and returns `publish_redacted_summary` as recommended, `publish_raw_log` as blocked/forbidden, `hold_external_update` as weak/permitted.
- Full test suite: `87 passed, 6 skipped, 0 failed` (up from `53 passed, 6 skipped, 0 failed`; +34 multi-scenario tests).
- Multi-scenario smoke: 34 tests across 4 baseline incident types (PII standard, public data, unverified facts, public+unverified) and 4 conflicting-memory variants. All 4 baseline scenarios produce distinct belief-strength profiles. Deontic layer is never overridden by memory evidence, even with STV 0.99/0.99 + EC 99:1. Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-multi-scenario-smoke/`.
- Automatic fallback detects PeTTaChainer unavailability and skips the 30s timeout via a module-level failure cache and `_pettachainer_available()` quick check.
- `petta_runtime.py` now has a 30s subprocess timeout with `TimeoutExpired` handling.
- `belief_source` metadata clearly marks when the heuristic fallback was used.
- **Memory-evidence bridge implemented**: `grade_beliefs_heuristic_with_memory()` accepts optional `petta-memory` handoff cache items (STV atoms via `parse_memory_evidence()` and EvidencePacket EC atoms) and fuses them with keyword-derived ground facts using the same subjective-logic combination rule. Memory grounds use their own strength/confidence directly (no rule-chain product). The bridge is wired through `reason_over_hyperbase()` and `solve_incident()` via optional `memory_items` parameters. 18 new tests pass; full suite 53 passed, 6 skipped, 0 failed. `petta-memory` 6 passed, 0 failed (no regressions). Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-memory-evidence-bridge/`.
- **petta-memory handoff smoke now probes the real heuristic-with-memory path**: `run_goalchainer_precompiled_handoff_smoke(..., include_heuristic_memory_probe=True)` imports the local GoalChainer pipeline, parses handoff items with `parse_memory_evidence()`, and calls `solve_incident(memory_items=...)` while preserving the non-live boundary. CLI flag: `goalchainer-smoke --heuristic-memory-probe`. Checks: focused `tests.test_goalchainer_smoke` 7 passed; full `petta-memory` unittest suite 377 passed; `git diff --check` passed; runtime artifact `goalchainer_heuristic_memory_probe_2026-07-07T0334Z.json` sha256 `3e55ca9531ef93ecd4e2f5b8375d318aa53b1cf21d4e02f6ae92724b3bdeaa2f` reports `decided=publish_redacted_summary`, `memory_proof_present=True`, `leak_check_safe=True`. Archived `artifacts/ggb-capacity-gates/20260706-petta-memory-goalchainer-heuristic-probe/`.
- **OmegaClaw skill surface smoke passed**: both Python CLI (`omegaclaw_skill.py`) and MeTTa skill surface (`run_in_omegaclaw.metta` via PeTTa/SWI) produce correct decisions. The MeTTa path loads OmegaClaw Core skills, registers GoalChainer skills, and evaluates `(eval (goalchainer-decision ...))` and `(eval (goalchainer-solve ...))` successfully. Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-skill-surface-smoke/`.

## Topology boundary update (2026-07-07 07:35 UTC)

Drafted `projects/omegaclaw/docs/omegaclaw_zerobot_topology_decision_note.md` and gate `artifacts/ggb-capacity-gates/20260707-topology-boundary-review/`. Recommendation: use GoalChainer first as a read-only decision sidecar over bounded task text plus selected `petta-memory` handoff packets; ThreadKeeper remains the queue/delegation/adjudication layer; accepted summaries are the only candidate egress to Telegram/OmegaClaw. Direct group or direct recursive OpenClaw bridges are deferred. No live runtime integration was made.

## Read-only sidecar update (2026-07-07 15:37 UTC)

Archived `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/`: a non-live sidecar harness read the accepted private ThreadKeeper/OpenClaw smoke record, constructed a bounded appraisal request, injected synthetic read-only `petta-memory` STV/EC handoff evidence, and called `solve_incident(memory_items=...)` with heuristic PLN forced. Result: 8/8 harness checks passed; baseline and memory-informed runs both recommended `publish_redacted_summary`; `publish_raw_log` remained forbidden/blocked; redacted-summary belief strength rose from `0.980529` to `0.996970`; raw-log strength dropped from `0.040000` to `0.012234`; leak check stayed safe. Focused GoalChainer memory tests passed (`52 passed`) with explicit local PeTTa/SWI paths. No Telegram message, provider call, runtime bridge, memory write, or supervisor launch occurred.

## Queue-sidecar contract update (2026-07-07 19:36 UTC)

Archived `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-contract/`: a non-live contract/spec gate for the next sidecar step. `sidecar_contract.json` defines a ThreadKeeper queued-task-compatible sidecar that accepts only bounded candidate text, selected read-only `petta-memory` evidence, and optional archived artifact paths; excludes live Telegram history, secrets/token files, unbounded raw transcripts, and writeable memory state; and returns only a `needs_adjudication` redacted-summary candidate. The draft task contract sets `requires_adjudication=true`, `patch_proposal_only=true`, one worker turn, `max_tool_calls=2`, narrow allowed paths, and explicit forbidden actions for Telegram posts, runtime bridge enablement, memory writes, secret access/printing, daemon install, and paid compute. Validation imported ThreadKeeper's `_validate_queued_dispatch_task()` and passed 10/10 invariant checks. No queue task was enqueued, worker/supervisor launched, provider called, Telegram message sent, or memory written.

## Offline adjudicator update (2026-07-08 03:58 UTC)

Archived `artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator/`: an artifact-only reviewer inspected the queue-sidecar output, queue result/report, sidecar contract, and prior private-smoke adjudication. It passed 12/12 checks and accepted the redacted-summary candidate (`Checkout payment retries are timing out.`) for offline evidence only. It explicitly does not approve Telegram posting, runtime bridge enablement, memory writes, provider calls, queue claims, supervisor launch, or broader live behavior changes.

## Reviewer policy/threshold update (2026-07-08 11:33 UTC)

Archived `artifacts/ggb-capacity-gates/20260708-goalchainer-reviewer-policy-thresholds/`: a reusable offline reviewer policy fixture (`reviewer_policy.json`) and validator (`validate_reviewer_policy.py`) now check future GoalChainer sidecar candidates against explicit thresholds and boundaries. The first replay over the accepted sidecar candidate passed 14/14 checks: status `needs_adjudication`, action `publish_redacted_summary`, raw log blocked/forbidden, leak-safe, candidate text bounded, required evidence IDs present, required non-actions preserved, live-scope flags false, redacted strength `0.996970 >= 0.95`, raw strength `0.012234 <= 0.05`, and redacted/raw margin `0.984736 >= 0.80`. No live runtime, Telegram, memory, provider, queue, supervisor, paid-compute, or security changes were made.

## Real petta-memory sidecar replay update (2026-07-09 20:15 UTC)

Archived `artifacts/ggb-capacity-gates/20260709-goalchainer-real-petta-memory-replay/`. This closes the synthetic-evidence gap in the earlier private-task sidecar: a 1,273-byte copy of the previously archived `live_goal_bridge_journal_2026-07-08T1830Z.metta` is loaded with `MediumMemoryStore`, exported through the production `goalchainer_handoff_cache()` contract, and narrowed to the promoted belief's two STV/EC items under a four-item cap, and supplied to `solve_incident(memory_items=...)` for one archived Protomegabot decision candidate. All selected STV/EC items retain belief, cluster, promotion-event/rule/domain/trust, source-kind, and boundary provenance. Harness passed 9/9; focused petta-memory tests passed 53, focused GoalChainer memory tests passed 52, full petta-memory tests passed 430, and journal SHA-256 was unchanged before/after. Result remained `publish_redacted_summary`; raw log remained forbidden/blocked; leak check remained safe. No live bridge, Telegram/provider/supervisor action, queue claim, memory write/promotion, secret access, paid compute, or push occurred.

Future work only: an explicitly bounded LLM may later parse selected relevant task text into logical expressions for reviewed AtomSpace insertion, with ECAN-like attention allocation and long-term-importance/staleness-based retention/removal. This gate does not implement or invoke that phase.

## Reviewer policy real-memory replay update (2026-07-09 23:34 UTC)

Archived `artifacts/ggb-capacity-gates/20260709-goalchainer-reviewer-policy-real-memory-replay/`: replayed the reusable offline reviewer policy from `20260708-goalchainer-reviewer-policy-thresholds` against the second candidate produced by the real `petta-memory` handoff replay gate. The artifact-local validator passed 15/15 checks: source gate passed, redacted-summary action/norm matched, raw log remained blocked/forbidden, redacted strength `0.997816` and raw strength `0.040000` met thresholds, margin was `0.957816`, leak check stayed safe, selected real-memory evidence was bounded at 2 STV/EC items, the journal hash stayed unchanged, and live boundary flags stayed false. Verdict remains offline evidence only: no Telegram post, runtime bridge, provider call, queue claim, supervisor launch, memory write/promotion, paid compute, or security/access change.

## Recommendation

The 2026-07-12 canary review-boundary gate found and closed a reusable-harness policy gap: a generic request could make raw-log publication recommended/permitted, after which the canary queued and accepted it without requiring adjudication. The exploratory canary now uses a sensitive-data fixture, checks forbidden norms before queueing, requires adjudication for every queued recommendation/candidate, remains patch-proposal-only, and limits offline acceptance to `publish_redacted_summary`. Three focused tests and an isolated fake-worker replay pass; evidence is archived at `artifacts/ggb-capacity-gates/20260712-goalchainer-canary-review-boundary/`. This does not authorize live egress.

GoalChainer is now functional end-to-end with the heuristic PLN fallback, producing correct decision payloads for the incident-response scenario through both the Python CLI and the actual OmegaClaw MeTTa skill surface. The memory-evidence bridge connects `petta-memory` promoted evidence to the heuristic belief grader via `grade_beliefs_heuristic_with_memory()`, and the `petta-memory` handoff smoke now optionally checks the actual `solve_incident(memory_items=...)` path from a fixture artifact. Multi-scenario smoke verifies differentiated decisions across 4 incident types and 4 conflicting-memory variants, confirming deontic invariants are never overridden by memory evidence. The read-only decision sidecar gate over a captured private ThreadKeeper task has passed, and the queue-mediated/adjudicated sidecar contract is now defined and schema-validated. The queue artifact/harness, offline adjudicator, and reusable reviewer policy/threshold fixture are now complete: the sidecar candidate was accepted for offline evidence only with no live authorization, and the same candidate passes explicit threshold/non-action/evidence checks. The next useful slice is replaying the policy on additional candidates, or explicit Ben approval for a private Telegram opt-in gate with stop conditions before any live bridge changes. The heuristic can serve as the default belief grader until PeTTaChainer's `compileadd` bottleneck is fixed upstream, and the `GOALCHAINER_USE_HEURISTIC_PLN` flag can force the heuristic path even when PeTTaChainer becomes available.
