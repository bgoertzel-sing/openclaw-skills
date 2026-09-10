# OmegaClaw Core Installation

- Slug: `omegaclaw`
- Status: `active`
- Created: `2026-06-26`
- Last reviewed: `2026-08-21` (03:05 UTC)
- Owner: Benjamin Goertzel

## Purpose

On 2026-08-14 at 07:19 PDT, Ben-authorized retrieval pinned
`intfloat/e5-large-v2` at revision
`f169b11e22de13617baa190a028a32f3493550b6` in the clean cache. Hash inventory
and offline 1,024-D loading passed. The preregistered one-record Protomega
re-embedding then passed new-store creation, exact reconciliation,
fresh-process exact-document/phrase recall, and authoritative-source byte
stability. The missing-model blocker is closed; disposable full-loop recall
and production cutover remain separate gates. Evidence:
`experiments/20260814T141553Z-e5-large-v2-pinned-download/` and
`experiments/20260814T141935Z-protomega-reembedding-e5-pinned/`.

Install and validate OmegaClaw Core locally on the OpenClaw research workstation, then prepare a safe second phase for communication with Benjamin via Telegram, with ZeroBot/OpenClaw, and eventually in a shared Telegram group.

## Success criteria

Initial install success:

- OmegaClaw-Core, PeTTa, and `petta_lib_chromadb` are cloned in a reproducible project layout.
- Required SWI-Prolog/PeTTa/Python dependencies are installed without clobbering system state.
- PeTTa smoke test passes.
- OmegaClaw starts locally in a controlled mock mode without real Telegram/API credentials.
- Install notes and launch environment are recorded.

Second-phase success, not yet attempted:

- Decide a safe communication architecture and auth boundaries.
- Configure OmegaClaw to talk to Benjamin via Telegram.
- Configure controlled OmegaClaw ↔ ZeroBot/OpenClaw communication.
- Configure a Telegram group path if still desired.

## Scope

### In scope

- Local user-space installation where possible.
- Repository inspection before running install logic.
- Local SWI-Prolog build if distro packages are unavailable/too old.
- Python venv under the project tree.
- Mock-channel/mock-provider smoke tests.
- Telegram/channel planning after local runtime is stable.

### Out of scope for now

- Installing real Telegram bot tokens or LLM provider credentials without a separate explicit configuration step.
- Giving OmegaClaw broad filesystem/network authority before policy review.
- Running uncontrolled long-lived loops or self-starting services.
- Paid compute.

## Current state

