# 2026-07-28 - Strict local HTTP send JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`57c9ebf`, preserving the completed safety-floor ancestry. The local HTTP
`/send` request body now rejects duplicate object keys, non-standard
`NaN`/`Infinity`, invalid UTF-8, non-object roots, and non-string `message` or
`auth` values before authentication or inbound message processing.

Eleven focused checks, Python compilation, `git diff --check`, PR #1 ancestry,
and the provider-free subagent/budget/local-JSON gate (`1099 passed`, LLM
calls/minute guard disabled) passed. The first command used unavailable
`python`; the second ancestry check used the absent local branch name; and one
broad-gate invocation used an outdated budget test filename. Corrected
commands passed. No provider, live queue/runtime, local-channel message,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

# 2026-07-28 - Strict Slack API response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`123d84e`, preserving the completed safety-floor ancestry. Slack Web API
responses now reject duplicate object keys, non-standard `NaN`/`Infinity`,
invalid UTF-8, non-object roots, and non-boolean success markers before
response processing.

Seven focused checks, Python compilation, `git diff --check`, PR #1 ancestry,
and the provider-free subagent/budget/JSON hardening gate (`1095 passed`, rate
and concurrency guards disabled) passed. No provider, live queue/runtime,
Slack, Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred. Two initial verification
invocations used outdated test filenames; the corrected provider-free gate
passed.

# 2026-07-28 - Strict local RPC JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`80c7fa0`, preserving the completed safety-floor ancestry. Local RPC outer
envelopes and nested request/response payloads now reject duplicate object
keys and non-standard `NaN`/`Infinity` tokens before RPC dispatch or response
delivery.

Eight focused checks, Python compilation, `git diff --check`, PR #1 ancestry,
and the provider-free subagent/budget/JSON hardening gate (`1111 passed`, rate
and concurrency guards disabled) passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-28 - Strict gateway-auth response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`802fadd`, preserving the completed safety-floor ancestry. Gateway auth status
and token-verification responses now reject duplicate object keys,
non-standard `NaN`/`Infinity`, invalid UTF-8, non-object roots, and non-boolean
decision markers before authentication state or token acceptance.

Three focused checks, Python compilation, `git diff --check`, PR #1 ancestry,
and the provider-free subagent/budget/JSON hardening gate (`1103 passed`, rate
and concurrency guards disabled) passed. An initial suite invocation used the
wrong rate-limit environment key and failed against the existing persistent
ledger; the corrected documented key passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge, force-push,
or remote-ref deletion occurred.

## 2026-07-28 - Strict Agentverse search-response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`900dc51`, preserving the completed safety-floor ancestry. Agentverse/Tavily
search responses now reject duplicate object keys and non-standard
`NaN`/`Infinity` tokens before structured search-result extraction. Malformed
responses retain the existing opaque-response fallback.

Three focused checks, Python compilation, `git diff --check`, PR #1 ancestry,
and the provider-free subagent/budget/JSON hardening gate (`1100 passed`, rate
and concurrency guards disabled) passed. The first two focused invocations
exposed missing source-path and optional `uagents` test dependencies; the
provider-free test now supplies the dependency stub and passed. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-27 - Strict inline task-contract JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3779c9a`, preserving the completed safety-floor ancestry. Inline JSON goal
objects now use the shared strict decoder: duplicate object keys and
non-standard `NaN`/`Infinity` tokens fail closed as persistent
`contract_invalid` records before escalation evaluation or worker/provider
calls. Ordinary non-JSON prose goals retain their existing behavior.

Three new malformed-contract cases (seven focused strict-JSON checks total),
Python compilation, `git diff --check`, and the provider-free subagent/budget
hardening gate (`1081 passed`, rate and concurrency guards disabled) passed.
The first full-suite invocation used the wrong rate-limit environment key and
hit the existing persistent ledger; the corrected rate key exposed stale
concurrency state, and the established fully provider-free command with both
guards disabled passed. No provider, live queue/runtime, Telegram, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-27 - Independent motivational score-policy v0.2 runner

Archived
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-independent-runner/`.
The provider-free runner binds the sealed v0.2 preregistration and both
revision sources without importing the preregistration validator or any prior
runner. It recomputes `evidence_gap = 1000 - evidence_sufficiency` from the
three admitted inputs, reproduces all five witnesses, and reaches
`inspect_evidence`, `answer_current`, `request_clarification`, and
`defer_for_review`.

Eight unit checks, Python compilation, and deterministic JSON replay passed.
Negative cases cover sealed identity drift, caller-supplied derived values,
boolean/fractional inputs, formula/weight/threshold/tie-order drift,
expectation drift, candidate unreachability, admission weakening, and
authority widening. This remains candidate-only with ThreadKeeper effect
`none`; no calibration, provider, live queue/runtime, Telegram, memory write,
paid compute, secret/access/security change, push, or merge occurred.

## 2026-07-27 - Strict persisted JSON records

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`945de9e`, preserving the completed safety-floor ancestry. Persisted
control-record reads now reject duplicate object keys and non-standard
`NaN`/`Infinity` number tokens rather than accepting Python's permissive JSON
extensions or silently keeping the last duplicate. The boundary covers bounded
queued-task and candidate-transcript reads plus run-index append, rotation, and
read-only audit parsing.

Five new strict-JSON cases (seventeen focused boundary/read checks total),
Python compilation, `git diff --check`, and the provider-free subagent/budget
hardening gate (`1069 passed`, LLM calls/minute guard disabled) passed. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-26 - ThreadKeeper exact direct-dispatch scalar types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`d8254ad`, preserving the completed safety-floor ancestry. Direct dispatch
integer limits and goal, tool-subset, and persona scalar arguments now require
exact built-in types. Behavior-bearing integer and string subclasses fail
closed as persistent `dispatch_args_invalid` records before overloaded
comparison, indexing, stripping, or conversion and before persona setup or
worker/provider calls.

Five focused subclass checks (fourteen focused dispatch-boundary checks total)
and the provider-free subagent/budget hardening gate (`1039 passed`, LLM
calls/minute guard disabled) passed, along with Python compilation and
`git diff --check`. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-26 - ThreadKeeper exact supervised-worker bounds

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`bb9cd07`, preserving the completed safety-floor ancestry. Explicit
supervised-worker task, idle-poll, consecutive-error, poll-interval, and
runtime bounds now require exact built-in numeric types. Behavior-bearing
integer and float subclasses fail closed before overloaded comparison or
conversion, lock acquisition, queue claims, or worker effects.

Two focused checks, Python compilation, `git diff --check`, completed
safety-floor ancestry, and the provider-free subagent/budget hardening gate
(`1029 passed`, LLM calls/minute guard disabled) passed. No provider, live
queue/runtime, Telegram, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-26 - Closed queued-dispatch task type boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f0ed2da`, preserving the completed safety-floor ancestry. Durable queued task
records now require exact built-in container, string, numeric, list, item,
limit, and nested-contract types. Behavior-bearing subclasses fail closed
during record validation before overloaded comparison, conversion, truth,
length, or mapping behavior can run and before queue execution or worker
effects.

Six focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`1010 passed`, LLM calls/minute guard disabled)
passed. An initial suite invocation used the wrong rate-limit environment key
and failed against the existing persistent 60-call ledger; the corrected
documented key passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-26 - Closed provider total-token type

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2886862`, preserving the completed safety-floor ancestry. Authenticated
OpenAI-compatible `usage.total_tokens` now requires an exact built-in integer.
Behavior-bearing integer subclasses fail closed as a private
`provider_response_invalid` control result before overloaded comparison or
arithmetic can run.

Five focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`1013 passed`, LLM calls/minute guard disabled)
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-25 - Independent serialized motivational reachability

Archived
`artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-serialized-consumer/`.
Its sealed JSON fixture is consumed without importing producer or earlier gate
code. The independent strict consumer reproduces the pinned ordinal selection
of `defer_for_review`, verifies registry and checkpoint hashes plus exact
cursor/trace/order and candidate-only authority, and rejects duplicate JSON
members, trailing content, mutation, a rehashed early cursor, and rehashed
authority widening. Six unit tests, Python compilation, and repository diff
checks pass. No scoring-policy change, ThreadKeeper/runtime effect, provider,
network, memory write, Telegram action, paid compute, secret/access change,
push, or merge occurred.

## 2026-07-25 - Closed provider response-metadata scalar types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`e638a15`, preserving the completed safety-floor ancestry. Authenticated
OpenAI-compatible response IDs and creation timestamps now require exact
built-in strings and integers. Behavior-bearing subclasses fail closed as
private `provider_response_invalid` control results before overloaded
whitespace or comparison behavior can run.

Nineteen focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`982 passed`, LLM calls/minute guard disabled)
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-25 - Closed provider usage-counter types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`d2c8611`. Authenticated provider input/output token counters now require exact
built-in integers. Behavior-bearing integer subclasses fail closed as private
`provider_response_invalid` control results before overloaded comparison,
aggregation, logging, or transcript behavior can run.

Three focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`980 passed`, LLM calls/minute guard disabled)
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-25 - Closed direct tool-runner shapes

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`497c9c8`. The direct `run_tools()` entry point now requires exact built-in
list/tuple shapes and rejects behavior-bearing list, tuple, and string
subclasses during complete-batch preflight. An earlier valid write cannot run
when a later record contains one of these hostile shapes.

Eleven focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`982 passed`, LLM calls/minute guard disabled)
passed. The first full-suite invocation used the wrong rate-limit environment
key and hit the existing persistent 60-call ledger; the corrected documented
command passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-25 - Persistent parser-exception failures

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f8335c2`. Exceptions at the tool-response parser boundary now fail closed as a
bounded structured parent error and persistent `skill_protocol_error`
transcript, rather than escaping `dispatch()` without a run record. The
exception class is retained for diagnosis while its potentially sensitive
message is not exposed.

Seven focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`985 passed`, LLM calls/minute guard disabled)
passed. An initial full-suite command named the wrong budget-test file, and a
second used the wrong rate-limit environment key and hit the existing
persistent 60-call ledger; the corrected documented command passed. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-24 - Final emit argument-container validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3973119`. Final `emit` records now use the same list-shaped argument-container
preflight as effectful tools. A malformed scalar, tuple, mapping, or null emit
container in a mixed batch therefore rejects the whole response before an
earlier valid file/provider/subprocess effect can run.

Four focused checks, the provider-free hardening suite (`958 passed`), Python 3
compilation, and `git diff --check` passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-24 - Per-consumer motivational raw-byte preflight

Archived provider-free gate
`artifacts/ggb-capacity-gates/20260724-motivation-per-consumer-preflight/`.
The preregistered contract content-addresses the strict Python and Node.js
implementations, tests, and reports, and requires each consumer to own its
raw-byte rejection boundary. A shared validator, peer import, missing negative
case, content drift, collapsed diversity dimension, or authority widening
fails closed.

Seven admission-contract checks passed. The pinned Python and Node.js suites
also replayed successfully, retaining candidate-set SHA-256
`7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`.
This is candidate-only evidence with ThreadKeeper effect `none`; no provider,
network, Telegram, queue, memory write, runtime change, paid compute, secret
access, push, or merge occurred.

## 2026-07-24 - ThreadKeeper typed tool-call containers

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`c0e4a61`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. Worker
tool-call validation now requires string tool names and list argument
containers. This closes the boundary where a scalar string with the expected
length could pass validation as an iterable and then be unpacked into a tool
effect. Tuples, mappings, and null also fail the complete-batch preflight.

Four focused checks and the provider-free subagent/budget hardening gate
(`968 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-24 - ThreadKeeper Ogham space path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`bd58fac`, preserving both current PR #1 and
`fork/agent/threadkeeper-safety-floor` ancestry. The shared file-tool/task-
contract path validator now rejects internal U+1680 OGHAM SPACE MARK. This
visually blank `Zs` character is the only non-ASCII Unicode space that does
not NFKC-normalize to ASCII space, so it previously survived the compatibility-
space guard inside a path component.

Four focused checks and the provider-free subagent/budget hardening gate
(`965 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. An initial full-suite command named the
wrong budget test file and failed before collection; the corrected established
suite passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-24 - ThreadKeeper braille blank path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`e74bcbe`, preserving the completed safety-floor ancestry. The shared
file-tool/task-contract path validator now rejects U+2800 BRAILLE PATTERN
BLANK. This visually empty symbol is neither a Unicode format character nor a
compatibility space, so it could previously distinguish filesystem paths while
remaining hidden in prompts and audit records.

Thirty-six focused checks and the provider-free subagent/budget hardening gate
(`961 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation, `git diff --check`, and completed safety-floor ancestry. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-24 - ThreadKeeper Khitan filler path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f03fcf0`, preserving the completed safety-floor ancestry. The shared
file-tool/task-contract path validator now rejects U+16FE4 KHITAN SMALL SCRIPT
FILLER. This visually empty combining mark is not a Unicode format character,
so it could previously distinguish filesystem paths while remaining hidden in
prompts and audit records.

Thirty-two focused checks and the provider-free subagent/budget hardening gate
(`957 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation, `git diff --check`, and completed safety-floor ancestry. The first
focused invocation referenced a stale absent virtualenv and failed before test
collection; the system Python rerun passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge, force-push,
or remote-ref deletion occurred.

## 2026-07-24 - Independent strict-JSON motivational registry consumer

Archived provider-free gate
`artifacts/ggb-capacity-gates/20260724-motivation-strict-json-consumer/`.
An independently implemented Python stdlib consumer reproduced candidate-set
SHA-256 `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`
from both byte-distinct producer fixtures after a strict raw-JSON boundary.
It replayed and rejected all five representation-preflight negatives and
rejected duplicate members at registry, candidate, and nested-contract
depths before semantic hashing.

Ten checks, direct replay, Python compilation, and targeted diff check passed.
This is candidate-only evidence with ThreadKeeper effect `none`; adjudication
remains required. No provider/network/Telegram call, queue claim, memory
write, runtime change, secret access, paid compute, push, or merge occurred.

## 2026-07-24 - Motivational registry representation preflight

Archived provider-free gate
`artifacts/ggb-capacity-gates/20260724-motivation-representation-preflight/`.
The JavaScript semantic canonicalizer maps ordinal `-0` to the same bytes as
`0`, exposing a concrete lexical ambiguity despite an unchanged registry
digest. A schema-specific preflight now requires unsigned canonical base-10
ordinal lexemes and NFC Unicode scalar strings without control/format code
points before invoking the existing strict registry verifier.

Both byte-distinct admitted fixtures retain candidate-set SHA-256
`7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`.
Five preregistered negative fixtures (`-0`, `0e0`, `0.0`, decomposed Unicode,
and a lone surrogate) fail closed; seven checks, the prior seven-check
JavaScript holdout, direct replay, and targeted diff check passed. This is
candidate-only evidence with ThreadKeeper effect `none`; no provider,
network, Telegram, queue, memory write, runtime change, paid compute, push, or
merge occurred.

## 2026-07-24 - Unicode compatibility-space path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`934d58e`. The shared relative-path validator now rejects Unicode characters
whose NFKC compatibility form contains an ASCII space. This closes the gap
where a compatibility space inside a path component could pass the raw
trailing-space check and later normalize into a Windows trailing-space alias.
File-tool and task-contract paths fail before worker LLM, audit, contract
authorization, or filesystem effects.

Twenty-eight focused checks, Python 3 compilation, `git diff --check`, remote
PR #1 safety-floor ancestry, and the provider-free hardening suite (`896
passed`, LLM calls/minute guard disabled) passed. The first full-suite
invocation used the wrong rate-limit environment key and hit the existing
persistent 60-call ledger; the corrected documented key passed. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-24 - NFC-normalized task-contract paths

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`8403e06`. The shared relative-path validator now requires NFC Unicode
normalization, so task-contract `allowed_paths` can no longer admit a
byte-distinct decomposed spelling that the corresponding file-tool call would
later reject. The failure occurs before worker LLM, contract authorization,
audit, or filesystem effects, and the rejected contract remains represented in
the persistent structured failure record.

Two focused checks, Python 3 compilation, `git diff --check`, remote PR #1
safety-floor ancestry, and the provider-free hardening suite (`868 passed`,
LLM calls/minute guard disabled) passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-23 - Motivational registry consumer-diversity contract

Archived a provider-free admission contract at
`artifacts/ggb-capacity-gates/20260724-motivation-consumer-diversity/`.
Portable-evidence admission now requires at least two content-addressed
consumers with distinct languages, runtimes, JSON libraries, and
implementation paths. Both must reproduce the pinned candidate-set hash and
must not import another admitted consumer. Ten tests and replay pass,
including fail-closed insufficient-count, collapsed-diversity, shared-code,
digest-disagreement, authority-widening, and unknown-field cases.

This gate evaluates evidence portability only. It does not select a candidate,
claim a task, mutate memory, or authorize ThreadKeeper/runtime behavior;
adjudication remains required and ThreadKeeper effect is `none`.

## 2026-07-23 - Unicode separator-lookalike path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`1a4f68d`. File-tool paths and task-contract `allowed_paths` now reject
U+2044 FRACTION SLASH, U+2215 DIVISION SLASH, U+29F8 BIG SOLIDUS, and U+29F9
BIG REVERSE SOLIDUS before worker LLM, audit, contract authorization, or
filesystem effects. This prevents filename text from visually masquerading
as an audited path boundary even though these characters do not normalize to
ASCII separators.

Sixteen focused checks, Python 3 compilation, `git diff --check`, remote PR #1
safety-floor ancestry, and the provider-free hardening suite (`795 passed`,
LLM calls/minute guard disabled) passed. The first verification command used
the absent `python` alias and failed before collection; the corrected Python 3
checks passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-23 - UTF-8 path-component byte limit

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a8d0311`. File-tool paths and task-contract `allowed_paths` now reject any
component exceeding 255 UTF-8 bytes. This closes the gap where a multibyte
name passed the character-count cap but failed only after worker LLM, audit,
or filesystem work.

Four focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the provider-free hardening gate (`752 passed`, LLM
calls/minute guard disabled) passed. One verification command used the absent
`python` alias and another referenced the local instead of remote safety-floor
branch; corrected checks passed. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-23 - ThreadKeeper Unicode dot compatibility rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`6a26286`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool and task-contract paths now reject compatibility characters whose
NFKC form contains ASCII dots, including U+2024 ONE DOT LEADER, U+2025 TWO DOT
LEADER, U+2026 HORIZONTAL ELLIPSIS, U+FE52 SMALL FULL STOP, and U+FF0E
FULLWIDTH FULL STOP. These characters can no longer bypass audited traversal,
extension, or Windows device-name checks and later compatibility-normalize to
ASCII dots.

Twenty focused checks and the provider-free subagent/budget hardening gate
(`828 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-23 - Superscript Windows device-path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`4d1fd33`. File-tool paths and task-contract `allowed_paths` now reject
Windows' superscript-digit device aliases `COM¹`--`COM³` and `LPT¹`--`LPT³`,
including aliases with extensions, before worker LLM, audit, contract
authorization, or filesystem effects.

Twenty-eight focused checks, Python compilation, `git diff --check`, and the
provider-free hardening gate (`703 passed`, LLM calls/minute guard disabled)
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-22 - Independent fixed-point checkpoint resume

Added provider-free gate
`artifacts/ggb-capacity-gates/20260723-motivation-fixed-point-resume/`.
The independent consumer verifies the self-hashed checkpoint, pinned source,
cursor, scale, margin, and prefix, then recomputes the suffix from source
scores. A falsified producer `resumed_trace` is ignored; checkpoint mutation,
source/suffix mutation, and policy drift fail closed. Five unit checks,
Python compilation, JSON replay, and targeted diff check passed. The output
remains candidate-only and adjudication-required with ThreadKeeper effect
`none`. No provider/network, live runtime/Telegram, memory write, secret,
paid-compute, push, or merge activity occurred.

## 2026-07-22 - Windows alternate-data-stream path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a0df4fc`. File-tool paths and task-contract `allowed_paths` now reject colons,
closing Windows alternate-data-stream spellings such as `safe.txt:hidden` and
`safe.txt::$DATA` before LLM, audit, or filesystem effects while retaining one
cross-platform path contract.

Seventeen focused checks, Python 3 compilation, `git diff --check`, and the
provider-free hardening gate (`663 passed`, LLM calls/minute guard disabled)
passed. The initial focused invocation used the unavailable `python` command
and failed before collection; the established virtualenv rerun passed. No
provider, live runtime/Telegram, paid compute, secrets/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-22 - Drive-qualified relative-path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2204b86`. File-tool paths and task-contract `allowed_paths` now reject Windows
drive-qualified spellings such as `C:/secret.txt` and `c:secret.txt` before
LLM, audit, or filesystem effects, closing a POSIX/Windows interpretation gap.

Ten focused checks, Python 3 compilation, `git diff --check`, and the
provider-free hardening gate (`661 passed`, LLM calls/minute guard disabled)
passed. An initial chained check found that `python` is unavailable after the
focused tests passed; the immediate `python3` compile and full gate passed. No
provider, live runtime/Telegram, paid compute, secrets/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-22 - Cross-platform relative-path separator validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`7c6b544`. File-tool paths and task-contract `allowed_paths` now reject
backslashes before effects and require forward-slash separators. This prevents
the audited spelling from denoting an ordinary filename on POSIX but a path
separator or traversal sequence on Windows.

Seven focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the provider-free subagent/budget gate (`659
passed`, LLM calls/minute guard disabled) passed. The initial check used the
unavailable `python` command; the immediate `python3` rerun passed. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-22 - NFC-normalized audited tool arguments

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`16a7776`. File-tool paths, search/analysis queries, and optional-shell commands now require NFC
Unicode normalization before effects. This gives each audited single-line
argument one canonical spelling while leaving write/append contents free to
contain decomposed Unicode.

Two focused checks, Python compilation, `git diff --check`, and the
provider-free subagent/budget gate (`634 passed`, LLM calls/minute guard
disabled) passed. One initial combined command named a nonexistent budget-test
file and failed before collection; the corrected established gate passed. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-22 - File-tool path boundary-whitespace rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`e972609`. Read, write, and append tool paths now reject leading or trailing
ASCII and Unicode whitespace before audit or filesystem effects. This closes a
visually ambiguous filename channel while preserving internal spaces.

Thirteen focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the provider-free subagent/budget gate (`616
passed`, LLM calls/minute guard disabled) passed. No provider, live
queue/runtime, Telegram, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-22 - Unicode noncharacter tool-argument rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`cc1e306`. Tool paths, search/analysis queries, and optional shell commands now
reject Unicode's permanently reserved U+FDD0--FDEF range and plane-ending
FFFE/FFFF code points before they can reach filesystem, prompt, subprocess, or
audit boundaries. Common linguistic and emoji joiners remain accepted.

Five focused checks, Python compilation, `git diff --check`, PR #1 safety-floor
ancestry, and the provider-free subagent/budget gate (`604 passed`, LLM
calls/minute guard disabled) passed. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-22 - Unknown provider SDK-field rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`fd927f8`. OpenAI-compatible SDK/Pydantic response objects with non-empty
`model_extra` now fail closed at the response, choice, message, and usage
layers. Extras are rejected by presence even when their values are null or
falsey, closing future or provider-specific output channels that are unknown
to the installed SDK schema and therefore absent from the named-field checks.

Twenty-four focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the provider-free subagent/budget gate (`603
passed`, LLM calls/minute guard disabled) passed. An initial combined command
used a stale budget-test filename and failed before that suite was collected;
the corrected established gate passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-21 - OpenAI-compatible error-payload rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`063ae25`. OpenAI-compatible completions carrying a non-null top-level `error`
payload, including explicit falsey values, now fail closed as private
`provider_response_invalid` outcomes without retry. This closes an ignored
provider failure channel beside content admitted to the textual protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`575 passed`, LLM calls/minute guard
disabled) passed. The first combined invocation used the wrong rate-limit env
name and hit the known persistent ledger; the corrected established gate
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-21 - OpenAI-compatible system-fingerprint rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2c44571`. OpenAI-compatible responses carrying non-null `system_fingerprint`
metadata, including explicit falsey values, now fail closed as private
`provider_response_invalid` outcomes without retry. This prevents an ignored
provider-build metadata channel from accompanying content admitted to
ThreadKeeper's textual tool protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`547 passed`, LLM calls/minute guard
disabled) passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-21 - OpenAI-compatible message-metadata rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`087b369`. OpenAI-compatible assistant messages carrying non-null `metadata`,
including explicit falsey values, now fail closed as private
`provider_response_invalid` outcomes without retry. This prevents an ignored
metadata channel from accompanying content admitted to ThreadKeeper's textual
tool protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`543 passed`, LLM calls/minute guard
disabled) passed. One invocation used a stale budget-test filename and failed
before collection; a second used the wrong rate-limit environment key and hit
the persistent test ledger; the corrected established gate passed. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-20 - OpenAI-compatible audio payload rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`1f6cb4c`. OpenAI-compatible assistant messages carrying a non-null `audio`
payload now fail closed as private `provider_response_invalid` outcomes without
retry. Explicit falsey audio values are also rejected, preventing an alternate
provider-output channel from accompanying text accepted by ThreadKeeper's
validated tool protocol.

Five focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`532 passed`, rate limiter disabled) passed.
One initial combined-gate command used a mistyped budget-test filename and
failed before collection; the corrected established gate passed. No provider,
queue, Telegram, paid compute, secrets/access change, push, merge, force-push,
or remote-ref deletion occurred.

## 2026-07-20 - Native provider image-payload rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`ba95d0c`. Native Ollama responses carrying a non-null `message.images` field
now fail closed as private `provider_response_invalid` outcomes without retry.
This prevents image attachments, including explicit falsey placeholders, from
forming a silently ignored alternate provider payload channel alongside the
validated textual protocol.

Twelve focused checks and the rate-limiter-disabled provider-free gate (`514
passed`) passed, along with Python compilation and `git diff --check`. The
first combined invocation hit the known persistent rate-limit ledger and also
exposed an assertion coupled to the prior tool-call error wording; the
established provider-free rerun passed after preserving that wording. No
provider, queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-20 - Native provider disabled-thinking enforcement

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`9865540`. Native Ollama responses now fail closed when `message.thinking`
contains nonempty hidden text or a malformed non-string value despite the
request's `think: false`; omission, null, and an empty disabled-thinking marker
remain compatible. This keeps provider output on the validated and persisted
assistant-content channel.

Six focused checks and the rate-limiter-disabled provider-free gate (`510
passed`) passed, along with Python compilation, `git diff --check`, and PR #1
safety-floor ancestry. The first combined invocation used a stale recorded
budget-test filename; the corrected default invocation then hit the known
persistent rate-limit ledger (508 passed, 2 rate-limited assertions), and the
established provider-free invocation passed. No provider, queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge, force-push,
or remote-ref deletion occurred.

## 2026-07-20 - Native provider creation timestamp presence validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`4cc9c7b`. Explicit native Ollama `created_at: null` now becomes a private
`provider_response_invalid` outcome without retry; omitted metadata remains
compatible. This closes the false equivalence between absent and explicitly
malformed timestamp metadata.

Eleven focused checks and the rate-limiter-disabled provider-free gate (`493
passed`) passed, along with Python compilation, `git diff --check`, and PR #1
safety-floor ancestry. The first combined invocation hit the known persistent
test rate-limit ledger (491 passed, 2 rate-limited assertions); the established
provider-free invocation passed. No provider, queue/runtime, Telegram, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-20 - Native provider context metadata validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`8cee8c2`. Explicit native Ollama `context` metadata must now be a list of
non-negative integer token IDs. Null, scalar, mapping, boolean-containing,
negative, and fractional values become private `provider_response_invalid`
outcomes without retry; omitted context remains compatible.

Ten focused checks and the combined provider-free gate (`497 passed`) passed,
along with Python compilation, `git diff --check`, and PR #1 safety-floor
ancestry. The first combined invocation used a stale budget-test filename; a
second exposed the known persistent default rate-limit ledger, and the
established rate-limiter-disabled provider-free gate passed. No provider, live
queue/runtime, Telegram, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-19 - ThreadKeeper provider response-ID validation

Continued the draft-PR-#1-derived hardening branch with commit `681d256`.
OpenAI-compatible provider responses that explicitly supply an ID must now use
a non-empty string. Empty, whitespace-only, boolean, numeric, list, and mapping
IDs return the private `provider_response_invalid` control result without
retry, preserving usable provider correlation metadata. Omitted IDs remain
compatible.

Eight focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`460 passed`) passed. A first combined
invocation used the wrong budget-test filename and then exposed the persistent
default rate-limit ledger; the established gate was rerun with its documented
provider-free rate limiter disabled and passed. No provider, live queue/runtime,
Telegram, paid compute, secrets/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-19 - ThreadKeeper provider message-role validation

Continued the draft-PR-#1-derived hardening branch with commit `e01fb92`.
Native and OpenAI-compatible provider responses that explicitly label their
message as user, system, tool, empty, boolean, or numeric now return the private
`provider_response_invalid` control result without retry. This prevents a
misrouted non-assistant payload from entering ThreadKeeper's textual tool
protocol while retaining compatibility with providers that omit role metadata.

Twelve focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`428 passed`) passed. No provider, live
queue/runtime, Telegram, paid compute, secrets/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-19 - OpenAI-compatible response model binding

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`0c44829`. OpenAI-compatible responses that explicitly identify a model must
match the requested model; mismatched and malformed values fail closed as
private `provider_response_invalid` outcomes without retry. Omitted response
model metadata remains compatible.

Eight focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`416 passed`) passed. An initially mistyped
budget-test filename failed before collection; the corrected established gate
passed. No provider, queue, Telegram, paid compute, secrets/access change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-19 - Explicit provider completion markers

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`533f671`. Native Ollama responses now require explicit `done=true`, and
OpenAI-compatible choices require explicit `finish_reason=stop`. Missing or
null markers fail closed as private `provider_response_invalid` outcomes
without retry, preventing ambiguous or partial model text from entering the
validated textual tool protocol.

Six focused checks and the combined provider-free subagent/budget gate (`404
passed`) passed, along with Python compilation and `git diff --check`. The
initial check used unavailable `python`; rerunning with `python3` passed. No
provider, queue, Telegram, paid compute, secrets/access change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-18 - Deprecated provider function-call rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a25d20d`. Native Ollama and OpenAI-compatible responses carrying the
deprecated provider-native `function_call` field now fail closed as private
`provider_response_invalid` outcomes without consuming retry allowance. This
closes the legacy compatibility path around the existing `tool_calls`
rejection and keeps ThreadKeeper's validated textual protocol as the only tool
execution channel.

Four focused checks and the combined provider-free subagent/budget gate (`403
passed`) passed, along with Python compilation, `git diff --check`, and draft
PR #1 safety-floor ancestry. The initial check used unavailable `python`;
rerunning with `python3` passed. No provider, queue, Telegram, paid compute,
secrets/access change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-18 - Provider-native tool-call rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`99622d0`. Native Ollama and OpenAI-compatible responses carrying provider-
native tool calls now fail closed as private `provider_response_invalid`
outcomes without consuming retry allowance. This prevents a second, silently
ignored action channel from accompanying ThreadKeeper's validated textual tool
protocol.

Ten focused checks and the combined provider-free subagent/budget gate (`396
passed`) passed, along with Python compilation and `git diff --check`. The
initial check used unavailable `python`; rerunning with `python3` passed. No
provider, queue, Telegram, paid compute, secrets/access change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-18 - OpenAI-compatible total-token accounting validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`cb5ea32`. OpenAI-compatible responses that supply `usage.total_tokens` must
now provide a non-negative integer equal to `prompt_tokens +
completion_tokens`. Boolean, string, negative, or contradictory totals fail
closed as private `provider_response_invalid` outcomes and do not consume
configured retries.

Seven focused checks and the combined provider-free subagent/budget gate (`394
passed`) passed, along with Python compilation, `git diff --check`, and remote
`agent/threadkeeper-safety-floor` ancestry. No provider, queue, Telegram, paid
compute, secrets/access change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-18 - Native provider required-content validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`45239b2`. Native provider responses must now explicitly include string
`message.content`; an omitted field fails closed as a private
`provider_response_invalid` outcome and does not consume configured retries.

Five focused checks and the combined provider-free subagent/budget gate (`389
passed`) passed, along with Python compilation, `git diff --check`, and PR #1
safety-floor ancestry. Two initial check invocations used stale recorded venv
paths; the installed `pytest` runner passed. No provider, queue, Telegram, paid
compute, secrets/access change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-18 - Native provider falsey-counter validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`486f7e8`. Native provider token counters now reach strict payload validation
without falsey normalization. Explicit boolean or empty-string counters fail
closed as private `provider_response_invalid` outcomes and do not consume
configured retries; missing counters remain compatible as zero.

Three focused checks and the combined provider-free subagent/budget gate (`388
passed`) passed, along with Python compilation and `git diff --check`. The
first check invocation used unavailable `python`; rerunning with `python3`
passed. No provider, queue, Telegram, paid compute, secrets/access change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-18 - Native provider response decoding validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`848f8a2`. Native-provider response bodies now require strict UTF-8 and valid
JSON. Decode and parse failures return the private
`provider_response_invalid` control result immediately, so deterministic bad
provider data cannot consume transport retries or enter worker parsing.

Five focused provider checks and the combined provider-free subagent/budget
gate (`386 passed`) passed, along with Python compilation and `git diff
--check`. The first check invocation used unavailable `python`; rerunning with
`python3` passed. No provider, queue, Telegram, paid compute, secrets/access
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-18 - OpenAI-compatible response-schema validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`0c26daf`. OpenAI-compatible responses now require a non-empty list/tuple of
choices with a first message/content field; when usage is supplied it must
provide both token counters for the existing strict type validation. Malformed
response objects return the private `provider_response_invalid` control result
without retry, preventing deterministic bad provider data from consuming retry
quota or being misrecorded as a transport failure. Missing usage remains
compatible as zero.

Python compilation, `git diff --check`, eight focused provider checks, the
combined provider-free subagent/budget gate (`384 passed`), and PR #1
safety-floor ancestry passed. An initially mistyped budget-test filename
failed before collection; the corrected established gate passed. No live
provider, queue, Telegram, subprocess, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-18 - Disposition appraisal evidence-binding hardening

Closed a provenance gap in the provider-free disposition appraisal artifact:
the snapshot previously admitted evidence IDs without binding packet content.
It now carries an exact digest for every admitted packet and rejects changed
strength, confidence, temporal relevance, supported action, provenance, or
proof under the unchanged snapshot. The refreshed gate passes 18/18 checks and
5 unit tests, including an explicit proof-substitution regression. No live
runtime, state, memory, queue, provider, or Telegram effect occurred.

## 2026-07-17 - Provider-free disposition appraisal gate

Completed the recommendation-only gate above ThreadKeeper commit `f09c621` at
`artifacts/ggb-capacity-gates/20260717-threadkeeper-disposition-appraisal/`.
Five synthetic fixtures bind exact task version, manifest, newest opaque
checkpoint, EvidenceSnapshot/PiChart fingerprints, and selected evidence
provenance before deterministic four-action scoring. Clear cases recommend
`hold`, `request_cancel`, `fail_terminal`, or `expire`; conflicting evidence
falls back to `hold` with `needs_adjudication` and a review deadline.

The validator now passes 18/18 checks and 5 unit tests. Negative cases reject task,
manifest, or checkpoint substitution; stale charts; unselected evidence;
content-mutated evidence; unknown dispositions; missing hold deadlines; and direct effect requests.
ThreadKeeper checkout/persistent fixture and petta-memory checkout fingerprints
were unchanged. No runtime bridge, provider, queue, Telegram, memory write,
disposition/lifecycle effect, paid compute, secret/access change, or remote
operation occurred. Any canary still requires Ben's explicit decision.

## 2026-07-17 - ThreadKeeper handoff-blocked operator dispositions

Commit `f09c621` on `agent/threadkeeper-persistent-workers` closes the
operator-recovery policy gap after stable `handoff_required` detection.
`apply_handoff_blocked_disposition` now persists an immutable self-hashed
decision before any optional lifecycle event. The only actions are hold,
durable cancellation request, terminal failure, and expiry; the record binds
the exact failed-retryable version, manifest, newest opaque checkpoint, actor,
rationale, and bounded evidence references. It refuses a task that already has
a resumable formal handoff and never checkpoints, requeues, calls a provider,
or runs tools. A crash between record and event is replay-safe.

Checks: Python compilation; lifecycle pytest (`62 passed`); combined
provider-free lifecycle/subagent/budget pytest (`375 passed`); `git diff
--check`. Evidence:
`experiments/20260717T210750Z-threadkeeper-operator-dispositions/`. No live
queue/provider/Telegram/ProtoMegaBot path, paid compute, access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-17 - ThreadKeeper mandatory requeue handoff and process reconstruction

Commit `35bf3b1` on `agent/threadkeeper-persistent-workers` closes the retry
continuity gap left by the first formal-handoff slice. Explicit retry requeue
now requires the newest verified checkpoint to contain a strict formal
handoff; an empty chain or newer generic checkpoint fails before enqueue. The
supervisor reports `handoff_required` and retains `FAILED_RETRYABLE` for
operator repair rather than losing the task or guessing from opaque state.

A provider-free fixture uses separate interpreters for initial work/process
exit, stale recovery/requeue, and resume. The resumed process has no inherited
memory and reconstructs its result from the verified manifest and handoff plus
the handoff-referenced `project/state.txt`. Python compilation, 54 lifecycle
tests, the combined lifecycle/subagent/budget gate (`367 passed`), PR #1
ancestry, and `git diff --check` passed. Evidence:
`experiments/20260717T171207Z-threadkeeper-handoff-requeue-resume/`. No live
provider/queue/Telegram/ProtoMegaBot path, paid compute, access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-17 - ProtoMegaBot 503 spam incident

- **Observed:** `openclaw/protomegabot-opus` repeatedly returned HTTP 503 with
  `upstream provider overloaded`; `openclaw/protomegabot-simple` and
  `openclaw/default` returned HTTP 200.
- **Observed:** ProtoCosmoBot status/tool traffic entered the OmegaClaw queue.
  The old context-only policy still ran triage, and its later skip state was not
  reliable at provider time.
- **Implemented:** `fb36d35` adds quiet overload classification, cooldown, one
  inexpensive fallback, and bounded nontransient notices; `a9c0060` moves
  sibling-addressed rejection to ingress; `74e46d2` also rejects unaddressed
  bot-authored traffic before enqueue.
- **Verification:** 4/4 overload-policy tests and 8/8 address/ingress tests;
  Python compilation, launcher/supervisor shell syntax, and diff checks passed.
  Direct health check: simple/default 200, Opus 503. Restarted supervisor showed
  one worker and zero MTProto bridges.
- Existing `memory/history.metta` changes were preserved and excluded from all
  commits. No push or paid compute.

## 2026-07-17 - ThreadKeeper unknown-tool batch preflight

Continued the draft-PR-#1-derived bounded ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next` with commit `8936cab`. Unknown or invented
worker tool names previously bypassed argument-schema preflight, allowing an
earlier valid mutation in the same parsed batch to execute before the unknown
call was rejected. Unknown names now return `SKILL_ARG_ERROR` during the
complete-batch preflight, before any tool effect.

