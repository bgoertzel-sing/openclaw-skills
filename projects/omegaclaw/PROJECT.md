# OmegaClaw Core Installation

- Slug: `omegaclaw`
- Status: `active`
- Created: `2026-06-26`
- Last reviewed: `2026-07-18`
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