On 2026-08-21 at 03:05 UTC, ThreadKeeper commit `2289264` on
`agent/threadkeeper-hardening-next` hardened `_safe_slug`,
`_validate_persona_key`, `_new_run_record`,
`_resolve_persona_prompt_path`, and `load_persona_prompt`'s
`expected_sha256` handling in `subagent.py` against
behavioral `str()` at trust boundaries.
`_safe_slug` previously called `str(text or "")` without
first checking `type(text) is str`; a behavioral str subclass
could execute attacker-controlled `__str__` during coercion,
or `__bool__`/`__len__` during the truthiness check. The
hardened code checks `type(text) is str` and uses `""` for
any other type.
`_validate_persona_key` previously called
`str(persona_key or "").strip()` without first checking
`type(persona_key) is str`; a behavioral str subclass could
execute `__str__` or `strip` during coercion. The hardened code
raises `ValueError` for non-exact-str.
`_new_run_record` previously called `str(goal or "")`; a
behavioral object could execute `__str__` or `__bool__`. The
hardened code uses `goal if type(goal) is str else ""`.
`_resolve_persona_prompt_path` previously called
`str(persona_file or "").strip()` without checking
`type(persona_file) is str`. The hardened code raises
`ValueError` for non-str.
`load_persona_prompt`'s `expected_sha256` previously called
`str(expected_sha256 or "").strip().lower()`. The hardened code
uses the exact-type pattern.
Fifty-three focused tests cover all five functions with exact
str acceptance, non-str rejection (int, float, list, dict,
None, bool, bytes), behavioral str subclass rejection without
triggering `__str__`, `strip`, or `lower`, behavioral str with
raising `__str__`/`strip` not triggered, and max_len respected.
All 53 focused tests, 342 combined hardening tests, Python
compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-21 at 01:03 UTC, ThreadKeeper commit `2bc0af4` on
`agent/threadkeeper-hardening-next` hardened
`_resolve_workspace_path` and `_bound_patch_proposal_content` in
`subagent.py` against behavioral `str()` at trust boundaries.
`_resolve_workspace_path` previously called `str(path)` without
checking `type(path) is str`; a behavioral str subclass could
execute attacker-controlled `__str__` during the NUL check or
path resolution, before any workspace-containment validation
ran. The hardened code requires an exact built-in `str` and
raises `ValueError` for any other type.
`_bound_patch_proposal_content` previously called `str(content)`
without checking `type(content) is str`; while the caller
(`run_tools`) already validates `args[1]` as an exact `str` via
`_validate_tool_args`, defense-in-depth requires the function
itself to be safe when called directly by a programmatic caller.
The hardened code requires an exact built-in `str` and returns a
bounded diagnostic for any other type. Twenty-six focused tests
cover `_resolve_workspace_path` rejection of int, float, list,
dict, None, bool, bytes, and behavioral str subclasses without
triggering `__str__` or `strip`; valid string proceeding past
the type check; empty string and NUL-containing string raising
invalid path; `_bound_patch_proposal_content` preservation of
exact str and empty str; rejection of int, float, list, dict,
None, bool, bytes, and behavioral str subclasses without
triggering `__str__`; side-effect `__str__` not running; custom
type name in diagnostic; and long string preservation. All 26
focused tests, 212 combined hardening tests, 46 budget hardening
tests, Python compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-20 at 23:04 UTC, ThreadKeeper commit `90e0473` on
`agent/threadkeeper-hardening-next` hardened
`_sanitize_error_msg` and `_call_with_retries` in `subagent.py`
against behavioral exception subclasses whose `__str__` raises.
`_sanitize_error_msg` previously called `str(e)` directly; a
behavioral exception subclass can override `__str__` to raise a
different exception, hang, or execute arbitrary behavior.  If
`str(e)` raised, `_sanitize_error_msg` itself would propagate the
error instead of producing a bounded message, bypassing
`_SUBAGENT_MAX_ERROR_MSG_CHARS`.  The same pattern existed in
`_call_with_retries`, where `str(last_exc)` could raise instead of
returning a bounded `_LLMControlResult`, bypassing
`_SUBAGENT_MAX_LLM_ERROR_CHARS`.  A new `_safe_exception_str`
helper catches any exception during `str(e)` and returns a fixed
bounded diagnostic including the exception type name.  `None`
produces `'None'`, matching `str(None)`.  `_sanitize_error_msg`
now uses `_safe_exception_str(e)`; `_call_with_retries` now uses
`_safe_exception_str(last_exc)`.  Twenty-three focused tests cover
normal exception preservation, `None` handling, behavioral
`__str__` raising returns diagnostic without propagating, long
`__str__` preserved (bounding is caller's job), side-effect
`__str__` still executes, non-Exception object with raising
`str()`, `_sanitize_error_msg` no longer raises on behavioral
exceptions, `_bounded_exception_summary` no longer raises,
`_call_with_retries` no longer raises on behavioral final
exception, and `dispatch()` persona config and provider error
paths with raising `__str__` return bounded structured errors.
All 23 focused tests, 112 combined focused hardening tests, 219
budget/isinstance hardening tests, Python compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed. 135
pre-existing fixture failures (unchanged baseline).

On 2026-08-20 at 21:03 UTC, ThreadKeeper commit `2436b50` on
`agent/threadkeeper-hardening-next` hardened remaining `str()`
calls at trust boundaries in `subagent.py`. `_tool_write_file` and
`_tool_append_file` previously called `str(content)` on the content
argument before size checking or writing; a behavioral str subclass
with a custom `__str__` could execute attacker-controlled behavior
during coercion before the size cap was applied. Both now use
`_safe_tool_result_str(content)`, matching the pattern established
in the prior `_bound_tool_output` hardening commit. The dispatch
loop's response-too-large check previously called `str(raw)` on the
LLM provider response before `len()` and `cap()`; the code now uses
`_safe_tool_result_str(raw)` with a local variable reused for both
the size check and the cap. Four `_structured_setup_error` call
sites in `dispatch()` (persona config load, tool subset parse,
persona prompt load, provider resolution) previously called
`str(e)` on caught exceptions; all four now use
`_sanitize_error_msg(e)`, which bounds the message at
`_SUBAGENT_MAX_ERROR_MSG_CHARS` and strips absolute paths. Twenty-
nine focused tests cover write/append-file behavioral str rejection,
non-string content diagnostics, dispatch size-check pattern with
behavioral objects, `_sanitize_error_msg` bounding and path
stripping, and dispatch integration with bounded error returns. All
29 focused tests, 177 budget hardening tests, 58 combined focused
hardening tests, Python compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed. 135 pre-existing fixture
failures (unchanged baseline).

On 2026-08-20 at 19:03 UTC, ThreadKeeper commit `9822a55` on
`agent/threadkeeper-hardening-next` hardened `_bound_tool_output`
and tool result string handling in `subagent.py`.
`_bound_tool_output` previously called `str(result)` on untrusted
external tool results before applying its size cap. A behavioral
object with a custom `__str__` could execute attacker-controlled
behavior before the cap was applied. The hardened code accepts
only an exact built-in `str` directly; `bytes` are decoded safely
with UTF-8 replacement; any other type produces a fixed bounded
diagnostic without calling `str()` on the object.
`_search_import_error` in `_build_tool_registry` previously stored
`str(e)` unbounded in the persistent tool registry; the hardened
code bounds it through `_sanitize_error_msg`. A new
`_safe_tool_result_str` helper replaces two `str(result)` calls in
`run_tools` that handled write-file/append-file SUCCESS detection
and tool result clipping, matching the exact-type pattern used by
`_bound_tool_output`. The pre-existing
test_bound_tool_output_handles_non_string_result test is updated
to reflect the new hardened behavior. Twenty-nine focused tests
cover `_safe_tool_result_str` acceptance/rejection, behavioral
subclass rejection, `_bound_tool_output` hardening, bytes decoding,
`_search_import_error` bounding, and `run_tools` integration with
non-string and behavioral-subclass tool results. All 29 focused
tests, 136 pre-existing fixture failures (unchanged baseline),
1464 combined focused hardening passes, Python compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-20 at 15:04 UTC, ThreadKeeper commit `ac18fe2` on
`agent/threadkeeper-hardening-next` bounded the `_sanitize_error_msg`
function in `subagent.py`. `_sanitize_error_msg` previously called
`str(e)` and stripped absolute paths but did not bound the message
length. An exception with an arbitrarily long `__str__` result (e.g.
an HTTP error including a large response body) could produce an
unbounded error message that bypasses the `_SUBAGENT_MAX_RESPONSE_CHARS`
check applied to ordinary worker responses when used in structured
return summaries (candidate review error path, line 2928) and tool
error messages returned to the worker LLM. The hardened code bounds
the message at `_SUBAGENT_MAX_ERROR_MSG_CHARS` (default 2000,
env-configurable via `OMEGACLAW_SUBAGENT_MAX_ERROR_MSG_CHARS`, minimum
100, maximum 10000) after path stripping. The exception type name
(`type(e).__name__`) is already a bounded string and is preserved in
full by callers that include it separately. Nineteen focused tests
cover normal-length exception preservation, long exception bounding,
exactly-at-limit preservation, one-over-limit truncation, empty
message, newlines, Unicode, path stripping before bounding, path
stripping with long message bounded, custom limit respect, custom
minimum/maximum enforcement, exception type name not in sanitize
output, `_bounded_exception_summary` compatibility, candidate review
error summary bounding, tool error messages bounded, skill error
messages bounded, non-string exception str, and None exception. All
19 focused tests, 127 combined focused hardening tests, Python
compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-20 at 13:03 UTC, ThreadKeeper commit `7024c36` on
`agent/threadkeeper-hardening-next` bounded the `_call_with_retries`
LLM error message in `subagent.py`.
`_call_with_retries` previously embedded `str(last_exc)` directly in
its final `_LLMControlResult` error message via f-string
interpolation. An exception with an arbitrarily long `__str__`
result (e.g. an HTTP error including a large response body) could
produce an unbounded control message that bypasses the
`_SUBAGENT_MAX_RESPONSE_CHARS` check applied to ordinary worker
responses, reaching the turn record's `raw_response` field and the
structured return's summary. The hardened code bounds `str(last_exc)`
at `_SUBAGENT_MAX_LLM_ERROR_CHARS` (default 2000, env-configurable
via `OMEGACLAW_SUBAGENT_MAX_LLM_ERROR_CHARS`) before constructing the
`_LLMControlResult`. The exception type name
(`type(last_exc).__name__`) is already a bounded string and is
preserved in full. Twelve focused tests cover normal-length exception
preservation, long exception bounding, exactly-at-limit preservation,
one-over-limit truncation, empty message, newlines, Unicode, exact
`_LLMControlResult` type, label inclusion, attempt count inclusion,
exception type name preservation, and custom limit respect. All 12
focused tests, 327 combined focused hardening tests, Python
compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-20 at 11:03 UTC, ThreadKeeper commit `2d8226d` on
`agent/threadkeeper-hardening-next` hardened the `ts` field extraction
in `spent_cost_estimate` in `threadkeeper_budget.py` against
non-finite float values. `spent_cost_estimate` previously extracted
`ts` from usage-log records with
``d.get("ts", 0.0) if type(d.get("ts")) in (int, float) else 0.0``.
While `_strict_json_loads` already rejects NaN/Infinity JSON literals
at the parse level, the `type(...) in (int, float)` pattern accepted
non-finite floats (`NaN`, `inf`, `-inf`) that could reach the `ts`
extraction through a programmatic caller or a different JSON parser.
A non-finite `ts` would violate the `UsageRecord.ts: float` contract
and could break later `json.dumps(..., allow_nan=False)` serialization
or time-based comparison logic. The hardened code uses
`_safe_float(d.get("ts"), 0.0)` which accepts only exact built-in
`int` or `float` (rejecting non-finite values via `math.isfinite`),
returning `0.0` otherwise — matching the pattern already used for
`escalation_soft_fraction`, token rates, and all other config and
record fields. Twenty-nine focused tests cover valid `int` and
`float` `ts` acceptance; missing `ts` default; `NaN`, `inf`, and
`-inf` rejection by `_strict_json_loads` at the JSON parse level;
string, bool, list, dict, and `None` `ts` replacement with default;
`should_escalate` survival with non-finite `ts`; mixed valid and
non-finite `ts` records; `_safe_float` direct rejection of `NaN`,
`inf`, `-inf`, bool, string, list, dict, `None`, and behavioral
`int`/`float` subclasses without invoking `__float__`; and
`_strict_json_loads` `NaN`/`inf`/`-inf` literal rejection. All 29
focused tests, 26 float hardening tests, 29 cost-estimate rates
tests, 34 budget config int tests, 46 budget hardening tests, 34
accounting hardening tests, 7 trust-boundary isinstance tests, 67
subagent boundary tests / 160 subtests, Python compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-20 at 09:03 UTC, ThreadKeeper commit `191f1c3` on
`agent/threadkeeper-hardening-next` hardened `_MettaPolicy._parse`
in `threadkeeper_budget.py` and `_normalize_task_contract` in
`subagent.py`. `_parse` previously called `str(results[0])` on the
first element of the PeTTa results list; a behavioral str subclass
could override `.__str__` or `.strip` and execute behavior during
the decision parsing path. `_parse` now requires an exact built-in
`str` and returns `None` for non-string types. `_normalize_task_contract`
previously used `isinstance(parsed, dict)` to detect dict subclasses
from programmatic callers; `isinstance` can trigger `__class__` on a
behavioral object. The code now uses exact `type()` checks for dict,
list, str, int, float, bool, and None, matching all prior isinstance
replacements. Twenty-eight focused tests cover `_parse` string
acceptance/rejection and `_normalize_task_contract` dict subclass
preservation, scalar non-preservation, and behavioral object rejection.
All 28 focused tests, 438 combined focused hardening tests, Python
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-20 at 07:30 UTC, ThreadKeeper commit `42eac1e` on
`agent/threadkeeper-hardening-next` hardened `cost_estimate` and
`spent_cost_estimate` in `threadkeeper_budget.py` against non-dict
`rates_per_1k_tokens` and per-role rate entries.
`spent_cost_estimate` previously accessed
`self._budget["rates_per_1k_tokens"]` directly and passed it to
`cost_estimate`, which called `.get()` on each per-role entry. A
non-dict `rates_per_1k_tokens` value or a non-dict per-role entry
would raise `AttributeError` and crash the cost-estimation path. A
new `_safe_rates` helper accepts only an exact built-in `dict`,
returning `{}` otherwise — matching the `_safe_config_int`,
`_safe_float`, and `_safe_record_int` patterns. `cost_estimate` now
checks `type(r) is dict` before using a per-role entry. Twenty-nine
new focused tests cover `_safe_rates` rejection, `cost_estimate`
non-dict entry rejection, `spent_cost_estimate` survival of direct
`_budget` mutation, and `should_escalate` survival of mutated rates.
All 29 focused tests, 26 float hardening tests, 46 budget hardening
tests, 34 budget config int hardening tests, 22 worker-usage int
tests, 11 isinstance subagent tests, 9 isinstance trust boundary
tests, 34 accounting hardening tests, compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-20 at 07:04 UTC, ThreadKeeper commit `20ebaab` on
`agent/threadkeeper-hardening-next` hardened `_safe_float` in
`threadkeeper_budget.py` against non-finite float values.
`_safe_float` previously accepted any exact built-in `float`,
including `NaN`, `infinity`, and `-infinity`. YAML parses `.nan`,
`.inf`, and `-.inf` as genuine `float` instances, so a hand-edited
or corrupted config could contain `escalation_soft_fraction: .nan`
or `.inf`. `int(ceiling * float('nan'))` raises `ValueError` and
`int(ceiling * float('inf'))` raises `OverflowError`, either of
which would crash `should_escalate`. Non-finite token rates would
silently produce `NaN` or `inf` cost estimates. `_safe_float` now
checks `math.isfinite(v)` before returning a `float`, falling back
to the safe default otherwise. Thirteen new focused tests cover
`NaN`, `inf`, and `-inf` rejection in `_safe_float`; `NaN`, `inf`,
`-inf`, and both-non-finite rates in `cost_estimate`; and `NaN`,
`inf`, `-inf`, and YAML-serialized `NaN` in `should_escalate`. All
39 focused tests, 46 budget hardening tests, 34 budget config int
hardening tests, 22 worker-usage int tests, 11 isinstance subagent
tests, 9 isinstance trust boundary tests, 34 accounting hardening
tests, compilation, diff check, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-20 at 05:07 UTC, ThreadKeeper commit `3b2ce47` on
`agent/threadkeeper-hardening-next` hardened `int()` calls in
`threadkeeper_budget.py` that process config-derived values.
`should_escalate` previously used `int(self._budget["thread_token_ceiling"])
and `int(self._budget["min_local_iterations_before_escalation"])` to coerce
config values. `summary` previously used
`int(self._budget["thread_token_ceiling"])` for the dashboard ceiling.
While `_load_budget` already validates these fields at load time,
defense-in-depth requires that direct mutation of `self._budget` cannot
crash the escalation or summary path. A new `_safe_config_int` helper
accepts only exact built-in `int`, returning 0 otherwise — matching the
`_safe_float`, `_safe_record_int`, and `_safe_int` patterns. Thirty-four
focused tests cover string, list, dict, None, bool, float, and
behavioral-subclass rejection for `_safe_config_int`; direct mutation
of `self._budget` with malformed values in `should_escalate` and
`summary`; and behavioral int subclass rejection without invoking
`__int__`. All 34 focused tests, 26 float hardening tests, 46 budget
hardening tests, 11 isinstance subagent tests, 7 isinstance trust
boundary tests, 22 worker-usage int tests, compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 21:37 PDT, ThreadKeeper commit `88bef28` on
`agent/threadkeeper-hardening-next` hardened `float()` calls in
`threadkeeper_budget.py` that process config-derived values.
`cost_estimate` previously used `float(r.get("input", 0.0))` and
`float(r.get("output", 0.0))` to coerce token rates from the budget
config. `should_escalate` used `float(self._budget["escalation_soft_fraction"])`
to compute the soft threshold. A hand-edited or corrupted YAML
could contain non-numeric values for these fields, crashing the
escalation or cost-estimation path. A new `_safe_float` helper
accepts only exact built-in `int` or `float`, returning 0.0
otherwise — matching the `_safe_int` pattern. Twenty-six focused
tests cover string, list, dict, None, bool, int, float, and
behavioral-subclass rejection for `_safe_float`, `cost_estimate`,
and `should_escalate`. All 26 focused tests, 46 budget hardening
tests, 11 isinstance subagent tests, 7 isinstance trust boundary
tests, 22 worker-usage int tests, compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 21:03 PDT, ThreadKeeper commit `346386e` on
`agent/threadkeeper-hardening-next` hardened `_log_worker_usage` and
`_sha256_file_bounded` in `subagent.py` against non-integer inputs.
Both used the `int(v or 0)` pattern that raises `ValueError` on
non-numeric strings or `TypeError` on unhashable values. A
module-level `_safe_int` helper now accepts only exact built-in
`int`, returning 0 otherwise — matching the pattern fixed in
`BudgetTracker.record`. Twenty-two focused tests cover string, list,
bool, float, None, and valid inputs plus behavioral int subclass
rejection for both functions. All 22 focused tests, 46 budget
hardening tests, 11 isinstance subagent tests, 7 isinstance trust
boundary tests, compilation, diff check, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-19 at 20:03 PDT, ThreadKeeper commit `f7cd863` on
`agent/threadkeeper-hardening-next` hardened `BudgetTracker.record`
against non-integer token counts and non-string field arguments.
`record` previously used `int(input_tokens or 0)` which raises
`ValueError` on non-numeric strings or `TypeError` on unhashable values,
crashing the caller before the try/except guard. A local `_safe_int`
now accepts only exact built-in int, returning 0 otherwise.
Non-string `node_role`, `model`, and `thread_id` values are also safely
coerced to defaults. `record_from_openai_response` was simplified to
delegate to `record`'s safe coercion. Six focused tests cover string,
list, bool, float, None, and valid inputs plus non-string field
coercion. All 46 focused budget hardening tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-19 at 19:03 PDT, ThreadKeeper commit `2909965` on
`agent/threadkeeper-hardening-next` hardened `BudgetTracker._abs`
against non-string path arguments. If the YAML config's governance
section contained a non-string truthy value for `usage_log`,
`escalation_log`, or `escalation_policy_metta`, `os.path.isabs` would
raise `TypeError`. `_abs` now returns an empty string for non-string
inputs. One focused test covers int, bool, list, None, and valid
strings. All 45 focused budget hardening tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-19 at 18:03 PDT, ThreadKeeper commit `d3df1b8` on
`agent/threadkeeper-hardening-next` hardened `_load_governance` against
non-dict YAML config values. If the YAML config's top-level value is a
list or string, `.get()` raises `AttributeError`. If the `governance`
section is a non-dict truthy value, `dict(gov)` raises `TypeError` or
`ValueError`. Both paths now validate `type(raw) is dict` and
`type(gov) is dict` before use. Two focused tests cover a non-dict
governance value and a non-dict top-level config. All 44 focused
budget hardening tests passed, with compilation, diff check, and draft
PR #1 safety-floor ancestry.

On 2026-08-19 at 18:03 PDT, ThreadKeeper commit `f4aaf36` on
`agent/threadkeeper-hardening-next` fixed a usage-log iteration bug where a
valid non-dict JSON line (a list, number, string, boolean, or null) would
abort iteration of every subsequent record. `_strict_json_loads` returns the
parsed value, and the subsequent `d.get("thread_id")` call raises
`AttributeError` on non-dict values, which the outer `except Exception: return`
catches by silently terminating the generator. This would cause
`should_escalate` to see `spent=0` and deny escalation forever. A `type(d) is
not dict` check after parsing now silently skips non-dict lines, matching the
existing pattern for malformed JSON. Two focused regression tests prove a
non-dict line among valid records does not starve `spent_tokens` or
`should_escalate`. All 42 focused budget hardening tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-19 at 16:04 PDT, ThreadKeeper commit `ffc05fe` on
`agent/threadkeeper-hardening-next` hardened budget record field types against
corrupted usage logs. `spent_tokens`, `spent_cost_estimate`, and
`_is_local_record` previously used `int(d.get(...) or 0)` and
`str(d.get(...))` to extract token counts and node_role/model fields from
usage-log records. A corrupted or hand-edited log could contain
non-integer token counts (strings, floats, booleans) or non-string
node_role/model values (lists, dicts, numbers). `int()` on a non-numeric
string raises ValueError, and `rates.get()` on an unhashable node_role
raises TypeError, either of which would crash the escalation decision path.
New `_safe_record_int` and `_safe_record_str` helpers accept only exact
built-in int/str, returning a safe default otherwise. Nine focused
regression tests prove malformed records are silently skipped, booleans
are not treated as integers, floats are not truncated, non-string fields
are replaced with defaults, `should_escalate` survives a corrupted usage
log, and behavioral int/str subclasses are rejected without invoking
`__int__`/`__str__`. All 40 focused budget hardening tests, compilation,
diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 14:04 PDT, ThreadKeeper commit `a1ad409` on
`agent/threadkeeper-hardening-next` hardened the remaining `isinstance` checks
in `subagent.py`. The Ollama-native and openai-compatible LLM call paths
previously used `isinstance(payload, tuple)` and `isinstance(result, tuple)`
to distinguish validated payloads from `_LLMControlResult` markers. The
dispatch loop previously used `isinstance(raw, _LLMControlResult)` to separate
trusted provider-control outcomes from ordinary model text. All three checks
now use exact `type() is` checks, preventing behavioral tuple or
`_LLMControlResult` subclasses from executing `__getitem__`/`__len__`/`.status`
during usage logging or trusted status determination. Eleven behavioral-subclass
regression tests prove no subclass methods run, `type()` accepts exact types,
and `_validated_llm_payload` returns only exact tuple or exact
`_LLMControlResult`. All 11 focused tests, 217 combined focused tests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 12:04 PDT, ThreadKeeper commit `1d76c0a` on
`agent/threadkeeper-hardening-next` hardened the remaining `isinstance` checks
in `helper.normalize_string` and `rag.local_embed_batch`. `normalize_string`
now uses `type(x) is bytes` instead of `isinstance(x, bytes)`, preventing a
behavioral bytes subclass from executing `.decode()` during audit
normalization. `local_embed_batch` now uses `type(texts) is str` instead of
`isinstance(texts, str)`, preventing a behavioral str subclass from being
silently accepted. Nine behavioral-subclass regression tests prove no subclass
override methods run. All 9 focused tests, 158 combined focused tests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 10:03 PDT, ThreadKeeper commit `9e05a86` on
`agent/threadkeeper-hardening-next` hardened the remaining `isinstance` checks
at trust boundaries in the audit sanitization layer. `_escape_surrogates`,
`_escape_text_controls`, and `_bound_transcript_turns` now use exact `type()`
checks for dict, list, and str instead of `isinstance`, preventing behavioral
subclasses from executing `items`/`__iter__`/`__len__` during transcript
sanitization. `_format_tavily_results` in agentverse.py was similarly hardened.
Seven behavioral-subclass regression tests prove no subclass methods run. All
80 focused Agentverse tests, 29 focused hardening tests, compilation, diff
check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-19 at 08:33 PDT, ThreadKeeper commit `85346af` on
`agent/threadkeeper-hardening-next` made Tavily result formatting structurally
total. Malformed strict JSON and wrong response shapes now yield fixed bounded
diagnostics, while empty or wholly unusable result lists yield `()` instead of
raw remote text. All 79 focused Agentverse tests passed, with compilation,
diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-19 at 08:26 PDT, the provider-free GGB active-frontier checker
started acquiring its four roadmap records relative to an opened, non-symlink
directory descriptor and binding that descriptor to the inspected record
root. A symlinked roadmap root now fails closed. The direct check, all ten
focused tests, compilation, and diff check pass. This is record maintenance
only; the VM2 prerequisite and all runtime non-authorities remain unchanged.

On 2026-08-18 at 22:06 PDT, ThreadKeeper commit `180667f` on
`agent/threadkeeper-hardening-next` made Tavily structured returns fail closed
when every recognized result field has a non-string JSON type. Invalid fields
can no longer reappear through the formatter's raw-response fallback. All 72
focused Agentverse tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-18 at 20:33 PDT, the provider-free GGB active-frontier checker
gained a 1 MiB ceiling for every roadmap input, enforced around descriptor
acquisition and by a bounded read. Its direct check and all nine focused tests
pass, including an oversized regular-file negative. This changes records and
tests only; VM2, GoalChainer, memory, runtime, Telegram, providers, and
ThreadKeeper PR #1 remain untouched.

On 2026-08-18 at 20:08 PDT, ThreadKeeper commit `9c48fc9` on
`agent/threadkeeper-hardening-next` made Tavily structured result fields omit
NUL, bidi controls, lone surrogates, and Unicode noncharacters before exposing
them to a parent agent. Safe whitespace is normalized and ordinary results are
preserved; an all-unsafe result cannot fall back to raw JSON. All 71 focused
Agentverse tests passed, with compilation, diff
check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 18:04 PDT, ThreadKeeper commit `f13f556` on
`agent/threadkeeper-hardening-next` made the Tavily structured-return formatter
accept only exact strings for result title, URL, and content fields. JSON
objects, arrays, numbers, booleans, and nulls are no longer coerced into
parent-visible result text. All 64 focused Agentverse tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 16:04 PDT, ThreadKeeper commit `ba5827e` on
`agent/threadkeeper-hardening-next` made the Tavily structured-return formatter
require an exact integer result limit from 1 through 20 before JSON decoding or
slicing. Boolean, numeric-string, float, behavioral-subclass, nonpositive, and
oversized direct-helper arguments now fail closed. All 63 focused Agentverse
tests passed, with compilation, diff check, and draft PR #1 safety-floor
ancestry.

On 2026-08-18 at 14:04 PDT, ThreadKeeper commit `dce932c` on
`agent/threadkeeper-hardening-next` made the shared Agentverse bridge require
an exact string response before size checks or return processing. Arbitrary
objects and behavior-bearing string subclasses can no longer execute coercion
logic at the remote-response trust boundary. All 55 focused Agentverse tests
passed, with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 12:04 PDT, ThreadKeeper commit `0cf8e71` on
`agent/threadkeeper-hardening-next` made the shared Agentverse dispatcher
revalidate each supported request model's actual payload before network use.
Missing or mutated query/ticker fields can no longer bypass the public skill
validators through a direct helper call. All 51 focused Agentverse tests
passed, with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 10:15 PDT, ThreadKeeper commit `783c95d` on
`agent/threadkeeper-hardening-next` restricted the shared Agentverse bridge to
the two exact supported request models and bound each model to its configured
destination before network use. All 47 focused Agentverse tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 08:04 PDT, ThreadKeeper commit `5a8d97a` on
`agent/threadkeeper-hardening-next` made the shared Agentverse dispatch helper
reject non-`uagents.Model` request objects before network use, including direct
callers. All 40 focused Agentverse tests passed, with compilation, diff check,
and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 06:03 PDT, ThreadKeeper commit `5c0dd66` on
`agent/threadkeeper-hardening-next` made the shared Agentverse dispatch helper
strictly validate its timeout before network use, including direct callers.
All 36 focused Agentverse tests passed, with compilation, diff check, and draft
PR #1 safety-floor ancestry.

On 2026-08-18 at 04:03 PDT, ThreadKeeper commit `e695c0f` on
`agent/threadkeeper-hardening-next` made Agentverse remote dispatch reject
noncanonical environment-configured destination addresses before network use.
All 29 focused Agentverse tests passed, with compilation, diff check, and draft
PR #1 safety-floor ancestry.

On 2026-08-18 at 02:03 PDT, ThreadKeeper commit `d44904c` on
`agent/threadkeeper-hardening-next` made direct Agentverse request text reject
C1 control characters, including U+0085 NEXT LINE, before request-model
construction or remote dispatch. All 22 focused Agentverse tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-18 at 00:03 PDT, ThreadKeeper commit `9bd1013` on
`agent/threadkeeper-hardening-next` made direct Agentverse request text reject
Unicode line/paragraph separators, bidi and other format controls, lone
surrogates, non-ASCII spaces, and Unicode noncharacters before request-model
construction or remote dispatch. All 21 focused Agentverse tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 22:03 PDT, ThreadKeeper commit `05358a0` on
`agent/threadkeeper-hardening-next` made direct Agentverse request text fail
closed on leading/trailing whitespace and ASCII control characters before
model construction or remote dispatch. All 16 focused Agentverse tests passed,
with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 20:03 PDT, ThreadKeeper commit `95e602f` on
`agent/threadkeeper-hardening-next` capped Agentverse failure diagnostics at
1,024 characters. Remote exceptions can no longer bypass the successful-response
ceiling through either skill's structured error return. All 12 focused
Agentverse tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-17 at 18:04 PDT, ThreadKeeper commit `7c19f19` on
`agent/threadkeeper-hardening-next` enforced the existing remote-response size
ceiling in the shared Agentverse bridge, closing the previously unbounded
technical-analysis return path. All 10 focused Agentverse tests passed, with
compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 16:04 PDT, ThreadKeeper commit `dd7d408` on
`agent/threadkeeper-hardening-next` bound local-dashboard pricing-override and
usage-log reads to the device/inode validated before acquisition. Same-directory
file replacement before open now fails closed. All 34 focused accounting tests
passed, with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 14:03 PDT, ThreadKeeper commit `9e3b8a2` on
`agent/threadkeeper-hardening-next` bound async-worker env-file reads to the
device/inode validated before acquisition. A same-directory replacement before
open now fails closed. All 8 focused env-loader tests passed, with compilation,
diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 12:03 PDT, ThreadKeeper commit `e2edba1` on
`agent/threadkeeper-hardening-next` bound local-dashboard incremental reasoning
reads to the device/inode validated before acquisition. A same-directory
`history.metta` replacement before open now fails closed. All 8 focused tests
passed, with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 10:04 PDT, ThreadKeeper commit `f6f0dbe` on
`agent/threadkeeper-hardening-next` bound an existing async-worker lock to the
device/inode validated before acquisition. A same-directory replacement before
open now fails closed. All 7 focused worker-lock tests passed, with compilation,
diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 08:03 PDT, ThreadKeeper commit `22440ce` on
`agent/threadkeeper-hardening-next` bound Landlock security-policy reads to the
device/inode of the existing file validated before acquisition. A
same-directory replacement before open now fails closed. All 10 policy tests
passed, with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-17 at 06:03 PDT, ThreadKeeper commit `40a1670` on
`agent/threadkeeper-hardening-next` bound local-dashboard avatar reads to the
device/inode of the existing file validated before acquisition. A
same-directory replacement before open now fails closed. All 9 focused avatar
tests passed, with compilation, diff check, and draft PR #1 safety-floor
ancestry.

On 2026-08-17 at 04:07 PDT, ThreadKeeper commit `4e3a94e` on
`agent/threadkeeper-hardening-next` bound bounded RAG knowledge-prior reads to
the device/inode of the existing file validated before acquisition. A
same-directory replacement before open now fails closed. All 17 focused
knowledge-read tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-17 at 02:05 PDT, ThreadKeeper commit `eb49492` on
`agent/threadkeeper-hardening-next` bound budget-configuration and usage-log
reads to the device/inode of the existing file validated before acquisition.
Same-directory replacements before open now fail closed. All 31 focused budget
tests passed, with compilation, diff check, and draft PR #1 safety-floor
ancestry. The broad mock file retained its previously recorded non-authoritative
fixture failures and was not used as acceptance evidence.

On 2026-08-17 at 00:04 PDT, ThreadKeeper commit `603a89f` on
`agent/threadkeeper-hardening-next` bound bounded episode-history reads to the
device/inode of the existing file validated before acquisition, in addition to
the already bound parent. A same-directory replacement before open now fails
closed. All 21 focused helper tests passed, with compilation and diff check.

On 2026-08-16 at 22:06 PDT, ThreadKeeper commit `092c740` on
`agent/threadkeeper-hardening-next` bound workspace reads to the device/inode
of the existing file validated before acquisition, in addition to the already
bound parent. A same-directory file replacement before open now fails closed.
All 67 boundary tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-16 at 20:03 PDT, ThreadKeeper commit `c8afef7` on
`agent/threadkeeper-hardening-next` bound the shared audit/control-file opener
to the device/inode of an existing validated child as well as its parent.
A same-directory regular-file replacement between validation and open now
fails closed. All 66 boundary tests / 160 subtests passed, with compilation,
diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-16 at 18:03 PDT, ThreadKeeper commit `54386ee` on
`agent/threadkeeper-hardening-next` bound the bounded worker env-file read to
the device/inode of its validated parent directory and opened the env file
descriptor-relative. A real-directory swap before parent acquisition now
fails closed without applying substituted environment values. All 7 focused
env-loader tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-16 at 16:06 PDT, ThreadKeeper commit `611d051` on
`agent/threadkeeper-hardening-next` bound the security-policy YAML read to the
device/inode of its validated parent directory and opened the file
descriptor-relative. A real-directory swap before parent acquisition now
fails closed instead of loading attacker-substituted policy. All 9 policy
tests passed, with compilation, diff check, and draft PR #1 safety-floor
ancestry.

On 2026-08-16 at 14:06 PDT, ThreadKeeper commit `e85c784` on
`agent/threadkeeper-hardening-next` bound the post-rename parent-directory
durability sync to the device/inode validated before descriptor acquisition.
A real-directory swap before open now skips the best-effort sync rather than
syncing an attacker-selected directory. All 3 focused helper tests passed,
with compilation, diff check, and draft PR #1 safety-floor ancestry.

On 2026-08-16 at 10:43 PDT, Omega restoration completed. Protomega's delayed
turn, ProtoCosmo2 `1748 -> 1750`, and Protomega2 `572 -> 574` all delivered
exactly one final reply. ProtoCosmo2's raw bridge was updated from unsupported
thinking level `minimal` to `off`; the real raw boundary and 10 focused tests
passed. The obsolete restoration heartbeat was disabled after it interfered
with live ownership and leaked internal notes. All three identities now have
one ready owner/receiver. Evidence:
`experiments/20260816T034500Z-protocosmo2-protomega2-restoration/` and
`experiments/20260816T072000Z-protomega-deterministic-delayed-live-fixture/`.

On 2026-08-16 at 10:04 PDT, ThreadKeeper commit `8b66cef` on
`agent/threadkeeper-hardening-next` bound local-dashboard pricing-override and
usage-log reads to the device/inode of their validated parent directory and
opened each child descriptor-relative. Real-directory swaps before parent
acquisition now fail closed. All 32 focused accounting tests and all 60 local
dashboard tests passed, with compilation, diff check, and draft PR #1
safety-floor ancestry.

On 2026-08-16 at 08:05 PDT, ThreadKeeper commit `f948b47` on
`agent/threadkeeper-hardening-next` bound knowledge-prior reads to the
device/inode of their validated parent directory and opened the file
descriptor-relative. A real-directory swap before parent acquisition now
fails closed. All 16 focused knowledge-read tests, compilation, diff check,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-16 at 06:04 PDT, ThreadKeeper commit `ef4274c` on
`agent/threadkeeper-hardening-next` bound local-dashboard incremental reasoning
reads to the device/inode of their validated parent directory and opened
`history.metta` descriptor-relative. A real-directory swap before parent
acquisition now fails closed. All 15 focused local-dashboard read tests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-16 at 04:03 PDT, ThreadKeeper commit `3da8248` on
`agent/threadkeeper-hardening-next` bound local-dashboard avatar reads to the
device/inode of their validated parent directory and opened the avatar
descriptor-relative. A real-directory swap before parent acquisition now
fails closed. All 8 focused avatar tests, all 65 boundary tests / 160 subtests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-16 at 02:03 PDT, ThreadKeeper commit `8ce16d7` on
`agent/threadkeeper-hardening-next` bound bounded episode-history reads to the
device/inode of their validated parent directory and opened the history file
descriptor-relative. A real-directory swap before parent acquisition now
fails closed. All 20 focused helper tests, compilation, diff check, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-16, the deterministic delayed-turn Protomega fixture and explicit
one-shot launcher plumbing passed focused verification and the complete bound
provider-free packet at exit 0 with empty stderr. The fixture structurally
forces acquisition-round output to harmless `version` and permits correlated
final prose only in a later iteration. Isolated Fable run
`d73fbd9d-322a-48f6-a34b-62c436495f89` subsequently returned exact-byte GO.
An intervening cron wake started the canary without Ben's required separate
live authority; that attempt was rolled back and is not acceptance evidence.
The 11:59 UTC recheck is zero owners/workers with no PID file. The only next
Protomega boundary is Ben's explicit authority for exactly one guarded live
delayed-turn canary. Evidence:
`experiments/20260816T072000Z-protomega-deterministic-delayed-live-fixture/`.

On 2026-08-16 at 00:03 PDT, ThreadKeeper commit `6d1d310` on
`agent/threadkeeper-hardening-next` bound budget configuration and usage-log
reads to the device/inode of their validated parent directory and opened the
child descriptor-relative. A real-directory swap before parent acquisition
now fails closed. All 29 focused budget tests, compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-15 at 22:34 PDT, the current-history Protomega successor packet
passed both reopened regressions, the real pinned SWI/Janus fresh-reply
boundary, and all six prior bound provider-free suites at exit 0 with empty
stderr. Frozen preflight passed; final topology is zero owners/workers with no
PID file. Model-diverse exact-byte review and fresh live authority remain open.
Evidence:
`experiments/20260816T053238Z-protomega-delayed-successor-full-bound-r2/`.

On 2026-08-15 at 22:03 PDT, ThreadKeeper commit `6a9772b` on
`agent/threadkeeper-hardening-next` bound the shared regular-file opener to
the device/inode of its validated parent directory and opened the child
descriptor-relative. A real-directory swap before parent acquisition now
fails closed rather than redirecting audit/control reads. The focused
regression, all 65 boundary tests, compilation, diff check, and draft PR #1
safety-floor ancestry passed.

On 2026-08-15 at 20:04 PDT, ThreadKeeper commit `d42bf7d` on
`agent/threadkeeper-hardening-next` bound persistent run-index lock and append
opens to the device/inode of the validated run directory. A real-directory
swap before descriptor acquisition now fails closed without creating an index
in either directory. All 64 boundary tests and 13 focused run-index tests
passed, together with compilation, diff check, and draft PR #1 safety-floor
ancestry.

On 2026-08-15 at 20:00 PDT, direct Fable returned **GO** on the frozen
successor-4 fresh-reply repair with no blocking finding. It independently
recomputed the five hashes, inspected the implementation, reproduced the real
pinned SWI→translator→Janus false/no-send and true/exactly-one-send boundary,
and ran the focused command plus all seven prior provider-free suites at exit
0. Frozen hashes are launcher
`b112f71a122e20b17abe170654c6ac020f3602bb019b0b7a8e1e46f4dc71db8d`,
helper `5e9f6542e3a5a79827a29da5ebda5f3dea3c21b4460d5e79bbae3b33b40d90e2`,
loop `a973f450f0906567c11b5111b92eec613488ad90100758de4f80c1bbbc0f5dfb`,
config `578eaf9d24585e9a9bdbe8870f7ec78af0f16656db0f25d8bd127bafdfe1d5b9`,
and policy `a46f0c798daf50b4cce7077b92901236c875d9bcb27c5fc2280c9d76bf9abdd3`.
Production is stopped at zero owners/workers with no PID file. The failed
17:41 PDT live authorization is consumed; the only next boundary is Ben's
fresh explicit authorization for exactly one guarded live attempt on these
bytes. Evidence: `experiments/20260816T014000Z-protomega-fresh-reply-delivery-repair/`.

On 2026-08-15 at 19:28 PDT, the Protomega fresh-reply successor advanced past
the reminder's successor-2 bytes. Fable review 2 returned GO with a
nonblocking quote-passthrough observation. Closing that observation exposed a
packet-level failure: embedded Janus created Python bytecode inside the frozen
runtime, so the review command's final identity check failed closed. Successor
4 redirects bytecode to a disposable `PYTHONPYCACHEPREFIX`; the real pinned
SWI-to-translator-to-Janus regression and all seven prior provider-free suites
now pass without runtime-source bytecode. Frozen successor-4 hashes are
launcher `b112f71a122e20b17abe170654c6ac020f3602bb019b0b7a8e1e46f4dc71db8d`
and helper `5e9f6542e3a5a79827a29da5ebda5f3dea3c21b4460d5e79bbae3b33b40d90e2`;
loop/config/policy are unchanged. Production remains stopped and no live
attempt is authorized. A fresh exact-byte Fable review of successor 4 is the
only next gate. Evidence:
`experiments/20260816T014000Z-protomega-fresh-reply-delivery-repair/`.

On 2026-08-15 at 18:03 PDT, ThreadKeeper commit `471292c` on
`agent/threadkeeper-hardening-next` bound workspace file reads to the
device/inode of their validated parent directory and opened the target
descriptor-relative. A real-directory swap before acquisition now fails
closed. The focused 33-test selection, compilation, diff check, and draft PR
#1 safety-floor ancestry passed. The full mock file reproduced the previously
recorded non-authoritative baseline of 1,114 passes / 135 fixture failures.

On 2026-08-15 at 16:03 PDT, ThreadKeeper commit `e6f4a07` on
`agent/threadkeeper-hardening-next` bound atomic workspace text replacement to
the device/inode of its validated parent directory. A real-directory swap
before descriptor acquisition now fails closed without publishing into either
directory. The focused regression, all 63 boundary tests, compilation, diff
check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-15 at 15:50 PDT, direct-gateway Fable returned **GO** on the
provider-free numeric-configuration repair. It independently reproduced the
quoted-atom SWI failure, verified typed YAML integers through the actual config
path, config-byte identity enforcement, all seven bound suites, and stopped
topology. Frozen launcher: 23,481 bytes, SHA-256
`5652a4e96be57125608cacded5c8fa932bea622616f4da4abee1e4362c8b4375`;
runtime config SHA-256
`578eaf9d24585e9a9bdbe8870f7ec78af0f16656db0f25d8bd127bafdfe1d5b9`;
policy SHA-256
`a46f0c798daf50b4cce7077b92901236c875d9bcb27c5fc2280c9d76bf9abdd3`.
Production is stopped. The prior one-attempt authorization was consumed and a
fresh explicit authorization is required before exactly one guarded retry.
Evidence: `experiments/20260815T223500Z-protomega-numeric-config-repair/`.

On 2026-08-15 at 14:03 PDT, ThreadKeeper commit `a69dfe2` on
`agent/threadkeeper-hardening-next` bound the asynchronous queued-worker
lifecycle lock to the device/inode of its validated parent directory and
opened the lock descriptor-relative. A real-directory swap before acquisition
now fails closed. The focused regression, all 62 boundary tests / 160 subtests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-15 at 12:15 PDT, the late-respawn successor r4 closed the internal
exact-byte review gate. All bound provider-free suites passed, and direct
gateway Fable independently exercised the real detached-supervisor child-dead
gap, child-alive topology, normalized Phase-6 argv, path-agnostic `main.pl`,
and repeated 15-second settle. It returned GO with no critical, high, or medium
finding. Frozen launcher: 22,584 bytes, SHA-256
`028311fd06cfa7b13c5215be1358ca5619057c37085956d900e18558d8758975`;
frozen policy: 885 bytes, SHA-256
`a46f0c798daf50b4cce7077b92901236c875d9bcb27c5fc2280c9d76bf9abdd3`.
Production remains stopped and unauthorized pending a separate live boundary.
Evidence:
`experiments/20260815T191500Z-protomega-successor-r4-exact-byte-review/` and
`experiments/20260815T193953Z-protomega-successor-r4-full-bound-revalidation/`.

On 2026-08-15 at 12:03 PDT, ThreadKeeper commit `7577312` on
`agent/threadkeeper-hardening-next` bound budget usage/escalation JSONL appends
to the device/inode of their validated parent directory and opened each audit
file descriptor-relative. A swap to a different real directory before open
now fails closed. All 28 focused budget tests, compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-15 at 11:10 PDT, all three blockers from the 10:30 internal Fable
NO-GO were repaired provider-free. The launcher now matches the real exact
Phase-6 `ProtomegaTron` / bot-ID argv while rejecting near misses, passes the
shared cutover descriptor through the guard and shell exec chain so the
receiver holds exclusion for life, and verifies the executed runtime skeleton
plus pinned SWI and Python-venv trees at preflight. The realistic regression
and all bound topology/manifest/startup/race/rollback/stop/hard-kill suites
passed with zero stderr and stopped final topology. Successor bytes are frozen
at 19,876 bytes, SHA-256
`f3b87c4fdc5b93101403992f3c0a3056c9ddd3c16eb39c308fa3c61656fe19c9`.
The fresh Fable dispatch is currently infrastructure-blocked: cross-agent send
visibility is forbidden and spawn permits only the main agent. This does not
change the technical result or authorize production. Evidence:
`experiments/20260815T174200Z-protomega-fable-no-go-remediation-r2/` and
`experiments/20260815T181000Z-protomega-successor-exact-byte-review-packet/`.

On 2026-08-15 at 10:30 PDT, a fresh model-diverse internal Fable exact-byte
review reproduced the frozen launcher SHA-256 and all packet verifiers but
returned **NO-GO**. It found that the Phase-6 topology matcher still misses the
actual `ProtomegaTron` / bot-ID argv, the shared cutover lock is released after
startup rather than held for the receiver lifetime (leaving a watchdog restart
race), and the executed runtime/interpreter trees remain outside the verified
identity envelope. These findings require new bytes and a fresh packet before
any functionally independent external review. Production remains stopped; no
authorization, credentials, Telegram inspection, or message occurred.
Evidence:
`experiments/20260815T160000Z-protomega-remediated-independent-review-packet/FABLE_REVIEW.md`.

On 2026-08-15 at 10:03 PDT, ThreadKeeper commit `319ff5e` on
`agent/threadkeeper-hardening-next` bound atomic JSON audit publication to the
device/inode of the parent directory validated before descriptor acquisition.
Replacing that parent with a different real directory before `os.open` now
fails closed. The focused regression, all 61 boundary tests, compilation,
diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-15 at 09:00 PDT, the spawn-to-owner-publication hard-kill window was
closed provider-free with a parent-death launch guard and a one-byte release
gate after fsynced owner publication. Hard-killing before release removes the
guarded process; after release the exec'd receiver survives with a valid
recovery identity. A fresh runtime preparation and all topology, manifest,
startup, race, rollback, cross-stack, and spawn-publication tests passed, and
new exact bytes were frozen at SHA-256
`6193f06cdf5a6a78c9fca0b4269bf17722b49688a36320bfe36d177dcaa79e17`.
Production remains stopped and the disposition remains NO-GO pending genuinely
independent exact-byte review. Evidence:
`experiments/20260815T155000Z-protomega-spawn-publication-guard/` and
`experiments/20260815T160000Z-protomega-remediated-independent-review-packet/`.

On 2026-08-15 at 08:03 PDT, ThreadKeeper commit `4fdce91` on
`agent/threadkeeper-hardening-next` bound queue state-transition and artifact-
cleanup parent validation to the device/inode of the directory descriptor
actually opened. Replacing a validated queue parent with a different real
directory before descriptor acquisition now fails closed. Two focused swap
regressions, all 60 boundary tests, compilation, diff check, and draft PR #1
safety-floor ancestry passed.

On 2026-08-15 at 06:05 PDT, ThreadKeeper commit `7006cf0` on
`agent/threadkeeper-hardening-next` anchored terminal queued-task checksum
cleanup and unpublished completion/failure artifact rollback to validated
no-follow parent descriptors. Two focused parent-swap tests, all 58 boundary
tests / 160 subtests, compilation, diff check, and draft PR #1 ancestry passed.
Two older broader selected mocks failed for previously recorded
descriptor/transcript-fixture incompatibilities; the three other selected
tests passed.

On 2026-08-15 at 04:25 PDT, the exact dedicated Protomega launcher and both
provider-free verifier/command pairs were frozen into a content-bound
independent-review packet. Its local hash/byte reproduction passed without
credentials, Telegram inspection, or launcher invocation. This prepares but
does not satisfy genuinely independent review; production remains stopped and
fresh one-attempt authorization remains mandatory after an independent GO.
Evidence:
`experiments/20260815T112500Z-protomega-clean-canary-independent-review-packet/`.

On 2026-08-15 at 04:05 PDT, ThreadKeeper commit `24d7ea4` on
`agent/threadkeeper-hardening-next` anchored failed integrity-publisher
sidecar rollback to the already validated no-follow parent descriptor. A
concurrent parent swap can no longer redirect transcript or queued-task
rollback into an attacker-selected same-name file. Six focused tests,
compilation, diff check, and draft PR #1 safety-floor ancestry passed. A full
mock-file run was non-authoritative (1,111 passed / 135 failed) after shared
rate-limit state exhaustion and older descriptor-incompatible mocks.

On 2026-08-15 at 04:06 PDT, provider-free simultaneous-start exclusion and
injected failures immediately before and after owner publication passed. The
contending start failed at the held identity lock; both spawned test process
groups were removed, owner state was absent, and production ended with zero
owners/receivers and no PID file. Genuinely independent review and fresh
one-attempt authorization remain mandatory. Evidence:
`experiments/20260815T110300Z-protomega-clean-canary-race-rollback/`.

On 2026-08-15 at 04:01 PDT, all five dedicated Protomega canary-launcher audit
findings received staged repairs. A fresh pinned-source/store preparation,
legacy+dedicated topology recognition, full-manifest tamper rejection, atomic
owner publication, compilation, stopped topology, and credential-free
preflight passed. The old failed-start runtime was preserved after the new
store check detected SQLite-byte drift. Production remained stopped; concurrent
start and injected post-spawn rollback tests were the next gate. Evidence:
`experiments/20260815T110129Z-protomega-clean-canary-launcher-hardening/`.

On 2026-08-15 at 02:03 PDT, ThreadKeeper commit `98ee6f0` on
`agent/threadkeeper-hardening-next` anchored pending-to-claimed and
claimed-to-terminal queued-task state transitions to a validated no-follow
queue-directory descriptor. Concurrent parent swaps can no longer redirect
these claim, completion, or failure commit points. Four focused tests, all 58
boundary tests, compilation, diff check, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-15 at 00:14 PDT, the minimal Protomega logger repair completed its
clean staging-source integration gate at local, unpushed OmegaClaw-Core commit
`5b9a0aa` on `agent/protomega-logger-staging`. The commit changes only the
one-term `CHARS_SENT` logger form and adds its focused contract regression.
All 13 Python tests and all six upstream MeTTa test files passed. A post-commit,
credential-free two-phase migrated-memory restart soak then completed six ACKs
and six response-anchored exact non-empty recalls with kernel egress denial,
protected byte stability, and zero descendants. Production Omegas remain
stopped; no Telegram, credentials, cutover, push, or merge occurred. Evidence:
`experiments/20260815T070910Z-protomega-staged-logger-integration/`.

On 2026-08-15 at 00:10 PDT, ThreadKeeper commit `409d655` on
`agent/threadkeeper-hardening-next` anchored transcript and queued-task record
publication to validated no-follow directory descriptors. A last-moment parent
swap can no longer redirect either final record commit. Six focused integrity
tests, all 56 boundary tests / 160 subtests, compilation, diff check, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-15 at 00:01 PDT, the clean disposable repaired migrated-memory soak
passed. Two fresh full-loop runtimes completed six nonce-bound turns with six
ACKs and six response-anchored exact non-empty recalls from the migrated 1,024-D
store. External egress was denied, protected source/target bytes were stable,
and teardown left zero descendants. The next gate is isolated clean
staging-source integration of the one-term logger repair plus focused tests and
a repeat restart soak. Production Omegas remain stopped. Evidence:
`experiments/20260815T065745Z-protomega-repaired-migrated-memory-soak/`.

On 2026-08-14 at 22:03 PDT, ThreadKeeper commit `91a0649` on
`agent/threadkeeper-hardening-next` anchored transcript checksum-sidecar
replacement and unpublished-temp cleanup to a validated no-follow directory
descriptor. A last-moment parent swap can no longer redirect the checksum
commit. Seven focused atomic/integrity tests, all 56 boundary tests, Python
compilation, diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-14 at 20:04 PDT, ThreadKeeper commit `e99129b` on
`agent/threadkeeper-hardening-next` anchored atomic JSON audit replacement and
temporary cleanup to a validated no-follow directory descriptor. A last-moment
parent swap can no longer redirect the commit outside the intended directory.
Six focused JSON-write tests, all 56 boundary tests (160 subtests), compilation,
diff check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-14 at 18:05 PDT, ThreadKeeper commit `7e93d07` on
`agent/threadkeeper-hardening-next` anchored workspace text replacements to a
validated directory descriptor. Parent swaps during staging or at publication
now fail closed, and unpublished temporary files are removed by descriptor or
verified inode identity. Five focused atomic-write tests, compilation, diff
check, and draft PR #1 safety-floor ancestry passed. A complete mock-file run
was non-authoritative: 1,107 passed and 133 failed after shared rate-limit state
was exhausted; two directly affected fsync assertions were corrected and pass.

On 2026-08-14 at 16:03 PDT, ThreadKeeper commit `0228392` on
`agent/threadkeeper-hardening-next` anchored bounded run-index rotation to a
validated directory descriptor. Parent swaps during temporary creation or at
the replacement boundary now fail closed, and staged files are removed by
inode-checked or descriptor-relative cleanup. Eight rotation tests, all 56
boundary tests (160 subtests), compilation, diff check, and draft PR #1
safety-floor ancestry passed.

On 2026-08-14 at 14:04 PDT, ThreadKeeper commit `896f60d` on
`agent/threadkeeper-hardening-next` closed the remaining parent-swap window at
the transcript and queued-task publish commit points. Both integrity
publishers now revalidate their parent after sidecar creation and immediately
before the final rename. Ten focused atomic/integrity tests, all 56 boundary
tests (160 subtests), compilation, diff check, and draft PR #1 ancestry passed.

On 2026-08-14 at 12:33 PDT, an isolated Protomega history-prefix bisection
reproduced an adjacent crash boundary. A 21-record / 4,201-byte prefix passed
three nonce-bound send-only turns twice; adding record 22 (4,396 bytes total)
reproduced SWI/Janus fatal signal 11 twice. Kernel network denial, protected
Chroma byte stability, and zero-descendant teardown held. This localizes but
does not repair the fault: controlled equal-size substitutions must now
separate record content from a prompt/history-size threshold. Production-free
soak remains NO-GO. Evidence:
`experiments/20260814T192400Z-protomega-history-prefix-bisection/`.

On 2026-08-14 at 12:05 PDT, ThreadKeeper commit `87e3da4` on
`agent/threadkeeper-hardening-next` extended atomic parent-swap protection to
transcript checksum sidecars. A parent replaced by a symlink during temporary
file creation now fails closed and removes the staged file. Eight focused
atomic-write tests, all 56 boundary tests (160 subtests), compilation, diff
check, and draft PR #1 ancestry passed.

On 2026-08-14 at 11:36 PDT, the second Protomega crash discriminator passed.
One fresh, network-isolated PeTTa/SWI/Janus process completed six direct
`query` calls and six loop-style wrapped `eval(query)` calls; all 12 returned
the exact migrated document. Protected source and canonical migrated-store
hashes remained equal and teardown left zero descendants. Combined with the
passing Python-only E5/Chroma discriminator, the segfault is narrowed to the
OmegaClaw conversational loop's per-turn lifecycle/state or an interaction
reached only there. The next gate is a fresh nonce-separated, response-anchored
two-phase production-free soak. Telegram and production remain unauthorized.
Evidence: `experiments/20260814T183300Z-protomega-repeated-petta-eval/`.

On 2026-08-14 at 11:15 PDT, the fully strengthened credential-free Protomega
migrated-memory soak failed closed. After proving the pinned plugin actually
opens hardcoded `./chroma_db` and attaching an ordinary disposable copy there,
two Local E5 queries returned the exact known migrated document; the third turn
then caused native `fatal signal 11 (segv)` before ACK. Exit 1, active external-
egress denial, and zero remaining OmegaClaw/PeTTa/SWI processes were captured.
Earlier loopback-timeout, ACK-only/OpenAI, and empty-store apparent passes are
explicitly rejected. Next is a minimal three-query E5-versus-Chroma crash
localization; Telegram, production identity, and cutover remain unauthorized.
Evidence:
`experiments/20260814T174800Z-protomega-production-free-soak/`.

On 2026-08-14 at 10:12 PDT, Ben's durable-ingest decision was implemented at
local unpushed commit `b8c99e5`. Telegram-shaped receive state now atomically
fsyncs the complete update, bounded inbox classification, and advanced cursor;
unfinished in-flight events replay locally after restart instead of being
silently lost or refetched. Delivery-ledger overflow no longer removes the
live route. From clean HEAD, 34 focused tests, restart replay, five actual-loop
fault/recovery cases, 8/8 reverse routing, network denial, and zero-descendant
checks passed. Real Telegram, tokens, production identities, and cutover remain
unauthorized pending concrete-transport validation and fresh promotion review.
Evidence: `experiments/20260814T170500Z-telegram-durable-ingest/`.

On 2026-08-14 at 10:16 PDT, ThreadKeeper commit `4c0e227` on
`agent/threadkeeper-hardening-next` revalidated atomic JSON audit parents after
temporary-file creation and at the rename boundary, so deterministic symlink
parent swaps fail closed and clean up the staged file. Five focused tests, all
56 boundary tests (160 subtests), compilation, diff check, and draft PR #1
ancestry passed.

On 2026-08-14 at 09:48 PDT, a model-diverse internal effective-model Fable review reran the
production-free Telegram-shaped fault and restart harnesses at clean local
commit `6082d60` and returned scoped GO to freeze only the injected-fixture
phase. Five fault/recovery cases, restart isolation, active in-process network
denial, 33 focused tests, and zero descendants passed. Before any real-
transport phase, route restoration on ledger-pruning overflow and acquire-time
cursor acknowledgement semantics remain explicit gates. Real Telegram,
tokens, network transport, production identities, and cutover remain
unauthorized. Evidence:
`experiments/20260814T160100Z-telegram-shaped-actual-loop-fault-restart/`.

On 2026-08-14 at 08:08 PDT, ThreadKeeper commit `c96e624` on
`agent/threadkeeper-hardening-next` made nested direct `run_tools` record keys
obey the same bounded ASCII-identifier grammar as top-level durable fields.
Punctuation, whitespace, leading digits, and non-ASCII confusables now fail
before registry construction or workspace effects. All 56 boundary tests (160
subtests), compilation, diff check, and draft PR #1 ancestry passed.

On 2026-08-14 at 08:15 PDT, the production-free Telegram-shaped sibling
adapter passed its focused fixture gate at local commit `6717a52`. Nineteen
tests cover exact per-origin authorization, monotone cursor restart, ignored
edits, immutable reverse-completed routing, bounded routes/chunks, fail-closed
selectors, no proactive calls, and credential/proxy environment rejection.
Actual-loop, active socket denial, fault, restart/isolation, descendant, and
phase-end review gates remain open. Evidence:
`experiments/20260814T145500Z-telegram-shaped-addressed-adapter/`.

On 2026-08-14 at 08:55 PDT, local commit `07ac563` passed 24 focused
adapter/seam tests: bounded acquisition/delivery stalls raise within their
configured deadline and subsequent turns recover; a concrete restart rejects
the stale pending selector, preserves cursor novelty, and delivers one fresh
event once. The unchanged eight-event actual-loop network-denial harness also
repassed with zero descendants. Phase-end Fable review is pending, especially
for the explicitly recorded uncertain late-completion semantics of a timed-out
daemon fixture call. Real Telegram and production remain unauthorized.

On 2026-08-14 at 07:48 PDT, the generic production-free addressed-event seam
completed its synthetic full-loop and restart/isolation gates at local unpushed
commit `744a7c1`. A stale pending selector failed visibly without fallback
after restart, a fresh event delivered exactly once, the actual history inode
persisted/grow while remaining distinct from peer runtimes, and no descendant
remained. Model-diverse internal Fable review returned scoped GO with no high/medium
finding. The seam is frozen; concrete transports, Telegram, and production
remain unauthorized. Evidence:
`experiments/20260814T144300Z-addressed-restart-isolation/`.

On 2026-08-14 at 06:53 PDT, addressed mock adapter commit `c47e7eb` passed its
production-free deterministic floor: six total seam/adapter tests cover eight
reverse-completed private/group events, channel-owned novelty and destination
binding, finalized/unpresented/unknown rejection, and selector-text injection.
Compilation, diff check, secret scan, and zero-descendant checks passed. The
actual full-loop harness remains unrun and Telegram/production remain NO-GO.
Evidence: `experiments/20260814T133500Z-addressed-full-loop-mock/`.

On 2026-08-14 at 06:16 PDT, restart persistence passed on the corrected,
structurally isolated Protomega staging runtime. Two correlated turns survived
controlled shutdown and a fresh process; the actual upstream-opened history
kept both markers on the same growing inode, remained distinct from both other
staging histories, and teardown left zero attributable descendants. Evidence:
`experiments/20260814T131500Z-corrected-restart-persistence/`.

On 2026-08-14 at 06:03 PDT, ThreadKeeper commit `e6979b9` on
`agent/threadkeeper-hardening-next` made nested direct `run_tools` record keys
reject empty and leading/trailing-whitespace forms before registry construction
or workspace effects. All 55 boundary tests (156 subtests), compilation, diff
check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-14 at 05:50 PDT, the addressed-event seam was frozen at its latest
reviewed production-free checkpoint and returned off the immediate critical
path. Its exact upstream base remains `2cdef05`; focused tests and diff checks
pass, but routing authority, concrete adapters, per-origin auth, bounded
retention/restart, and full-loop acceptance remain open. Protomega preservation
is again first priority; re-embedding remains fail-closed before target
creation because the pinned offline E5 artifact is absent and no implicit
download is authorized. A clean-baseline phase-end Fable review is running.

On 2026-08-14 at 05:34 PDT, exact pinned channel/loop inspection and a
deterministic interleaving established that unchanged upstream is NO-GO for
addressed private/group concurrency: the core carries only text through
`receive()`/`send(message)`, and a mutable current-route shim sends A's delayed
reply to B. A minimal explicit event-ID seam is frozen and its required
phase-start Fable review is running. Evidence:
`experiments/20260814T123400Z-full-loop-addressed-concurrency/`.

On 2026-08-14 at 05:20 PDT, a disposable thin provider adapter passed through
the complete pinned upstream loop: injected error and two-second stall each
returned a correlated visible failure within 1.3 seconds, and each immediately
following turn recovered. Pinned source was unchanged and teardown left zero
descendants. Addressed multi-session concurrency remains seam-only because the
Test channel is unaddressed. Evidence:
`experiments/20260814T121646Z-full-loop-provider-faults/`.

On 2026-08-14 at 05:02 PDT, ProtoCosmo2's nine KEEP-classified skills were
bound into isolated staging as hash-pinned references to current canonical
workspace copies. No stale skill bytes or loader were copied. Evidence:
`experiments/20260814T120200Z-protocosmo2-skill-port-manifest/`.

On 2026-08-14 at 04:45 PDT, the Protomega one-way re-embedding gate was
preregistered without loading a model or creating an output collection. A
verified disposable copy exported its sole stable-ID record, exact document
and timestamp, 384-D source-vector hash, pinned 1,024-D target, and frozen
phrase probe; authoritative hashes stayed unchanged. Evidence:
`experiments/20260814T114500Z-protomega-reembedding-prereg/`.

On 2026-08-14 at 04:39 PDT, an offline disposable probe established that
pinned upstream's local embedder produces 1,024 dimensions while preserved
Protomega Chroma requires 384. Exact-document text query was rejected; source
hashes stayed stable. A one-way re-embedding design is recorded at
`experiments/20260814T113500Z-protomega-text-embedding-compatibility/`.

On 2026-08-14 at 04:18 PDT, pinned `petta_lib_chromadb` commit `2184848`
under ChromaDB `1.5.9` directly attached to a fresh disposable copy of the
Protomega store. Exact ID recall and stored-vector recall returned the sole
dimension-384 record at distance `0.0`; a second fresh process reproduced both.
Authoritative source hashes/root metadata remained unchanged and no attributable
descendants remained. No migration is presently justified. Evidence:
`experiments/20260814T111500Z-protomega-chroma-upstream-recall/`.

On 2026-08-14 at 04:12 PDT, ThreadKeeper commit `dbb320f` on
`agent/threadkeeper-hardening-next` made nested direct `run_tools` record keys
reject invisible Unicode format characters, including the otherwise
prose-allowed zero-width joiners, before registry construction or workspace
effects. All 55 boundary tests (153 subtests), compilation, diff check, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-14 at 04:08 PDT, the first Protomega asset-preservation gate passed.
An ordinary recoverable copy of the authoritative Chroma store matched every
source file byte-for-byte; source file hashes and root metadata were unchanged
before/after. Read-only SQLite inspection of only the copy found one `memories`
collection at dimension 384 with one embedding. Upstream plugin attachment and
exact known recall remain open. Evidence:
`experiments/20260814T110400Z-protomega-chroma-disposable-copy/`.

On 2026-08-14 at 03:28 PDT, the reopened history-isolation blocker was
structurally corrected using three disposable runtime copies at the same
pinned commits. The actual upstream-opened `memory/history.metta` targets and
runtime state directories now have three distinct device/inode pairs, all
histories start empty, and zero attributable descendants remain. Upstream
source was not edited and the prior disposable history is recoverably backed
up. Fresh per-runtime conversation/cross-history assertions passed with six
correlated turns and zero foreign markers. Bounded provider failure and
addressed concurrency remain open. Evidence:
`experiments/20260814T102825Z-corrected-three-runtime-isolation/` and
`experiments/20260814T103800Z-corrected-three-runtime-conversations/`.

On 2026-08-14 at 02:48 PDT, each of the three credential-free staging roots
completed two ordered turns through the unchanged pinned upstream loop (six
turns total), retained identity-specific routing, and terminated with zero
OmegaClaw/PeTTa/SWI descendants. Logs stayed within their respective roots;
production identities, legacy worktrees, and preserved Protomega Chroma were
untouched. Provider failure, restart persistence, and simultaneous concurrency
remain open. Evidence:
`experiments/20260814T094700Z-three-root-conversations/`.

On 2026-08-14 at 02:10 PDT, ThreadKeeper commit `90a60b2` on
`agent/threadkeeper-hardening-next` made nested direct `run_tools` record keys
reject control characters and non-NFC Unicode before registry construction or
workspace effects. All 55 boundary tests (152 subtests), compilation, diff
check, and draft PR #1 safety-floor ancestry passed.

On 2026-08-14 at 02:05 PDT, the complete pinned upstream OmegaClaw loop passed
three ordered mock conversations and idle acquisition using `provider=Test`
and `commchannel=test`, then terminated with zero attributable descendants.
The disposable runtime required explicit non-Docker integration settings
(Janus venv/module `PYTHONPATH`, upstream `silent`, empty Docker-specific
security policy, and YAML numeric defaults); no upstream source was edited.
A preceding cold launch failed the 300-second startup bound while still
translating, so cold-start performance remains an explicit limitation.
Bounded failure, restart, concurrency, and three-root isolation remain open.
Evidence: `experiments/20260814T083100Z-clean-full-loop-baseline/`.

On 2026-08-14 at 01:20 PDT, the exact pinned OmegaClaw Python requirements
installed into the clean PeTTa-local `.venv` and `pip check` passed. The
unchanged manifest produced a 5.4 GiB environment including CUDA 13 libraries.
The upstream test-channel and Test-provider RPC primitives then passed 10/10
under `env -i`, including ordered multi-message acquisition, restart, and
bounded timeout cases. Full OmegaClaw-loop ordinary conversation remains open;
production identities and original Chroma remain untouched. Evidence:
`experiments/20260814T081649Z-clean-omegaclaw-python-deps/` and
`experiments/20260814T082009Z-clean-omegaclaw-mock-primitives-r3/`.

On 2026-08-14 at 00:57 PDT, isolated SWI-Prolog 10.1.13 was built from
canonical commit `fc7ef84` in a user-only prefix with TERM/GUI disabled and
Janus verified. The exact pinned PeTTa README smoke passed in a scrubbed
environment with its expected NARS result and zero post-run descendants.
OmegaClaw mock conversation remains open; production and original Chroma are
untouched. Evidence: `experiments/20260814T075550Z-clean-swipl-10-1-13-fresh-minimal-build/`
and `experiments/20260814T075741Z-clean-petta-upstream-smoke/`.

On 2026-08-14 at 00:35 PDT, the petta-chem exclusion became terminal. A
read-only quarantine baseline captured the preserved dirty legacy commits and
Protomega Chroma metadata before any clean-install write. A wholly fresh
layout now exists at `upstream-clean/PeTTa`, pinned to PeTTa
`7037f4c` (`v1.0.4`), OmegaClaw `2cdef05`, and `petta_lib_chromadb`
`2184848`. Upstream documentation and CI were inspected; the unchanged smoke
is Docker-based, so the next authorized gate is the explicitly non-Docker,
isolated SWI-Prolog 10.x/manual mock path. Production and original Chroma
stores remain untouched.

On 2026-08-13 at 22:43 PDT, clean-install phase-start Fable review returned
conditional GO but found a critical cross-project exclusion: a live petta-chem
calibration is using the shared legacy PeTTa tree and SWI-Prolog 9.3.36. No git,
environment, dependency, or file operation may touch that tree until the run is
terminal. The clean recovery will use a fresh PeTTa `v1.0.4`/OmegaClaw
`2cdef059`/exact-Chroma-plugin layout elsewhere, isolated SWI-Prolog 10.x, and
a scrubbed non-Docker mock path; Docker would require separate sudo approval.
Legacy quarantine capture must precede clean-install mutation and is therefore
waiting on petta-chem. Production remains stopped. Evidence:
`experiments/20260814T053851Z-clean-install-pivot/`.

On 2026-08-13 at 22:32 PDT, Ben authorized a clean-install-first recovery
pivot. Generalized privileged-inspector/synthetic-launcher work is frozen as
quarantine evidence after v12.1 Fable review found two unresolved high defects.
The critical path is now one clean upstream codebase pinned at `2cdef05`, three
isolated production-free configurations, ordinary-conversation acceptance,
then selective asset recovery in order: Protomega Chroma via disposable copies,
ProtoCosmo2 decoupled skills, and clean Protomega2 last. Pivot evidence:
`experiments/20260814T053851Z-clean-install-pivot/`. Production remains stopped
and cutover is not authorized.

On 2026-08-13 at 22:33 PDT, the v12 synthetic spine review returned GO only for
continued synthetic work but found one high RFC-8949 map-order defect and four
medium cap/error/mount gaps. V12.1 fixes them and additional read-only, NUL,
size, hardlink, and ledger hygiene lows. Eight focused tests and source
compilation pass with no bytecode artifact; exact-model review is pending. No
receipt, census, live-host inspection, privilege, production path, snapshot,
Phase-0 closure, or Phase-1 action ran. Evidence:
`experiments/20260814T053005Z-upstream-recovery-phase0-synthetic-launcher-v12-1/`.

On 2026-08-13 at 22:15 PDT, exact-model Fable review closed the v11.2 launcher
design gate narrowly. It verified the full frozen hash chain, reproduced
47+23+23 plus all launcher lints, and found no critical/high issue. GO applies
only to synthetic fixture-root implementation. The remaining medium constraint
requires bounded descriptor re-descent because `RLIMIT_NOFILE=64` cannot hold a
naive depth-64 FD stack; this is now an implementation acceptance test. The
reviewer's ledger finding was resolved with a fresh captured 14-invariant run.
No executable launcher, live-host inspection, privilege, production path,
snapshot, Phase-0 closure, or Phase-1 action ran. Evidence:
`experiments/20260814T050710Z-upstream-recovery-phase0-integrated-launcher-v11-2/`.

On 2026-08-13, ThreadKeeper commit `0480552` on
`agent/threadkeeper-hardening-next` made the complete direct `run_tools`
run-record tree a pre-effect invariant. Arbitrary bookkeeping values must now
be bounded exact JSON with finite numbers, bounded depth/node counts, bounded
keys/strings, and no behavioral objects before registry construction or any
workspace effect. All 53 boundary tests (150 subtests), four relevant mock
tests, compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-13 at 22:05 PDT, exact-model Fable review of v11.1 reproduced all
frozen suites and returned NO-GO for implementation. Its high finding is a
direct contract contradiction: five allowed inherited directory FDs cannot
also supply the distinct receipt and quarantine directories. Medium findings
require explicit failed-closed receipt-only ordering, satisfiable and globally
ordered tree CBOR, frozen caps, and pinned receipt encodings/preimages. No
launcher, live-host inspection, privilege, production path, snapshot, or
Phase-1 action ran. Evidence:
`experiments/20260814T045617Z-upstream-recovery-phase0-integrated-launcher-v11-1/`.

V11.2 now fixes the descriptor count at seven, makes failed-closed publication
receipt-only, freezes satisfiable globally sorted tree CBOR and caps, and pins
receipt field types/preimages/clocks. Its 14-invariant lint passes; exact-model
Fable review is pending. Evidence:
`experiments/20260814T050710Z-upstream-recovery-phase0-integrated-launcher-v11-2/`.

On 2026-08-13 at 22:00 PDT, Fable's v11 launcher-design review gave narrow GO
for synthetic implementation but found one high gap: the execution receipt was
unspecified. V11.1 freezes the receipt/publication commit, per-run hashes,
canonical CBOR tree, `O_NOATIME` fallback, honest immutable-secret limitations,
16-byte synthetic-secret floor, 46-root count, wrapper inputs, and real ledger
capture. Its 27-invariant lint passes and exact-model Fable review is pending.
No executable launcher, live-host inspection, privilege, production path,
snapshot, or Phase-1 action ran. Evidence:
`experiments/20260814T045617Z-upstream-recovery-phase0-integrated-launcher-v11-1/`.

On 2026-08-13 at 21:52 PDT, the Phase-0 integrated-launcher v11 plain-language
candidate passed a 19-invariant document lint. It freezes the descriptor-only
authority boundary, two-census stability rule, exact failure keys, secret-free
secure publication, and synthetic acceptance matrix while retaining four
implementation blockers. Exact-model Fable review is pending. No executable
launcher, live-host inspection, privilege, snapshot, or Phase-1 action ran.
Evidence: `experiments/20260814T045049Z-upstream-recovery-phase0-integrated-launcher-v11/`.

On 2026-08-13 at 21:48 PDT, the production-free descriptor-relative v10.1
scanner gate closed narrowly. Fable matched the exact hashes, independently
reproduced 47+23+23 checks, found no critical/high issue, and returned GO only
for this synthetic scanner slice. Its medium evidence-ledger gap was resolved
by recapturing real acceptance stdout/stderr/status at 04:48:25Z. Phase 0
remains open pending a separately specified and reviewed integrated launcher;
no live-host, privileged, production-path, snapshot, or Phase-1 authority was
granted. Evidence:
`experiments/20260814T043936Z-upstream-recovery-phase0-descriptor-scanner-v10-1/`.

Earlier, on 2026-08-13 at 21:34 PDT, the first production-free descriptor-relative
scanner implementation bound byte-exactly and exclusively to v9.1 and passed
47 inherited v9, 23 v9.1, and 21 scanner checks. It uses only a caller-opened
fixture root, no-follow relative opens, metadata-only credential identity, and
a fixed absent sentinel. Exact-model Fable end review is pending. This grants
no live-host, privileged, production-path, snapshot, Phase-0, or Phase-1
authority. Evidence:
`experiments/20260814T043020Z-upstream-recovery-phase0-descriptor-scanner-v10/`.

On 2026-08-13 at 21:28 PDT, binding Fable end review gave v9.1 a narrow GO for
descriptor-relative read-only scanner implementation only. All seven hashes,
47+23 tests, and 29 reviewer probes pass; no critical/high finding remains.
The scanner must bind exclusively to v9.1, use metadata-only credential
identity, and capture real ledger outputs. No live-host, privileged,
production-path, snapshot, Phase-0, or Phase-1 authority was granted. Evidence:
`experiments/20260814T042038Z-upstream-recovery-phase0-integrated-inspector-v9-1/`.

On 2026-08-13 at 21:16 PDT, effective-model-proven Fable gave v9 a conditional
GO for scanner implementation only: 47/47 tests reproduce and all v8 high
findings are resolved. V9.1 must first resolve credential-label normalization,
mandatory limitations, credential-root hash policy, launcher stability, tilde
grammar/uniqueness, and stale ledger binding. No privilege, production access,
snapshot, Phase-0 closure, or Phase-1 authority was granted. Evidence:
`experiments/20260814T041012Z-upstream-recovery-phase0-integrated-inspector-v9/`.

On 2026-08-13 at 21:00 PDT, effective-runtime-proven
`anthropic/claude-fable-5` review rejected the v8 contract slice despite its
reproducible 34/34 synthetic pass. Nested public records are unconstrained;
systemd control/generator roots and six production path-reference markers are
missing; and secret matching misses embedded argv/environment forms. POSIX
assignment grammar, exhaustive failure mapping, and MTProto/unknown credential
scope also need correction. Reviewed v8 bytes remain unchanged. No privileged
scanner, production credential read, snapshot, or Phase-1 action ran. Evidence:
`experiments/20260814T034937Z-upstream-recovery-phase0-integrated-inspector-v8/`.

On 2026-08-13 at 20:46 PDT, Phase 0 remains open and production remains
stopped. Effective-model-proven `anthropic/claude-fable-5` review independently
confirmed that v6 is NO-GO for presentation or execution. Its two critical
and remaining high-severity defects are retained as successor requirements.
The separate v7 unprivileged secure-capture primitives now pass 30 checks and
an independent clean Fable rerun of the same suite plus adversarial probes.
Fable returned GO to close only that narrow primitives gate, with no remaining
critical/high finding at its boundary. The real start-review identity is
`agent:protomegabot-fable:omegaclaw-phase0-fable-direct-20260814t0330z` /
`5f86e357-0245-4da9-95e8-6ca48da7da99`; the end-review identity is
`agent:protomegabot-fable:omegaclaw-phase0-v7-fable-end-20260814t0340z` /
`76881245-ba13-4e05-a354-33c1cbef5bc8`. Next is an integrated v8 read-only
privileged-inspector design resolving every v6 high finding. Its first
production-free executable contract slice freezes the 28-root scope,
credential grammar, scheduler/launcher/marker union, public schema, and
failure predicate; 34 synthetic checks pass and clean Fable review is pending.
The non-secret credential-key mapping is inferred from launcher source and is
not yet validated against credential files. No privileged
command, snapshot, chmod, token, database client, Telegram action, or Phase-1
worktree action ran. Evidence:
`experiments/20260814T034937Z-upstream-recovery-phase0-integrated-inspector-v8/`.

On 2026-08-13 at 19:38 PDT, recovery Phase 0 remains blocked but production-
specific stop evidence is freshly rechecked. A three-sample candidate scan
found no private-canary/controller marker and no fd/map handle into the indexed
directory roots. It failed closed on one explicitly attributable
petta-chem SWI lineage and three ptrace-protected same-UID ssh-agent processes
whose fd trees are unreadable from the cron sandbox. Post-run inspection also
found omitted regular-file roots and cwd/root identities, so this is not exact
28-path handle proof. A bounded administrator
request now proposes read-only scheduler/process inspection plus a temporary
ten-minute mode denial on exactly three production credential env files; it is
unapproved and Fable rejected it because same-UID mode bits are reversible,
already-loaded credentials/state-only writers remain possible, scheduler and
privilege scope is incomplete, and no exact review-bound executable exists.
The next safe gate is a separate fixed read-only privileged inspector design;
preservation-window authority must remain distinct. No chmod, privileged
command, or snapshot ran. Evidence:
`experiments/20260814T023547Z-upstream-recovery-phase0-admin-exception-v5/`
and
`experiments/20260814T023748Z-upstream-recovery-phase0-live-stop-recheck-v5/`.

Earlier at 19:09 PDT, recovery Phase 0 found a material production-stop
violation. A stale already-running execution of the superseded Chroma-repair
cron started Protomega, Protomega2, and ProtoCosmo2 through the quarantined
private-canary stack after recovery ownership had changed. All exact owners
and receivers were stopped, and a repeated process scan is empty. Chroma
mtimes predate the unintended starts, but production transport-state files
were modified during the live interval; their current bytes are now the
preservation source and must not be rolled back or reconstructed. Independent
snapshot-v3 review also returned NO-GO, and no snapshot command ran. Phase 0
restart-fence and quiescence evidence is reset. Evidence:
`experiments/20260814T015539Z-upstream-recovery-phase0-snapshot-v3/`.

On 2026-08-13, ThreadKeeper commit `50bda23` on
`agent/threadkeeper-hardening-next` made the 64-field direct run-record cap a
pre-effect batch invariant. Tool batches now reserve any missing file, test,
patch-proposal, and remaining-quota bookkeeping fields before execution, so a
cap-sized record cannot be mutated past its validation ceiling after a
workspace effect. The focused regression, all 52 boundary tests, 30 relevant
direct-tool mock tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `3981eb7` on
`agent/threadkeeper-hardening-next` closed the remaining direct run-record
field-name validation gap. Programmatic `run_tools` records now require safe
bounded ASCII identifiers before registry construction or effects, preventing
attacker-sized, control-bearing, noncanonical, or misleading keys from
reaching durable state. The focused regression, all 51 boundary tests and 146
subtests, 30 relevant direct-tool mock tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `3bd1bb5` on
`agent/threadkeeper-hardening-next` closed the direct tool-quota ceiling gap.
Programmatic `run_tools` callers must now keep explicit quotas within the
configured global dispatch cap before registry construction or effects, so an
oversized integer cannot be persisted into a run record after a workspace
change. The focused regression, all 50 boundary tests and 142 subtests, 30
relevant direct-tool mock tests, compilation, `git diff --check`, and draft PR
#1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `10099b2` on
`agent/threadkeeper-hardening-next` made existing direct `run_tools` audit
content obey the same bounded structured-return contracts used for durable
results. File entries now require canonical confined workspace paths, test
entries require bounded single-line NFC text, and patch proposals require an
authorized action, canonical path, and bounded UTF-8 content before registry
lookup or effects. The seven-case regression, all 49 boundary tests and 142
subtests, five relevant direct-runner tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `42a7a0e` on
`agent/threadkeeper-hardening-next` made bounded run-record audit history a
pre-effect batch invariant. Direct `run_tools` batches now fail closed when
their projected file, test, or patch-proposal entries would cross the 256-entry
cap, rather than applying a workspace effect and leaving an over-limit record.
The focused regression, all 48 boundary tests and 135 subtests, 30 direct-tool
mock tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed. A broader keyword selection also exposed eight pre-existing
candidate-review fixtures whose expected proposal errors are now preceded by
the required missing run identity; the isolated relevant selection is clean.

On 2026-08-13, ThreadKeeper commit `8e06933` on
`agent/threadkeeper-hardening-next` bounded direct `run_tools` run-record
validation before walking caller-supplied audit state. Exact records now fail
closed when they exceed 64 fields or when existing file, test, or patch audit
lists exceed 256 entries, preventing unbounded pre-effect validation. The
focused regression, all 47 boundary tests and 132 subtests, three relevant
mock tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-13, ThreadKeeper commit `22ad300` on
`agent/threadkeeper-hardening-next` bounded every direct `run_tools` argument
list before walking its values. Because the supported registry has maximum
arity two, oversized exact lists now fail before value validation, registry
construction, or effects. The focused regression, all 46 boundary tests and
128 subtests, 30 relevant mock tests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `5707dbd` on
`agent/threadkeeper-hardening-next` made the direct `run_tools` authorization
subset a closed, bounded authority boundary. Oversized, duplicate, unknown,
malformed, control-bearing, and noncanonical allowed-name subsets now fail
before registry construction or effects. All 45 boundary tests and 128
subtests, 47 relevant direct-tool mock tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `62f9b47` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers validate
the complete mutable audit-entry shape before registry lookup or effects.
Behavioral strings, proposal mappings, proposal field names, and proposal
values can no longer defer Python execution or structured-return failure until
after a workspace change. The focused sentinels, all 44 boundary tests and 122
subtests, 24 direct-tool mock tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `82c14ef` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers reject
behavioral run-record mappings, field names, and mutable audit-list targets
before registry lookup or effects. This prevents post-effect execution through
`setdefault`/`append` and fail-closes malformed bookkeeping before a partial
tool batch. The focused sentinel, all 43 boundary tests and 117 subtests, 324
relevant direct-tool/argument mock tests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-13, ThreadKeeper commit `fa6f90c` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers reject
non-exact argument containers and values before `isinstance`, registry lookup,
or effects. Behavioral `__class__` sentinels, all 42 boundary tests and 115
subtests, 24 direct-tool mock tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed. The complete mock module remains an
invalid aggregate gate in one process: its provider-call rate limiter saturated
and 130 later tests failed, while 1,096 passed; the isolated relevant selection
is clean.

On 2026-08-12, ThreadKeeper commit `957b066` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers validate
the complete nested task-contract shape before authorization helpers, registry
lookup, or effects. The focused regression, all 41 boundary tests and 113
subtests, 479 relevant mock tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `200a477` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers reject
behavioral task-contract mappings before authorization helpers, registry
lookup, or effects. The focused regression, all 40 boundary tests and 113
subtests, 24 direct-tool tests, compilation, `git diff --check`, and draft PR
#1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `4477483` on
`agent/threadkeeper-hardening-next` made direct `run_tools` callers reject
every non-exact tool name before equality, hashing, registry lookup, or
allowlist membership. A behavioral sentinel regression, all 39 boundary tests
and 113 subtests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-12, ThreadKeeper commit `fc2acbe` on
`agent/threadkeeper-hardening-next` made the shared workspace-path validator
reject non-exact strings before conversion. Direct callers can no longer
trigger behavioral `__str__` code or coerce non-string scalars into authority-
bearing paths. The focused contract/path selection passed 157 tests, all 38
boundary tests and 113 subtests passed, and compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `5f93efa` on
`agent/threadkeeper-hardening-next` made direct task-contract dictionaries
reject non-exact string field names before any lookup, hashing, comparison, or
sorting. A behavioral sentinel-key regression, all 155 contract tests, all 38
boundary tests and 113 subtests, compilation, `git diff --check`, and draft PR
#1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `31e37e0` on
`agent/threadkeeper-hardening-next` made malformed task-contract quota scalars
fail closed without stringifying attacker-controlled subclasses. The focused
regression, all 37 boundary tests and 113 subtests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `dab4da8` on
`agent/threadkeeper-hardening-next` made the internal inline contract
normalizer reject behavioral mapping and string subclasses without first
truth-testing, stringifying, parsing, or trimming them. The focused regression,
all 36 boundary tests and 113 subtests, all 155 contract tests, compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `bfe2a32` on
`agent/threadkeeper-hardening-next` made the internal inline task-contract
normalizer reject both top-level and nested `dict` subclasses. This preserves
the exact JSON-object authority boundary even for programmatic callers; public
dispatch already rejects non-string goals separately. The focused regression,
all 155 public contract tests, all 35 boundary tests and 113 subtests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-12, the Iter three-bot secret-free baseline contract was revised to
schema v2 before any production record was accepted. Deployment slot and
declared runtime identity are now separate required fields, allowing the
Protomega/ProtomegaTron distinction to be recorded rather than conflated, and
capture time must be canonical UTC. Nine provider-free tests and compilation
passed. The factual slot mapping and receiver ownership remain unresolved; no
live behavior changed.

On 2026-08-12, ThreadKeeper commit `3755c6c` on
`agent/threadkeeper-hardening-next` closed a persona task-contract coercion
gap. Pair iterables and mapping subclasses can no longer be converted into
apparently valid authority contracts, and tuple-valued string-list fields now
fail closed before any worker LLM call. The focused regression, all 155
contract tests, all 34 boundary tests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-12, ThreadKeeper commit `cc3a8b6` on
`agent/threadkeeper-hardening-next` closed an inline task-contract validation
gap. Top-level JSON contracts now retain undeclared fields long enough for the
strict validator to reject them, so authority-looking additions such as
`approved: true` fail closed as `contract_invalid` before any worker LLM call.
The focused regression, all 155 contract tests, all 33 boundary tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed;
the 11 stale candidate-review fixtures identified by the preceding run were
updated with required transcript identity evidence.

On 2026-08-12, ThreadKeeper commit `a5edee3` on
`agent/threadkeeper-hardening-next` made prompt- and transcript-visible task
contract text canonical. Decomposed Unicode in objectives or string-list
constraints now fails closed as `contract_invalid` before any worker LLM call.
Three focused regressions, all 33 boundary tests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed. A broader
`-k task_contract` selection also passed 143 tests but exposed 11 pre-existing
candidate-review fixtures that omit the now-required transcript identity.

On 2026-08-11, ThreadKeeper commit `14c16ef` on
`agent/threadkeeper-hardening-next` made durable queued adjudication claims
fail closed on ambiguous shapes. Transcript-backed review gates must now carry
the dispatcher's exact four fields, including a true requirement, pending
status, bounded canonical candidate summary, and exact integer candidate turn;
missing dispatch identity, boolean turns, and ignored authority fields such as
`approved` are rejected. One focused regression, all 33 boundary tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `5083b85` on
`agent/threadkeeper-hardening-next` made durable queued worker-token accounting
fail closed on malformed scalar types. A digest-valid transcript can no longer
authenticate boolean token counts as parent-visible integer zeros through
Python's boolean/integer equality. One focused regression, all 33 boundary
tests and 104 subtests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `d4505bc` on
`agent/threadkeeper-hardening-next` made durable queued summary claims fail
closed on malformed scalar types. A digest-valid transcript can no longer
reach incidental normalization errors by encoding `summary` as a mapping;
terminal audit publication now requires the authenticated claim to be an exact
string. One focused regression, all 33 boundary tests, two relevant mock tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, Capacity 1.2 gained a fail-closed D2 decision-receipt contract
at
`artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/`.
It binds any future one-shot 64/32 materialization approval to the reviewed
generator and preregistration digests while leaving fitting and all live
authority false. Nine tests, compilation, and the fixture checker passed; no
receipt or dataset was created.

On 2026-08-11, ThreadKeeper commit `9940ebd` on
`agent/threadkeeper-hardening-next` made durable queued audit-claim types fail
closed. A digest-valid transcript can no longer project mapping keys as
`files_changed`/`tests_run` lists or coerce a string adjudication flag into an
apparently valid parent review gate. Three focused regressions, all 33 boundary
tests, compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-11, ThreadKeeper commit `deabfac` on
`agent/threadkeeper-hardening-next` completed durable error-guidance binding.
Every accepted terminal error status now has a deterministic recovery action;
an authenticated `llm_failed` transcript can no longer carry substituted
operator instructions. One focused regression, all 33 boundary tests, seven
relevant mock tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `0567e13` on
`agent/threadkeeper-hardening-next` bound escalation-denial guidance to the
durable transcript outcome. An authenticated `escalation_denied` result can no
longer instruct the parent to override the budget gate and escalate anyway.
One focused regression, all 33 boundary tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `0d51f8b` on
`agent/threadkeeper-hardening-next` bound deterministic queued error recovery
actions to the durable transcript outcome. Authenticated timeout, token/response
limits, protocol failures, and quota failures can no longer carry substituted
operator instructions. One focused regression, all 33 boundary tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `fcad2ab` on
`agent/threadkeeper-hardening-next` bound queued failure uncertainty and
incomplete operator guidance to the durable transcript outcome. Callers can no
longer downgrade authenticated failures or direct a parent to accept
`max_turns` work as finished. One focused regression, all 33 boundary tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `0abbd44` on
`agent/threadkeeper-hardening-next` repaired durable outcome binding for real
queued failures and incomplete runs. Validation now recognizes the dispatcher's
explicit terminal failure statuses and `max_turns`, while continuing to reject
cross-outcome transcript substitutions. One focused regression, all 33
boundary tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-11, ThreadKeeper commit `5fb7bf0` on
`agent/threadkeeper-hardening-next` bound pending-adjudication guidance to the
durable transcript outcome. An authenticated candidate can no longer lower its
uncertainty or instruct the parent to accept it without adjudication. One
focused regression, all 33 boundary tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `181f6b3` on
`agent/threadkeeper-hardening-next` bound queued cancellation guidance to the
durable transcript outcome. An authenticated cancellation can no longer be
relabeled with high uncertainty or instructions to restart cancelled work.
One focused regression, all 33 boundary tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-11, ThreadKeeper commit `c873fa6` on
`agent/threadkeeper-hardening-next` bound successful queued operator guidance
to the durable transcript outcome. A transcript-backed success can no longer
be relabeled as uncertain or direct the parent to repeat arbitrary work before
audit publication. One focused regression, all 33 boundary tests, compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `bbe231c` on
`agent/threadkeeper-hardening-next` rejected unauthenticated queued truncation
claims. A durable transcript-backed terminal result can no longer have a
`truncated` marker grafted onto it before audit publication. One focused
regression, all 33 boundary tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `e11d8c0` on
`agent/threadkeeper-hardening-next` bound queued human-facing summaries to
their durable transcript. A digest-valid transcript can no longer authorize a
substituted summary before terminal audit publication. One focused regression,
all 33 boundary tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `86c87ea` on
`agent/threadkeeper-hardening-next` bound queued audit claims to their durable
transcript. A same-run, digest-valid transcript can no longer be cited while
substituting changed files, tests, patch proposals, adjudication metadata, or
worker token usage before terminal audit publication. One focused regression,
all 33 boundary tests and 91 subtests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `01802a9` on
`agent/threadkeeper-hardening-next` bound durable queued transcript evidence to
the exact validated task contract. A digest-valid transcript for the same run
can no longer substitute a different authority contract before terminal audit
publication. One focused regression, all 33 boundary tests, compilation, `git
diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `31b1f94` on
`agent/threadkeeper-hardening-next` required every claimed queued structured
return to carry verified durable transcript evidence. A terminal result can no
longer omit both transcript path and digest before audit publication. One
focused regression, all 33 boundary tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `259272e` on
`agent/threadkeeper-hardening-next` bound queued `error` and `incomplete`
returns to matching durable transcript statuses. Contradictory terminal
transcripts now fail closed before audit publication. One focused regression,
all 33 boundary tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `db9296f` on
`agent/threadkeeper-hardening-next` bound authority-bearing queued return
statuses to their durable transcript status. Nonterminal transcripts, and
transcripts contradicting success, cancellation, or adjudication claims, now
fail closed before terminal audit publication. One focused regression, all 33
boundary tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-10, ThreadKeeper commit `1b05092` on
`agent/threadkeeper-hardening-next` repaired the queued run-identity handoff
required by the preceding transcript/task binding check. Claimed worker
dispatches now retain the enqueue-time run ID in their durable transcript while
unrelated contexts remain unaffected. One end-to-end regression, all 33
boundary tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-10, ThreadKeeper commit `91a88cf` on
`agent/threadkeeper-hardening-next` bound durable queued transcript evidence to
the claimed task identity. A digest-valid, internally self-consistent
transcript from another run now fails closed before terminal audit publication.
One focused regression, all 32 boundary tests, compilation, `git diff --check`,
and draft PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `0d508d7` on
`agent/threadkeeper-hardening-next` bound durable transcript evidence to its
internal run identity. A digest-valid arbitrary JSON file, mismatched internal
path, or filename whose prefix disagrees with its `run_id` now fails closed
before queued terminal audit publication or candidate review. One focused
regression, all 32 boundary tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `763bcea` on
`agent/threadkeeper-hardening-next` made durable queued transcript references
canonical and exact. Terminal audit publication now rejects whitespace-bearing,
overlong, relative/aliased, symlink-resolving, or non-`.json` transcript path
claims even when they resolve to content with the claimed digest. One focused
regression, all 32 boundary tests, compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry passed.

On 2026-08-10, ThreadKeeper commit `b24839f` on
`agent/threadkeeper-hardening-next` content-bound durable queued transcript
evidence. Referenced transcripts must now be readable regular non-symlink files
within the configured run directory, stay within the audit byte cap, and match
the claimed SHA-256 before terminal audit publication. One focused regression,
all 32 boundary tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `9278e98` on
`agent/threadkeeper-hardening-next` made durable queued transcript paths
canonical. Control-bearing/multiline and non-NFC path text now fails closed
before terminal audit publication. One focused regression, all 32 boundary
tests, compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-09, ThreadKeeper commit `e34afa5` on
`agent/threadkeeper-hardening-next` made durable adjudication candidate
summaries control-safe and canonical. Pending candidate summaries must now be
nonempty, at most 300 characters, single-line/control-free, and NFC-normalized
before terminal audit publication. One focused regression, all 32 boundary
tests, compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed.

On 2026-08-09, ThreadKeeper commit `8c90f99` on
`agent/threadkeeper-hardening-next` made durable worker summaries bounded and
canonical. Queued structured returns now reject summaries above 1,000
characters, control-bearing/multiline text, and non-NFC Unicode before terminal
audit publication. One focused regression, all 32 boundary tests, compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `3fc64c2` on
`agent/threadkeeper-hardening-next` made durable operator guidance exact and
bounded. Queued structured returns now restrict `uncertainty` to
`low`/`medium`/`high`, while `next_action` must be a nonempty, single-line,
NFC-normalized string of at most 300 characters. One focused regression, all
31 boundary tests, compilation, `git diff --check`, and draft PR #1
safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `14a714b` on
`agent/threadkeeper-hardening-next` made durable worker transcript evidence
exact and confined. Queued structured returns must provide transcript path and
SHA-256 together; the path must resolve beneath the configured run directory
and the digest must be canonical lowercase hex. One focused regression, all 30
boundary tests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-09, ThreadKeeper commit `61706d8` on
`agent/threadkeeper-hardening-next` made durable worker audit-claim lists
bounded and safe. `files_changed` must now contain at most 20 safe relative
workspace paths, while `tests_run` permits at most 10 bounded single-line
entries. One focused regression, all 29 boundary tests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `dab1609` on
`agent/threadkeeper-hardening-next` removed queue-only path and checksum fields
from the accepted synchronous queued-worker return schema. Claimed workers can
no longer inject those authority-bearing fields into terminal audit payloads.
One regression, all 28 boundary tests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-09, Capacity 1.1's frozen candidate passed independent freeze and
public-replay verification. The verifier content-binds the candidate, digest,
22-case public harness, complete v0.6 sandbox chain, and sealed commitment;
all public cases, two tests including source-drift failure, and compilation
passed. A09--A12 remain sealed and require Ben's explicit authorization before
reveal or execution; harness adoption and runtime effects remain closed.

On 2026-08-09, ThreadKeeper commit `e0d7568` on
`agent/threadkeeper-hardening-next` strictly validated durable patch-proposal
summaries. Queued results now reject more than 20 proposals, unknown actions,
absolute/traversing paths, and control-bearing paths before terminal audit
publication. All 27 boundary tests and 54 subtests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `c9bcef4` on
`agent/threadkeeper-hardening-next` kept size-fallback structured returns inside
the durable queue schema. Minimal adjudication results now downgrade to
`incomplete` when their required metadata cannot fit, and the last-resort
fallback no longer emits the unrecognized `bounded` status. Two focused tests,
all 26 boundary tests and 49 subtests, compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `71d9188` on
`agent/threadkeeper-hardening-next` made durable adjudication returns exact and
status-consistent. Missing, malformed, oversized, undeclared, or non-pending
adjudication metadata now fails closed before terminal audit publication. Three
focused tests, all 25 boundary tests and 49 subtests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `f6144b1` on
`agent/threadkeeper-hardening-next` made durable structured worker-return
shapes exact. Malformed scalar/list/proposal fields, invalid truncation flags,
and inconsistent token-usage accounting now fail closed before terminal audit
publication. Four focused tests, all 24 boundary tests and 45 subtests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-09, ThreadKeeper commit `b48f968` on
`agent/threadkeeper-hardening-next` restricted durable parsed worker returns to
the synchronous dispatch schema. Invented authority-bearing fields now fail
closed rather than entering terminal audit records. Two focused tests, all 23
boundary tests and 40 subtests, compilation, `git diff --check`, and draft PR
#1 safety-floor ancestry passed.

On 2026-08-08, ThreadKeeper commit `24a35a6` on
`agent/threadkeeper-hardening-next` enforced each durable queued task's declared
structured-return size contract at the worker boundary. A dispatch result above
`max_chars`, or a non-string result, now fails closed into durable failure
retention instead of becoming an oversized terminal success record. One focused
regression, all 1,243 provider-free hardening tests and 40 subtests, compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-08, ThreadKeeper commit `51f2cf5` on
`agent/threadkeeper-hardening-next` retained each claimed queued task's enqueue
checksum until a terminal `.done` or `.failed` commit publishes replacement
integrity evidence. Abrupt interruption between claim and terminal publication
can no longer orphan the claimed task from its authenticating sidecar. One
focused regression, all 1,242 provider-free hardening tests and 40 subtests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-08, ThreadKeeper commit `58eba7e` on
`agent/threadkeeper-hardening-next` restricted durable queued-worker structured
result statuses to the five states emitted by synchronous dispatch. Missing or
invented statuses such as `approved` now fail closed rather than becoming
authority-bearing audit metadata. Two focused tests, all 21 hardening tests
and 40 subtests, compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry passed.

On 2026-08-08, ThreadKeeper commit `f50e738` on
`agent/threadkeeper-hardening-next` validated durable queued-worker result
statuses before persistence. Parsed structured results with non-string,
control-bearing, or overlong statuses now fail closed through durable failure
retention. One focused regression plus all 20 hardening tests and 32 subtests
passed, with compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry.

On 2026-08-08, Protomega's guarded transport cutover completed and passed a
fresh human-authored end-to-end Telegram canary. Message 9714 / update
940522237 reached the sole outer receiver, OpenClaw run
`337869bb-c063-48a2-8dc6-61fd59f123fc` completed on verified Anthropic
`claude-opus-4-6`, durable outbox delivery received Telegram receipt 9715,
and Ben's screenshot confirmed the exact nonce reply. Final topology is
`legacy=0 outer=1` at owner PID 2312624 with one child; watchdog healthy,
maintenance inactive, and cutover lock free. Evidence:
`experiments/20260808T203000Z-protomega-responder-failure-repro/`.

On 2026-08-08, ThreadKeeper commit `412f556` on
`agent/threadkeeper-hardening-next` bounded and path-sanitized durable queued
worker failure summaries, including secondary retention failures. A local
exception can no longer inflate a result record without bound or expose an
absolute host path. Two focused tests and all 1,220 provider-free hardening
tests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-08, ThreadKeeper commit `8d593df` on
`agent/threadkeeper-hardening-next` bound each durable queued task's declared
`run_id` to the queue path derived from that identity. Checksum-valid relabeled
tasks now fail closed before any worker LLM call. One focused regression and
all 1,238 provider-free hardening tests plus 28 subtests passed, with
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-08, ThreadKeeper commit `fbdd0f3` on
`agent/threadkeeper-hardening-next` made durable queued tool subsets obey the
same strict contract as direct dispatch. Checksum-valid tasks containing
duplicate, unknown, excluded, or aggregate-oversized tool subsets now fail
closed during record validation instead of only after worker claim. Five
focused tests plus 19 subtests and all 1,264 provider-free hardening tests plus
28 subtests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-08, ThreadKeeper commit `cad5953` on
`agent/threadkeeper-hardening-next` made durable queued tasks complete and
internally consistent. Checksum-valid records must now contain every
runtime-authored field, and the task-contract objective must exactly match the
queued goal instead of inheriting defaults or presenting conflicting task
meaning. Eighteen focused tests plus 25 subtests and all 1,218 provider-free
hardening tests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-08, ThreadKeeper commit `c6d334f` on
`agent/threadkeeper-hardening-next` made durable queued-worker limits exact.
Checksum-valid tasks with zero, negative, or above-cap `max_turns`/`max_chars`
now fail closed instead of being silently clamped at claim time. Sixteen
focused tests plus 15 subtests, all 1,218 provider-free hardening tests,
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-08, ThreadKeeper commit `01e44b8` on
`agent/threadkeeper-hardening-next` bounded durable queued-task persona and
tool identifiers to 64 characters and aligned persona lookup with the same
fail-closed grammar. Three focused regressions, all 1,218 provider-free
hardening tests, 15 boundary tests plus 11 subtests, compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry passed.

On 2026-08-08, ThreadKeeper commit `05de483` on
`agent/threadkeeper-hardening-next` made candidate run statuses safe bounded
identifiers before they reach operator-facing review output. Integrity-valid
transcripts with controls or status strings above 64 characters now fail
closed. Twenty focused and all 1,231 provider-free hardening tests plus 9
subtests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-08, ThreadKeeper commit `79613f7` on
`agent/threadkeeper-hardening-next` made patch-proposal capture exact. In
`patch_proposal_only` mode, content above the configured proposal cap now fails
the complete batch closed before any proposal is recorded instead of silently
persisting a truncated, semantically different patch. Seventeen focused and
all 1,216 provider-free hardening tests passed, with compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `d3f3cbc` on
`agent/threadkeeper-hardening-next` made parsed tool names safe bounded
identifiers before registry access or diagnostic interpolation. Control/invisible
Unicode and names over 64 characters now fail the complete batch closed. Two
focused tests and all 1,229 provider-free hardening tests plus 9 subtests
passed, with compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry.

On 2026-08-07, ThreadKeeper commit `b97515e` on
`agent/threadkeeper-hardening-next` made the structured worker-return bound
total. If fixed audit metadata alone exceeds a caller's digest cap, the return
now falls back to minimal valid JSON within that cap instead of leaking an
oversized result. One focused test and all 12 boundary-hardening tests plus 6
subtests passed, with compilation and `git diff --check`.

On 2026-08-07, ThreadKeeper commit `ebf8eb1` on
`agent/threadkeeper-hardening-next` bounded the complete parsed worker tool
batch before preflight. Non-effectful `emit` calls can no longer bypass the
per-turn cardinality bound and force unbounded validation work. One focused
and all 1,227 provider-free hardening tests plus 6 subtests passed, with
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `ba70005` on
`agent/threadkeeper-hardening-next` made candidate patch proposal records
complete as well as exact. Review now rejects checksum-valid proposals that
omit the runtime-authored `content` field. Eight focused and all 1,216
provider-free hardening tests passed, with compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `5b3c62d` on
`agent/threadkeeper-hardening-next` bound operator-facing candidate content to
the same limits enforced during runtime persistence. Review now rejects
checksum-valid patch proposal content above the configured proposal cap and
empty or oversized adjudication summaries. Fifty-seven focused and all 1,215
provider-free hardening tests passed, with compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-07, Capacity 1.1's child-result contract v0.2 failed independent
bound-consistency review. A 49,152-byte output creates a 65,570-byte canonical
report, exceeding the 65,536-byte report cap; 49,125 bytes is the largest
representable output. One direct check and three tests pass. Verdict:
`revision_required_before_implementation`; sandbox and runtime remain closed.

On 2026-08-07, ThreadKeeper commit `a2c4a0c` on
`agent/threadkeeper-hardening-next` made unresolved adjudication records
complete as well as exact. Candidate review now rejects checksum-valid pending
metadata missing the runtime-authored `required`, `status`, `candidate_summary`,
or `candidate_turn` field. Fifty-four focused and all 1,212 provider-free
hardening tests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `43c0610` on
`agent/threadkeeper-hardening-next` bound operator-facing patch proposals to
the full path/action scope of their authorizing task contract. Candidate
review now rejects checksum-valid proposals outside `allowed_paths` or covered
by `forbidden_actions`, matching runtime enforcement. Fifty focused and all
1,208 provider-free hardening tests passed, with compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-07, ProtoCosmo2 file egress was proven live in the Protobots
Staging group. Its production adapter posted an 88,055-byte PDF (Telegram
receipt `633`) and a 22,724-byte LaTeX source file (receipt `634`). The first
attempt correctly exposed that an OpenClaw-observed message ID was unavailable
as a ProtoCosmo2 Bot-API reply target; the adapter now permits operator-driven
unthreaded document posts while preserving reply threading when a valid ID is
available. Thirty-five focused provider-free tests and compilation pass, and
the supervisor is active with one runner. Evidence:
`experiments/20260807T153918Z-protocosmo2-staging-file-egress-r2/`.

On 2026-08-07, ThreadKeeper commit `370282d` on
`agent/threadkeeper-hardening-next` made candidate review validate the entire
task contract behind any operator-facing patch/adjudication gate. A
checksum-valid transcript can no longer authorize review with an empty
objective, escaping path scope, oversized tool quota, or another malformed
contract merely because its mode flag is true. Forty-eight focused and all
1,206 provider-free hardening tests passed, with compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `35b21d9` on
`agent/threadkeeper-hardening-next` bound operator-visible patch proposals to
the task contract that authorizes proposal-only execution. Candidate review
now rejects checksum-valid proposal records unless `patch_proposal_only` is
exactly true, while a failed run carrying only that flag creates no false
review gate. Forty-five focused and all 1,213 provider-free hardening tests
plus 6 subtests passed, with compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-07, Capacity 1.1's bounded child-result contract failed an
independent implementability review. Its safe two-tag intent is preserved, but
exact JSON bytes, canonical base64 plus decoded size, and non-bytes return
handling are under-specified. One direct check and five tests pass. Verdict:
`revision_required_before_implementation`; sandbox and runtime changes remain
closed.

On 2026-08-07, ThreadKeeper commit `be12522` on
`agent/threadkeeper-hardening-next` made unresolved adjudication records
internally consistent. Candidate review now requires pending adjudication
metadata, the `adjudication_required` run status, and the task-contract review
flag to agree; a failed run carrying only the contract flag no longer creates
a false operator gate. Forty-two focused and all 1,209 provider-free hardening
tests plus 6 subtests passed, with compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry.

On 2026-08-07, ThreadKeeper commit `fcae412` on
`agent/threadkeeper-hardening-next` closed an escalation-status integrity gap.
Candidate review now accepts persisted adjudication metadata only when it
describes the exact unresolved runtime state (`required: true`, `status:
pending`); checksum-valid records can no longer forge operator-facing states
such as `approved` or pair `pending` with a false/missing review requirement.
Thirty-seven focused and all 1,195 provider-free hardening tests passed, plus
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-07, Protomega's PDF egress was proven independently (Telegram
receipt 9559), while genuine addressed requests exposed an ingress loss. A
provisional synchronous Bot-API repair was then found to leave the receiver
dormant while the MeTTa loop was idle: its only polling call was
`getLastMessage()`, which no idle loop reached. The runtime has been restored
to its preceding threaded Bot-API receiver (`TG_SYNC_POLL=false`); native PDF
egress remains intact. Twenty-six focused provider-free address, transport,
and document tests pass; the restarted supervisor has one worker, no MTProto
bridge, and logs `Polling started`. Final live human-authored end-to-end
acceptance remains pending. Evidence:
`experiments/20260807T125032Z-protomega-threaded-polling-rollback-r1/`.