Provider-free direct and two-turn dispatch regressions prove that an earlier
valid `write-file` remains effect-free and the rejection is retained in the
persistent transcript. Four focused tests, the combined subagent/budget gate
(`357 passed`), Python compilation, and `git diff --check` passed. No provider,
live queue/runtime, Telegram, paid compute, credential/access/security change,
push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-17 - ThreadKeeper malformed tool-batch preflight

Continued the draft-PR-#1-derived bounded ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next` with commit `1ef286a`. Previously,
`run_tools` validated arguments immediately before each individual call, so an
earlier valid mutation could occur before a later malformed call was rejected.
Also, the tolerant response parser could silently skip a malformed
parenthesized record while retaining earlier valid calls. Tool argument shapes
are now preflighted as a complete batch before the first effect, and every
line-leading parenthesized protocol record must map to a parsed call before the
batch is executed. Ordinary non-protocol prose remains recoverable.

Two provider-free regressions prove that both a parsed bad-arity second write
and a skipped unterminated second write prevent the first valid write from
reaching the filesystem; the latter run recovers on a second turn and retains
the protocol error in its transcript. Python compilation, `git diff --check`,
PR #1 ancestry, three focused tests, and the combined subagent/budget gate
passed (`355 passed`). No provider, live queue/runtime, Telegram, subprocess,
paid compute, credential/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper malformed-response evidence persistence

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`5342db5`. Strict tool validation already prevented lone-surrogate file payloads
from reaching filesystem effects, but the rejected raw worker response could
still cross two unsafe UTF-8 boundaries: bounded history could place it in the
next provider prompt, and `ensure_ascii=False` transcript serialization could
fail and lose the durable record. Worker responses, parsed call evidence, tool
results, final records, and parent payloads now preserve lone surrogates as
visible literal `\udxxx` escapes before those boundaries.

The provider-free regression drives a malformed `write-file` turn followed by
a valid recovery emit. It verifies no output file exists, the second prompt
contains only the visible escape, and the checksummed transcript persists the
argument rejection without `record_write_error`. Python compilation,
`git diff --check`, PR #1 safety-floor ancestry, and the combined focused
subagent/budget suite passed (`353 passed`). No provider, queue, subprocess,
Telegram, paid compute, secret/access change, push, merge, force-push, or remote
ref deletion occurred.

## 2026-07-17 - ProtoMegaBot2 persistent canary contract (offline only)

Completed the roadmap's next artifact-only gate at
`artifacts/ggb-capacity-gates/20260717-protomegabot2-persistent-canary-contract/`.
The draft manifest pins isolated artifact-local workspace/run roots,
ThreadKeeper source `e7e997e`, a fake loopback-only provider with no credential
variable, zero Telegram/egress, one synthetic task, zero tool calls, bounded
attempts/turns/tokens/runtime, cancel/stop paths, expected evidence, rollback,
and forbidden production roots. The validator imports no runtime code and
performs no effects.

Contract validation, Python compilation, six focused positive/fail-closed
tests, fixture validation, and `git diff --check` pass. Launch preflight exits
2 as intended because approval, approver identity, and scope are absent. No
supervisor/provider/queue/Telegram/ProtoMegaBot process, secret, memory write,
paid compute, runtime-tree edit, push, or merge occurred. The next step is a
Ben decision on exact canary scope and stop conditions, not an automatic run.

## 2026-07-16 - ThreadKeeper surrogate tool-payload validation

Continued strict tool-boundary validation on the draft-PR-#1-derived
`agent/threadkeeper-hardening-next` branch and committed `31e2ebf`. All tool
arguments now reject Unicode surrogate code points before provider,
subprocess, audit, or filesystem effects. This specifically closes the
remaining `write-file` / `append-file` content gap: multiline file content
remains supported, but non-UTF-8-encodable Python surrogate values fail as
`SKILL_ARG_ERROR` before the registered file tool is called. Two focused
regressions prove zero tool effects for write and append.

Checks: PR #1 safety-floor ancestry; Python compilation; focused argument
pytest (`5 passed`); combined provider-free subagent/budget pytest (`352
passed`); `git diff --check`. No provider, live queue, Telegram, runtime
wiring, paid compute, secrets/access/security change, push, merge, force-push,
or remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper persona-config control-text validation

Continued strict configuration/tool-boundary validation on the PR #1-derived
`agent/threadkeeper-hardening-next` branch and pushed commit `4528c41`.
Required persona scalars and optional `base_url` now reject Unicode line and
paragraph separators, bidi/invisible formatting controls, ASCII controls, and
lone surrogates before persona prompt or provider setup. Six focused fixtures
cover `persona_file`, provider, model, node role, endpoint kind, and base URL.
Python compilation, focused pytest (`11 passed`), combined subagent/budget
pytest (`331 passed`), and `git diff --check` passed. No provider, live queue,
Telegram, runtime wiring, paid compute, access/security change, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-16 - Bounded persistent-worker supervisor reconciliation

Added the first provider-free supervisor slice on isolated ThreadKeeper branch
`agent/threadkeeper-persistent-workers`, commit `3673e94`. The bounded
`supervise_persistent_once` pass integrity-checks the complete task status set
before callbacks, reconciles each task at most once, derives replay-stable IDs
from verified task versions, explicitly recovers/requeues expired attempts,
observes cancellation before queue execution, and stops before effects for
corrupt state or exhausted budgets. Four synthetic fixtures cover restart,
cancellation, corruption, and budget exhaustion; the combined lifecycle and
focused hardening gate passed 360 tests plus Python compilation and diff check.
This is an in-process reconciliation primitive, not yet the roadmap's separate
subprocess restart proof. No ProtoMegaBot/ProtoMegaBot2 wiring, provider,
Telegram, queue supervisor process, secrets/access change, paid compute, push,
or merge occurred. Evidence:
`experiments/20260716T153400Z-threadkeeper-persistent-supervisor-v1/RUN.md`.

## 2026-07-16 - ThreadKeeper terminal-result delivery acknowledgement

Implemented the next provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, pushed commit `bf5cf10`. Terminal
results can now be persisted as bounded immutable delivery records keyed to the
exact terminal lifecycle event ID and payload digest. Bounded parent polling
returns only unacknowledged deliveries and re-verifies event/result lineage;
acknowledgement writes a separate immutable, self-hashed record bound to the
delivery digest. Delivery and acknowledgement retries are idempotent, while
nonterminal/stale events, payload substitution, conflicting acknowledgement
IDs, and record tampering fail closed.

Checks: PR #1 safety-floor ancestry; Python compilation; focused delivery tests
(`3 passed`); provider-free lifecycle suite (`42 passed`); combined
lifecycle/subagent/budget gate (`355 passed`); `git diff --check`. No provider,
tool, Telegram, credential, supervisor, ProtoMegaBot process/path, paid compute,
merge, force-push, or remote-ref deletion was used. Next: mechanically observed
runtime/tool accounting, then supervisor integration.

## 2026-07-16 - ThreadKeeper crash-retry-safe inbox consumption

Implemented the next provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, pushed commit `dc8dd79`. New
`consume_inbox_item` verifies the task's current `WAITING_INPUT` event and the
exact immutable inbox item, performs the existing bounded enqueue effect, then
writes a self-hashed receipt binding the manifest, source event, item digest,
and queue digest before the `WAITING_INPUT -> QUEUED` lifecycle CAS. A retry
after lifecycle-write failure reuses the verified receipt without repeating
enqueue. Conflicting item reuse and receipt tampering fail closed. The verified
item payload is carried into the queued objective only as explicitly labeled
untrusted task context.

Checks: PR #1 safety-floor ancestry; Python compilation; focused inbox tests
(`6 passed`); provider-free lifecycle suite (`39 passed`); combined
lifecycle/subagent/budget gate (`352 passed`); `git diff --check`. No provider,
tool, Telegram, credential, supervisor, ProtoMegaBot process/path, paid compute,
merge, force-push, or remote-ref deletion was used. Next: bounded idempotent
result-delivery acknowledgement.

## 2026-07-15 - ThreadKeeper crash-retry-safe queued-attempt accounting

Implemented the next provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, commit `fed6c2a`. A completed queued
attempt now creates a bounded immutable, self-hashed result receipt before its
strict input/output/total-token counters enter the task-level ledger. If the
ledger append fails, retrying the same claim verifies and reuses the receipt
without repeating the queue effect. Usage IDs remain idempotent and bound to
the immutable attempt; inconsistent token totals, counter-schema drift,
receipt tampering, and conflicting result replays fail closed. Verified resume
checkpoint identity is preserved on receipt replay.

Checks: Python compilation; persistent lifecycle suite (`33 passed`); focused
subagent/budget regressions (`313 passed`); combined total `346 passed`;
`git diff --check`. No provider, tool, Telegram, credential, supervisor,
ProtoMegaBot process/path, paid compute, merge, force-push, or remote-ref
deletion was used. Next: idempotent inbox/result delivery, then automatic
runtime/tool accounting after the queue runner exposes those compact counters.

## 2026-07-15 - Topology approval and automation recovery

Ben accepted the staged communication topology: distinct ProtomegaTron
Telegram identity, local OpenClaw Gateway only as provider, explicit chat
allowlists, and no unrestricted direct agent-session bridge. The existing
ThreadKeeper queue/GoalChainer sidecar remains bounded, checksummed,
candidate-only, and adjudication-gated.

Replaced the disabled channel watchdog's impossible isolated `sessions_list`
design with `bin/channel-watchdog.py`, a read-only local-journal scanner that
emits only pattern/time/session identifiers and never quotes content. Five
synthetic regressions, Python compilation, live silent scan, and forced cron run
passed. Re-enabled cron `70cd9d3f-8ed4-4d86-8887-917eb919c6b9` without widening
tree-scoped session visibility.

The OmegaClaw watchdog is enabled and currently reports
`ALREADY_RUNNING pid=1544920`; the previously discussed PID `1437624` was a
valid supervisor at that earlier snapshot, not stale bookkeeping. Re-enabled
ThreadKeeper, petta-chem, and GGB workers have since completed healthy runs.

## 2026-07-15 - ThreadKeeper explicit persistent requeue effect

Implemented the next provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, local commit `9727ad7`. New
`requeue_persistent` keeps stale-attempt recovery and requeue as separate
operator effects: only `FAILED_RETRYABLE` tasks are accepted; immutable
manifest, attempt, and checkpoint lineage is verified before enqueue; the
normal bounded queue adapter must return a valid queue digest; and a
compare-and-swap `FAILED_RETRYABLE -> QUEUED` event records that digest.
Duplicate requeue IDs are idempotent. A failed enqueue leaves the task
retryable, and corrupt checkpoint payloads fail before the enqueue adapter.

Gate `artifacts/ggb-capacity-gates/20260715-threadkeeper-persistent-requeue-effect/`
passed Python compilation, `git diff --check`, and 335 combined focused tests.
No provider, tool, Telegram, credential, supervisor, ProtoMegaBot process/path,
push, merge, or paid compute was used. Remaining recovery work is checkpoint
consumption by the next attempt and an idempotent receipt that closes the
enqueue-success/event-append crash window.

## 2026-07-15 - ThreadKeeper persistent-worker durable manifests, events, and status APIs

Implemented the second provider-free slice of the persistent-worker mandate
on isolated branch `agent/threadkeeper-persistent-workers` in worktree
`projects/omegaclaw/worktrees/threadkeeper-persistent-workers`, commit
`f82d168` (based on `7aa49e1` lifecycle contract).

Added three storage primitives to `src/persistent_worker.py`:

1. `create_task_manifest(root, manifest)` — atomically creates an immutable
   `tasks/<id>/manifest.json` with version tags (`MANIFEST_VERSION`,
   `LIFECYCLE_VERSION`), SHA-256 self-integrity, strict field validation, and
   `os.link`-based create-if-absent semantics. Rejects symlinks and
   non-regular files via `O_NOFOLLOW` and `lstat` checks.
2. `append_task_event(root, task_id, ...)` — appends one CAS-checked lifecycle
   event to `events.jsonl`. Enforces expected-version/prior-state
   compare-and-swap, SHA-256 hash chaining (`previous_event_sha256`), idempotent
   replay for duplicate `event_id` with matching fields, legal transition check
   via `transition_decision`, `fcntl.flock` advisory locking on POSIX, and size
   limits on individual events and total log.
3. `worker_status(root, task_id)` and `list_worker_statuses(root, limit)` —
   read-only projections that replay the event chain from the manifest,
   verifying every hash, version, and transition. Return bounded
   `status.v1` records. Fail closed on symlinks, unknown versions, tampered
   records, and oversized logs.

Updated `docs/persistent-workers.md` phased plan to reflect implemented
lifecycle/status work.

Checks: Python compile; 11 persistent-worker lifecycle/storage tests passed;
5 existing subagent hardening regression tests passed (delegate unchanged);
16 total passed, 0 failed. `git diff --check` clean. No provider, tool,
process, queue, Telegram, ProtoMegaBot, or production path touched.

## 2026-07-14 - ProtoMegaBot output and Telegram pipeline hardening

Investigated the lost Bot Philosophy reply and reproduced the failure: ambiguous
prompt syntax plus raw MeTTa-shaped history led the model to emit parenthesized
prose and valid `pin` calls without `send`; permissive repair allowed partial
execution and silently discarded the reply. Archived a GPT-5.6-sol consultation
and the adopted specification under `docs/`. Implemented the P0 hardening slice
on isolated branch `agent/protomega-output-pipeline-hardening`, commit `a16e714`,
then integrated it carefully into the existing dirty live checkout while
preserving its newer tier-routing work and unrelated local changes.

The new path prefers `omegaclaw.action.v1` JSON, strictly validates all actions
before execution, allows one formatter-only repair, visibly fails when a human
reply is missing, separates untrusted history, tracks correlation IDs, preserves
continuation routing, records Telegram dedup only after success, resumes failed
multi-chunk sends, and permits outbound sends during poll-health faults.
Validation: helper assertions and Python compile passed; `src/loop.metta` parsed
under the pinned PeTTa/SWI runtime; all 31 focused test bodies passed. Pytest's
only error was its unconditional session-cleanup attempt to invoke unavailable
Docker. The supervisor was restarted and showed clean polling/iterations without
send, poll, or traceback errors. Its stale MTProto-only readiness check was made
transport-aware and now reports the active Bot API topology as process-ready.
A human Telegram canary remains the final
end-to-end check; durable inbound journaling and persistent delivery receipts
remain follow-up work.

## 2026-07-13 - ThreadKeeper non-empty task-contract field hardening

Continued strict task-contract validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `a2c62eb` (`Reject blank task contract fields`). Blank or whitespace-only objectives and blank entries in `allowed_paths`, `forbidden_actions`, or `done_criteria` now return structured `contract_invalid` records before provider setup or worker LLM calls. String-list normalization preserves trimmed blank entries for validation instead of silently dropping malformed contract data.

Checks: PR #1 safety-floor ancestry; Python compile; focused validation pytest (`19 passed`); full focused subagent/budget hardening pytest (`310 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally left untouched because its worktree contains active unrelated runtime modifications. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

## 2026-07-13 - Goal/task contract refresh and empirical next gates

Refreshed `docs/GOAL_TASK_STATE_CONTRACT.md` to v0.2 against the archived `20260712-goalchainer-canary-review-boundary` rather than the older permissive draft. The contract now requires every queued `recommended`/`candidate` decision to remain `patch_proposal_only` and `requires_adjudication`, excludes forbidden/held/weak/blocked results before queue construction, removes any canary auto-accept path, and defines offline acceptance as evidence-only—not live egress, patch application, task claim, or memory authority. Added explicit malformed/duplicate input negatives as the next unimplemented conformance slice.

Added `GGB_NEXT_GATES.md` as the concise active frontier over the long historical roadmap: (1) artifact-only GoalChainer→ThreadKeeper adapter conformance, (2) immutable `petta-memory` evidence→appraisal replay with mutation rejection, and (3) a neutral schema over chemistry, ThreadKeeper, memory, and GoalChainer gate records. Each gate names capacities, anchors, pass criteria, and one small implementation task; live Telegram/provider/runtime and memory-write boundaries remain held. Focused GoalChainer canary policy verification passed (`python3 -m pytest -q tests/test_threadkeeper_canary_policy.py`: 3 passed). No live integration, queue claim, provider/Telegram action, memory write/promotion, secrets/access change, paid compute, push, or merge.

## 2026-07-13 - ThreadKeeper persona/task-contract object-shape hardening

Continued strict setup/task-contract validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `22a8ade` (`Reject non-object task contract configs`). Persona JSON roots and configured `task_contract` fields now must be objects. Inline nested `task_contract` values must also be objects; malformed null, boolean, numeric, array, or string values now return structured `contract_invalid` records before provider setup or worker LLM calls instead of raising during normalization or being silently ignored in favor of the outer goal object. Inline malformed values remain persisted in the transcript for audit.

Checks: PR #1 safety-floor ancestry; Python compile; focused object-shape pytest (`15 passed`); full focused subagent/budget hardening pytest (`298 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally left untouched because its worktree contains active unrelated runtime modifications and live transport work. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

## 2026-07-13 - ThreadKeeper typed task-contract objective hardening

Continued strict task-contract validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `55bf691` (`Reject typed task contract objectives`). Inline JSON task contracts now preserve the supplied `objective` type through normalization and require it to be a string during validation. Explicit null, boolean, numeric, array, and object objectives return a structured `contract_invalid` transcript before any worker LLM call instead of being silently stringified into prompt text. The failed typed value remains in the transcript for audit.

Checks: PR #1 safety-floor ancestry; Python compile; focused subagent/budget hardening pytest (`283 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally left untouched because its worktree contains active unrelated runtime modifications and untracked files. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

## 2026-07-13 - Cross-project keyword GGB fixture PeTTa runtime gate

Extended `local/check-ggb-gate-petta-runtime.py` beyond the current ThreadKeeper `gate-id`/`check` keyword shape to the independent GoalChainer+`petta-memory` real-evidence replay fixture, which uses a `gate-slug` summary and legacy unkeyed `ggb-check (name ...)` atoms. Embedded gate keys must still match the summary; unkeyed checks are scoped to the already structurally checked five-file fixture directory. Exact source atom queries passed in local PeTTa for the canonical positional fixture (4 checks), ThreadKeeper keyword fixture (6 checks), and GoalChainer+memory keyword fixture (8 checks); a copy missing `METRICS.metta` failed closed. Refreshed `artifacts/ggb-capacity-gates/20260713-ggb-keyword-petta-runtime-smoke/` and the GGB roadmap. This is cross-project representative evidence, not universal schema normalization. No live runtime/provider/Telegram/queue/memory-write activity or authority change.

## 2026-07-13 - ThreadKeeper non-empty final-return hardening

Continued structured-return validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `93d6b8f` (`Reject empty final emits`). Empty and whitespace-only `(emit ...)` values now fail closed as `EMIT_PROTOCOL_VIOLATION` before a successful parent digest can be accepted, ensuring every successful structured return has a meaningful summary. Added end-to-end transcript/status regressions and updated the subagent reference.

Checks: PR #1 safety-floor ancestry; Python compile; focused emit/protocol pytest (`14 passed`); focused subagent/budget hardening pytest (`278 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally left untouched because its worktree contains active unrelated runtime modifications and untracked files. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

## 2026-07-13 - ThreadKeeper final-emit envelope hardening

Continued strict return-protocol validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `99aebc0` (`Reject hidden text beside final emits`). `parse_calls()` remains tolerant for recoverable tool turns, but a successful final emit now requires the stripped raw response to contain exactly one non-empty ASCII-newline record. Ignored narration and malformed extra call lines beside an otherwise valid `(emit ...)` therefore fail closed as `EMIT_PROTOCOL_VIOLATION` instead of becoming a parent digest.

Checks: PR #1 safety-floor ancestry; Python compile; focused emit/protocol pytest (`12 passed`); focused subagent/budget hardening pytest (`276 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally not modified because its worktree has active unrelated runtime work. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

## 2026-07-13 - GGB keyword-shaped fixture PeTTa runtime gate

Extended `local/check-ggb-gate-petta-runtime.py` beyond the canonical positional run-contract shape to one current keyword-shaped ThreadKeeper gate. The bounded checker now extracts balanced top-level summary/check expressions, scopes checks to the summary gate ID, and asks local PeTTa to match the exact source atom shapes. Positional regression still returns `(partial true)` plus four checks; `20260713-threadkeeper-unicode-control-arg-hardening` returns status `pass` plus all six expected checks. A missing-`METRICS.metta` negative fixture fails closed. Archived `artifacts/ggb-capacity-gates/20260713-ggb-keyword-petta-runtime-smoke/` and refreshed the roadmap/mapping. This is representative simple-keyword coverage, not universal schema normalization. No live runtime/provider/Telegram/queue/memory-write activity or authority change.

## 2026-07-13 - ThreadKeeper final-emit Unicode/control hardening

Continued strict return/tool-protocol validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Committed `842792b` (`Reject unsafe Unicode in final emits`). Final `(emit ...)` values now fail closed on unsafe Unicode controls, line/paragraph separators, formatting characters, and lone surrogates before a successful parent digest is accepted. Protocol parsing now splits records only on ASCII newline so hidden Unicode separators remain inside the argument and reach validation; failed-input turn evidence is escaped visibly before transcript persistence.

Checks: PR #1 safety-floor ancestry; Python compile; focused emit/protocol pytest (`8 passed`); focused subagent/budget hardening pytest (`274 passed`); `git diff --check`. The nested OmegaClaw-Core runtime source was intentionally left untouched because that worktree contains active unrelated runtime modifications/untracked files, so runtime parity is not claimed. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, push, force-push, or remote-ref deletion.

## 2026-07-13 - GGB sibling fixture real-PeTTa runtime gate

Closed the roadmap's minimal PeTTa parser/runtime-smoke gap for the canonical positional GGB run-contract fixture. Added `local/check-ggb-gate-petta-runtime.py`: it requires the five sibling files, invokes the existing structural checker, extracts the positional `run-summary` and passed `ggb-check` labels, loads a temporary concatenated fixture in the recorded local PeTTa/SWI runtime under a 30-second timeout, and requires exact query output. The `20260701-petta-chem-run-contract` fixture returned `(partial true)` plus its four expected check labels. Archived `artifacts/ggb-capacity-gates/20260713-ggb-petta-runtime-smoke/`. Compile, source-fixture runtime query, negative missing-file fail-closed, new-gate sibling-fixture check, and `git diff --check` all passed. This is not a universal schema claim: newer keyword-shaped fixtures should be normalized separately before broad runtime-query coverage. No live runtime/provider/Telegram/queue/memory-write activity, secrets/access changes, paid compute, push, merge, or force-push.

## 2026-07-13 - ThreadKeeper Unicode run-control path gate refresh

Refreshed the existing `20260713-threadkeeper-unicode-control-arg-hardening` gate for ThreadKeeper commit `6e0e49b` (`Harden Unicode run-control paths`) on `agent/threadkeeper-hardening-next`. The shared unsafe-text guard now covers queued-dispatch paths, worker `stop_file`, and queued-task `cancel_file` paths as well as file/query/optional-shell arguments, rejecting unsafe Unicode controls/formatting and lone surrogates before queue claim or worker-lock creation. Verified PR #1 safety-floor ancestry, clean ThreadKeeper status, Python compile, focused subagent/budget hardening pytest (`268 passed`), `git diff --check`, and the six-check GGB sibling fixture. The OmegaClaw-Core runtime tree was not modified and parity is not claimed because it contains active untracked/modified runtime work. No live runtime, queue claim, provider/subprocess activity, secrets/access changes, paid compute, merge, push, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper unsafe Unicode format/surrogate argument hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `cf0db9a` (`Reject unsafe Unicode tool argument formats`) to `fork/agent/threadkeeper-hardening-next`. File paths, external query arguments, and optional-shell command strings now reject unsafe Unicode `Cf` formatting characters (including soft hyphen, word joiner, and BOM) and lone surrogate code points before filesystem, provider, or subprocess handling. U+200C/U+200D remain accepted for linguistic and emoji joining. Synced the nested OmegaClaw runtime source. Checks: PR #1 ancestry, Python compile, focused subagent/budget hardening pytest (`266 passed`), `git diff --check`, runtime source `cmp`. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper Unicode line-separator tool-argument hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `8de75d5` (`Reject Unicode line separators in tool args`) to `fork/agent/threadkeeper-hardening-next`. File paths, external query arguments, and optional-shell command strings now reject Unicode C1 controls and line/paragraph separators (`U+0085`, `U+2028`, `U+2029`) as well as ASCII controls before filesystem, provider, or subprocess handling. This closes hidden prompt/transcript/audit line-injection ambiguity left by ASCII-only validation. Synced the nested OmegaClaw runtime source. Checks: Python compile, focused subagent/budget hardening pytest (`263 passed`), `git diff --check`, runtime source `cmp`. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper unquoted file-content trailing-call hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `08e7f39` (`Reject trailing calls in unquoted file content`) to `fork/agent/threadkeeper-hardening-next`. Legacy unquoted `write-file` / `append-file` content now fails closed on spaced or compact same-line trailing calls before workspace mutation; ordinary parenthesized prose remains accepted. Synced the nested OmegaClaw runtime source. Checks: Python compile, focused subagent/budget hardening pytest (`262 passed`), `git diff --check`, runtime source `cmp`. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper unquoted trailing-call protocol hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `6a62c97` (`Reject unquoted trailing single-arg calls`) to `fork/agent/threadkeeper-hardening-next`.

Unquoted one-argument calls now reject ambiguous same-line `) (` trailing-call payloads before optional shell, external query, file-read, or final-emit handling. Ordinary unquoted parenthesized prose remains accepted. Synced `src/subagent.py` into the nested OmegaClaw runtime source. Checks: PR #1 ancestry, Python compile, focused subagent/budget hardening pytest (`260 passed`), `git diff --check`, runtime source `cmp` and compile. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper optional-shell command argument GGB gate

Archived `artifacts/ggb-capacity-gates/20260712-threadkeeper-shell-arg-hardening/` for ThreadKeeper head `76ec6b6`. The gate records the dedicated `OMEGACLAW_SUBAGENT_MAX_SHELL_ARG_CHARS` cap (default 4096), applied before optional-shell command parsing or subprocess execution while retaining the broader per-tool cap as a second ceiling. It is coordinated against PR #1 and mapped to GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Checks: PR ancestry, compile, focused hardening pytest (`256 passed`), diff check, runtime source sync, and fixture checker. No live runtime, shell subprocess, provider, or queue behavior was exercised.

## 2026-07-12 - ThreadKeeper technical-analysis argument GGB gate

Archived `artifacts/ggb-capacity-gates/20260712-threadkeeper-technical-analysis-arg-hardening/` for ThreadKeeper head `35c0c98`. The gate records the new bounded market-symbol grammar for `technical-analysis`, coordinated against PR #1 and mapped to GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Common symbols pass while prose, leading `$`/dot, control characters, and over-32-character values fail before execution. Checks: PR ancestry, compile, focused hardening pytest (`254 passed`), diff check, runtime source sync, and fixture checker. No live runtime/provider/queue behavior or authority changes.

## 2026-07-11 - ThreadKeeper append-file streaming read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `67032df` (`Bound append-file reads after open`) to `fork/agent/threadkeeper-hardening-next`.

Atomic `append-file` now reads at most the configured file-size cap plus one character from its already-open no-follow fd and rejects cap crossing before replacement. This closes the post-`fstat` growth gap where an existing workspace file could otherwise be read without a streaming bound. Added regression coverage, updated docs, and synced the nested OmegaClaw runtime source. Checks: `py_compile`; focused hardening pytest (`253 passed`); `git diff --check`; runtime source `cmp`. No paid compute, live wiring, secrets/access/security changes, queue/provider activity, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper command/query argument control-character hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `9b00e38` (`Reject control chars in subagent command args`) to `fork/agent/threadkeeper-hardening-next`.

Subagent `shell` command strings and external query tool arguments (`search`, `tavily-search`, `technical-analysis`) now reject ASCII control characters before subprocess/provider execution. File-tool paths already had this line-forging/ambiguous-name guard; this extends strict tool-argument validation to the remaining one-string execution/query tools while preserving normal whitespace-free commands and natural-language queries. Updated focused regressions and subagent reference docs; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused tool-argument pytest (`10 passed, 223 deselected`); focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`246 passed` for subagent + budget hardening tests); `git diff --check`; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-11 - ThreadKeeper symlink workspace-root hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `b25d763` (`Reject symlink subagent workspaces`) to `fork/agent/threadkeeper-hardening-next`.

Existing `OMEGACLAW_SUBAGENT_WORKSPACE` roots now fail closed unless they are real non-symlink directories before `read-file`/`write-file`/`append-file` resolution or optional allowlisted `shell` execution. Missing dedicated workspace roots remain lazily creatable for historical write-file ergonomics, but a symlinked workspace root can no longer redirect file or shell tool effects into its target. `_sanitize_error_msg()` was adjusted so workspace-root validation failures still return structured sanitized tool errors rather than escaping through the error sanitizer. Updated focused regressions and subagent reference docs; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused symlink-workspace pytest (`4 passed, 227 deselected`); focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`244 passed` for subagent + budget hardening tests); `git diff --check`; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.
# Working Notes

## 2026-07-11 - ThreadKeeper workspace/command-argument GGB gate

Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-workspace-command-arg-hardening/` for ThreadKeeper head `9b00e38`, recording the latest local-boundary/tool-argument hardening as a GGB capacity gate. The gate covers existing workspace-root symlink rejection (`b25d763`) plus optional shell and external query argument control-character rejection (`9b00e38`), mapped to capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` from `bf65398`/242-test evidence to `9b00e38`/246-test evidence.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py src/threadkeeper_budget.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py Autotests/mock/test_subagent_hardening_mock.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`246 passed`); `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper unquoted emit trailing-payload validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `bf65398` (`Reject unquoted emit trailing payloads`) to `fork/agent/threadkeeper-hardening-next`.

The final-emit protocol already rejected same-line trailing payloads after quoted emits. This patch closes the legacy unquoted counterpart: a worker response like `(emit done) (write-file "hidden.txt" "nope")` now surfaces as an `EMIT_PROTOCOL_VIOLATION` argument-count error instead of accepting the whole tail as a successful bare emit digest. Added focused regression coverage, updated subagent reference docs, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused emit/protocol pytest (`6 passed, 223 deselected`); focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`242 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper persona config scalar validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `78c43f2` (`Validate persona config scalar fields`) to `fork/agent/threadkeeper-hardening-next`.

Persona config control fields now fail closed before prompt/provider setup unless they are short non-empty strings: `persona_file`, `provider`, `model`, `api_key_env`, `node_role`, `endpoint_kind`, and optional `base_url` are capped by `OMEGACLAW_SUBAGENT_MAX_PERSONA_SCALAR_CHARS` (default 2048). `api_key_env` must be a safe env-var identifier, and optional `persona_sha256` must be a 64-character hex SHA-256. This tightens the remaining setup/config validation path before worker LLM calls. Updated focused regression tests and persona/reference docs; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`241 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper audit/accounting read-cap GGB gate

Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-audit-readcap-hardening/` for current ThreadKeeper head `bedfadb`, mapping run-index audit streaming cap enforcement (`e7ae245`), transcript audit no-path-`getsize` regular-file checks (`6a6916f`), and budget accounting/config fd-level read-cap hardening (`bedfadb`) to GGB capacities 1.3/3.2/3.5/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to current 237-test/head `bedfadb` evidence and preserved the Telegram-private blocker: active-supervisor handling plus explicit approval/stop conditions are still required before any live private smoke.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py src/threadkeeper_budget.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py Autotests/mock/test_subagent_hardening_mock.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`237 passed`); `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper budget accounting/config read-cap hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `bedfadb` (`Bound budget accounting reads after open`) to `fork/agent/threadkeeper-hardening-next`.

`src/threadkeeper_budget.py` now rechecks budget config and usage-log size on the opened file descriptor with `fstat`, then performs bounded byte reads using the existing `THREADKEEPER_MAX_BUDGET_CONFIG_BYTES` and `THREADKEEPER_MAX_BUDGET_LOG_BYTES` caps. This closes the accounting/config counterpart of the recent run-index/transcript read-cap TOCTOU hardening: a local file that grows or is swapped after the initial `lstat` can no longer turn budget checks into unbounded reads. Added focused regressions that force the initial `lstat` to under-report size, updated README, and synced `threadkeeper_budget.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/threadkeeper_budget.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`237 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper transcript audit size-check nofollow hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `6a6916f` (`Avoid path getsize in transcript audits`) to `fork/agent/threadkeeper-hardening-next`.

`verify_subagent_run_index()` no longer uses path-based `os.path.getsize()` for referenced transcript size prechecks. The audit now uses `lstat` to reject symlink/non-regular transcript records before hashing, while `_sha256_file_bounded()` still opens through the no-follow regular-file helper and enforces `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` during the streamed hash read. This closes the transcript-audit counterpart of the earlier setup/index size-check TOCTOU hardening. Added a focused regression that monkeypatches `os.path.getsize` to fail, updated subagent docs, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`235 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper budget audit-log parent hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `4034064` (`Harden budget audit log parents`) to `fork/agent/threadkeeper-hardening-next`.

