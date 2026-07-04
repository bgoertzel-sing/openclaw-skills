# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-04 - ThreadKeeper queued-task integer type hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `ac7dfd4` (`Reject coerced queued task integers`) as a narrow strict queue-schema validation slice.

Queued-worker validation now rejects checksum-valid queue records whose integer metadata is only coercible rather than actually JSON-integer typed: e.g. `max_turns: 1.5` or `max_chars: "1000"`. This closes a lenient Python `int(...)` path before any worker LLM call. Bad claimed tasks continue to fail closed as `queue_worker_error` and are retained as `*.failed` plus compact result audit sidecars.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`67 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - Intent router and cost telemetry prep for Anthropic API key

Ben said the Anthropic API key is likely to arrive by Tuesday and asked for intent-router machinery plus cost tracking before then. Updated local plugin `plugins/intent-model-router/` (enabled in OpenClaw config) so routing is explicit and Anthropic-ready without requiring the key yet.

Changes: `index.js` now has exported classification helpers, separate routine/deep/Anthropic intent tiers, conservative OmegaClaw/ProtomegaTron routing, configurable `anthropicModel` with `enableAnthropic` gate, optional long-prompt-to-Anthropic routing, and `llm_output` token/cost telemetry to JSONL. Cost records intentionally omit prompt/assistant content and include provider/model, usage counts, estimated USD when locally priced, and the router tier/reason. `openclaw.plugin.json` schema now exposes the new routing and cost-tracking settings.

Checks: `node --check plugins/intent-model-router/index.js`; transformed helper self-test for routine/deep/Anthropic/OmegaClaw classification and Anthropic cost estimate; `jq empty plugins/intent-model-router/openclaw.plugin.json`; `openclaw plugins list` shows `intent-model-router` enabled and Anthropic provider enabled. No Anthropic key was installed, no Gateway restart was performed, no secrets were touched, and no paid calls were made.

## 2026-07-04 - GGB roadmap refresh for queued-task schema validation

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the reusable ThreadKeeper hardening gate fixture after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at head `7628f49`. The roadmap now maps queued-task schema validation and queued task-contract schema validation into capacities 3.2 (bounded delegation), 4.5 (patch/adjudication/queue proposal discipline), and 5.2 (audit/accounting integrity).

Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `MANIFEST.metta`, `METRICS.metta`, and `SUMMARY.metta` so the gate artifact records checksum-valid-but-schema-invalid queued records failing closed before worker LLM calls: unexpected fields, unsafe/unbounded `run_id`, invalid/non-finite/boolean `queued_at`, malformed/oversized/NUL-containing `cancel_file`, malformed task-contract list fields, and non-finite/boolean `max_turns`/`max_chars`.

Checks: ThreadKeeper branch/evidence inspection (`git status`, `git log`), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`66 passed`), `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`, and `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gate fixtures. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper queued-task contract schema tightening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `7628f49` (`Tighten queued task contract schema`) as a strict queue/task-contract validation slice.

Queued-worker validation now rejects checksum-valid but schema-invalid queue records with non-finite/boolean numeric metadata (`queued_at`, `max_turns`, `max_chars`) and task-contract list fields that are not explicit string lists or contain NUL/non-string entries. This closes a Python/JSON edge where `NaN` or `true` could pass numeric checks, and where malformed contract list fields could be interpreted leniently before a queued worker LLM call. Bad claimed tasks continue to fail closed as `queue_worker_error` and are retained as `*.failed` plus compact result audit sidecars.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`66 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper queued-task strict schema validation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `7a1866d` (`Validate queued subagent task schema`) as a small queued-worker integrity/strict-validation slice.

Queued-worker task validation now fail-closes on unexpected queue-record fields, unsafe/unbounded `run_id`, invalid `queued_at`, or malformed/oversized/NUL-containing `cancel_file` metadata before any worker LLM call. This complements the existing required queue checksum sidecars: operators can intentionally update a queue task only by updating its checksum, but a checksum-valid task still must match the narrow schema consumed by `run_queued_dispatch(...)`. Bad claimed tasks remain retained as `*.failed` with compact result audit sidecars.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`64 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper optional-shell output controls

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `0cde0c7` (`Bound subagent shell output controls`) as a small strict tool/resource-bound hardening slice.

The optional allowlisted subagent `shell` tool now parses `OMEGACLAW_SUBAGENT_SHELL_OUTPUT_CAP` (default 4000) and `OMEGACLAW_SUBAGENT_SHELL_TIMEOUT_S` (default 30.0) with the same defensive env parsing used by other safety knobs. Shell stdout/stderr returns now include an explicit truncation marker when capped, instead of silently slicing output. This preserves disabled-by-default shell, command-name-only executable allowlist, argv-list/no-shell execution, workspace cwd, sanitized PATH/minimal env, no stdin, argv cap, timeout, and output cap behavior.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`63 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper optional-shell argv cap

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `30adb54` (`Bound optional subagent shell argv`) as a small strict tool-argument validation hardening slice.

The optional subagent `shell` tool now has `OMEGACLAW_SUBAGENT_SHELL_MAX_ARGV` (default 32, defensively parsed/clamped) and rejects overlong argv lists before subprocess launch. It also rejects NUL-containing argv tokens in the direct shell helper path. This preserves the existing disabled-by-default, allowlisted command-name-only, argv-list/no-shell, workspace-pinned `cwd`, sanitized `PATH`/minimal env, no-stdin, timeout, and output-cap guardrails while bounding another resource/argument surface.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`62 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper queued-task checksum sidecars

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `f916dfe` (`Verify queued subagent task checksums`) as a queue-integrity hardening slice.