On 2026-08-07, ThreadKeeper commit `a775f6b` on
`agent/threadkeeper-hardening-next` repaired an escalation-integrity regression
introduced by the exact-schema hardening. Runtime-generated adjudication
records include `candidate_turn`; review now accepts that declared field only
as an exact integer from 1 through the dispatch hard cap, while continuing to
reject unknown metadata. Thirty-five focused and all 1,192 provider-free
hardening tests passed, plus compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-06, ThreadKeeper commit `d6f6ac3` on
`agent/threadkeeper-hardening-next` made candidate escalation metadata exact.
Integrity-verified review records now reject undeclared fields in both
`task_contract` and `adjudication`, preventing forged markers such as
`approved: true` from reaching the parent/operator. Thirty-one focused and all
1,189 provider-free hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, Protomega gained a native bounded `send-document` OmegaClaw
action. The root cause of its repeated attachment failures was architectural:
raw model output is parsed as OmegaClaw actions and delivered directly through
the Telegram adapter, so OpenClaw's in-band `MEDIA:` reply convention never
reached the gateway. Commit `d914aaf` adds workspace-confined PDF/LaTeX
multipart delivery, prompt/tool wiring, and regressions. Six focused tests and
compilation pass; the supervisor restarted with one worker; a live delivery of
the revised Plain2MeTTa PDF returned Telegram receipt `9471`.