`src/threadkeeper_budget.py` usage/escalation audit appends no longer use `os.makedirs(..., exist_ok=True)` for log parent creation. They now create parent directories component-by-component with `lstat` checks, reject symlink/non-directory ancestors before opening logs, fsync the log file, and best-effort fsync the parent directory. This closes the budget/accounting counterpart of the earlier subagent audit-parent symlink hardening while preserving the budget module's never-raise behavior on the agent response path. Added focused symlink-parent/ancestor regression tests, updated README, and synced `threadkeeper_budget.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/threadkeeper_budget.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`234 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper run-index audit read bounding

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `e7ae245` (`Bound run-index audit reads`) to `fork/agent/threadkeeper-hardening-next`.

`verify_subagent_run_index()` now enforces `OMEGACLAW_SUBAGENT_MAX_INDEX_AUDIT_BYTES` during the no-follow `index.jsonl` line scan, not only before opening the file. It uses the existing `lstat` size for the early oversized check and counts bytes as they are streamed, so local growth after the initial stat cannot turn a read-only run-index audit into an unbounded read. Added focused regressions proving path-based `getsize()` is no longer used for the index check and that cap crossing during the scan returns structured `index_audit_too_large`. Updated `docs/reference-skills-subagent.md` and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`231 passed` for subagent + budget hardening tests); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper task-contract path hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-task-contract-path-hardening/` for current ThreadKeeper head `558c3dc`, covering strict task-contract `allowed_paths` validation plus file-tool control-character rejection across GGB capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 230-test/head `558c3dc` evidence.

Checks: PR #1 ancestry check; source/runtime `py_compile`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`230 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, supervisor/daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper task-contract path validation hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `558c3dc` (`Harden task contract path validation`) to `fork/agent/threadkeeper-hardening-next`.

Task-contract `allowed_paths` now uses the same strict workspace-relative path validator as `read-file` / `write-file` / `append-file`: absolute paths, parent-directory traversal, oversized path strings, empty strings, and control characters fail closed during contract validation before any worker LLM call, workspace resolution, contract path check, file-tool execution, or audit record use. File-tool path validation also now rejects control characters to prevent ambiguous local filenames or transcript/audit line-forging artifacts. Updated `docs/reference-skills-subagent.md`, added focused regressions, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`230 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-10 - ThreadKeeper file-tool/guard-state GGB gate refresh

Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-file-tool-guardstate-hardening/` for current ThreadKeeper head `23ebb66`, covering file-tool relative-path validation (`23ebb66`) plus LLM guard-state parent symlink hardening (`2350afa`) across GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 225-test/head `23ebb66` evidence.

Checks: PR #1 ancestry check; source/runtime `py_compile`; focused mock pytest (`225 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, supervisor/daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper file-tool relative-path validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `23ebb66` (`Reject non-relative file tool paths`) to `fork/agent/threadkeeper-hardening-next`.

Subagent `read-file` / `write-file` / `append-file` tool-call argument validation now fails closed unless the path is workspace-relative and contains no parent-directory traversal (`..`). This tightens the strict tool-argument validation layer before workspace path resolution, contract checks, audit paths, or file-tool execution, so worker responses cannot smuggle host absolute paths or traversal syntax into local tool/audit handling. Added focused regression coverage and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`225 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper LLM guard-state parent symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `2350afa` (`Reject symlink LLM guard state parents`) to `fork/agent/threadkeeper-hardening-next`.

Per-endpoint worker LLM rate-limit and concurrency guard-state setup now validates the configured `OMEGACLAW_SUBAGENT_RUN_DIR` parent as a real non-symlink directory before creating or opening `.llm-rate-*` / `.llm-inflight-*` JSON state files. This closes the remaining parent-directory redirection gap after earlier no-follow final-file hardening for guard state: a symlinked run directory now fails closed instead of placing rate/concurrency guard artifacts under the symlink target. Added focused regression coverage and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`223 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper audit ancestor-directory symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `1cbc15b` (`Reject symlink audit ancestor directories`) to `fork/agent/threadkeeper-hardening-next`.

Shared audit/run directory creation now walks parent components with `lstat` and `mkdir` one component at a time instead of using `os.makedirs(..., exist_ok=True)`, so symlinked ancestor directories such as `run-dir/link/nested` fail closed before any nested audit/log path can be created under the symlink target. Worker usage-log setup now uses the same component-by-component validation and no longer pre-creates parent paths with `os.makedirs`. Added focused regression coverage for worker `usage.jsonl` symlink ancestors and atomic JSON audit writes through symlink ancestors; updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`221 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper append-file size-check nofollow hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `aec4c9b` (`Use nofollow fd for append size checks`) to `fork/agent/threadkeeper-hardening-next`.

`append-file` now performs existing-file size checks from the already-open regular non-symlink fd returned by `_open_workspace_file_read()` instead of a separate path-based `os.path.getsize()` call. This closes a small local TOCTOU/symlink-swap gap between workspace containment resolution, size inspection, and reading existing content; new-file appends also reject content that would exceed the file-size cap once the trailing newline is added. Added focused regression coverage and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`211 passed` for subagent hardening; `219 passed` with budget hardening); `git diff --check`; PR #1 ancestry check; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-10 - ThreadKeeper accounting/protocol hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-accounting-protocol-hardening/` for current ThreadKeeper head `25d96c8`, covering quoted-final-emit trailing-payload rejection (`33d79a5`) and worker usage-log parent hardening (`25d96c8`) across GGB capacities 1.3/3.2/3.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 218-test/head `25d96c8` evidence.

Checks: PR #1 ancestry check; source/runtime `py_compile`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`218 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, supervisor/daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper worker usage-log parent hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `25d96c8` (`Harden worker usage log parent`) to `fork/agent/threadkeeper-hardening-next`.

Worker LLM accounting appends to the shared `usage.jsonl` now validate the parent directory as a real non-symlink directory before opening the log, and best-effort fsync the parent directory after append. This closes a local symlink-parent redirection gap left after earlier final-file no-follow hardening for worker usage accounting. Added focused symlink-parent regression coverage, updated `docs/reference-skills-subagent.md`, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`218 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed it remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper quoted-emit trailing-payload validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `33d79a5` (`Reject trailing payloads after quoted emits`) to `fork/agent/threadkeeper-hardening-next`.

The tolerant single-argument parser now requires a quoted one-argument call to end at the closing quote modulo whitespace. This closes a protocol-validation gap where a same-line payload like `(emit "done") (write-file "hidden.txt" "nope")` could be parsed as one successful `emit` argument rather than a malformed final response; it now returns structured `EMIT_PROTOCOL_VIOLATION` before any final digest is accepted. Updated `docs/reference-skills-subagent.md` and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`217 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed it remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-10 - ThreadKeeper parent-directory symlink hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-parent-symlink-hardening/` to map current ThreadKeeper head `28adabf` onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. The gate covers `b567ad9` audit/run/queue parent-directory validation plus `28adabf` workspace `write-file`/`append-file` parent-directory revalidation before lock/temp-file creation and atomic replacement. Refreshed `GGB_CAPACITIES_ROADMAP.md` from stale `14d7f90`/212-test evidence to `28adabf`/216-test evidence.

Checks: PR #1 ancestry check returned exit 0 (with existing ambiguous-ref warning); source/runtime `py_compile`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`216 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, supervisor/daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper workspace write-parent symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `28adabf` (`Reject symlink workspace file parents`) to `fork/agent/threadkeeper-hardening-next`.

Workspace `write-file` and `append-file` atomic replacements now revalidate their parent path as a real non-symlink directory tree under `OMEGACLAW_SUBAGENT_WORKSPACE` immediately before creating lock/temp files. The helper creates missing workspace directories component-by-component with `lstat` checks instead of following swapped symlink ancestors, closing a remaining local TOCTOU gap where a parent directory could be replaced after `_resolve_workspace_path` containment but before `mkstemp`/lock creation. Added focused parent-swap regression tests and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`216 passed` for subagent + budget hardening tests); `git diff --check`; fetched `origin/pr-1` and confirmed it remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper audit parent-directory symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `b567ad9` (`Reject symlink audit parent directories`) to `fork/agent/threadkeeper-hardening-next`.

Atomic JSON audit writes and transcript checksum sidecar writes now validate required parent directories as real non-symlink directories before creating temp files, and queued-run/index setup paths use the same check before queue/index writes. This closes the follow-on gap where a local symlinked run/audit parent directory could redirect durable queue/transcript/index artifacts despite no-follow checks on the final file names. The async worker loop now returns structured `worker_config_invalid` if the configured run directory is unsafe before lock acquisition or queue claim. Added focused symlink-parent regression tests and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`214 passed` for subagent + budget hardening tests); `git diff --check`; fetched `origin/pr-1` and confirmed it remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper workspace file tool no-follow hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `14d7f90` (`Harden workspace file tool reads with O_NOFOLLOW`) to `fork/agent/threadkeeper-hardening-next`.

`_tool_read_file` and `_tool_append_file` previously used plain `open()` after `_resolve_workspace_path` (which uses `realpath` to resolve symlinks and check workspace containment). Added `_open_workspace_file_read(path)` helper that opens with `O_NOFOLLOW` and validates the fd is a regular non-symlink file via `fstat`, closing a TOCTOU symlink-swap gap between path resolution and the actual file read. The helper catches `ELOOP`/`EEXIST` `OSError` from `os.open` on symlink targets and converts to `ValueError` so existing tool error handling is preserved. Added 4 focused tests: direct symlink rejection by the helper, regular-file acceptance by the helper, symlink-escape rejection in `read-file` (via existing `realpath` containment), and symlink-escape rejection in `append-file` (via existing `realpath` containment). Updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`212 passed` for subagent + budget hardening tests); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper budget audit log hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `5b5c6d9` (`Harden budget audit log files`) to `fork/agent/threadkeeper-hardening-next`.

`src/threadkeeper_budget.py` now treats budget/accounting logs as local audit files: usage-log and escalation-log appends reject pre-existing symlink/non-regular targets and open through no-follow regular-file checks; usage-log reads reject symlink/non-regular sources and skip oversized logs via `THREADKEEPER_MAX_BUDGET_LOG_BYTES` (default 1 MiB). Added focused tests for symlink write rejection, symlink read rejection, and bounded usage-log reads; updated README; synced `src/threadkeeper_budget.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/threadkeeper_budget.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`204 passed` for new budget hardening plus existing subagent hardening tests); `git diff --check`; runtime budget source cmp; pushed to fork. Attempted the full `Autotests/mock` suite, but it exceeded the 300s local timeout after showing pre-existing failures, so it was not used as a pass gate. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper persona setup symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `0f0b2cc` (`Reject symlink persona setup files`) to `fork/agent/threadkeeper-hardening-next`.

Persona config JSON (`<persona_key>.json`) and persona prompt files now fail closed unless they are regular non-symlink files, and both reads use the shared no-follow regular-file opener before JSON parsing, prompt SHA-256 pinning, or prompt construction. This narrows the remaining setup-file redirection race/gap before any worker LLM call while preserving path confinement, byte caps, and sanitized errors. Added focused symlink regression tests, updated `docs/reference-skills-subagent.md`, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`200 passed`); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper no-follow audit read hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `1220907` (`Use nofollow opens for audit reads`) to `fork/agent/threadkeeper-hardening-next`.

Read-only `verify_subagent_run_index()` now opens `index.jsonl` through the shared regular non-symlink no-follow helper for the actual audit scan after its lstat/size checks, and async-worker stale-lock metadata reads now use the same no-follow helper instead of builtin `open()` after lstat. This narrows the remaining race window for local symlink replacement between validation and read while preserving existing bounded-read and fail-closed behavior. Added focused opener-regression tests, updated `docs/reference-skills-subagent.md`, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`198 passed`); runtime source compile/cmp; `git diff --check`; PR #1 ancestry check; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper worker usage accounting symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `7f3a70e` (`Harden worker usage accounting writes`) to `fork/agent/threadkeeper-hardening-next`.

Worker LLM usage accounting writes to shared `usage.jsonl` now append through the same regular non-symlink no-follow opener used for local audit/control files. This prevents a pre-existing local `usage.jsonl` symlink from redirecting worker accounting writes outside the configured memory directory while preserving best-effort/no-raise logging. Added focused tests for normal append and symlink rejection, updated `docs/reference-skills-subagent.md`, and synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`193 passed`); `git diff --check`; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-09 - ThreadKeeper transcript/guard-state hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-transcript-guard-hardening/` to map the latest ThreadKeeper audit-read and worker-LLM guard-state path hardening onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Current branch `agent/threadkeeper-hardening-next` is at `4c73526`; `origin/pr-1` remains an ancestor; nested OmegaClaw-Core runtime `subagent.py` matches the ThreadKeeper source.

This gate records `3a31e25` (per-endpoint `.llm-rate-*.json` / `.llm-inflight-*.json` guard state now opens through the regular non-symlink no-follow helper) plus `4c73526` (transcript JSON reads and transcript hashing for candidate review/run-index verification now reject symlink transcript records rather than following them). Updated `GGB_CAPACITIES_ROADMAP.md` to current 191-test/head evidence.

Checks: PR #1 ancestry check; source/runtime `py_compile`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`191 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker on the new gate. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, daemon/scheduler install, queue enqueue/claim, provider call, merge, force-push, or remote-ref deletion.


## 2026-07-09 - ThreadKeeper transcript audit symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `4c73526` (`Reject symlink transcript audit records`) to `fork/agent/threadkeeper-hardening-next`.

Transcript JSON reads used by `review_subagent_candidate()` and transcript hashing used by `verify_subagent_run_index()` now open through the shared regular non-symlink no-follow helper. `_resolve_subagent_transcript_path()` still checks realpath containment under `OMEGACLAW_SUBAGENT_RUN_DIR`, but returns the original absolute path so symlink transcript records are rejected rather than silently resolved/followed. This closes a local transcript/audit redirection gap without changing queue/worker semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`191 passed`); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper audit-path hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-audit-path-hardening/` to map the latest ThreadKeeper workspace lock and run-index tail/rotation hardening onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Current branch `agent/threadkeeper-hardening-next` is at `59140ac`; `origin/pr-1` remains an ancestor; nested OmegaClaw-Core runtime `subagent.py` matches the ThreadKeeper source.

Checks: PR #1 ancestry check; source/runtime `py_compile`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`188 passed`); ThreadKeeper `git diff --check`; runtime source `cmp`; OmegaClaw GGB fixture checker. Updated `GGB_CAPACITIES_ROADMAP.md` to current head/test evidence. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, daemon/scheduler install, queue enqueue/claim, provider call, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper workspace file-lock symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `6c281bc` (`Reject symlink workspace file locks`) to `fork/agent/threadkeeper-hardening-next`.

Per-target workspace lock files used by atomic `write-file` / `append-file` updates now open through the shared regular non-symlink no-follow helper. Existing symlink or non-regular `.target.lock` paths fail closed before file-tool synchronization, preventing a local workspace lock path from redirecting coordination outside `OMEGACLAW_SUBAGENT_WORKSPACE`. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`186 passed`); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper checksum sidecar symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `7387f40` (`Reject symlink integrity sidecars`) to `fork/agent/threadkeeper-hardening-next`.

Required local `.sha256` integrity sidecars are now rejected if they are symlinks or non-regular files before any digest read. The reader uses the existing no-follow regular-file open path, preserves the configured byte cap (`OMEGACLAW_SUBAGENT_MAX_SHA256_SIDECAR_BYTES`), and keeps path details out of errors. This tightens queued-task checksum verification and candidate/transcript sidecar review without changing worker semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`185 passed`); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper run-index symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `372e336` (`Reject symlink run index files`) to `fork/agent/threadkeeper-hardening-next`.

Finished-run `index.jsonl` appends and read-only `verify_subagent_run_index()` audits now reject symlink/non-regular `index.jsonl` and `index.jsonl.lock` paths, using no-follow opens where available for newly created audit files. This closes a local audit-log redirection gap in the persistent run-record path without changing queue/worker semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`184 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper inline task-contract list validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `cbe37d3` (`Tighten inline task contract list validation`) to `fork/agent/threadkeeper-hardening-next`.

Inline/persona task-contract string-list fields (`allowed_paths`, `forbidden_actions`, `done_criteria`) no longer stringify scalar or non-string values during normalization. Malformed list-shape contracts now fail closed as `contract_invalid` before worker LLM calls, matching the stricter queued-task contract validator and preventing accidental broadening of file/path/action constraints. Updated focused tests and reference docs; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`181 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-08 - ThreadKeeper async worker signal-state cleanup

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `2258f6a` (`Clear async worker signal state after run`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now clears its module-local SIGTERM/SIGINT stop flag in the `finally` cleanup path after restoring prior signal handlers and writing finished lock metadata. This prevents a graceful stop handled by one supervised same-process worker-loop run from poisoning a later invocation into exiting before it checks the queue. Added focused regression coverage and updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`179 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper Telegram-private preflight blocker

Archived non-live gate `artifacts/ggb-capacity-gates/20260708-threadkeeper-telegram-private-preflight/` before any further ThreadKeeper Telegram-private smoke. The artifact-local checker reads local supervisor/runner scripts, the staged integration RUN, current supervisor `status`, and source/runtime `subagent.py` only; it does not start/stop supervisors, call Telegram/providers, enqueue tasks, read secret env contents, or change runtime behavior.

Result: `preflight_report.json` is `blocked` with 9/12 checks passing. Blockers: the staged gate says `TG_PRIVATE_ONLY=true`, but `local/omegaclaw-telegram-private-supervisor.sh` currently defaults `DEFAULT_TG_PRIVATE_ONLY=false`; its default `DEFAULT_TG_CHAT_IDS` includes non-private/group-style targets (`-5437945421,-1003983157420,-5459676079`); and `status` reported an already active supervisor (`active pid 679631`) during the preflight. Positive check: ThreadKeeper source `src/subagent.py` and the nested OmegaClaw-Core runtime copy are byte-identical.

Verification: non-live preflight checker completed; GGB fixture checker passed for the new gate; targeted `git diff --check` passed. Recommended next action: resolve the private-only/default-chat boundary or require explicit safe environment overrides before any live private Telegram smoke; keep group/channel targets as a separate explicit gate. No paid compute, Telegram call, provider call, queue enqueue, secret read, supervisor start/stop, runtime behavior change, push/merge/force-push, or daemon/scheduler install.


## 2026-07-08 - ThreadKeeper queued task symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `df483df` (`Reject symlink queued task records`) to `fork/agent/threadkeeper-hardening-next`.

Queue listing/backpressure now count only regular non-symlink `queue/*.json` records, oldest-first sorting uses `lstat`, and `run_queued_dispatch()` rejects symlink/non-regular queued-task paths before atomic claim or JSON/sidecar reads. This closes a local queue redirection/false-backpressure gap without changing worker semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`178 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper worker-lock GGB refresh

Archived `artifacts/ggb-capacity-gates/20260708-threadkeeper-worker-lock-hardening/` to map the latest ThreadKeeper async-worker lock hardening through the GGB capacity gate pattern. Current branch `agent/threadkeeper-hardening-next` is at `db834ce`; `origin/pr-1` remains an ancestor. The gate records the bounded stale-lock metadata reader (`76587eb`), symlink/non-regular stale-lock metadata rejection and lock-acquisition rejection (`db834ce`), runtime-tree sync, and 177 focused mock tests passing.

Checks: PR #1 ancestry check; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`177 passed`); source/runtime `py_compile`; source/runtime `cmp`; OmegaClaw GGB fixture checker. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, daemon/scheduler install, push, merge, force-push, or remote-ref deletion.


## 2026-07-08 - ThreadKeeper async worker lock symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `db834ce` (`Reject symlink async worker locks`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async-worker loop now ignores symlink/non-regular `.async-worker.lock` files when reading stale-lock metadata and rejects symlink/non-regular lock paths before acquiring a new worker lock, using `O_NOFOLLOW` where available plus an `fstat` regular-file check. This closes a local lock redirection gap without changing queue semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`177 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-08 - ThreadKeeper worker lock metadata read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `76587eb` (`Bound worker lock metadata reads`) to `fork/agent/threadkeeper-hardening-next`.

The async worker stale-lock reader now bounds `.async-worker.lock` metadata reads with `OMEGACLAW_SUBAGENT_ASYNC_WORKER_LOCK_METADATA_BYTES` (default 8192, minimum 1024) before UTF-8/JSON parsing. Oversized/corrupt lock metadata is ignored instead of being surfaced as stale-lock evidence, keeping operator/supervisor diagnostics from parsing adversarial local blobs. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`175 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-08 - ThreadKeeper bounded-read GGB refresh

Archived `artifacts/ggb-capacity-gates/20260708-threadkeeper-bounded-read-refresh/` to consolidate the latest ThreadKeeper bounded local-read/audit evidence through the GGB gate pattern. The gate covers escalation policy pinning (`313664a`), persona config/prompt setup (`6e790ba`), worker LLM rate/concurrency guard state (`63bc0bc`), candidate/checksum sidecars (`ef89b40`/`77197df`), and streamed transcript audit hashing (`062ee72`). Current branch `agent/threadkeeper-hardening-next` is at `062ee72`; `origin/pr-1` remains an ancestor; nested OmegaClaw-Core runtime `subagent.py` matches the ThreadKeeper source.

Checks: PR #1 ancestry check; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`174 passed`); `py_compile` for source/runtime copy; source/runtime `cmp`; ThreadKeeper `git diff --check`; OmegaClaw GGB fixture checker. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, daemon/scheduler install, push, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper streamed transcript audit hashing

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `062ee72` (`Stream transcript audit hashing`) to `fork/agent/threadkeeper-hardening-next`.

`verify_subagent_run_index()` no longer hashes referenced transcripts with one whole-file `read()`. It now uses `_sha256_file_bounded()` to stream transcript SHA-256 checks in fixed-size chunks while still enforcing `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` during the read, preserving the existing oversized-transcript failure mode and closing a race/heap spike gap if a transcript changes between size check and hash. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`174 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper worker LLM state read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `63bc0bc` (`Bound worker LLM state reads`) to `fork/agent/threadkeeper-hardening-next`.

The per-endpoint worker LLM rate-limit and concurrency guard state files (`.llm-rate-*.json` / `.llm-inflight-*.json` under `OMEGACLAW_SUBAGENT_RUN_DIR`) are now read with `OMEGACLAW_SUBAGENT_MAX_LLM_STATE_BYTES` (default 65536, minimum 1024). Oversized/corrupt local guard state is reset under the existing lock instead of being loaded with unbounded `json.load()`, preserving fail-safe backpressure behavior without exposing a local memory-read DoS path. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`173 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.


## 2026-07-09 - GoalChainer reviewer policy replay on real petta-memory evidence

Archived `artifacts/ggb-capacity-gates/20260709-goalchainer-reviewer-policy-real-memory-replay/` as the second replay of the offline GoalChainer reviewer policy. The artifact-local validator reads the unchanged policy from `20260708-goalchainer-reviewer-policy-thresholds` plus the archived real `petta-memory` replay report only; it does not call providers/Telegram, enqueue or claim queue tasks, launch supervisors, write/promote memory, inspect secrets, or alter runtime config.

Result: 15/15 checks passed. The normalized candidate remains `needs_adjudication`/offline-only, recommends `publish_redacted_summary`, keeps `publish_raw_log` blocked/forbidden, passes thresholds (`redacted_strength=0.997816`, `raw_strength=0.040000`, margin `0.957816`), verifies leak safety, verifies 2 bounded real STV/EC evidence items, and confirms the source memory journal hash stayed unchanged. Added `.metta` sibling fixtures; JSON parse, Python compile, fixture checker, and targeted diff-check passed.

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-08 - GoalChainer reviewer policy/threshold fixture

Archived `artifacts/ggb-capacity-gates/20260708-goalchainer-reviewer-policy-thresholds/` as the next non-live sidecar gate. The new `reviewer_policy.json` and artifact-local `validate_reviewer_policy.py` replay the accepted GoalChainer queue-sidecar candidate against explicit offline reviewer criteria: `needs_adjudication` status, `publish_redacted_summary` recommendation, obligated norm status, `publish_raw_log` blocked/forbidden, leak-safe artifact, bounded candidate text, required evidence IDs, required non-actions, false live-scope flags, and belief thresholds (`redacted_strength >= 0.95`, `raw_strength <= 0.05`, margin `>= 0.80`).

Result: validator passed 14/14 and emitted `policy_report.json`; JSON parse, Python compile, GGB fixture checker, and targeted diff-check passed. This is still offline evidence only: no Telegram post, memory write, runtime bridge enablement, provider call, queue claim, supervisor launch, paid compute, secrets/access/security change, push, merge, or force-push.

## 2026-07-08 - ThreadKeeper persona setup read caps

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `6e790ba` (`Bound persona setup reads`) to `fork/agent/threadkeeper-hardening-next`.

Persona config and prompt setup now has explicit local read caps before JSON parsing, SHA-256 prompt hashing, and prompt construction: `OMEGACLAW_SUBAGENT_MAX_PERSONA_CONFIG_BYTES` (default 65536) and `OMEGACLAW_SUBAGENT_MAX_PERSONA_PROMPT_BYTES` (default 262144, `0` disables). Oversized persona artifacts fail closed before worker LLM calls and avoid echoing absolute local paths in setup errors. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`171 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper escalation policy integrity read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `313664a` (`Bound escalation policy integrity reads`) to `fork/agent/threadkeeper-hardening-next`.

Cloud-delegation `escalation.metta` SHA-256 pinning now bounds local policy reads with `OMEGACLAW_SUBAGENT_MAX_ESCALATION_POLICY_BYTES` (default 1048576, `0` disables) before hashing. Oversized pinned policies deny escalation before any worker LLM call, and integrity mismatch/read errors no longer echo absolute local paths. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`169 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper sidecar read-cap GGB refresh

Archived `artifacts/ggb-capacity-gates/20260708-threadkeeper-sidecar-read-cap-refresh/` to map the latest ThreadKeeper sidecar-read hardening through the GGB capacity gate pattern. Current branch `agent/threadkeeper-hardening-next` is at `ef89b40`; `origin/pr-1` remains an ancestor. The gate records the bounded candidate-review `.sha256` sidecar reader, the earlier required checksum sidecar cap, runtime-tree sync, and 168 focused mock tests passing.

Checks: PR #1 ancestry check; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`168 passed`); `py_compile` for source/test/runtime copy; source/runtime `cmp`; ThreadKeeper `git diff --check`; OmegaClaw GGB fixture checker. No paid compute, live Telegram/OmegaClaw/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper checksum sidecar read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `77197df` (`Bound checksum sidecar reads`) to `fork/agent/threadkeeper-hardening-next`.

Required local `.sha256` integrity sidecars are now read with `OMEGACLAW_SUBAGENT_MAX_SHA256_SIDECAR_BYTES` (default 4096, minimum 128) before digest parsing, so a tampered queue/task sidecar cannot force queue workers or audit helpers to load an arbitrary local blob into memory. Missing, oversized, malformed, non-UTF-8, or invalid digest sidecars now fail closed without echoing absolute local paths. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`167 passed`); runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper shell output memory capture cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `d29f462` (`Bound shell output memory capture`) to `fork/agent/threadkeeper-hardening-next`.

The optional allowlisted `shell` tool no longer uses `capture_output=True`, which collected combined stdout/stderr in memory before applying `OMEGACLAW_SUBAGENT_SHELL_OUTPUT_CAP`. It now redirects stdout/stderr to a temporary file and reads only `cap + 1` bytes back into memory before returning the existing truncation marker. This preserves argv-only/no-shell execution, workspace cwd pinning, sanitized env, timeout, and output-cap behavior while closing a memory-bounding gap for noisy allowlisted commands. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`165 passed`); `pr-1` ancestor check; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper patch-proposal transcript content cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `c784765` (`Bound patch proposal transcript content`) to `fork/agent/threadkeeper-hardening-next`.

Patch-proposal-only `write-file`/`append-file` calls still do not mutate workspace files, and parent digests still expose only bounded `{action,path}` proposal metadata. The full proposed content persisted in local transcripts is now bounded by `OMEGACLAW_SUBAGENT_MAX_PATCH_PROPOSAL_CHARS` (default 20000, minimum 1) with an explicit truncation marker, so review transcripts cannot grow unbounded if operators raise general tool-argument caps or workers propose large file bodies. Added focused regression coverage, docs, and env clamp coverage. Synced `src/subagent.py` to the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`164 passed`); `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper final emit type validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `52a9bc9` (`Require string final emits`) to `fork/agent/threadkeeper-hardening-next`.

`_extract_final_emit()` now rejects non-string final `emit` arguments with `EMIT_PROTOCOL_VIOLATION` instead of coercing JSON objects/lists/numbers/booleans with `str()`. This keeps final summaries/adjudication candidates under the same strict type expectations as normal tool-call arguments and prevents typed malformed output from being accepted as a successful final digest. Added direct and dispatch-level regression tests, updated `docs/reference-skills-subagent.md`, and synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`160 passed`); `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - GoalChainer queue-mediated sidecar contract

Completed the non-live follow-on contract gate after the read-only sidecar: `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-contract/`. The new `sidecar_contract.json` defines a candidate-summary sidecar that fits ThreadKeeper's existing queued-task/task-contract schema and keeps GoalChainer as an appraisal/drafting layer only: selected read-only `petta-memory` evidence and bounded candidate text in, `needs_adjudication` redacted-summary candidate out.

Validation imported ThreadKeeper `_validate_queued_dispatch_task()` and passed 10/10 checks: queued-task schema accepted; `requires_adjudication=true`; `patch_proposal_only=true`; one worker turn; `max_tool_calls=2`; live/runtime side effects forbidden; live Telegram/secrets/unbounded raw transcript/writeable memory excluded; raw-log publication blocked in the output schema; non-actions explicitly include no Telegram post, no memory write, no runtime bridge change. Fixture checker passed on the `.metta` sibling files. No actual queue task was enqueued, no worker/supervisor launched, no provider call, no Telegram message, no memory write, no secrets/access/security setting changed, no paid compute, and no push/merge/force-push.

Next small slice: add an offline adjudicator/reviewer harness for the queue-sidecar `needs_adjudication` candidate, or ask Ben for explicit private Telegram opt-in approval with stop conditions before any live bridge/runtime behavior changes.

## 2026-07-07 - GoalChainer read-only sidecar over private ThreadKeeper task

Completed the non-live Bundle D sidecar gate proposed by the topology boundary review. Added `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/` with `run_readonly_sidecar.py`, `.metta` sibling fixtures, and `report.json`. The harness reads archived private OpenClaw/ThreadKeeper smoke records, constructs a bounded appraisal request, injects synthetic read-only `petta-memory` handoff evidence (STV support for `publish_redacted_summary`; EC opposition to `publish_raw_log`), and runs GoalChainer `solve_incident(memory_items=...)` with heuristic PLN forced.

Results: 8/8 harness checks passed. Baseline and memory-informed runs both recommend `publish_redacted_summary`; `publish_raw_log` remains forbidden/blocked; memory evidence parsed/fused; redacted-summary belief strength changed `0.980529 -> 0.996970`; raw-log strength changed `0.040000 -> 0.012234`; the executed redacted artifact leak check is safe. Focused GoalChainer memory tests pass (`52 passed`) when run with explicit local `GOALCHAINER_PETTA_DIR` and `GOALCHAINER_PETTA_SWIPL`. No live Telegram/OmegaClaw runtime bridge, provider call, memory write, ThreadKeeper supervisor launch, secrets/access/security change, paid compute, push, merge, or force-push.

Next small slice: define a queue-mediated/adjudicated sidecar contract for candidate summaries before any live bridge; private Telegram opt-in still requires explicit Ben approval and stop conditions.

## 2026-07-07 - ThreadKeeper transcript hash audit read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `a258c73` (`Bound transcript hash audit reads`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` (default 1048576, `0` disables) so read-only `verify_subagent_run_index()` checks each referenced transcript size before reading it to verify SHA-256. Oversized transcripts are reported as structured `transcript_too_large` issues under `index_tampered` and are not read into memory, closing the follow-on audit-memory gap after the earlier `index.jsonl` scan cap. Updated docs/tests and synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`155 passed`); runtime-tree compile/source cmp; `git diff --check`; `origin/pr-1` remains an ancestor. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper native worker HTTP response cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `ddf9aae` (`Bound native worker HTTP responses`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_LLM_HTTP_RESPONSE_BYTES` (default 1048576, `0` disables) to bound the raw HTTP body read from native Ollama-compatible worker transports before JSON decoding. This closes a transport-layer memory-bounding gap: OpenAI-compatible SDK calls remain bounded after parsed content by `OMEGACLAW_SUBAGENT_MAX_RESPONSE_CHARS`, while native urllib calls now avoid reading arbitrarily large local provider bodies into memory. Added focused tests for oversized native bodies and under-cap decode/token accounting; updated docs and synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`153 passed`); `origin/pr-1` remains an ancestor; runtime-tree compile/source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper audit/cap refresh GGB gate

Refreshed the GGB roadmap with the latest ThreadKeeper hardening evidence at branch `agent/threadkeeper-hardening-next` head `080ed28`: final emit cap, configurable JSON audit/task read cap, non-finite numeric env rejection, raw worker response cap, and run-index audit read cap. Added gate artifact `artifacts/ggb-capacity-gates/20260707-threadkeeper-audit-cap-refresh/` with `.metta` sibling fixtures. Verified focused ThreadKeeper mock pytest (`151 passed`), runtime-tree sync (`src/subagent.py` equals nested OmegaClaw-Core runtime copy), runtime compile, fixture checker, and targeted diff check. No live runtime behavior, Telegram/worker supervisor launch, secrets/access/security changes, paid compute, daemon/scheduler install, push, merge, or force-push.

## 2026-07-07 - OmegaClaw/ZeroBot topology boundary review

Drafted `docs/omegaclaw_zerobot_topology_decision_note.md` and archived GGB gate `artifacts/ggb-capacity-gates/20260707-topology-boundary-review/`. Recommendation: use a supervised queue-mediated bridge before any live bidirectional OmegaClaw↔ZeroBot/OpenClaw chat bridge. GoalChainer should first run as a read-only decision sidecar over bounded task text plus selected `petta-memory` handoff evidence; ThreadKeeper remains the delegation/audit/adjudication layer; accepted/adjudicated summaries are the only candidate egress. Direct Telegram group and direct recursive OpenClaw bridges are deferred. No live Telegram/OmegaClaw/GoalChainer/ThreadKeeper behavior changed; no secrets/access/security settings, paid compute, daemon/scheduler install, push, merge, or force-push.

Checks: document exists; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py projects/omegaclaw/artifacts/ggb-capacity-gates/20260707-topology-boundary-review`; targeted `git diff --check`.


## 2026-07-07 - ThreadKeeper non-finite numeric env hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `2f0a10b` (`Reject non-finite numeric env knobs`) to `fork/agent/threadkeeper-hardening-next`.

`_env_float()` now rejects non-finite float env values (`nan`, `inf`, `-inf`, case-insensitive variants) and falls back to the documented safe defaults instead of letting NaN/Infinity propagate into retry backoff, shell timeout, async worker poll/runtime bounds, queued-task max age, or dispatch timeout controls. This closes a small numeric-config validation gap left after malformed/below-minimum env parsing was hardened. Updated reference docs and added focused reload coverage. Synced `src/subagent.py` to the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`148 passed`); `origin/pr-1` remains an ancestor before commit; runtime-tree `py_compile` and source/runtime `cmp`. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper run-index audit read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `080ed28` (`Bound subagent run index audits`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_INDEX_AUDIT_BYTES` (default 1048576, 0 disables) so the read-only `verify_subagent_run_index()` helper refuses to scan oversized `index.jsonl` files, returning structured `index_audit_too_large` before reading entries or transcript files. This complements index-entry rotation and prevents an unbounded/auditor-triggered local read when rotation is intentionally disabled. Updated docs and focused mock coverage; synced `src/subagent.py` to the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`151 passed`); `origin/pr-1` remains an ancestor; runtime-tree `py_compile` and source/runtime `cmp`. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper raw worker response cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `fc34757` (`Bound raw subagent worker responses`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_RESPONSE_CHARS` (default 50000, minimum 1) so oversized raw worker responses fail closed as `response_too_large` before tool-call parsing/execution and before unbounded transcript persistence. The transcript stores only a bounded preview, preserves worker token accounting, and returns a structured parent digest with `next_action` guidance. This complements the final `emit` cap, transcript field caps, per-turn tool-call cap, and token budget controls. Updated docs and focused mock coverage; synced `src/subagent.py` to the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`149 passed`); `origin/pr-1` remains an ancestor; runtime-tree `py_compile` and source/runtime `cmp`. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper final emit size cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `4d7d4f4` (`Bound final subagent emit size`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_EMIT_CHARS` (default 20000, minimum 1) so a worker's final `(emit ...)` argument is protocol-validated before being accepted as successful output, transcript summary, or adjudication candidate. Oversized emits now return structured `EMIT_PROTOCOL_VIOLATION` with transcript status `emit_protocol_violation` instead of letting an unbounded final answer become persisted run state. This complements existing parent digest, transcript-turn, transcript-field, transcript-summary, and tool-argument caps.

Added focused coverage for oversized emit rejection and numeric env clamp/reload behavior; updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` to the OmegaClaw-Core runtime tree with zero diff.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`147 passed`); runtime-tree `py_compile`; `origin/pr-1` remains an ancestor via existing local ref before commit. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - petta-memory GoalChainer heuristic-memory probe

