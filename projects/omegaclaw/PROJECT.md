# OmegaClaw Core Installation

- Slug: `omegaclaw`
- Status: `active`
- Created: `2026-06-26`
- Last reviewed: `2026-07-26`
- Owner: Benjamin Goertzel

## Purpose

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