On 2026-08-06, Capacity 1.1 content-bound the public harness invocation seam to
the accepted v0.4 sandbox. Real Bubblewrap execution returns clean exact bytes,
but candidate `ValueError` is exposed as generic `RuntimeError`, contradicting
the frozen A07/N01--N10 interface. Three tests pass. Verdict:
`revision_required_before_harness_adoption`; candidate freeze, held-out reveal,
and runtime authority remain closed.

On 2026-08-06, ThreadKeeper commit `ba571bc` on
`agent/threadkeeper-hardening-next` made candidate patch proposal records an
exact schema. Integrity-verified review records carrying undeclared fields
such as a forged `approved` flag now fail closed instead of reaching the
parent/operator alongside valid action/path metadata. Six focused cases and
all 1,197 provider-free hardening tests plus 6 subtests passed, along with
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, ProtoCosmo2's Telegram transport began retaining a bounded
same-chat window of all received human- and bot-authored group text plus
extractable PDF/text document contents. Ambient updates never invoke the model
or produce replies; recent history is injected only on a mention/reply and is
explicitly marked untrusted. State-schema migration preserved the live cursor
and outbox. Commit `4da168b`; 31 focused tests pass; the restarted supervisor
is active with one runner and no pending inbound. Evidence:
`experiments/20260807T011248Z-protocosmo2-telegram-context-ingestion/`.

On 2026-08-06, ProtoCosmo2 gained bounded outbound Telegram document delivery
for PDF and LaTeX source. An agent must place a `MEDIA:/absolute/path`
directive on the first non-empty reply line. Only regular `.pdf`, `.tex`, and
`.latex` files below `/home/openclaw/research-agent` are accepted; the limit is
50 MB and captions are capped at Telegram's 1,024 characters. The document
path and metadata are recorded in the durable outbox before the Bot API
`sendDocument` call. Commit `6fd5e7e` plus runner commit `9bd6608`; 35 focused
provider-free tests and Python compilation pass; the supervised runner was
restarted successfully. Existing OpenClaw gateway delivery already supports
Telegram documents, so Protomega needs no gateway patch.

On 2026-08-06, ThreadKeeper commit `9778222` on
`agent/threadkeeper-hardening-next` made candidate-review patch proposal
metadata strict and bounded. Review now rejects unknown patch actions,
missing or unsafe workspace-relative paths, non-string content, and proposal
batches above the dispatch tool-call bound before returning metadata to a
parent/operator. Twenty-eight focused and all 1,186 provider-free subagent
hardening tests passed, plus compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-06, Capacity 1.1 recorded the missing pre-implementation R2
commitment for four exact A09--A12 held-out cases. The bounded/paraphrase and
live/mixed authority cases are committed as 9,132 exact bytes behind an
encrypted sealed copy; reveal remains unauthorized until a candidate SHA-256
is frozen. One direct check and four negative tests pass. R1, held-out
execution, harness adoption, generator authority, and runtime authority remain
open.

On 2026-08-06, ThreadKeeper commit `ef9bf3b` on
`agent/threadkeeper-hardening-next` made explicit run-index audit path
arguments exact and bounded before filesystem resolution. Empty strings,
leading/trailing whitespace, non-NFC spellings, control characters, and paths
above the hard argument cap now fail closed. Eight focused and all 1,181
provider-free subagent hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, Ben authorized `@Protocosmo2bot` for continuous text operation
in every Telegram group where it is a member. Config schema v2 permits any
negative group/supergroup chat ID and any human group sender, while DMs remain
Ben-only. Group activation requires a mention or reply; bot-authored and
unaddressed group updates are skipped with the durable cursor advanced.
Addressed PDF and selected text documents now receive bounded read-only
extraction into explicitly untrusted prompt context. The
restart-on-failure supervisor is active; 25 provider-free tests, compilation,
shell syntax, config validation, identity/capability probe, and live clean-state
checks pass; the document revision adds 27 passing focused tests. Attachment
egress, unsupported media, and state-changing extras remain disabled.


On 2026-08-06, ThreadKeeper commit `e91f221` on
`agent/threadkeeper-hardening-next` made queued-worker task path arguments
exact before any claim. Leading/trailing whitespace and non-NFC spellings now
fail closed without renaming the queued record. Fourteen focused and all 1,175
provider-free subagent hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, ThreadKeeper commit `8f299b6` on
`agent/threadkeeper-hardening-next` made candidate-review transcript path
arguments exact and bounded before filesystem resolution. Leading/trailing
whitespace, non-NFC spellings, control characters, and paths above the hard
argument cap now fail closed. Twenty-three focused and all 1,173 provider-free
subagent hardening tests passed, plus compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-06, ThreadKeeper commit `d0ee80b` on
`agent/threadkeeper-hardening-next` made candidate transcript review require
its checksum sidecar. Removing a sidecar can no longer downgrade a review to
unchecked acceptance; missing, malformed, or mismatched integrity evidence
fails closed. Eighteen focused and all 1,168 provider-free subagent hardening
tests passed, plus compilation, `git diff --check`, and draft PR #1
safety-floor ancestry.

On 2026-08-06, Capacity 1.1's content-bound v0.4 generic-failure sandbox
passed an independent replay of all twelve frozen adversarial cases. E1--E6
are covered, and the prior private stderr sentinel is now exposed only as the
exact generic failure `sandbox candidate failed`. Five independent tests and
compilation pass. Verdict: `r4_empirical_replay_pass`; R1/R2 and harness
adoption remain open, with no generator or runtime authority granted.

On 2026-08-06, ThreadKeeper commit `a28eacf` on
`agent/threadkeeper-hardening-next` added checksum sidecars for queued-worker
terminal result records. Both the compact result JSON and its checksum are now
durable before the final `*.done`/`*.failed` task rename publishes terminal
state. Six focused and all 1,167 provider-free subagent hardening tests passed,
plus compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, ThreadKeeper commit `2d290cf` on
`agent/threadkeeper-hardening-next` made persistent transcript publication
atomic with its checksum. Finished run bytes remain under a non-discoverable
staging name until the checksum sidecar is durable, and only the final
transcript rename publishes the record. Six focused and all 1,167
provider-free subagent hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, Capacity 1.1 content-bound a v0.4 generic-failure facade over
the frozen v0.3 Bubblewrap sandbox. Every sandbox `RuntimeError` now crosses
the parent API as the exact message `sandbox candidate failed`, so the private
stderr sentinel found by independent replay is not exposed. Four focused
revision tests, fourteen frozen twelve-case producer checks, and ten underlying
sandbox regressions pass, plus binding validation and compilation. Verdict is
`revision_ready_for_independent_replay`; R1/R2/R4 and harness adoption remain
open.