Completed the next Bundle D handoff step from the GGB roadmap: `projects/petta-memory/repos/petta-memory` now lets `run_goalchainer_precompiled_handoff_smoke(..., include_heuristic_memory_probe=True)` also exercise GoalChainer's actual `solve_incident(memory_items=...)` heuristic-with-memory path. Added CLI flag `goalchainer-smoke --heuristic-memory-probe`, a focused unittest, and gate record `artifacts/ggb-capacity-gates/20260706-petta-memory-goalchainer-heuristic-probe/`.

Runtime artifact: `projects/petta-memory/repos/petta-memory/artifacts/goalchainer_heuristic_memory_probe_2026-07-07T0334Z.json` sha256 `3e55ca9531ef93ecd4e2f5b8375d318aa53b1cf21d4e02f6ae92724b3bdeaa2f`. It reports `heuristic_with_memory_path_checked=True`, `decided=publish_redacted_summary`, `memory_proof_present=True`, and `leak_check_safe=True`.

Checks: focused `PYTHONPATH=src python3 -m unittest tests.test_goalchainer_smoke -v` (`7 passed`), full `PYTHONPATH=src python3 -m unittest discover -s tests -v` (`377 passed`), `git diff --check`, and `local/check-ggb-gate-fixtures.py` on the new gate. No live Telegram/OmegaClaw runtime integration, no OmegaClaw skill loading, no accepted directive/task claim, no memory write, no secrets/access/security changes, no paid compute, no daemon/scheduler install, no push/merge/force-push.

## 2026-07-06 - ThreadKeeper search/tavily-search/technical-analysis output size cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `ee894d3` (`Add output size cap for search/tavily-search/technical-analysis tools`) to `fork/agent/threadkeeper-hardening-next`.

The `_tool_read_file` function already bounds output via `_SUBAGENT_MAX_READ_FILE_CHARS` (default 20000) and `_tool_shell` bounds via `_SHELL_OUTPUT_CAP` (default 4000), but `search`, `tavily-search`, and `technical-analysis` had no tool-level output cap. While `run_tools` clips all tool results to 2000 chars for the prompt via `_clip(str(result), 2000)`, the full unbounded external API response was in memory before clipping. A very large search response or tavily result could consume significant memory.

New config knob `OMEGACLAW_SUBAGENT_MAX_SEARCH_OUTPUT_CHARS` (default 4000, 0 disables, matching the pattern of other bounding knobs) caps the output at the tool level. Added `_bound_tool_output(result, cap=None)` helper that reads the module-level config at call time (not as a default parameter, which would be evaluated once at function definition time and ignore monkeypatching in tests). All three search-type tool registrations in `_build_tool_registry()` are now wrapped: `lambda q: _bound_tool_output(websearch.search(q))`, etc.

Added 6 focused tests (137 total): large result truncation with marker, small result preservation, cap disabled when 0, non-string result handling (lists/dicts str()'d and bounded), search registry wrapping (FakeWebsearch with 10k output, verified truncation), tavily/technical-analysis registry wrapping (FakeAgentverse with 10k outputs for both tools).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`137 passed`); `origin/pr-1` remains an ancestor (75 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper configurable JSON audit/task read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `209da6c` (`Make JSON audit read cap configurable`) to `fork/agent/threadkeeper-hardening-next`.

`_read_json_file()` already had a hard-coded 256 KiB read cap for queue records and reviewable transcript JSON, but operators could not tune it and the oversize error included the local path. Added `OMEGACLAW_SUBAGENT_MAX_JSON_FILE_BYTES` (default 262144, minimum 1024) and made `_read_json_file()` use that module-level cap by default while preserving explicit per-call override support. Oversize errors now avoid echoing absolute local paths, matching the existing error-sanitization direction.

Added 2 focused tests: configured size-cap rejection with no tmp path leak, and explicit max_bytes success/digest behavior. Also extended the numeric env reload fallback/clamp test to cover the new knob.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`146 passed`); `origin/pr-1` remains an ancestor via existing local ref. Synced `subagent.py` to the OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - GoalChainer petta-memory evidence bridge

Implemented the memory-evidence bridge that connects `petta-memory` promoted evidence packets to GoalChainer's heuristic PLN belief grader. This is the concrete bridge described as the next step in Bundle D of the GGB roadmap.

**Changes:**

1. `heuristic_beliefs.py`: Added `parse_memory_evidence()` to parse `petta-memory` handoff cache items (STV atoms and EvidencePacket EC atoms) into `MemoryEvidenceItem` objects. Added `grade_beliefs_heuristic_with_memory()` that fuses memory evidence with keyword-derived ground facts using the existing subjective-logic combination rule. Fixed `_ground_to_sl()` to handle `memory_*` rule labels by using the fact strength/confidence directly (no rule-chain product), since memory evidence doesn't go through a PLN implication rule.

2. `metta_reasoner.py`: Extended `reason_over_hyperbase()` with optional `memory_items` parameter. When the heuristic path is active and memory items are provided, beliefs are graded with `grade_beliefs_heuristic_with_memory()` instead of the baseline `grade_beliefs_heuristic()`. The `belief_source` metadata and `input` field reflect memory evidence presence.

3. `pipeline.py`: Extended `solve_incident()` with optional `memory_items` parameter, passed through to `reason_over_hyperbase()`.

4. `tests/test_heuristic_memory_bridge.py`: New test file with 18 tests covering `parse_memory_evidence` (STV/EC parsing, mixed items, unparseable skipping, zero-total skipping, clamping), `grade_beliefs_heuristic_with_memory` (no-memory baseline equivalence, empty-list baseline, STV adjustment, EC adjustment, conflicting memory lowering strength, memory for unsupported actions, multiple items fused, proof tagging), `reason_over_hyperbase` with memory (belief adjustment, baseline equivalence), and `solve_incident` with memory (correct decision with positive memory, correct decision with conflicting memory).

**Results:**
- New tests: 18 passed, 0 failed
- Full GoalChainer suite: 53 passed, 6 skipped, 0 failed (up from 35 passed, 6 skipped, 0 failed)
- `petta-memory` GoalChainer smoke tests: 6 passed, 0 failed (no regressions)
- GGB fixture checker passes across all 19 gate fixtures including the new `20260706-goalchainer-memory-evidence-bridge` gate

**Key design decisions:**
- Memory evidence is only applied through the heuristic path. When PeTTaChainer becomes available (compileadd bottleneck fixed), memory items would need to be loaded as PLN premises instead.
- The bridge parses atoms by regex, not by loading them through PeTTa. This is intentional for the non-live heuristic path.
- Memory evidence does not override the deontic verdict (forbidden/obligated/permitted), which comes from `lib_deontic` independently. Memory evidence only adjusts the PLN belief strength/confidence that feeds the scoring engine.
- When no memory items are provided, `grade_beliefs_heuristic_with_memory()` is identical to `grade_beliefs_heuristic()`.

**Environment:** Same as prior GoalChainer gates: `GOALCHAINER_PETTA_DIR=projects/omegaclaw/repos/PeTTa`, `GOALCHAINER_PETTA_SWIPL=projects/omegaclaw/local/swipl-9.3.36/lib/swipl/bin/x86_64-linux/swipl`, `GOALCHAINER_PETTACHAINER_DIR=projects/petta-memory/repos/PeTTaChainer`.

No live Telegram/OmegaClaw runtime integration, secrets/access/security changes, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper empty search/tavily-search/technical-analysis query rejection

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `86cc243` (`Reject empty search/tavily-search/technical-analysis queries`) to `fork/agent/threadkeeper-hardening-next`.

The `_validate_tool_args` function previously validated argument count, null, path-emptiness, path length, shell-emptiness, overall arg length, and NUL bytes for all tools, but `search`, `tavily-search`, and `technical-analysis` had no empty/whitespace-only check. A worker LLM response containing `(search "")` or `(tavily-search "   ")` would pass validation and call the external search/agentverse API with an empty query, wasting a network call and potentially returning unhelpful results.

New validation: for `search`, `tavily-search`, and `technical-analysis`, the first argument must be non-empty after stripping whitespace, matching the existing pattern for `shell` commands. This rejects `(search "")`, `(tavily-search "   ")`, `(technical-analysis "\t\n")`, etc.

Added 2 focused tests: (1) `test_validate_tool_args_search_rejects_empty_query` — verifies all three search-type tools reject empty, whitespace, and tab/newline queries; (2) `test_validate_tool_args_search_accepts_nonempty_query` — verifies all three pass with real query strings.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`131 passed`); `origin/pr-1` remains an ancestor (74 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper run index entry bounding with rotation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `ca98d36` (`Add run index entry bounding with rotation`) to `fork/agent/threadkeeper-hardening-next`.

The compact audit index (`index.jsonl`) previously grew unbounded — every finished subagent run appends a hash-chained entry, and for long-running @Protomegabot deployments with many queued tasks, this file could grow very large over time. New config knob `OMEGACLAW_SUBAGENT_MAX_INDEX_ENTRIES` (default 0 = disabled, matching the pattern of other bounding knobs) caps the number of entries. When non-zero, the index is rotated after each append to keep only the most recent N entries.

The rotation recomputes the hash chain for retained entries: the first retained entry gets `previous_entry_sha256 = ""` (as if it were the first entry) and each subsequent entry's `previous_entry_sha256` links to the prior retained entry's recomputed `entry_sha256`. This means `verify_subagent_run_index` still passes on the retained portion — the chain is intact within the retained entries, and an auditor can verify it as they would a fresh index.

The rotation is performed under the existing index lock so concurrent appenders are safe. If rotation fails for any reason, the index remains append-only and unbounded (the safe default). The rotation uses an atomic temp-file + `os.replace` rewrite.

Added 5 focused tests: (1) rotation truncates to cap (5 appends with cap=3 → 3 retained, correct entries, chain intact); (2) disabled when 0 (default, no rotation); (3) no rotation under cap (4 appends with cap=4, all retained); (4) rotated index verifies correctly (4 appends with cap=2, `verify_subagent_run_index` passes with 2 entries checked); (5) single-entry cap (3 appends with cap=1, only last entry retained).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`129 passed`); `origin/pr-1` remains an ancestor (73 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - GoalChainer OmegaClaw skill surface non-live smoke

Ran the full GoalChainer pipeline through both the Python CLI skill surface (`omegaclaw_skill.py`) and the actual OmegaClaw MeTTa skill surface (`run_in_omegaclaw.metta` via PeTTa/SWI). This is the first end-to-end demonstration of GoalChainer through the actual OmegaClaw MeTTa `eval` → `py-call` → pipeline → PeTTa/SWI deontic/directive runtime path, not just direct Python CLI invocation.

**Python CLI results:**
- `goalchainer-decision`: exit 0; `publish_redacted_summary` recommended (obligated, score 1.010108, belief STV 0.9805/0.9933), `publish_raw_log` blocked (forbidden, score -1.0), `hold_external_update` weak (permitted, score 0.385841). Evidence source: `omega-core-petta-lib-deontic-pettachainer` with `belief_source: heuristic_pln`.
- `goalchainer-solve`: exit 0; decided `publish_redacted_summary`; artifact has all sensitive fields redacted (customer_email, order_id, request_payload, access_token, stack_trace); leak check `safe=True, leaked=[]`.
- `goalchainer-directive`: exit 0; task states: `publish_redacted_summary=ready`, `publish_raw_log=blocked`, `hold_external_update=backlog`; claim: `agent=responder, task=publish_redacted_summary`; runtime: `OmegaClaw-Core lib_directive on PeTTa`.

**MeTTa skill surface results (via `run_in_omegaclaw.metta`):**
- OmegaClaw Core skill registry loaded (`import! &self (library OmegaClaw-Core src/skills)`)
- GoalChainer skills registered (`import! &self goalchainer_skill`)
- `goalchainer-skill-docs` emitted 4 skill descriptions
- `(eval (goalchainer-decision ...))` produced: `DECISION (GoalChainer on PeTTa: lib_deontic + PeTTaChainer + MetaMo)`, `recommended: publish_redacted_summary (score 1.010108)`, `blocked: publish_raw_log (lib_deontic: forbidden)`
- `(eval (goalchainer-solve ...))` produced: `SOLVE: decided publish_redacted_summary (recommended), channel external`, `blocked: publish_raw_log (lib_deontic: forbidden)`, `redacted: customer_email, order_id, request_payload, access_token, stack_trace`, `kept: error_code=PAYMENT_TIMEOUT`, `leak check: safe=True leaked=[]`

**Environment:** `GOALCHAINER_PETTA_DIR=projects/omegaclaw/repos/PeTTa`, `GOALCHAINER_PETTA_SWIPL=projects/omegaclaw/local/swipl-9.3.36/lib/swipl/bin/x86_64-linux/swipl`, `GOALCHAINER_PETTACHAINER_DIR=projects/petta-memory/repos/PeTTaChainer`.

**Test suite:** 35 passed, 6 skipped, 0 failed.

**GGB fixture checker:** passes across all 18 gate fixtures including the new `20260706-goalchainer-skill-surface-smoke`.

No live Telegram/OmegaClaw runtime integration, secrets/access/security changes, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper transcript summary bounding and empty shell command rejection

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `fb60ebf` (`Bound transcript summary field and reject empty shell commands`) to `fork/agent/threadkeeper-hardening-next`.

Two concrete hardening improvements:

1. **Transcript summary bounding**: The transcript record's `summary` field (set by `_finish_run_record`) was not bounded, even though `_bound_transcript_turns` already bounds the `turns` list. A very long worker emit value was stored as-is in the transcript JSON file, potentially producing very large files from runaway dispatches. New config knob `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_SUMMARY_CHARS` (default 0 = disabled, matching the pattern of other transcript bounding knobs) caps the summary with an explicit `[...summary truncated at N chars...]` marker when enabled.

2. **Empty shell command rejection**: `_validate_tool_args` now rejects `shell` commands that are empty or whitespace-only after stripping, closing a gap where `(shell "")` or `(shell "   ")` passed validation but produced a confusing runtime 'empty command' error deeper in the execution path.

Added 5 focused tests: (1) long summary capped with marker; (2) cap disabled when 0 (default); (3) short summary preserved; (4) empty/whitespace shell commands rejected; (5) non-empty shell commands accepted.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`124 passed`); `origin/pr-1` remains an ancestor (72 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper per-task duration and total runtime in worker loop results

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `1c6c0c6` (`Add per-task duration and total runtime to worker loop results`) to `fork/agent/threadkeeper-hardening-next`.

The worker loop result items now include `task_duration_s` (wall-clock seconds from task start to completion) for each drained task, covering both successful and error results. The structured return also now includes `total_runtime_s` across all return paths (`worker_idle`, `worker_drained`, `worker_config_invalid`, `worker_already_running`) so operators can see the overall loop duration without subtracting timestamps.

This improves operator audit visibility: slow tasks are immediately identifiable in the results list, and the total loop runtime is available without parsing `started_at`/`finished_at` pairs. The `task_duration_s` field is added to result items after `run_queued_dispatch` returns (or after an exception is caught), so it reflects the actual wall-clock time spent on each task including setup, LLM calls, tool execution, and teardown.

Added 5 focused tests: (1) `test_worker_loop_results_include_task_duration_s` — verifies 2 successful results each have numeric non-negative `task_duration_s`; (2) `test_worker_loop_results_include_task_duration_s_on_error` — verifies error results also include `task_duration_s`; (3) `test_worker_loop_return_includes_total_runtime_s` — verifies `total_runtime_s` is present in the `worker_idle` return and consistent with `started_at`/`finished_at`; (4) `test_worker_loop_config_invalid_includes_total_runtime_s` — verifies `total_runtime_s` in the `worker_config_invalid` return; (5) `test_worker_loop_already_running_includes_total_runtime_s` — verifies `total_runtime_s` is present in the idle return path.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`119 passed`); `origin/pr-1` remains an ancestor (71 commits ahead). Synced the updated `subagent.py` to the OmegaClaw-Core runtime tree and verified compile and zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper worker loop lock metadata completion fields and queue depth

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `1f4d70b` (`Add completion fields and queue depth to worker loop lock metadata`) to `fork/agent/threadkeeper-hardening-next`.

The finished lock metadata previously dropped `tasks_completed` and `consecutive_errors` that were present in the running lock metadata, leaving operators without completion counts in the final lock file. The finished metadata now includes `tasks_completed`, `consecutive_errors`, and `remaining_queue_tasks` (pending queue count) for full operator audit after the worker exits.

The running lock metadata (both pre-task and post-task updates) now also includes `remaining_queue_tasks`, computed as `len(_pending_queued_dispatch_paths())` at the time the metadata is written. This gives operators live queue depth visibility while the worker is actively processing, complementing the existing `tasks_attempted`, `tasks_completed`, `consecutive_errors`, `error_count`, and `current_task_*` fields.

Added 3 focused tests: (1) `test_finished_lock_metadata_includes_completion_fields` — verifies `tasks_completed`, `consecutive_errors`, and `remaining_queue_tasks` are present in the finished lock metadata after a clean `worker_idle` exit; (2) `test_running_lock_metadata_includes_remaining_queue_tasks` — queues 3 tasks, spies on `run_queued_dispatch` to capture running lock metadata during execution, verifies decreasing `remaining_queue_tasks` across calls (3→2→1) and 0 in the finished metadata; (3) `test_finished_lock_metadata_shows_errors_after_failures` — makes all worker LLM calls raise, verifies `tasks_completed=0`, `consecutive_errors=2`, `error_count=2`, and `remaining_queue_tasks=0` in the finished lock metadata.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`114 passed`); `origin/pr-1` remains an ancestor (70 commits ahead). Synced the updated `subagent.py` to the OmegaClaw-Core runtime tree and verified compile and zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - GoalChainer deontic/directive runtime seams fixed

Diagnosed and fixed the two remaining GoalChainer runtime failures that were blocking Bundle D progress:

1. **`derive_deontic` returning `unregulated` for all actions**: Root cause was that `omegaclaw-deontic` (the separate `lib_deontic` package at `https://github.com/MesTTo/omegaclaw-deontic`) had not been installed into the local OmegaClaw-Core tree. The `external/omegaclaw-deontic/` directory in the GoalChainer clone was empty. Cloned the repo and ran `./install.sh` to copy `lib_deontic.metta` and its submodules (platform Prolog files, deontic engine, query, explain, trust, eventcalc) into `PeTTa/repos/OmegaClaw-Core/`.

2. **`lib_directive` plan not surfacing ready/next/claim state**: Same root cause as (1) — `lib_directive` is part of the same `omegaclaw-deontic` package and was not installed.

3. **PeTTa library path resolution gap**: PeTTa resolves `(library OmegaClaw-Core ...)` to `PeTTa/OmegaClaw-Core/...` via `library_path(Base)` set in `metta.pl`, but the local clone was at `PeTTa/repos/OmegaClaw-Core/`. Created a symlink `PeTTa/OmegaClaw-Core -> repos/OmegaClaw-Core` so library imports resolve correctly.

After these fixes, the full deontic→directive pipeline works:
- `derive_deontic(evidence)` correctly returns `publish_raw_log=forbidden`, `publish_redacted_summary=obligated`, `hold_external_update=permitted`
- `register_directive(deontic)` correctly classifies task states (`blocked`, `ready`, `backlog`), surfaces ready/next/claim state, and claims `publish_redacted_summary` for the responder agent
- GoalChainer test suite: `26 passed, 6 skipped, 9 failed` (up from `25 passed, 6 skipped, 10 failed`). All 9 remaining failures are PeTTaChainer-related (missing `GOALCHAINER_PETTACHAINER_DIR` or `compileadd` stack-limit). Deontic, directive, scoring, execution, and skill tests all pass (15 tests).

The `petta-memory` PeTTaChainer `compileadd` bottleneck remains the only blocking issue for the full GoalChainer pipeline (`solve_incident`), which requires PeTTaChainer belief grading.

Non-live changes only: cloned `omegaclaw-deontic` for inspection, ran its installer into the local OmegaClaw-Core tree, created a symlink for PeTTa library resolution. No live Telegram/OmegaClaw runtime wiring, secrets/access/security changes, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper current-task tracking in worker loop lock metadata

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `41f863c` (`Add current-task tracking to worker loop lock metadata`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now writes `current_task_started_at` and `current_task_queue_path` into the lock metadata before calling `run_queued_dispatch(queue_path)`, then clears them (sets to `None`) after the task completes in the post-task metadata update and in the `finally` block's finished metadata. This closes a diagnostic gap: previously, if a worker crashed mid-task (SIGKILL, OOM), the stale lock would show `status=running` with `tasks_attempted=N` but no indication of which task was being processed or when it started. Now, the stale_lock metadata includes `current_task_started_at` and `current_task_queue_path`, giving operators/supervisors crash diagnostics that identify the problematic task and approximate crash timing.

The initial lock metadata (written before any task) also includes `current_task_started_at: None` and `current_task_queue_path: None` for consistency.

Added 3 focused tests: (1) lock metadata during task execution includes current-task fields — uses a spy on `run_queued_dispatch` to read lock metadata mid-task and verifies `current_task_started_at` is not None and `current_task_queue_path` matches the queue path, then verifies the finished lock has cleared fields; (2) stale lock from crashed mid-task worker includes current-task fields — simulates a crashed worker with `current_task_started_at=1500.0` and a queue path, verifies the `stale_lock` in the return includes both fields; (3) finished lock metadata has null current-task fields after clean worker_idle exit.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`111 passed`); `origin/pr-1` remains an ancestor (69 commits ahead). Synced the updated `subagent.py` to the OmegaClaw-Core runtime tree and verified compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper stale worker lock detection

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `6bbf76d` (`Detect stale worker lock from crashed previous worker`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now detects stale locks from crashed previous workers: before acquiring the flock, the loop reads the existing lock file metadata. If the file shows `status=running` but the flock can be acquired (meaning the previous holder is dead/gone), the structured return includes `stale_lock` audit metadata (pid, started_at, max_tasks, tasks_attempted, etc.) so operators and supervisors can detect when a previous worker died without clean shutdown (e.g. SIGKILL, OOM). The `stale_lock` field is also included in the early `max_tasks=0` no-claim return (always `None`) and the `worker_already_running` return for consistency.

Added 3 focused tests: (1) stale lock detected from simulated crash — writes `status=running` metadata without holding flock, verifies `stale_lock` has the old PID and the lock file is then overwritten with `finished` metadata from the new worker; (2) no stale lock on fresh start — no previous lock file exists; (3) no stale lock after clean shutdown — previous lock file shows `status=finished`.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`108 passed`); `origin/pr-1` remains an ancestor (68 commits ahead). Synced the updated `subagent.py` to the OmegaClaw-Core runtime tree and verified compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper tool error path sanitization

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `25483fb` (`Sanitize absolute paths from tool error messages`) to `fork/agent/threadkeeper-hardening-next`.

Tool error messages (read-file, write-file, append-file, shell) previously included raw exception text that could leak absolute filesystem paths (e.g. workspace root, /tmp, /home) to the worker LLM and into persisted transcripts. A worker LLM seeing these paths could exfiltrate them via emit, or they could be persisted in transcripts accessible to parent agents.

Added `_sanitize_error_msg(e)` helper that:
- Replaces the workspace root with `<workspace>` placeholder
- Replaces remaining absolute Unix paths (e.g. /tmp/secret, /home/user/data) with `<path>` placeholder
- Leaves non-path messages unchanged

Also removed the workspace root from `_resolve_workspace_path`'s escape error message (was `f"path escapes subagent workspace ({root}): {path}"`, now just `"path escapes subagent workspace"`) and from the shell missing-workspace error, preventing leaks at the source.

Updated `run_tools()` error handlers (`SKILL_ARG_ERROR`, `SKILL_RUNTIME_ERROR`) to use the same sanitizer.

Added 4 focused tests: path escape in read/write/append tools verifies no workspace root or `/home/` in error, `_resolve_workspace_path` error content verifies no absolute paths, `_sanitize_error_msg` replacement behavior verifies workspace and absolute path replacement, shell missing-workspace error verifies no leaked path.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`105 passed`); `origin/pr-1` remains an ancestor (67 commits ahead). Synced the updated `subagent.py` to the OmegaClaw-Core runtime tree and verified compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper graceful SIGTERM/SIGINT worker-loop shutdown

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `c8a14e4` (`Add graceful SIGTERM/SIGINT handling to worker loop`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop (`subagent.run_queued_worker_loop(...)`) now registers signal handlers for SIGTERM and SIGINT that set a module-level flag (`_worker_signal_state["stop_requested"]`) instead of raising. The main loop checks this flag at each iteration and exits cleanly with `stop_reason="signal"` when a supervisor sends SIGTERM/SIGINT, rather than dying abruptly mid-task and orphaning a `.claimed` queue record or leaving the lock file in `running` state. Prior signal handlers are restored in the `finally` block so the worker loop does not leak its handler into the caller's context. The status mapping now treats `signal` the same as `stop_file` → `worker_stopped`.

This closes a concrete hardening gap: previously, a supervisor sending SIGTERM to the worker process (e.g., via `setsid` + `kill -TERM -- -PID`) would kill it immediately, potentially leaving a claimed task orphaned and the lock file stuck in `running` state.

Added 2 focused tests: `test_run_queued_worker_loop_graceful_signal_shutdown` (pre-sets the signal flag, verifies `worker_stopped` with `stop_reason="signal"` and finished lock metadata) and `test_run_queued_worker_loop_restores_signal_handlers` (verifies SIGTERM handler is restored to its pre-loop value after the loop exits).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`101 passed`); `origin/pr-1` remains an ancestor (66 commits ahead). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper dispatch-level token budget cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `14ec2ee` (`Add dispatch-level token budget cap`) to `fork/agent/threadkeeper-hardening-next`.

Added `OMEGACLAW_SUBAGENT_MAX_TOKENS_PER_DISPATCH` (default 0 = disabled): when non-zero, the dispatch loop checks total accumulated worker LLM tokens (input + output) after each worker LLM call and returns a structured `token_budget_exceeded` record if the cap is exceeded. `worker_token_usage` is persisted to the transcript before returning. This complements the existing per-turn/per-dispatch tool-call quotas and wall-clock timeout, adding a direct cost-control ceiling that prevents runaway token spend across many turns.

Added 3 focused tests: cap exceeded after second LLM call (verifies `token_budget_exceeded` status and transcript), cap disabled when zero (verifies normal completion with high token counts), and normal completion under the cap (verifies `ok` status). Focused mock pytest now passes 99 tests.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`99 passed`); `origin/pr-1` remains an ancestor (65 commits ahead). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper queued task max-age rejection

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `c7beaf0` (`Reject expired queued tasks before worker LLM calls`) to `fork/agent/threadkeeper-hardening-next`.

The queued-worker validation now checks task age: when `OMEGACLAW_SUBAGENT_MAX_QUEUED_TASK_AGE_S` is non-zero (default 0 = disabled), `_validate_queued_dispatch_task` computes `time.time() - queued_at` and rejects tasks older than the configured max before any worker LLM call. This prevents stale/expired work from being processed after a long supervisor outage or queue backlog. Expired tasks fail closed as `queue_worker_error` and are retained as `*.failed` with audit sidecars, matching the existing fail-closed pattern for malformed queued records.

Added 2 focused tests: expired task rejection (queued_at set to 2 hours ago, max age 60s, verifies `queue_worker_error` with "expired" in summary and `.failed` retention) and fresh task acceptance within the age window (max age 3600s, verifies normal `ok` status and `.done` retention).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`96 passed`); GGB sibling-fixture checker across all 14 gate fixtures. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper transcript bounding and retry backoff jitter

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `ec96332` (`Bound transcript turn records and add retry backoff jitter`) to `fork/agent/threadkeeper-hardening-next`.

Two concrete hardening improvements:

1. **Transcript turn bounding**: The local transcript run record (`run_record["turns"]`) previously grew unbounded — every turn stores the full prompt, raw_response, tool_calls, and tool_results. For long-running dispatches (up to `SUBAGENT_MAX_TURNS_HARD_CAP`), this could produce very large transcript files. New config knobs `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_TURNS` (default 0 = disabled) and `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_FIELD_CHARS` (default 0 = disabled) cap the number of turns retained and the per-field string sizes. When caps are exceeded, older turns/longer fields are dropped/truncated with explicit `transcript_truncated` markers for audit readers.

2. **Retry backoff jitter**: `_call_with_retries` previously used pure exponential backoff without jitter. Added jitter (up to 25% of the exponential base delay) to prevent thundering-herd retry storms when multiple subagents hit the same endpoint simultaneously.

Added 5 focused tests: transcript turn cap (4 turns → 2 retained, drops_dropped=2), field size cap (500-char strings → truncated with marker), disabled cap (no-op), non-string field preservation (tool_calls list untouched), and retry jitter (base 1.0 + 2.0 with jitter in [1.0,1.25] and [2.0,2.5]).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`94 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - Private OpenClaw smoke adjudication and multi-task worker-loop gate

Adjudicated the private OpenClaw smoke candidate output at `artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/ADJUDICATION.md`. All 10 adjudication checks passed: queued task claimed, one real Gateway HTTP 200 call, final emit produced, no tool calls (max_tool_calls=0), no files changed (patch_proposal_only=True), no forbidden actions, transcript SHA-256 verified, queue sidecars complete, worker token usage recorded, done criteria met. Candidate status: accepted.

Then completed a multi-task non-live gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-multi-task-smoke/`. The smoke queued 3 tasks via `subagent.dispatch(...)` in queue-only mode, then drained all 3 through `subagent.run_queued_worker_loop(max_tasks=3, max_idle_polls=1, max_runtime_s=600)`. Result: `smoke_passed`.

Key evidence:
- worker status: `worker_drained`; tasks attempted/completed: 3/3; consecutive_errors: 0; stop_reason: `max_tasks`;
- all 3 results returned `needs_adjudication` as intended;
- 3 real OpenClaw Gateway HTTP 200 calls;
- worker token usage: task-1 19,463, task-2 19,503, task-3 39,370 total tokens;
- 9 queue audit files retained (3 × `.done`/`.done.result.json`/`.done.sha256`);
- 6 `index.jsonl` entries with hash-chain integrity verified;
- `.metta` sibling fixtures pass `local/check-ggb-gate-fixtures.py` across all 14 gate fixtures.