Queue-only dispatch now writes a required `<queue-task>.sha256` sidecar and returns `queue_sha256_path` in the structured parent digest. `subagent.run_queued_dispatch(queue_path)` atomically claims the task, verifies the sidecar before validating the queued contract or calling the worker LLM, and fails closed on missing/mismatched checksums. Claimed bad/tampered tasks are retained as `*.failed` with compact `*.failed.result.json` and a fresh checksum sidecar for retained bytes when possible; successful claims leave `*.done` plus a checksum sidecar.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`61 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-03 - ThreadKeeper queue result-sidecar filtering

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `38ae193` (`Ignore queue result sidecars when draining`) as a small async-queue audit/backpressure correctness follow-up.

After the failed-claim retention slice, retained sidecars such as `*.failed.result.json` live beside pending `queue/*.json` tasks for audit. The pending queue listing/backpressure helpers now share `_is_pending_queue_task_name(...)`, which counts only live task records and ignores any retained `*.result.json` sidecars. This prevents failed/done audit records from being mistaken for fresh work or producing false queue backpressure. Focused regression coverage now asserts that a retained failed sidecar leaves zero pending queue tasks.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`52 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. Refreshed the GGB roadmap/gate fixture to head `38ae193`. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-03 - ThreadKeeper queued-worker failed-claim retention

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `5a472cd` (`Retain failed queued subagent claims`) as a small audit/integrity follow-up to the queued-worker primitive.

`subagent.run_queued_dispatch(queue_path)` now keeps queue failure records auditable after atomic claim: if queued JSON/shape validation or execution fails after `queue/*.json` is renamed to `*.claimed`, the helper moves the task to `*.failed` and writes a compact `*.failed.result.json` sidecar. This prevents malformed claimed tasks from lingering in an ambiguous limbo state or disappearing without a result record. Path-escape errors before claim still return structured `queue_worker_error` without touching out-of-queue files.

Updated `docs/reference-skills-subagent.md`, focused mock coverage, `GGB_CAPACITIES_ROADMAP.md`, and the ThreadKeeper GGB gate fixture (`RUN.md`, `MANIFEST.metta`, `METRICS.metta`, `SUMMARY.metta`) to reflect head `5a472cd` and 52 focused mock tests.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`52 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - GGB roadmap refresh for queued-worker primitive and bounded drain

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the ThreadKeeper hardening gate fixture after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at head `ec17402`. The roadmap now maps the queued-worker primitive (`run_queued_dispatch(queue_path)`) and bounded operator-supervised drain helper (`drain_queued_dispatches(max_tasks=1)`) into GGB capacities 3.2 and 4.5 while preserving the explicit non-live boundary: no daemon, no polling loop, no self-scheduling, and no OmegaClaw/Telegram runtime behavior change.

Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `MANIFEST.metta`, `METRICS.metta`, and `SUMMARY.metta` so the reusable gate artifact reflects ThreadKeeper head `ec17402`, queued-worker commit `8eae787`, bounded-drain commit `ec17402`, and focused mock pytest evidence of 51 passing tests.

Checks: ThreadKeeper branch/evidence inspection (`git status`, `git log`, grep for `run_queued_dispatch`/`drain_queued_dispatches`), `git diff --check` in ThreadKeeper, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`51 passed`), `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`, and `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gate fixtures. No live OmegaClaw/Telegram/runtime integration, secrets/access/security setting changes, paid compute, merge, or force-push.

## 2026-07-03 - GGB roadmap refresh for queue-only/adjudication evidence

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the archived ThreadKeeper hardening gate fixture after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at documentation head `1c001e4`, code head `09899a0`, and queue-only feature commit `a33b1e3`. The roadmap now maps queue-only durable dispatch records/backpressure into GGB capacity 3.2 (bounded delegation) and reinforces capacity 4.5 evidence for parent-side review/adjudication. No live runtime integration was made: queue-only still only persists task records, and adjudication only marks a candidate output for parent/supervisor review.

Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `METRICS.metta`, and `SUMMARY.metta` so the reusable gate artifact reflects queue-only dispatch, optional adjudication, documentation head `1c001e4`, and 47 focused mock tests.

Checks: ThreadKeeper branch/evidence inspection (`git status`, `git log`, grep for `queue_path`/`queue_sha256`/`requires_adjudication`/`adjudication`), `git diff --check` in ThreadKeeper, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`47 passed`), `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`, and `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gate fixtures. No live OmegaClaw/Telegram/runtime integration, secrets/access/security setting changes, paid compute, merge, or force-push.

## 2026-07-03 - ThreadKeeper optional adjudicator gate

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `09899a0` (`Add optional adjudicator gate for high-stakes subagent outputs`) as the final Phase 3 candidate slice: when a JSON/persona task contract sets `requires_adjudication: true`, the subagent runs its normal worker loop, but the final `emit` is treated as a candidate output rather than an accepted result.

The transcript records `status=adjudication_required` with `candidate_summary` and `candidate_turn`. The structured parent digest returns `status=needs_adjudication` with bounded `adjudication` metadata (`required`, `status`, `candidate_summary`). No second LLM call is made inside the dispatch loop—the parent/supervisor must route the candidate to an adjudicator before accepting it. The child prompt also receives an `ADJUDICATION_REQUIRED` notice so it knows its output is a candidate.

Pushed follow-up `1c001e4` to document the new field in `docs/reference-skills-subagent.md`, including the task-contract parameter description, return-field documentation, and a new failure-mode table row.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`47 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - ThreadKeeper queue-only async dispatch primitive

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `a33b1e3` (`Add queue-only subagent dispatch mode`) as the first async/backpressure Phase 3 slice: when `OMEGACLAW_SUBAGENT_QUEUE_ONLY=1`, dispatch still performs setup, task-contract, tool-subset, persona-prompt, escalation, and cancellation checks, then persists a durable `OMEGACLAW_SUBAGENT_RUN_DIR/queue/*.json` task record instead of initializing/calling the worker LLM. The structured parent digest returns `status=queued`, `queue_path`, and `queue_sha256`; the local transcript/index path remains the audit source. A bounded queue cap (`OMEGACLAW_SUBAGENT_MAX_QUEUED_DISPATCHES`, default 32) returns structured `queue_backpressure` before any worker call when full.

This is not yet a live async worker/supervisor; it is a reversible enqueue primitive that preserves contracts/cancellation/backpressure and lets a future consumer claim tasks safely.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`45 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - GGB roadmap/gate refresh for ThreadKeeper patch-proposal evidence

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the archived ThreadKeeper hardening gate fixture after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at head `f77ac1b`. The roadmap now maps `patch_proposal_only` task contracts to GGB capacity 4.5 (patch proposal/adjudication): child `write-file`/`append-file` calls can record full proposed changes in transcripts without mutating workspace files, and the parent digest exposes bounded proposal metadata for review/test/apply. This remains non-live/local evidence only; parent-side review/apply/adjudication and PR/CI are still separate coordination steps.

Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `METRICS.metta`, and `SUMMARY.metta` so the reusable GGB gate artifact reflects ThreadKeeper head `f77ac1b`, 43 focused mock tests, and the new patch-proposal-only check.

Checks: ThreadKeeper branch/evidence inspection (`git status`, `git log`, grep for `patch_proposal_only`/`patch_proposals`), `git diff --check` in ThreadKeeper, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`43 passed`), `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`, and `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gate fixtures. No live OmegaClaw/Telegram/runtime integration, secrets/access/security setting changes, paid compute, merge, or force-push.

## 2026-07-03 - ThreadKeeper patch-proposal-only task contracts

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `f77ac1b` (`Add subagent patch proposal mode`) as a small Phase 3 parent-review hardening slice: JSON/persona task contracts may now set strict boolean `patch_proposal_only`; when enabled, subagent `write-file` and `append-file` calls pass normal tool/path/contract validation but do not mutate workspace files. Instead, the transcript stores full `patch_proposals` entries (`action`, `path`, `content`) and the structured parent digest exposes bounded `{action, path}` metadata, leaving review/tests/application to the parent/supervisor.

Added focused tests for no-write proposal capture and fail-closed non-boolean contract validation; updated `docs/reference-skills-subagent.md` with the new task-contract field, return field, and failure/mode notes.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`43 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - GGB roadmap/gate refresh for ThreadKeeper Phase 3 evidence

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the archived ThreadKeeper hardening gate fixture after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at head `554fb85`. The roadmap now maps dispatch wall-clock timeout to bounded delegation (3.2), worker token accounting to budget/cost awareness (3.5), and transcript checksum/index/token-accounting evidence to audit/accounting integrity (5.2). Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `METRICS.metta`, and `SUMMARY.metta` so the reusable GGB gate artifact reflects the current 40-test local focused pytest gate rather than stale 32/37-test evidence.

Checks: ThreadKeeper branch/evidence inspection (`git status`, `git log`, grep for `worker_token_usage`/`dispatch_timeout`), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`40 passed`), and `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gate fixtures. No live OmegaClaw/Telegram/runtime integration, secrets/access/security setting changes, paid compute, merge, or force-push.

## 2026-07-03 - ThreadKeeper dispatch wall-clock timeout and worker token accounting

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `554fb85` as a Phase 3 audit/accounting hardening slice with two features:

1. **Dispatch-level wall-clock timeout** (`OMEGACLAW_SUBAGENT_DISPATCH_TIMEOUT_S`, default 600s): checked before each LLM call and tool execution in the dispatch loop. Even if individual LLM calls are bounded by `_SUBAGENT_LLM_TIMEOUT_S`, a subagent making many fast calls could run for a very long time. On timeout, dispatch returns a structured `dispatch_timeout` record with `status=error` and persists the transcript. Set to `0` to disable.

2. **Worker token accounting**: `_call_subagent_llm` now returns `(text, in_tokens, out_tokens)` tuples instead of just text, capturing token counts from both Ollama native (`prompt_eval_count`/`eval_count`) and OpenAI-compatible (`prompt_tokens`/`completion_tokens`) provider paths. The dispatch loop aggregates `total_in_tokens`/`total_out_tokens` across all worker LLM calls and stores them in the transcript run record as `worker_token_usage` (`input_tokens`, `output_tokens`, `total_tokens`). The structured parent digest also includes `worker_token_usage` when any worker LLM calls were made, strengthening audit and cost accounting. It is omitted from the structured return when no worker LLM calls were made (e.g., setup errors before the loop).

Added focused tests: `test_dispatch_wall_clock_timeout_stops_before_llm` (patches `_dispatch_timeout_exceeded` to return True, verifies structured `dispatch_timeout` return and transcript status) and `test_worker_token_usage_aggregated_in_structured_return` (verifies input/output/total token aggregation across two LLM calls in a dispatch, both in transcript and structured return). Updated existing test mocks to handle the new tuple return from `_call_subagent_llm`. Updated `docs/reference-skills-subagent.md` with the new env knob, failure mode, and `worker_token_usage` field documentation.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`40 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - GoalChainer gate sibling fixture

Added `.metta` sibling fixture files for the non-live GoalChainer incident harness gate under `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/`: `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, and `SUMMARY.metta`. This extends the GGB run-contract fixture pattern to goal-arbitration/motivation evidence while keeping the integration boundary explicit: no OmegaClaw skill loaded, no Telegram/runtime behavior changed, and no live adoption implied. Refreshed `GGB_CAPACITIES_ROADMAP.md` to record four checkable fixture examples across `petta-chem`, ThreadKeeper, `petta-memory`, and GoalChainer.

Checks: `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py projects/omegaclaw/local/run-goalchainer-incident-harness.py`; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` across the GoalChainer, petta-chem, ThreadKeeper, and petta-memory gate fixtures passed. No paid compute, runtime/Telegram, secrets/access/security settings, live GoalChainer integration, push, merge, or force-push.

## 2026-07-02 - ThreadKeeper per-turn tool quota hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `94d57c9` (`Cap subagent tool calls per turn`) as a small quota/strict-dispatch hardening slice: subagent tool execution is now capped per worker response via `OMEGACLAW_SUBAGENT_MAX_TOOL_CALLS_PER_TURN` (default `3`, defensively parsed/clamped). If a worker emits more parsed non-`emit` calls in one response, dispatch stops before executing the extra call, returns structured `TURN_QUOTA_EXCEEDED`, and persists transcript status `turn_quota_exceeded`. This complements the existing per-dispatch quota and task-contract `max_tool_calls` narrowing so one malformed turn cannot spend the whole dispatch quota in a single batch.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`37 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - GoalChainer bounded incident harness

Built `projects/omegaclaw/local/run-goalchainer-incident-harness.py` as the next non-live GoalChainer gate. The harness runs one incident-response decision report with explicit local PeTTa/SWI paths and a documented heuristic acceptability fallback, intentionally bypassing the known PeTTaChainer `compileadd` bottleneck rather than loading any OmegaClaw skill or touching Telegram/runtime state. Archived the result at `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/` (`RUN.md`, `report.json`).

Result: the bounded report recommends `publish_redacted_summary`; relation-level Prolog directive classification maps `forbidden -> blocked`, `obligated -> ready`, and `permitted -> backlog`. Remaining runtime seams are now sharper: local `derive_deontic` returned only `unregulated` statuses for the incident request, so the harness used the same policy fallback encoded by `deontic_engine.build_theory`; and the generated OmegaClaw `lib_directive` plan still returns empty status/next lists plus an error-shaped claim response despite correct relation-level classification.

Checks: `python3 -m py_compile projects/omegaclaw/local/run-goalchainer-incident-harness.py`; harness run writing `report.json` passed. No paid compute, runtime/Telegram, secrets/access/security settings, live GoalChainer integration, push, merge, or force-push.

## 2026-07-02 - ThreadKeeper shell executable path hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `8e12b18` (`Restrict subagent shell executable paths`) as a small strict tool-argument validation follow-up: the optional subagent `shell` tool remains disabled by default, argv-only, executable-allowlisted, no-stdin, and workspace-cwd-bound, and now rejects explicit executable paths such as `/tmp/ls` or `/usr/bin/python` even if the basename is allowlisted. Subagents must invoke allowlisted command names only.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`34 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper numeric env parsing hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `24bf6bf` (`Harden subagent numeric env parsing`) as a small configuration-integrity slice: numeric subagent safety knobs now parse through bounded helpers, so malformed env values fall back to documented defaults and below-minimum values clamp instead of crashing module import or accidentally disabling timeout/retry, quota, digest, contract, or validation guards. Updated the subagent reference docs, focused regression coverage, and the ThreadKeeper GGB roadmap/gate fixture evidence.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`32 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - GGB roadmap refresh after provider-fail-closed and PeTTaChainer profiling

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the ThreadKeeper hardening gate fixture after the latest local related-project progress. ThreadKeeper branch `agent/threadkeeper-hardening-next` is now at `c3e836b` with provider setup failing closed as structured `provider_invalid` records, and focused mock pytest passes 31 tests via `projects/omegaclaw/local/threadkeeper-pytest-venv`. The ThreadKeeper gate sibling fixture now records head `c3e836b` and 31 focused tests.

Also updated the memory roadmap status from a pending PeTTaChainer runtime choice to the current evidence: `petta-memory` has local SWI/Janus/PeTTaChainer smoke validation, STV/EvidencePacket export, bounded profiling, and 67 stdlib unit tests passing. Current blocker/next task is narrower: instrument PeTTaChainer compile/add internals or add a precompiled/minimal-rule path because add-only proof/contextual packet stages time out before query isolation.

Checks run: ThreadKeeper `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused ThreadKeeper pytest (`31 passed`); `petta-memory` unittest (`67 passed`); `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`; GGB fixture checker across petta-chem, ThreadKeeper, and petta-memory gates; trailing-whitespace scan for touched OmegaClaw roadmap/gate files. No runtime/Telegram, secrets/access/security settings, paid compute, push, merge, or ThreadKeeper PR #1 changes were made.

## 2026-07-02 - ThreadKeeper run-record index hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `d8b922f` (`Index subagent run records`) as a small persistent-record/auditability slice: when a subagent run finishes and writes its transcript plus `.sha256` sidecar, it now appends a compact JSONL entry to `OMEGACLAW_SUBAGENT_RUN_DIR/index.jsonl`. Entries include run id, persona key, status, timestamps, transcript path, and transcript SHA-256; appends use a sidecar `fcntl` lock for cross-process writers where available. The parent still receives only the bounded structured digest.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`30 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.


## 2026-07-02 - petta-memory GGB gate sibling fixture

Applied the GGB `.metta` sibling fixture pattern to the `petta-memory` OmegaClaw-style prompt/index gate at `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/`. Added `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, and `SUMMARY.metta` to serialize the non-live/read-only memory gate as run-contract-shaped evidence atoms. This is the third checkable GGB gate fixture, after `petta-chem` and ThreadKeeper.

Also improved `local/check-ggb-gate-fixtures.py` so it recognizes both `## Checks run` and plain `## Checks` sections and common code-block command lines. Verification: `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py` passed; the checker passes on all three sibling fixtures; `PYTHONPATH=src python3 -m unittest discover -s tests -v` in `projects/petta-memory/repos/petta-memory` passed 64 tests. No live OmegaClaw runtime, Telegram state, secrets/access/security settings, paid compute, push, merge, or ThreadKeeper PR #1 changes were made.

## 2026-07-02 - ThreadKeeper task-contract quota narrowing

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `1d30b4b` (`Allow task contracts to narrow subagent tool quotas`) as a small quota/task-contract hardening slice: JSON/persona task contracts may now include optional `max_tool_calls`, validated as a strict non-negative integer before any worker LLM call. The dispatch loop clamps the effective tool-call quota to the lower of global `OMEGACLAW_SUBAGENT_MAX_TOOL_CALLS` and contract `max_tool_calls`, persists the normalized quota in transcripts, and shows it in child prompts. Docs were updated in `docs/reference-skills-subagent.md` and `memory/personas-subagent/README.md`.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`30 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper transcript checksum hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `0d1d0af` (`Add subagent transcript checksums`) as a small audit-integrity follow-up: finished subagent transcript records are still written atomically, and now get a local `<transcript>.sha256` sidecar. The structured parent digest also returns `transcript_sha256`, allowing the parent/supervisor to verify the saved transcript bytes later without expanding parent context.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`28 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper GGB gate sibling fixture

Applied the GGB `.metta` sibling fixture pattern to a second archived gate: `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/`. Added `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, and `SUMMARY.metta` to serialize the software-governance gate as run-contract-shaped evidence atoms. The fixture includes the ThreadKeeper task contract, PR #1 non-duplication constraints, branch/head provenance, RUN.md check coverage, current focused mock pytest evidence, uncertainty, and follow-up actions.

Verification: `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed 28 tests in `projects/omegaclaw/repos/ThreadKeeper`; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` passed on both `20260701-petta-chem-run-contract` and `20260701-threadkeeper-hardening`. This closes the previous next-small-task of applying the fixture/checker to a second archived gate. No runtime, Telegram, secret, access/security, push, merge, or PR #1 changes were made.

## 2026-07-01 - ThreadKeeper no-tool-subset structured setup records

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `caf3f9b` (`Structure no-tool subagent setup errors`) to close one remaining setup-failure record gap: dispatches with neither an explicit tool subset nor persona `default_tool_subset` now return the bounded structured JSON digest and persist a minimal transcript record with status `tool_subset_invalid`, instead of using the legacy raw error string and no transcript.

Checks: `git diff --check` passed; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct assertion replay confirmed the no-tool-subset path writes a transcript and does not call the worker LLM. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` was initially blocked because `/usr/bin/python3` had no `pytest` installed; resolved on 2026-07-02 by using `projects/omegaclaw/local/threadkeeper-pytest-venv` and commit `ca872e4`, which skips Docker post-session cleanup on hosts without Docker. Current focused mock pytest gate passes 28 tests.

## 2026-07-01 - GGB gate fixture smoke checker

Added `local/check-ggb-gate-fixtures.py`, a stdlib-only offline smoke checker for GGB capacity-gate `.metta` sibling fixtures. It verifies required fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`), balanced parentheses/strings after comments, exactly one top-level `run-summary`, and textual coverage between `RUN.md` checks and `ggb-check` atoms.

Archived the run at `artifacts/ggb-capacity-gates/20260702-ggb-fixture-smoke/RUN.md`. Verification passed on `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/`: required files balanced; one top-level `run-summary`; 3 `RUN.md` checks covered by 4 `ggb-check` atoms. `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py` and trailing-whitespace scan passed. The checker is intentionally not a full MeTTa/PeTTa parser; next step is applying the sibling-fixture pattern/checker to a second archived gate.

The roadmap was also refreshed with current related-project status: `petta-memory` has 53 stdlib tests and PeTTaChainer is the leading PLN runtime candidate pending local SWI/Janus/`petta` availability; `petta-chem` has PeTTa-side folded summaries through seed-37 and twenty-seven serialized exp02 run-contract records. No runtime, Telegram, secret, access, security, push, merge, or ThreadKeeper PR #1 changes were made.

## 2026-07-01 - OmegaSim feedback attachment captured for Hyperseed/OmegaHive design

Ben forwarded `omegasim feedback.txt` in the ProtomegaTron Telegram channel. The attachment argues that the OmegaSim negative result is mostly a queue-centric abstraction result, and recommends the next simulator add bounded thresholded cognitive appraisal rather than arbitrary logistic chaos. It prioritizes latent motivational state, semantic/artifact fields, prediction error, trust/provenance, fatigue/overload, adaptive thresholds, softmax action selection with sigmoidally gated appraisal inputs, costly prediction, hysteresis, artifact-handoff thresholds, and residual-state lobe discovery with linear/shuffled controls.

Primary durable design note was recorded in `projects/hyperseed-formalizations/NOTES.md`; follow-up task added to `projects/hyperseed-formalizations/TASKS.md` to revise/extend note 0004 and drive A6/A7/A8 experiment families. Source attachment: `/home/openclaw/tmp/omegaclaw-telegram-attachments/1782952328-file_7.txt.extracted.txt`.



## 2026-07-01 - GGB gate .metta sibling fixture for petta-chem run-contract gate

Added `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) under `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/`. These serialize the GGB capacity-gate metadata itself as PeTTa-shaped atoms following the field mapping in `GGB_GATE_RUN_CONTRACT_MAPPING.md`. The `run-record` uses `na` for chemistry-specific slots (abundances, ACS candidates, ablations) since this is a software-governance gate, not a chemistry experiment.

The fixture demonstrates that GGB capacity gates can be rendered as PeTTa-shaped evidence atoms. Verification: all 5 required files present, exactly one `run-summary`, every `RUN.md` check has a corresponding `ggb-check` atom. Source evidence re-verified in `petta-chem` on `main` commit `f83cd62`: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, and `git diff --check` all passed.

Also refreshed the roadmap with new `petta-memory` progress (audit view, tightened binary relation validation, 52 tests passing, up from 45) and new `petta-chem` progress (factored generated-control template, seed-31 factored control, sweep-kind report). No runtime, Telegram, secret, access, security, push, merge, or ThreadKeeper PR #1 changes were made.

## 2026-07-01 - GGB gate-to-run-contract mapping

Added `GGB_GATE_RUN_CONTRACT_MAPPING.md` and archived `artifacts/ggb-capacity-gates/20260701-ggb-run-contract-mapping/RUN.md` as a Bundle C follow-up. The mapping was based on local inspection of `GGB_CAPACITY_GATE_TEMPLATE.md`, `projects/petta-chem/repos/petta-chem/src/run_contract.metta`, and `experiments/run_contract/README.md`. It maps GGB gate fields to the existing `petta-chem` run-contract pattern (`run-config`, `run-manifest`, `run-summary`, `run-record`) while keeping non-chemistry governance/software evidence in explicit GGB companion atoms rather than pretending every gate has chemistry-specific abundances or ACS candidates.

Checks: required source files exist, required mapping headings are present, the roadmap references the mapping artifact, and trailing-whitespace scan passed for the touched OmegaClaw files. No runtime, Telegram, secret, access, security, push, merge, or ThreadKeeper PR #1 changes were made. Next small task: add optional `.metta` sibling files for one archived GGB gate and check coverage against its `RUN.md`.


## 2026-07-01 - ThreadKeeper worker LLM concurrency guard

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `07c8742` (`Add subagent LLM concurrency guard`) as the calls/minute guard's companion backpressure slice: `_call_with_retries` now reserves and releases cross-process per-endpoint in-flight worker LLM slots through an `fcntl`-locked state file under `SUBAGENT_RUN_DIR`. Default cap is `OMEGACLAW_SUBAGENT_MAX_CONCURRENT_LLM_CALLS=4`; set it to `0` to disable locally. Stale/dead owners are pruned, and exhausted slots return structured `concurrency_limited` transcript status instead of launching additional long worker calls.

Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct concurrency assertion replay passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - GGB Bundle B follow-up OmegaClaw-style prompt/index fixture

Archived a follow-up partial GGB capacity-gate record at `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/RUN.md`. In `projects/petta-memory/repos/petta-memory` on branch `agent/parser-validation`, added `fixtures/omegaclaw_prompt_context.metta` and a regression test that loads the fixture into a temporary `MediumMemoryStore`, runs `OmegaClawMemoryBridge.prompt_view_metta()` with reads explicitly enabled under a bounded read-only policy, and checks `MediumMemoryStore.index_view()` over the same journal.

Result: the non-live prompt wrapper includes relevant `ProtomegabotMemory` context, excludes an unrelated scheduling distractor under the gate budget, omits raw cluster envelope atoms, remains parseable, and the generated `MM-index` exposes retrieval edges for the relevant commitment/open-question/status atoms. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 45 tests; `git diff --check` passed. Live OmegaClaw integration and autonomous writes remain intentionally disabled.

## 2026-07-01 - GGB Bundle C petta-chem run-contract gate

Archived a third partial GGB capacity-gate record at `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/RUN.md` for `petta-chem` scientific run-contract reuse. This maps primarily to capacities 2.3, 4.4, and 5.4. The gate is read/test only against `projects/petta-chem/repos/petta-chem`; no live OmegaClaw/Telegram integration, secrets, access, or security settings were changed.

Verification in `petta-chem` on branch `main` commit `4a80388`: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, and `git diff --check` passed. The gate confirms that current exp02 records provide a reusable evidence pattern for GGB gates: config, manifest/provenance, events, abundances, metrics, ACS candidates, ablations, controls, and replay/status summary across all nine current random/shuffled/no-catalysis records. Limitation: this verifies the source pattern but does not yet translate GGB capacity gates into PeTTa atoms. Next small task is a thin mapping sketch from `GGB_CAPACITY_GATE_TEMPLATE.md` to run-contract atoms.

## 2026-07-01 - ThreadKeeper explicit provider metadata hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor`. Added local commit `0b185a4` to remove the remaining fragile cloud/local and Ollama/OpenAI transport classification heuristics from `src/subagent.py`: persona configs now require explicit `node_role` for budget/escalation classification, and `endpoint_kind`/provider metadata controls `ollama_native` vs OpenAI-compatible worker calls without inspecting localhost/base-url/model strings. This targets Lila's concern about `_CLOUD_MODEL_HINTS`/string heuristics while preserving the existing PR #1 safety-floor work.

Focused coverage was added in `Autotests/mock/test_subagent_hardening_mock.py` for missing `node_role` rejection and for an intentionally misleading localhost base URL that still uses OpenAI-compatible transport when `endpoint_kind` says so. Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct metadata and dispatch assertion replay passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - GGB Bundle B petta-memory prompt/index gate

Archived a second partial GGB capacity-gate record at `artifacts/ggb-capacity-gates/20260701-petta-memory-prompt-view/RUN.md` for `petta-memory` bounded prompt/index/PLN views. This maps primarily to capacities 1.2, 2.1, 2.2, 4.3, and 5.4. The gate is intentionally non-live: no OmegaClaw runtime state, Telegram behavior, secrets, or autonomous writes were changed.

Verification during the cron run in `projects/petta-memory/repos/petta-memory`: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 34 tests, including default-disabled/read-only OmegaClaw bridge tests, bounded prompt-view relevance tests, `MM-index`/direct-query parity, and PLN-safe filtering/normalized promoted-premise metadata. `git diff --check` also passed. Current limitations: the `petta-memory` repo has uncommitted local work on branch `agent/parser-validation`, live OmegaClaw integration is still disabled by design, and first PLN inference smoke remains blocked on runtime choice. The next non-live follow-up was completed later with an OmegaClaw-style prompt/index fixture through `OmegaClawMemoryBridge.prompt_view_metta()` plus `index_view`.

## 2026-07-01 - First GGB capacity-gate record and roadmap refresh

Updated `GGB_CAPACITIES_ROADMAP.md` from an initial plan into a more current status artifact. Bundle A now reflects actual local ThreadKeeper hardening progress on branch `agent/threadkeeper-hardening-next` rather than a pending implementation target: timeout/retry/backoff, bounded child-history digests, structured JSON parent returns, persistent transcript records, atomic subagent writes, stricter tool validation, quotas, cancellation, and optional `escalation.metta` integrity pinning. Added `GGB_CAPACITY_GATE_TEMPLATE.md` and archived the first partial empirical gate at `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`.

The same roadmap refresh connects current `petta-memory` status (read-only prompt-view wrapper sketch, prompt relevance ordering, stricter PLN promotion metadata, normalized PLN mapping atoms, generated `MM-index`/`index-view`, 31 stdlib tests passing in project record) and current `petta-chem` status (v0.1 run-contract atoms plus exp02 small deterministic control sweep) to the next capacity gates. Verification during this cron run: in `projects/omegaclaw/repos/ThreadKeeper`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-06-30 - GGB Capacities Curriculum as ProtomegaBot upgrade roadmap

Ben suggested adopting Gödel Oruži's forwarded `GGB Capacities Curriculum v0.1` attachment as a rough medium-term mandate for upgrading `@Protomegabot` intelligence, step by step. Treat it as a planning scaffold rather than a fixed spec: 25 capacities across foundational, reasoning, self-improvement, collective, and governance levels; each should become an empirical gate with an archived result. Existing work already fits especially Level 1.2 memory management, 1.4 safe shell execution, 1.5 channel communication, 2.4 code reading, 2.5 architecture proposal, 3.4 failure analysis, 3.5 budget awareness, 4.1 peer communication, and 5.4 transparency.

Created `projects/omegaclaw/GGB_CAPACITIES_ROADMAP.md` as the first-pass artifact. It maps all 25 capacities using concise working labels to existing anchors in OmegaClaw/ThreadKeeper, `petta-memory`, and `petta-chem`; lists empirical gates and next small tasks; and defines first gate bundles: (A) ThreadKeeper timeout/digest/structured return/persistent transcript records, explicitly avoiding duplicate work against PR #1; (B) read-only `petta-memory` prompt-view smoke; and (C) reuse of `petta-chem` run-contract atoms for capacity-gate records. Open decisions left for Ben are communication topology and whether to replace the working capacity names with exact source labels if needed.

## 2026-06-30 - ThreadKeeper coordination with Zar/@zariuq agents

Ben asked ProtomegaTron to attend the preceding messages from Zar's AI agents (`@zariuq`) and update the ThreadKeeper-upgrade activity accordingly. Initially those preceding messages were not visible in `sessions_history`, and GitHub PR inspection showed no comments/reviews yet on `hlgreenblatt/ThreadKeeper#1`. Ben clarified that the Oruzi entities are bots created by Zar. Current local state: branch `agent/threadkeeper-safety-floor` at commit `3a870c5` is pushed to `bgoertzel-sing/ThreadKeeper` and draft PR https://github.com/hlgreenblatt/ThreadKeeper/pull/1 remains open.

Ben then supplied screenshots of forwarded Lila and Gödel Oruzi messages. Visible content confirms broad agreement with the original audit and adds/prioritizes hardening items:

- Verified original critical gaps: fail-open budget gate, no path sandboxing, `shell=True` with apostrophe filtering, synchronous dispatch, no structured return, no cancellation/quotas/task contracts/full transcript preservation, and tolerant/regexy tool-call parsing.
- Additional issues from Lila: no timeout on `_call_subagent_llm`; unbounded history list/context bloat; no atomic file writes; `escalation.metta` is agent-writable and can bypass its own budget gate; first `(emit ...)` wins and may discard better later outputs; `_CLOUD_MODEL_HINTS` string matching is fragile; no calls/minute or concurrency caps; no persona file integrity check; no argument validation in `run_tools`.
- Gödel's prioritization: architecture is sound; P0 path sandbox and argv-list/allowlisted shell; P1 configurable fail-open/fail-closed budget gate and structured run records; P2 full child transcript preservation and patch-proposal mode; P3 async queued dispatch with cancellation.
- Lila's priority sequence: P1 path sandbox; P2 argv-only exec/no `shell=True`; P3 fail-closed budget gate; P4 LLM timeout + retry/backoff; P5 structured return; P6 full child transcript saved locally with digest to parent; P7 task contracts; P8 cancellation token + per-dispatch quotas; P9 atomic writes; P10 make `escalation.metta` read-only or integrity-checked.

Reconciliation: the existing draft PR/branch already covers the first safety-floor cluster (path sandbox, fail-closed fallback, disabled/allowlisted argv-only shell, and tests). Updated `TASKS.md` to treat the screenshots as the concrete Zar/Oruzi feedback and to queue the remaining items as the next hardening work rather than redoing Phase 1.

## 2026-06-27 - ProtomegaTron `No response from OpenClaw.` suppression

Observed in `artifacts/telegram-private-supervisor/omegaclaw-telegram-private.log` around iterations 2528-2529: OpenClaw Gateway returned HTTP 200, but the raw model text was literally `No response from OpenClaw.`; OmegaClaw then wrapped that plain text as a `send` command for fresh Telegram messages. Patched `repos/PeTTa/repos/OmegaClaw-Core/src/helper.py` so exact no-op strings are suppressed before plain-text wrapping and also when emitted as `send No response from OpenClaw.` or `(send "No response from OpenClaw.")`. Verified with `python3 src/helper.py` and `python3 -m py_compile src/helper.py lib_llm_ext.py channels/telegram.py`. Restarted the private Telegram supervisor; status reports active pid 39909 and startup log shows idle iterations without backend `CHARS_SENT` calls.

## 2026-06-27 ProtomegaTron group responsiveness follow-up

Observed `@Protomegabot are you ok now?` reached OmegaClaw after the group restart, then SWI-Prolog/Janus crashed with fatal signal 11 while in the OpenClaw/Python call path (`janus:py_call/3`, `omegaclaw/2`). This was a real process crash, not only Telegram polling failure.

Immediate mitigation:
- restarted the Telegram runner in group auto-bind mode (`TG_PRIVATE_ONLY=false`, empty `TG_CHAT_ID`, `OMEGACLAW_TIMEOUT=86400`);
- changed `local/omegaclaw-telegram-private-supervisor.sh` defaults to group auto-bind, 24h timeout, and watchdog-style relaunch after runner exit/crash;
- verified bash syntax with `bash -n local/omegaclaw-telegram-private-supervisor.sh`;
- verified live supervisor and `swipl` process after restart.

Caveat: the adapter initializes its Telegram offset by default, so the pre-restart group ping is intentionally skipped after restart. A fresh group ping is needed to verify end-to-end response. Telegram `getUpdates` showed 0 pending updates after restart.

## 2026-06-27 ProtomegaTron fresh-ping crash follow-up

Fresh group ping "@Protomegabot are u back?" was received and logged as HUMAN-MSG, but the OmegaClaw process terminated during/after the OpenClaw prompt call before replying. The prompt was about 51k characters because memory/history.metta contained a large polluted tail of stale "No response from OpenClaw." episodes and the runtime injected maxHistory=30000 plus maxFeedback=50000.

Mitigation applied:
- capped Telegram runner prompt baggage via local/run-omegaclaw-openclaw-telegram-private.sh: maxHistory=8000, maxFeedback=8000, maxRecallItems=8, maxEpisodeRecallLines=8 by default;
- rotated the polluted history to artifacts/history-archives/history.20260627T170451-0700.metta and replaced live memory/history.metta with a concise system note preserving key task context;
- restarted group auto-bind runner and verified live pids include timeout 86400 with maxHistory=8000 and maxFeedback=8000 plus live swipl.

Because Telegram offset initializes on startup, the ping that caused the crash was already consumed/skipped after restart. Another fresh group ping is needed for end-to-end confirmation.

## 2026-06-27 ProtomegaTron Janus/OpenClaw bridge mitigation

After rotating history and reducing prompt context, fresh group ping still reached OmegaClaw and then segfaulted before any `[LLM_RAW]` provider log. A direct OpenClaw call from PeTTa's Python venv succeeded, so the likely fault is the embedded SWI/Janus + Python OpenAI SDK call path rather than Gateway or Telegram.

Mitigation applied:
- patched `repos/PeTTa/repos/OmegaClaw-Core/lib_llm_ext.py` so `OpenClawProvider` can call the Gateway through a short-lived child Python process using stdlib `urllib`, returning only plain stdout to Janus;
- set `OPENCLAW_SUBPROCESS=1` by default in `local/run-omegaclaw-openclaw-telegram-private.sh`;
- verified `python3 -m py_compile` for `lib_llm_ext.py`, `channels/telegram.py`, and `src/helper.py`;
- verified direct venv `lib_llm_ext.callProvider('OpenClaw', ...)` with `OPENCLAW_SUBPROCESS=1` returns a normal model string;
- restarted the group auto-bind runner; live supervisor pid 41934, live swipl pid 41942, and `/proc/.../environ` confirms `OPENCLAW_SUBPROCESS=1`.

A fresh group ping is needed to verify whether the subprocess bridge avoids the segfault in the full Telegram loop.

## 2026-06-28 ProtomegaTron full-loop reply and anti-spam continuation mitigation

Fresh group pings around 2026-06-27 23:16-23:17 PDT verified the full MeTTa runner can now complete Telegram receive -> OpenClaw subprocess -> Telegram send. Relevant log markers included `HUMAN-MSG`, `OpenClawProvider._chat_subprocess child ok`, `[LLM_RAW]`, `RESPONSE: ((send ...))`, `RESULTS`, and `[TELEGRAM] Sent message chunk`.

Afterward, the loop repeatedly called OpenClaw on the synthetic anti-spam message `DO NOT RE-SEND OR SPAM!`, producing repeated no-op `No response from OpenClaw.` results. A very short-term mitigation capped `OMEGACLAW_MAX_NEW_INPUT_LOOPS` at 1, but Ben correctly noted that this was only a hack.

Applied a safer code-level mitigation in `repos/PeTTa/repos/OmegaClaw-Core/src/loop.metta`: after a completed OpenClaw turn and history/result update, clear `&loops` to 0. This preserves the known-good loop structure but prevents blind continuation calls on anti-spam prompts. Restored the runner default `maxNewInputLoops=50` in `local/run-omegaclaw-openclaw-telegram-private.sh`.

Verification: after restart, supervisor stayed active; runtime command shows `maxNewInputLoops=50`; iterations advanced from 1 through 12 with no idle `CHARS_SENT`, `OpenClawProvider._chat_subprocess`, or `[LLM_RAW]` markers. This confirms no idle backend spend in the quiet window. Remaining design work: replace blind continuation with an explicit continuation/autonomous-work protocol, likely separate from group-chat wake cycles.

## 2026-06-28 explicit continuation protocol

Ben correctly objected that capping `maxNewInputLoops` at 1 was only a short-term hack. Implemented a real continuation protocol instead:

- Added a new MeTTa skill in `repos/PeTTa/repos/OmegaClaw-Core/src/skills.metta`: `(continue-thinking reason)`. It sets `&continueRequested` true and returns `CONTINUE-REQUESTED`.
- Added `continue-thinking` to `src/helper.py`'s known command set so the response normalizer preserves it as a valid LLM command.
- Updated `src/loop.metta` so each LLM command batch clears `&continueRequested` before evaluation; after evaluation, the loop only keeps `&loops` alive if `continue-thinking` was explicitly called. Otherwise it sets `&loops` to 0 and waits for a fresh Telegram input or an explicit wake.
- Replaced the synthetic non-fresh prompt marker with `CONTINUATION-MSG: continue-only-if-explicitly-requested`, so continuation turns are no longer framed as `DO NOT RE-SEND OR SPAM!`.
- Updated `memory/prompt_OpenClaw.txt` to instruct ProtomegaTron to call `continue-thinking` only for concrete immediate internal next steps, and not to rely on anti-spam/no-op turns.

Verification: `python3 -m py_compile` passed for helper/lib_llm_ext/telegram adapter; `python3 src/helper.py` assertions passed; supervisor restarted successfully with `maxNewInputLoops=50`; runtime iterations advanced through at least 15 quiet iterations with no runtime `CHARS_SENT`, OpenClaw subprocess, or `[LLM_RAW]` calls. Log shows `continue-thinking` compiled and `&continueRequested` state wired into the loop.

## 2026-06-30 - ThreadKeeper hardening next branch: LLM retries, records, digests, structured returns

Created local branch `agent/threadkeeper-hardening-next` commit `f79891c` from `fork/agent/threadkeeper-safety-floor` / PR #1 head (`3a870c5`) to avoid duplicating completed Phase 1 safety-floor work. Added next-layer hardening in `projects/omegaclaw/repos/ThreadKeeper/src/subagent.py`:

- Configurable subagent worker LLM timeout/retry/backoff via `OMEGACLAW_SUBAGENT_LLM_TIMEOUT_S` (default `180`), `OMEGACLAW_SUBAGENT_LLM_RETRIES` (default `1`, meaning one retry), and `OMEGACLAW_SUBAGENT_LLM_BACKOFF_S` (default `1.0`, exponential). Both local Ollama `/api/chat` and OpenAI-compatible cloud calls use the bounded call path; failures now report attempt count and provider path.
- Atomic `write-file` implementation for subagents using temp-file + `fsync` + `os.replace`, preserving the Phase 1 workspace sandbox.
- Stronger tool argument validation in `run_tools`: required arg counts, non-null args, non-empty file paths, and NUL-byte rejection before dispatching to tool functions.
- Deterministic bounded subagent history: only the recent tail stays in prompt history; evicted turns are summarized into a bounded `HISTORY_DIGEST` instead of letting long-running subagents bloat context.
- Persistent local subagent run records/transcripts: each dispatch gets a run id and atomically written JSON transcript under `memory/subagent-runs` by default, configurable with `OMEGACLAW_SUBAGENT_RUN_DIR`. Records include goal, persona, full prompts/responses/tool calls/results, history digest, files changed, test-like shell commands, status, and summary.
- Structured parent returns: successful, failed, and max-turns dispatches now return bounded JSON with `summary`, `files_changed`, `tests_run`, `uncertainty`, `next_action`, `transcript_path`, and `status`, while keeping full details out of parent context.
- Added focused tests in `Autotests/mock/test_subagent_hardening_mock.py` for retry success/failure, strict arg rejection, atomic write replacement, bounded-history digestion, structured dispatch return, persisted transcript, and file-change tracking.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed. `pytest` is not installed in the base environment (`python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` -> `No module named pytest`), so the new tests could not be run through pytest here. Replayed the same assertions in a direct Python script and they passed.

## 2026-06-30 - ThreadKeeper hardening next: quotas, cancellation, escalation integrity

Continued local branch `agent/threadkeeper-hardening-next` in `projects/omegaclaw/repos/ThreadKeeper`, still based on PR #1 safety-floor head and avoiding completed Phase 1 sandbox/shell/budget fallback work. Added three small follow-on controls in `src/subagent.py`:

- Per-dispatch subagent tool-call quota via `OMEGACLAW_SUBAGENT_MAX_TOOL_CALLS` (default `24`), enforced across turns and returned as structured `status=error` with `QUOTA_EXCEEDED` when exhausted.
- File-based cancellation token via `OMEGACLAW_SUBAGENT_CANCEL_FILE`, checked before LLM calls and during tool execution; cancellation returns structured `status=cancelled` and persists the transcript record.
- Optional escalation policy integrity pin: `OMEGACLAW_ESCALATION_METTA_SHA256` checks the SHA-256 of `src/escalation.metta` or `OMEGACLAW_ESCALATION_METTA_PATH` before cloud delegation and fails closed on mismatch/missing policy.

Extended `Autotests/mock/test_subagent_hardening_mock.py` for quota stop behavior, pre-LLM cancellation, and escalation hash mismatch denial. Checks passed: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` and direct Python assertion replay for quota/cancel/integrity. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked by missing pytest in the base environment.

## 2026-07-01 - ThreadKeeper task-contract hardening slice

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still based on draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 sandbox/shell/budget work. Added local commit `68d7bc5` with a small task-contract slice in `src/subagent.py`: dispatch goals may now be plain text or JSON contract objects (or persona `task_contract`) with `objective`, `allowed_paths`, `forbidden_actions`, and `done_criteria`; contracts are injected into the child prompt, persisted in subagent run transcripts, and enforced for file-tool path bounds plus forbidden tool actions. Added focused tests for path-limited writes and forbidden write actions. Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct contract assertion replay passed; pytest remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper append-file atomic write hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still based on draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 sandbox/shell/budget work. Added local commit `f6df5ef` to close the remaining file-tool atomicity gap: subagent `append-file` now reads existing content and writes the combined result through a temp file with `fsync` followed by `os.replace`, matching the already-hardened `write-file` path and preserving cleanup of temp files. Added focused regression coverage in `Autotests/mock/test_subagent_hardening_mock.py`.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed. A direct Python assertion for atomic append behavior passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper persona integrity hardening slice

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 sandbox/shell/budget work. Added local commit `2fcb0ba` (`Pin subagent persona integrity`) to address the remaining persona-integrity/key-validation gap from the Lila/Gödel feedback: persona lookup keys are now restricted to simple identifiers instead of path-like values, and persona JSON may include optional `persona_sha256` to pin the persona prompt file. If the pinned prompt hash mismatches, dispatch fails closed before any worker LLM call.

Focused coverage was added in `Autotests/mock/test_subagent_hardening_mock.py` for path-traversal-like persona keys and persona prompt SHA-256 mismatch. Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct persona-integrity assertions passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper persona example metadata hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 work. Added local commit `5fdd131` (`Harden subagent persona examples`) to make the committed persona examples and deployment README match the newly enforced safety metadata: example configs now set explicit `node_role`, explicit `endpoint_kind`, and `persona_sha256` pins for the bundled prompt. The README now states that provider/model/base URL strings must not be used for safety classification and documents `task_contract`/prompt hash fields.

Focused coverage was added in `Autotests/mock/test_subagent_hardening_mock.py` to assert that all committed `*.json.example` persona configs include valid explicit metadata and a valid prompt SHA-256 pin. Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct persona-example metadata assertions passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper worker LLM rate-limit guard

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added local commit `9b6439c` (`Add subagent LLM rate limit guard`) as a small backpressure/calls-per-minute hardening slice: `_call_with_retries` now atomically reserves worker LLM calls in a per-endpoint-label state file under `SUBAGENT_RUN_DIR` using `fcntl` locking. The default cap is `OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=60`; set it to `0` to disable locally. If the cap is exceeded, dispatch gets a structured `rate_limited` transcript record and bounded parent return instead of making another worker call.

Focused coverage was added in `Autotests/mock/test_subagent_hardening_mock.py` to verify that the second call in a one-call/minute window is blocked and does not invoke the worker function. Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct rate-limit assertion replay passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper locked file writes and subagent docs refresh

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 sandbox/shell/budget work. Added commit `34c96b4` (`Lock subagent file writes`) to strengthen the atomic-write slice: `write-file` and `append-file` now share a helper that writes temp-file + fsync + `os.replace`, and both take a per-target `fcntl` lock while updating a workspace file. This closes the lost-update race for concurrent append-style subagent artifacts while preserving sandbox path resolution. Updated `docs/reference-skills-subagent.md` so the reference now matches the hardening branch's structured JSON returns, persistent transcript records, timeout/retry/backoff, quotas/cancellation, rate/concurrency guards, workspace sandbox, and escalation hash pin.

Checks: `git diff --check` and `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed. A direct multiprocessing assertion replay confirmed 4 concurrent append workers produced all 48 expected unique lines with no temp files left behind. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper emit protocol and tool-argument bounds

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, still coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added pushed commit `5f33c8b` (`Harden subagent emit protocol`) with a small integrity/validation hardening slice: subagent dispatch now accepts `(emit "...")` only when it is the sole parsed call in a worker response, rejects mixed `emit` + tool-call / conflicting final responses with structured `EMIT_PROTOCOL_VIOLATION`, and records that status in the persistent transcript. This closes the forwarded Lila concern that first-emit-wins could discard later/contradictory output. Tool argument validation now also bounds file-path argument length and per-argument string length via `OMEGACLAW_SUBAGENT_MAX_PATH_ARG_CHARS` and `OMEGACLAW_SUBAGENT_MAX_TOOL_ARG_CHARS`. Updated focused tests and subagent docs.

Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct assertion replay for oversized arguments plus mixed emit/tool rejection passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.


## 2026-07-01 - ThreadKeeper task-contract validation bounds

Continued `projects/omegaclaw/repos/ThreadKeeper` on local branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added commit `8b35a91` (`Validate subagent task contracts`) as a small follow-up to the task-contract slice: normalized contracts are now validated before any worker LLM call, `allowed_paths` entries are dry-run resolved against the subagent workspace so path escapes fail closed, and contract list size/item length are bounded via `OMEGACLAW_SUBAGENT_MAX_CONTRACT_ITEMS` / `OMEGACLAW_SUBAGENT_MAX_CONTRACT_ITEM_CHARS`. Updated focused tests and subagent reference docs.

Checks: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct assertions for allowed-path escape plus oversized contract rejection passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper task-contract strict-shape follow-up

Continued `projects/omegaclaw/repos/ThreadKeeper` on `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `a4a9b87` (`Tighten subagent task contract validation`) to the fork branch after first pushing the prior local contract-bounds commit `8b35a91`.

This slice tightens task-contract validation before any worker LLM call: normalized contracts now persist the `objective` in transcript `task_contract`, bound objective length via `OMEGACLAW_SUBAGENT_MAX_CONTRACT_OBJECTIVE_CHARS`, and reject unsafe `forbidden_actions` entries that are not simple action identifiers. Docs now mention strict contract field bounds and the current argv-list shell restriction.

Checks: `git diff --check` passed; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct assertion replay for unsafe forbidden action and oversized objective passed. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-01 - ThreadKeeper setup-failure transcript records

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `970b519` (`Record subagent setup failures`) to close a remaining structured-return / persistent-record gap: early setup failures, invalid task contracts, invalid tool subsets, persona prompt/hash failures, provider setup failures, and escalation-policy denials now return the same bounded JSON parent digest shape and persist minimal local transcript records instead of returning only raw `(subagent error: ...)` strings. Transcript statuses now distinguish `setup_error`, `contract_invalid`, `tool_subset_invalid`, `persona_prompt_invalid`, `provider_invalid`, and `escalation_denied`.

Checks: `git diff --check` passed; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; targeted direct assertions confirmed invalid-contract and escalation-denial paths produce JSON returns plus transcript records without calling the worker LLM. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-02 - ThreadKeeper persona prompt sandbox hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `f1a8a70` (`Sandbox subagent persona prompts`) as a small strict-validation/persona-integrity follow-up: persona prompt paths now resolve under `PERSONA_DIR` and fail closed on empty values, `..` escapes, symlink escapes, or absolute paths outside the persona directory before any worker LLM call. Hash pinning still works for relative paths and absolute in-directory paths.

Checks: `git diff --check` passed; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct assertion replay confirmed relative/absolute prompt escapes are rejected and dispatch persists a structured `persona_prompt_invalid` transcript without calling the worker LLM. `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` remains blocked because `/usr/bin/python3` has no `pytest` installed.

## 2026-07-02 - ThreadKeeper cloud provider setup fail-closed

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `c3e836b` (`Fail closed on missing subagent cloud client`) as a small provider/structured-error hardening slice: OpenAI-compatible subagent providers now require the local client/SDK to initialize during setup. If initialization fails, dispatch returns the bounded structured parent digest and persists a minimal transcript with status `provider_invalid` before any worker LLM call. Native Ollama endpoints remain stdlib/urllib-based and do not require the OpenAI SDK.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`31 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper shell workspace cwd hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `893a0e3` (`Run subagent shell commands in workspace`) as a small shell/tool-argument containment follow-up: when the optional subagent `shell` tool is explicitly enabled and the executable is allowlisted, commands now run with `cwd` fixed to `OMEGACLAW_SUBAGENT_WORKSPACE` and stdin closed (`subprocess.DEVNULL`). Missing workspace directories fail closed before execution. This preserves argv-only/no-`shell=True` behavior while preventing workspace-scoped contracts from being undermined by inherited process cwd.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`33 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - GoalChainer exploratory intake gate

Inspected MesTTo `OmegaClaw-GoalChainer` as an external exploratory source for Protomegabot goal-orientation/motivation reasoning. Cloned to `projects/omegaclaw/repos/OmegaClaw-GoalChainer` and pinned the intake to commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`. Produced `GOALCHAINER_INTEGRATION_MAP.md` and archived `artifacts/ggb-capacity-gates/20260702-goalchainer-intake/RUN.md`.

Findings: the architecture is directly relevant to the GGB roadmap: natural-language request → evidence/deontic status → PeTTaChainer/PLN acceptability → SNARS proof/provenance → MetaMo individual/collective motivation → OmegaClaw directive/task claim. It looks especially useful as a design pattern for a future `petta-memory` promoted-evidence packet feeding a bounded goal/norm/motivation decision report.

Checks: Python source compile passed. Pytest diagnostics were intentionally non-live and showed the repo is not yet ready for Protomegabot runtime use here: default env produced `22 passed, 8 skipped, 11 failed` because runtime-dependent tests assume `/home/user/Dev/PeTTa`; with local PeTTa/SWI paths, `25 passed, 6 skipped, 10 failed`; with local PeTTa/SWI plus `projects/petta-memory/repos/PeTTaChainer`, `25 passed, 6 skipped, 10 failed` after ~133s, with PeTTaChainer `compileadd` exceeding SWI `--stack_limit=8g` and one directive ready-task assertion still failing. No live OmegaClaw/Telegram runtime, secrets/access/security settings, paid compute, push, merge, or PR #1 changes were made.

Next small step: build a bounded non-live harness for one incident-style GoalChainer decision report, either isolating/bypassing the PeTTaChainer compile/add bottleneck or using a documented minimal/precompiled acceptability path, then diagnose directive task-state mapping before any OmegaClaw skill is loaded.

## 2026-07-02 - ThreadKeeper shell PATH sanitization

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `01fe0d8` (`Sanitize subagent shell PATH`) as a strict tool-argument/shell-containment follow-up: the optional subagent `shell` tool remains disabled by default, argv-only, executable-allowlisted, command-name-only, no-stdin, and workspace-cwd-bound, and now runs with a sanitized `PATH` that removes empty/`.` entries and entries resolving inside `OMEGACLAW_SUBAGENT_WORKSPACE`. This closes the allowlisted-basename hijack case where a workspace-controlled executable could be found first after `cwd` was pinned to the workspace.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`35 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper shell environment scrubbing

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `b828ebf` (`Scrub subagent shell environment`) as a small strict shell-containment follow-up: when the optional `shell` tool is explicitly enabled, argv-only, executable-allowlisted, command-name-only, workspace-cwd-bound commands now run with a minimal child environment instead of inheriting the parent agent environment. The child env keeps sanitized `PATH`, pins `HOME` to `OMEGACLAW_SUBAGENT_WORKSPACE`, and preserves only locale/timezone variables, so API keys/tokens/session vars are not exposed to allowlisted subprocesses.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`36 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-02 - ThreadKeeper read-file result bounding

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `f880c50` (`Bound subagent read-file output`) as a small bounded-context/tool-output hardening slice: subagent `read-file` now reads at most `OMEGACLAW_SUBAGENT_MAX_READ_FILE_CHARS + 1` characters (default `20000`) and returns an explicit truncation marker instead of loading/returning an arbitrarily large file into worker context. The new knob uses the same defensive env parsing/clamping as the existing validation/quota caps, and the subagent reference docs now list it.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`38 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - ThreadKeeper hash-chained run-index audit hardening

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `d0c887d` (`Hash-chain subagent run index`) as a small Phase 3 audit-integrity follow-up: compact `index.jsonl` subagent run entries now include `previous_entry_sha256` and `entry_sha256`, computed under the same sidecar lock used for appends. Transcript files still receive individual `.sha256` sidecars and structured parent digests still return `transcript_sha256`; the index hash chain gives supervisors a cheap way to detect local truncation, reordering, rewrite drift, or corruption in the audit listing without reading full transcripts into parent context.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`41 passed`). Refreshed the ThreadKeeper GGB gate fixture and roadmap status; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py` passed across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer fixtures. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - ThreadKeeper queued subagent worker primitive

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `8eae787` (`Add queued subagent worker primitive`) as the next async-dispatch hardening slice after queue-only mode.

The new Python helper `subagent.run_queued_dispatch(queue_path)` atomically claims one queued `queue/*.json` task, revalidates the queued task shape/path, suppresses `OMEGACLAW_SUBAGENT_QUEUE_ONLY` only for the worker dispatch call, runs the normal synchronous `dispatch(...)` validation/execution path, writes a compact `*.result.json`, and leaves the consumed task as `*.done` for audit rather than silently re-running it. Malformed/escaping queue paths return structured `status=queue_worker_error` before any worker LLM call.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`49 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - ThreadKeeper bounded queued dispatch drain helper

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `ec17402` (`Add bounded queued dispatch drain helper`) as a small async-dispatch hardening slice after the queued-worker primitive.

The new Python helper `subagent.drain_queued_dispatches(max_tasks=1)` lists pending `OMEGACLAW_SUBAGENT_RUN_DIR/queue/*.json` tasks oldest-first, runs at most the requested/clamped count through `run_queued_dispatch`, returns compact JSON drain metadata, preserves `OMEGACLAW_SUBAGENT_QUEUE_ONLY`, and deliberately does not daemonize, sleep, poll forever, self-schedule, or start from `dispatch`. This gives an operator/supervisor a bounded primitive for async queue draining without turning ThreadKeeper into an unsupervised live worker.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`51 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-03 - ThreadKeeper run-index audit verifier

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commits `ee883ce` (`Add subagent candidate review helper`) and `b14ade5` (`Add subagent run index verifier`) to `fork/agent/threadkeeper-hardening-next`.

This slice strengthens persistent run-record audit integrity without changing live runtime behavior: `subagent.verify_subagent_run_index(index_path=None)` now performs a bounded, read-only audit of the local `index.jsonl` hash chain under `OMEGACLAW_SUBAGENT_RUN_DIR` and verifies recorded local transcript SHA-256s. It returns compact JSON statuses (`index_verified`, `index_tampered`, `index_missing`, or `index_audit_error`) and deliberately does not repair/rewrite files, drain queues, call a worker LLM, daemonize, self-schedule, or expand transcripts into parent context.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`57 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, or live async worker loop.

## 2026-07-03 - ThreadKeeper queue sidecar worker-task rejection

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `d0d1dfa` (`Reject queue result sidecars as worker tasks`) to `fork/agent/threadkeeper-hardening-next`: `_resolve_queue_task_path` now accepts only live pending `queue/*.json` task-record basenames, so explicit queued-worker calls reject retained audit sidecars such as `*.done.result.json` / `*.failed.result.json` before any claim/rename. Added regression coverage that a result sidecar remains in place and is not renamed to `.claimed` or `.failed`.

Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` passed (`58 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-03 - ThreadKeeper queued-worker contract preservation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `76bd2c4` (`Preserve queued subagent task contracts`) as a small queue/task-contract integrity follow-up.

Issue closed: queue-only dispatch persisted a normalized `task_contract` in `queue/*.json`, but `subagent.run_queued_dispatch(queue_path)` re-ran synchronous dispatch with only the raw goal string, which could drop queued `allowed_paths`, `forbidden_actions`, `max_tool_calls`, `patch_proposal_only`, or `requires_adjudication` constraints during worker execution. The worker primitive now validates queued `task_contract` shape before running, fails retained claimed tasks closed if invalid, and re-injects the contract into the synchronous dispatch goal while queue-only mode is suppressed. Added focused regression coverage proving a queued `allowed_paths` contract still blocks an unsafe write and permits the safe path during the worker run.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`59 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - GGB gate template source-grounding refinement

Refined `GGB_CAPACITY_GATE_TEMPLATE.md` as a narrow roadmap-quality gate improvement rather than a runtime change. The template now requires a source-grounding checklist under inputs/fixtures: mutable state should be inspected from current project files or commands instead of chat recall alone; external/exploratory sources should be named with URL/path and commit or retrieval date when available; and untrusted attachment/user content should be marked as data, not instructions. The evidence section now separates direct observations/check outputs from inferences/design judgments and explicitly lists unsupported or untested claims excluded from the gate result.

Updated `GGB_CAPACITIES_ROADMAP.md` to mark capacity 2.1 (retrieval/source grounding) and 5.4 (transparency/calibrated uncertainty) as partial passes for future gate records, with the next task being to apply the new fields in the next new capacity-gate artifact.

Checks: `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py projects/omegaclaw/artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract projects/omegaclaw/artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening projects/omegaclaw/artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture projects/omegaclaw/artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness` passed. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.