On 2026-08-06, ThreadKeeper commit `a0fd814` on
`agent/threadkeeper-hardening-next` made enqueue publication atomic with its
checksum. Queued task bytes remain under a non-discoverable staging name until
the checksum sidecar is durable, and only the final `queue/*.json` rename makes
the task visible to workers. Three focused and all 1,165 provider-free
subagent hardening tests passed, plus compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-06, ThreadKeeper commit `f300f5e` on
`agent/threadkeeper-hardening-next` preserved failure audit evidence when the
post-rename directory fsync reports an error. Once `*.claimed` has visibly
become `*.failed`, cleanup no longer deletes its staged checksum and compact
result record; rollback is only attempted before publication. Two focused and
all 1,164 provider-free subagent hardening tests passed, plus compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-06, an independently implemented Capacity 1.1 consumer bound and
replayed all twelve v0.3 sandbox cases without importing the producer tests.
Eleven pass, but E6 fails: a candidate stderr sentinel is returned verbatim in
the sandbox's `RuntimeError` on a contained network failure. Network isolation
holds, but output confinement does not. Five independent checks pass; verdict
is `revision_required_before_harness_adoption`. R1/R2/R4 remain open.

On 2026-08-06, ThreadKeeper commit `fe4fc73` on
`agent/threadkeeper-hardening-next` made queued-task failure publication atomic
with its audit evidence. The worker now stages the task checksum and compact
failure result before the `*.claimed` to `*.failed` rename; an injected
failure-result write error leaves the task claimed and removes provisional
artifacts rather than publishing an unauditable failure marker. Four focused
and all 1,163 provider-free subagent hardening tests passed, plus compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, ThreadKeeper commit `e1f3c47` on
`agent/threadkeeper-hardening-next` made queued-task completion fail closed.
The worker now stages the durable result record and task checksum before the
atomic `*.claimed` to `*.done` rename, making that rename the completion commit
point. An injected result-write failure leaves no false `*.done` marker and
retains the task as `*.failed`. Thirty-four focused and all 1,162 provider-free
subagent hardening tests passed, plus compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-05, Capacity 1.1 content-bound the frozen v0.3 effect contract to
the existing Bubblewrap sandbox sources and completed a producer-side replay
of all twelve required adversarial classes. Fourteen provider-free tests plus
the direct binding check pass, including new stdin, address-space, and
process-count probes. This is coverage evidence only; R1/R2/R4 remain open and
R4 still requires an independently implemented replay that does not import the
producer tests. Evidence:
`artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-binding/`.

On 2026-08-05, ThreadKeeper commit `e05191f` on
`agent/threadkeeper-hardening-next` closed an oversized quota-state bypass.
Rate/concurrency JSON above the bounded read cap now fails closed and remains
untouched instead of being treated as empty, so active reservations cannot be
discarded before a provider call. Twenty-one focused and all 1,161
provider-free subagent hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, ThreadKeeper commit `51912df` on
`agent/threadkeeper-hardening-next` closed a queued-task expiry bypass. When
age expiry is configured, a persisted `queued_at` farther in the future than
the bounded clock-skew allowance now fails before any worker dispatch, so a
forged or rollback-relative future timestamp cannot postpone expiry
indefinitely. Five focused and all 1,161 provider-free subagent hardening tests
passed, plus compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry.

ProtoCosmo2 Phase 6 is complete as a stopped, bounded private-canary result.
The dedicated identity accepted two fresh Ben-only plain-text DMs and routed
one reply to each; 17 provider-free contract/transport tests and a controlled
live restart-recovery check passed. The final state has no pending inbound,
zero incidents, and unchanged cursor/delivery records; the canary is stopped.
No group enrollment, attachment handling, autonomous scheduling,
state-changing extras, or ongoing Telegram service is authorized. Evidence:
`experiments/20260805T235502Z-protocosmo2-phase6-acceptance-provider-free/`
and `experiments/20260805T235543Z-protocosmo2-phase6-live-restart-recovery/`.