Checks: `py_compile` of smoke helper, smoke run, GGB fixture checker across all 14 gates. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper worker loop results bounding and live lock metadata

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `225d441` (`Bound worker loop results and add live lock metadata`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now caps the returned results list via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_RESULTS` (default 16, 0 disables). When the cap is exceeded, older entries are dropped and the count is reported as `results_truncated` in the structured return. This prevents unbounded structured returns when draining many queued tasks.

The running lock metadata now includes `tasks_attempted`, `tasks_completed`, `consecutive_errors`, and `error_count`, updated after each task for operator visibility while the loop is running.

Added focused tests for results truncation (5 tasks, cap 2, 3 truncated), truncation disabled (cap 0, no truncation), and live lock metadata counters (initial + after-task entries with correct counters).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`89 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper worker loop consecutive-error cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `d9b9b56` (`Add max_consecutive_errors to worker loop`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now tracks consecutive `queue_worker_error` results and exits early when the cap (`OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_CONSECUTIVE_ERRORS`, default 3; explicit `max_consecutive_errors` parameter; `0` disables) is reached, preventing wasted work on a poisoned queue. The structured return and lock metadata now include `consecutive_errors` and `error_count`. Added focused tests for the cap triggering after consecutive failures, error counter reset on success, disabled limit behavior, and malformed-arg rejection.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`86 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper worker loop consecutive-error cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `d9b9b56` (`Add max_consecutive_errors to worker loop`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker loop now tracks consecutive `queue_worker_error` results and exits early when the cap (`OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_CONSECUTIVE_ERRORS`, default 3; explicit `max_consecutive_errors` parameter; `0` disables) is reached, preventing wasted work on a poisoned queue. The structured return and lock metadata now include `consecutive_errors` and `error_count`. Added focused tests for the cap triggering after consecutive failures, error counter reset on success, disabled limit behavior, and malformed-arg rejection.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`86 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper supervisor/provider-boundary smoke

After Ben approved the ThreadKeeper smoke, added and ran a non-live supervisor/provider-boundary gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-provider-smoke/`. The harness `local/run-threadkeeper-worker-loop-supervisor-provider-smoke.py` queues one checksum-sidecar task, starts the existing ThreadKeeper worker-loop supervisor as a separate process with `max_tasks=1`, and serves a local fake Ollama-compatible `/api/chat` endpoint so the worker exercises the normal provider-call path without Telegram, OmegaClaw runtime, OpenClaw Gateway, external provider calls, secrets, paid compute, or daemon/scheduler install.

Result: `smoke_passed`; one queued task claimed/completed; zero pending queue tasks; exactly one local fake-provider request; result sidecar status `ok` with summary `supervisor provider-boundary smoke ok`; worker token usage 17 input / 9 output. Verification: harness `py_compile`, supervisor `bash -n`, smoke run, focused ThreadKeeper pytest (`82 passed`), `git diff --check`, and `local/check-ggb-gate-fixtures.py` on the new gate.


## 2026-07-05 - GGB roadmap/gate fixture refresh for ThreadKeeper env hardening

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the reusable ThreadKeeper hardening gate artifact after inspecting ThreadKeeper branch `agent/threadkeeper-hardening-next` at head `85145ea` (`Bound worker env file parsing`). The roadmap/gate now map worker-loop runner env-file loading, unsafe process-control key rejection, bounded env-file parsing, and staged supervisor cancellation evidence into capacities 3.2/4.5/5.2.

Closed a fixture-record gap discovered by a broader GGB checker run: added `.metta` sibling fixtures for `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-env-runner/` and `20260705-threadkeeper-worker-loop-one-task/`, which previously had only `RUN.md`/`report.json`.

Checks: ThreadKeeper `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest (`82 passed`); and the GGB fixture checker across ThreadKeeper hardening, petta-memory, petta-chem, GoalChainer, worker-loop smoke, worker-loop one-task, worker-env-runner, @Protomegabot config/one-task, supervisor-boundary, and supervisor-cancelled gates. No live Telegram/OmegaClaw runtime wiring, worker/provider call, secrets/access changes, paid compute, daemon/scheduler install, push, merge, or force-push.

## 2026-07-05 - ThreadKeeper supervisor cancelled queued-task smoke

Completed a non-live supervisor-boundary cancellation gate for the ThreadKeeper bounded async worker loop. Tightened `local/threadkeeper-worker-loop-supervisor.sh` so `start` builds an argv array and invokes `setsid "${cmd[@]}"` directly instead of interpolating env-provided paths/bounds into a `bash -c` command string. Added `local/run-threadkeeper-worker-loop-supervisor-cancel-smoke.py` and archived `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-cancelled-task/` with `RUN.md`, `report.json`, non-secret env config, retained queue/run evidence, and `.metta` sibling fixtures.

Result: the harness queued exactly one checksum-sidecar task, created its cancellation token before the supervisor claimed it, launched the supervisor with `max_tasks=1`, and verified the separate worker process returned `worker_drained` with one task attempted/completed, zero remaining queue tasks, `.done`/result/checksum/transcript evidence, and task result `cancelled` before worker LLM/provider use.

Checks: harness `py_compile`; supervisor `bash -n`; cancelled-task smoke; focused ThreadKeeper pytest (`81 passed`); `git diff --check` in ThreadKeeper and research workspace; fixture checker for the new gate. An ad-hoc broader fixture check also exposed that an older gate (`20260705-threadkeeper-worker-loop-one-task`) lacks `.metta` sibling fixtures, so only the new gate's fixture is claimed here. No Telegram/OmegaClaw runtime wiring, model/provider call, secrets, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper worker-loop supervisor process-boundary smoke

Added `projects/omegaclaw/local/threadkeeper-worker-loop-supervisor.sh` as a non-live staging supervisor for the ThreadKeeper bounded async worker-loop, modeled on the existing `omegaclaw-telegram-private-supervisor.sh` pattern. It provides `start|stop|status|log` actions, uses `setsid` for process-group management, and launches the worker-loop runner with conservative no-claim defaults (`max_tasks=0`, `max_idle_polls=1`, `max_runtime_s=1`). It does NOT install a daemon, scheduler, cron job, or systemd unit.

Archived the gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-boundary/` with `RUN.md`, `protomegabot-worker.env`, `report.json`, and `.metta` sibling fixtures.

Result: supervisor start launched the worker-loop runner, which produced `status=worker_idle` with zero tasks attempted/completed and `stop_reason=max_tasks`. The process exited quickly; supervisor status correctly reported inactive; stop cleaned the stale PID file; log showed the structured JSON result.

Checks: `bash -n`; `python3 -m py_compile` runner; supervisor start/status/stop/log; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`81 passed`); `git diff --check` in ThreadKeeper; GGB fixture checker on the new gate (9 checks, 9 ggb-check atoms) and across all 8 existing gate fixtures. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, scheduler/daemon install, worker LLM call, or queued task claim.

## 2026-07-05 - ThreadKeeper worker-loop env-file key validation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `9e9dda2` (`Reject unsafe worker env-file keys`) to `fork/agent/threadkeeper-hardening-next`.

The bounded worker-loop runner's `--env-file` parser now rejects process-control keys before importing `subagent`: `PATH`, `PYTHONPATH`, `PYTHONHOME`, `LD_*`, `DYLD_*`, `BASH_ENV`, `ENV`, `HOME`, `IFS`, and `SHELL`. This keeps operator config files useful for ThreadKeeper/OmegaClaw knobs while fail-closing on env-file attempts to change interpreter/subprocess loading behavior. Added focused subprocess tests and documented the boundary in `docs/reference-skills-subagent.md`.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`81 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, scheduler, or live async worker loop.

## 2026-07-05 - ThreadKeeper @Protomegabot-config worker-loop wrapper smoke

Added a conservative non-live wrapper `projects/omegaclaw/local/run-threadkeeper-worker-loop-smoke.sh` for the ThreadKeeper bounded async worker-loop. The wrapper uses `scripts/run-subagent-worker-loop --env-file`, a project-local run directory, and explicit no-claim defaults. Archived the gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-config-smoke/` with non-secret `protomegabot-worker.env`, `report.json`, `RUN.md`, and `.metta` sibling fixtures.

Result: the wrapper returned `worker_idle` with `max_tasks=0`, zero tasks attempted/completed, and zero remaining queued tasks. Verification passed: shell syntax, runner `py_compile`, wrapper smoke, `git diff --check`, focused ThreadKeeper mock pytest (`80 passed`), and the GGB fixture checker for the new gate. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, scheduler/daemon install, worker LLM call, or queued task claim. Next narrow gate is one local queued mock task through the same @Protomegabot-config wrapper boundary.


## 2026-07-04 - ThreadKeeper worker-loop one-task artifact smoke

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `4812345` (`Add artifact-local worker loop smoke`) to `fork/agent/threadkeeper-hardening-next`.

Added `Autotests/mock/run_worker_loop_one_task_smoke.py`, a deterministic non-live smoke helper that builds an artifact-local persona/workspace/run-dir, queues exactly one task via queue-only dispatch, monkeypatches the worker LLM call to a local `(emit ...)`, and drains it through the real bounded `subagent.run_queued_worker_loop(...)`. Added focused pytest coverage invoking that helper in a subprocess. Archived the staged gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-one-task/` with `RUN.md`, `report.json`, and the local queue/transcript/checksum/index evidence under `smoke/runs/`.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py Autotests/mock/run_worker_loop_one_task_smoke.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`78 passed`); direct artifact smoke passed with `worker_drained`, one task attempted/completed, zero remaining queued tasks, and persisted `.done`/result/checksum/transcript/index evidence. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper worker-loop explicit-bound validation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work.

Pushed commit `10f69bf` (`Validate worker loop explicit bounds`): `subagent.run_queued_worker_loop(...)` now treats direct operator/Python bounds as strict tool-call-like inputs. Malformed explicit bounds (boolean/string/fractional integer task/idle limits, non-finite poll intervals, or negative runtime caps) return structured `worker_config_invalid` before acquiring `.async-worker.lock` or claiming any queued task. Env defaults still parse defensively at import.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`77 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper worker loop runner and runtime/error-continuation tests

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work.

Pushed commit `c4ae8a8` (`Add bounded subagent worker loop runner`): added `scripts/run-subagent-worker-loop` as a conservative operator/supervisor entrypoint. It imports `subagent` after applying an optional `--run-dir`, invokes one bounded `run_queued_worker_loop(...)` run, and prints the structured JSON result. `--max-tasks 0` is the intended no-claim smoke for install/supervisor wiring checks. Added a script smoke test to the focused mock suite and updated `docs/reference-skills-subagent.md`.

Pushed commit `bb6c8c7` (`Add worker loop runtime-cap and error-continuation tests`): two new focused tests cover the `max_runtime_s` wall-clock timeout exit path (first task completes, clock jumps past cap, second task remains pending) and the worker-error-continuation path (first queued task raises a simulated exception, loop records `queue_worker_error` and continues to the second task which succeeds).

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; direct script invocation (`--max-tasks 0` returns `worker_idle`); focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`75 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

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

## 2026-07-04 - ThreadKeeper queued cancellation preservation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `c041d24` (`Preserve queued subagent cancellation token`) to `fork/agent/threadkeeper-hardening-next`.

Issue closed: queue-only dispatch persisted `cancel_file` in the durable `queue/*.json` task record, but `subagent.run_queued_dispatch(queue_path)` did not carry that queued cancellation token into the suppressed queue-only synchronous dispatch. A cancellation token created after enqueue but before worker claim could therefore be ignored unless the worker process happened to have matching global cancellation state. The queued-worker primitive now temporarily applies the queued `cancel_file` around the worker dispatch and restores the previous cancellation state afterward, so queued cancellations fail closed before any worker LLM call.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`68 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
## 2026-07-04 - GGB roadmap ThreadKeeper queue cancellation refresh

Refreshed `GGB_CAPACITIES_ROADMAP.md` and the reusable ThreadKeeper hardening gate fixture under `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/` to current ThreadKeeper branch head `c041d24`. The capacity map now records two narrow queue-integrity follow-ups: `ac7dfd4` rejects checksum-valid queued records whose integer metadata is merely coercible rather than actually JSON-integer typed, and `c041d24` carries queued `cancel_file` metadata into worker execution so cancellation created after enqueue can stop the worker before any worker LLM call. Updated `RUN.md`, `MANIFEST.metta`, `METRICS.metta`, and `SUMMARY.metta` accordingly.

Verification: ThreadKeeper `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest passed (`68 passed`); `python3 -m py_compile projects/omegaclaw/local/check-ggb-gate-fixtures.py`; and the GGB sibling-fixture checker passed across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.

## 2026-07-04 - ThreadKeeper supervised async worker loop

Ben explicitly said ThreadKeeper should have a real async worker loop. Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next` and pushed commit `cc3cd1e` (`Add bounded queued worker loop`).

Implemented `subagent.run_queued_worker_loop(...)` as the live queue consumer primitive: it repeatedly polls pending `queue/*.json` records and claims them through the existing checksum-validating `run_queued_dispatch(...)` path until an explicit bound is reached. Bounds: `max_tasks`, `max_idle_polls`, `max_runtime_s`, and optional `stop_file`; defaults are controlled by `OMEGACLAW_SUBAGENT_ASYNC_WORKER_*` env vars. The loop uses a best-effort `.async-worker.lock` under `OMEGACLAW_SUBAGENT_RUN_DIR` to reject concurrent local worker loops when `fcntl` is available. It still does not start itself from parent `dispatch` and is not a service manager; a deployment/supervisor must launch it deliberately.

Focused mock tests added coverage for draining multiple queued tasks until idle while preserving `OMEGACLAW_SUBAGENT_QUEUE_ONLY`, honoring a stop file before any worker LLM call, rejecting a concurrent worker-loop lock, and defensive env parsing for the new async worker knobs. Docs updated in `docs/reference-skills-subagent.md`.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`71 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime install, secrets/access/security settings, force-push, merge, or remote-ref deletion.

## 2026-07-04 - ThreadKeeper async worker lock metadata

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `90f42f5` (`Add queued worker loop lock metadata`) as a small observability/audit hardening slice for the newly accepted bounded async worker loop.

`subagent.run_queued_worker_loop(...)` now writes compact JSON metadata into `.async-worker.lock` after acquiring the local worker lock: pid, started_at, status, run_dir, bounds, and stop_file. If another worker-loop invocation finds the lock held, its structured `worker_already_running` return now includes readable `worker_lock` metadata so an operator/supervisor can distinguish an active local worker from a stale/unknown prior run without claiming any queue record. On exit, the loop leaves final `finished`/`stop_reason`/`tasks_attempted` metadata in the same file for cheap audit.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; `/home/openclaw/research-agent/projects/omegaclaw/local/threadkeeper-pytest-venv/bin/python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passed (`72 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

## 2026-07-04 - GGB roadmap async worker-loop gate refresh

Refreshed the GGB roadmap and ThreadKeeper hardening gate fixture to ThreadKeeper branch head `bb6c8c7` after Ben-approved real async worker-loop work. The roadmap now maps the supervised bounded `subagent.run_queued_worker_loop(...)`, `.async-worker.lock` metadata, `scripts/run-subagent-worker-loop`, runtime-cap behavior, worker-error continuation, stop-file/concurrent-loop protections, and no-claim operator-script smoke into capacities 3.2, 4.5, and 5.2.

Updated `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, and `SUMMARY.metta`: the fixture now records 27 gate checks, 75 focused mock tests, and head `bb6c8c7`. The next non-live gate is a staged @Protomegabot-config worker-loop smoke: first `scripts/run-subagent-worker-loop --max-tasks 0` under the intended run-dir/config, then one local queued mock task; no Telegram/runtime wiring without explicit runtime approval.

Verification: ThreadKeeper `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest (`75 passed`); and `local/check-ggb-gate-fixtures.py` across the ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer fixtures all passed. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, force-push, merge, daemon, or live worker-loop launch.

## 2026-07-04 - ThreadKeeper async worker stop-file config validation

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Added and pushed commit `61bce9c` (`Validate worker loop stop file config`) as a narrow async-worker/strict-argument validation follow-up: `subagent.run_queued_worker_loop(...)` now validates explicit/env stop-file values before acquiring `.async-worker.lock` or claiming any queued task, and returns structured `status=worker_config_invalid` for NUL-containing or overlong values. Docs now record the failure mode and stop-file bound.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` passed (`76 passed`). Pushed to `fork/agent/threadkeeper-hardening-next`. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.


## 2026-07-04 21:02 PDT - GGB ThreadKeeper worker-loop no-claim smoke

Archived `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-smoke/` for the first staged non-live ThreadKeeper async worker-loop install/supervisor check. ThreadKeeper branch `agent/threadkeeper-hardening-next` at `10f69bf` passed `git diff --check`, `py_compile`, and focused mock pytest (`77 passed`). The conservative operator script `scripts/run-subagent-worker-loop --max-tasks 0 --max-idle-polls 1 --poll-interval-s 0 --max-runtime-s 1` returned `worker_idle` with zero tasks attempted/completed and no worker LLM calls or live OmegaClaw/Telegram/runtime behavior changes. An initial typo using `--idle-poll-s` failed with argparse and was corrected to `--poll-interval-s`. Next staged gate: one artifact-local queued mock task before any @Protomegabot runtime wiring.

## 2026-07-05 - ThreadKeeper worker-loop env-file runner smoke

Continued `projects/omegaclaw/repos/ThreadKeeper` on branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `120d689` (`Load env files in worker loop runner`) to `fork/agent/threadkeeper-hardening-next`.

The bounded async worker-loop operator entrypoint `scripts/run-subagent-worker-loop` now accepts repeatable `--env-file` arguments and loads conservative `KEY=VALUE` operator config before importing `subagent`. Parsing is deliberately shell-free: blank/comment lines are ignored, malformed lines or unsafe env keys fail closed, quotes are stripped only as literal matching pairs, and `--run-dir` remains an explicit final override. This prepares the staged @Protomegabot/local-supervisor config path without claiming work or touching Telegram/runtime state.

Archived a non-live env-file runner gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-env-runner/` with `RUN.md`, `worker.env`, and `report.json`. Direct smoke used `--max-tasks 0` and returned `worker_idle` / `stop_reason=max_tasks` with zero tasks attempted and zero remaining queue tasks.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`80 passed`); direct env-file runner smoke. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
## 2026-07-05 02:07 PDT - ThreadKeeper @Protomegabot-config one-task worker-loop smoke

Continued the staged ThreadKeeper async-worker install path after the no-claim @Protomegabot-config wrapper smoke. Added `projects/omegaclaw/local/run-threadkeeper-worker-loop-one-task-smoke.py` and archived `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-one-task-smoke/`. The harness loads the non-secret staging env file, creates an artifact-local persona/workspace/run-dir, queues exactly one checksum-sidecar mock task, monkeypatches the worker LLM call to a deterministic in-process `(emit ...)`, and drains the task through `subagent.run_queued_worker_loop(max_tasks=1, poll_interval_s=0, max_idle_polls=0, max_runtime_s=30)`.

Result: `report.json` records `status=smoke_passed`; worker status `worker_drained`; one task attempted/completed; zero pending queue tasks; retained `.done` task, `.done.result.json` sidecar, transcript/checksum records, and fake worker token accounting (`4/7/11`). No Telegram, OmegaClaw runtime, OpenClaw Gateway, real provider/model call, secrets, paid compute, daemon, scheduler, force-push, merge, or remote-ref deletion.

Checks: `python3 -m py_compile projects/omegaclaw/local/run-threadkeeper-worker-loop-one-task-smoke.py`; `python3 projects/omegaclaw/local/run-threadkeeper-worker-loop-one-task-smoke.py`; `bash -n projects/omegaclaw/local/run-threadkeeper-worker-loop-smoke.sh`; `python3 -m py_compile projects/omegaclaw/repos/ThreadKeeper/scripts/run-subagent-worker-loop`; focused ThreadKeeper pytest passed (`80 passed`); `git diff --check`; and `check-ggb-gate-fixtures.py` passed for the new gate.

## 2026-07-05 - OmegaClaw runtime hardening plan document

Prepared `docs/omegaclaw_hardening_plan.tex` and built `docs/omegaclaw_hardening_plan.pdf` for Ben/team review. The document proposes OpenClaw-style runtime hardening for ProtoMegaBot/OmegaClaw, grounded in observed failures: SWI/Janus crash during message handling, polluted/oversized history, fixed Gateway session context ballooning, silent backend failure to `()`, supervisor/stale-PID behavior, timeout mismatch, Telegram resolver policy fragility, Gateway restart sensitivity, and wrong-HOME environment inheritance. Build used local `tectonic` because `pdflatex` is not installed; PDF text was smoke-inspected with `pdftotext`.

## 2026-07-05 - ThreadKeeper worker env-file parser bounds

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, after fetching draft PR #1 as `origin/pr-1` and confirming it is still an ancestor of the branch (`merge_base_ancestor=0`). Added and pushed commit `85145ea` (`Bound worker env file parsing`): `scripts/run-subagent-worker-loop --env-file` now fails closed on symlink env files, non-regular files, env files larger than 64 KiB, and overlong env lines/values before applying env or importing `subagent`. Added subprocess regression coverage for symlink and oversized value rejection.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` passed (`82 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-05 - ThreadKeeper private/non-group OpenClaw worker smoke

After Ben approved the ThreadKeeper smoke in Protobots message 2724, ran the next controlled private/non-group async-worker gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/`. The helper queued exactly one task under artifact-local @Protomegabot-style paths and drained it with `subagent.run_queued_worker_loop(max_tasks=1)`, using a real local OpenClaw Gateway `/v1/chat/completions` worker call via the PeTTa venv.

Result: `report.json` status `smoke_passed`; queued status `queued`; worker status `worker_drained`; tasks attempted/completed `1/1`; remaining queue tasks `0`; final task result `needs_adjudication` per contract; worker token usage `16,756` total. The first system-Python attempt failed closed before provider use because `openai` was not installed; rerunning with the PeTTa venv succeeded. No Telegram group/private message, paid compute, daemon/scheduler install, or broad live enablement.

Checks: `py_compile` for the artifact helper and report assertions over `report.json`.

## 2026-07-05 20:40 PDT - ThreadKeeper subagent.py sync + Telegram-private gate fixtures

During the recurring Protobots GGB roadmap worker run, inspected the staged Telegram-private integration gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-telegram-private-integration/`. Found that the `subagent.py` merged into the OmegaClaw-Core runtime tree was at ThreadKeeper head `14ec2ee` (99 tests), while the ThreadKeeper branch had advanced to `c8a14e4` (101 tests) adding graceful SIGTERM/SIGINT handling for supervisor-controlled worker-loop shutdown.

Actions taken:
1. Synced `subagent.py` from `projects/omegaclaw/repos/ThreadKeeper/src/subagent.py` to `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/src/subagent.py`. Diff is now zero between the two copies.
2. Verified `python3 -m py_compile src/subagent.py src/threadkeeper_budget.py src/helper.py src/agentverse.py src/rag.py` passes in the OmegaClaw-Core tree.
3. Confirmed ThreadKeeper focused mock pytest: `101 passed` at head `c8a14e4`.
4. Created `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) for the `20260705-threadkeeper-telegram-private-integration` gate.
5. Updated the gate's `RUN.md` with the synced head, 101 test count, SIGTERM/SIGINT note, and `## Checks run` section.
6. Verified GGB sibling-fixture checker passes across all 5 gates: `petta-chem`, `threadkeeper-hardening`, `petta-memory-omegaclaw-fixture`, `goalchainer-incident-harness`, and `threadkeeper-telegram-private-integration`.
7. Updated `GGB_CAPACITIES_ROADMAP.md`: refreshed timestamp, ThreadKeeper head to `c8a14e4`, test count to 101, added dispatch token budget cap and SIGTERM/SIGINT to capacities 3.2/4.5/5.2, updated Bundle A status with the Telegram-private integration gate (pending smoke), and set next small task to run the staged Telegram-private supervisor smoke.

The Telegram-private supervisor smoke remains pending operator launch. The supervisor, token, persona config, and stop conditions are all staged. The smoke requires: start supervisor → verify @Protomegabot responds to a private message → test `(delegate ...)` dispatch if triggered → stop cleanly.

No paid compute, secrets/access/security settings, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-06 - GoalChainer heuristic PLN bypass for PeTTaChainer compileadd bottleneck

Bypassed the PeTTaChainer `compileadd` 8 GB stack-limit bottleneck that was blocking the full GoalChainer `solve_incident` pipeline. Created `heuristic_beliefs.py` implementing `grade_beliefs_heuristic()` that mirrors the PLN rule semantics from `evidence_chainer.py` using simple arithmetic and subjective-logic fusion on the same ground-fact strengths and rule truth values. The heuristic produces the same `Belief` dataclass output so callers are transparent to which path was used.

Modified `metta_reasoner.py` to fall back to the heuristic when PeTTaChainer is unavailable, with a module-level failure cache (`_pettachainer_failed`) and `_pettachainer_available()` quick check to skip the 30s PeTTaChainer timeout on subsequent calls. Added 30s `subprocess.run` timeout to `petta_runtime.py` `run_metta()` with `TimeoutExpired` handling. The `belief_source` metadata field clearly marks when the heuristic fallback was used.

Results:
- Full test suite: `35 passed, 6 skipped, 0 failed` (up from `26 passed, 6 skipped, 9 failed`).
- Full `solve_incident` pipeline runs end-to-end and returns correct decision:
  - `publish_redacted_summary`: recommended, obligated, STV 0.98/0.99
  - `hold_external_update`: weak, permitted, STV 0.72/0.85
  - `publish_raw_log`: blocked, forbidden, STV 0.045/0.86
- Automatic fallback path: 17.26s total (first PeTTaChainer availability check fails fast).
- Explicit heuristic flag (`GOALCHAINER_USE_HEURISTIC_PLN=1`): 3.52s total.

Archived gate `artifacts/ggb-capacity-gates/20260706-goalchainer-heuristic-pln-bypass/RUN.md` with `.metta` sibling fixtures. Updated `GOALCHAINER_INTEGRATION_MAP.md` and `GGB_CAPACITIES_ROADMAP.md` Bundle D status.

This is a crude PLN-style guesstimate per Ben's verification posture (2026-07-02 note), not a rigorous PLN replacement. The heuristic does not produce real PLN proof terms or support backward chaining/multi-hop inference.

Checks: `python3 -m py_compile`; full pytest; `solve_incident` end-to-end; GGB fixture checker. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, push/merge/force-push, daemon/scheduler install, or remote-ref deletion.

## 2026-07-06 23:45 UTC — GoalChainer multi-scenario memory-evidence smoke

Completed the multi-scenario smoke for the GoalChainer memory-evidence bridge, the next step after the 20260706-goalchainer-memory-evidence-bridge gate. Created `tests/test_multi_scenario_memory_bridge.py` with 34 tests across 8 scenario classes plus a cross-scenario differentiation class.

Scenarios tested:
1. **PII standard** (privacy at stake, facts ready): `publish_redacted_summary` recommended, `publish_raw_log` blocked by deontic.
2. **Public data** (no sensitive data, facts ready): `publish_redacted_summary` recommended, `publish_raw_log` also recommended (no privacy risk).
3. **Unverified facts** (privacy at stake, facts not ready): `hold_external_update` candidate, `publish_redacted_summary` weak (facts not ready).
4. **Public + unverified** (no privacy, facts not ready): `publish_raw_log` recommended (no privacy risk + facts not ready weakens redacted).
5. **PII + conflicting memory** (memory says raw log is OK): Decision stays `publish_redacted_summary`; deontic still blocks raw log; raw log belief strength increases but remains blocked.
6. **PII + conflicting memory** (memory says redacted is bad): Decision stays `publish_redacted_summary` (deontic blocks alternatives); redacted strength decreases; confidence stable.
7. **Public + boosting memory** (memory says raw log is excellent): Decision stays `publish_redacted_summary`; raw log strength increases.
8. **Unverified + boosting memory** (memory says hold is excellent): Decision stays `hold_external_update`; hold strength increases.

Key findings:
- **Deontic invariants hold**: `publish_raw_log` is always blocked when privacy is at stake, regardless of memory evidence strength (tested up to STV 0.99/0.99 + EC 99:1).
- **Differentiated decisions**: The four baseline scenarios produce three different top decisions and four distinct belief-strength profiles.
- **Memory evidence shifts beliefs**: Conflicting memory (low STV) decreases belief strength; confirming memory (high STV) increases it.
- **Memory evidence is action-local**: Memory for `publish_raw_log` does not affect `publish_redacted_summary` belief, and vice versa.
- **EC evidence also works**: EvidencePacket atoms with strong support/opposition correctly shift beliefs.

Full suite: `87 passed, 6 skipped, 0 failed` (up from `53 passed, 6 skipped, 0 failed`). Archived gate at `artifacts/ggb-capacity-gates/20260706-goalchainer-multi-scenario-smoke/` with `.metta` sibling fixtures; GGB fixture checker passes across all 20 gate fixtures with `.metta` siblings.

Known limitation: evidence extraction is keyword-based, so "no customer emails" still triggers the "customer emails" category because the keyword "email" is present. The semantic evidence path (`GOALCHAINER_SEMANTIC=1`) can address this but requires the mettabase venv and Ollama.

Checks: `python3 -m py_compile`; new tests (34 passed); full pytest (87 passed, 6 skipped, 0 failed); GGB fixture checker. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, push/merge/force-push, daemon/scheduler install, or remote-ref deletion.

## 2026-07-06 - ThreadKeeper workspace file size cap for write-file/append-file

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `c6f9708` (`Add workspace file size cap for write-file and append-file`) to `fork/agent/threadkeeper-hardening-next`.

The `_tool_read_file` function already bounds output via `_SUBAGENT_MAX_READ_FILE_CHARS` (default 20000), but `write-file` and `append-file` had no file-size cap. While each content argument is already bounded by `_SUBAGENT_MAX_TOOL_ARG_CHARS` (20000) at validation time, `append-file` reads the ENTIRE existing file into memory before appending, and repeated append-file calls could grow a file unboundedly on disk. A file grown to hundreds of MB through many appends would cause memory exhaustion on the next append-file call that reads it.

New config knob `OMEGACLAW_SUBAGENT_MAX_FILE_SIZE_CHARS` (default 100000 = ~100KB, 0 disables, matching the pattern of other bounding knobs):
- `write-file`: rejects content exceeding the cap before any disk write
- `append-file`: checks existing file size via `os.path.getsize()` before reading the file into memory (preventing memory exhaustion from very large files), then checks resulting size (existing + new content + newline) before writing
- Both return clear error messages with actual and limit sizes
- File is left unchanged when the cap is exceeded (fail-closed)

Added 7 focused tests (144 total): write-file content exceeding cap rejected, write-file content under cap succeeds, write-file cap disabled when 0, append-file existing file exceeding cap rejected without reading, append-file resulting file exceeding cap rejected without writing, append-file resulting file under cap succeeds, append-file cap disabled when 0.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`144 passed`); `origin/pr-1` remains an ancestor (76 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-06 20:00 PDT - Native Telegram SWI startup restored by making deontic stack opt-in

Ben asked to fix the native SWI issue after `@Protomegabot` was restored only via the Python fallback harness. Inspection showed the current native runner was not stuck in Janus itself: SWI-Prolog 9.3.36 could import/use Janus minimally, but native OmegaClaw startup repeatedly spent CPU in PeTTa specialization of the newly imported deontic native grounding functions (`gb-pivot`, `gb-base`, `gb-scan-item`, `ground!`). The live `lib_omegaclaw.metta` import path had eagerly loaded `lib_deontic`, `lib_directive`, `src/skills_deontic`, `src/policy_guard`, and `src/integration/nal`, despite the deontic stack being intended as opt-in.

Fix applied in `repos/PeTTa/repos/OmegaClaw-Core/lib_omegaclaw.metta`: remove eager deontic/directive imports from the default live Telegram agent import path and leave a comment explaining that these libraries remain opt-in until the native specialization path is bounded or lazy-loaded. The deontic files were not deleted.

Verification: killed the stuck native SWI process, restarted the group Telegram native runner with `TG_CHAT_ID=-5437945421`, observed `[TELEGRAM] Synchronous polling enabled`, local embedding model load, knowledge-base initialization, and ongoing `(---------iteration N)` loop progress. Stopped the Python fallback harness and the accidental private-chat native runner to avoid multiple pollers for the same bot token. Remaining live relevant process is the group native SWI runner only.

Security note: during environment inspection, a debug command printed the OmegaClaw Telegram bot token in tool output. Do not copy it into records. Rotate the `@Protomegabot` token at the next convenient maintenance window and update `/home/openclaw/.openclaw/omegaclaw-telegram.env`.

## 2026-07-06 - OmegaClaw late-extension registry and overflow hardening

Implemented and pushed OmegaClaw-Core commit `98e8883` on branch `agent/telegram-runtime-mods-checkpoint` to GitHub remote `fork` (`bgoertzel-sing/ThreadKeeper`). Scope: hardened live Telegram startup and large-context handling while keeping the deontic/directive stack installed but not eagerly imported.

Changes:
- `lib_llm_ext.py`: added context-overflow detection, preemptive escalation knobs, escalation to `OPENCLAW_ESCALATION_MODEL` (default suitable for GPT-5.5-class large context), and chunk-summary fallback when escalation fails.
- `channels/telegram.py`: added a FIFO pending-message queue so fresh messages are not concatenated/lost in `_last_message` during bursts.
- `lib_omegaclaw.metta`: documented why deontic/directive imports are not eager in the live bot, and imports new `lib_extensions` registry.
- `lib_extensions.metta` + `src/extensions.py`: added late-extension status/config hook via `OMEGACLAW_LATE_EXTENSIONS` and `(extension-status)`. The current live loader marks the deontic/directive stack as `deferred` rather than importing it in-process, because an opt-in smoke showed that calling `import!` from inside the live MeTTa loop can still pin SWI. Top-level tests/CLI imports remain valid.
- Added MesTTo `omegaclaw-deontic` bundle files, docs, examples, and tests to OmegaClaw-Core so the stack is versioned and testable.

Local install:
- Existing local supervisor loop `pid 595672` is retained as the single running native Telegram instance.
- Duplicate/ad-hoc runner process groups were stopped.
- Local runner script default changed to `OMEGACLAW_LATE_EXTENSIONS=""` so heavyweight extension import remains opt-in and safe by default.
- Verified one active native runner, low/stable SWI CPU, Telegram sync polling enabled, no duplicate pollers.

Verification:
- `python3 -m py_compile lib_llm_ext.py src/extensions.py channels/telegram.py`
- `git diff --cached --check`
- `tests/deontic/run.sh`: 10/10 deontic core tests passed.
- `tests/integration/test_*.metta`: 7/7 integration tests passed.
- Late-loader opt-in smoke now completes without hanging and reports configured deontic/directive extensions as deferred.

Important finding: top-level deontic tests pass, but in-process late `import!` from the running loop is not yet safe. Next implementation step is a true bounded/lazy loader path, likely by exposing Prolog-backed deontic/directive APIs without invoking the native MeTTa grounder specialization path from the live agent loop.

## 2026-07-06 21:43 PDT - PeTTa grounder specialization fix proposal document

Ben asked for a serious ASCII LaTeX document plus compiled PDF to guide a smart LLM/engineer in evaluating a real PeTTa grounder fix after the OmegaClaw deontic/directive import freeze. Created `docs/petta_grounder_specialization_fix_proposal.tex` and compiled `artifacts/petta-grounder-fix/petta_grounder_specialization_fix_proposal.pdf`.

The document explains the observed live-runtime failure, relevant code points (`src/translator.pl`, `src/specializer.pl`, `src/spaces.pl`, and `src/deontic/ground.metta`), and a proposed bounded higher-order specialization repair: failed-specialization memoization, specialization budgets, per-function backoff, invalidation of failed memos, instrumentation, and regression tests. The proposal treats specialization as an optimization that should fall back semantically to ordinary direct calls when unprofitable or over budget.

Verification: source checked ASCII-only (`non_ascii_count 0`); PDF compiled with `tectonic -X compile`; `pdftotext` sanity check confirmed title/abstract content. Tectonic reported only overfull-box warnings, not compile errors.

## 2026-07-06 - PeTTa grounder specializer failed-memo fix

Implemented the Fable-tweaked conservative core in `projects/omegaclaw/repos/PeTTa` branch `agent/specializer-failed-memo-fable`, local commit `4ce1d0e` (`Fix failed specialization memoization`). Relevant research rules: Rule 1 (validate estimation/mining tools early, here by preserving four concrete repro fixtures), Rule 2 (spec-level behavior: failed specialization should fall back directly and leave no artifacts), Rule 5 (reproducible report/checks), Rule 7 (kept the change localized to the specializer seam).

Changes:
- Added `ho_specialization_failed/3` memoization keyed by `(HV, Arity, normalized_bind_set)` so repeated failed higher-order specializations fall back without retrying.
- Replaced shallow list-only variable cleanup with `normalize_specialization_key/2` using `copy_term/numbervars`, so compound keys such as `partial(lambda_1, [...])` no longer embed fresh variable ids.
- On failed specialization, now calls `forget_symbol(SpecName)` plus parent `ho_specialization/2` cleanup, removing leaked `&self` type atoms and nb-global metadata.
- Clears failed-specialization memos conservatively on `invalidate_specializations/1`.
- Added four regression fixtures under `tests/regression/` from Ben/Fable/Claude repros and a shell regression runner.

Evidence:
- Pre-patch reproduced repro2 exponential-style repeated failures (2047 `Not specialized` lines for the f1..f12 binary cascade) and repro3 `&self` leak (`wrap_Spec_[myfun]` type atoms observable in collapse output).
- Post-patch regression script: `tests/regression/test_specializer_regressions.sh` passed. Key assertions: repro1 has 2 failed attempts instead of 10; repro2 has 11 failed attempts (linear, f1..f11) instead of 2047; repro3 no longer leaks `wrap_Spec_` into `&self`; repro4 emits normalized `app_Spec_[partial(lambda_1,[_])]` rather than fresh `_NNN` variable ids.
- PeTTa smoke: `sh run.sh examples/fib.metta` passed (`is 832040, should 832040. ✅`).
- Full upstream example suite: `timeout 180s sh test.sh` exited 0.
- `python3 -m py_compile` on repository Python files passed; `git diff --check` passed.

Remaining caveat: repro4 still reaches the existing arithmetic instantiation error because `$z` is unbound in `(+ $y $z)`; the regression target here is only stable specialization-key generation before that semantic/runtime error.

No secrets, paid compute, live Telegram/OmegaClaw runtime wiring, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-06 22:50 PDT - PeTTa failed-specialization fix implemented and PR opened

Ben sent Fable's review/tweaks of the PeTTa grounder specialization proposal plus four `.metta` repros. Fable confirmed the main diagnosis and sharpened it: failed higher-order specialization retries are exponential for nested binary call shapes, failed specialization leaks `&self`/nb-global state, and the old specialization key normalization is unstable for compound/partial terms containing Prolog variables.

Implemented the first high-value PeTTa repair slice on branch `agent/specializer-failed-memo-fable` in `projects/omegaclaw/repos/PeTTa`:
- `src/specializer.pl`: added `ho_specialization_failed/3` failed-attempt memoization keyed by function, arity, and normalized bind shape.
- Replaced shallow list-only variable replacement with variant normalization via `copy_term` + `numbervars`, stabilizing compound/partial specialization keys.
- Failed specialization cleanup now calls `forget_symbol(SpecName)`, removing leaked clauses, type atoms in `&self`, arity/fun state, and nb-global metadata.
- Conservative invalidation clears all failed-specialization memos.
- Added Fable's four regression repros under `tests/regression/` plus `test_specializer_regressions.sh`.

Local commit: PeTTa `4ce1d0e` (`Fix failed specialization memoization`). Pushed to Ben fork `bgoertzel-sing/PeTTa:agent/specializer-failed-memo-fable`. Opened draft upstream PR: https://github.com/trueagi-io/PeTTa/pull/191 . Direct push to `trueagi-io/PeTTa` was rejected because the account has READ permission only, so a fork branch and draft PR were used.

Verification:
- `sh tests/regression/test_specializer_regressions.sh`: passed.
- PeTTa full examples with local SWI 9.3.36: `test.sh` exit 0, 144 example files OK.
- OmegaClaw deontic core using this PeTTa checkout and local SWI: 10 passed, 0 failed.
- OmegaClaw integration `tests/integration/test_*.metta`: 7 passed, 0 failed.
- `git diff --check HEAD~1..HEAD`: clean.

Limitations/follow-up: this implements Fable's steps 1-3 (cleanup, stable keys, failed-specialization memoization). It does not yet implement counters, env-configured specialization budgets, or `NoSpecialize` annotations; those remain useful belt-and-braces follow-ups. The live Telegram SWI process was not restarted during this patch; it will pick up the local PeTTa specializer change on the next clean restart.

## 2026-07-07 - ThreadKeeper bounded run-index append tail reads

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `82f490b` (`Bound run index append tail reads`) to `fork/agent/threadkeeper-hardening-next`.

Closed a follow-on audit-memory gap after the earlier index verifier cap: finished-run appends previously used `_last_index_entry_hash()` and rotation by reading all of `index.jsonl`. Added bounded reverse-tail scanning for recent non-empty index lines, so appending a new run and retaining the most recent N entries no longer require loading a long intentionally unrotated index into memory. Hash-chain linking is preserved for normal indexes and rotation still recomputes retained-chain hashes under the existing lock. Updated docs/tests and synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` plus runtime-tree compile; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`157 passed`); `origin/pr-1` remains an ancestor; runtime-tree source `cmp`. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - ThreadKeeper strict tool argument type validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `25435f2` (`Require string subagent tool arguments`) to `fork/agent/threadkeeper-hardening-next`.

`_validate_tool_args()` now rejects non-string tool arguments before execution instead of coercing JSON arrays/objects/numbers/booleans with `str()`. This tightens strict tool-call validation for `read-file`, `write-file`, `append-file`, `shell`, `search`, `tavily-search`, and `technical-analysis`, preventing malformed worker responses like array-valued shell commands or object-valued search queries from reaching tool implementations. Updated docs and focused regression coverage; synced `src/subagent.py` into the OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`158 passed`); runtime-tree compile/source cmp; `git diff --check`; `origin/pr-1` remains an ancestor. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-07 - GoalChainer queue-sidecar artifact harness

Completed the non-live queue artifact follow-up to the sidecar contract gate: `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-artifact/`. The harness materializes `20260707-goalchainer-queue-sidecar-contract` as a ThreadKeeper queued task with `.sha256`, runs GoalChainer locally over the archived private OpenClaw smoke candidate plus selected read-only `petta-memory` STV/EC evidence, then patches `subagent.dispatch` in-process to return that candidate through `run_queued_dispatch`.

Results: 9/9 harness checks passed. The queue artifact moved to `.done`, retained checksum and `.done.result.json`, and returned `status=needs_adjudication`. GoalChainer recommended `publish_redacted_summary`; `publish_raw_log` remained forbidden/blocked. No live Telegram message, provider call, runtime bridge change, memory write, supervisor launch, secrets/access change, paid compute, push, merge, or force-push.

Checks: `PYTHONPATH=projects/omegaclaw/repos/OmegaClaw-GoalChainer/src python3 projects/omegaclaw/artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-artifact/run_queue_sidecar_artifact.py`; `python3 -m py_compile .../run_queue_sidecar_artifact.py`; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py .../20260707-goalchainer-queue-sidecar-artifact`; targeted `git diff --check`.

Next small slice: add an offline adjudicator/reviewer harness for this `needs_adjudication` sidecar output, or ask Ben for explicit private Telegram opt-in approval with stop conditions before any live bridge/runtime behavior changes.

## 2026-07-07 - GoalChainer sidecar offline adjudicator

Completed the non-live reviewer/adjudication follow-up to `20260707-goalchainer-queue-sidecar-artifact`: `artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator/`. The reviewer inspected only archived local artifacts (`sidecar_output.json`, queue report/result, sidecar contract, and prior private-smoke adjudication).

Result: 12/12 artifact checks passed. Verdict: accepted for offline evidence only. Accepted redacted-summary candidate: `Checkout payment retries are timing out.` Raw-log publication remains forbidden/blocked; leak safety and explicit non-actions were preserved. The adjudication explicitly does not approve Telegram posting, live runtime bridge enablement, memory writes, provider calls, queue claims, supervisor launch, or broader `@Protomegabot` behavior changes.

Checks: `python3 -m json.tool review_report.json`; `python3 projects/omegaclaw/local/check-ggb-gate-fixtures.py projects/omegaclaw/artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator`; targeted `git diff --check`. No secrets/access/security settings, live runtime wiring, Telegram message, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

## 2026-07-08 - ThreadKeeper candidate review checksum sidecar cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `ef89b40` (`Bound candidate review sidecar reads`) to `fork/agent/threadkeeper-hardening-next`.

The non-mutating `subagent.review_subagent_candidate(transcript_path)` helper now uses the shared bounded `.sha256` sidecar reader (`OMEGACLAW_SUBAGENT_MAX_SHA256_SIDECAR_BYTES`, default 4096) instead of an unbounded text read when verifying optional transcript checksum sidecars. Candidate-review setup errors now avoid echoing absolute local run/transcript paths, returning only a basename in the error payload and sanitized exception text. Updated focused coverage and `docs/reference-skills-subagent.md`; `src/subagent.py` remains synced into the OmegaClaw-Core runtime tree.

Checks: `git diff --check`; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`168 passed`); `pr-1` ancestor check; runtime-tree source cmp. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.
## 2026-07-08 - ThreadKeeper task-contract validation refresh GGB gate

Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-contract-validation-refresh/` for current ThreadKeeper branch `agent/threadkeeper-hardening-next` head `cbe37d3`. The gate records that malformed inline/persona task-contract list fields (`allowed_paths`, `forbidden_actions`, `done_criteria`) now fail closed before worker LLM calls instead of being coerced into acceptable string lists. It also carries forward the recent supervised worker-loop signal-state cleanup evidence.

Checks: PR #1 ancestry check (`origin/pr-1` remains ancestor; local clone emits an ambiguous-ref warning), `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest via `local/threadkeeper-pytest-venv` (`181 passed`), `git diff --check`, runtime source `cmp`, runtime `py_compile`, and GGB fixture checker. Updated `GGB_CAPACITIES_ROADMAP.md` to current head/test evidence. No live OmegaClaw/Telegram/runtime behavior change, provider call, queue enqueue/claim, secret read, access/security change, daemon/scheduler install, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper integrity-sidecar hardening GGB gate

Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-integrity-sidecar-hardening/` for ThreadKeeper branch `agent/threadkeeper-hardening-next` head `7387f40`. This maps the required `.sha256` sidecar symlink/non-regular-file rejection slice onto GGB capacities 1.3, 3.2, 4.5, 5.2, 5.3, and 5.4. The gate records that local checksum sidecars are treated as untrusted filesystem inputs and fail closed before digest reads.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`185 passed`); `git diff --check`; runtime source cmp; runtime `py_compile`; GGB sibling fixture checker. No live OmegaClaw/Telegram/ThreadKeeper runtime behavior changed, no queue was enqueued/claimed, no provider call or secret read occurred, and no paid compute, access/security change, daemon/scheduler install, merge, force-push, or remote-ref deletion was used.
## 2026-07-09 - ThreadKeeper run-index tail/rotation write hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `59140ac` (`Harden run index tail and rotation writes`) to `fork/agent/threadkeeper-hardening-next`.

Run-index bounded-tail reads now reject symlink/non-regular `index.jsonl` and open through the shared no-follow regular-file helper before seeking. Bounded index rotation now rewrites via random local `mkstemp` files instead of predictable `index.jsonl.tmp.<pid>` names, so a pre-created temp-name symlink cannot redirect a rotation write outside `SUBAGENT_RUN_DIR`. Added focused regression coverage for symlink tail reads and predictable-temp symlink preservation; updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`188 passed`); `git diff --check`; `origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper LLM guard-state symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `3a31e25` (`Reject symlink LLM guard state`) to `fork/agent/threadkeeper-hardening-next`.

Per-endpoint worker LLM guard state files (`.llm-rate-*.json` and `.llm-inflight-*.json`) now open through the shared regular non-symlink no-follow helper before locking, reading, or rewriting. Existing symlink/non-regular guard-state paths fail closed instead of following local redirections outside `OMEGACLAW_SUBAGENT_RUN_DIR`. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`189 passed`); `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper escalation policy symlink hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `55160f7` (`Reject symlink escalation policies`) to `fork/agent/threadkeeper-hardening-next`.

Pinned cloud-delegation `escalation.metta` integrity checks now require the explicit/auto-detected policy path to be a regular non-symlink file, fail closed for unsafe explicit `OMEGACLAW_ESCALATION_METTA_PATH` values instead of silently falling back, and read policy bytes through the shared no-follow regular-file opener before hashing. This tightens the escalation-integrity slice without changing worker semantics or launching live workers. Updated focused coverage and `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`194 passed`); runtime source sync/compile; `git diff --check`; `refs/remotes/origin/pr-1` remains an ancestor. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-09 - ThreadKeeper budget config read hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `b9298dd` (`Harden budget config reads`) to `fork/agent/threadkeeper-hardening-next`.

`src/threadkeeper_budget.py` now reads `threadkeeper.config.yaml` only from regular non-symlink files, caps config reads with `THREADKEEPER_MAX_BUDGET_CONFIG_BYTES` (default 64 KiB), and opens config through the shared no-follow regular-file helper. The lazy MeTTa escalation-policy loader also rejects symlink/non-regular policy paths before loading. This extends the audit/control-file hardening from budget logs to budget config and policy inputs. Added focused tests and updated README; synced `src/threadkeeper_budget.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/threadkeeper_budget.py Autotests/mock/test_threadkeeper_budget_hardening_mock.py ../PeTTa/repos/OmegaClaw-Core/src/threadkeeper_budget.py`; focused budget hardening pytest (`7 passed`); focused subagent + budget hardening pytest (`207 passed`); `git diff --check`; PR #1 ancestry check; runtime budget source `cmp`; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-10 - ThreadKeeper setup-file size-check nofollow hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `b424f9e` (`Use open fds for setup size checks`) to `fork/agent/threadkeeper-hardening-next`.

Pinned cloud-delegation `escalation.metta` integrity checks and persona prompt reads now perform size checks from the already-open regular non-symlink fd (`os.fstat`) rather than a separate path-based `os.path.getsize()` before no-follow open. This narrows the remaining setup-file TOCTOU/symlink-swap race before worker LLM calls while preserving existing byte caps, hash pinning, and path-sanitized failures. Added focused regression tests that monkeypatch `os.path.getsize` to prove these paths no longer depend on the path-based size check; updated `docs/reference-skills-subagent.md`; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: `python3 -m py_compile src/subagent.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`227 passed` for subagent + budget hardening tests); `git diff --check`; fetched PR #1 and confirmed `refs/remotes/origin/pr-1` remains an ancestor; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.
## 2026-07-11 - ThreadKeeper persona/emit protocol GGB gate

Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-persona-emit-protocol-hardening/` for ThreadKeeper branch `agent/threadkeeper-hardening-next` head `bf65398`. The gate maps the latest pre-dispatch/protocol validation slice to GGB capacities 1.1, 1.3, 3.2, 4.5, 5.2, 5.3, and 5.4: persona config scalar fields now fail closed before worker prompt/provider setup unless bounded and type-safe, and legacy unquoted final emits now reject same-line trailing payloads as `EMIT_PROTOCOL_VIOLATION` before any successful digest/adjudication candidate is accepted.

Checks: local PR ancestry check; `python3 -m py_compile` for ThreadKeeper and runtime synced `subagent.py`/`threadkeeper_budget.py` plus focused mock tests; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`242 passed`); `git diff --check`; runtime source `cmp`; GGB sibling fixture checker. No paid compute, live OmegaClaw/Telegram/ThreadKeeper runtime behavior change, queue enqueue/claim outside local tests, provider call, secret read, access/security setting change, daemon/scheduler install, merge, force-push, or remote-ref deletion.
## 2026-07-11 ThreadKeeper queued-dispatch path argument hardening

- Repo: `projects/omegaclaw/repos/ThreadKeeper`, branch `agent/threadkeeper-hardening-next`, commit `c2f299e` (`Bound queued dispatch path arguments`), pushed to `fork/agent/threadkeeper-hardening-next`; safety-floor branch remains an ancestor of HEAD.
- Hardened `subagent.run_queued_dispatch(queue_path)` to reject oversized strings and NUL/control characters before queue-dir resolution, claim/rename, checksum verification, or worker LLM setup. This extends strict argument validation to explicit queued-worker operator paths and avoids multiline audit/status ambiguity.
- Added focused regressions proving newline and oversized queue paths return `queue_worker_error` without creating `.claimed`/`.failed` files. Updated `docs/reference-skills-subagent.md`. Synced `src/subagent.py` into the nested OmegaClaw runtime tree.
- Verification: `python3 -m py_compile src/subagent.py`; focused queue path pytest (`3 passed, 232 deselected`); focused mock hardening pytest (`248 passed` across subagent + budget hardening); `git diff --check`; runtime source `cmp`/compile.
- Boundaries: no paid compute, provider calls, live Telegram/runtime wiring, secrets/access/security changes, queue enqueue/claim outside local tests, daemon/scheduler install, force-push, merge, or remote-ref deletion.


## 2026-07-11 - ThreadKeeper run-control path argument hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 safety-floor work. Pushed commit `be5ea1f` (`Reject control chars in run control paths`) to `fork/agent/threadkeeper-hardening-next`.

Worker-loop `stop_file` and queued-task `cancel_file` control-token paths now fail closed on NUL/control characters before run-dir resolution, worker-lock acquisition, queue claim validation, cancellation checks, or worker LLM setup. This closes the control-plane counterpart of the recent queue-path/tool-argument line-forging hardening: operator arguments and queued task records can no longer inject multiline status/audit text through stop/cancel token paths. Updated focused regressions and subagent reference docs; synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: PR #1 ancestry check; `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py ../PeTTa/repos/OmegaClaw-Core/src/subagent.py`; focused run-control pytest (`9 passed, 228 deselected`); focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`250 passed` for subagent + budget hardening tests); `git diff --check`; runtime source cmp/compile; pushed to fork. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, queue enqueue/claim outside local tests, provider call, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper run-control path GGB gate

Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-run-control-path-hardening/` for ThreadKeeper branch `agent/threadkeeper-hardening-next` head `be5ea1f`. The gate maps queued-dispatch path bounding plus worker-loop `stop_file` / queued-task `cancel_file` control-character rejection to GGB capacities 1.1, 1.3, 3.2, 4.5, 5.2, 5.3, and 5.4.

Checks: PR #1 ancestry check; `python3 -m py_compile` for ThreadKeeper and runtime synced `subagent.py`/`threadkeeper_budget.py` plus focused mock tests; focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`250 passed`); `git diff --check`; runtime source `cmp`; GGB sibling fixture checker. No paid compute, live OmegaClaw/Telegram/ThreadKeeper runtime behavior change, queue enqueue/claim outside local tests, provider call, secret read, access/security setting change, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper worker env-file loading hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor` and avoiding duplicate Phase 1 work. Pushed commit `10dad06` (`Harden worker env file loading`) to `fork/agent/threadkeeper-hardening-next`.

The conservative worker-loop runner `scripts/run-subagent-worker-loop` now opens `--env-file` config with no-follow semantics when available, checks regular-file status and size on the opened fd with `fstat`, and parses from that fd. This keeps operator env-file loading bounded and fail-closed before `subagent` import while reducing path/stat/open race exposure.

Checks: `python3 -m py_compile scripts/run-subagent-worker-loop Autotests/mock/test_subagent_hardening_mock.py`; focused worker-loop script pytest (`5 passed, 233 deselected`); focused hardening pytest (`238 passed`); `git diff --check`. A broader mock-suite attempt passed 243 tests but hit 3 Docker-dependent integration failures because `docker` is unavailable on this host. No paid compute, live OmegaClaw/Telegram/ThreadKeeper runtime behavior change, queue enqueue/claim outside tests, provider call, secret/access setting change, daemon/scheduler install, merge, force-push, or remote-ref deletion.

## 2026-07-11 - ThreadKeeper worker env streaming read cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor`. Pushed commit `6a9452d` (`Bound worker env reads after open`) to `fork/agent/threadkeeper-hardening-next`.

The worker-loop runner now reads an opened env file as at most 64 KiB plus one byte and rejects cap crossing during the read, rather than relying only on the opened-fd `fstat` size. It also rejects invalid UTF-8 explicitly before parsing. This closes a local post-`fstat` growth race that could otherwise make the env loader consume an unbounded file before importing `subagent`. Added a focused underreported-size regression.

Checks: PR #1 ancestry check; `py_compile`; focused runner pytest (`5 passed, 234 deselected`); focused hardening pytest (`252 passed`); `git diff --check`; pushed to fork. No paid compute, live wiring, secrets/access/security changes, queue enqueue/claim outside tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper technical-analysis argument validation

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `35c0c98` (`Validate technical analysis ticker arguments`) to `fork/agent/threadkeeper-hardening-next`.

`technical-analysis` tool calls now fail closed unless their sole argument matches a bounded 1-32 character market-symbol grammar. This narrows a provider-facing tool that previously accepted arbitrary free-form query text despite its ticker-only backend contract. Added regressions for common symbols and malformed/free-form values, updated docs, and synced the nested OmegaClaw runtime source. Checks: `py_compile`; focused hardening pytest (`254 passed` after correcting the initial grammar to permit caret-prefixed index symbols); `git diff --check`; runtime source `cmp`. No paid compute, live wiring, secrets/access/security changes, queue/provider activity, daemon/scheduler install, force-push, merge, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper external query argument cap

Continued ThreadKeeper hardening on `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `73b6b7b` (`Bound external query arguments`) to `fork/agent/threadkeeper-hardening-next`. `search`, `tavily-search`, and `technical-analysis` now enforce a dedicated `OMEGACLAW_SUBAGENT_MAX_QUERY_ARG_CHARS` cap (default 4096) before provider execution, in addition to the broader tool-argument cap. Added focused coverage and docs; synced the nested OmegaClaw runtime source. Checks: PR #1 ancestry, `py_compile`, focused hardening pytest (`255 passed`), `git diff --check`, runtime source `cmp`. No live wiring, provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper optional shell argument cap

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `76ec6b6` (`Bound optional shell command arguments`) to `fork/agent/threadkeeper-hardening-next`.

The optional allowlisted argv-only `shell` tool now has a dedicated command-input cap, `OMEGACLAW_SUBAGENT_MAX_SHELL_ARG_CHARS` (default 4096), enforced before `shlex` parsing or subprocess execution. The existing broader per-tool argument cap remains defense in depth. Added focused coverage, updated reference docs, and synced the nested OmegaClaw runtime source. Checks: PR #1 ancestry; Python compile; focused hardening pytest (`256 passed`); `git diff --check`; runtime source `cmp`. No live runtime/provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper unterminated quoted tool argument hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `0781f57` (`Reject unterminated quoted tool arguments`) to `fork/agent/threadkeeper-hardening-next`.

Single-argument worker tool calls beginning with an unterminated quote now parse into an invalid argument shape, so `shell`, external query tools, `read-file`, and final `emit` fail closed instead of treating the malformed raw payload as one executable argument. Added focused regression coverage and synced the nested OmegaClaw runtime source. Checks: source/runtime compile; focused hardening pytest (`257 passed`); `git diff --check`; runtime source `cmp`. No live wiring, subprocess/provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper quoted file-content protocol hardening

Continued ThreadKeeper hardening on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / `agent/threadkeeper-safety-floor`. Pushed commit `dd3f7e5` (`Reject malformed quoted file tool content`) to `fork/agent/threadkeeper-hardening-next`.

Quoted `write-file` / `append-file` content now must have a closing quote with only whitespace afterward. Unterminated content and same-line trailing payloads surface as argument-count violations before workspace mutation, closing the two-argument counterpart of the recent single-argument/emit protocol checks. Normal quoted content remains accepted. Synced `src/subagent.py` into the nested OmegaClaw-Core runtime tree.

Checks: Python compile; focused hardening pytest (`258 passed`); `git diff --check`; runtime source `cmp`; pushed to fork. No live runtime, provider, queue, subprocess, secrets/access/security changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper unquoted trailing single-argument call hardening

Continued on `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding Phase 1 duplication. Commit `6a62c97` extends same-line trailing-call rejection from final emits to every single-argument worker tool: malformed unquoted payloads such as `(search safe) (emit hidden)` now become argument-count failures before provider, subprocess, file-read, or emit handling. Ordinary parenthesized prose remains accepted. Updated docs/tests and synced nested OmegaClaw runtime source. Checks: compile; focused hardening pytest (`260 passed`); diff check; runtime source cmp. No live wiring, provider/subprocess/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 — PLN naming note from Ben

Ben clarified that the PLN renaming (in the context of GoalChainer's heuristic PLN-style beliefs and the petta-memory πPLN/patham9 bridge) affects naming in the software only, not design. Future subagents working on GoalChainer or petta-memory integration should treat "PLN" naming as cosmetic; the underlying probabilistic logic design is unchanged.

## 2026-07-12 - ThreadKeeper compact trailing-call protocol hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `3a296ad` (`Reject compact unquoted trailing calls`) to `fork/agent/threadkeeper-hardening-next`.

Unquoted one-argument calls now reject compact same-line `)(` trailing-call payloads as well as spaced `) (` payloads before optional shell, provider-backed query, file-read, or final-emit handling. Ordinary balanced parenthesized prose remains accepted. Synced `src/subagent.py` into the nested OmegaClaw runtime source. Checks: Python compile, focused subagent/budget hardening pytest (`260 passed`), `git diff --check`, and runtime source `cmp`. No live runtime, provider, queue, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.
## 2026-07-12 - GoalChainer canary review-boundary gate

Inspected the new non-live GoalChainer→ThreadKeeper canary and found a concrete policy gap: its generic default fixture made `publish_raw_log` recommended/permitted, queued it, and accepted it; recommended tasks also set `requires_adjudication=false`. Narrowly hardened the exploratory canary without touching ThreadKeeper PR #1: the default fixture now explicitly contains sensitive data, forbidden norms are rejected before queueing, every queued output remains `patch_proposal_only` and requires adjudication, and the offline reviewer allowlists only `publish_redacted_summary`. Added three focused regressions and archived `artifacts/ggb-capacity-gates/20260712-goalchainer-canary-review-boundary/`. Checks passed: 3 focused tests, compile, diff check, and an isolated fake-worker replay with one accepted redacted-summary candidate, raw log forbidden/not queued, and hold deferred. No provider/Gateway, Telegram, live runtime, memory write, secret, paid-compute, push, or merge activity.

## 2026-07-12 - ThreadKeeper bidirectional-control tool-argument hardening

Continued strict tool-argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `5624013` (`Reject bidi controls in tool args`) to `fork/agent/threadkeeper-hardening-next`. File paths, external queries, and optional-shell commands now reject Unicode bidirectional formatting/isolate controls before filesystem/provider/subprocess handling, preventing visually reordered prompt/transcript/audit arguments while preserving benign format characters such as emoji joiners. Synced nested OmegaClaw runtime source. Checks: compile, focused hardening pytest (`265 passed`), diff check, runtime source cmp. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

## 2026-07-12 - ThreadKeeper Unicode-control argument GGB gate

Archived `artifacts/ggb-capacity-gates/20260713-threadkeeper-unicode-control-arg-hardening/` at ThreadKeeper head `5624013`. The combined gate records that file paths, external queries, and optional-shell commands reject C1 controls, Unicode line/paragraph separators, and bidi formatting/isolate controls before filesystem/provider/subprocess handling. PR #1 safety-floor ancestry passed; source compile, `git diff --check`, 265 focused hardening tests, and the GGB sibling-fixture checker passed. The current OmegaClaw-Core checkout contains no runtime `subagent.py`, so byte-parity is explicitly not claimed. No live integration or external side effect occurred.

## 2026-07-12 - ProtoMegaBot installation and reliability report

Created the source-grounded report `docs/protomegabot_omegaclaw_installation_architecture_20260712.tex` and compiled `docs/protomegabot_omegaclaw_installation_architecture_20260712.pdf` (15 pages). It documents the project-local PeTTa/SWI/Janus/Python/OpenClaw installation, hybrid MTProto-receive/Bot-API-send architecture, multi-chat routing invariant, dated failure chronology, observed 21:16 and 21:19 process states, and prioritized remediation. Newly confirmed issues include synchronous Bot API polling leaking into MTProto mode, an orphaned bridge coexisting with a restarted bridge, private-help-text versus broad executable-default drift, and the Telethon session database being mode 0644 while the secret env is correctly 0600. Verification: ASCII-only LaTeX source, Tectonic compile, 15-page `pdfinfo`, full `pdftotext` section checks, fatal LaTeX and credential-pattern scans, and SHA-256 capture. No credential values, live reconfiguration, process stop/restart, paid compute, or remote operation.

## 2026-07-12 - ProtoMegaBot P0 stabilization patch (not deployed)

Implemented a source/test-only first remediation slice in the active nested OmegaClaw-Core checkout. Telegram receive now has one authoritative `TG_RECEIVE_TRANSPORT` (`mtproto` or `bot_api`), rejects contradictory legacy settings, makes `getUpdates` fail closed in MTProto mode, disables synchronous polling there, and fails startup instead of silently falling back to Bot API. The MTProto bridge no longer uses `setsid`; it receives an expected-parent PID, arms Linux `PR_SET_PDEATHSIG`, rechecks parent identity, uses a mode-0600 singleton lock, waits for an actual connected readiness event, and normalizes session-file modes to 0600. The local launcher now defaults `TG_SYNC_POLL=false`; supervisor status distinguishes ownership, worker count, owned/global bridge count, and explicitly does not claim end-to-end health. Added `Autotests/test_telegram_transport_invariants.py`. Evidence: 14 focused pytest checks passed with `--noconftest`; four address-filter unittests passed; `py_compile`, shell syntax, and `git diff --check` passed. The repository's normal pytest teardown remains environment-blocked because it unconditionally invokes unavailable Docker after tests (the tests themselves passed before teardown). Read-only live status proved the new check catches the current broken topology: one worker, zero owned bridges, and two global bridge processes at final inspection. No live process was stopped, restarted, or reconfigured, so the patch is not yet active.

## 2026-07-12 - ProtoMegaBot staged reliability repair plan

Wrote `PROTOMEGABOT_REPAIR_PLAN_20260712.md`, converting the GPT-5.6-sol architecture review and direct runtime/source evidence into a 15-step gated remediation sequence. Immediate order is inventory, package/review the existing source-only P0 patch, add negative transport/ownership tests, obtain approval for controlled cleanup/restart, establish one service generation, prove runtime receive exclusivity, and run a fixed-response private canary. Subsequent gates replace mutable `_active_chat_id` routing with immutable per-message envelopes, introduce framed/bounded IPC and backpressure, split liveness/readiness/end-to-end health, add privacy-safe event journaling, classify native crashes, run a one-variable crash matrix, and only then expand from private soak to multi-chat/group use. The plan explicitly treats signal 11 and exit 137 separately and does not claim deployment readiness.

## 2026-07-12 - Fable route-override defect isolated and patched locally

Direct local inference with `anthropic/claude-fable-5` reached the Anthropic provider and returned an Anthropic 429 rate-limit response, proving the configured provider/auth route exists; this supersedes the earlier hypothesis that Anthropic configuration/auth was absent. Source inspection showed `plugins/intent-model-router` always reclassified prompts in `before_model_resolve`, even when a caller/session had explicitly selected Fable, so ordinary technical review prompts were overwritten to `openai/gpt-5.6-sol`. Patched the router to preserve an explicit `anthropic/claude-fable-5` selection and added focused detection coverage. Checks: 9 Node tests pass, JS syntax checks pass, `git diff --check` passes. Activation remains blocked because the Gateway is a system-scope `openclaw-agent.service`; the ordinary `openclaw gateway restart` correctly refused and this Telegram session has no elevated tool grant. No service was restarted. After an approved restart, verify effective execution metadata; Anthropic may still return 429 until its account rate window/cap permits a request.

## 2026-07-13 - ThreadKeeper Unicode run-control path hardening

Continued strict argument validation on `projects/omegaclaw/repos/ThreadKeeper` branch `agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and avoiding duplicate Phase 1 work. Pushed commit `6e0e49b` (`Harden Unicode run-control paths`) to `fork/agent/threadkeeper-hardening-next`.

Explicit queued-dispatch paths and worker stop/queued-task cancellation token paths now use the same Unicode-safe control validation as tool arguments. They reject Unicode separators, bidi/unsafe invisible formatting characters, and lone surrogates before queue claim/rename, worker-lock acquisition, token checks, or worker LLM setup. Added focused regressions for queued paths and stop files; updated docs and synced the nested OmegaClaw runtime source.

Checks: PR #1 ancestry; Python compile; focused control-path pytest (`4 passed`); focused subagent/budget hardening pytest (`268 passed`); `git diff --check`; runtime source `cmp`; pushed to fork. No live runtime, provider, queue claim outside tests, subprocess, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.
# 2026-07-15 — ThreadKeeper persistent-worker mandate

Ben expanded the ThreadKeeper implementation mandate to include a native asynchronous persistent-worker mode, distinct from bounded synchronous `delegate`. Created isolated worktree `worktrees/threadkeeper-persistent-workers` on branch `agent/threadkeeper-persistent-workers` from clean local head `a2c62eb` (six commits ahead of its tracking branch). The architecture baseline is `docs/persistent-workers.md` inside that worktree. Research Rules 2, 3, 5, 6, and 7 are directly relevant: specify stateful behavior first; extend the existing hardened queue/supervisor substrate; preserve reproducible evidence; model continuity as event/checkpoint lineage; and keep MeTTa/Python abstraction seams explicit. ProtoMegaBot production is excluded; eventual live testing is ProtoMegaBot2-only.
## 2026-07-15 - ThreadKeeper persistent spawn and cancellation surfaces

Implemented the third provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, following durable manifest/event/status
commit `f82d168`. Added idempotent `spawn_persistent` and `cancel_persistent`
surfaces plus a lifecycle-gated queue claim wrapper. Spawn reuses the existing
persona/task-contract/tool-subset/escalation validation and queue-only record;
cancellation creates the task-scoped durable token before recording its CAS
event. Causal intervention tests prove cancellation that wins first prevents
the later claim wrapper and queue/provider effect, while integration tests prove
the real queued worker returns `cancelled` without calling the worker LLM.

Evidence: experiment
`experiments/20260715T150724Z-threadkeeper-persistent-spawn-cancel-v1/` passed
16 unit tests and 315 combined lifecycle/full focused subagent tests, plus
Python compilation and `git diff --check`. No provider, Telegram, ProtoMegaBot,
credential, supervisor, or production path was touched. Remaining limitation:
attempt leases, checkpoint/restart recovery, and queue-result reconciliation
remain phase 4.

## 2026-07-15 - ThreadKeeper persistent attempt/checkpoint recovery records

Implemented the next provider-free persistent-worker slice on isolated branch
`agent/threadkeeper-persistent-workers`, commit `43d34fe`, and pushed the branch
normally to `fork/agent/threadkeeper-persistent-workers`. A lifecycle claim now
validates lease inputs before mutation and creates a versioned, bounded,
hash-linked immutable attempt/lease before the queued-dispatch effect.
Checkpoints are atomic, bounded, payload-hashed, idempotent by ID, and verified
as an immutable chain. Restart recovery fails closed for active, missing,
mismatched, or corrupt lineage; an expired verified attempt is idempotently
recorded as `FAILED_RETRYABLE`, with requeue deliberately left as a separate
durable effect.

Evidence:
`experiments/20260715T151639Z-threadkeeper-persistent-attempt-checkpoint-recovery-v1/`
passed Python compilation, `git diff --check`, and 332 combined persistent
lifecycle/storage plus full subagent/budget hardening tests. No paid compute,
provider, live queue, Telegram, credential, supervisor, ProtoMegaBot process or
production path was used. Next: explicit resume/requeue effects and crash
fixtures at claim/attempt/checkpoint boundaries, then durable task budgets and
inbox/result delivery.

## 2026-07-15 - ThreadKeeper verified checkpoint resume handoff

Continued the provider-free persistent-worker track on isolated branch
`agent/threadkeeper-persistent-workers`. Commit `1b2d670` binds the latest
verified checkpoint ID and SHA-256 into each new immutable attempt and passes
the verified structured checkpoint to the queued runner. The existing queued
worker validates the checkpoint identity/payload and exposes bounded canonical
resume context through the task contract; first attempts continue with no
checkpoint. Tests cover checkpoint-free claims and recovery/requeue into a
second attempt, including the actual queued-worker transcript.

Checks: 25 narrow lifecycle/resume tests; 337 combined persistent lifecycle,
subagent hardening, and budget hardening tests; Python compilation; `git diff
--check`. Commit pushed normally to `fork/agent/threadkeeper-persistent-workers`.
No provider, paid compute, Telegram, live queue/supervisor, credential,
ProtoMegaBot process, production path, merge, force-push, or remote-ref deletion.
Next: an idempotent enqueue receipt plus crash fixtures across the queue/event
boundary.
## 2026-07-15 - ThreadKeeper persistent enqueue receipts

Closed the spawn/requeue enqueue-to-event crash window on isolated branch
`agent/threadkeeper-persistent-workers`, commit `29948e9`, normally pushed to
`fork/agent/threadkeeper-persistent-workers`. Spawn and explicit requeue now
write bounded immutable receipts keyed by the operation ID and bound to the
task-manifest and queue digests before appending their lifecycle CAS event.
After a simulated event-write crash, retry reuses the verified receipt and does
not repeat the queue effect. Per-task enqueue locking serializes concurrent
operations where `fcntl` is available; malformed or conflicting receipts fail
closed.

Evidence:
`experiments/20260715T190300Z-threadkeeper-persistent-enqueue-receipts-v1/`
passed 27 narrow lifecycle/storage tests, 340 combined persistent lifecycle,
subagent hardening, and budget hardening tests, Python compilation, and `git
diff --check`. No provider, paid compute, live queue/supervisor, Telegram,
credential, ProtoMegaBot process, production path, merge, force-push, or remote
ref deletion occurred. Next: durable task-level budgets, then inbox/result
delivery.

## 2026-07-15 - ThreadKeeper persistent task-level budget ledger

Continued the isolated persistent-worker track on
`agent/threadkeeper-persistent-workers` and pushed commit `4b7399e` normally to
`fork/agent/threadkeeper-persistent-workers`. Task manifests now accept only a
closed set of positive integer budget limits. Immutable task usage deltas are
bounded, append-only, hash-linked, idempotent by usage ID, and bound to verified
attempt lineage. `budget_status()` reconstructs monotone attempt/token/time/tool
consumption across restarts; exhausted limits block claim and explicit requeue
before the queue/provider/tool effect.

Evidence:
`experiments/20260715T210802Z-threadkeeper-persistent-task-budgets-v1/`
passed 30 narrow lifecycle/storage tests and 343 combined persistent lifecycle,
subagent hardening, and budget hardening tests, plus Python compilation and
`git diff --check`. No provider, paid compute, live queue/supervisor, Telegram,
credential, ProtoMegaBot process, production path, merge, force-push, or remote
ref deletion occurred. Next: crash-safe queued-attempt accounting handoff, then
idempotent inbox/result delivery.

## 2026-07-15 - ThreadKeeper task-contract tool-quota validation

Continued the bounded synchronous ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`agent/threadkeeper-safety-floor` ancestor. Commit `e4481a8` closes a remaining
strict-validation exception path: task-contract `max_tool_calls` must not
exceed the global dispatch quota, and arbitrarily long decimal strings are
rejected before `int()` conversion. Invalid values persist a structured
`contract_invalid` transcript without provider or worker LLM setup.

Checks: focused quota pytest (`5 passed`); combined subagent/budget hardening
pytest (`313 passed`); Python compilation; `git diff --check`; PR #1 ancestry.
The nested OmegaClaw runtime copy was not synced because it already lags the
hardening branch by several local commits. No paid compute, provider, live
queue/runtime, Telegram, subprocess, credential/access change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-15 - ThreadKeeper closed-schema task contracts

Continued the bounded synchronous ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`agent/threadkeeper-safety-floor` ancestor. Commit `0fc6efb`, pushed normally to
`fork/agent/threadkeeper-hardening-next`, makes nested and
persona task contracts closed-schema inputs: unknown or misspelled controls now
persist a structured `contract_invalid` transcript before provider or worker
setup instead of being silently discarded. Top-level inline goal envelopes keep
their existing compatibility behavior.

Checks: focused task-contract pytest (`6 passed`); combined subagent/budget
hardening pytest (`315 passed`); Python compilation; `git diff --check`; PR #1
ancestry. The nested OmegaClaw runtime copy remains intentionally unsynced while
it lags several local hardening commits. No paid compute, provider, live queue,
runtime, Telegram, subprocess, credential/access change, merge, force-push, or
remote-ref deletion occurred.

# 2026-07-15 - OpenClaw chat-room identity Phase 1

Read all 757 lines of `docs/chat_room_identity_design/chat_room_identity_design.tex`. The sole PDF was generated 20 seconds after the TeX and contains the same Phase 1 schema/roadmap; no separate revised PDF was present. Traced the pipeline through `bot-message.ts` -> `bot-message-context.ts` -> `bot-message-context.session.ts` -> generic channel inbound context -> `MsgContext` -> inbound prompt metadata.

Implementation commit `4c8cc1f5` adds a pure Telegram identity/envelope classifier and integration. Parent review found that reply-to-self incorrectly outranked an explicit mention of another bot, contrary to the v2 conflict rule, and that the new module had four extension-lint violations. Follow-up commit `4d234b80` makes explicit mentions authoritative when signals conflict, adds disagreement/reinforcement fixtures, and fixes the lint findings. Review also found an unconditional pre-generation `INCIDENTAL` skip, which contradicted Ben's explicit v2 definition of always-attending bots; follow-up `2e0ed9e0` removes that skip and adds a processor regression proving incidental messages reach attention policy. Validation commands: direct Vitest runs with `test/vitest/vitest.extension-telegram.config.ts` (32 passed across classifier and processor suites) and `test/vitest/vitest.auto-reply.config.ts` (75 passed); `corepack pnpm tsgo:core`; `corepack pnpm lint:extensions`; focused `oxfmt --check`; `git diff --check`. The aggregate `pnpm check` could not run initially because `pnpm` was only available through Corepack and its child processes require a PATH-visible executable. An initial multi-project test invocation also exposed a shallow-checkout cleanup issue and removed the first disposable clone; the branch was reconstructed from the pinned tag and verified with direct Vitest invocations.

# 2026-07-15 - Machintel v2 registry and suppression milestone

The preserved library PDF and named extracted attachment were discovered to be the unrelated 12-page Labs Constitution, despite the sidecar metadata. The authoritative complete Revision-2 source is the 857-line `docs/chat_room_identity_design/chat_room_identity_design_v2.tex`; implementation proceeded from that checked source and the artifact defect remains to repair separately.

OpenClaw branch `agent/chat-room-identity-phase1` commit `e54d3356` adds `channels.telegram.botRegistry`, upgrades the structured envelope/self context to v2, derives sender/reply bot flags only from the registry, records social role/important bots and reinforced mention+reply agreement, and recognizes structured `SUPPRESS` in the existing silent-delivery gateway. Evidence: focused identity 9/9, token policy 60/60, core type check, scoped diff check. A full extension lint attempt produced no diagnostics but was manually interrupted after a prolonged quiet run, so it is not claimed as passing for this milestone.

ProtoMegaBot2 commit `9a03011` adds the same mechanical schema to `channels/telegram.py`/`message_envelope.py`, registry JSON loading, mention-first classification, inspectable MeTTa policy relations, and a publish gate suppressing `SUPPRESS`, legacy `NO_REPLY`, acknowledgement-only text, and silence explanations. Provider-free canary evidence is 7/7 focused tests plus Python compilation and scoped diff check. Existing unrelated `memory/history.metta` changes were preserved and excluded from the commit. No live source, process, Telegram token, provider, or secret file was touched.

## 2026-07-15 - ThreadKeeper direct dispatch-limit validation

Continued the bounded synchronous ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next`, coordinated against current draft PR #1
head `3a870c5` / its safety-floor ancestry. Commit `6b71b45`, pushed normally
to `fork/agent/threadkeeper-hardening-next`, removes a remaining lossy input
path: direct `dispatch` no longer converts booleans/floats or silently replaces
malformed `max_turns` / `max_chars` with defaults. Invalid or pathologically
long decimal inputs persist a structured `dispatch_args_invalid` transcript
before persona config, provider setup, or worker LLM calls. Decimal integer
strings remain supported for MeTTa/Python compatibility and valid integer caps
retain their existing clamp behavior.

Checks: focused numeric-boundary pytest (`6 passed`); combined subagent/budget
hardening pytest (`320 passed`); Python compilation; `git diff --check`; remote
PR #1 head/ancestry check. The nested OmegaClaw runtime copy remains
intentionally unsynced while it lags several local hardening commits. No paid
compute, provider, live queue/runtime, Telegram, subprocess, credential/access
change, merge, force-push, or remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper persistent inbox storage

Continued the isolated persistent-worker track on
`agent/threadkeeper-persistent-workers`, coordinated against draft PR #1 and
without duplicating its Phase 1 safety-floor work. Commit `66b249a`, pushed
normally to `fork/agent/threadkeeper-persistent-workers`, adds bounded immutable
inbox items as a provider-free storage receipt. Each item has a strict versioned
schema, sequence, task/source-event/actor identity, bounded object payload,
payload digest, and self-hash; creation is atomic and serialized per task.
Eligibility is fail-closed: the task must currently be `WAITING_INPUT` and the
item must bind to the current lifecycle event. Duplicate item IDs replay after
restart, while stale sources, conflicting duplicates, malformed schema,
sequence gaps, symlinks/non-regular records, and tampering are rejected. This
slice intentionally performs no queue, lifecycle, provider, or tool effect.

Checks: Python compilation; lifecycle pytest (`36 passed`); combined lifecycle,
subagent, and budget hardening pytest (`349 passed`); `git diff --check`; PR #1
ancestry; clean pushed worktree. No paid compute, provider, live queue/runtime,
Telegram, secret/access/security change, merge, force-push, or remote-ref
deletion occurred. Next: separate inbox consumption/requeue receipts, then
result delivery/acknowledgement.

Roadmap worker follow-up at 2026-07-16 07:36 UTC archived the implementation as
`artifacts/ggb-capacity-gates/20260716-threadkeeper-persistent-inbox-storage/`.
The combined 349-test provider-free gate replayed cleanly, and the sibling
fixture checker covered all 7 recorded checks. `GGB_NEXT_GATES.md` now makes the
remaining boundary explicit: storage is complete, while consumption/requeue
must use a separate receipt that proves crash replay cannot consume or enqueue
twice. No source/runtime change or live authority was added.

## 2026-07-16 - ThreadKeeper direct dispatch scalar validation

Continued the bounded synchronous hardening track on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 / its
`agent/threadkeeper-safety-floor` ancestry without duplicating Phase 1.
Commit `ae99ed3`, pushed normally to
`fork/agent/threadkeeper-hardening-next`, makes direct `dispatch` reject
non-string goals, persona keys, and explicit tool subsets plus blank goals.
Malformed boundary values now produce a persistent structured
`dispatch_args_invalid` record before persona/provider setup instead of being
stringified or raising at `.strip()`.

Checks: focused scalar/limit pytest (`9 passed`); combined subagent/budget
hardening pytest (`329 passed`); Python compilation; `git diff --check`; PR #1
ancestry. The nested OmegaClaw runtime copy remains intentionally unsynced while
it lags several hardening commits. No paid compute, provider, live queue/runtime,
Telegram, subprocess, credential/access/security change, merge, force-push, or
remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper compound dispatch-argument validation

Continued the bounded synchronous hardening track on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
safety-floor ancestry. Commit `a1a1bce` closes a compound-invalid-input edge:
integer-limit errors are now combined with scalar validation before persistent
error-record construction. A call containing both a malformed limit and
non-string goal/tool subset/persona previously took the earlier limit-error
path and could pass the unsafe persona value into transcript filename
construction; it now returns and persists one `dispatch_args_invalid` record
with sanitized record identity, before persona/provider setup.

Checks: compound/numeric/scalar focused pytest (`10 passed`); full focused
subagent pytest (`312 passed`); combined subagent/budget gate (`325 passed`);
Python compilation; `git diff --check`; PR #1 ancestry. No provider, live
queue/runtime, Telegram, subprocess, paid compute, secret/access/security
change, merge, force-push, or remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper persona resource/default-tool validation

Continued the bounded synchronous hardening track on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`agent/threadkeeper-safety-floor` ancestry without duplicating Phase 1. Commit
`619e223` validates optional persona resource and tool defaults during config
load: `max_output_tokens` must be a non-boolean integer from 1 through the
operator hard cap `OMEGACLAW_SUBAGENT_MAX_OUTPUT_TOKENS` (default 8,192), while
`default_tool_subset` must be a non-empty bounded list of safe tool identifiers
that are registered and v1-callable. Malformed/oversized limits, scalar or
mixed-type lists, unsafe identifiers, excluded tools, and unknown tools now
fail closed before escalation or provider setup.

Checks: focused persona-config pytest (`22 passed`); combined provider-free
subagent/budget hardening pytest (`342 passed`); Python compilation;
`git diff --check`; PR #1 ancestry. The nested OmegaClaw runtime copy remains
intentionally unsynced while it lags several hardening commits. No paid
compute, provider, live queue/runtime, Telegram, subprocess,
credential/access/security change, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-16 - Persistent supervisor subprocess restart gate

ThreadKeeper branch `agent/threadkeeper-persistent-workers` commit `c06725e`
adds a provider-free subprocess fixture for the first real interpreter-boundary
restart gate. Separate Python processes create an expired claimed attempt,
recover and requeue it, then restart with cancellation asserted. The last
process observes durable `QUEUED` state; the external effect journal contains
exactly one enqueue and no runner call. Focused lifecycle tests pass 48/48 and
the combined persistent/subagent/budget gate passes 361 tests; Python compile
and `git diff --check` pass. No live runtime, provider, Telegram, queue service,
memory promotion, credentials, paid compute, push, merge, or production wiring.
## 2026-07-16 - ThreadKeeper exclusive persistent-supervisor ownership

Completed the next provider-free persistent-worker supervisor slice on
isolated branch `agent/threadkeeper-persistent-workers`, commit `e7e997e`.
`supervise_persistent_once` now takes a non-blocking root-scoped OS file lock
before durable-state preflight or callbacks. Concurrent callers and hosts
without the locking primitive fail closed before queue/runner effects; the lock
path uses the existing regular-file/no-symlink guard and crash exit releases
ownership. A two-interpreter contention regression holds the owner during fake
enqueue, proves the contender emits no effect, then verifies exactly one owner
enqueue. Lifecycle pytest passed 49 tests; the combined provider-free gate
passed 362 tests, plus Python compilation and `git diff --check`. Evidence:
`experiments/20260716T210300Z-threadkeeper-persistent-supervisor-ownership-v1/RUN.md`.
No live queue/provider/Telegram, ProtoMegaBot path/process, paid compute,
credential/access change, push, merge, force-push, or remote-ref deletion.

## 2026-07-16 - ThreadKeeper dispatch-deadline retry hardening

Continued bounded synchronous hardening on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`fork/agent/threadkeeper-safety-floor` ancestor without duplicating Phase 1.
Commit `4b4524a` binds each worker provider timeout to the smaller configured
LLM timeout or remaining dispatch wall-clock budget. Retry backoff is capped by
that deadline, a new attempt cannot start after expiry, and the dispatch checks
again after the provider returns so a late successful-looking result is not
accepted. Late calls persist a structured `dispatch_timeout` record with
observed token accounting.

Checks: focused timeout/retry pytest (`7 passed`); combined provider-free
subagent/budget hardening pytest (`350 passed`); Python compilation;
`git diff --check`; safety-floor ancestry. An initial check invocation used an
incorrect relative venv path and exited 127 before collecting tests; the
corrected commands passed. No provider, live runtime/queue, Telegram,
subprocess worker, paid compute, credential/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-16 - ThreadKeeper closed-schema persona configs

Continued bounded synchronous hardening on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`fork/agent/threadkeeper-safety-floor` ancestor without duplicating Phase 1.
Commit `150b185` makes persona configuration a closed-schema boundary:
unknown or misspelled controls such as `max_output_token` now fail during
config load before escalation/provider setup. The existing deployed `notes`
metadata remains allowed, but must be a bounded string without unsafe control
characters. Added focused accept/reject regressions and updated the subagent
reference.

Checks: focused persona-config pytest (`39 passed`); combined provider-free
subagent/budget hardening pytest (`347 passed`); Python compilation;
`git diff --check`; safety-floor ancestry. The nested OmegaClaw runtime copy
remains intentionally unsynced while it lags the hardening branch. No paid
compute, provider, live queue/runtime, Telegram, subprocess,
credential/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-17 - ThreadKeeper complete-batch authorization preflight

Continued bounded synchronous hardening on
`agent/threadkeeper-hardening-next`, coordinated against draft PR #1 and its
`fork/agent/threadkeeper-safety-floor` ancestor without duplicating Phase 1.
Commit `63a63d3` makes worker authorization failures effect-free across the
complete response batch. A later registered tool outside the dispatch subset,
a task-contract-forbidden tool, an unregistered runtime tool, or a file call
outside task-contract `allowed_paths` is now rejected during preflight before
an earlier valid mutation can execute. Existing contract regressions now prove
the worker must retry an authorized write in a separate response.

Checks: focused authorization preflight pytest (`4 passed`); combined
provider-free subagent/budget hardening pytest (`359 passed`); Python
compilation; `git diff --check`; safety-floor ancestry. One combined check
command ran the full passing pytest gate and then exited 127 because the shell
had no bare `python`; compilation was rerun successfully with the project test
venv. No provider, live runtime/queue, Telegram, subprocess worker, paid
compute, credential/access/security change, push, merge, force-push, or
remote-ref deletion occurred.
## 2026-07-17 - ThreadKeeper effect-free quota preflight

Continued the draft-PR-#1-derived bounded ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next` with commit `4fa20bc`. Worker batches that
exceeded the per-turn or remaining dispatch/task-contract quota previously
applied earlier valid calls before rejecting the tail. Both quota checks now
run after complete-batch validation/authorization but before the first effect.

Provider-free regressions now prove neither file in a two-write over-quota
batch reaches the workspace for global, per-turn, or task-contract quotas.
Three focused tests and the combined subagent/budget gate (`364 passed`),
Python compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
passed. No provider, live queue/runtime, Telegram, paid compute,
credential/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-17 - ThreadKeeper reasoning-envelope protocol validation

Continued the draft-PR-#1-derived bounded synchronous hardening track on
`agent/threadkeeper-hardening-next` with commit `5ce53aa`, preserving
`fork/agent/threadkeeper-safety-floor` ancestry. The tolerant response parser
previously stripped well-formed `<think>...</think>` blocks but could parse and
execute a tool-shaped line after an unclosed, stray, or nested reasoning
marker. A new envelope preflight rejects those ambiguous forms before
`run_tools`; the same check prevents a final `emit` inside an unclosed block
from being accepted. Sequential well-formed reasoning blocks retain the
existing stripping behavior.

Provider-free regressions cover unclosed, stray, and nested envelopes with
no file effect, acceptance of a well-formed reasoning block, and rejection of
a hidden final emit. The combined boundary/subagent/budget gate passes 369
tests, plus Python compilation, `git diff --check`, and Phase 1 safety-floor
ancestry. An initial aggregate command named a nonexistent budget-test path
and collected no tests; the corrected three-file gate passed. No provider,
live queue/runtime, Telegram, subprocess worker, paid compute,
credential/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-17 - ThreadKeeper WAITING_INPUT handoff enforcement

Continued the provider-free persistent-worker track on
`agent/threadkeeper-persistent-workers` with commit `50aaaa2`. Inbox-driven
resume now verifies the complete checkpoint chain and requires its newest
checkpoint to be a formal handoff belonging to the current attempt before a
new enqueue or consumption-receipt replay. Missing handoffs and a newer opaque
checkpoint fail closed, leave the task in `WAITING_INPUT`, and produce no queue
effect. Existing inbox fixtures now model a durable attempt/handoff chain.

Checks: persistent lifecycle suite (`56 passed`); combined lifecycle/subagent/
budget gate (`369 passed`); Python compilation; `git diff --check`; draft PR #1
safety-floor ancestry. No provider, live queue/runtime, Telegram, ProtoMegaBot,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred. Evidence:
`experiments/20260717T190841Z-threadkeeper-waiting-input-handoff/`.

## 2026-07-17 - ThreadKeeper Markdown fence protocol validation

Continued the draft-PR-#1-derived bounded synchronous hardening track on
`agent/threadkeeper-hardening-next` with commit `79bfd4d`, preserving
`fork/agent/threadkeeper-safety-floor` ancestry. The tolerant response parser
previously removed Markdown fence marker lines without checking that the
envelope was balanced or supported, so tool-shaped lines inside an unclosed,
nested, or malformed fence could execute. Complete-batch preflight now accepts
only balanced, non-nested triple-backtick fences with the existing bounded
language-token alphabet. Malformed envelopes cause zero tool effects, and the
same validation prevents a final `emit` inside an unclosed fence from becoming
a parent result. Well-formed fenced tool calls retain their existing behavior.

Checks: focused fence/thinking protocol pytest (`10 passed`); combined
provider-free subagent/budget gate (`370 passed`); Python compilation;
`git diff --check`; Phase 1 safety-floor ancestry. The first compilation
command used the unavailable bare `python` alias and exited before testing;
the corrected `python3`/project-venv checks passed. No provider, live
queue/runtime, Telegram, subprocess worker, paid compute,
credential/access/security change, push, merge, force-push, or remote-ref
deletion occurred.
## 2026-07-17 - ThreadKeeper unsupported Markdown fence validation

Continued the draft-PR-#1-derived bounded ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next` with local commit `3175ab4`. Markdown
tilde-fence markers were outside the parser's supported triple-backtick v1
syntax but were not recognized as fence markers, so tool-shaped lines inside
them could execute. Unsupported tilde fences now reject the complete worker
batch before effects. A provider-free regression proves that both a call
inside the fence and an otherwise valid write earlier in the response cause
zero filesystem effects.

Checks: `fork/agent/threadkeeper-safety-floor` ancestry; focused fence pytest
(`7 passed`); combined provider-free subagent/budget pytest (`372 passed`);
Python compilation; `git diff --check`. An initial focused test invocation and
one combined invocation used incorrect relative paths and failed before test
collection; corrected project-venv commands passed. No provider, live queue,
Telegram, runtime wiring, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

## 2026-07-17 - ThreadKeeper enforceable forbidden-action contracts

Continued the draft-PR-#1-derived bounded ThreadKeeper hardening track on
`agent/threadkeeper-hardening-next` with local commit `3353e80`. Task contracts
previously accepted any syntactically safe `forbidden_actions` identifier even
though runtime enforcement recognized only tool names and a small alias set. A
misspelling could therefore persist as an apparent constraint with no effect.
The accepted vocabulary is now derived from the same centralized alias map used
at authorization, and unknown identifiers fail before worker/provider setup.

Focused contract pytest passed 7 tests; the combined provider-free subagent/
budget gate passed 379 tests, plus Python compilation, `git diff --check`, and
draft PR #1 safety-floor ancestry. No provider, live queue/runtime, Telegram,
subprocess worker, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

## 2026-07-18 - ThreadKeeper retry cancellation responsiveness

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`fccaac8`. Provider retry/backoff previously observed the dispatch deadline but
did not observe a cancellation token until the worker call returned to the
outer turn loop. A configured cancellation token is now checked before every
attempt and polled at bounded intervals during retry backoff. Cancellation
stops before another provider attempt and persists as a structured
`status=cancelled` result and cancelled transcript rather than an LLM failure.

Checks: focused retry tests (`5 passed`); combined provider-free
subagent/budget gate (`381 passed`); Python compilation; `git diff --check`;
draft PR #1 safety-floor ancestry. No provider, queue, Telegram, subprocess,
paid compute, secret/access/security change, push, merge, force-push, or remote
ref deletion occurred.

## 2026-07-18 - ThreadKeeper authenticated provider-control returns

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`21b8883`. Dispatch previously inferred provider cancellation, rate limiting,
concurrency limiting, and terminal retry failure from ordinary response-string
prefixes. Because provider response content is worker-controlled, a worker
could emit the cancellation prefix and forge a structured cancelled parent
return and cancelled transcript. Retry/control outcomes now use a private
internal string marker carrying the trusted status; identical ordinary worker
text stays untrusted and proceeds through normal protocol handling.

Checks: focused retry/control tests (`6 passed`); combined provider-free
subagent/budget gate (`382 passed`); Python compilation; `git diff --check`;
draft PR #1 safety-floor ancestry. No provider, queue, Telegram, subprocess,
paid compute, secret/access/security change, push, merge, force-push, or remote
ref deletion occurred.

## 2026-07-18 - ThreadKeeper authenticated provider-boundary failures

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`78a05b9`. The native Ollama transport's HTTP byte-cap failure and the
defensive missing-cloud-client path still returned ordinary strings. Dispatch
therefore could treat provider failures as worker protocol text and finish as
`incomplete`, weakening structured returns and durable failure classification.
Both paths now return private `_LLMControlResult` markers. Oversized provider
bytes are never JSON-decoded or parsed as tools, the parent receives
`status=error`, and the transcript retains `provider_response_invalid`.

Checks: provider-free subagent/budget gate (`380 passed`); focused provider-
boundary regressions included; Python compilation; `git diff --check`; draft
PR #1 safety-floor ancestry. No provider, queue, Telegram, subprocess, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.
## 2026-07-18 - ThreadKeeper provider payload type validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`9b5dc2a`. Provider payloads are now authenticated before they enter the worker
protocol or dispatch accounting. Native and OpenAI-compatible responses must
contain string content and non-negative integer token counts (with absent usage
remaining compatible as zero); booleans, strings, negative counters, malformed
native response/message objects, and structured non-string content fail closed
as `provider_response_invalid`. Usage is logged only after validation.

Checks: four focused provider-boundary regressions; combined provider-free
subagent/budget gate (`382 passed`); Python compilation; `git diff --check`;
draft PR #1 safety-floor ancestry. The first focused-check command used an
incorrect relative venv path and exited 127 before collection; the corrected
absolute project-venv command passed. No provider, queue, Telegram, subprocess,
paid compute, secret/access/security change, push, merge, force-push, or remote
ref deletion occurred.
## 2026-07-18 - Disposition score perturbation calibration

Completed the next provider-free slice above the disposition appraisal gate.
Five preregistered synthetic admitted-evidence archetypes were exhaustively
perturbed over `{-0.03, 0, +0.03}^4` (405 samples). All four clear cases kept
their expected recommendation in 81/81 samples. The conflicting stop/hold case
remained adjudicated in 72/81 samples and otherwise resolved only to its
nominal top action; no decisive recommendation jumped to another decisive
action. The replay digest is
`sha256:b43be1f443b8576f6a50a3ce4d7923ba0c43a07b473ec42a4a43d1b92d1ed1d0`.

The validator passed 15/15 checks and four unit tests. This does not establish
calibration on operational evidence. Before any canary, the next evidence step
is a separately reviewed, redacted offline corpus derived from immutable
evidence packets with preregistered labels. No live state, memory, provider,
queue, supervisor, Telegram, runtime, secret, access, or paid-compute effect
occurred.
## 2026-07-18 - ThreadKeeper ambiguous provider choices

Continued the draft-PR-#1-derived hardening branch with commit `e41d33f`.
OpenAI-compatible provider responses must now contain exactly one choice;
multiple-choice responses fail closed as authenticated
`provider_response_invalid` outcomes after one call instead of silently
selecting the first candidate. Three focused checks and the combined
provider-free subagent/budget gate (`390 passed`) passed, along with Python
compilation, `git diff --check`, and PR #1 safety-floor ancestry. No provider,
queue, Telegram, paid compute, secrets/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-19 - ThreadKeeper unfinished provider responses

Commit `5bfa906` on `agent/threadkeeper-hardening-next` closes a provider-boundary
truncation gap. An explicit native Ollama `done=false` response or an
OpenAI-compatible choice with a non-`stop` finish reason can no longer pass
partial text into ThreadKeeper's textual tool parser. Both return the private
`provider_response_invalid` control outcome after one call. Providers omitting
finish metadata remain compatible. Four focused regressions, Python compilation,
`git diff --check`, and the combined provider-free subagent/budget gate (`400
passed`) succeeded. No provider, live runtime, Telegram, paid compute, secret or
access change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-19 - ThreadKeeper provider refusal/error signals

Commit `b9b547c` on `agent/threadkeeper-hardening-next` closes a provider-
boundary ambiguity after the completion-marker work. A native Ollama response
with a non-null top-level `error`, or an OpenAI-compatible message with a
non-null `refusal`, now becomes an authenticated `provider_response_invalid`
outcome after one call even if the provider also supplies apparently completed
tool-shaped content. Refusal/error content cannot reach ThreadKeeper's textual
tool parser or consume retry allowance.

Two focused regressions, Python compilation, `git diff --check`, the combined
provider-free subagent/budget gate (`406 passed`), and draft PR #1 safety-floor
ancestry passed. No live provider, queue/runtime, Telegram, subprocess worker,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.
# 2026-07-19 - Reject truncated native completion reasons

ThreadKeeper commit `a83f0a4` on `agent/threadkeeper-hardening-next` closes a
native-provider completion gap: Ollama can report `done=true` with
`done_reason=length`, which is terminal but truncated. Explicit non-`stop`
reasons now return authenticated `provider_response_invalid` control outcomes
without retry, preventing partial tool-shaped text from entering worker
protocol. Omitted `done_reason` remains compatible with older providers.

Verification passed eight focused completion-boundary tests, Python
compilation, `git diff --check`, PR #1 ancestry, and the combined provider-free
subagent/budget gate (`408 passed`). An initially mistyped relative venv path
and then a stale budget-test filename failed before test collection; the
corrected established checks passed. No live provider, paid compute, secrets,
access/security changes, push, merge, force-push, or remote-ref deletion.
# 2026-07-19 - Native provider model-identity binding

ThreadKeeper commit `476a475` on `agent/threadkeeper-hardening-next` now
rejects an explicit native-provider response model that differs from the
requested model, including malformed falsey/non-string values. Omitted model
metadata remains compatible. Rejection is an authenticated
`provider_response_invalid` control outcome and consumes no retry allowance,
so content cannot be executed or usage attributed under the wrong requested
route. Six focused checks, Python compilation, `git diff --check`, and the
combined provider-free subagent/budget gate (`412 passed`) succeeded. An
initial gate command used a nonexistent budget-test filename; the corrected
established gate passed. No live provider, queue, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-19 disposition split input binding

- Hardened the synthetic-only split preregistration so every report carries a
  canonical `input_corpus_sha256` binding the complete input document.
- Assignment continues to hash only the scoped seed and immutable task-version
  digest. Relabeling, reviewer changes, or record reordering cannot move a
  record between splits, but they now change the corpus provenance digest.
- Provider-free verification passed 12 unit tests plus compile, fixture replay,
  JSON parsing, and scoped `git diff --check`.
- This remains offline evidence only; it grants no operational corpus,
  provider, canary, or runtime authority.
# 2026-07-19 - OpenAI-compatible choice-index validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`5127c89`. When an OpenAI-compatible provider supplies an index for the single
required response choice, it must be the integer zero. Nonzero, negative,
boolean, string, and fractional indices now return the private
`provider_response_invalid` control result without retry; omitted index
metadata remains compatible.

Eight focused checks and the combined provider-free subagent/budget gate (`436
passed`) passed, along with Python compilation and `git diff --check`. The first
focused invocation exposed two test assertions inserted across an existing test
boundary; the assertions were relocated and the complete gate then passed. No
provider, queue, Telegram, paid compute, secrets/access change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-19 - Provider-native tool-field presence validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`4e06b2d`. Native Ollama and OpenAI-compatible provider responses now reject
explicit falsey `tool_calls` and deprecated `function_call` fields instead of
treating them as absent. Only omission/null represents no provider-native tool
request, keeping ThreadKeeper's validated textual tool protocol as the sole
execution path.

Eight focused regressions and the combined provider-free subagent/budget gate
(`444 passed`) passed, along with Python compilation and `git diff --check`.
An initial combined-gate command named a stale budget-test path and failed
before collection; the corrected repository test path passed. No provider,
queue, Telegram, paid compute, secrets/access change, push, merge, force-push,
or remote-ref deletion occurred.
## 2026-07-19 - Synthetic disposition split adequacy

Archived `artifacts/ggb-capacity-gates/20260719-disposition-split-adequacy/`.
The provider-free validator closes an evaluation-design gap left by deterministic
hash assignment: it requires exact corpus/assignment identity, at least four
records in each partition, and coverage of `hold`, `request_cancel`,
`fail_terminal`, and `expire` in development, calibration, and held-out test.
Eight unit tests and Python compilation pass. Constructed fixtures only; no
operational evidence selection/redaction, scorer fitting, runtime behavior,
provider, Telegram, memory write, push, or merge.
# 2026-07-19 - OpenAI-compatible response object binding

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f7df01a`. Explicit OpenAI-compatible response `object` metadata must now equal
`chat.completion`; wrong-type, empty, boolean, numeric, list, and mapping values
become private `provider_response_invalid` outcomes without consuming retry
allowance. Omitted metadata remains compatible with older SDK fixtures.

Eight focused checks and the combined provider-free subagent/budget gate (`457
passed`) passed, along with Python compilation and `git diff --check`. An
initial combined invocation named a nonexistent legacy budget-test path; the
correct established gate then passed. No provider, queue, Telegram, paid
compute, secrets/access change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-19 - OpenAI-compatible response timestamp validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`67f3576`. Explicit OpenAI-compatible completion `created` metadata must now be
a non-negative integer Unix timestamp. Negative, boolean, fractional, string,
list, and mapping values return the private `provider_response_invalid` control
result immediately and do not consume transport retries; omitted metadata
remains compatible.

Nine focused checks and the combined provider-free subagent/budget gate (`469
passed`) passed, along with Python compilation and `git diff --check`. One
initial combined invocation exhausted the persistent test rate-limit ledger;
the established provider-free gate was rerun with rate limiting explicitly
disabled and passed. No provider, queue, Telegram, paid compute, secrets/access
change, push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-20 - Native provider creation-timestamp validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`b4bb993`. Explicit native Ollama `created_at` metadata must now be a
non-empty, timezone-aware ISO/RFC 3339 timestamp. Boolean, numeric, empty,
malformed, collection, and timezone-free values return the private
`provider_response_invalid` control result without retry; omitted timestamps
remain compatible.

Ten focused checks, Python compilation, `git diff --check`, PR #1 safety-floor
ancestry, and the combined provider-free subagent/budget gate (`471 passed`)
passed. The first combined invocation hit the persistent default test rate
ledger; the established provider-free gate passed with calls-per-minute
disabled and an isolated run directory. No provider, live queue/runtime,
Telegram, paid compute, secrets/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-20 - Provider-free motivation-state replay gate

Materialized the Bach/MetaMo next gate at
`artifacts/ggb-capacity-gates/20260720-motivation-state-replay/`. A pinned
synthetic `petta-memory`-shaped snapshot deterministically updates competence
and uncertainty-reduction needs plus six bounded modulators, then ranks fixed
GoalChainer-shaped candidates. The bounded evidence-inspection candidate ranks
first; every output remains candidate-only, adjudication-required, and records
ThreadKeeper effect `none`. Seven unit tests and Python compile pass, covering
replay determinism, full packet/candidate order invariance, evidence-identity
mutation rejection, stale/missing temporal provenance, finite/range rejection,
and monotonic information-seeking under higher uncertainty urgency. Updated
the concise and long GGB roadmaps; the next offline slice is multi-event decay
and restart equivalence. No memory write/promotion, task claim/enqueue, live
runtime/provider/Telegram action, secret access, paid compute, push, merge, or
runtime authority change.
## 2026-07-20 - Native provider duration-metadata validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`bcbae5e`. Explicit native Ollama `total_duration`, `load_duration`,
`prompt_eval_duration`, and `eval_duration` metadata must now be non-negative
integers. Boolean, negative, fractional, string, and null values return the
private `provider_response_invalid` control result without retry; omitted
duration fields remain compatible.

Eight focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the combined provider-free gate (`479 passed`)
passed. An initial combined invocation exposed an existing order-dependent
test rate-ledger leak in two older tests; the established gate passed with
calls-per-minute disabled. No provider, live queue/runtime, Telegram, paid
compute, secrets/access/security change, push, merge, force-push, or remote-ref
deletion occurred.
# 2026-07-20 - Motivation temporal replay gate

Materialized the next provider-free GGB motivation slice at
`artifacts/ggb-capacity-gates/20260720-motivation-temporal-replay/`. Three
strictly timed synthetic events apply bounded decay to two needs. A self-hashed
checkpoint after two events reproduces the uninterrupted final state and
ranking after restart; mutation and non-monotonic time fail closed. A final
clock-only event leaves `inspect_bounded_evidence` top-ranked. Six unit tests
and Python compilation pass. All recommendations remain adjudication-required
candidates with ThreadKeeper effect `none`; no live/runtime/memory effects or
remote operations occurred.
# 2026-07-20 - Native provider model-presence validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`4d04499`. Native Ollama response model metadata is now presence-sensitive:
an explicitly supplied JSON null can no longer be treated like omitted
metadata and instead returns the private `provider_response_invalid` control
result without retry. Omitted metadata remains compatible.

Seven focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the combined provider-free gate (`500 passed`)
passed. One initial combined invocation used a stale rate ledger and exposed
the known order-dependent test isolation issue; the established gate passed
with calls-per-minute disabled. No provider, queue, Telegram, paid compute,
secrets/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-20 - Native provider completion-reason presence validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`16100b6`. Native Ollama `done_reason` metadata is now presence-sensitive:
explicit JSON null can no longer masquerade as omitted metadata and instead
returns the private `provider_response_invalid` control result without retry.
Omission remains compatible.

Four focused checks, Python compilation, `git diff --check`, PR #1
safety-floor ancestry, and the combined provider-free gate (`503 passed`)
passed. The first combined invocation hit the known order-dependent rate-ledger
test isolation issue in two older cases; the established gate passed with
calls-per-minute disabled. No provider, queue, Telegram, paid compute,
secrets/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-20 - Native provider message-role presence validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`5bb8af3`. Native Ollama responses that explicitly supply `message.role` must
now use `assistant`; JSON null can no longer pass as if the field were omitted.
Malformed authenticated responses fail closed as `provider_response_invalid`
without consuming retry allowance, while omission remains compatible.

The focused regression passed (1 test). The combined provider-free
subagent/budget gate passed 504 tests with
`OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=0`, plus Python compilation and
`git diff --check`. A first combined invocation named a nonexistent budget-test
file; the corrected invocation then hit the persistent local rate-limit state
in two pre-existing cases, so deterministic replay explicitly disabled that
guard. Draft PR #1 safety-floor ancestry passed. No provider, queue, Telegram,
paid compute, secrets/access change, push, merge, force-push, or remote-ref
deletion occurred.
## 2026-07-20 - Native provider message-schema allowlist

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a450d82`. Native Ollama response messages now reject every field outside the
explicitly handled role/content/thinking/images/tool-call compatibility schema,
including null and falsey unknown values. This closes ignored message-level
payload channels while retaining the already validated standard fields.

Twelve focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`518 passed`, rate limiter disabled) passed.
No provider, queue, Telegram, paid compute, secrets/access change, push, merge,
force-push, or remote-ref deletion occurred.
## 2026-07-20 - Native provider top-level response allowlist

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`b059a8d`. Native Ollama responses now reject every top-level field outside the
explicitly handled response schema, including null and falsey unknown values.
This closes ignored alternate payload channels while retaining the validated
message, completion, timing, context, error, and token-accounting fields.

Eight focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`522 passed`, rate limiter disabled) passed.
No provider, queue, Telegram, paid compute, secrets/access change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-21 - OpenAI-compatible annotation rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3beac3b`. OpenAI-compatible assistant responses carrying non-null
`annotations`, including explicit falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents an
ignored citation/annotation side channel from accompanying content admitted to
ThreadKeeper's textual tool protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`531 passed`, rate limiter disabled)
passed. The first combined invocation named a stale budget-test filename; the
corrected established gate passed. No provider, queue, Telegram, paid compute,
secrets/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-21 - OpenAI-compatible reasoning-content rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`49a8a17`. OpenAI-compatible assistant responses carrying non-null
`reasoning_content`, including explicit falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents an
ignored hidden-reasoning channel from accompanying content admitted to
ThreadKeeper's textual tool protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`535 passed`, rate limiter disabled)
passed. The first combined invocation named a stale budget-test filename; the
corrected established gate passed. No provider, queue, Telegram, paid compute,
secrets/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

# 2026-07-21 - OpenAI-compatible assistant-name rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`78d6224`. OpenAI-compatible assistant responses carrying non-null message
`name` metadata, including explicit falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents an
alternate message identity from accompanying content admitted to
ThreadKeeper's textual tool protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`539 passed`, rate limiter disabled)
passed. One initial combined invocation used the wrong rate-limit environment
key and hit the intended limiter; rerunning with the established key passed.
No provider, queue, Telegram, paid compute, secrets/access/security change,
push, merge, force-push, or remote-ref deletion occurred.
# 2026-07-21 - OpenAI-compatible service-tier rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`ef2b8f4`. OpenAI-compatible responses carrying non-null `service_tier`
metadata, including explicit falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents
unrequested provider scheduling-class metadata from being silently ignored
beside content admitted to ThreadKeeper's textual protocol.

Four focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`551 passed`, rate limiter disabled)
passed. No provider, queue, Telegram, paid compute, secrets/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
# 2026-07-21 - OpenAI-compatible choice-logprobs rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`af147ac`. OpenAI-compatible responses carrying non-null choice `logprobs`
metadata, including explicit falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents an
ignored token-probability output channel from accompanying content admitted to
ThreadKeeper's textual tool protocol.

Four focused checks, Python compilation, `git diff --check`, PR #1 safety-floor
ancestry, and the combined provider-free subagent/budget gate (`555 passed`,
rate limiter disabled) passed. The first combined invocation named a stale
budget-test filename; the corrected established gate passed. No provider,
queue, Telegram, paid compute, secrets/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
## 2026-07-21 - ThreadKeeper choice content-filter metadata rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3030a6a`. OpenAI-compatible choices carrying non-null
`content_filter_results`, including falsey values, now return the private
`provider_response_invalid` control result without retry. This prevents
unpersisted provider moderation metadata from silently accompanying text
admitted to ThreadKeeper's textual protocol.

Four focused checks and the provider-free subagent/budget gate (`559 passed`,
rate limiter disabled) passed, along with Python compilation and
`git diff --check`. An initial combined invocation named a stale budget-test
file; a second used the wrong rate-limit environment key and exposed the known
persistent ledger. The corrected established gate passed. PR #1 safety-floor
ancestry remains intact. No provider, live queue/runtime, Telegram, paid
compute, secrets/access/security change, push, merge, force-push, or remote-ref
deletion occurred.
## 2026-07-21 - ThreadKeeper prompt-filter metadata rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`de49e1c`. OpenAI-compatible responses carrying non-null top-level
`prompt_filter_results`, including explicit falsey values, now fail closed as
private `provider_response_invalid` outcomes without retry. This prevents an
ignored prompt-side moderation metadata channel from accompanying content
admitted to ThreadKeeper's textual protocol.

Four focused checks and the provider-free subagent/budget gate with
`OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=0` (`563 passed`) passed, along with
Python compilation and `git diff --check`. One initial combined invocation
used a stale budget-test filename and a second used the wrong rate-limit env
key; the corrected established gate passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-21 - OpenAI-compatible parsed-payload rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f711a73`. OpenAI-compatible assistant messages carrying a non-null SDK
`parsed` payload now fail closed as private `provider_response_invalid`
outcomes without retry, so unsolicited structured output cannot accompany the
validated textual protocol. Four focused checks and the rate-limiter-disabled
provider-free subagent/budget gate (`567 passed`) passed, along with Python
compilation, `git diff --check`, and PR #1 safety-floor ancestry. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-21 - OpenAI-compatible token-detail rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`b990113`. OpenAI-compatible usage records carrying non-null
`prompt_tokens_details` or `completion_tokens_details`, including explicit
falsey values, now fail closed as private `provider_response_invalid` outcomes
without retry. This prevents ignored fine-grained provider accounting from
accompanying the validated aggregate token protocol.

Eight focused checks, Python compilation, `git diff --check`, and the combined
provider-free subagent/budget gate (`571 passed`, LLM calls/minute guard
disabled) passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
## 2026-07-22 - ThreadKeeper provider response metadata rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`ed7283c`. Non-null OpenAI-compatible top-level response `metadata`, including
explicit falsey values, now becomes a private `provider_response_invalid`
outcome without retry. This prevents an unvalidated provider-controlled
metadata channel from accompanying text admitted to ThreadKeeper's protocol.

Four focused checks passed. Python compilation and `git diff --check` passed;
the provider-free subagent/budget gate passed 579 tests with
`OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=0`. An initial combined run used the
wrong limiter variable and hit the persistent test ledger; the documented
rerun passed. No provider, live runtime, Telegram, paid compute, secrets/access
change, push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-22 - ThreadKeeper query/shell boundary-whitespace rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`192ccd2`. External search, Tavily, technical-analysis, and optional-shell
arguments now reject leading or trailing ASCII or Unicode whitespace. This
keeps each accepted command/query identical to its audited and prompt-visible
representation and fails before provider, subprocess, or audit effects.

Twenty-eight focused boundary-whitespace checks, Python compilation,
`git diff --check`, PR #1 safety-floor ancestry, and the provider-free
subagent/budget gate (`632 passed`, LLM calls/minute guard disabled) passed.
No provider, live queue/runtime, Telegram, paid compute, secrets/access change,
push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-22 - Unambiguous run-control paths

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`8402cad`. Queued-task cancellation paths and async-worker stop-file paths now
reject leading or trailing ASCII/Unicode whitespace and require NFC Unicode
normalization. Validation occurs before queue claims, worker-lock creation, or
worker LLM calls, preventing distinct control-token spellings from being
silently trimmed or represented ambiguously in records.

Eight focused checks, Python compilation, `git diff --check`, and the
provider-free subagent/budget gate (`640 passed`, LLM calls/minute guard
disabled) passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
## 2026-07-22 - ThreadKeeper canonical relative path spellings

Continued the draft-PR-#1-derived hardening branch with commit `3ca23e7`,
preserving `fork/agent/threadkeeper-safety-floor` ancestry. File-tool paths and
task-contract `allowed_paths` now require their literal relative spelling to
equal `os.path.normpath` output. Spellings such as `./safe.txt`,
`safe//out.txt`, `safe/./out.txt`, and `safe/` therefore fail before audit,
contract authorization, or filesystem effects instead of naming a normalized
path different from the recorded input.

Twenty-six focused checks, Python compilation, `git diff --check`, and the
provider-free subagent/budget gate (`652 passed`, LLM calls/minute disabled)
passed. An initial combined-gate command referenced a stale budget-test
filename and collected no tests; the corrected repository path passed. No
provider, live queue/runtime, Telegram, paid compute, secrets/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
# 2026-07-22 - Independent fixed-point motivational checkpoint ingest

Added `artifacts/ggb-capacity-gates/20260722-motivation-fixed-point-ingest/` as
a consumer separate from the checkpoint producer. It recomputes the canonical
checkpoint digest and source-fixture SHA-256, then admits only the pinned v0.1
schema, cursor 2, scale 1000, margin 50, and expected trace prefix. Tests prove
checkpoint mutation, stale source identity, scale/margin policy drift, and
trace drift fail closed. Four unit checks, two-file compile, JSON replay, and
scoped diff check passed; report SHA-256 field
`064f3381f6132c5ed6f8856f44c9aa31d79392ec6ce02e687ab725646c77def5`.
No provider/network call, memory write, ThreadKeeper/runtime change, push, or
merge occurred.
# 2026-07-22 - ThreadKeeper Windows device-name path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2e003c3`. File-tool paths and task-contract `allowed_paths` now reject
case-insensitive Windows reserved device components, including device names
with extensions (`CON.txt`, `COM1.log`). This prevents a path audited as an
ordinary workspace file on POSIX from resolving as a device on Windows.

Twenty-three focused checks and the full provider-free hardening suite (`679
passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. The first compile invocation used the
unavailable `python` executable after pytest had passed; rerunning with
`python3` passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-23 - ThreadKeeper Windows-trimmed component rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`049939b`. File-tool paths and task-contract `allowed_paths` now reject any
component ending in a dot or space. This prevents Windows from silently
trimming an audited spelling such as `report.txt.` or `safe /report.txt` into
another path.

Forty focused checks and the full provider-free hardening suite (`691 passed`,
LLM calls/minute guard disabled) passed, along with Python 3 compilation and
`git diff --check`. One initial focused command referenced a nonexistent local
`.venv`; the installed provider-free pytest command then ran successfully. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
# 2026-07-23 - ThreadKeeper invisible path-joiner rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`31e3cdd`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. File-tool
paths and task-contract `allowed_paths` now reject the otherwise permitted
Unicode format joiners U+200C/U+200D. These invisible, filename-significant
characters can no longer create audited path spellings that visually collapse
to different filesystem names.

Eight focused checks and the provider-free subagent/budget gate (`724 passed`,
LLM calls/minute guard disabled) passed, along with Python compilation and
`git diff --check`. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-23 - Windows-forbidden filename-character rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`638618b`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool paths and task-contract `allowed_paths` now reject `<`, `>`, `"`,
`|`, `?`, and `*`. POSIX can otherwise admit these Windows-forbidden filename
characters, creating non-portable audited paths and wildcard/redirection-like
spellings at downstream boundaries.

Twenty-four focused checks and the provider-free subagent/budget gate (`748
passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. An initial post-suite compilation command
used unavailable `python`; the corrected `python3` check passed. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.
# 2026-07-23 - ThreadKeeper variation-selector path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f9f04e0`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool paths and task-contract `allowed_paths` now reject Unicode variation
selectors U+FE00--U+FE0F and U+E0100--U+E01EF. These invisible,
filename-significant code points can no longer create audited spellings that
render identically while naming different files.

Twelve focused checks and the full provider-free hardening suite (`751 passed`,
LLM calls/minute guard disabled) passed, along with Python 3 compilation and
`git diff --check`. The first focused command used unavailable `python`; the
corrected installed venv/Python 3 checks passed. No provider, live
queue/runtime, Telegram, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

# 2026-07-23 - ThreadKeeper Mongolian variation-selector path rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f8e9691`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool paths and task-contract `allowed_paths` now also reject the Mongolian
free variation selectors U+180B--U+180D and U+180F. This closes the remaining
standard Unicode variation-selector range that could create invisible,
filename-significant differences in audited paths.

Twenty-eight focused checks and the full provider-free hardening suite (`767
passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. The first focused command used unavailable
`python` and therefore ran no tests; the corrected `python3` commands passed.
No provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

# 2026-07-23 - Cross-producer motivational registry canonicalization

Added a provider-free candidate-only gate at
`artifacts/ggb-capacity-gates/20260723-motivation-cross-producer-canonicalization/`.
Two manually independent JSON serializations have different raw bytes but
canonicalize to the previously admitted candidate-set SHA-256
`7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`.
Five unit checks cover convergence and fail-closed semantic mutation,
action-authority widening, unknown fields, and candidate reordering. Python
compilation and JSON report replay passed. No provider/network call, producer
code import, memory mutation, task claim, ThreadKeeper/runtime change,
Telegram egress, paid compute, push, or merge occurred.

# 2026-07-23 - ThreadKeeper Unicode separator compatibility rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2f749e3`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool and task-contract paths now reject U+FE68 SMALL REVERSE SOLIDUS,
U+FF0F FULLWIDTH SOLIDUS, and U+FF3C FULLWIDTH REVERSE SOLIDUS. These
characters can no longer be recorded as ordinary filename text and later
compatibility-normalized into path separators by a downstream consumer.

Twelve focused checks and the provider-free subagent/budget hardening gate
(`792 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

# 2026-07-23 - ThreadKeeper forbidden-filename compatibility rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3f2280a`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool and task-contract paths now reject Unicode characters whose NFKC
forms contain `:`, `<`, `>`, `"`, `|`, `?`, or `*`, including small-form and
fullwidth punctuation. These characters can no longer be audited as ordinary
filename text and later compatibility-normalized into alternate-stream or
Windows-forbidden filename syntax.

Thirty-six focused checks and the provider-free subagent/budget hardening gate
(`864 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation and `git diff --check`. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.

# 2026-07-23 - ThreadKeeper compatibility device-name rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`3bd18da`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
File-tool paths and task-contract `allowed_paths` now reject components whose
NFKC form becomes a canonical Windows device name. Fullwidth and
subscript-digit aliases such as `ＣＯＮ.txt`, `ＣＯＭ１.log`, and `ＬＰＴ₉.txt`
can no longer pass validation under one audited spelling and later normalize
into reserved device syntax.

Forty-four focused checks and the provider-free hardening suite (`867 passed`,
LLM calls/minute guard disabled) passed, along with Python 3 compilation and
`git diff --check`. An initial full-suite invocation hit the expected
persistent local calls/minute ledger (`90 failed, 777 passed`); the established
guard-disabled rerun passed. No provider, live queue/runtime, Telegram, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

# 2026-07-24 - ThreadKeeper embedded separator compatibility rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`0dbd260`, preserving the completed safety-floor ancestry. The shared
file-tool/task-contract path validator now rejects any non-separator Unicode
character whose NFKC form contains `/` or `\`, rather than only characters
whose complete normalized form equals one separator. This closes the missed
symbols ℀, ℁, ℅, and ℆, which normalize to `a/c`, `a/s`, `c/o`, and `c/u`.

Twenty-eight focused checks and the provider-free subagent/budget hardening
gate (`925 passed`, LLM calls/minute guard disabled) passed, along with Python
3 compilation and `git diff --check`. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.

# 2026-07-24 - ThreadKeeper invisible Unicode filler rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`0cf8295`, preserving the completed safety-floor ancestry. The shared
file-tool/task-contract path validator now rejects U+034F COMBINING GRAPHEME
JOINER, U+115F HANGUL CHOSEONG FILLER, U+1160 HANGUL JUNGSEONG FILLER,
U+3164 HANGUL FILLER, and U+FFA0 HALFWIDTH HANGUL FILLER. These visually empty
non-format characters can no longer distinguish a filesystem path while
remaining hidden in prompts and audit records.

Twenty focused checks and the provider-free subagent/budget hardening gate
(`945 passed`, LLM calls/minute guard disabled) passed, along with Python 3
compilation, `git diff --check`, and completed safety-floor ancestry. An
initial full-suite invocation used the wrong guard environment variable and
hit the expected persistent local calls/minute ledger (`90 failed, 855
passed`); the corrected established invocation passed. No provider, live
queue/runtime, Telegram, paid compute, secret/access/security change, push,
merge, force-push, or remote-ref deletion occurred.

# 2026-07-24 - ThreadKeeper invisible Khmer path-control rejection

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`f5e873d`, preserving the completed safety-floor ancestry. The shared
file-tool/task-contract path validator now rejects U+17B4 KHMER VOWEL INHERENT
AQ and U+17B5 KHMER VOWEL INHERENT AA. These visually empty characters are
classified as combining marks rather than format characters, so they bypassed
the existing Unicode-format guard.

Twenty-eight focused checks and the provider-free subagent/budget hardening
gate (`953 passed`, LLM calls/minute guard disabled) passed, along with Python
3 compilation, `git diff --check`, and completed safety-floor ancestry. The
first focused invocation named a nonexistent virtualenv and failed before test
collection; the established local ThreadKeeper pytest environment then passed.
No provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

# 2026-07-24 - Strict JavaScript motivational-registry consumer

Added a separately implemented provider-free Node.js consumer at
`artifacts/ggb-capacity-gates/20260724-motivation-strict-javascript-consumer/`.
Its recursive raw-JSON parser rejects duplicate members at registry, candidate,
and nested-contract depths, three noncanonical numeric spellings, non-NFC text,
control/format text, and lone surrogates before independently applying the
closed semantic, nested-digest, ordering, and action-authority contracts.

Both byte-distinct producer fixtures reproduce candidate-set SHA-256
`7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`.
Ten checks, two Node syntax checks, and direct replay pass. This supplies a
second language/runtime boundary for the next per-consumer byte-preflight
admission contract. Candidate-only; ThreadKeeper effect `none`. No provider,
network, Telegram, memory write, live task claim/runtime change, secret,
paid compute, push, or merge occurred.
# 2026-07-24 - ThreadKeeper tool-call record-shape preflight

Continued the draft-PR-#1-derived hardening branch with commit `896f0bf`.
`run_tools` now requires a list batch whose entries are exact two-field
`(name, arguments)` tuples before it unpacks or executes any record. A
malformed later record therefore cannot raise after bypassing the intended
complete-batch safety boundary, and an earlier valid file/provider/subprocess
effect remains unexecuted.

Four focused checks, Python compilation, `git diff --check`, remote PR #1
safety-floor ancestry, and the provider-free hardening suite (`962 passed`,
LLM calls/minute guard disabled) passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
# 2026-07-24 - Canonical Unicode final emit boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2bad03e`. The dedicated final `emit` validator now rejects lone Unicode
surrogate code points and non-NFC text before returning a successful structured
parent digest or recording a successful transcript. This closes a validation
gap created because final emits terminate before the ordinary tool execution
path.

Two focused checks and the provider-free hardening suite (`959 passed`, LLM
calls/minute guard disabled with the documented environment key) passed,
together with Python compilation, `git diff --check`, and remote PR #1
safety-floor ancestry. An initial full-suite invocation used the wrong
rate-limit environment key and also exposed one expected assertion that needed
the new specific surrogate diagnostic; the corrected suite passed. No provider,
network, Telegram, live queue/runtime, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

# 2026-07-25 - ThreadKeeper dispatch parser-output preflight

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a43aa39`. `dispatch()` now validates that parser output is a list of exact
two-field tuples with string tool names and list argument containers before it
destructures the batch for transcript recording or final-emit handling.
Malformed parser output therefore becomes a persistent structured
`skill_protocol_error` rather than an uncaught unpacking/type error.

Five focused checks, Python compilation, `git diff --check`, and the full
provider-free hardening suite (`964 passed`, LLM calls/minute guard disabled)
passed. No provider, network, Telegram, live queue/runtime, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

# 2026-07-25 - ThreadKeeper exact parser-container boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`cbbc36f`. The closed parser-output preflight now requires exact built-in
`list`, `tuple`, and `str` types, rejecting behavior-bearing subclasses before
destructuring, transcript normalization, or any tool effect. Rejections remain
persistent structured `skill_protocol_error` records.

Nine focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`968 passed`, LLM calls/minute guard disabled)
passed. An initial full-suite invocation used the wrong rate-limit environment
key and hit the existing persistent 60-call ledger; the corrected documented
key passed. No provider/network/Telegram call, paid compute, secret/access
change, push, merge, force-push, or remote-ref deletion occurred.

# 2026-07-25 - ThreadKeeper exact parser argument-value boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`814be73`. The complete parser-output batch preflight now requires every
argument value to be an exact built-in string. A behavior-bearing string
subclass or other non-string value cannot reach emit handling, transcript
normalization, or tool execution, and a malformed later call prevents an
earlier valid tool from taking effect. Failures persist as structured
`skill_protocol_error` records.

Six focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite (`983 passed`, LLM calls/minute guard disabled
with `OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=0`) passed. The first full-suite
invocation used the wrong environment key and hit the persistent 60-call
ledger; it also identified one prior non-string-emit assertion whose expected
failure stage moved to the earlier parser boundary. The corrected suite
passed. No provider/network/Telegram call, live queue/runtime, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-25 - Exact provider-content string boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`1d830c9`, preserving the completed safety-floor ancestry. The authenticated
provider payload validator now accepts only exact built-in string content.
Behavior-bearing `str` subclasses fail closed as private
`provider_response_invalid` control results before parser, prompt-building,
bounding, or transcript-persistence operations can invoke subclass behavior.

Two focused checks and the full provider-free subagent hardening suite passed
(`978 passed`, LLM calls/minute guard disabled), along with Python compilation
and `git diff --check`. An initial full-suite invocation used the wrong
rate-limit environment key and hit the existing persistent 60-call ledger; the
corrected documented key passed. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.
# 2026-07-25 - ThreadKeeper native-provider metadata exact types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`a8d338b`, preserving completed safety-floor ancestry. Native-provider duration
fields, context containers, and context token IDs now require exact built-in
integer/list types. Behavior-bearing subclasses fail closed as
`provider_response_invalid` before overloaded comparison or iteration can run,
and invalid authenticated responses are not retried.

Twenty-one focused checks and the provider-free subagent/budget hardening gate
(`998 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation and `git diff --check`. An initial broad command named a stale
budget test file and failed before collection; the corrected repository path
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-25 - ThreadKeeper native response container/scalar boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`11c46d6`, preserving the completed safety-floor ancestry. Authenticated
native-provider response and message mappings now require exact built-in
dictionaries, while model, creation-time, role, and completion-reason metadata
require exact built-in strings. Behavior-bearing subclasses fail closed as
`provider_response_invalid` before overloaded iteration, comparison, stripping,
or timestamp normalization can execute.

Six focused checks, Python compilation, `git diff --check`, and the
provider-free subagent/budget hardening gate (`1004 passed`, LLM calls/minute
guard disabled) passed. An initial full-suite command named a stale budget test
file and failed before collection; a second invocation used the wrong
rate-limit environment key and exhausted the persistent test ledger. The
correct established invocation passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge, force-push,
or remote-ref deletion occurred.
# 2026-07-25 - ThreadKeeper native thinking metadata boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`9fda4c5`, preserving the completed safety-floor ancestry. Authenticated native
provider `thinking` metadata must now be null or an exact built-in string.
Behavior-bearing string subclasses fail closed as `provider_response_invalid`
before overloaded equality can run.

Four focused checks and the provider-free subagent/budget hardening gate
(`1005 passed`, LLM calls/minute guard disabled) passed, along with
`git diff --check`. One initial full-suite command named a stale absent budget
test file and failed before collection; the corrected established suite
passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
# 2026-07-25 - ThreadKeeper OpenAI-compatible completion metadata boundary

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`dd251e8`, preserving the completed safety-floor ancestry. Authenticated
OpenAI-compatible completion object/model, finish reason, message role, choice
index, choice containers, and SDK extra-field mappings now require exact
built-in types. Behavior-bearing subclasses fail closed as
`provider_response_invalid` before overloaded comparison, length, or truth
operations can execute.

Seven focused checks, Python compilation, `git diff --check`, and the
provider-free subagent/budget hardening gate (`1012 passed`, LLM calls/minute
guard disabled) passed. The first full-suite command used an incorrect relative
virtualenv path, and the next named a stale budget test file; both failed before
collection of the full gate, and the corrected established invocation passed.
No provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-26 - ThreadKeeper exact task-contract types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`5d964c6`, preserving the completed safety-floor ancestry. Task-contract
mappings, objectives, string-list containers/items, integer/string quotas, and
boolean policy fields now require exact built-in types. Behavior-bearing
subclasses fail closed before overloaded membership, truth, length, string, or
numeric operations can run.

Four focused checks and the provider-free subagent/budget hardening gate
(`1017 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation and `git diff --check`. An initial full-suite command named a stale
budget-test filename and failed before collection; the corrected established
suite passed. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.
## 2026-07-26 - ThreadKeeper exact persona-configuration types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`e67e05e`, preserving the completed safety-floor ancestry. Persona config
containers, nested task contracts, scalar strings, output-token limits, and
default tool lists/items now require exact built-in types. Behavior-bearing
subclasses fail closed during setup before overloaded membership, truth,
length, string, or numeric operations and before any worker/provider call.

Five focused checks and the provider-free subagent hardening gate (`1015
passed`, LLM calls/minute guard disabled) passed, along with Python compilation
and `git diff --check`. No provider, live queue/runtime, Telegram, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.

## 2026-07-26 - ThreadKeeper exact manual-drain quota type

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`c16efa7`, preserving the completed safety-floor ancestry. The bounded manual
queue-drain entrypoint now requires `max_tasks` to be an exact non-negative
built-in integer. Booleans, strings, floats, negative integers, and
behavior-bearing integer subclasses return structured `worker_config_invalid`
without enumerating the queue or invoking a worker.

Seven focused checks and the provider-free subagent/budget hardening gate
(`1034 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation and `git diff --check`. An initial focused command used a
workspace-relative virtualenv path from inside the repository and failed
before test collection; the corrected relative path passed. No provider,
live queue/runtime, Telegram, paid compute, secret/access/security change,
push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-26 - ThreadKeeper exact queued-dispatch path type

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`896a38e`, preserving the completed safety-floor ancestry. The operator-facing
`run_queued_dispatch(queue_path)` boundary now requires an exact non-empty
built-in string. Non-string values and behavior-bearing string subclasses fail
closed as structured `queue_worker_error` results before truth testing, string
coercion, queue-directory access, task claim, or worker/provider effects.

Nine focused checks and the provider-free subagent/budget hardening gate (`1047
passed`, LLM calls/minute guard disabled) passed, along with Python compilation
and `git diff --check`. An initial focused command used the unavailable
`python` alias and failed before collection; the Python 3 rerun passed. No
 provider, live queue/runtime, Telegram, paid compute, secret/access/security
 change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-27 - Motivational feature-interaction preregistration

Archived
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-feature-interaction-preregistration/`.
The content-addressed contract binds score-policy v0.1 and the prior independent
boundary runner, then seals seven out-of-sample multi-feature cases before
execution. It covers the answer/defer crossover immediately below, at, and
above equality, an answer/request tie, joint high-feature cases, and the
review-risk override against a higher request score.

The gate also exposes a structural reachability limitation:
`score(inspect_evidence) = review_risk - evidence_sufficiency` is always at
most `score(defer_for_review) = review_risk`; when equal, the tie order selects
defer. Thus `inspect_evidence` cannot be selected anywhere in the admitted
feature domain under v0.1. This is a preregistered diagnostic, not calibration
evidence or approval to change policy/runtime behavior.

Nine provider-free checks, Python compilation, and diff checks pass. Contract
SHA-256:
`1a7c0b3c60d9d3c66e3df415825b1a6b7fb5301cdd3df64d662ee6addfec258c`.
No provider/network/Telegram call, queue claim, memory write, runtime wiring,
policy change, paid compute, secret access, push, or merge occurred.

## 2026-07-27 - ThreadKeeper operator path argument types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`e834d39`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. The
parent/operator run-index audit and candidate transcript review entry points
now reject non-string values and behavior-bearing string subclasses before
truth testing, coercion, or filesystem path resolution. The shared worker
stop/cancel-file resolver similarly requires an exact built-in string or null;
a hostile stop-file subclass now returns `worker_config_invalid` before lock
acquisition.

Eight focused checks and the provider-free subagent/budget hardening gate
(`1054 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation, `git diff --check`, and completed safety-floor ancestry. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-27 - ThreadKeeper candidate review record validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`4a141fd`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. The
read-only candidate transcript review now validates the exact JSON types of
every field used to present a patch/adjudication decision: transcript
container, status/summary strings, task-contract and adjudication objects,
boolean review flags, patch-proposal list/object shapes, and proposal
action/path strings. Malformed persisted records return
`candidate_review_error` rather than being truth-tested, sliced, skipped, or
presented as review-ready.

Fifteen focused checks and the provider-free subagent/budget hardening gate
(`1063 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation, `git diff --check`, and completed safety-floor ancestry. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-27 - ThreadKeeper direct tool-runner control types

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`9091e2e`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. The
direct `run_tools()` boundary now validates the call batch's exact list type
before truth testing. It also requires exact built-in list/tuple/set
authorization containers with exact string items, and an optional exact
non-negative integer quota, before iteration, membership, comparison, or
coercion. Behavior-bearing subclasses therefore fail closed before registry,
workspace, cancellation, or tool effects.

Nine focused checks and the provider-free subagent/budget hardening gate (`1051
passed`, LLM calls/minute guard disabled) passed, along with Python compilation
and `git diff --check`. The completed safety-floor branch is an ancestor of the
new commit. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-27 - ThreadKeeper persisted run-index entry validation

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`8669f16`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. The
read-only run-index auditor now validates each decoded entry before hashing,
normalizing hash fields, resolving transcript paths, or reading transcripts.
Entries must be exact JSON objects; identity, status, path, and hash fields
must be exact strings; timestamps must be finite numbers or null. Invalid JSON
retains its distinct diagnostic, while wrong persisted field types fail closed
as `invalid_index_entry:ValueError`.

Fourteen focused checks and the provider-free subagent/budget hardening gate
(`1064 passed`, LLM calls/minute guard disabled) passed, along with Python
compilation, `git diff --check`, and completed safety-floor ancestry. No
provider, live queue/runtime, Telegram, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.

## 2026-07-27 - ThreadKeeper strict persona configuration JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`6f4f10d`, preserving `fork/agent/threadkeeper-safety-floor` ancestry. Persona
configuration files now use the shared strict JSON decoder, so duplicate
object keys and Python-accepted `NaN`/`Infinity` tokens fail closed as
malformed JSON before provider/model selection, default-tool or task-contract
processing, escalation, or worker/provider calls.

Three new malformed-file cases and nine focused checks passed. The
provider-free subagent/budget hardening gate passed all 1077 tests with the
LLM calls/minute guard disabled, along with Python compilation,
`git diff --check`, and completed safety-floor ancestry. An initial focused
command used unavailable `python`; rerunning with the installed `python3`
passed. The first full-suite run exposed four test doubles still patching the
permissive decoder; updating them to patch the strict boundary made the full
gate pass. No provider, live queue/runtime, Telegram, paid compute,
secret/access/security change, push, merge, force-push, or remote-ref deletion
occurred.

## 2026-07-27 - ThreadKeeper strict persisted LLM quota state

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`d6b1b96`, preserving `fork/agent/threadkeeper-safety-floor` ancestry.
Persisted rate-limit and concurrency-control state now uses the shared strict
JSON decoder. Duplicate object keys and Python-accepted `NaN`/`Infinity`
tokens fail closed before quota reservation or any provider call, and the
malformed state remains untouched for diagnosis.

Eight focused checks and the provider-free subagent/budget hardening gate
(`1083 passed`, LLM rate and concurrency guards disabled outside their focused
tests) passed, along with Python compilation, `git diff --check`, and completed
safety-floor ancestry. The first full-suite invocation left the default
concurrency guard enabled and encountered pre-existing persistent in-flight
test state; rerunning with both external guards disabled, while their focused
tests explicitly enabled them, passed. No provider, live queue/runtime,
Telegram, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
## 2026-07-27 - ThreadKeeper strict async-worker lock metadata JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`1bd8008`, preserving the completed safety-floor ancestry. Persisted
async-worker lock metadata now uses the shared strict JSON decoder, so
duplicate object keys and Python's non-standard `NaN`/`Infinity` tokens fail
closed as absent stale-lock metadata rather than influencing operator-facing
diagnostics.

Three new malformed-record cases and six focused checks passed. The
provider-free hardening suite passed with both LLM rate and concurrency guards
disabled (`1084 passed`), along with Python compilation and `git diff --check`.
The first focused invocation used a nonexistent repository-local virtualenv
and failed before collection. The first full-suite invocation inherited a
stale concurrency ledger and produced 10 `concurrency_limited` failures; the
corrected documented guard settings passed. No provider/network/Telegram
call, queue claim, runtime wiring, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-27 - ThreadKeeper strict budget usage-ledger JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`749cc91`, preserving the completed safety-floor ancestry. Persisted budget
usage-ledger JSONL records now use a strict decoder, so duplicate object keys
and Python's non-standard `NaN`/`Infinity` tokens are ignored as malformed
records instead of influencing thread token totals or cost estimates. Valid
neighboring records remain available.

Fourteen focused checks passed. The provider-free hardening suite passed with
both LLM rate and concurrency guards disabled (`1085 passed`), along with
Python compilation and `git diff --check`. An initial focused command named a
nonexistent repository-local virtualenv and failed before collection. An
initial full-suite command used the wrong rate-limit environment key and hit
the existing persistent 60-call ledger; the corrected documented setting
passed. No provider/network/Telegram call, queue claim, runtime wiring, paid
compute, secret/access/security change, push, merge, force-push, or remote-ref
deletion occurred.
## 2026-07-27 - Closed local-channel accounting JSON boundary

Continued `projects/omegaclaw/repos/ThreadKeeper` on
`agent/threadkeeper-hardening-next`, preserving the completed draft-PR-#1
safety-floor ancestry. Commit `d726db4` makes local-channel pricing overrides
and usage-ledger JSONL records reject duplicate object keys and Python's
non-standard `NaN`/`Infinity` tokens. Malformed records cannot influence
operator-visible token or cost totals, while valid neighboring ledger records
remain usable.

Three focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite passed (`1088 passed`) with both local LLM rate
and concurrency guards disabled. The first combined suite run encountered
pre-existing persistent concurrency reservations and failed 10 provider
boundary cases as `concurrency_limited`; rerunning with the documented local
concurrency guard disable passed. No provider, live queue/runtime, Telegram,
paid compute, secret/access/security change, push, merge, force-push, or
remote-ref deletion occurred.
## 2026-07-27 - Strict native-provider response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`edee61f`, preserving the completed safety-floor ancestry. Native
Ollama-compatible provider responses now use the existing strict JSON decoder.
Duplicate object keys and Python's non-standard `NaN`/`Infinity` tokens fail
closed as private `provider_response_invalid` control results before response
content, metadata, or token counters can influence worker behavior.

Four focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite passed (`1091 passed`) with both local LLM rate
and concurrency guards disabled. The first full-suite run exposed ten test
mocks that patched the former decoder entry point; those mocks were updated to
exercise the strict decoder seam and the corrected suite passed. No provider,
network, Telegram, live queue/runtime, paid compute, secret/access/security
change, push, merge, force-push, or remote-ref deletion occurred.
## 2026-07-28 - Strict Telegram API response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`297f362`, preserving the completed safety-floor ancestry. Telegram Bot API
responses now use strict JSON and strict UTF-8 decoding. Duplicate object
keys, Python's non-standard `NaN`/`Infinity` tokens, non-object roots, and
non-boolean `ok` markers fail closed before update, authentication, or message
processing.

Six focused checks, Python compilation, `git diff --check`, and the
provider-free hardening suite passed (`1097 passed`) with local LLM rate and
concurrency guards disabled. No provider, network, Telegram, live
queue/runtime, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
## 2026-07-28 - Strict Mattermost response JSON

Continued the draft-PR-#1-derived ThreadKeeper hardening branch with commit
`2dcab8e`, preserving the completed safety-floor ancestry. Mattermost REST
identity/profile responses and websocket event/post envelopes now use strict
JSON and strict UTF-8 decoding. Duplicate object keys, Python's non-standard
`NaN`/`Infinity` tokens, and non-object roots fail closed before identity,
profile, event, or post processing.

Ten focused provider-free checks passed, along with Python compilation and
`git diff --check`. A broad `Autotests/mock` invocation used an incomplete
test environment, produced unrelated failures, and was interrupted; no
full-suite result is claimed. No provider, network, Mattermost, Telegram,
live queue/runtime, paid compute, secret/access/security change, push, merge,
force-push, or remote-ref deletion occurred.