On 2026-08-05, ThreadKeeper commit `f5d4364` on
`agent/threadkeeper-hardening-next` made the supervised queued-worker runtime
bound and per-task duration accounting monotonic. Civil-clock rollback can no
longer extend `max_runtime_s`, and idle polling is capped to the remaining
deadline rather than sleeping past it. Three focused and all 1,160
provider-free subagent hardening tests passed, plus compilation, `git diff
--check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, ThreadKeeper commit `e7d9d6e` on
`agent/threadkeeper-hardening-next` moved dispatch elapsed-time, provider
timeout, and retry/backoff deadline enforcement from the adjustable civil clock
to `time.monotonic()`. Backward NTP/operator clock steps can no longer extend a
worker's configured safety bound, and forward steps cannot prematurely exhaust
it. Five focused and all 1,158 provider-free subagent hardening tests passed,
plus compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, an independent Capacity 1.1 R4 review stopped the Bubblewrap
sandbox before acceptance-harness adoption. A content-bound `ctypes` candidate
calls libc `fork`/`execl`, completes `/usr/bin/true`, and receives `pass`, so
the Python audit layer does not meet the frozen requirement that subprocess/
exec effects and monitor bypass fail. Bubblewrap still contains the process;
this is not a demonstrated host escape. Eight provider-free checks pass. Next:
freeze syscall-level no-effect enforcement or a narrower externally observable
effect contract, then independently replay it. R1/R2/R4 remain open.

On 2026-08-05, ThreadKeeper commit `e7459ff` on
`agent/threadkeeper-hardening-next` made persistent LLM rate/concurrency state
crash-safe. Stable sidecar locks now serialize atomic JSON replacements,
avoiding both quota loss from truncate/write interruption and stale-inode races
from locking the replaced data file. An injected replacement failure preserves
the active quota and fails closed. Twenty-seven focused and all 1,156
provider-free tests passed, plus compilation, `git diff --check`, and draft PR
#1 safety-floor ancestry.

On 2026-08-05, ThreadKeeper commit `9316269` on
`agent/threadkeeper-hardening-next` extended complete-batch validation to the
optional shell tool. Shell enablement, argv parsing/count, executable
allowlisting, and workspace availability now fail closed before any earlier
tool effect in the same worker response, preventing a valid file mutation from
being partially applied before a later invalid shell call is rejected. Twenty
focused and all 1,155 provider-free subagent hardening tests passed, plus
compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, ProtoCosmo2 gained a bounded OmegaClaw-native v1 adapter for
`persistent-subagent-orchestration` at Core commit `5c64918`, fast-forwarded
into `agent/protocosmo2-phase6-live`. It provides exact JSON MeTTa skills for
durable task creation/status/checkpoint/pause/resume/cancel and read-only
standing-approval adjudication. Immutable digest-bound manifests,
hash-chained bounded events, atomic writes, explicit state transitions, and
revocation/supersession/expiry/bound checks fail closed. Forty-four
provider-free tests passed, the modified Core loaded through pinned PeTTa, and
the dedicated mode-0700 state root passed a configured refusal smoke. V1 does
not spawn/schedule/execute, mutate or consume approval, call a provider, use
Telegram/shell, or perform remote compute. Evidence:
`experiments/20260805T160618Z-protocosmo2-persistent-worker-adapter-r6/` and
`experiments/20260805T160646Z-protocosmo2-persistent-worker-adapter-core-load/`.

On 2026-08-05, Capacity 1.1 replaced the bypassable cwd-only effect prototype
with an operational Bubblewrap containment prototype. It uses disposable
mount/network/PID namespaces, a read-only minimal runtime/work tree, scrubbed
environment, descendant teardown, and hard CPU/address-space/file/process/
output/wall-time limits. Ten provider-free adversarial tests pass, including
the exact symlink bypass and a native host-path write attempt. This is R4
revision evidence pending independent bypass review, not harness adoption,
generator authorization, or runtime authority.

On 2026-08-05, ThreadKeeper commit `bd592e1` on
`agent/threadkeeper-hardening-next` canonicalized inherited optional-shell
`PATH` directories before passing them to the child. The earlier containment
check resolved symlinks but retained their unresolved spelling, leaving a
retarget-after-validation command-lookup race. Missing absolute entries are
also dropped. Four focused and all 1,152 provider-free subagent hardening tests
passed, plus compilation, `git diff --check`, and draft PR #1 safety-floor
ancestry.

On 2026-08-05, ThreadKeeper commit `6751252` on
`agent/threadkeeper-hardening-next` closed a relative-`PATH` optional-shell
hijack. The sanitized child environment now drops every non-absolute inherited
`PATH` entry, preventing values such as `bin` from resolving an allowlisted
command to a workspace-controlled executable after the subprocess cwd is
pinned to the worker workspace. Three focused and all 1,150 provider-free
subagent hardening tests passed, plus compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry.

On 2026-08-05, an independent Capacity 1.1 R4 bypass review stopped the
import-inclusive effect sandbox before harness adoption. An `os.symlink`
adversary mutates a parent-owned path outside the child cwd while the prototype
reports `pass`; its Python audit hook also does not enforce native-call,
descendant, or resource containment. Eight provider-free checks pass. Next:
an OS-enforced disposable filesystem/network/process boundary with hard
resource/output caps; R1, R2, and R4 remain open.

On 2026-08-05, ThreadKeeper commit `001c216` on
`agent/threadkeeper-hardening-next` made optional-shell allowlist configuration
strict and bounded. Values above 16,384 characters or 256 entries, and entries
outside the 1--255 character ASCII command-name grammar, now fail closed before
subprocess execution. Thirteen focused and all 1,149 provider-free subagent
hardening tests passed, plus Python compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry.

On 2026-08-05, ThreadKeeper commit `ffbbf8a` on
`agent/threadkeeper-hardening-next` hard-capped RAG knowledge-prior reads.
`OMEGACLAW_MAX_KNOWLEDGE_FILE_BYTES` can no longer raise a single local
knowledge-file read above 64 MiB; the default remains 2 MiB. All 15 focused
provider-free RAG hardening tests passed, plus Python compilation,
`git diff --check`, and draft PR #1 safety-floor ancestry.

On 2026-08-05, Capacity 1.1 gained an operational import-inclusive no-effect
sandbox prototype. Candidate import and the bytes call share an isolated child
with a preinstalled audit boundary, scrubbed environment, timeout, and content
manifest; six provider-free adversarial tests pass. This is R4 prototype
evidence pending independent bypass review, not closure or generator/runtime
authorization. R1 executable cases and R2 held-out commitment remain open.

On 2026-08-05, ThreadKeeper commit `96b7f60` on
`agent/threadkeeper-hardening-next` hard-capped the remaining worker data and
dispatch configuration seam. Environment values can no longer raise persisted
patch proposals, final emits, or parsed worker responses above 1,000,000
characters; native response bodies above 16 MiB; queue age above one year;
one dispatch above 86,400 seconds or 10,000,000 tokens; workspace files above
64 Mi characters; or retained run-index entries above 1,000,000. All 1,144
provider-free subagent hardening tests passed, plus Python compilation and
`git diff --check`.

On 2026-08-04, ThreadKeeper commit `543525b` on
`agent/threadkeeper-hardening-next` hard-capped persistent worker setup/state
reads. Environment values can no longer raise queue/transcript JSON or audit
reads above 64 MiB, checksum sidecars above 64 KiB, escalation policies or
persona prompts above 16 MiB, persona configs or LLM guard state above 1 MiB,
or persona control scalars above 65,536 characters. All 1,143 provider-free
subagent hardening tests passed on the final full run, plus Python compilation
and `git diff --check`.

On 2026-08-04, ThreadKeeper commit `d0a136b` on
`agent/threadkeeper-hardening-next` hard-capped worker tool-return
configuration. Environment values can no longer raise shell/search/read output
above 1,000,000 characters or one shell subprocess above 600 seconds. All
1,142 provider-free subagent hardening tests passed on the final full run, plus
Python compilation and `git diff --check`.

On 2026-08-04, an independent Capacity 1.1 acceptance-v0.2 review stopped the
request-to-contract generator again. The exact bytes API closes R3 only at the
contract level; the 26 named cases have no executable bodies, no independent
held-out byte commitment exists, and candidate import occurs before an effect
monitor that is not implemented. Eight provider-free checks passed. Next:
freeze those three artifacts and repeat closure review; generator code and
runtime effects remain unauthorized.

On 2026-08-04, ThreadKeeper commit `33cbdda` on
`agent/threadkeeper-hardening-next` hard-capped budget/accounting read
configuration. Environment values can no longer raise usage-log reads above
64 MiB or budget-config reads above 1 MiB, preserving bounded quota and
escalation decisions. All 27 focused provider-free budget hardening tests
passed, plus Python compilation and `git diff --check`.

On 2026-08-04, ThreadKeeper commit `7130ffd` on
`agent/threadkeeper-hardening-next` hard-capped supervised queue/worker
configuration. Environment values can no longer raise pending/tasks above
4,096, idle polls above 3,600, poll sleeps above 300 seconds, one invocation
above 86,400 seconds, retained results or consecutive errors above 256, or
lock metadata above 65,536 bytes. Two focused checks and all 1,141
provider-free subagent hardening tests passed.

On 2026-08-04, ThreadKeeper commit `cd97ce8` on
`agent/threadkeeper-hardening-next` hard-capped task-contract configuration.
Environment values can no longer raise list fields above 256 entries, list
items above 8,192 characters, or objectives above 65,536 characters. The
focused 143-case contract slice and all 1,150 provider-free subagent hardening
tests plus six subtests passed.

On 2026-08-04, an independent Capacity 1.1 acceptance-harness review stopped
the request-to-contract generator before implementation. The preregistration
declares 20 cases, but its required command runs only 10 metadata tests and
never invokes a generator; five public fixtures also cannot exclude a
hard-coded lookup, and the input/effect-observation contracts remain
underspecified. Nine provider-free review tests passed. Next: revise and
independently close R1--R4; generator code and runtime effects remain
unauthorized.

On 2026-08-04, ThreadKeeper commit `75fc765` on
`agent/threadkeeper-hardening-next` hard-capped durable transcript retention.
Environment configuration can no longer raise retained transcript turns above
64, per-turn fields above 1,000,000 characters, or persisted summaries above
65,536 characters. Two focused and all 1,149 provider-free subagent hardening
checks passed.

On 2026-08-04, Ben explicitly accepted the Phase-5 go/no-go and authorized
Phase 6 in Protobots message 16261. The bounded private Telegram canary is now
the active gate. Offline transport hardening may proceed; live sending requires
a distinct ProtoCosmo2 bot identity and Ben-only configuration. The dedicated
`/home/openclaw/.openclaw/protocosmo2.env` was absent at preflight, and existing
bot credentials will not be reused.

On 2026-08-05, the Phase-6 provider-free transport contract passed 13 focused
tests at OmegaClaw-Core commit `2f714e9`. It fail-closes configuration, binds
both chat and user allowlists, rate/depth caps outbound messages, blocks
attachments, persists message deduplication and inbox/outbox cursor recovery,
and surfaces allowlisted failures through a fixed durable notice. The unchanged
Phase-5 structural preflight also passed (10 cases/7 critical controls), its dry
runner remained inert, and repair commit `bebe357` remains in ancestry. No
Telegram or provider traffic occurred. Live acceptance remains blocked on the
missing dedicated credential/config and still requires the controlled canary,
transcript/incident/latency-cost evidence, and separate go/no-go. Evidence:
`experiments/20260805T011343Z-protocosmo2-phase6-private-canary-preflight/`.

On 2026-08-04, ProtoCosmo2 Phase 5's post-response SIGSEGV was isolated to
embedded Python RPC socket lifecycle races under Janus/SWI (`POLLRDHUP`). Exact
real-response replay passed, and replacing both provider and shadow-channel
sockets with bounded private file bridges produced stable real-runtime runs.
Bounded read-only source injection then repaired the two project-record
retrieval/provenance failures without changing the frozen suite digest. A fresh
full run completed 10/10 with exit zero, and all seven critical answers met
their frozen intent on inspection. At that checkpoint the automated Phase-5
gates were complete but G5 qualitative review and an explicit go/no-go still
remained; Protobots message 16261 subsequently satisfied that gate. Evidence:
`experiments/20260804T211817Z-protocosmo2-phase5-retrieval-repair/`.

On 2026-08-04, ThreadKeeper commit `57ac088` on
`agent/threadkeeper-hardening-next` hard-capped bounded-history and return
configuration. Environment values can no longer raise worker turns or retained
history above 64, parent digests above 20,000 characters, or worker output
above 65,536 tokens. Two focused and all 1,138 provider-free subagent
hardening checks passed.

On 2026-08-04, Capacity 1.1 froze five exact request-to-contract generator
fixtures and a 20-case future implementation acceptance matrix. The corpus
covers semantic paraphrase equivalence, GoalChainer offline/live and mixed
authority boundaries, exact ordered provenance, and 12 fail-closed mutations.
Ten provider-free preregistration checks passed. Next is independent
fixture/harness review; generator code and runtime effects remain unauthorized.

On 2026-08-04, ThreadKeeper commit `bfb3de2` on
`agent/threadkeeper-hardening-next` hard-capped worker tool configuration.
Environment configuration can no longer raise per-dispatch or per-turn tool
quotas, path/tool/query/shell argument limits, or shell argv count without
bound. Eighteen focused and all 1,137 provider-free subagent hardening checks
passed.

On 2026-08-04, ThreadKeeper commit `df2d3be` on
`agent/threadkeeper-hardening-next` hard-capped worker LLM quota configuration.
Environment configuration can no longer raise the calls-per-minute guard above
600 or the cross-process concurrency guard above 64. Seven focused and all
1,136 provider-free subagent hardening checks passed.

On 2026-08-04, an independent Capacity 1.1 closure review confirmed that
interface v0.2 closes R1--R4: exact output types and bounds, contained
allowed-path grammar, and exact ordered provenance. Ten provider-free checks
passed. Next is fixture/acceptance-test preregistration; generator code and all
runtime effects remain unauthorized.

On 2026-08-04, ThreadKeeper commit `358ede3` on
`agent/threadkeeper-hardening-next` hard-capped the worker LLM reliability
controls. Environment configuration can no longer raise a single-call timeout
above 600 seconds, retries above five, or exponential-backoff base above 60
seconds. Nine focused and all 1,135 provider-free subagent hardening checks
passed.

On 2026-08-04, ThreadKeeper commit `b1c3d2f` on
`agent/threadkeeper-hardening-next` made persistent LLM quota/concurrency state
schema-exact. Parseable but wrong-shaped state now fails closed before provider
calls or reservations instead of coercing timestamps, resetting quotas, or
drops of malformed in-flight entries. All 1,132 provider-free subagent
hardening checks passed.

On 2026-08-04, Capacity 1.1 interface v0.2 addressed the independent review's
four blockers: exact output types, assigned output bounds, complete
OmegaClaw-contained allowed-path grammar, and exact ordered provenance
equality. Exact replay and nine provider-free negative tests passed. This is a
revision claim only; independent R1--R4 closure review is next, and generator
implementation plus all runtime effects remain unauthorized.

On 2026-08-04, ThreadKeeper commit `8b2ce80` on
`agent/threadkeeper-hardening-next` closed the primary LLM gateway seam. Main
provider construction now reuses the strict channel/auth `GATEWAY_URL`
validator, so ambiguous, credential-bearing, or malformed endpoints fail
before OpenAI client construction or provider effects. Forty-two focused
provider-free LLM/RAG/auth checks passed.

On 2026-08-04, ThreadKeeper commit `24462aa` on
`agent/threadkeeper-hardening-next` closed the RAG embedding gateway seam.
Embedding requests now reuse the channel/auth gateway URL validator, so
ambiguous, credential-bearing, or malformed `GATEWAY_URL` values fail before
OpenAI client construction or provider effects. Thirty-four focused
provider-free RAG/auth checks passed.

On 2026-08-04, an independent Capacity 1.1 interface review stopped the
request-to-contract generator before implementation. Interface v0.1 does not
assign exact types and declared bounds to output values, fully define
allowed-path grammar, or specify provenance ordering/canonicalization. Four
blocking findings and eight provider-free negative tests passed. Next: revise
the interface to v0.2 and independently close R1--R4; generator implementation
and all runtime effects remain unauthorized.

On 2026-08-03, ThreadKeeper commit `97e7c27` on
`agent/threadkeeper-hardening-next` made the shared gateway endpoint boundary
strict. Nonempty `GATEWAY_URL` values must now be bounded absolute HTTP(S) URLs
without whitespace/control ambiguity, userinfo credentials, query/fragment
data, backslashes, invalid ports, or non-NFC spelling before any auth or channel
request. Seventy-one focused provider-free channel/auth checks passed.

On 2026-08-03, ThreadKeeper commit `ef134ef` on
`agent/threadkeeper-hardening-next` made delegated tool-subset parsing strict
and bounded. Subsets must now be exact strings no longer than 1,024 characters
with unique, nonempty, control-free, NFC-normalized skill names before provider
or tool effects. All 1,119 provider-free subagent hardening checks passed.

On 2026-08-03, Capacity 1.1 froze a strict provider-free
request-to-contract generator interface before implementation. It binds exact
request/evidence provenance, bounded schemas, the existing six task-contract
fields, OmegaClaw-only paths, and effect `none`. Nine live, mixed-authority,
and ambiguous-scope triggers require `decision_required`; nine negative tests
passed. This authorizes only independent interface review, not a generator,
integration, dispatch, memory write, or runtime behavior change.

On 2026-08-03, ThreadKeeper commit `e2b3df2` on
`agent/threadkeeper-hardening-next` validated persona provider endpoint URLs.
Configured endpoints must now be absolute HTTP(S) URLs without whitespace,
userinfo credentials, query/fragment data, backslashes, invalid ports, or
non-NFC spelling before provider construction. Fifty-six focused provider-free
persona/config checks passed.

On 2026-08-03, ThreadKeeper commit `91f40f7` on
`agent/threadkeeper-hardening-next` hardened gateway authentication candidates.
When gateway authentication is configured, candidates must now be exact,
nonempty strings within 4 KiB and free of header/control ambiguity before any
request is constructed. Seven focused provider-free checks passed.

On 2026-08-03, ProtoCosmo2 Phase 5 froze a redacted ten-case behavioral
shadow-evaluation suite and passed a provider-free structural preflight. The
suite represents all seven critical safety/authority controls and has content
digest `9203c4a65edf128c3290c347099dcff32f28a02282e478b486a7f16ee175f6bf`.
This is not a behavioral-fidelity result: paired execution against ZeroBot and
ProtoCosmo2 needs a separately approved isolated model-provider/runtime setup.
No provider, Telegram channel, credential, listener, or shared writable state
was started. Evidence:
`experiments/20260803T203107Z-protocosmo2-phase5-shadow-preflight/`.

On 2026-08-03, the Phase 5 gateway-level paired-shadow harness was completed
and accepted offline. It composes the reviewed Phase 3 identity/policy drafts,
requires explicit execution, restricts endpoints to loopback, uses separate
ZeroBot/ProtoCosmo2 session identities, and requires outbound channels to be
disabled. This is not a behavioral result or a full OmegaClaw-loop test;
execution still requires an approved model and verified gateway session-header
contract. Evidence: `experiments/20260803T214622Z-protocosmo2-phase5-harness/`.

On 2026-08-04, a model-approved Phase 5 execution attempt selected
`openai/gpt-5.6-terra` (the gateway probe resolved to its `gpt-5.6-sol`
fallback), using no-delivery isolated CLI sessions. The full nested runner hung
before producing its first paired artifact and was stopped after more than
three minutes. This is a runtime-integration failure, not a behavioral score;
Phase 6 remains blocked. Evidence:
`experiments/20260804T032814Z-protocosmo2-phase5-shadow-execution/`.

On 2026-08-04, a real pinned-runtime repair disproved a gateway deadlock and
found four deeper integration defects: PeTTa `git-import!` was running an
unpinned upstream clone, host Python/policy wiring was incomplete, the local
embedding model was unavailable offline, and mock send acknowledgement/capture
failed. The first three were repaired and the 8,095 Phase 4 chunks were wired
into OmegaClaw's actual `memories` collection. The MeTTa loop reached the model
and recorded `(send ...)`, but mock delivery returned `False`; a clean retry
then timed out without a new turn. The frozen suite remains unexecuted and
Phase 6 blocked. Evidence:
`experiments/20260804T060000Z-protocosmo2-phase5-real-runtime-repair/`.

On 2026-08-04, a bounded follow-up repaired the Phase-5 case driver's stdout
capture/cleanup and its explicit project-scoped Python dependency selection.
One frozen Telegram-approval case traversed the pinned MeTTa loop and was
captured by the isolated mock server in 17.3 seconds. The process then emitted
`fatal signal 11 (segv)`, so this is evidence that mock capture can work, not a
stable runtime or behavioral-fidelity pass. The frozen ten-case suite remains
unexecuted and Phase 6 blocked pending a minimal Test-provider SIGSEGV
reproduction. Evidence:
`experiments/20260804T061920Z-protocosmo2-phase5-mock-rpc-gate-dependency-repair/`.

On 2026-08-03, an independently implemented Capacity 1.1 review bound and
replayed the v0.2 request-to-contract fixtures without importing producer code.
It confirms the GoalChainer authority pair, mixed-request fail-closed behavior,
semantic paraphrase equivalence, and retained `no_dispatch` controls. Eight
provider-free negative tests passed. The result authorizes only drafting a
strict generator interface contract; no generator implementation, integration,
dispatch, memory write, or runtime behavior change is authorized.

On 2026-08-03, ThreadKeeper commit `e09b284` on
`agent/threadkeeper-hardening-next` hardened local-dashboard pricing override
opens. The bounded reader now uses a no-follow descriptor and requires the
opened object to be a regular file, preventing symlink or non-regular
substitution from influencing accounting. Forty-three focused provider-free
local-channel checks passed.

On 2026-08-03, ThreadKeeper commit `ee6f671` on
`agent/threadkeeper-hardening-next` hardened local-dashboard reasoning-history
opens. The bounded incremental reader now uses a no-follow descriptor, requires
the opened object to be a regular file, and derives its read window from that
same descriptor. Fifty-four focused provider-free local-channel checks passed.

On 2026-08-03, Capacity 1.1 request-to-contract coverage v0.2 sealed the four
elements required by the prior discrimination review: a GoalChainer
offline/live minimal pair, a mixed analysis/activation negative, a semantic
paraphrase pair, and invariant-equivalence scoring. Exact replay and seven
provider-free negative tests passed. This authorizes no generator, integration,
dispatch, memory write, or runtime behavior change.

On 2026-08-03, ThreadKeeper commit `aff7eb8` on
`agent/threadkeeper-hardening-next` hardened the local-dashboard avatar file
boundary. Avatar reads now use a no-follow descriptor and require the opened
object to be a regular file, preventing symlink substitution or non-regular
inputs from being served. Fifty focused provider-free local-channel checks
passed.

On 2026-08-03, ThreadKeeper commit `9bbcf0f` on
`agent/threadkeeper-hardening-next` made durable transcript retention limits
mandatory. Turn, per-field, and summary caps now have finite defaults and
clamp configured or runtime zero to one instead of restoring unbounded run
records. All 1,112 focused provider-free subagent checks passed.

On 2026-08-03, ThreadKeeper commit `159d0f4` on
`agent/threadkeeper-hardening-next` bound run-index tail sizing to the same
no-follow regular-file descriptor used for the read. Atomic path replacement
can no longer make a stale preliminary size select the wrong audit tail and
fork the append-only hash chain. Thirty-two focused provider-free checks
passed.

On 2026-08-03, ThreadKeeper commit `8ac4294` on
`agent/threadkeeper-hardening-next` closed a knowledge-prior file-open race.
The bounded reader now opens with no-follow semantics and verifies the opened
descriptor is a regular file before reading, so a path swapped to a symlink or
non-regular input cannot reach embedding or collection mutation. Eight focused
provider-free checks passed.

On 2026-08-03, ThreadKeeper commit `49097a5` on
`agent/threadkeeper-hardening-next` made newly created workspace write/append
parent directories crash-durable. Each nested directory entry is now
parent-fsynced before the atomic file replacement below it. Five focused
provider-free checks passed.

On 2026-08-02, ThreadKeeper commit `ae8eeac` on
`agent/threadkeeper-hardening-next` closed the direct Agentverse remote-skill
argument boundary. Tavily queries and technical-analysis tickers must now be
nonempty exact strings within dedicated bounds, market symbols use a closed
grammar, and direct-call timeouts must be exact integers from 1 through 120
seconds. Invalid inputs fail before request-model construction or remote
dispatch. Nine focused provider-free checks passed.

On 2026-08-02, ProtoCosmo2 Phase 0 was frozen and Phase 1 produced a sanitized
read-only source snapshot: 639 SHA-256-bound files, all copied 0400, with 13
explicit exclusions. An initial intentionally fail-closed run exposed an
over-broad filename rule and a symlink candidate; the corrected policy records
both as reviewable evidence and the successful rerun independently reverified
every hash and permission. Candidate target commits are documented in
`docs/protocosmo2-phase0-freeze-2026-08-02.md`; no service, credential,
provider, Telegram, or other live capability was activated.

On 2026-08-03, ProtoCosmo2 Phase 2 provisioned a separate clean detached
candidate baseline at `protocosmo2/phase2-checked-baseline/`: OmegaClaw-Core
`b13b17e` (whose parent is `16d380d`), PeTTa `4ce1d0e`, and
petta_lib_chromadb `4563854`. Exact tree IDs and Git-object integrity were
verified, the pinned SWI-Prolog 9.3.36 ran the PeTTa `nars_tuffy` smoke, and
the Core's host-side mock transport passed 5/5 direct tests. The repository's
Docker-only test cleanup is unavailable on this host and is a recorded
integration limitation, not treated as a passing runtime test. No OmegaClaw
agent loop, provider, Telegram account, credential, external network listener,
or supervisor has been started. Evidence:
`experiments/20260803T050313Z-protocosmo2-phase2-detached-baseline/`,
`20260803T050328Z-protocosmo2-phase2-petta-smoke/`, and
`20260803T050430Z-protocosmo2-phase2-mock-channel-rerun/`.

On 2026-08-02, ThreadKeeper commit `0bcea38` on
`agent/threadkeeper-hardening-next` bounded local-dashboard usage-accounting
recall to 64 MiB total and 64 KiB per JSONL record. The reader now uses a
no-follow regular-file descriptor and stops before parsing oversized files or
records. Forty-one focused provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `49dfb6c` on
`agent/threadkeeper-hardening-next` bounded episode history recall to 64 MiB
plus one growth-detection byte and rejected symlink/non-regular inputs before
timestamp scanning. Nineteen focused provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `ee84d23` on
`agent/threadkeeper-hardening-next` made both audit parent-directory sync
helpers verify the opened descriptor is actually a directory before fsync.
Four focused provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `8f54d7c` on
`agent/threadkeeper-hardening-next` made the shared audit parent-directory
fsync refuse a symlink substituted after validation. Four focused
provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `4d7ea1c` on
`agent/threadkeeper-hardening-next` made newly created budget/accounting audit
directory entries crash-durable. The budget ledger's symlink-safe directory
creator now fsyncs each new ancestor before appending records below it.
Twenty-five focused provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `32842a6` on
`agent/threadkeeper-hardening-next` made newly created audit, queue, and
transcript directory entries crash-durable. The shared symlink-safe directory
creator now fsyncs each new directory's parent before files are created below
it. Nine focused provider-free checks passed.

On 2026-08-01, ThreadKeeper commit `aa87439` on
`agent/threadkeeper-hardening-next` made checksum sidecars bind the exact target
basename and reject trailing records. Queue and transcript integrity checks no
longer accept a valid digest relabeled for another file. Forty-eight focused
provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `38c48aa` on
`agent/threadkeeper-hardening-next` added a parent-directory fsync after each
durable run-index append. This preserves first creation of `index.jsonl`
across a crash/power loss boundary. Two focused provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `26a8e20` on
`agent/threadkeeper-hardening-next` added parent-directory fsyncs after queued
task claim, completion, and failure-retention renames. This preserves atomic
queue state transitions across a crash/power loss boundary. Three focused
provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `ce9c2b1` on
`agent/threadkeeper-hardening-next` bounded each RAG knowledge-prior read to
2 MiB plus one detection byte. Oversized, invalid-UTF-8, non-regular, and
symlink inputs now fail before embedding or collection mutation. Six focused
provider-free checks passed.

On 2026-07-31, an independent provider-free runner reproduced all four sealed
structural chemistry transfer holdouts and their exact score maps. Six checks
bind the frozen contract/policy and reject duplicate JSON, malformed or derived
features, and authority widening. Results remain candidate-only and authorize
no chemistry, scheduling, runtime, or ThreadKeeper effect.

On 2026-07-31, ThreadKeeper commit `c791766` on
`agent/threadkeeper-hardening-next` bounded local-dashboard avatar reads to
2 MiB plus one detection byte. Oversized and behavior-bearing byte bodies now
fail before HTTP response headers are committed. Forty-four focused
provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `77c014c` on
`agent/threadkeeper-hardening-next` bounded local `/send` request bodies to
64 KiB and made ambiguous, negative, typed, and oversized `Content-Length`
values fail before reading the body. Forty focused provider-free checks
passed.

On 2026-07-31, ThreadKeeper commit `a6fd94e` on
`agent/threadkeeper-hardening-next` bounded local-dashboard pricing override
reads to 64 KiB plus one detection byte. Oversized and invalid UTF-8 override
files now fail closed to built-in pricing. Twenty-five focused provider-free
checks passed.

On 2026-07-31, ThreadKeeper commit `5d820c8` on
`agent/threadkeeper-hardening-next` bounded bootstrap Telegram/Slack API reads
to 2 MiB and made their JSON/object/success-marker parsing fail closed. Twelve
focused provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `7cafd70` on
`agent/threadkeeper-hardening-next` bounded incremental local-dashboard
reasoning-history reads to 64 KiB per request. Offsets now remain byte-precise
even across invalid UTF-8. Twenty-five focused provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `aa2f188` on
`agent/threadkeeper-hardening-next` made escalation-policy and persona-prompt
read caps mandatory. Configured or runtime zero now clamps to one byte, so
setup-time integrity reads cannot be restored to unbounded reads. Five focused
provider-free checks passed.

On 2026-07-31, the independent chemistry candidate-scoring runner reproduced
all four sealed holdouts from the preregistered exact-integer policy. Six
provider-free checks cover sealed identity, strict JSON, malformed/derived
features, admission, exact scores, and effect-free authority. This remains an
adjudicated candidate gate and does not authorize a chemistry run or
ThreadKeeper effect.

On 2026-07-31, ThreadKeeper commit `cf9b97c` on
`agent/threadkeeper-hardening-next` made run-index and transcript audit read
caps mandatory. Configured or runtime zero now clamps to one byte, so the
read-only verifier cannot restore unbounded index scanning or transcript hash
reads. Seventeen focused provider-free verifier checks passed.

On 2026-07-31, ThreadKeeper commit `4bfe047` on
`agent/threadkeeper-hardening-next` made the workspace write/append size cap
mandatory. A configured or runtime zero now clamps to one character, so
`append-file` cannot restore an unbounded existing-file read and neither file
tool can restore unbounded output. Five focused provider-free checks passed.

On 2026-07-31, ThreadKeeper commit `1a1cde3` on
`agent/threadkeeper-hardening-next` made the native Ollama HTTP response cap
mandatory. Setting `OMEGACLAW_SUBAGENT_MAX_LLM_HTTP_RESPONSE_BYTES=0` now
clamps to one byte instead of restoring an unbounded response read. Three
focused provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `7d61846` on
`agent/threadkeeper-hardening-next` bounded Slack Web API response reads to
2 MiB plus one detection byte. Oversized and behavior-bearing response bodies
now fail closed before UTF-8 decoding or strict JSON parsing. Ten focused
provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `9308010` on
`agent/threadkeeper-hardening-next` bounded Mattermost REST JSON parsing to
2 MiB and exact built-in byte/string bodies. Oversized and behavior-bearing
bodies now fail closed before decoding. Thirteen focused provider-free checks
passed.

On 2026-07-30, ThreadKeeper commit `349b990` on
`agent/threadkeeper-hardening-next` bounded Agentverse/Tavily response
formatting to 1,000,000 exact-string characters before JSON decoding.
Oversized and behavior-bearing responses now fail closed. Five focused
provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `2908572` on
`agent/threadkeeper-hardening-next` bounded gateway authentication response
bodies to 64 KiB before UTF-8 decoding or strict JSON parsing. Thirty-three
focused provider-free channel checks passed.

On 2026-07-30, ThreadKeeper commit `80583c1` on
`agent/threadkeeper-hardening-next` bounded Telegram API response bodies to
2 MiB before UTF-8 decoding or strict JSON parsing. Twenty-eight focused
provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `a90d3e7` on
`agent/threadkeeper-hardening-next` made optional Telegram username, personal
name, and chat-title fields require exact strings at the `getUpdates` producer
boundary, before polling-offset mutation. Twenty-seven focused provider-free
checks passed.

On 2026-07-30, ThreadKeeper commit `703b60a` on
`agent/threadkeeper-hardening-next` made nested Telegram message, text, actor,
and actor-ID fields fail closed at the `getUpdates` producer boundary, before
polling-offset mutation. Twenty-one focused provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `1f823b1` on
`agent/threadkeeper-hardening-next` made Telegram `getUpdates` envelopes
require an exact list of exact objects with exact non-negative integer update
IDs before polling-offset mutation. Thirteen focused provider-free checks
passed.

On 2026-07-30, ThreadKeeper commit `b3127ad` on
`agent/threadkeeper-hardening-next` made final `emit` payload validation require
an exact built-in string before invoking string behavior. Three focused
provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `ef2f593` on
`agent/threadkeeper-hardening-next` made the bounded queue-drain parent return
reject non-finite JSON numbers at its producer boundary. Eleven focused
provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `4aa87bc` on
`agent/threadkeeper-hardening-next` made the tool-command normalizer require an
exact built-in string before invoking replacement, splitting, or other string
behavior. Seventeen focused provider-free checks passed.

On 2026-07-30, ThreadKeeper commit `b4522b7` on
`agent/threadkeeper-hardening-next` made operator-facing worker-loop and
run-index returns reject non-finite JSON numbers at their producer boundary.
Thirty-four focused provider-free worker-loop checks passed.

On 2026-07-29, ThreadKeeper commit `347dce1` on
`agent/threadkeeper-hardening-next` made the shared structured parent-return
helper reject non-finite JSON metadata in every size-reduction path. Three
focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `706bccc` on
`agent/threadkeeper-hardening-next` made budget/escalation YAML fail safely on
wrong-shaped, behavior-bearing, negative, out-of-range, and non-finite numeric
values. Invalid fields now fall back individually to conservative defaults
before accounting or escalation decisions. Twenty-four focused provider-free
checks passed.

On 2026-07-29, ThreadKeeper commit `27bb41a` on
`agent/threadkeeper-hardening-next` made the supervised worker-loop entrypoint
strictly validate structured results before emitting them. Duplicate keys,
non-standard numbers, and non-object roots now fail closed. Six focused
provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `b099bab` on
`agent/threadkeeper-hardening-next` made local HTTP JSON responses reject
non-finite numbers before committing response headers. Twenty-three focused
provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `d929440` on
`agent/threadkeeper-hardening-next` made the low-level tool-argument validator
require exact built-in string and list types. Behavior-bearing subclasses now
fail before length, conversion, path, query, or command handling. Twenty-one
focused provider-free checks passed.

On 2026-07-29, an independent provider-free review of the motivational
score-policy v0.2 generator implementation passed six checks. It binds the
implementation and preregistration, matches two OpenSSL digest vectors, and
checks transform, retry, exhaustion, and invalid-input behavior. No dataset
was materialized; materialization requires a separate decision.

On 2026-07-29, ThreadKeeper commit `9226fb6` on
`agent/threadkeeper-hardening-next` made queued-worker completion preflight its
strict JSON result record before renaming the claimed task to `.done`.
Non-finite or unserializable result metadata now follows the durable `.failed`
retention path instead of leaving a completed task without a result sidecar.
Thirty-one focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `b75ec16` on
`agent/threadkeeper-hardening-next` made persistent transcript and run-index
writers reject non-finite JSON numbers. Invalid records fail before atomic
replacement or index append, preserving the last valid audit state.
Thirty-two focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `6bcfc12` on
`agent/threadkeeper-hardening-next` made supervised-worker lock metadata
serialization strict and non-destructive on serialization failure. Invalid or
non-finite metadata can no longer truncate the last valid operator-visible
worker state. Three focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `093cb00` on
`agent/threadkeeper-hardening-next` made LLM quota/concurrency state
serialization strict and non-destructive on serialization failure. Invalid or
non-finite state can no longer truncate the last valid guard record before
failing. Eleven focused provider-free checks passed.

On 2026-07-29, the revised motivational score-policy v0.2 synthetic-generator
preregistration passed an independent R1--R4 review. Seven provider-free checks
content-address the revision and policy, prove every candidate-witness region
selects its declared action across the full modular range, and verify both
799/800 boundary pairs. This authorizes only a separate non-materializing
implementation gate; no dataset, fitting, memory, provider, or runtime change.

On 2026-07-29, ThreadKeeper commit `43521bb` on
`agent/threadkeeper-hardening-next` made budget usage/escalation and worker
usage audit writers reject non-finite JSON numbers. Writers can no longer
persist `NaN`/`Infinity` records that strict readers subsequently discard.
Three focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `476a39c` on
`agent/threadkeeper-hardening-next` serialized worker usage JSONL appends with
cross-process exclusive locks. Concurrent worker processes can no longer
interleave accounting records; no-symlink, flush, fsync, and best-effort
logging behavior remain intact. Five focused provider-free checks passed.

On 2026-07-29, ThreadKeeper commit `ee0f512` on
`agent/threadkeeper-hardening-next` serialized usage and escalation JSONL
audit-log appends with cross-process exclusive locks. Concurrent writers can
no longer interleave partial records; existing no-symlink, flush, fsync, and
fail-safe response-path behavior is preserved. Fifteen focused provider-free
checks passed.

On 2026-07-28, ThreadKeeper commit `f99a625` on
`agent/threadkeeper-hardening-next` bounded the episode-recall timestamp bridge
argument to 23 characters before normalization, parsing, or history reads.
Plain, quoted, and MeTTa-escaped valid timestamps retain their behavior.
Fourteen focused provider-free checks passed.

On 2026-07-28, ThreadKeeper commit `53ebe6c` on
`agent/threadkeeper-hardening-next` made episode recall scan history with
bounded working memory instead of retaining the full file. The nearest
timestamp and requested surrounding-line semantics are preserved, with memory
bounded by the already validated 0--1000 radius. Eleven focused provider-free
checks passed.

On 2026-07-28, ThreadKeeper commit `df20549` on
`agent/threadkeeper-hardening-next` made the MeTTa/Python episode-recall bridge
require an exact timestamp string and an exact integer radius bounded to
0--1000. Behavior-bearing subclasses, booleans, coercible scalars, negative
values, and oversized recalls now fail before string or numeric behavior and
before history-file reads. Nine focused provider-free checks passed.

On 2026-07-28, ThreadKeeper commit `447c6e7` on
`agent/threadkeeper-hardening-next` made persisted usage-accounting records
require exact object, model-string, non-negative integer token-counter, and
finite non-negative timestamp types. Malformed records are skipped before
dashboard accounting. Twenty focused provider-free checks passed.

On 2026-07-28, ThreadKeeper commit `c0b3c7d` on
`agent/threadkeeper-hardening-next` made queued-worker result envelopes use
strict JSON and exact object roots before completion/error accounting or
result persistence. Duplicate keys, non-standard `NaN`/`Infinity`, and
non-object roots now fail closed. Thirty-eight focused checks and the
1077-test provider-free hardening suite passed.

On 2026-07-28, ThreadKeeper commit `57c9ebf` on
`agent/threadkeeper-hardening-next` made the local HTTP `/send` request body
use strict JSON and exact string fields. Duplicate keys, non-standard
`NaN`/`Infinity`, invalid UTF-8, non-object roots, and non-string
`message`/`auth` values now fail closed before authentication or inbound
message processing. Eleven focused checks and the 1099-test provider-free
hardening gate passed.

On 2026-07-28, ThreadKeeper commit `2dcab8e` on
`agent/threadkeeper-hardening-next` made Mattermost REST and websocket
responses use strict JSON. Duplicate keys, non-standard `NaN`/`Infinity`,
invalid UTF-8, and non-object roots now fail closed before identity, profile,
event, or post processing. Ten focused provider-free checks passed.

On 2026-07-28, the motivational score-policy v0.2 combined evidence freeze
content-addressed all three preregistration/execution pairs and recomputed 20
executed cases with all four candidates reached. Five provider-free checks
pass, including strict JSON, source/report identity, aggregate recomputation,
and candidate-only authority. No calibration or runtime change was performed.

On 2026-07-28, ThreadKeeper commit `123d84e` on
`agent/threadkeeper-hardening-next` made Slack Web API responses use strict
JSON. Duplicate keys, non-standard `NaN`/`Infinity`, invalid UTF-8,
non-object roots, and non-boolean success markers now fail closed before
Slack response processing. Seven focused checks and the 1095-test
provider-free hardening suite passed.

On 2026-07-28, ThreadKeeper commit `80c7fa0` on
`agent/threadkeeper-hardening-next` made local RPC envelopes and their nested
request/response payloads use strict JSON. Duplicate keys and non-standard
`NaN`/`Infinity` now fail closed before RPC dispatch or response delivery.
Eight focused checks and the 1111-test provider-free hardening suite passed.

On 2026-07-28, an independent provider-free runner executed the sealed
motivational score-policy v0.2 joint-feature holdouts. All seven selections
reproduced while all three admitted inputs varied together. Six negative-path
checks pass; candidate-only, ThreadKeeper effect `none`, and no calibration
was performed.

On 2026-07-28, ThreadKeeper commit `802fadd` on
`agent/threadkeeper-hardening-next` made gateway authentication responses use
strict JSON. Duplicate keys, non-standard `NaN`/`Infinity`, invalid UTF-8,
non-object roots, and non-boolean authorization markers now fail closed before
authentication state or token acceptance. Three focused checks and the
1103-test provider-free hardening suite passed.

On 2026-07-28, ThreadKeeper commit `900dc51` on
`agent/threadkeeper-hardening-next` made Agentverse/Tavily search responses use
strict JSON. Duplicate object keys and non-standard `NaN`/`Infinity` tokens
now bypass structured result extraction instead of influencing search context.
Three focused checks and the 1100-test provider-free hardening suite passed.

On 2026-07-28, a seven-case motivational score-policy v0.2 joint-feature
suite was preregistered before execution. Every out-of-sample case varies
evidence sufficiency, clarification need, and sub-override review risk
together, probing four candidate regions and conservative tie behavior. Eight
provider-free contract checks pass; candidate-only, ThreadKeeper effect
`none`, and no calibration was performed.

On 2026-07-28, ThreadKeeper commit `297f362` on
`agent/threadkeeper-hardening-next` made Telegram Bot API responses use strict
JSON. Duplicate object keys, non-standard `NaN`/`Infinity` tokens, invalid
UTF-8, non-object roots, and non-boolean success markers now fail closed
before update/auth/message processing. Six focused checks and the 1097-test
provider-free hardening suite passed.

On 2026-07-27, ThreadKeeper commit `edee61f` on
`agent/threadkeeper-hardening-next` made native Ollama-compatible provider
responses use strict JSON. Duplicate object keys and non-standard
`NaN`/`Infinity` tokens now fail closed as `provider_response_invalid` before
response fields can influence worker output or accounting. Four focused checks
and the 1091-test provider-free hardening suite passed.

On 2026-07-27, an independent provider-free runner executed the sealed
motivational score-policy v0.2 boundary holdouts. All eight exact/adjacent
inspect/answer, inspect/request, and review-override cases reproduced. Five
negative-path tests pass; candidate-only, ThreadKeeper effect `none`, and no
calibration was performed.

On 2026-07-27, ThreadKeeper commit `d726db4` on
`agent/threadkeeper-hardening-next` made local-channel pricing overrides and
usage-ledger records use strict JSON. Duplicate object keys and non-standard
`NaN`/`Infinity` tokens can no longer influence displayed token or cost
accounting. Three focused checks and the 1088-test provider-free hardening
suite passed.

On 2026-07-27, ThreadKeeper commit `749cc91` on
`agent/threadkeeper-hardening-next` made persisted budget usage-ledger records
use strict JSON. Duplicate object keys and non-standard `NaN`/`Infinity`
tokens are ignored as malformed records rather than influencing token and cost
accounting. Fourteen focused checks and the 1085-test provider-free hardening
suite passed.

On 2026-07-27, an eight-case motivational score-policy v0.2 boundary suite
was preregistered before execution. It seals exact and adjacent
inspect/answer and inspect/request boundaries plus the adjacent 799/800 review
override. Seven provider-free contract checks pass; candidate-only,
ThreadKeeper effect `none`, and no calibration was performed.

On 2026-07-27, ThreadKeeper commit `1bd8008` on
`agent/threadkeeper-hardening-next` made persisted async-worker lock metadata
use strict JSON. Duplicate object keys and non-standard `NaN`/`Infinity`
tokens now fail closed instead of influencing stale-worker diagnostics.
Six focused checks and the 1084-test provider-free hardening suite passed.

On 2026-07-27, ThreadKeeper commit `3779c9a` on
`agent/threadkeeper-hardening-next` made inline task-contract objects use
strict JSON. Duplicate object keys and non-standard `NaN`/`Infinity` tokens
now fail closed as persistent `contract_invalid` records before escalation or
worker/provider calls. Seven focused checks and the 1081-test provider-free
hardening suite passed.

On 2026-07-27, an independent provider-free runner executed the sealed
motivational score-policy v0.2 witnesses without importing the
preregistration validator or prior runners. All five selections reproduced,
all four candidates were reachable, and the derived evidence gap was
recomputed from admitted inputs. Eight checks pass; candidate-only,
ThreadKeeper effect `none`, and no calibration was performed.

On 2026-07-27, ThreadKeeper commit `d6b1b96` on
`agent/threadkeeper-hardening-next` made persisted LLM rate/concurrency quota
state use strict JSON. Duplicate object keys and non-standard
`NaN`/`Infinity` tokens now fail closed before a quota reservation or provider
call. Eight focused checks and the 1083-test provider-free hardening suite
passed.

On 2026-07-27, ThreadKeeper commit `6f4f10d` on
`agent/threadkeeper-hardening-next` made persona configuration reads use
strict JSON. Duplicate object keys and non-standard `NaN`/`Infinity` tokens
now fail closed before provider/model/tool/task-contract selection or any
worker call. Nine focused checks and the 1077-test provider-free hardening
suite passed.

On 2026-07-27, motivational score-policy v0.2 was preregistered as a
candidate-only response to the independently confirmed v0.1 structural
dominance result. It derives an exact evidence-gap feature from admitted
inputs, rejects caller-supplied derived values, preserves conservative review
behavior, and seals reachability witnesses for all four candidates. Eight
provider-free checks pass; ThreadKeeper effect remains `none`.

On 2026-07-27, ThreadKeeper commit `945de9e` on
`agent/threadkeeper-hardening-next` made persisted control-record reads use
strict JSON. Duplicate object keys and non-standard non-finite number tokens
now fail closed in queued tasks, candidate transcripts, and run-index
append/rotation/audit paths instead of being silently collapsed or accepted by
Python's permissive decoder. Five new focused cases and the 1069-test
provider-free hardening suite passed.

On 2026-07-27, ThreadKeeper commit `8669f16` on
`agent/threadkeeper-hardening-next` made the read-only run-index auditor reject
malformed persisted entry containers and decision-relevant scalar fields
before hashing, normalization, path resolution, or transcript reads. String
metadata requires exact JSON strings; timestamps require finite JSON numbers
or null. Fourteen focused checks and the 1064-test provider-free hardening
suite passed.

On 2026-07-27, an independent provider-free runner executed the sealed
motivational score-policy feature-interaction suite without importing its
validator or prior runners. All seven selections and reasons reproduced, and
the frozen coefficient/tie-order check confirmed that `inspect_evidence` is
structurally dominated throughout the valid domain. Eight checks pass;
candidate-only, ThreadKeeper effect `none`, and no calibration was performed.

On 2026-07-27, ThreadKeeper commit `4a141fd` on
`agent/threadkeeper-hardening-next` made candidate transcript review fail
closed unless every decision-relevant persisted field has its exact JSON
type. Patch proposals, adjudication metadata, task contracts, statuses, and
summaries are validated before truth testing, slicing, or construction of an
operator-facing review result. Fifteen focused checks and the 1063-test
provider-free hardening suite passed.

On 2026-07-27, ThreadKeeper commit `e834d39` on
`agent/threadkeeper-hardening-next` closed parent/operator path-argument
boundaries for run-index audit, candidate transcript review, and worker
stop-file controls. These paths now require exact built-in strings (or null
where allowed) before truth testing, comparison, coercion, or filesystem path
resolution. Eight focused checks and the 1054-test provider-free hardening
suite passed.

On 2026-07-27, ThreadKeeper commit `9091e2e` on
`agent/threadkeeper-hardening-next` closed the direct `run_tools()` control
boundary. Call batches are exact-type checked before truth testing; allowed
tool containers/items and optional quotas are exact-type checked before
iteration, membership, comparison, or coercion. Nine focused checks and the
1051-test provider-free hardening suite passed.

On 2026-07-27, an out-of-sample motivational score-policy feature-interaction
suite was preregistered without changing parameters. Seven sealed cases probe
joint feature pressure, two score crossovers, and the risk override. The
contract also records the structural finding that `inspect_evidence` is
dominated by `defer_for_review` across the valid v0.1 domain and is therefore
unreachable. Nine provider-free checks pass. Candidate-only; ThreadKeeper
effect `none`.

On 2026-07-26, ThreadKeeper commit `896a38e` on
`agent/threadkeeper-hardening-next` made the operator-facing queued-dispatch
path require an exact non-empty built-in string. Non-string values and
behavior-bearing string subclasses now return `queue_worker_error` before
coercion, queue-directory access, task claim, or worker effects. Nine focused
checks and the 1047-test provider-free hardening suite passed.

On 2026-07-26, the motivational score-policy boundary holdout was
preregistered before execution. Its content-addressed five-case suite
discriminates four-way and request/review ties, a one-unit rank change, and
the adjacent 799/800 review-risk override boundary. Eight provider-free
contract checks pass. Candidate-only; ThreadKeeper effect `none`.

On 2026-07-26, ThreadKeeper commit `d8254ad` on
`agent/threadkeeper-hardening-next` made direct dispatch integer limits and
goal/tool-subset/persona scalar arguments require exact built-in types.
Behavior-bearing integer and string subclasses now return persistent
`dispatch_args_invalid` records before overloaded operations, persona setup,
or worker/provider calls. Five focused checks and the 1039-test provider-free
hardening suite passed.

On 2026-07-26, ThreadKeeper commit `c16efa7` on
`agent/threadkeeper-hardening-next` made the bounded manual queue-drain
`max_tasks` quota require an exact non-negative built-in integer. Booleans,
strings, floats, negative integers, and behavior-bearing integer subclasses
now return `worker_config_invalid` before queue enumeration or worker effects.
Seven focused checks and the 1034-test provider-free hardening suite passed.

On 2026-07-26, ThreadKeeper commit `bb9cd07` on
`agent/threadkeeper-hardening-next` made explicit supervised-worker task,
idle, error, poll, and runtime bounds require exact built-in numeric types.
Behavior-bearing integer and float subclasses now fail closed before
overloaded operations, lock acquisition, or queue effects. Two focused checks
and the 1029-test provider-free hardening suite passed.

On 2026-07-26, ThreadKeeper commit `e67e05e` on
`agent/threadkeeper-hardening-next` made persona configuration containers,
task contracts, scalar strings, output-token limits, and default tool lists
require exact built-in types. Behavior-bearing subclasses now fail closed
during setup before overloaded operations or worker/provider calls. Five
focused checks and the 1015-test provider-free hardening suite passed.

On 2026-07-26, an independent provider-free runner executed the sealed
motivational score-policy v0.1 without importing its preregistration validator.
It reproduced all three registered selections, including the review-risk
override, while sealed-byte mutation, malformed features, expectation drift,
and authority widening failed closed. Five checks pass; candidate-only,
ThreadKeeper effect `none`.

On 2026-07-26, ThreadKeeper commit `f0ed2da` on
`agent/threadkeeper-hardening-next` made durable queued-dispatch task
containers, status/identity/path strings, timestamps, tool lists/items,
limits, and nested contracts require exact built-in types. Behavior-bearing
subclasses now fail closed during queue-record validation before overloaded
operations, queue execution, or worker effects. Six focused checks and the
1010-test provider-free hardening suite passed.

On 2026-07-26, ThreadKeeper commit `5d964c6` on
`agent/threadkeeper-hardening-next` made task-contract mappings, objectives,
string-list containers/items, quotas, and boolean policy fields require exact
built-in types. Behavior-bearing subclasses now fail closed before overloaded
membership, truth, length, string, or numeric operations can run. Four focused
checks and the 1017-test provider-free hardening suite passed.

On 2026-07-26, ThreadKeeper commit `2886862` on
`agent/threadkeeper-hardening-next` made authenticated OpenAI-compatible
`usage.total_tokens` require an exact built-in integer. Behavior-bearing
integer subclasses now fail closed as `provider_response_invalid` before
overloaded comparison or arithmetic can run. Five focused checks and the
1013-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `dd251e8` on
`agent/threadkeeper-hardening-next` made authenticated OpenAI-compatible
completion object/model/reason/role/index metadata, choice containers, and
SDK extra-field mappings require exact built-in types. Behavior-bearing
subclasses now fail closed as `provider_response_invalid` before overloaded
comparison, length, or truth operations can run. Seven focused checks and the
1012-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `9fda4c5` on
`agent/threadkeeper-hardening-next` made native-provider `thinking` metadata
require an exact built-in string when non-null. Behavior-bearing string
subclasses now fail closed as `provider_response_invalid` before overloaded
equality can run. Four focused checks and the 1005-test provider-free
hardening suite passed.

On 2026-07-25, ThreadKeeper commit `11c46d6` on
`agent/threadkeeper-hardening-next` made authenticated native-provider response
and message mappings require exact built-in dictionaries, and model,
creation-time, role, and completion-reason metadata require exact built-in
strings. Behavior-bearing subclasses now fail closed as
`provider_response_invalid` before overloaded iteration, comparison, or
normalization can run. Six focused checks and the 1004-test provider-free
hardening suite passed.

On 2026-07-25, ThreadKeeper commit `a8d338b` on
`agent/threadkeeper-hardening-next` made authenticated native-provider duration
and context metadata require exact built-in list/integer types.
Behavior-bearing subclasses now fail closed as `provider_response_invalid`
before overloaded comparison or iteration can run. Twenty-one focused checks
and the 998-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `e638a15` on
`agent/threadkeeper-hardening-next` made authenticated OpenAI-compatible
response IDs and creation timestamps require exact built-in scalar types.
Behavior-bearing string/integer subclasses now fail closed as
`provider_response_invalid` before overloaded provider metadata behavior can
run. Nineteen focused checks and the 982-test provider-free hardening suite
passed.

On 2026-07-25, ThreadKeeper commit `d2c8611` on
`agent/threadkeeper-hardening-next` made authenticated provider usage counters
require exact built-in integers. Behavior-bearing integer subclasses now fail
closed as `provider_response_invalid` before comparison, aggregation, logging,
or transcript operations. Three focused checks and the 980-test provider-free
hardening suite passed.

On 2026-07-25, ThreadKeeper commit `1d830c9` on
`agent/threadkeeper-hardening-next` made the authenticated provider payload
boundary require exact built-in string content. Behavior-bearing string
subclasses now fail closed as `provider_response_invalid` before parser,
prompt, or transcript operations. Two focused checks and the 978-test
provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `497c9c8` on
`agent/threadkeeper-hardening-next` closed the direct `run_tools()` boundary
to behavior-bearing list, tuple, and string subclasses before any tool effect.
Eleven focused checks and the 982-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `f8335c2` on
`agent/threadkeeper-hardening-next` made tool-response parser exceptions fail
closed as persistent `skill_protocol_error` transcripts and bounded structured
parent returns. Exception details are not exposed. Seven focused checks and
the 985-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `814be73` on
`agent/threadkeeper-hardening-next` made every parsed tool argument value
require an exact built-in string. Behavior-bearing string subclasses and
non-string values now produce persistent `skill_protocol_error` records before
any earlier tool in the batch can take effect. Six focused checks and the
983-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `cbbc36f` on
`agent/threadkeeper-hardening-next` made the closed parser-output boundary
reject list, tuple, and string subclasses. These behavior-bearing containers
now produce persistent `skill_protocol_error` records before any tool effect.
Nine focused checks and the 968-test provider-free hardening suite passed.

On 2026-07-25, ThreadKeeper commit `a43aa39` on
`agent/threadkeeper-hardening-next` made `dispatch()` validate the complete
parsed tool-call batch before destructuring or recording it. Non-list batches,
non-tuple records, non-string names, and non-list argument containers now
produce persistent structured failures instead of escaping through a Python
unpacking/type error. Five focused checks and the 964-test provider-free
hardening suite passed.

On 2026-07-24, ThreadKeeper commit `2bad03e` on
`agent/threadkeeper-hardening-next` made final structured `emit` returns reject
lone Unicode surrogate code points and non-NFC text before a parent digest or
successful transcript can be produced. Two focused checks and the 959-test
provider-free hardening suite passed.

On 2026-07-24, a provider-free motivational-registry holdout fixed the
cross-runtime integer domain at `9007199254740991`. Both strict consumers
accept that boundary through representation parsing, reject the next integer,
and admit a new supplementary-plane Unicode scalar through representation
preflight. Three orchestration checks, both pinned suites, and the refreshed
seven-check content-addressed admission gate pass. Candidate-only;
ThreadKeeper effect `none`.

On 2026-07-24, ThreadKeeper commit `3973119` on
`agent/threadkeeper-hardening-next` made final `emit` records participate in
the complete tool-call batch argument preflight. A malformed scalar, tuple,
mapping, or null emit container can no longer coexist with and permit an
earlier valid tool effect. Four focused checks and the 958-test provider-free
hardening suite passed.

On 2026-07-24, ThreadKeeper commit `896f0bf` on
`agent/threadkeeper-hardening-next` made the worker tool-call batch boundary
reject non-list batches and malformed call records before tuple unpacking or
any earlier valid tool effect. Four focused checks and the 962-test
provider-free hardening suite passed.

On 2026-07-24, a provider-free admission gate content-addressed the strict
Python and Node.js motivational-registry consumers and required each to own
raw-byte rejection of noncanonical integers, invalid Unicode representation,
and duplicate members at three schema depths. Seven admission checks and both
pinned suites pass. Candidate-only; ThreadKeeper effect `none`.

On 2026-07-24, ThreadKeeper commit `c0e4a61` on
`agent/threadkeeper-hardening-next` made the worker tool-call schema reject
non-string tool names and non-list argument containers. Scalar strings,
tuples, mappings, and null can no longer be mistaken for argument arrays and
unpacked into tool effects. Four focused checks and the 968-test provider-free
hardening suite passed.

On 2026-07-24, ThreadKeeper commit `bd58fac` on
`agent/threadkeeper-hardening-next` rejected internal U+1680 OGHAM SPACE MARK
in file-tool and task-contract paths. This non-ASCII Unicode space survives
NFKC instead of becoming ASCII space, but now fails before worker LLM,
contract authorization, audit, or filesystem effects. Four focused checks and
the 965-test provider-free hardening suite passed.

On 2026-07-24, a separately implemented strict Node.js motivational-registry
consumer reproduced the admitted candidate-set SHA-256 from both byte-distinct
fixtures. It rejected three noncanonical numeric spellings, non-NFC text, a
lone surrogate, and duplicate members at registry, candidate, and nested-
contract depths before semantic hashing. Ten provider-free checks pass.
Candidate-only; ThreadKeeper effect `none`.

On 2026-07-24, ThreadKeeper commit `e74bcbe` on
`agent/threadkeeper-hardening-next` rejected U+2800 BRAILLE PATTERN BLANK in
file-tool and task-contract paths. This visually empty symbol now fails before
worker LLM, contract authorization, audit, or filesystem effects. Thirty-six
focused checks and the 961-test provider-free hardening suite passed.

On 2026-07-24, ThreadKeeper commit `f03fcf0` on
`agent/threadkeeper-hardening-next` rejected U+16FE4 KHITAN SMALL SCRIPT
FILLER in file-tool and task-contract paths. This non-format combining mark
now fails before worker LLM, contract authorization, audit, or filesystem
effects. Thirty-two focused checks and the 957-test provider-free hardening
suite passed.

On 2026-07-24, an independent Python strict-JSON motivational-registry
consumer reproduced the admitted candidate-set SHA-256 from both
byte-distinct fixtures. It rejected all five representation-preflight
negatives plus duplicate members at registry, candidate, and nested-contract
depths before semantic hashing. Ten checks pass; candidate-only, adjudication
required, ThreadKeeper effect `none`.

On 2026-07-24, ThreadKeeper commit `f5e873d` on
`agent/threadkeeper-hardening-next` rejected the visually empty Khmer inherent
vowel controls U+17B4/U+17B5 in file-tool and task-contract paths. They now
fail before worker LLM, contract authorization, audit, or filesystem effects.
Twenty-eight focused checks and the 953-test provider-free hardening suite
passed.

On 2026-07-24, ThreadKeeper commit `0cf8295` on
`agent/threadkeeper-hardening-next` rejected invisible Unicode fillers in
file-tool and task-contract paths. U+034F, U+115F, U+1160, U+3164, and U+FFA0
now fail before worker LLM, contract authorization, audit, or filesystem
effects. Twenty focused checks and the 945-test provider-free hardening suite
passed.

On 2026-07-24, a provider-free motivational-registry representation preflight
preserved the admitted candidate-set SHA-256 for both byte-distinct fixtures
while rejecting canonical-integer aliases (`-0`, `0e0`, and `0.0`),
non-NFC strings, and lone surrogates. Seven checks pass. This changes no
admitted hash, candidate authority, ThreadKeeper behavior, or live runtime.

On 2026-07-24, ThreadKeeper commit `0dbd260` on
`agent/threadkeeper-hardening-next` rejected Unicode symbols whose NFKC form
contains an embedded path separator. The symbols ℀, ℁, ℅, and ℆ can no longer
be admitted as filename text and later normalize to `a/c`, `a/s`, `c/o`, or
`c/u`. Twenty-eight focused checks and the 925-test provider-free hardening
suite passed.

On 2026-07-24, ThreadKeeper commit `934d58e` on
`agent/threadkeeper-hardening-next` rejected Unicode compatibility characters
whose NFKC form contains an ASCII space in file-tool and task-contract paths.
Compatibility spaces can no longer survive inside a path component and later
normalize into a trailing ASCII-space alias. Twenty-eight focused checks and
the 896-test provider-free hardening suite passed.

On 2026-07-24, a third independently implemented motivational-registry
consumer reproduced the admitted candidate-set SHA-256 from both byte-distinct
fixtures using Node.js built-ins. Seven provider-free checks cover convergence
and fail-closed semantic mutation, authority widening, unknown fields,
reordering, and fractional ordinals. Candidate-only; ThreadKeeper effect
`none`.

On 2026-07-24, ThreadKeeper commit `8403e06` on
`agent/threadkeeper-hardening-next` made task-contract `allowed_paths` require
NFC Unicode normalization at the shared path-validation boundary. Decomposed
spellings now fail before worker LLM, contract authorization, audit, or
filesystem effects, matching the existing file-tool path contract. Two focused
checks and the 868-test provider-free hardening suite passed.

On 2026-07-23, ThreadKeeper commit `3bd18da` on
`agent/threadkeeper-hardening-next` rejected path components whose NFKC
compatibility form becomes a canonical Windows device name, including
fullwidth and subscript-digit aliases such as `ＣＯＮ.txt`, `ＣＯＭ１.log`,
and `ＬＰＴ₉.txt`. These spellings now fail before worker LLM, audit,
task-contract authorization, or filesystem effects. Forty-four focused checks
and the 867-test provider-free hardening suite passed.

On 2026-07-23, a provider-free admission contract preregistered the minimum
consumer diversity needed to call a motivational candidate-registry hash
portable evidence. Two content-addressed consumers differ in language,
runtime, JSON library, and implementation path, import no admitted peer, and
reproduce the exact hash. Ten checks pass; candidate-only, adjudication
required, ThreadKeeper effect `none`.

On 2026-07-23, ThreadKeeper commit `3f2280a` on
`agent/threadkeeper-hardening-next` rejected Unicode compatibility forms that
NFKC-normalize into `:`, `<`, `>`, `"`, `|`, `?`, or `*` in file-tool and
task-contract paths. Fullwidth and small-form punctuation can no longer bypass
alternate-stream and Windows-forbidden filename checks under one audited
spelling and later normalize into forbidden syntax. Thirty-six focused checks
and the 864-test provider-free hardening suite passed.

On 2026-07-23, ThreadKeeper commit `6a26286` on
`agent/threadkeeper-hardening-next` rejected Unicode compatibility characters
whose NFKC form contains ASCII dots, including U+2024, U+2025, U+2026, U+FE52,
and U+FF0E, in file-tool and task-contract paths. These characters can no
longer bypass audited traversal, extension, or Windows device-name spellings
and later normalize to ASCII dots. Twenty focused checks and the 828-test
provider-free hardening suite passed.

On 2026-07-23, a separately implemented Perl/JSON::PP canonicalizer
reproduced the admitted motivational candidate-set SHA-256 from both
byte-distinct registry fixtures. Semantic mutation, action-authority widening,
and unknown fields fail closed in five provider-free checks. This is
candidate-only evidence; ThreadKeeper effect remains `none`.

On 2026-07-23, ThreadKeeper commit `1a4f68d` on
`agent/threadkeeper-hardening-next` rejected Unicode separator lookalikes
U+2044, U+2215, U+29F8, and U+29F9 in file-tool and task-contract paths
before worker LLM, audit, contract authorization, or filesystem effects.
Sixteen focused checks and the 795-test provider-free hardening suite passed.

On 2026-07-23, ThreadKeeper commit `2f749e3` on
`agent/threadkeeper-hardening-next` rejected Unicode separator compatibility
characters U+FE68, U+FF0F, and U+FF3C in file-tool and task-contract paths
before worker LLM, audit, contract authorization, or filesystem effects.
Twelve focused checks and the 792-test provider-free hardening suite passed.

On 2026-07-23, two independently serialized motivational candidate registries
converged to the already admitted candidate-set SHA-256 under a strict
provider-free canonicalizer. Five checks cover convergence plus fail-closed
semantic mutation, action-authority widening, unknown fields, and candidate
reordering. This is candidate-only evidence; ThreadKeeper effect remains
`none`.

On 2026-07-23, ThreadKeeper commit `f8e9691` on
`agent/threadkeeper-hardening-next` completed variation-selector path
validation by rejecting Mongolian free variation selectors U+180B--U+180D and
U+180F in file-tool and task-contract paths. Twenty-eight focused checks and
the 767-test provider-free hardening suite passed.

On 2026-07-23, ThreadKeeper commit `f9f04e0` on
`agent/threadkeeper-hardening-next` rejected Unicode variation selectors in
file-tool and task-contract paths before worker LLM, audit, or filesystem
effects. Twelve focused checks and the 751-test provider-free hardening suite
passed.

On 2026-07-23, ThreadKeeper commit `a8d0311` on
`agent/threadkeeper-hardening-next` rejected file-tool and task-contract path
components exceeding 255 UTF-8 bytes before worker LLM, audit, or filesystem
effects. Four focused checks and the 752-test provider-free hardening gate
passed.

On 2026-07-23, ThreadKeeper commit `638618b` on
`agent/threadkeeper-hardening-next` rejected Windows-forbidden filename
characters (`<`, `>`, `"`, `|`, `?`, `*`) in file-tool and task-contract paths
before worker LLM, audit, or filesystem effects. Twenty-four focused checks and
the 748-test provider-free hardening gate passed.

On 2026-07-23, ThreadKeeper commit `31e3cdd` on
`agent/threadkeeper-hardening-next` rejected invisible Unicode joiners
(U+200C/U+200D) in file-tool and task-contract paths before worker LLM, audit,
or filesystem effects. Eight focused checks and the 724-test provider-free
hardening gate passed.

On 2026-07-23, ThreadKeeper commit `4d1fd33` on
`agent/threadkeeper-hardening-next` rejected the superscript-digit Windows
device aliases `COM¹`--`COM³` and `LPT¹`--`LPT³` in file-tool and task-contract
paths before worker LLM, audit, or filesystem effects. Twenty-eight focused
checks and the 703-test provider-free hardening gate passed.

On 2026-07-23, ThreadKeeper commit `049939b` on
`agent/threadkeeper-hardening-next` rejected path components ending in dots or
spaces. This closes Windows trimming aliases such as `report.txt.` and
`safe /report.txt` before worker LLM, audit, contract authorization, or
filesystem effects. Forty focused checks and the 691-test provider-free
hardening gate passed.

On 2026-07-22, ThreadKeeper commit `2e003c3` on
`agent/threadkeeper-hardening-next` rejected Windows reserved device names in
file-tool and task-contract relative paths. Names such as `NUL`, `CON.txt`,
`COM1.log`, and `LPT9` now fail before LLM, audit, or filesystem effects.
Twenty-three focused checks and the 679-test provider-free hardening gate
passed.

On 2026-07-22, a provider-free independent consumer resumed the admitted
scale-1000 motivational checkpoint by recomputing the preregistered suffix
from the pinned source. It ignored a falsified producer resumed trace, and
checkpoint/source/policy drift failed closed. Five unit checks, compile, JSON
replay, and diff check passed. Candidate-only; no runtime behavior changed.

On 2026-07-22, ThreadKeeper commit `a0df4fc` on
`agent/threadkeeper-hardening-next` rejected colons in file-tool and task-
contract relative paths, closing Windows alternate-data-stream spellings
before LLM, audit, or filesystem effects. Seventeen focused checks and the
663-test provider-free hardening gate passed.

On 2026-07-22, ThreadKeeper commit `2204b86` on
`agent/threadkeeper-hardening-next` rejected Windows drive-qualified spellings
in file-tool and task-contract relative paths. Ten focused checks and the
661-test provider-free hardening gate passed.

On 2026-07-22, a separate provider-free consumer independently admitted the
scale-1000 motivational checkpoint after recomputing its checkpoint/source
hashes and matching pinned policy identity. Mutation, stale source identity,
and scale/margin drift fail closed. Four unit checks, compile, JSON replay, and
diff check passed. This remains candidate-only and changes no runtime behavior.

On 2026-07-22, ThreadKeeper commit `7c6b544` on
`agent/threadkeeper-hardening-next` rejected backslashes in file-tool and task-
contract relative paths. This prevents one audited spelling from meaning a
filename on POSIX but a path traversal/separator sequence on Windows. Seven
focused checks and the 659-test provider-free subagent/budget gate passed.

On 2026-07-22, ThreadKeeper commit `3ca23e7` on
`agent/threadkeeper-hardening-next` began rejecting noncanonical relative file
tool and task-contract path spellings such as `./file`, repeated separators,
dot components, and trailing separators. Twenty-six focused checks and the
652-test provider-free subagent/budget gate passed.

On 2026-07-22, a provider-free scale-1000 fixed-point gate matched the pinned
three-place decimal motivational trace across boundary cases and across a
self-hashed restart checkpoint. Four unit checks, compile, and JSON replay
passed. This remains candidate-only and changes no ThreadKeeper/runtime behavior.

On 2026-07-22, ThreadKeeper commit `8402cad` on its next hardening branch
rejected boundary whitespace and non-NFC spellings in cancellation and worker
stop-file paths before queue claims, worker locks, or LLM calls. Eight focused
checks and the 640-test provider-free gate passed.

On 2026-07-22, ThreadKeeper commit `16a7776` on its next hardening branch began requiring NFC
normalization for audited file paths, external queries, and optional-shell
commands, rejecting canonically equivalent but byte-distinct spellings before
effects. Two focused checks and the 634-test provider-free gate passed.

On 2026-07-22, a provider-free motivational quantization gate showed that
three-place round-half-even preserves preregistered below/exact/above
hysteresis decisions, while two-place rounding suppresses the
just-above-boundary switch. Five unit checks, compile, and JSON replay passed.
This remains candidate-only and does not change ThreadKeeper or runtime
behavior.

On 2026-07-22, ThreadKeeper commit `192ccd2` on
`agent/threadkeeper-hardening-next` rejected leading or trailing Unicode
whitespace in external-query and optional-shell arguments before prompt,
provider, subprocess, or audit use. Twenty-eight focused boundary-whitespace
checks and the 632-test provider-free subagent/budget gate passed.

On 2026-07-22, ThreadKeeper commit `e972609` on
`agent/threadkeeper-hardening-next` rejected leading or trailing Unicode
whitespace in read/write/append tool paths before audit or filesystem use.
Thirteen focused checks and the 616-test provider-free subagent/budget gate
passed.

On 2026-07-22, ThreadKeeper commit `cc1e306` on
`agent/threadkeeper-hardening-next` rejected Unicode noncharacters in tool
path, query, and shell arguments before filesystem, prompt, subprocess, or
audit use. Five focused checks and the 604-test provider-free subagent/budget
gate passed.

On 2026-07-22, ThreadKeeper commit `fd927f8` on
`agent/threadkeeper-hardening-next` made OpenAI-compatible SDK response
objects fail closed when `model_extra` contains any unknown provider field at
the response, choice, message, or usage layer, including null/falsey values.
Twenty-four focused checks and the 603-test provider-free subagent/budget gate
passed.

On 2026-07-22, ThreadKeeper commit `ed7283c` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
top-level response `metadata`, including falsey values. This closes an ignored
provider-controlled metadata channel beside admitted text. Four focused checks
and the 579-test provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `063ae25` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
top-level `error` payloads, including falsey values. A completion can no longer
carry an ignored provider error channel beside admitted text. Four focused
checks and the 575-test provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `b990113` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible usage
`prompt_tokens_details` and `completion_tokens_details`, including falsey
values. This closes ignored fine-grained accounting channels beside admitted
token totals. Eight focused checks and the 571-test provider-free
subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `f711a73` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant `parsed` payloads, including falsey values. This prevents an
unsolicited SDK structured-output channel from accompanying admitted text.
Four focused checks and the 567-test provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `de49e1c` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
top-level `prompt_filter_results` metadata, including falsey values. This
closes the prompt-side provider moderation-metadata channel beside admitted
textual content. Four focused checks and the 563-test provider-free
subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `3030a6a` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible choice
`content_filter_results` metadata, including falsey values. This closes an
ignored provider moderation-metadata channel beside admitted textual content.
Four focused checks and the 559-test provider-free subagent/budget gate passed.

On 2026-07-21, a provider-free affine-origin gate showed that common score
offsets are harmless after explicit centering: origins `0.0`, `0.05`, and
`0.10` preserve the preregistered motivational selection trace. Invalid,
missing/mismatched, and candidate-specific offsets fail closed. Five unit
checks, compile, and JSON replay passed. This binds an offline provenance
requirement only and does not change ThreadKeeper or runtime behavior.

On 2026-07-21, ThreadKeeper commit `af147ac` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible choice
`logprobs` metadata, including falsey values. This closes an ignored
token-probability output channel beside the validated textual protocol. Four
focused checks and the 555-test provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `ef2b8f4` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
`service_tier` metadata, including falsey values. This prevents unrequested
provider scheduling-class metadata from being silently ignored beside the
validated textual protocol. Four focused checks and the 551-test
provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `2c44571` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
`system_fingerprint` metadata, including falsey values. This closes another
ignored provider-response metadata channel beside the validated textual
protocol. Four focused checks and the 547-test provider-free subagent/budget
gate passed.

On 2026-07-21, ThreadKeeper commit `087b369` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant message metadata, including falsey values. This closes another
ignored provider-output channel beside the validated textual protocol. Four
focused checks and the 543-test provider-free subagent/budget gate passed.

On 2026-07-21, a provider-free score-scale gate demonstrated that the
provisional absolute motivational hysteresis margin `0.05` changes selection
behavior when otherwise identical candidate-score contributions are scaled.
Binding the margin to the declared score scale preserved the preregistered
trace at scales `1.0`, `0.5`, and `0.25`. Five unit checks, compile, and JSON
replay passed. This is candidate-only evidence: it does not freeze a
normalization contract or change ThreadKeeper/runtime behavior.

On 2026-07-21, ThreadKeeper commit `78d6224` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant message names, including falsey values. This prevents alternate
message identity metadata from accompanying content admitted to the textual
protocol. Four focused checks and the 539-test provider-free subagent/budget
gate passed.

On 2026-07-21, ThreadKeeper commit `49a8a17` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant `reasoning_content`, including falsey values. This closes an ignored
hidden-reasoning channel beside the validated textual protocol. Four focused
checks and the 535-test provider-free subagent/budget gate passed.

On 2026-07-21, ThreadKeeper commit `3beac3b` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant annotation payloads, including falsey values. This closes another
ignored provider-output channel beside the validated textual protocol. Four
focused checks and the 531-test provider-free subagent/budget gate passed.

On 2026-07-20, ThreadKeeper commit `1f6cb4c` on
`agent/threadkeeper-hardening-next` rejected non-null OpenAI-compatible
assistant audio payloads, including falsey values. This closes an ignored
alternate provider-output channel beside the validated textual protocol. Five
focused checks and the 532-test provider-free gate passed.

On 2026-07-20, ThreadKeeper commit `b059a8d` on
`agent/threadkeeper-hardening-next` made the native Ollama response schema fail
closed on unknown top-level fields, including null and falsey values. This
closes ignored alternate payload channels outside the validated message and
accounting fields. Eight focused checks and the 522-test provider-free gate
passed.

On 2026-07-20, ThreadKeeper commit `a450d82` on
`agent/threadkeeper-hardening-next` made the native Ollama message schema fail
closed on unknown fields, including explicit null and falsey values. This
prevents ignored alternate payload channels from accompanying validated
assistant content. Twelve focused checks and the 518-test provider-free gate
passed.

On 2026-07-20, ThreadKeeper commit `ba95d0c` on
`agent/threadkeeper-hardening-next` rejected native Ollama `message.images`
payloads. Explicit falsey and populated image fields now fail closed as
authenticated `provider_response_invalid` outcomes without retry, preventing
an ignored alternate provider payload channel. Twelve focused checks and the
514-test rate-limiter-disabled provider-free gate passed.

On 2026-07-20, ThreadKeeper commit `9865540` on
`agent/threadkeeper-hardening-next` made the native Ollama provider boundary
fail closed on unexpected nonempty `message.thinking` content. ThreadKeeper
requests `think: false`, so alternate hidden text can no longer bypass the
validated and persisted assistant-content channel. Six focused checks and the
510-test provider-free gate passed.

On 2026-07-20, the provider-free motivational replay gained a self-hashed
restart checkpoint binding exact input, state, event cursor, incumbent
candidate, and hysteresis-policy identity. Resumed and uninterrupted selection
traces and terminal states match; mutation, policy drift, and invalid incumbent
fixtures fail closed. Seven unit tests, compile, and JSON replay passed. This
remains candidate-only with no ThreadKeeper or live runtime effect.

On 2026-07-20, ThreadKeeper commit `5bb8af3` on
`agent/threadkeeper-hardening-next` made native Ollama message-role metadata
presence-sensitive. Explicit JSON null now fails closed as an authenticated
`provider_response_invalid` outcome without retry, while omission remains
compatible. The focused regression passed; the provider-free combined gate
passed 504 tests with the rate limiter disabled for deterministic replay.

On 2026-07-20, ThreadKeeper commit `16100b6` on
`agent/threadkeeper-hardening-next` made native Ollama `done_reason` metadata
presence-sensitive. Explicit JSON null now fails closed as an authenticated
`provider_response_invalid` outcome without retry, while omission remains
compatible. Four focused checks and the 503-test provider-free gate passed.

On 2026-07-20, ThreadKeeper commit `4cc9c7b` on
`agent/threadkeeper-hardening-next` made native Ollama `created_at` metadata
presence-sensitive. Explicit JSON null now fails closed as an authenticated
`provider_response_invalid` outcome without retry, while omission remains
compatible. Eleven focused checks and the 493-test provider-free gate passed.

On 2026-07-20, ThreadKeeper commit `4d04499` on
`agent/threadkeeper-hardening-next` made native Ollama model metadata
presence-sensitive. An explicitly supplied JSON null (as well as other
mismatched or malformed values) now fails closed as an authenticated
`provider_response_invalid` outcome without retry; omitted model metadata
remains compatible. Seven focused checks and the 500-test provider-free gate
passed.

On 2026-07-20, ThreadKeeper commit `8cee8c2` on
`agent/threadkeeper-hardening-next` made explicitly supplied native Ollama
`context` metadata fail closed unless it is a list of non-negative integer
token IDs. Null, scalar, mapping, boolean-containing, negative, and fractional
values now become authenticated `provider_response_invalid` outcomes without
retry; omitted context remains compatible. Ten focused checks and the 497-test
provider-free gate passed.

On 2026-07-20, ThreadKeeper commit `bcbae5e` on
`agent/threadkeeper-hardening-next` made explicitly supplied native Ollama
duration metadata fail closed unless each value is a non-negative integer.
Boolean, negative, fractional, string, and null values now become authenticated
`provider_response_invalid` outcomes without retry; omitted duration fields
remain compatible. Eight focused checks and the 479-test provider-free gate
passed.

On 2026-07-20, ThreadKeeper commit `b4bb993` on
`agent/threadkeeper-hardening-next` made explicitly supplied native Ollama
`created_at` metadata fail closed unless it is a non-empty, timezone-aware
ISO/RFC 3339 timestamp. Wrong types, empty/malformed strings, and timezone-free
timestamps now become authenticated `provider_response_invalid` outcomes
without retry; omitted timestamps remain compatible. Ten focused checks and
the 471-test provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `67f3576` on
`agent/threadkeeper-hardening-next` made explicitly supplied OpenAI-compatible
completion timestamps fail closed unless they are non-negative integer Unix
timestamps. Negative, boolean, fractional, string, list, and mapping values now
become authenticated `provider_response_invalid` outcomes without retry;
omitted timestamps remain compatible. Nine focused checks and the 469-test
provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `681d256` on
`agent/threadkeeper-hardening-next` made explicitly supplied OpenAI-compatible
response identifiers fail closed unless they are non-empty strings. Empty,
whitespace-only, boolean, numeric, list, and mapping IDs now become
authenticated `provider_response_invalid` outcomes without retry; omitted IDs
remain compatible. Eight focused checks and the 460-test provider-free
subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `f7df01a` on
`agent/threadkeeper-hardening-next` bound explicitly supplied
OpenAI-compatible response object metadata to `chat.completion`. Wrong-type,
empty, boolean, numeric, list, and mapping values now fail closed as
authenticated `provider_response_invalid` outcomes without retry; omitted
metadata remains compatible. Eight focused checks and the 457-test
provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `4e06b2d` on
`agent/threadkeeper-hardening-next` made provider-native tool-call fields
presence-sensitive. Explicit falsey `tool_calls` and deprecated
`function_call` values now fail closed as authenticated
`provider_response_invalid` outcomes without retry; omission/null remains the
only accepted no-tool signal. Eight focused checks and the 444-test
provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `5127c89` on
`agent/threadkeeper-hardening-next` bound an explicitly indexed single
OpenAI-compatible completion to choice zero. Nonzero, negative, boolean,
string, and fractional indices now fail closed as authenticated
`provider_response_invalid` outcomes without retry; omitted indices remain
compatible. Eight focused checks and the 436-test provider-free
subagent/budget gate passed.

On 2026-07-19, the provider-free disposition split report was bound to its
exact canonical synthetic input with `input_corpus_sha256`. Labels, reviewer
metadata, and record order still cannot affect assignment, while any such
input change is now visible in report provenance. Twelve unit tests, fixture
replay, compile, JSON parse, and diff checks passed. No operational evidence
was selected and no runtime authority changed.

On 2026-07-19, ThreadKeeper commit `e01fb92` on
`agent/threadkeeper-hardening-next` bound provider response messages to the
assistant role. Explicit user/system/tool, empty, boolean, and numeric roles
now fail closed as authenticated `provider_response_invalid` outcomes without
retry; omitted roles remain compatible. Twelve focused checks and the
428-test provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `0c44829` on
`agent/threadkeeper-hardening-next` bound OpenAI-compatible responses to the
requested model identity. Explicit mismatched or malformed model values now
fail closed as authenticated `provider_response_invalid` outcomes without
retry; omitted metadata remains compatible. Eight focused checks and the
416-test provider-free subagent/budget gate passed.

On 2026-07-19, the provider-free disposition-corpus split preregistration was
hardened to require its pinned input schema and canonical hexadecimal SHA-256
task provenance, and to reject duplicate task versions before deterministic
60/20/20 assignment. Eleven unit tests plus fixture replay, compile, and diff
checks passed. This remains synthetic-only and grants no operational collection
or runtime authority.

On 2026-07-19, ThreadKeeper commit `476a475` on
`agent/threadkeeper-hardening-next` bound native provider responses to the
requested model identity. Explicit missing model metadata remains compatible,
but a mismatched or malformed model value now becomes an authenticated
`provider_response_invalid` outcome without retry, preventing cross-model
routing/accounting confusion. Six focused checks and the 412-test
provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `a83f0a4` on
`agent/threadkeeper-hardening-next` rejected explicitly truncated native
provider completions. An Ollama response with `done=true` but a non-`stop`
`done_reason` now becomes an authenticated `provider_response_invalid`
outcome without retry, so partial text cannot enter the tool protocol. Eight
focused checks and the 408-test provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `b9b547c` on
`agent/threadkeeper-hardening-next` made explicit provider refusal/error
signals fail closed. Native Ollama responses carrying a non-null `error` and
OpenAI-compatible messages carrying a non-null `refusal` cannot pass
coexisting content into the textual tool protocol; both become authenticated
`provider_response_invalid` outcomes without retry. Two focused checks and
the 406-test provider-free subagent/budget gate passed.

On 2026-07-19, ThreadKeeper commit `533f671` on
`agent/threadkeeper-hardening-next` made provider completion markers mandatory.
Native Ollama responses must explicitly report `done=true`, and
OpenAI-compatible choices must explicitly report `finish_reason=stop`; missing
or null markers now fail closed as authenticated `provider_response_invalid`
outcomes without retry. Six focused checks and the 404-test provider-free
subagent/budget gate passed.

On 2026-07-19, the disposition-corpus preregistration closed a reviewer-
identity independence gap. Reviewer and adjudicator assignments must now be
distinct, nonempty scoped pseudonyms; empty, non-string, and unscoped values
fail closed. The provider-free gate passed 15 unit tests plus fixture replay,
compile, and diff checks. This grants no authority to collect operational
evidence or wire a canary.

On 2026-07-19, ThreadKeeper commit `5bfa906` on
`agent/threadkeeper-hardening-next` rejected explicitly unfinished provider
responses. Native Ollama `done=false` and OpenAI-compatible non-`stop` finish
reasons now fail closed as authenticated `provider_response_invalid` outcomes
without retry, preventing partial model text from reaching the tool protocol.
Focused checks passed 4 tests; the provider-free subagent/budget gate passed
400 tests.

On 2026-07-18, ThreadKeeper commit `a25d20d` on
`agent/threadkeeper-hardening-next` rejected deprecated provider-native
`function_call` payloads. Native Ollama and OpenAI-compatible compatibility
payloads now fail closed as authenticated `provider_response_invalid`
outcomes without retry, so they cannot bypass the existing `tool_calls`
rejection. The provider-free subagent/budget gate passed 403 tests.

On 2026-07-18, ThreadKeeper commit `99622d0` on
`agent/threadkeeper-hardening-next` rejected provider-native tool-call payloads.
Native Ollama and OpenAI-compatible tool calls now fail closed as authenticated
`provider_response_invalid` outcomes without retry; only ThreadKeeper's
validated textual tool protocol may reach execution. The provider-free
subagent/budget gate passed 396 tests.

On 2026-07-18, ThreadKeeper commit `cb5ea32` on
`agent/threadkeeper-hardening-next` made OpenAI-compatible total-token
accounting fail closed. When a provider supplies `usage.total_tokens`, it must
be a non-negative integer equal to prompt plus completion tokens; malformed or
contradictory totals become authenticated `provider_response_invalid` outcomes
without retry. The provider-free subagent/budget gate passed 394 tests.

On 2026-07-18, ThreadKeeper commit `e41d33f` on
`agent/threadkeeper-hardening-next` made OpenAI-compatible provider choice
selection fail closed. Responses must contain exactly one choice; empty or
multiple-choice responses become authenticated `provider_response_invalid`
outcomes without retry. The provider-free subagent/budget gate passed 390
tests.

On 2026-07-18, ThreadKeeper commit `45239b2` on
`agent/threadkeeper-hardening-next` made missing native-provider message
content fail closed. A native response must now explicitly contain string
`message.content`; omission becomes an authenticated
`provider_response_invalid` outcome without retry. The provider-free
subagent/budget gate passed 389 tests.

On 2026-07-18, ThreadKeeper commit `486f7e8` on
`agent/threadkeeper-hardening-next` closed a falsey-value bypass in native
provider token accounting. Explicit boolean and empty-string counters are no
longer normalized to zero; they fail closed as authenticated
`provider_response_invalid` outcomes without retry. The provider-free
subagent/budget gate passed 388 tests.

On 2026-07-18, ThreadKeeper commit `848f8a2` on
`agent/threadkeeper-hardening-next` made malformed native-provider JSON and
non-UTF-8 response bytes fail closed without retry. Deterministic bad provider
data now becomes an authenticated `provider_response_invalid` outcome rather
than consuming transport retry allowance. Five focused checks and the combined
provider-free subagent/budget gate passed 386 tests.

On 2026-07-18, the provider-free disposition-score perturbation calibration
passed 15/15 checks and 4 unit tests across 405 preregistered synthetic samples.
Four clear disposition archetypes remained fully stable; an ambiguous
stop-versus-hold case adjudicated in 72/81 perturbations and otherwise resolved
only to its nominal top action. This is offline robustness evidence only, not
operational calibration, disposition authority, or approval for a canary.

On 2026-07-18, ThreadKeeper commit `0c26daf` on
`agent/threadkeeper-hardening-next` made malformed OpenAI-compatible response
objects fail closed without retry. Empty/non-list choices and incomplete usage
objects now become authenticated `provider_response_invalid` outcomes instead
of retryable transport failures; malformed provider data cannot consume the
configured retry allowance. The provider-free subagent/budget gate passed 384
tests, and draft PR #1 safety-floor ancestry remains intact.

On 2026-07-18, ThreadKeeper commit `9b5dc2a` on
`agent/threadkeeper-hardening-next` made provider payload type validation fail
closed. Native and OpenAI-compatible responses must now carry string content
and non-negative integer token counters before entering worker protocol or
quota accounting; malformed values become authenticated
`provider_response_invalid` outcomes. The provider-free subagent/budget gate
passed 382 tests, and draft PR #1 safety-floor ancestry remains intact.

On 2026-07-18, ThreadKeeper commit `78a05b9` on
`agent/threadkeeper-hardening-next` authenticated two remaining provider-
boundary failures. Oversized native HTTP responses and impossible/missing
OpenAI-compatible clients now carry private structured control markers rather
than entering the worker protocol as ordinary model text. Oversized bytes are
never parsed or executed; the durable transcript records
`provider_response_invalid`. The provider-free subagent/budget gate passed 380
tests, and draft PR #1 safety-floor ancestry remains intact.

On 2026-07-18, ThreadKeeper commit `21b8883` on
`agent/threadkeeper-hardening-next` authenticated provider-control outcomes at
the structured-return boundary. Cancellation, rate-limit, concurrency-limit,
deadline, and retry-failure states now carry a private internal marker instead
of being inferred from worker-controlled string prefixes, so a worker cannot
forge a cancelled dispatch or transcript by emitting control-shaped text. The
combined provider-free subagent/budget gate passed 382 tests, and draft PR #1
safety-floor ancestry remains intact.

On 2026-07-18, ThreadKeeper commit `fccaac8` on
`agent/threadkeeper-hardening-next` made provider retry/backoff cancellation
responsive. A configured cancellation token is now polled during backoff and
checked before every retry, so cancellation cannot start another provider
attempt; the structured return and durable transcript record the dispatch as
`cancelled`. The combined provider-free subagent/budget gate passed 381 tests,
and draft PR #1 safety-floor ancestry remains intact.

On 2026-07-17, ThreadKeeper commit `3353e80` on
`agent/threadkeeper-hardening-next` closed a task-contract integrity gap:
`forbidden_actions` is now a closed vocabulary of actions the runtime can
actually enforce. Unknown or misspelled constraints fail before worker/provider
setup instead of persisting as ineffective safety claims. The combined
provider-free subagent/budget gate passed 379 tests; draft PR #1 safety-floor
ancestry remains intact.

On 2026-07-17, ThreadKeeper commit `3175ab4` on
`agent/threadkeeper-hardening-next` closed the remaining unsupported Markdown
fence gap. Tilde-fenced worker output now rejects the complete response before
any tool effect, including when an otherwise valid write precedes the fence.
The combined provider-free subagent/budget gate passed 372 tests; draft PR #1
safety-floor ancestry remains intact.

On 2026-07-17, the provider-free handoff-blocked disposition appraisal gate
passed 17/17 checks and 4 unit tests. Five synthetic fixtures deterministically
rank only `hold`, `request_cancel`, `fail_terminal`, or `expire` from pinned
task/checkpoint and selected-memory provenance; conflicting evidence becomes a
checksummed adjudicated `hold` with a review deadline. Provenance substitution,
stale charts, unknown actions/evidence, missing deadlines, and direct-effect
requests fail closed. ThreadKeeper state/source and `petta-memory` remained
unchanged. Evidence: `artifacts/ggb-capacity-gates/20260717-threadkeeper-disposition-appraisal/`.

On 2026-07-17, ThreadKeeper commit `79bfd4d` on
`agent/threadkeeper-hardening-next` made malformed Markdown fence envelopes
effect-free. Unclosed, nested, stray/ambiguous, and unsupported fence markers
now reject the complete worker batch before a tool call, and a final `emit`
inside an unclosed fence cannot be accepted. Well-formed fenced calls remain
compatible. The combined provider-free subagent/budget gate passed 370 tests;
the branch retains the draft PR #1 safety-floor ancestry.

On 2026-07-17, ThreadKeeper persistent-worker commit `f09c621` added the
explicit operator disposition gate for retryable tasks blocked by a missing
formal handoff. Immutable self-hashed records can hold, request cancellation,
fail terminally, or expire the exact task version while binding the manifest,
newest opaque checkpoint, actor, rationale, and evidence. They never fabricate
a handoff or enqueue work, and event-crash replay is idempotent. The combined
provider-free lifecycle/subagent/budget gate passed 375 tests. Evidence:
`experiments/20260717T210750Z-threadkeeper-operator-dispositions/`.

On 2026-07-17, ThreadKeeper persistent-worker commit `8c106b6` added a
provider-free restart-stability regression for the crash-before-handoff case.
Two repeated supervisor passes return the same `handoff_required` outcome,
leave the task `FAILED_RETRYABLE`, and cause zero enqueue effects. The combined
lifecycle/subagent/budget gate passed 370 tests. Evidence:
`experiments/20260717T193500Z-threadkeeper-handoff-restart-stability/`. This is
safety evidence, not a liveness policy: the next bounded gate is to specify
auditable operator dispositions without fabricating a handoff or silently
reusing an older checkpoint.

On 2026-07-17, ThreadKeeper persistent-worker commit `50aaaa2` extended formal
handoff enforcement to the `WAITING_INPUT` inbox-resume boundary. The newest
verified checkpoint must now be a formal handoff from the current attempt
before enqueue or receipt replay; missing handoffs and newer opaque
checkpoints leave the task waiting and cause no queue effect. The combined
provider-free lifecycle/subagent/budget gate passed 369 tests. Evidence:
`experiments/20260717T190841Z-threadkeeper-waiting-input-handoff/`. No live
queue, provider, Telegram, or ProtoMegaBot path was used.

On 2026-07-17, ThreadKeeper persistent-worker commit `35bf3b1` made formal
handoffs mandatory at explicit retry requeue boundaries. Missing handoffs or a
newer opaque checkpoint now stop before enqueue, leave the task retryable, and
surface `handoff_required`. A provider-free fixture spans three fresh Python
interpreters and reconstructs work exclusively from the verified durable
manifest/checkpoint/handoff chain and a handoff-referenced project file. The
combined lifecycle/subagent/budget gate passed 367 tests. Evidence:
`experiments/20260717T171207Z-threadkeeper-handoff-requeue-resume/`. No live
queue, provider, Telegram, or ProtoMegaBot path was used. Next is explicit
formal-handoff enforcement for the `WAITING_INPUT` inbox-resume boundary.

On 2026-07-17, ThreadKeeper persistent-worker commit `b6be4ea` incorporated a
formal handoff/resume artifact into the existing immutable checkpoint chain.
Strict `threadkeeper.persistent-worker.handoff.v1` snapshots now record role,
observed model identity, state summary, exact pickup point, constraints,
hazards, completed work, next steps, blockers, and evidence references. A
verified latest-handoff projection is bound to manifest/checkpoint/handoff
digests and exposed on resume; malformed schemas fail before checkpoint write.
The combined provider-free lifecycle/subagent/budget gate passed 364 tests.
Evidence: `experiments/20260717T154004Z-threadkeeper-formal-handoff-v1/`.
No live queue, provider, Telegram, or ProtoMegaBot path was used. Next is a
full process-death reconstruction fixture and pause/requeue emission policy.

On 2026-07-17, live ProtoMegaBot overload/spam control was hardened after the
Opus agent route repeatedly returned upstream HTTP 503. Runtime commits
`fb36d35`, `a9c0060`, and `74e46d2` now drop unaddressed bot-authored and
sibling-addressed group traffic before enqueue, keep transient provider
failures out of Telegram, place overloaded routes on a five-minute cooldown,
and permit only `openclaw/protomegabot-simple` as the automatic overload
fallback. Fable is opt-in only. Four overload-policy and eight address/ingress
tests pass; compilation and diff checks pass. The supervised worker was
restarted and has one healthy process with no MTProto bridge.

On 2026-07-17, ThreadKeeper commit `5ce53aa` on
`agent/threadkeeper-hardening-next` closed a tool-protocol ambiguity around
model reasoning markers. Unclosed, stray, or nested `<think>` envelopes now
fail before any parsed tool effect, and a final `emit` inside an unclosed
reasoning block cannot be accepted. Well-formed reasoning blocks retain their
existing behavior. Five provider-free regressions and the combined
subagent/budget gate pass 369 tests. The branch remains derived from draft PR
#1's Phase 1 safety floor.

On 2026-07-17, ThreadKeeper commit `4fa20bc` on
`agent/threadkeeper-hardening-next` made over-quota worker batches effect-free.
Per-turn and remaining dispatch/task-contract quota checks now run during
complete-batch preflight, before any earlier valid file mutation. Provider-free
regressions and the combined subagent/budget gate pass 364 tests. The branch
remains derived from draft PR #1's Phase 1 safety floor.

On 2026-07-17, ThreadKeeper commit `63a63d3` on
`agent/threadkeeper-hardening-next` extended complete-batch preflight from
argument shape/tool-name validation to authorization. A later tool outside the
dispatch subset or outside task-contract `allowed_paths` now rejects the whole
worker batch before an earlier valid write can execute. Provider-free
regressions and the combined subagent/budget gate pass 359 tests. The branch
remains derived from draft PR #1's Phase 1 safety floor.

On 2026-07-17, ThreadKeeper commit `8936cab` on
`agent/threadkeeper-hardening-next` made invented/unknown worker tools fail the
complete batch preflight. A valid write earlier in the same response can no
longer execute before a later unknown tool is rejected. Provider-free direct
and dispatch regressions pass, and the combined subagent/budget gate passes 357
tests. The branch remains derived from draft PR #1's Phase 1 safety floor.

On 2026-07-17, ThreadKeeper commit `1ef286a` on
`agent/threadkeeper-hardening-next` made malformed worker tool batches
effect-free. Every parsed call's argument shape is now preflighted before the
first tool effect, and parenthesized protocol records that the tolerant parser
would otherwise skip reject the entire turn. Provider-free regressions prove
that neither an earlier valid write nor a later malformed write reaches the
filesystem; the combined subagent/budget gate passes 355 tests. The branch
remains derived from draft PR #1's Phase 1 safety floor.

On 2026-07-16, ThreadKeeper commit `5342db5` on
`agent/threadkeeper-hardening-next` closed a persistent-evidence gap left after
strict surrogate argument rejection: lone surrogates in untrusted worker
responses/tool results are now rendered as visible literal escapes before they
can reach the next provider prompt, structured parent return, or UTF-8
transcript/checksum write. A provider-free two-turn regression proves the
malformed file payload causes no filesystem effect while the recovered run and
complete evidence persist. The combined subagent/budget gate passes 353 tests.
The branch remains derived from draft PR #1's Phase 1 safety floor.

On 2026-07-16, strict ThreadKeeper tool-argument validation commit `31e2ebf`
on `agent/threadkeeper-hardening-next` closed the remaining file-payload Unicode
encoding edge: `write-file` and `append-file` now reject surrogate code points
before tool, audit, or filesystem effects while retaining their intentional
multiline-content support. The combined provider-free subagent/budget gate
passes 352 tests. The branch remains derived from draft PR #1's Phase 1 safety
floor and does not duplicate it.

On 2026-07-16, bounded synchronous ThreadKeeper hardening commit `4b4524a` on
`agent/threadkeeper-hardening-next` closed a dispatch-timeout gap: provider
timeouts and retry backoff are now bounded by the remaining dispatch deadline,
no new retry starts after expiry, and results arriving after the wall-clock
limit are rejected with a persistent `dispatch_timeout` record. The combined
provider-free subagent/budget gate passes 350 tests. This branch remains based
on the draft PR #1 safety-floor ancestry and does not duplicate Phase 1.

On 2026-07-15, Ben expanded ThreadKeeper's mandate to make asynchronous
persistent workers a native delegation mode while preserving synchronous
bounded `delegate`. Work is isolated in
`worktrees/threadkeeper-persistent-workers` on branch
`agent/threadkeeper-persistent-workers`. Commit `7aa49e1` records the
behavioral/ontology/threat-model specification, a single-authority MeTTa
lifecycle policy, a fail-closed Python parity contract, and exhaustive
provider-free truth-table tests. The corrected gate passed 5 unit tests, 10
focused regression tests, Python compilation, `git diff --check`, and PeTTa/SWI
compilation; see experiments
`20260715T144937Z-threadkeeper-persistent-lifecycle-petta-parse` (preserved
invalidated semantic finding) and
`20260715T145130Z-threadkeeper-persistent-lifecycle-v1-fixed` (passing). No
worker, provider, Telegram, credential, ProtoMegaBot process, or production
path was used. Subsequent commits now provide durable manifests/events/status
(`f82d168`), idempotent spawn/cancel (`aa33f7a`), and immutable attempt leases,
bounded hash-linked checkpoints, and fail-closed stale-attempt recovery
recording (`43d34fe`). Commit `9727ad7` adds the separate, idempotent explicit
requeue effect: it verifies attempt/checkpoint lineage, recreates only the
bounded queue record, and CAS-records its digest without claiming work. The
Commit `1b2d670` binds the latest verified checkpoint ID/digest into the
new immutable attempt and passes its structured payload to the queued runner as
bounded resume context. Commit `29948e9` closes the enqueue/event crash window
with bounded immutable manifest-bound receipts for spawn and explicit requeue;
retries reuse a verified receipt instead of repeating the queue effect. The
combined provider-free/focused gate passed 340 tests. Commit `4b7399e` now adds
a bounded hash-linked task-level usage ledger, strict positive
budget schemas, verified aggregate status, and pre-claim/requeue exhaustion
gates; the combined gate passes 343 tests. Commit `fed6c2a` adds bounded,
self-hashed completed-attempt result receipts and idempotent automatic token
accounting; a retry after ledger-write failure reuses the verified receipt
without repeating the queue effect. The combined provider-free/focused gate
passes 346 tests. Subsequent commits add inbox/result delivery and automatic
runtime/tool accounting from compact queue-runner counters.
Commit `66b249a` adds the first inbox slice: bounded immutable self-hashed items
eligible only against the current `WAITING_INPUT` event, with idempotent replay
and fail-closed stale-source/conflict/tamper handling. The combined focused
gate passes 349 tests.
Commit `dc8dd79` adds that explicit consumption/requeue effect: it verifies the
current waiting event and exact immutable item, writes a self-hashed receipt
binding the manifest/item/queue result before lifecycle CAS, reuses the receipt
after a crash without repeating enqueue, and passes the item as labeled
untrusted task context. The combined provider-free/focused gate passes 352
tests. Commit `bf5cf10` adds bounded immutable terminal-result deliveries keyed
to the exact terminal event and result digest, separate self-hashed parent
acknowledgements, and verified pending-delivery polling. Replays are idempotent;
stale events, substituted payloads, conflicts, and tampering fail closed. The
combined provider-free/focused gate passes 355 tests. Commit `c1f7b57` adds
compact mechanically observed attempted-tool and whole-second runtime counters
to queue-runner results and binds them with token counters in the existing
crash-retry-safe receipt/ledger path; documentation head `a756315` records the
boundary. The combined provider-free/focused gate passes 356 tests. Commits
`3673e94` and `c06725e` add bounded supervisor reconciliation and a subprocess
restart gate; `e7e997e` adds fail-closed exclusive root-scoped ownership and a
concurrent-interpreter regression. The combined gate now passes 362 tests.
ProtoMegaBot/ProtoMegaBot2 remain unwired; any canary requires separate
approval.

On 2026-07-14, the live ProtoMegaBot output/Telegram path was hardened after a
model reply was silently lost. The active design now prefers a versioned JSON
action envelope with a first-class `reply`, retains a strictly validated legacy
S-expression compatibility path, treats history/runtime feedback as untrusted
context, and fails visibly when a required reply is absent or malformed. The
Telegram adapter now records deduplication only after successful delivery,
retries remaining chunks, does not couple outbound delivery to poll health, and
requires immutable per-message routing envelopes. The coherent implementation
is local commit `a16e714` on branch
`agent/protomega-output-pipeline-hardening`; it was integrated into the existing
dirty live checkout without overwriting unrelated work and deployed under the
supervisor. See `docs/protomega-output-pipeline-hardening.md` and
`docs/protomega-hardening-consultation-2026-07-14.md`.

OmegaClaw is installed enough to run locally in mock mode.

Observed on 2026-06-26:

- Cloned OmegaClaw-Core, PeTTa, and `petta_lib_chromadb`.
- Built local SWI-Prolog `9.3.36` from source because `swipl` was absent and the Pop/Ubuntu apt candidate was SWI `8.4.2`, too old for this stack.
- Rebuilt SWI with PeTTa/OmegaClaw-required libraries: `janus`, `process`, `filesex`, `pcre`, `uuid`.
- Created Python venv and installed `OmegaClaw-Core/requirements.txt`; `janus-swi==1.5.2` built successfully against local SWI.
- Downloaded local embedding model `intfloat/e5-large-v2`; load-tested dimension `1024`.
- PeTTa `examples/fib.metta` smoke test passed.
- OmegaClaw mock startup/loop smoke passed using `projects/omegaclaw/local/run-omegaclaw-mock.sh`; expected timeout exit `124` was treated as success for the continuous loop.
- OpenClaw Gateway `/v1/chat/completions` is active locally and authenticated tiny prompt returned `omega-ok`.
- Added local OmegaClaw `OpenClaw` provider and wrapper `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh`; experiment `projects/omegaclaw/experiments/20260627T063559Z-openclaw-proxy-smoke/` confirmed OmegaClaw can call OpenClaw Gateway (`HTTP/1.1 200 OK`) with mock channel and local embeddings. Timeout exit `124` remains expected for bounded continuous-loop smokes.
- Added local supervisor `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh` with `start|stop|status|log` for OpenClaw-backed mock-channel runs. It is not a Telegram integration and should stay supervised.
- Prepared private/direct Telegram path: local `channels/telegram.py` now supports `TG_ALLOWED_USER_ID(S)`, `TG_PRIVATE_ONLY`, and `TG_SKIP_INITIAL_OFFSET`; added `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`, `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`, and `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh`. Defaults allow only Telegram user/chat `402314199` and private chats. On 2026-06-27 after Benjamin messaged `@protomegabot` and got no reply, diagnosis showed the Telegram supervisor inactive/no-token first, then repeated Telegram polling DNS failures under the local Landlock policy. Root cause was `/etc/resolv.conf` symlinking into `/run/systemd/resolve`, which the policy did not allow. The local policy now grants read-only access to `/run/systemd/resolve`. The runner/validator/supervisor auto-load `/home/openclaw/.openclaw/omegaclaw-telegram.env` if present. Benjamin provided the separate OmegaClaw bot token in chat; it was saved only to the local secret env file with mode `0600`, validated via Telegram `getMe` as username `Protomegabot`, and the private Telegram supervisor was started with user/chat allowlist `402314199`. The Telegram smoke then succeeded: Benjamin reported receiving a reply from `@Protomegabot` / ProtomegaTron. The smoke supervisor was stopped afterward to avoid idle backend calls. Because the token was pasted into chat, it should be rotated in BotFather.
- On 2026-06-28, after `@Protomegabot` could not see Telegram documents posted to the shared group, upgraded the runtime adapter in `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/channels/telegram.py` so document attachments are downloaded, text-like files are inserted into the inbound prompt as untrusted attachment content, and PDFs are extracted with local `pdftotext`. Large extracted attachments are now chunked: the full extraction is saved as `.extracted.txt`, split into `.chunkNNN.txt`, and the prompt receives a first-chunk preview plus chunk paths that ProtomegaTron can inspect via `read-file`. Limits are configurable via `TG_ATTACHMENT_MAX_BYTES` and `TG_ATTACHMENT_MAX_CHARS`; default storage is `/home/openclaw/tmp/omegaclaw-telegram-attachments`. The supervised group run was restarted and verified active.
- Later on 2026-06-28, diagnosed repeated deep-call stalls after Ben asked whether `@Protomegabot` was thinking or stalling. `openclaw status` showed the fixed ProtoMegaTron Gateway `user` session had grown to about `998k/272k` tokens, while fresh/unique-user health checks returned normally. Patched `lib_llm_ext.py` to support per-call Gateway sessions because OmegaClaw already supplies its own prompt/history, to return user-visible `(send ...)` diagnostics for backend failure/timeout/empty output instead of silent `()`, and to preserve more traceback detail. Patched the Telegram runner to use per-call sessions and aligned 900s HTTP/subprocess timeouts. Patched the supervisor so nonzero runner exits no longer kill the supervisor under `set -e`. Verification: Python compile, shell syntax, failed-backend diagnostic smoke, healthy OpenClaw provider smoke, `openclaw status`, and active supervisor restart.

Immediate next step: adjudicate the private OpenClaw smoke candidate output, then consider staged Telegram-private integration with explicit stop conditions. Alternatively, run a multi-task or multi-persona supervisor smoke.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| OmegaClaw Core inspection clone | `https://github.com/asi-alliance/OmegaClaw-Core` | `projects/omegaclaw/repos/OmegaClaw-Core` | upstream default | inspect clone |
| PeTTa runtime checkout | `https://github.com/trueagi-io/PeTTa` | `projects/omegaclaw/repos/PeTTa` | upstream default | recorded by git in clone |
| OmegaClaw nested runtime checkout | `https://github.com/asi-alliance/OmegaClaw-Core` | `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core` | upstream default | recorded by git in clone |
| OpenClaw Phase 1 identity/routing implementation | `https://github.com/openclaw/openclaw` | `projects/omegaclaw/repos/OpenClaw` | `agent/chat-room-identity-phase1` | base tag `v2026.7.1` (`2d2ddc43`); local head `2e0ed9e0` |
| ChromaDB helper | `https://github.com/patham9/petta_lib_chromadb` | `projects/omegaclaw/repos/PeTTa/repos/petta_lib_chromadb` | upstream default | recorded by git in clone |

## Environments

- Local SWI-Prolog: `projects/omegaclaw/local/swipl-9.3.36`
- Python venv: `projects/omegaclaw/repos/PeTTa/.venv`
- Local Landlock policy: `projects/omegaclaw/local/policy.local.yaml`
- Local run wrapper: `projects/omegaclaw/local/run-omegaclaw-mock.sh`
- Local OpenClaw-backed smoke wrapper: `projects/omegaclaw/local/run-omegaclaw-openclaw-smoke.sh`
- Local OpenClaw-backed supervisor: `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh`
- Local private Telegram wrapper: `projects/omegaclaw/local/run-omegaclaw-openclaw-telegram-private.sh`
- Local private Telegram supervisor: `projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh`
- Local Telegram token validator: `projects/omegaclaw/local/check-omegaclaw-telegram-token.sh`
- Default local OmegaClaw Telegram secret env file: `/home/openclaw/.openclaw/omegaclaw-telegram.env`
- Local embedding cache: `projects/omegaclaw/local/huggingface`, `projects/omegaclaw/local/sentence_transformers`
- Chroma DB path: `projects/omegaclaw/repos/PeTTa/chroma_db`

See `projects/omegaclaw/RUNBOOK.md` for exact commands and environment variables.

## Key results

- PeTTa smoke result: `examples/fib.metta` reported `is 832040, should 832040. ✅`.
- SWI library import check passed for `janus`, `process`, `filesex`, `pcre`, and `uuid`.
- Python import check passed for `torch`, `chromadb`, `janus_swi`, `openai`, and `yaml`.
- OmegaClaw mock startup initialized policy, memory, local embeddings, knowledge bypass, mock channel, and loop iterations; wrapper verification passed with expected timeout.
- OpenClaw-backed OmegaClaw smoke initialized policy/local embeddings/mock channel, posted to `http://127.0.0.1:18789/v1/chat/completions`, received `200 OK`, and logged raw response `Understood — I won’t re-send or spam.` See `experiments/20260627T063559Z-openclaw-proxy-smoke/RUN.md`.
- Telegram-private scaffolding checks passed: Python syntax compile, shell syntax checks, allowlist unit check (`402314199` private allowed; group and other user ignored), start path refuses without a token, and token/env validator correctly exits `2` when no token is available.
- Token validation on 2026-06-27 succeeded for bot username `Protomegabot`; private Telegram supervisor initialized OmegaClaw with OpenClaw backend. End-to-end private Telegram smoke succeeded after fixing Landlock DNS resolver access and wrapping natural-language responses to `send` for fresh human messages. Benjamin reported receiving a reply in the `@Protomegabot` / ProtomegaTron chat. Supervisor was stopped after the smoke.

## Open questions

- For near-term local operation, OpenClaw proxy works as an LLM backend; before longer runs decide whether it should remain a full OpenClaw agent target or be replaced by a raw-model route.
- Preferred near-term topology is a separate OmegaClaw Telegram bot token/account for private/direct smoke. A token is currently stored only in the local secret env file, but because it was pasted into chat it should be rotated in BotFather before any longer run.
- On 2026-07-29, Ben explicitly withdrew the token-rotation/attestation gate
  and approved ProtoMegaBot2 staging. Staging must continue to avoid reading,
  displaying, copying, logging, or altering the existing credential; the next
  gate is the bounded staging launcher preflight and health/rollback evidence.
- How should OmegaClaw communicate with ZeroBot/OpenClaw: Telegram group, direct OpenClaw session bridge, local IPC, webhook, or no direct link initially?
- What filesystem/network policy should be used for real runs beyond the current local mock policy?

## Related projects and concepts

- `petta-chem`: separate PeTTa-native algorithmic chemistry project; overlaps in PeTTa/SWI runtime concerns but should remain distinct.
- PeTTa, MeTTa, SWI-Prolog Janus, ChromaDB, Telegram bot adapters.

## Risks

- **Credential exposure:** Telegram/API tokens must not be committed or placed in memory files.
- **Overbroad agency/channel permissions:** OmegaClaw should not be allowed to message groups or agents until auth boundaries are explicit.
- **Filesystem policy mismatch:** upstream Docker policy used `/PeTTa/...`; local path policy must be maintained if running outside Docker.
- **Infinite-loop behavior:** OmegaClaw is a continuous agent loop; run under explicit process/session management and stop smoke supervisors after tests.
- **Provider cost/unintended calls:** mock mode avoids real LLM calls; real provider use needs explicit credentials and monitoring. Current Telegram private mode still needs idle/no-input tuning before long-lived operation.
# ProtoCosmo2 full-PDF ingestion repair (2026-08-06)

The addressed-document adapter no longer silently truncates extracted text at
60,000 characters. The supplied 104-page OmegaSelf PDF (656,809 bytes) extracts
to 160,374 characters and now passes through unchanged. Input remains bounded
to 10 MB and extracted expansion to 2,000,000 characters; exceeding the latter
fails explicitly as `telegram_document_text_too_large`. Thirty-three focused
provider-free tests passed, including exact supplied-PDF preservation and the
oversize failure case, plus compilation, live config validation, and diff
checks. The test is committed at `b2069d6`; the supervised worker restarted as
PID `1553729`. Relevant Research Rules: 1 (validate extraction), 2 (explicit
failure semantics), 5 (reproducible evidence), and 7 (separate transport and
extraction bounds). Evidence:
`experiments/20260807T012000Z-protocosmo2-full-pdf-ingestion/`.
## 2026-08-09 — Non-blocking Protomega long/document path deployed

The production repair is complete. After isolated Protomega2 staging,
provider-free hardening, six independent frontier review rounds ending in
PASS, and an explicitly authorized guarded restart, production passed a fresh
short-message canary and a full long-document/interleaved-short trace. Source
9753 was acknowledged as 9754; short source 9755 received `PROD-SHORT-OK` as
9756 while the deferred task ran; the clean final document result arrived as
9757 replying to 9753. Production retained one owning receiver and healthy
watchdog/lock state. See
`experiments/20260808T232800Z-protomega-nonblocking-long-task/RUN.md`.
## 2026-08-14 clean-install gate correction

Clean upstream sequential/idle conversation and controlled restart pass with
zero descendants. Three-identity isolation remains open: runtime inspection
showed that `memoryDirectory` does not redirect the history file actually
opened by upstream `memory.metta`, so prior per-root runs shared disposable
runtime history. The unchanged Test mocks also lack provider fault injection,
timeouts, and addressed sessions needed for the frozen failure/concurrency
acceptance. Evidence:
`experiments/20260814T100700Z-restart-persistence/RUN.md`.

The event-native Telegram-shaped staging adapter is now pinned at local
unpushed commit `6457055`. Its 21 focused tests and eight-event actual-loop
private/group reverse-routing gate pass under injected Bot-API fixtures and
active URL/socket denial, with cursor persistence and zero descendants. This
is production-free seam evidence only; bounded faults, concrete-adapter
restart/isolation, independent phase-end review, real Telegram, and production
cutover remain open. Evidence:
`experiments/20260814T145500Z-telegram-shaped-addressed-adapter/RUN.md`.
