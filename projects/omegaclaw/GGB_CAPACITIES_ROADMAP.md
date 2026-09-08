# Protobots GGB Capacities Roadmap

As of 2026-08-15 15:30 UTC, the reusable ThreadKeeper gate for capacities
3.2, 4.5, and 5.2 is refreshed to local branch head `4fdce91`. Queue state
transitions and artifact cleanup now bind the validated queue parent to the
device/inode of the directory descriptor actually opened, so a swap to a
different real directory before rename or unlink fails closed. The two direct
regressions and the complete boundary file pass (60 tests / 160 subtests), as
do compilation, diff check, and the cross-project GGB fixture checker. This is
local hardening evidence coordinated above draft PR #1's safety-floor ancestry;
it grants no live worker, OmegaClaw/Telegram, push, merge, or runtime authority.

As of 2026-08-15 07:30 UTC, the active conversational-memory/recovery gate for
capacities 2.4, 3.1, 3.4, 4.2, 5.1, and 5.2 is production-free complete. The
minimal logger repair at local unpushed OmegaClaw-Core commit `5b9a0aa` passed
13 Python tests, all six upstream MeTTa test files, and a two-phase restart
soak with six ACKs and six response-anchored exact recalls from the migrated
1,024-D store. Kernel egress denial, protected-byte stability, and
zero-descendant teardown passed. The next small task is a separate production
promotion review; no push, merge, Telegram, credentials, production canary, or
cutover is authorized. Evidence:
`experiments/20260815T070910Z-protomega-staged-logger-integration/`.

Capacities 1.3, 1.5, 2.4, 3.1, 3.4, 4.2, 5.1, and 5.2 now have a
provider-free Iter three-bot baseline contract at
`artifacts/ggb-capacity-gates/20260812-iter-three-bot-baseline-contract/`.
Its v2 schema distinguishes deployment slot from declared runtime identity
and fails closed on secret-like fields, ambiguous identity, noncanonical
capture time, placeholder routing evidence, or live authority. Nine tests and
compilation pass. The next empirical gate is a read-only, secret-free capture
of the three requested slots followed by an independent comparison of source
commits, receiver ownership, and routing fingerprints. Unknown facts must stay
explicitly unknown; no receiver/process control, credential access, state
mutation, Iter adapter, or ThreadKeeper PR #1 change is authorized.

Capacity 1.2 now has an executable, fail-closed D2 decision-receipt contract at
`artifacts/ggb-capacity-gates/20260811-motivation-materialization-decision-receipt-contract/`.
It accepts only Ben's exact authority for one provider-free deterministic 64/32
materialization and binds the reviewed generator and preregistration digests.
Nine tests reject absent/declined/inferred decisions, source or scope drift,
size/type/execution widening, secondary authority, duplicate members,
oversized files, and symlinks; compilation and the five-file fixture checker
pass. No receipt or dataset was created. Next: wait for Ben's explicit D2
decision, then independently bind it to the source message before any separate
one-shot materializer. Fitting, memory, ThreadKeeper, GoalChainer, provider,
Telegram, and runtime authority remain closed.

Capacity 1.1's current decision seam is now executable and fail closed at
`artifacts/ggb-capacity-gates/20260811-heldout-decision-receipt-contract/`.
The provider-free contract accepts only Ben's exact authorization for one
local A09--A12 score run against the frozen candidate and sealed-copy digests;
all other authority stays false. Nine tests cover exact acceptance plus
missing/declined, drifted, widened, duplicate-member, oversized, symlink, and
extra-field failures, and the five-file GGB fixture passes. This creates no
approval receipt and does not reveal or execute held-outs. The next gate still
requires Ben's explicit D1 decision, followed by independent source-message
binding before any separate one-shot runner is built.

Capacity 1.1 now has a fail-closed held-out authorization preflight at
`artifacts/ggb-capacity-gates/20260810-heldout-authorization-preflight/`.
It binds the frozen candidate, sealed A09--A12 commitment and encrypted-copy
digest, and independent public verification without decrypting or revealing
held-out bytes. Five provider-free checks, including four drift/authority
negatives, pass. The only next action is Ben's explicit authorization for one
four-case execution against candidate SHA-256
`df182ee8cafab2a7356352375916e06c2b1e39a60aae61378bb918fb39a27126`
through the bound v0.6 sandbox. Harness adoption, candidate edits,
ThreadKeeper PR #1 changes, memory writes, dispatch, providers, Telegram,
paid compute, and runtime effects remain separately closed.

Capacity 1.1's frozen zero-effect candidate has passed independent freeze and
public-replay verification at
`artifacts/ggb-capacity-gates/20260809-request-to-contract-candidate-freeze-independent-verification/`.
The verifier binds the candidate digest, public harness, complete v0.6 sandbox
chain, and sealed commitment; all 22 public cases and the source-drift negative
pass. The next empirical gate requires Ben's explicit authorization to reveal
and execute A09--A12. Harness adoption is a separate post-score decision, and
no ThreadKeeper PR #1, memory, provider, Telegram, dispatch, or runtime
authority is granted.

Capacity 1.1's combined R1/R2/R4 readiness and candidate-freeze review passes
at `artifacts/ggb-capacity-gates/20260809-request-to-contract-combined-readiness-review/`.
The review binds the public executable cases, sealed four-case commitment, and
v0.6 containment/invocation replay, and fixes the next safe order: implement a
non-live candidate without reveal, record and verify its source SHA-256, then
seek separate held-out reveal/execution authorization. No harness, ThreadKeeper
PR #1, memory, provider, Telegram, dispatch, or runtime authority is granted.

Capacity 1.1's content-bound v0.6 Bubblewrap facade passes an independent
twelve-probe R4 and public invocation-seam replay at
`artifacts/ggb-capacity-gates/20260809-request-to-contract-os-sandbox-v06-independent-replay/`.
All twelve cases pass with E1--E6 coverage; the v0.5 stderr-flood regression
now fails with the exact generic error, while exact binary output, fixed input-
rejection typing, and source-drift rejection pass. The next small gate is an
independent combined R1/R2/R4 readiness and candidate-freeze review. Held-out
reveal, harness adoption, ThreadKeeper PR #1 changes, and runtime effects remain
unauthorized.

Capacity 1.1's next producer revision is implemented at
`artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v06-stream-bounds/`.
The non-live facade now validates each captured stream and their aggregate
before accepting the child report, including the v0.5 failure mode where a
candidate catches stderr file-limit errors and returns normally. The next
empirical gate is an independently content-bound twelve-probe R4 and public
invocation-seam replay. No held-out reveal, harness adoption, ThreadKeeper PR
#1 change, or runtime effect is authorized.

Capacity 1.1's v0.5 independent R4 and invocation-seam replay found one
containment regression at
`artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v05-independent-replay/`.
Eleven of twelve adversarial cases pass and E1--E6 are exercised; exact binary
return, fixed candidate-rejection typing, and source-drift rejection also pass.
The output-flood case fails because 1,000,000 stderr bytes are captured but not
bounded or checked on the success path. Verdict:
`revision_required_before_harness_adoption`. The next gate is a producer-only
captured-stream/aggregate bound revision followed by a fresh independent
replay. No held-out reveal, harness adoption, ThreadKeeper PR #1 change, or
runtime effect is authorized.

Capacity 1.1 now has a producer-side Bubblewrap facade revision that uses the
accepted v0.3 child-result codec inside the isolated child and at the parent
boundary. Exact binary bytes and the fixed rejection/generic-failure split pass
four provider-free tests at
`artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v05-codec-binding/`.
The next gate is an independent, content-bound R4 and invocation-seam replay;
held-out reveal, harness adoption, ThreadKeeper PR #1, and runtime effects stay
closed.

Capacity 1.1's bounded result-tag contract now fails independent
implementability review at
`artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract-independent-review/`.
The review content-binds the frozen contract and preserves its safe two-tag
intent, but finds three ambiguities: the JSON canonicalization label does not
freeze bytes, base64 canonicality and decoded size are unspecified, and
non-bytes candidate returns have no generic-failure classification. One direct
check and five tests pass. Verdict: `revision_required_before_implementation`.
The next small task is a contract-only v0.2 revision; sandbox implementation,
held-out reveal, harness adoption, and runtime effects remain closed.

Capacity 1.1 now freezes the bounded result-tag contract needed to repair the
public invocation seam without reopening candidate-controlled error detail.
Only exact `ok` and `rejected_input` child reports are admitted; rejection is
limited to a `ValueError` from the candidate call and maps to a generic parent
`ValueError`, while all other failures remain generic `RuntimeError`. The
contract requires fresh R4, seam, and public invalid-input replays before
adoption. One direct check and seven tests pass at
`artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract/`.
This authorizes no implementation, held-out reveal, harness, or runtime effect.

Capacity 1.1 now records the independently authored A09--A12 reveal
commitment before any generator implementation. The exact held-out bytes cover
a new bounded PeTTa-memory record request and semantic paraphrase plus new live
and mixed GoalChainer-to-ThreadKeeper task-claim requests. Their SHA-256 is
content-bound at
`artifacts/ggb-capacity-gates/20260806-request-to-contract-heldout-commitment/`;
only an encrypted sealed copy is in the gate and reveal remains unauthorized
until a candidate hash is frozen. The direct checker and four negative tests
pass. This closes the missing R2 commitment record, not held-out execution,
R1, harness adoption, generator authority, or runtime authority.

Capacity 1.1 now freezes executable implementations of all 22 public
generator-facing cases (A01--A08 and N01--N14) at
`artifacts/ggb-capacity-gates/20260806-request-to-contract-public-executable-cases/`.
The harness accepts a monitored invocation seam and tests exact canonical
outputs, byte determinism, paraphrase equivalence, live/mixed authority,
ordered provenance, digest/path/NFC/bound failures, and output authority
confinement. Three self-tests pass. This advances but does not close R1: the
independent A09--A12 reveal and its pre-implementation R2 commitment are still
missing, and the production seam must be content-bound to the accepted v0.4
sandbox before harness adoption. No generator or runtime authority is granted.

Capacity 1.1's content-bound v0.4 generic-failure sandbox now passes an
independent replay of all twelve frozen cases. The consumer binds the contract,
producer record, facade, and underlying Bubblewrap sources, covers E1--E6,
and confirms that the prior private stderr sentinel is exposed only as the
exact message `sandbox candidate failed`. Five independent provider-free
checks and compilation pass at
`artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v04-independent-replay/`.
Verdict: `r4_empirical_replay_pass`. Next: implement and freeze R1 executable
cases and an independent R2 held-out commitment before harness adoption. No
generator or runtime effect is authorized.

Capacity 1.1's independently implemented v0.3 consumer now binds the contract,
producer binding, and sandbox source bytes and executes all twelve required
cases without importing producer tests. Eleven pass, but E6 fails: a contained
network adversary's private stderr sentinel is forwarded verbatim in
`RuntimeError`. Five independent checks pass at
`artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-independent-replay/`.
The generic-failure v0.4 revision and its passing replay are recorded above.
R1/R2 and harness adoption remain open; generator and runtime effects remain
unauthorized.

Capacity 1.1 now has a frozen, testable resolution to the R4 contract mismatch.
The v0.3 boundary evaluates externally observable outcomes rather than trying
to detect every Python or native call: host immutability, network isolation,
descendant teardown, ambient-authority removal, finite resource use, and output
confinement. It requires twelve adversarial case classes and explicitly treats
a fully confined `fork`/`exec` as internal computation, not an escaping effect.
Five provider-free contract tests and the direct checker pass at
`artifacts/ggb-capacity-gates/20260805-request-to-contract-effect-boundary-v03/`.
The v0.4 content binding and passing empirical replay are recorded above. This
does not authorize the harness, generator, or runtime effects; R1/R2 remain
open.

Capacity 1.1's independent R4 review stops the new OS sandbox before harness
adoption. A content-bound candidate bypasses Python audit events through
`ctypes`, calls libc `fork`/`execl`, completes `/usr/bin/true`, and receives
`pass`. Bubblewrap still contains the process and blocks the demonstrated host
filesystem escape, but the result contradicts the frozen contract that
subprocess/exec effects and monitor bypass fail. Eight provider-free review
checks pass at
`artifacts/ggb-capacity-gates/20260805-request-to-contract-os-sandbox-independent-review/`.
The v0.3 contract above resolves this by freezing the narrower externally
observable boundary; its implementation and independent replay are still
pending. R1/R2/R4 remain open; generator code and runtime effects remain
unauthorized.

Capacity 1.1's R4 revision moves candidate import and execution into a
Bubblewrap OS boundary with disposable mount/network/PID namespaces, a
read-only minimal runtime/work tree, descendant teardown, and hard CPU,
address-space, file-size, process, open-file, captured-output, and wall-time
limits. Ten provider-free adversarial tests pass, including the exact prior
`os.symlink` escape and a native host-path write attempt. Evidence:
`artifacts/ggb-capacity-gates/20260805-request-to-contract-os-sandbox/`.
This is prototype evidence pending independent bypass review, not R4 closure
or acceptance-harness adoption. R1 executable cases and R2 held-out commitment
remain open; generator code and runtime effects remain unauthorized.

Capacity 1.1's revised generator-acceptance preregistration also stops before
implementation. An independent content review confirms the exact bytes API
closes R3 at the contract level, but R1/R2/R4 remain open: its 26 cases are
names without executable bodies, no held-out byte commitment exists, and the
candidate is imported before an effect monitor that has no implementation.
Eight provider-free checks pass at
`artifacts/ggb-capacity-gates/20260805-request-to-contract-generator-acceptance-v02-independent-review/`.
Next: freeze the executable harness, held-out commitment, and import-inclusive
sandbox; generator code and runtime effects remain unauthorized.

Capacity 1.1's first generator-acceptance preregistration failed independent
implementability review because its advertised 20-case command only checked
metadata, admitted fixture lookup, and left its API and effect observation
ambiguous. Contract-level v0.2 now freezes an exact raw-bytes API, canonical
JSON, a 26-case generator-facing target, explicit effect monitoring, and a
held-out commitment/reveal boundary after candidate hash freeze. Ten
provider-free structural tests pass. Evidence:
`artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-acceptance-preregistration-v02/`.
Next: independent review must freeze the real 26 case implementations and
held-out commitment and close R1--R4; no generator code or runtime effect is
authorized.

As of 2026-07-30 UTC, the motivational score-policy v0.2 deterministic
generator has passed revised preregistration, independent review,
implementation-only, and independent implementation-review gates. A separate
materialization preflight binds the exact 64/32 synthetic split and fails
closed while approval is absent. The next step is a decision from Ben on
deterministic materialization only; fitting, memory writes, ThreadKeeper
effects, providers, Telegram, and runtime behavior remain unauthorized.
Evidence:
`artifacts/ggb-capacity-gates/20260729-motivation-score-policy-v02-materialization-preflight/`.

- Source: Gödel Oruži, `GGB Capacities Curriculum v0.1`, as forwarded by Ben; this file treats it as a rough medium-term planning scaffold, not a frozen spec.
- Scope: upgrade `@Protomegabot`/ProtomegaTron intelligence through concrete empirical gates while coordinating with OmegaClaw Core, ThreadKeeper PR #1, PeTTa intermediate memory, and `petta-chem` algorithmic chemistry.
- Last updated: 2026-08-15 15:30 UTC / 2026-08-15 08:30 PDT; refreshed during recurring Protobots GGB roadmap worker run.

## Operating rule

Capacity 1.1's frozen v0.3 externally observable-effect contract is now bound
to the existing Bubblewrap implementation and exercised against all twelve
required adversarial classes at
`artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-binding/`.
Fourteen provider-free tests cover host writes through Python and native calls,
parent-path link escape, network, descendant teardown, credential environment,
stdin, CPU/address-space/process/output exhaustion, and exact byte return.
This closes the producer-side coverage gap only. R4 still requires an
independently implemented, content-bound replay that does not import the
producer tests; R1 and R2 also remain open. No harness, generator, memory,
dispatch, provider, Telegram, or runtime authority is granted.

The structural chemistry transfer lane is now sealed end-to-end at
`artifacts/ggb-capacity-gates/20260731-chemistry-structural-transfer-evidence-receipt/`.
The receipt content-binds the larger RAF-shape preregistration, independent
runner, and four exact results; five provider-free checks fail on artifact or
replay drift, duplicate JSON, and authority widening. This strengthens bounded
cross-domain evidence/appraisal gates (capacities 2.2, 3.2, 4.1, 4.3, 5.2,
5.4) but grants no execution or runtime authority. The lane stops for
adjudication rather than extending the scorer again.

The chemistry-to-planning lane now has a compact evidence receipt at
`artifacts/ggb-capacity-gates/20260731-chemistry-candidate-scoring-evidence-receipt/`.
It content-binds the read-only adapter, sealed preregistration, independent
runner, and all four exact replay selections and score maps. Five provider-free
checks reject artifact/replay mutation, duplicate JSON, and authority widening.
This advances bounded evidence use and candidate appraisal (capacities 2.2,
3.2, 4.1, 4.3, 5.2, 5.4) without authorizing chemistry execution, experiment
scheduling, ThreadKeeper/PR #1 effects, or runtime behavior. Next: preregister
one structurally different chemistry fixture before extending the scorer.

Each capacity should graduate only through an archived, reproducible gate: prompt/task input, bounded permissions, artifacts changed, checks run, result summary, and known failure modes. Prefer local tests and project records over live chat demonstrations.

The concise current frontier is maintained in `GGB_NEXT_GATES.md`. The goal/task adapter, immutable memory-to-appraisal replay, neutral cross-domain run-contract schema, provider-free persistent supervisor boundary, formal handoff enforcement, restart stability, four explicit operator dispositions, and recommendation-only disposition appraisal now pass. The appraisal snapshot binds each admitted evidence packet's content digest, so evidence mutations fail closed before GoalChainer-style scoring. The approval-bound isolated ProtoMegaBot2 canary remains behind explicit approval.

The motivational registry now has strict raw-byte consumers in two languages
and a preregistered per-consumer admission rule. The rule content-addresses
both implementations, tests, and reports; requires distinct language,
runtime, parser, and implementation path; and requires each consumer to own
noncanonical-integer, Unicode-scalar/NFC, and duplicate-member rejection. A
shared validator or peer import fails closed. Seven admission checks and both
pinned consumer suites pass at
`artifacts/ggb-capacity-gates/20260724-motivation-per-consumer-preflight/`.
This advances capacities 1.2, 2.2, 3.2, 3.5, 4.1, 5.2, and 5.4 without
granting task, memory, egress, or runtime authority. The portable-boundary
holdout now passes, and
`artifacts/ggb-capacity-gates/20260725-motivation-representation-contract-freeze/`
content-addresses that holdout, the admission contract, and both consumer
reports while pinning the maximum portable integer, new valid Unicode scalar,
candidate-set digest, and candidate-only authority. A separately versioned
v0.2-to-v0.3 semantic migration now adds only `defer_for_review`, preserves
checkpoint state, and binds old/new registry and checkpoint identities in a
candidate-only receipt. Seven provider-free tests pass, including fail-closed
downgrade and authority-widening cases, at
`artifacts/ggb-capacity-gates/20260725-motivation-candidate-registry-migration/`.
The migrated receipt replay and new-candidate reachability gates now pass; an
independent strict consumer also reproduces the pinned `defer_for_review`
selection from sealed JSON without importing producer code. Its six tests
include duplicate-member, trailing-content, mutation, rehashed-cursor, and
rehashed-authority negatives at
`artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-serialized-consumer/`.
The reachability evidence contract is now frozen at
`artifacts/ggb-capacity-gates/20260726-motivation-reachability-contract-freeze/`.
It content-addresses the fixture, independent consumer, and tests while
pinning registry/checkpoint identities, replay position, exact selection,
absence of a score policy, and candidate-only authority. Score-policy v0.1 is
now separately preregistered at
`artifacts/ggb-capacity-gates/20260726-motivation-score-policy-preregistration/`.
It binds the frozen predecessor, candidate-set identity, scale-1000 integer
arithmetic, exact features/weights, conservative tie breaking, a review-risk
override, and three holdouts. Seven provider-free contract checks pass, and an
independent runner reproduced all three selections in five checks without
importing the validator. The next discriminating suite is preregistered at
`artifacts/ggb-capacity-gates/20260726-motivation-score-policy-boundary-holdout-preregistration/`.
Its five sealed cases cover exact ties, a one-unit rank change, and the
adjacent 799/800 override boundary while binding the policy and prior runner
identities. Eight provider-free contract checks pass. An independent runner
now reproduces all five selections and reasons without importing that
validator or the prior runner; six checks include sealed-byte, expectation,
feature-scalar, admission-rule, and authority negatives at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-boundary-holdout-independent-runner/`.
This does not modify the frozen boundary or provide calibration evidence.
The out-of-sample feature-interaction suite was preregistered at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-feature-interaction-preregistration/`.
Seven sealed cases probe multi-feature pressure and two score crossovers. The
contract also makes a structural policy limitation testable:
`inspect_evidence` is unreachable under v0.1 because its score is never greater
than `defer_for_review`, which also wins their exact tie. Nine provider-free
contract checks pass. An independent runner reproduced all seven selections,
both crossovers, and the dominance result in eight checks without importing
the preregistration validator or prior runners. No calibration was performed.
A separately versioned v0.2 candidate is now preregistered at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-preregistration/`.
It preserves the three admitted inputs and conservative review override, but
derives `evidence_gap = 1000 - evidence_sufficiency` internally so
`inspect_evidence` has a genuine low-evidence reachability region. All four
candidates have sealed witnesses; eight provider-free contract checks pass.
An independent runner now reproduces all five sealed witnesses and selects
every registered candidate while recomputing `evidence_gap` solely from the
three admitted inputs. Eight provider-free checks cover sealed identity,
caller-supplied derived values, malformed scalars, policy/expectation drift,
candidate unreachability, admission weakening, and authority widening at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-independent-runner/`.
The out-of-sample boundary, joint-feature, evidence-freeze, reviewed generator,
and approval-preflight gates described below supersede that former next step.
The current frontier is Ben's decision on deterministic 64/32 materialization
only. None of these artifacts grants fitting, live, task, memory, provider,
Telegram, runtime, or ThreadKeeper authority.

The provider-free `motivation-state-v0.1` gate now binds a synthetic immutable
`petta-memory`-shaped snapshot to two need variables and six bounded
modulators, then ranks fixed GoalChainer-shaped candidates without effects.
Seven tests cover deterministic replay, full record-order invariance,
fail-closed evidence mutation and temporal provenance, finite/range checks,
and monotonic information-seeking under increased uncertainty urgency. The
next small gate is multi-event temporal decay and restart equivalence; no live
motivation state or task-claim authority is implied.

The admitted motivational candidate registry now has a third holdout
canonicalizer implemented independently with Node.js built-ins. It reproduces
the exact candidate-set SHA-256 from both byte-distinct producer fixtures and
rejects semantic mutation, action-authority widening, unknown fields,
candidate reordering, and a fractional ordinal. Seven checks pass at
`artifacts/ggb-capacity-gates/20260724-motivation-javascript-holdout/`.
This is candidate-only portability evidence; ThreadKeeper effect remains
`none`.

The follow-on representation preflight now passes at
`artifacts/ggb-capacity-gates/20260724-motivation-representation-preflight/`.
It preserves the admitted hash for both producer fixtures while rejecting
ordinal lexeme aliases `-0`, `0e0`, and `0.0`, non-NFC semantic text, and a
lone surrogate before semantic hashing. Seven provider-free checks pass.
This is still candidate-only and grants no ThreadKeeper/runtime authority.
The independent Python strict-JSON follow-on at
`artifacts/ggb-capacity-gates/20260724-motivation-strict-json-consumer/`
replays all five failures and rejects duplicate members at registry,
candidate, and nested-contract depths before semantic hashing. Ten checks
pass while both producer fixtures retain the admitted hash. The per-consumer
admission gate now requires duplicate-member rejection from every admitted
consumer; a shared byte-boundary validator is not independent evidence.

The follow-on temporal gate now replays three explicitly timed events with
bounded per-hour decay. A self-hashed checkpoint after two events resumes to
the same terminal state and ranking as uninterrupted replay; checkpoint
mutation and non-monotonic timestamps fail closed, and a final clock-only
step preserves the top-ranked candidate. Six tests and Python compilation
pass at `artifacts/ggb-capacity-gates/20260720-motivation-temporal-replay/`.
The next small gate should preregister a genuine competing-needs rank switch
and hysteresis margin rather than merely testing rank preservation.

The follow-on scale-sensitivity gate now demonstrates that absolute
hysteresis margin `0.05` depends on score units: it permits the preregistered
switch at scale `1.0` and suppresses it at `0.5` and `0.25`. Scaling the margin
with a pinned positive score scale preserves the trace across all three. Five
unit checks, compile, and JSON replay pass at
`artifacts/ggb-capacity-gates/20260721-motivation-score-scale/`. This blocks a
premature runtime-default freeze; the next offline task is a dimensionless
normalization contract with fail-closed scale provenance.

The representation boundary is now probed at
`artifacts/ggb-capacity-gates/20260722-motivation-quantization/`. Decimal-string
inputs with pinned three-place round-half-even preserve preregistered
below/exact/above hysteresis decisions; a two-place control erases the small
above-boundary advantage and suppresses its switch. Five unit checks, compile,
and JSON replay pass. This is candidate-only evidence that precision is
behavior-bearing, not a frozen runtime default. Next: test integer fixed-point
equivalence across boundary and restart fixtures.

That fixed-point equivalence gate now passes at
`artifacts/ggb-capacity-gates/20260722-motivation-fixed-point/`. Converting the
pinned values to scale-1000 integers after round-half-even preserves the exact
three-case decimal selection trace, and replay after a two-case self-hashed
checkpoint matches uninterrupted execution. Four unit checks, compile, and
JSON replay pass. Candidate-only; ThreadKeeper effect `none`. Next: accept a
checkpoint as input and reject mutation, stale source identity, or policy drift.

Independent ingest and resume now pass at
`artifacts/ggb-capacity-gates/20260722-motivation-fixed-point-ingest/` and
`artifacts/ggb-capacity-gates/20260723-motivation-fixed-point-resume/`.
The resume consumer verifies the checkpoint/source identities and pinned
cursor/scale/margin, then recomputes the suffix directly from the source; a
deliberately falsified producer `resumed_trace` is ignored. Five unit checks,
compile, and JSON replay pass. Candidate-only; ThreadKeeper effect `none`.
The candidate-set resume gate now passes at
`artifacts/ggb-capacity-gates/20260723-motivation-candidate-set-resume/`.
Its checkpoint binds an ordered, versioned set of three candidate IDs and
recomputes a two-event suffix with two rank switches. Candidate mutation or
reordering, stale version, unknown score keys, policy drift, and checkpoint
mutation fail closed. Six unit checks, compile, and JSON replay pass.
Candidate-only; ThreadKeeper effect `none`. Next: bind per-candidate
semantic/action-contract digests so stable IDs cannot conceal changed meaning
or effects.

That contract-digest gate now passes at
`artifacts/ggb-capacity-gates/20260723-motivation-candidate-contract-digests/`.
Each candidate carries separately hashed semantics and bounded action authority;
the resulting ordered registry digest is checkpoint-bound before replay.
Stable-ID semantic mutation, effect/authority widening, digest substitution,
candidate reordering, and checkpoint mutation fail closed. Six unit checks,
compile, and JSON replay pass. Candidate-only; ThreadKeeper effect `none`.
Next: give the registry and checkpoint to an independent consumer that does not
call the producer's sealing function.

The independent ingest is complete, and the follow-on cross-producer
serialization gate now passes at
`artifacts/ggb-capacity-gates/20260723-motivation-cross-producer-canonicalization/`.
Two byte-distinct registry renderings converge to the previously admitted
candidate-set SHA-256 under an exact-schema canonicalizer. Semantic mutation,
action-authority widening, unknown fields, and candidate reordering fail
closed. Five unit checks, compilation, and JSON replay pass. This remains
candidate-only evidence with ThreadKeeper effect `none`.

The independent implementation gate now passes at
`artifacts/ggb-capacity-gates/20260723-motivation-independent-canonicalizer/`.
A Perl/JSON::PP implementation that imports no producer or Python
canonicalization code reproduces the exact admitted hash from both fixtures.
Semantic mutation, authority widening, and unknown fields fail closed in five
provider-free checks. This strengthens portability evidence but grants no
runtime authority.

The consumer-diversity admission contract now passes at
`artifacts/ggb-capacity-gates/20260724-motivation-consumer-diversity/`.
It preregisters a minimum of two content-addressed consumers that must differ
in language, runtime, JSON library, and implementation path, agree on the
exact candidate-set hash, and import no other admitted consumer. Ten tests
cover admission, insufficient count, collapsed runtime/library diversity,
shared code, hash disagreement, authority widening, and unknown fields.
This admits portable evidence only; candidate selection remains adjudicated
and ThreadKeeper effect remains `none`.

The v0.2 synthetic score-policy generator has now crossed an
implementation-only gate at
`artifacts/ggb-capacity-gates/20260729-motivation-score-policy-v02-generator-implementation/`.
Seven provider-free checks bind the reviewed preregistration, replay the exact
SHA-256 counter primitive and family transforms, reject a cross-split duplicate,
and demonstrate bounded exhaustion with no output. No 64/32 dataset, labels, or
fit were materialized; the module intentionally has no full-dataset entry point.
The independent formula/vector review also passes six provider-free checks at
`artifacts/ggb-capacity-gates/20260729-motivation-score-policy-v02-generator-implementation-review/`.
The subsequent materialization preflight binds the reviewed generator and exact
64/32 scope, but direct execution exits blocked while approval is absent.
Therefore the next action is Ben's decision on deterministic materialization
only, not fitting or runtime integration.

That normalization contract now passes at
`artifacts/ggb-capacity-gates/20260721-motivation-normalization-contract/`.
It normalizes pinned score fields by a declared positive finite scale and uses
dimensionless margin `0.05`; the expected trace is invariant at scales `1.0`,
`0.5`, and `0.25`. Invalid and score-mismatched scale metadata fail closed.
This is candidate-only and does not freeze an operational policy. Next: probe
affine-offset sensitivity and whether origin/centering metadata must be bound.

The affine-origin probe now passes at
`artifacts/ggb-capacity-gates/20260721-motivation-affine-origin/`. Centering
common score-field origins `0.0`, `0.05`, and `0.10` before scale normalization
preserves the preregistered trace. Invalid, missing/mismatched, and
candidate-specific offsets fail closed. This supports binding explicit origin
provenance whenever upstream scores are not zero-origin; it does not select an
operational feature schema or change runtime behavior. Next: test whether
per-field scales/origins preserve the trace and fail closed on field swaps.

The disposition gate now also carries four provider-free metamorphic checks:
evidence-container order and admitted-but-unselected evidence leave the decision
projection invariant, strengthening the winning evidence is monotonic, and a
bounded low-weight selected distractor does not overturn a clear decision.
This narrows a concrete robustness gap without granting runtime or disposition
authority. A follow-on artifact now preregisters exact and adjacent confidence/
margin edges and deterministically shrinks an unsafe confidence-only selection
rule to a canonical checksummed two-score counterexample (8/8 checks, 4 unit
tests). The next offline task is bounded perturbation/calibration on
representative admitted-evidence score distributions.

The provider-free persistent-worker supervisor boundary is now complete through
exclusive ownership. Reconciliation commit `3673e94` covers corruption,
cancellation, budget exhaustion, and expired-attempt requeue; restart commit
`c06725e` proves durable behavior across fresh interpreters; commit `e7e997e`
adds a non-blocking root-scoped OS lock and a two-interpreter contention
regression. Lifecycle tests pass 49/49 and the combined provider-free gate
passes 362 tests. The next implementation artifact is an isolated ProtoMegaBot2
canary manifest plus fail-closed preflight validator. No canary launch, runtime
copy, provider call, or Telegram authority follows without separate explicit
approval. The offline canary validator now also compares the manifest's full
source SHA and branch with the actual isolated checkout, so stale or substituted
ThreadKeeper source fails before approval can authorize launch.
It additionally rejects tracked or untracked checkout changes not covered by
that SHA and requires the three named production boundaries, preventing a dirty
source tree or substituted exclusion list from passing by assertion.

## Near-term implementation spine

1. **Do not duplicate ThreadKeeper PR #1.** Treat PR #1 / branch `agent/threadkeeper-safety-floor` as already covering the first safety floor: path sandbox, fail-closed budget fallback, disabled/allowlisted argv-only shell execution, and tests.
2. **ThreadKeeper hardening branch status:** local branch `agent/threadkeeper-hardening-next` has implemented the next reliability/recordability slice: LLM timeout/retry/backoff, bounded child history digests, structured JSON returns, persistent transcript records, atomic subagent writes, stricter tool validation, per-dispatch quotas, cancellation, optional `escalation.metta` integrity pinning, persona prompt sandboxing, bounded read output, per-turn tool-call caps, dispatch wall-clock timeout, worker token accounting, hash-chained run-index audit entries, task-contract `patch_proposal_only` mode for parent-reviewed changes, queue-only dispatch records with backpressure, optional `requires_adjudication` candidate outputs for high-stakes results, a queued-worker claim/run primitive with failed-claim audit retention, a bounded operator-supervised queue drain helper, queue-drain filtering that ignores retained `*.result.json` audit sidecars, queued-task contract preservation during worker execution, required queue-task checksum sidecars verified before worker LLM calls, queued-task schema validation for unexpected fields/unsafe run IDs/cancel-file metadata, tighter queued task-contract schema checks for malformed list fields, non-finite/boolean numeric metadata, and coerced non-integer numeric metadata; queued cancellation-token preservation into worker execution; bounded optional subagent shell argv plus explicit NUL rejection, capped optional shell output with truncation markers and timeout parsing, a non-mutating `review_subagent_candidate(transcript_path)` helper for parent/operator review of patch proposals and adjudication candidates, a read-only `verify_subagent_run_index(index_path=None)` audit helper for the compact run-index hash chain plus recorded transcript SHA-256s, queued task max-age rejection via `OMEGACLAW_SUBAGENT_MAX_QUEUED_TASK_AGE_S` (default 0 = disabled) to reject stale/expired tasks before worker LLM calls, transcript turn/field bounding via `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_TURNS`/`OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_FIELD_CHARS`, retry backoff jitter (up to 25% of exponential base), worker-loop results bounding via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_RESULTS`, live lock metadata with task counters, consecutive-error cap via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_CONSECUTIVE_ERRORS`, dispatch-level token budget cap via `OMEGACLAW_SUBAGENT_MAX_TOKENS_PER_DISPATCH`, transcript summary bounding via `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_SUMMARY_CHARS`, empty shell command rejection, run index entry bounding with rotation via `OMEGACLAW_SUBAGENT_MAX_INDEX_ENTRIES` (default 0 = disabled; when non-zero, the audit index is rotated after each append to keep the most recent N entries with recomputed hash chain), per-task duration and total runtime in worker loop results, completion fields and queue depth in lock metadata, current-task tracking in lock metadata for crash diagnostics, stale worker lock detection, absolute path sanitization from tool error messages, empty search/tavily-search/technical-analysis query rejection, search/tavily-search/technical-analysis output size cap via `OMEGACLAW_SUBAGENT_MAX_SEARCH_OUTPUT_CHARS`, workspace file size cap for write-file/append-file via `OMEGACLAW_SUBAGENT_MAX_FILE_SIZE_CHARS` (default 100000, 0 disables), final emit bounding via `OMEGACLAW_SUBAGENT_MAX_EMIT_CHARS`, configurable JSON audit/task read caps via `OMEGACLAW_SUBAGENT_MAX_JSON_FILE_BYTES`, non-finite numeric env rejection, raw worker response bounding via `OMEGACLAW_SUBAGENT_MAX_RESPONSE_CHARS`, and run-index audit read bounding via `OMEGACLAW_SUBAGENT_MAX_INDEX_AUDIT_BYTES`, transcript hash audit read bounding via `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES`, bounded reverse-tail index append scans, strict tool/final-emit type validation, worker control-token path confinement, patch-proposal transcript content bounding, temporary-file optional shell output capture, queue/checksum sidecar read caps, and bounded optional candidate-review `.sha256` sidecar reads, escalation/persona/worker-LLM-state read caps, streamed transcript audit hashing, bounded async-worker stale-lock metadata reads, symlink/non-regular async-worker lock rejection, fail-closed inline/persona task-contract list validation for malformed `allowed_paths`/`forbidden_actions`/`done_criteria`, async-worker signal-state cleanup after supervised runs, run-index symlink/non-regular rejection, required `.sha256` integrity sidecar symlink/non-regular rejection before digest reads, workspace file-lock symlink/non-regular rejection, run-index tail/rotation write hardening via no-follow reads and random local temp files, per-endpoint worker LLM guard-state symlink/non-regular rejection, and transcript audit symlink/non-regular rejection for candidate review/run-index verification, symlink/non-regular rejection for JSON audit-write and transcript-sidecar destinations, no-follow regular-file opens for workspace file-tool source reads, and fail-closed parent-directory validation for audit/run/queue paths plus workspace atomic writes, single-argument quoted final-emit trailing-payload rejection, worker usage-log parent-directory hardening, symlinked queued-dispatch directory rejection before queue listing/counting/claim, symlinked LLM guard-state parent rejection, and absolute/parent-traversal file-tool path rejection before workspace resolution, strict task-contract `allowed_paths` workspace-relative validation, file-tool control-character rejection, budget audit-log parent-directory hardening, transcript/run-index audit read bounding, and budget accounting/config fd read-cap hardening, persona config scalar validation before provider setup, unquoted final-emit trailing-payload rejection, symlinked existing workspace-root rejection, and shell/query argument control-character rejection, preventing runaway local reads/persistence, unsafe contract coercion, poisoned same-process worker-loop stop state, unsafe local audit path following, symlink-swap workspace reads, or symlink-redirected queued-worker task roots before tool parsing, transcript expansion, reviewer paths, setup paths, guard-state parsing, audit scans, or worker dispatch. After Ben explicitly approved a real async worker loop, the branch now also has a supervised bounded `subagent.run_queued_worker_loop(...)` primitive, compact `.async-worker.lock` owner/status metadata, an operator script `scripts/run-subagent-worker-loop`, and mock coverage for no-claim script smoke, one-task artifact-local drain, env-file loading, unsafe env-file key rejection, bounded env-file parsing, runtime cap, worker-error continuation, stop-file behavior, and concurrent-loop rejection. The worker-loop env-file boundary now also uses no-follow opened-fd validation, a 64 KiB streaming cap plus overflow sentinel, and strict UTF-8 decoding before environment application or `subagent` import. `py_compile`, direct assertion replay, and the focused hardening pytest gate now pass locally (268 tests via `local/threadkeeper-pytest-venv`; fork branch head `6e0e49b`). The latest argument-validation slices reject unsafe Unicode controls/formatting and lone surrogates in file, query, optional-shell, queued-dispatch, worker-stop, and queued-task cancellation paths before effects, queue claim, or worker-lock creation. Staged non-live worker-loop gates are archived under `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-smoke/`, `20260705-threadkeeper-worker-loop-one-task/`, `20260705-threadkeeper-worker-env-runner/`, `20260705-threadkeeper-protomegabot-config-smoke/`, and `20260705-threadkeeper-worker-supervisor-boundary/`: the newest supervisor gates add `local/threadkeeper-worker-loop-supervisor.sh` (start/stop/status/log), verify no-claim process-boundary launch, and verify a separate supervised process can return a queued task as `cancelled` before any worker LLM/provider use. The latest queue/worker-loop follow-ups preserve fail-closed queue validation and keep the loop supervisor/operator launched rather than self-started from parent dispatch. A staged Telegram-private integration gate (`20260705-threadkeeper-telegram-private-integration/`) records the merge of ThreadKeeper's hardened `subagent.py`, `threadkeeper_budget.py`, `escalation.metta`, `skills.metta`, `lib_omegaclaw.metta`, and persona config into the OmegaClaw-Core runtime tree; runtime tree was subsequently re-synced through then-current ThreadKeeper source; the current OmegaClaw-Core checkout has an untracked runtime `src/subagent.py` amid active runtime modifications, so parity at head `6e0e49b` is not claimed. A follow-up non-live preflight gate (`20260708-threadkeeper-telegram-private-preflight/`) initially blocked on private-only/default-chat defaults and active supervisor state. Gate `20260710-threadkeeper-telegram-private-defaults-hardening/` resolves the default-boundary slice by changing the private supervisor defaults to `DEFAULT_TG_PRIVATE_ONLY=true`, `DEFAULT_TG_CHAT_ID=402314199`, and `DEFAULT_TG_CHAT_IDS=402314199`; the remaining blocker is mutable process state (`active pid 822634` during the gate) plus explicit approval/stop conditions before any live private smoke.
3. **Memory integration target:** use `petta-memory` as a read-only prompt-view source first; current `petta-memory` work already has prompt-view ordering, stricter PLN promotion metadata, normalized PLN atoms, generated `MM-index`/`index-view` retrieval edges, complete-atom bounded rendering for prompt/index/PLN-safe views, default-disabled/read-only OmegaClaw wrapper tests, an OmegaClaw-style prompt/index fixture gate, audit view, tightened binary relation/envelope/containment validation, 88 stdlib unit tests passing, local SWI/Janus/PeTTaChainer smoke validation, bounded PeTTaChainer profiling that isolates the current compile/add bottleneck, and a non-live PeTTa `static-import!` microbenchmark path that loads normalized scratch atoms into a selected runtime predicate and verifies exact fact membership.
4. **PeTTa/chemistry target:** use `petta-chem` run-contract atoms and replay/ablation discipline as the pattern for scientific/cognitive experiment records. `petta-chem` now has a v0.1 run-contract smoke, generated/control exp02 sweep summaries, PeTTa-side folded summary atoms, a host harness that serializes seventy-five exp02 run-contract records, a factored generated-control template through seed-107, a sweep-kind report, and early exp03 multi-tick dynamic bridge/aggregate/export atoms over full-source random/control families. Bundle C has partial GGB gate records, a thin field mapping in `GGB_GATE_RUN_CONTRACT_MAPPING.md`, `.metta` sibling fixture files for the `20260701-petta-chem-run-contract` gate, and a local fixture smoke checker archived in `artifacts/ggb-capacity-gates/20260702-ggb-fixture-smoke/RUN.md`. The same sibling-fixture/checker pattern now also passes on the ThreadKeeper hardening gate, the `petta-memory` OmegaClaw-style prompt/index fixture, and the GoalChainer incident harness. The bounded runtime checker now covers the canonical positional fixture plus two independent keyword variants: ThreadKeeper `gate-id`/`check` atoms and GoalChainer+`petta-memory` `gate-slug`/`name` atoms. `local/check-ggb-gate-petta-runtime.py` loads all five sibling files and queries exact source atom shapes under a 30-second timeout. The positional fixture returns `(partial true)` plus four checks; ThreadKeeper returns `"pass"` plus six checks; the real-memory GoalChainer replay returns `passed` plus eight checks. Evidence is archived at `artifacts/ggb-capacity-gates/20260713-ggb-petta-runtime-smoke/` and `20260713-ggb-keyword-petta-runtime-smoke/`; this is representative cross-project coverage, not a universal schema claim.
5. **OmegaClaw runtime target:** keep Telegram/OpenClaw runs supervised, bounded, and observable; avoid broad new channel authority until communication topology is decided.
6. **Gate-record target:** use `GGB_CAPACITY_GATE_TEMPLATE.md` for each empirical capacity gate so upgrades produce comparable evidence records instead of chat-only claims. As of 2026-07-04, the template explicitly includes source-grounding and claim/evidence-separation fields so mutable state, external exploratory sources, direct observations, inferences, and excluded/untested claims are distinguished in each future gate.
7. **Goal/motivation target:** treat MesTTo `OmegaClaw-GoalChainer` as an external exploratory source for goal-aware/deontic/motivation task selection. Intake map is recorded in `GOALCHAINER_INTEGRATION_MAP.md`; a bounded non-live incident harness is archived at `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/`. As of 2026-07-06, the deontic and directive runtime seams are fixed, and a heuristic PLN belief grader (`heuristic_beliefs.py`) bypasses the PeTTaChainer `compileadd` bottleneck: the full `solve_incident` pipeline runs end-to-end, all 35 tests pass (0 failures), and the pipeline correctly recommends `publish_redacted_summary` with `publish_raw_log` blocked/forbidden. As of 2026-07-06 12:42 UTC, a memory-evidence bridge (`grade_beliefs_heuristic_with_memory()`) now feeds `petta-memory` promoted evidence packets (STV and EC atoms) as read-only inputs that adjust the heuristic belief grader's ground facts via subjective-logic fusion. 18 new tests pass; full suite 53 passed, 6 skipped, 0 failed. Gate archived at `artifacts/ggb-capacity-gates/20260706-goalchainer-memory-evidence-bridge/`. As of 2026-07-06 23:45 UTC, a multi-scenario smoke (34 new tests) verifies differentiated decisions across 4 incident types (PII standard, public data, unverified facts, public+unverified) and 4 conflicting-memory variants, confirming the deontic layer is never overridden by memory evidence and belief profiles are distinct across scenarios. Full suite 87 passed, 6 skipped, 0 failed. Gate archived at `artifacts/ggb-capacity-gates/20260706-goalchainer-multi-scenario-smoke/`. As of 2026-07-07 03:34 UTC, `petta-memory` `run_goalchainer_precompiled_handoff_smoke()` has an optional heuristic-memory probe that calls GoalChainer `solve_incident(memory_items=...)` on handoff cache items; 377 `petta-memory` tests pass and runtime artifact `goalchainer_heuristic_memory_probe_2026-07-07T0334Z.json` decides `publish_redacted_summary` with memory proof evidence and safe leak check. Gate archived at `artifacts/ggb-capacity-gates/20260706-petta-memory-goalchainer-heuristic-probe/`. Next step completed: drafted `docs/omegaclaw_zerobot_topology_decision_note.md` and archived `artifacts/ggb-capacity-gates/20260707-topology-boundary-review/`, recommending a supervised queue-mediated bridge plus read-only GoalChainer sidecar before live bridge changes. Next step completed: archived read-only decision sidecar gate `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/`; it appraised the captured private ThreadKeeper smoke with synthetic read-only `petta-memory` STV/EC evidence, passed 8/8 harness checks, preserved `publish_raw_log` as forbidden/blocked, and changed belief strengths without live integration. Next implementation gates completed: archived `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-contract/`, a non-live contract/spec gate defining a queue-mediated/adjudicated GoalChainer sidecar for candidate summaries; then archived `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-artifact/`, which materializes that contract as a ThreadKeeper queued task with checksum sidecar, runs GoalChainer locally over selected read-only `petta-memory` evidence, and exercises `run_queued_dispatch` with patched in-process dispatch so the queue claim/done/result/checksum path returns `needs_adjudication` without provider/Telegram/runtime side effects. Next step completed: archived `artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator/`, accepting the redacted-summary candidate for offline evidence only after 12/12 artifact checks while explicitly preserving the no-Telegram/no-memory-write/no-runtime-bridge boundary. Next step completed: archived `artifacts/ggb-capacity-gates/20260708-goalchainer-reviewer-policy-thresholds/`, a reusable offline reviewer policy/threshold fixture over the accepted sidecar candidate. It passed 14/14 checks, requiring `needs_adjudication`, redacted-summary recommendation, raw-log block, leak safety, evidence links, non-action preservation, live-scope false flags, and belief thresholds (`redacted_strength >= 0.95`, `raw_strength <= 0.05`, margin `>= 0.80`). Next step completed: archived `artifacts/ggb-capacity-gates/20260709-goalchainer-reviewer-policy-real-memory-replay/`, replaying the reusable reviewer policy against the real `petta-memory` handoff replay candidate. It passed 15/15 checks, accepted the redacted-summary candidate for offline evidence only, preserved raw-log blocking, verified bounded/unchanged real memory evidence, and kept all live-scope flags false. A 2026-07-12 review-boundary replay also caught and closed a canary-policy gap: generic input could queue/accept a permitted raw-log action and recommended outputs skipped adjudication. The canary now uses a sensitive-data fixture, checks forbidden norms before queueing, requires adjudication for every queued output, and limits offline acceptance to redacted summaries; 3 focused tests and an isolated fake-worker replay pass (`20260712-goalchainer-canary-review-boundary`). Next step: keep the sidecar path non-live unless Ben approves private Telegram opt-in with explicit stop conditions.

8. **Persistent-worker cognition substrate:** the isolated `agent/threadkeeper-persistent-workers` branch now has durable lifecycle/status, spawn/cancel, immutable attempts/checkpoints, crash-safe enqueue/requeue, bounded budgets, inbox consumption, event-bound result delivery/acknowledgement, mechanically observed token/tool/runtime accounting, bounded reconciliation, subprocess restart coverage, and exclusive supervisor ownership through `e7e997e`. The combined provider-free gate passes 362 tests; `experiments/20260716T210300Z-threadkeeper-persistent-supervisor-ownership-v1/` records the latest slice. The next artifact is an approval-bound isolated ProtoMegaBot2 canary contract and preflight validator; this track remains isolated from PR #1 and all ProtoMegaBot production paths, and no live canary is authorized.

## Capacity map and empirical gates

The labels below are concise working names for the 25 capacities. Where the original curriculum wording differs, update names without changing the empirical-gate discipline.

| ID | Working capacity | Existing anchor | Near-term empirical gate | Next small task |
|---|---|---|---|---|
| 1.1 | Task framing and done criteria | Project notebooks, `TASKS.md`, runbooks | Partial pass: the archived-record audit verifies six fields; v0.2 seals a GoalChainer offline/live pair, mixed activation negative, paraphrase pair, and invariant policy; an independent content-bound replay confirms all four; the strict interface freezes bounded input/output schemas and nine fail-closed decision triggers (`20260803-request-to-contract-generator-interface`) | Independently review schema completeness and fail-closed semantics; do not implement the generator, and treat five synthetic cases as insufficient evidence of free-form framing quality |
| 1.2 | Bounded memory management | `petta-memory` MemoryCluster journal; OmegaClaw history caps | Partial pass: bounded prompt/index/PLN views, non-live OmegaClaw-style prompt/index fixture, and selected-space `static-import!` runtime fact-membership microbenchmarks pass locally | Next: decide whether the safe normalized `static-import!` loader path should become the first broader inference smoke, while keeping PeTTaChainer `compileadd` bottleneck work isolated |
| 1.3 | Tool/result discipline | Existing project-record updates and checks; ThreadKeeper structured returns | Partial pass: ThreadKeeper hardening gate now has `.metta` sibling fixtures, focused hardening pytest evidence (268 passing tests at head `6e0e49b`), staged no-claim/env-file/@Protomegabot-config async worker-loop smoke gates, opened-fd/stream-capped env-file read evidence, audit/size-cap refresh fixture evidence, async-worker lock hardening fixture evidence, and dedicated query/shell/run-control execution-argument guards | Next: decide PR/update path after PR #1 coordination; keep adding fixture coverage to new gates |
| 1.4 | Safe shell/file execution | ThreadKeeper PR #1 safety floor | Malicious path/shell fixtures fail closed; allowed argv-only command passes | Coordinate remaining work after PR #1 instead of rewriting sandbox code |
| 1.5 | Channel communication | Telegram adapter allowlists, attachment handling, auto-ack | Partial/blocking evidence: non-live preflight found private-smoke defaults unsafe; follow-up `20260710-threadkeeper-telegram-private-defaults-hardening` now makes the private supervisor default to `TG_PRIVATE_ONLY=true` and direct chat `402314199`, but an active supervisor was still observed; no live check run | Handle the active-supervisor boundary and require explicit approval/stop conditions before any live private smoke; keep group/channel targets separate |
| 2.1 | Retrieval and source grounding | Project Markdown, attachments, memory search; `GGB_CAPACITY_GATE_TEMPLATE.md` source-grounding checklist | Partial pass: future gate records now require inspected mutable state, named external source/commit/date when available, and untrusted-content marking rather than chat-only recall | Apply the checklist in the next new gate artifact and keep source-grounding fields concise |
| 2.2 | Claim/evidence separation | `petta-memory` epistemic roles; normalized PLN mapping; Hyperseed p-bit notes | Partial pass: raw quoted/unpromoted claims excluded from PLN view; promoted beliefs require rule/trust/domain metadata | Use the local PeTTaChainer smoke/profiling harness to isolate compile/add bottlenecks before broader normalized `MM-PLN*` inference |
| 2.3 | Experiment representation | `petta-chem` run-contract atoms; EXPO/Hyperseed attachment; `GGB_CAPACITY_GATE_TEMPLATE.md`; `GGB_GATE_RUN_CONTRACT_MAPPING.md` | Partial pass: exp02 run-contract serialization covers config, manifest, events, metrics, ACS candidates, controls, and summary; exp03 adds replayable multi-tick random/control dynamics and aggregate/export atoms; GGB template fields have a thin run-contract mapping; sibling fixtures pass the structural checker; and the canonical positional fixture plus ThreadKeeper `gate-id`/`check` and GoalChainer+memory `gate-slug`/`name` keyword variants load/query successfully in real local PeTTa (`20260713-ggb-petta-runtime-smoke`, `20260713-ggb-keyword-petta-runtime-smoke`) | Use the bounded checker on simple positional/keyword fixtures; define a neutral normalized schema before claiming broader historical coverage |
| 2.4 | Code reading and patch localization | OmegaClaw Telegram/lib_llm_ext patches; ThreadKeeper audit | Agent identifies existing branch/PR and makes a non-overlapping patch plan | For ThreadKeeper, start with timeout/digest/structured-return files only |
| 2.5 | Architecture proposal | OmegaClaw topology notes; memory wrapper sketch; GoalChainer intake map/harness | Partial pass: `GOALCHAINER_INTEGRATION_MAP.md` maps interfaces/risks, deontic and directive runtime seams work locally, heuristic PLN belief grader bypasses PeTTaChainer `compileadd` bottleneck, full `solve_incident` pipeline runs end-to-end through the actual OmegaClaw MeTTa skill surface with correct decisions, memory-evidence bridge feeds `petta-memory` promoted evidence packets into the heuristic belief grader, multi-scenario smoke verifies differentiated decisions across 4 incident types and 4 conflicting-memory variants with deontic invariants holding, `petta-memory` handoff smoke probes `solve_incident(memory_items=...)` from a fixture artifact (377 tests pass), `docs/omegaclaw_zerobot_topology_decision_note.md` recommends a queue-mediated bridge/read-only sidecar before live changes, `20260707-goalchainer-readonly-sidecar-private-task` runs that sidecar over a captured private ThreadKeeper task with 8/8 checks passed, and `20260707-goalchainer-queue-sidecar-contract` validates a non-live queue-mediated/adjudicated sidecar contract against ThreadKeeper's queued-task schema; `20260707-goalchainer-queue-sidecar-artifact` materializes it as a checksum-protected queued task; `20260708-goalchainer-sidecar-offline-adjudicator` accepts the redacted-summary candidate for offline evidence only with 12/12 checks, and `20260708-goalchainer-reviewer-policy-thresholds` turns that into a reusable 14/14 offline reviewer policy/threshold fixture, and `20260709-goalchainer-reviewer-policy-real-memory-replay` replays it on a second real-`petta-memory` candidate with 15/15 checks passed | Next: keep non-live unless Ben explicitly approves private Telegram opt-in with stop conditions; otherwise replay the reviewer policy fixture on additional candidates when available |
| 3.1 | Multi-step planning | OpenClaw/OmegaClaw runbooks; project tasks; gate template | Plan stays current and maps each step to a testable artifact | Use the template on the next two gate bundles and trim fields that prove redundant |
| 3.2 | Bounded delegation | ThreadKeeper dispatch design | Partial pass: child agent receives quotas, allowed paths, cancellation, queued cancellation-token preservation, return schema, per-turn tool-call cap, dispatch wall-clock timeout, patch-proposal-only mode, queue-only dispatch records/backpressure, optional `requires_adjudication` candidate gate, a queued-worker claim/run primitive with failed-claim audit retention, a bounded non-daemon queue drain helper, Ben-approved supervised bounded async worker-loop primitive with lock metadata and operator script, dispatch-level token budget cap, graceful SIGTERM/SIGINT handling, and stale worker lock detection; non-live no-claim, one-task artifact-local, env-file, @Protomegabot-config wrapper, supervisor-boundary, cancellation, supervisor/provider-boundary, private OpenClaw, and multi-task (3-task) smokes now pass and are archived; private OpenClaw smoke candidate output adjudicated and accepted; ThreadKeeper hardened `subagent.py` is byte-identical between source and OmegaClaw-Core runtime tree. Telegram-private preflight/defaults gates now block live private-smoke launch on active-supervisor state plus explicit approval/stop conditions rather than missing private-only/default-chat defaults | Next: resolve the Telegram-private preflight blockers first; then only with explicit approval/stop conditions verify `@Protomegabot` responds, `(delegate ...)` dispatch works, and supervisor stops cleanly |
| 3.3 | Long-context compression | ThreadKeeper bounded digesting; OmegaClaw per-call sessions | Long child transcript is saved locally; parent receives digest plus pointers | Verify transcript persistence/digest fields with a fixture record path in a gate artifact |
| 3.4 | Failure analysis and recovery | Protomegabot stall/segfault/root-cause notes | Failed turn produces visible diagnostic, root-cause note, and re-smoke gate | Convert one recent failure analysis into a reusable run-record example |
| 3.5 | Budget/cost awareness | Fail-closed budget gate; no paid compute policy; ThreadKeeper worker token accounting | Partial pass: unknown budget state blocks expensive/cloud action, local smoke continues, worker LLM token usage is aggregated into transcripts/structured returns, and budget config/usage-log reads are bounded from the opened fd after fstat rechecks | Keep budget checks explicit in task contracts; decide how parent dashboards should consume `worker_token_usage` |
| 4.1 | Peer/subagent communication | ThreadKeeper PR #1; Zar/Oruzi feedback reconciliation; local hardening branch | Parent/child exchange has objective, transcript, summary, uncertainty, next action | Replay the structured child-return fixture into a capacity-gate artifact |
| 4.2 | Cross-system bridge discipline | OmegaClaw↔OpenClaw provider; Telegram boundaries | Bridge has explicit auth, session, timeout, and failure semantics | Decide raw-model route vs full OpenClaw-agent route for OmegaClaw backend |
| 4.3 | Shared memory coordination | `petta-memory` read-only wrapper branch; generated `MM-index`/`index-view`; GoalChainer memory-evidence bridge | Partial pass: read-only bridge prompt view and generated index are smoke-tested together on an OmegaClaw-style fixture; GoalChainer's heuristic belief grader accepts `petta-memory` promoted evidence packets (STV and EC atoms) via `grade_beliefs_heuristic_with_memory()` and fuses them with keyword-derived ground facts; multi-scenario smoke (34 tests) verifies differentiated decisions across 4 incident types and 4 conflicting-memory variants with deontic invariants holding; `petta-memory` has a non-live `goalchainer-smoke --heuristic-memory-probe` artifact checking the actual `solve_incident(memory_items=...)` path; the read-only sidecar gate applies selected evidence to a captured private ThreadKeeper task without memory writes; the queue-sidecar contract gate narrows any future sidecar to selected read-only evidence and candidate-only adjudicated output; the queue-sidecar artifact gate now materializes that contract as a checksum-protected ThreadKeeper task and returns `needs_adjudication` via patched non-provider queue dispatch; the offline adjudicator gate accepts the resulting redacted-summary candidate for evidence only while preserving no-write/no-live boundaries; the reviewer-policy gate now captures reusable threshold/non-action/evidence criteria for future sidecar candidates, and the real-memory policy replay shows the same thresholds accept a second archived candidate while preserving read-only/no-live boundaries | Keep live writes disabled; next replay the reviewer policy fixture on additional candidates when available or wait for explicit private Telegram approval with stop conditions |
| 4.4 | Scientific collaboration loops | `petta-chem` exp00/exp01/exp02 contract/replay/ablation | Partial pass: exp02 small sweep discriminates random-polymer fixtures from shuffled/no-catalysis controls under run-contract records | Use exp03 dynamic aggregate/export records as the next evidence pattern before stronger emergence claims |
| 4.5 | Patch proposal/adjudication | ThreadKeeper `patch_proposal_only` + `requires_adjudication` task contracts; queue-only dispatch records | Partial pass: child `write-file`/`append-file` calls can record full proposed changes in transcript without mutating workspace, high-stakes outputs can be flagged as candidates needing adjudication, async dispatch can persist a queue record without calling a worker LLM, queued records can be claimed/drained in bounded operator-supervised batches while failed claims are retained for audit, the supervised async worker loop can poll boundedly under explicit max-task/idle/runtime/stop-file controls, done/failed result sidecars are ignored by pending-queue listing/backpressure and rejected if explicitly passed as worker tasks, malformed/tampered/schema-invalid queued records fail closed before worker LLM calls, queued cancellation tokens are preserved into worker execution, dispatch-level token budget caps are active, graceful SIGTERM/SIGINT allows supervisor-controlled shutdown, and a non-mutating transcript review helper verifies checksum sidecars and reports proposal/adjudication gates without applying or accepting anything | Next: run the staged Telegram-private supervisor smoke; add explicit apply/adjudicator routing harnesses if needed; keep worker-loop launch under operator/supervisor control and do not accept/apply reviewed candidates without explicit approval |
| 5.1 | Governance boundaries | Allowlists, private-only modes, project safety notes | New live authority requires decision record and rollback/stop path | Draft communication-topology decision before new live group bridge |
| 5.2 | Audit/accounting integrity | Project records, run manifests, transcripts; ThreadKeeper transcript SHA-256/index/token accounting | Partial pass: subagent transcripts have checksum sidecars/index records, required `.sha256` sidecars reject symlink/non-regular paths before digest reads, workspace lock files, workspace file-tool source reads, and run-index tail/rotation paths reject symlink/non-regular or predictable-temp redirection, worker token accounting in persisted run records, transcript audit paths, JSON audit-write destinations, transcript-sidecar destinations, and per-endpoint LLM guard-state files reject symlink/non-regular redirection, queued-worker failures retain `.failed` task/result audit records, explicit worker calls reject retained result sidecars before claim/rename, queued-task checksum/schema validation rejects malformed/coerced records before worker LLM calls, queued cancellation tokens are preserved into worker execution, async worker-loop runs leave compact lock/status metadata for operator audit, dispatch-level token budget is capped, and graceful SIGTERM/SIGINT exit leaves final lock metadata for audit, and stale worker lock detection reports crashed previous worker metadata (pid, started_at, etc.) when a new worker acquires an abandoned flock, and run index entry bounding via `OMEGACLAW_SUBAGENT_MAX_INDEX_ENTRIES` rotates the audit log to prevent unbounded growth with recomputed hash chain for retained entries, budget usage/escalation audit-log parents reject symlink/non-directory ancestors before writes, run-index/transcript audit reads enforce bounded no-follow/regular-file checks, and budget config/usage-log reads are capped after fd-level size rechecks, and persona/emit protocol hardening is recorded before candidate/adjudication acceptance | Decide PR/update path and whether the parent should verify transcript sidecars plus worker-loop lock/result records before trusting child digests |
| 5.3 | Robustness to adversarial/ambiguous input | Attachment untrusted markers; parser validation | Prompt/file injection fixtures are treated as untrusted data and cannot change policy | Add a hostile attachment/prompt fixture to capacity-gate tests |
| 5.4 | Transparency and calibrated uncertainty | Notes, diagnostics, decision logs; gate-template claim/evidence separation | Partial pass: future gate records now separate direct observations/check outputs from inferences/design judgments and explicitly list unsupported/untested claims excluded | Add `uncertainty` to ThreadKeeper structured returns where it is useful and keep gate summaries calibrated |
| 5.5 | Self-improvement loop governance | This roadmap; project notebooks; GoalChainer verification-posture note | Capacity upgrades are reviewed as empirical gates, not self-modifying autonomy; first GoalChainer/self-improvement-adjacent gates can use crude PLN/heuristic plausibility checks while preserving risk tiers | Keep upgrades in local branches/artifacts; no prompt/safety/tool-policy/runtime-behavior changes without explicit request |

## First gate bundle to execute

**Bundle A: ThreadKeeper reliability + recordability (supports 1.1, 1.3, 2.4, 3.2, 3.3, 3.5, 4.1, 4.5, 5.2, 5.4). Status: implemented locally and archived; focused local pytest evidence (268 tests at head `6e0e49b`) and `.metta` sibling fixtures pass; private OpenClaw smoke adjudicated and accepted; multi-task (3-task) smoke passed; Telegram-private defaults are now private-only/direct-chat by default, but live smoke still needs active-supervisor handling plus explicit approval/stop conditions.**

- Prerequisite: inspect PR #1 branch and avoid edits to its sandbox/shell/budget safety-floor code unless rebasing requires it.
- Implemented on local branch `agent/threadkeeper-hardening-next`: subagent LLM timeout with retry/backoff and clear failure result; bounded child-history/digesting; persistent transcript/run-record path; structured JSON returns; atomic subagent writes; strict tool argument validation; tool-call quota; cancellation token; optional escalation policy integrity pin; patch-proposal-only mode for parent-reviewed workspace changes.
- Checks recorded in `TASKS.md`/`NOTES.md`: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct assertion replay passed for retry/failure, arg validation, atomic writes, bounded digesting, structured return, transcript persistence, file-change tracking, quota, cancellation, and escalation hash mismatch. The focused mock pytest gate now passes locally via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`250 passed` as of head `be5ea1f`, including queued-dispatch path bounding, worker stop-file/cancel-file control-character rejection, symlink workspace-root rejection, shell/query argument control-character rejection, persona config scalar validation, unquoted final-emit trailing-payload rejection, strict task-contract allowed_paths validation, file-tool control-character rejection, queued-dispatch directory symlink rejection, workspace file-tool no-follow read coverage and parent-directory symlink hardening, dispatch timeout, worker token accounting, hash-chained run-index coverage, run-index verifier coverage, patch-proposal-only coverage, queue-only/backpressure coverage, requires-adjudication coverage, candidate-review coverage, queued-worker claim/run coverage, failed-claim retention coverage, bounded queue-drain coverage, ignored/rejected result-sidecar coverage, queued task-contract preservation, missing/mismatched queue checksum rejection, queued-task schema validation, queued task-contract schema validation, coerced queued integer rejection, queued cancellation-token preservation, queued task max-age rejection, transcript turn/field bounding, retry backoff jitter, worker-loop results bounding, live lock metadata, consecutive-error cap, dispatch-level token budget cap, graceful SIGTERM/SIGINT handling, stale worker lock detection, final emit/response/audit-read bounding, supervised async worker-loop lock/stop/runtime/error-continuation/config-validation behavior, and operator-script no-claim smoke, env-file runner support, unsafe env-file key rejection, bounded env-file parsing, staged @Protomegabot-config wrapper/supervisor/cancellation smoke, bounded async-worker lock metadata reads, symlink/non-regular async-worker lock rejection, signal-state cleanup after supervised worker-loop runs, fail-closed inline/persona task-contract list validation, run-index symlink/non-regular rejection, required `.sha256` integrity sidecar symlink/non-regular rejection, workspace file-lock symlink/non-regular rejection, run-index tail/rotation write hardening, per-endpoint worker LLM guard-state symlink/non-regular rejection, transcript audit symlink/non-regular rejection, JSON audit-write/transcript-sidecar symlink destination rejection, workspace read-file/append-file source no-follow regular-file coverage, quoted-final-emit trailing-payload protocol violation coverage, worker usage-log parent hardening, budget audit-log parent hardening, transcript audit size-check nofollow hardening, and budget accounting/config read-cap hardening).
- Core hardening gate record archived at `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`; staged worker-loop gates now include `20260705-threadkeeper-worker-loop-smoke`, `20260705-threadkeeper-worker-loop-one-task`, `20260705-threadkeeper-worker-env-runner`, `20260705-threadkeeper-protomegabot-config-smoke`, `20260705-threadkeeper-protomegabot-one-task-smoke`, `20260705-threadkeeper-worker-supervisor-boundary`, `20260705-threadkeeper-worker-supervisor-cancelled-task`, `20260705-threadkeeper-worker-supervisor-provider-smoke`, `20260705-threadkeeper-private-openclaw-smoke` (adjudicated and accepted), `20260705-threadkeeper-multi-task-smoke`, `20260705-threadkeeper-telegram-private-integration` (pending smoke), and `20260707-threadkeeper-audit-cap-refresh`, plus `20260708-threadkeeper-sidecar-read-cap-refresh`, `20260708-threadkeeper-bounded-read-refresh`, `20260708-threadkeeper-worker-lock-hardening`, `20260709-threadkeeper-contract-validation-refresh`, `20260709-threadkeeper-integrity-sidecar-hardening`, and `20260709-threadkeeper-audit-path-hardening`, and `20260709-threadkeeper-transcript-guard-hardening`, plus `20260709-threadkeeper-audit-write-hardening`, and `20260710-threadkeeper-workspace-file-nofollow-hardening`, plus `20260710-threadkeeper-parent-symlink-hardening`, `20260710-threadkeeper-accounting-protocol-hardening`, and `20260710-threadkeeper-queue-dir-symlink-hardening`, plus `20260710-threadkeeper-file-tool-guardstate-hardening`, and `20260710-threadkeeper-task-contract-path-hardening`, and `20260711-threadkeeper-budget-audit-parent-hardening`, plus `20260711-threadkeeper-audit-readcap-hardening` and `20260711-threadkeeper-persona-emit-protocol-hardening`; `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) now pass `local/check-ggb-gate-fixtures.py` for the fixture-bearing ThreadKeeper/GoalChainer/memory/chemistry gates (excluding older mapping-only records without sibling fixtures).
- Latest follow-up gate `20260713-threadkeeper-unicode-control-arg-hardening` records head `6e0e49b` / 268 focused tests for rejecting unsafe Unicode controls/formatting and lone surrogates in file, query, shell, queued-dispatch, worker-stop, and queued-task cancellation paths before effects, queue claim, or worker-lock creation; prior gate `20260712-threadkeeper-quoted-tool-protocol-hardening` records head `dd3f7e5` / 258 focused tests for fail-closed unterminated quoted single arguments and malformed quoted file-content calls before execution/workspace mutation; prior gate `20260712-threadkeeper-shell-arg-hardening` records head `76ec6b6` / 256 focused tests for a dedicated optional-shell command length cap before parsing/execution; prior gate `20260712-threadkeeper-technical-analysis-arg-hardening` records head `35c0c98` / 254 focused tests for bounded market-symbol grammar before `technical-analysis` execution; prior gate `20260712-threadkeeper-worker-env-read-hardening` records head `6a9452d` / 252 focused tests for no-follow, opened-fd-bounded, strict-UTF-8 worker env-file reads before `subagent` import; prior gate `20260711-threadkeeper-run-control-path-hardening` records head `be5ea1f` / 250 focused tests for queued-dispatch path bounding plus worker stop-file and queued-task cancel-file control-character rejection; prior gate `20260711-threadkeeper-workspace-command-arg-hardening` records head `9b00e38` / 246 focused tests for symlink workspace-root rejection plus shell/query argument control-character rejection; prior gate `20260711-threadkeeper-persona-emit-protocol-hardening` records head `bf65398` / 242 focused tests for fail-closed persona config scalar validation plus unquoted final-emit trailing-payload rejection; prior gate `20260711-threadkeeper-audit-readcap-hardening` records head `bedfadb` / 237 focused tests for run-index/transcript audit read bounding plus budget accounting/config fd read-cap hardening; prior gate `20260711-threadkeeper-budget-audit-parent-hardening` records budget usage/escalation audit-log parent hardening; prior gate `20260710-threadkeeper-task-contract-path-hardening` records strict task-contract `allowed_paths` validation and file-tool control-character rejection; the prior `20260710-threadkeeper-file-tool-guardstate-hardening` gate records non-relative file-tool path rejection and symlinked worker LLM guard-state parent rejection, and `20260710-threadkeeper-queue-dir-symlink-hardening` records queued-dispatch directory symlink rejection. Next small task: handle the remaining `20260708`/`20260710` Telegram-private preflight blocker before any live private smoke: defaults now match private-only/direct-chat intent, but an active supervisor was observed during the gate and must not be interrupted or reused without explicit approval/stop conditions. Keep live group/broader enablement as separate decisions.

**Bundle B: Memory prompt-view/index smoke (supports 1.2, 2.1, 2.2, 4.3). Status: two partial gates archived; live OmegaClaw integration still intentionally disabled.**

- Use `petta-memory` read-only OmegaClaw wrapper sketch; no live/autonomous writes.
- Fixture coverage now includes bounded prompt recall, index/direct-query parity, e2e promoted/unpromoted claim separation, and default-disabled/read-only OmegaClaw bridge tests.
- Checks recorded in `artifacts/ggb-capacity-gates/20260701-petta-memory-prompt-view/RUN.md`: original gate passed 34 stdlib tests and `git diff --check`; subsequent `petta-memory` project records reported bounded rendering, wrapper hardening, PeTTa parser validation, PeTTaChainer STV/EvidencePacket export, and isolated profiling up to 67 stdlib tests. Follow-up gate `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/RUN.md` adds a non-live OmegaClaw-style prompt/index fixture; current local verification passes 88 stdlib tests plus non-live selected-space static-import runtime fact-membership microbenchmarks and the GGB sibling-fixture checker.
- Gate result: bounded prompt view keeps relevant topic/status atoms under budget, `MM-index` parity matches direct id/type/about/status/role queries, PLN-safe view excludes raw/unpromoted claims and emits normalized promoted-premise metadata, and the read-only OmegaClaw bridge now has a fixture that combines `prompt_view_metta()` with `index_view`. The gate now also has `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) that pass `local/check-ggb-gate-fixtures.py` alongside the petta-chem and ThreadKeeper gates. Next small task: decide whether the normalized static-import path is enough for a first broader inference smoke; keep live OmegaClaw memory wiring behind the reviewed boundary gate.

**Bundle C: Scientific run-contract reuse (supports 2.3, 4.4, 5.2, 5.4). Status: partial gates archived; source run-contract pattern verified, a thin GGB-template-to-run-contract mapping exists, sibling fixture files pass the structural checker, and the canonical positional fixture now passes a real local PeTTa load/query gate.**

- Use `petta-chem` run-contract atoms as the template for Protobot capacity-gate records.
- Current source pattern: exp02 has planted reciprocal-pair and generated-unplanted random/control families, `exp02-sweep-point`/summary atoms, per-run contract serialization for seventy-five current exp02 records, a factored generated-control template through seed-107, a sweep-kind report, and exp03 dynamic run-record/export/aggregate atoms over tested full-source random/control families.
- Checks recorded in `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/RUN.md`: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, and `git diff --check` passed in `petta-chem` commit `4a80388`. Follow-up mapping gate `artifacts/ggb-capacity-gates/20260701-ggb-run-contract-mapping/RUN.md` added `GGB_GATE_RUN_CONTRACT_MAPPING.md` after inspecting `src/run_contract.metta` and the run-contract README.
- `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) added under `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/`, `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/`, and `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/` following the mapping in `GGB_GATE_RUN_CONTRACT_MAPPING.md`. `local/check-ggb-gate-fixtures.py` now verifies required files, balanced fixture syntax, exactly one top-level `run-summary`, and `RUN.md` check coverage by `ggb-check` atoms; it passes on all three gates. Source checks re-verified separately: `run_exp02.sh`, `test_exp02_contract_files.sh`, and `git diff --check` all pass.
- Gate result: `petta-chem` provides a concrete evidence-record pattern for config, manifest/provenance, metrics, ACS candidates, ablations, controls, caveats, and replay/status summaries. `GGB_GATE_RUN_CONTRACT_MAPPING.md` maps GGB gate fields onto this pattern using companion atoms for non-chemistry gates. Sibling fixtures demonstrate that the mapping is serializable and structurally checkable across scientific, software-governance, memory-read, and goal-arbitration gates. The `20260713-ggb-petta-runtime-smoke` closes the minimal runtime gap for the canonical positional shape; `20260713-ggb-keyword-petta-runtime-smoke` now adds independent ThreadKeeper and GoalChainer+`petta-memory` keyword variants without rewriting source fixtures. Next small task: use the checker on known simple variants and design a neutral normalized schema before claiming broad historical coverage.

**Bundle D: GoalChainer intake / non-live goal-arbitration gate (supports 2.2, 2.5, 3.1, 4.3, 5.1, 5.5). Status: full pipeline functional with heuristic PLN fallback; memory-evidence bridge implemented; multi-scenario, `petta-memory` handoff-probe, topology-boundary, and private-task read-only sidecar gates passed; no live runtime integration.**

- Source inspected: MesTTo `OmegaClaw-GoalChainer` at commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`.
- Integration map: `GOALCHAINER_INTEGRATION_MAP.md` covers inputs/outputs, OmegaClaw skill surface, PeTTa/PeTTaChainer/MetaMo/directive dependencies, `petta-memory` evidence handoff shape, and non-live smoke gate proposal.
- Gate records: `artifacts/ggb-capacity-gates/20260702-goalchainer-intake/RUN.md`, `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/RUN.md`, `artifacts/ggb-capacity-gates/20260706-goalchainer-deontic-directive-fix/RUN.md`, `artifacts/ggb-capacity-gates/20260706-goalchainer-heuristic-pln-bypass/RUN.md`, `artifacts/ggb-capacity-gates/20260706-goalchainer-skill-surface-smoke/RUN.md`, `artifacts/ggb-capacity-gates/20260706-goalchainer-memory-evidence-bridge/RUN.md`, `artifacts/ggb-capacity-gates/20260706-goalchainer-multi-scenario-smoke/RUN.md`, `artifacts/ggb-capacity-gates/20260706-petta-memory-goalchainer-heuristic-probe/RUN.md`, and `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/RUN.md`.
- Checks: Python source compile passed. Deontic/directive/scoring/skill tests pass (15 tests). Full GoalChainer suite reached `87 passed, 6 skipped, 0 failed` after the multi-scenario smoke. `petta-memory` GoalChainer smoke tests now include the optional heuristic-memory probe: 7 focused tests passed, full `petta-memory` unittest suite passed (`377 passed`), `git diff --check` passed, and runtime artifact `goalchainer_heuristic_memory_probe_2026-07-07T0334Z.json` reports `heuristic_with_memory_path_checked=True`, `decided=publish_redacted_summary`, `memory_proof_present=True`, `leak_check_safe=True`. Full `solve_incident` pipeline returns correct decision (`publish_redacted_summary` recommended, `publish_raw_log` blocked/forbidden, `hold_external_update` weak/permitted).
- Heuristic PLN belief grader: `heuristic_beliefs.py` mirrors PLN rule semantics using subjective-logic fusion, bypassing the PeTTaChainer `compileadd` 8 GB stack-limit bottleneck. Automatic fallback via `_pettachainer_available()` quick check and module-level failure cache. `petta_runtime.py` has 30s subprocess timeout with `TimeoutExpired` handling.
- Memory-evidence bridge: `grade_beliefs_heuristic_with_memory()` accepts optional `petta-memory` handoff cache items (STV atoms and EvidencePacket EC atoms) and fuses them with keyword-derived ground facts using the same subjective-logic combination rule. The `parse_memory_evidence()` function parses handoff cache items into `MemoryEvidenceItem` objects. Memory grounds use their own strength/confidence directly (no rule-chain product). The bridge is wired through `reason_over_hyperbase()` and `solve_incident()` via optional `memory_items` parameters. When no memory items are provided, behavior is identical to the baseline heuristic.
- Sibling fixture status: `.metta` sibling fixtures pass `local/check-ggb-gate-fixtures.py` for the new `20260706-petta-memory-goalchainer-heuristic-probe` gate and earlier GoalChainer gates.
- Skill surface smoke: first end-to-end demonstration of GoalChainer through the actual OmegaClaw MeTTa skill surface (`run_in_omegaclaw.metta` with `(eval (goalchainer-decision ...))` and `(eval (goalchainer-solve ...))` via PeTTa/SWI). Also verified via Python CLI for `goalchainer-decision`, `goalchainer-solve`, and `goalchainer-directive`. All produce correct decisions: `publish_redacted_summary` recommended/obligated, `publish_raw_log` blocked/forbidden, `hold_external_update` weak/permitted. Solve produces redacted artifact with leak check safe=True. Directive maps to ready/blocked/backlog task states with responder claim.
- Next small tasks completed: `20260707-goalchainer-queue-sidecar-contract` defines and validates a queue-mediated/adjudicated sidecar contract for candidate summaries; `20260707-goalchainer-queue-sidecar-artifact` materializes the contract as a checksum-protected ThreadKeeper queued task and returns a GoalChainer candidate through patched non-provider `run_queued_dispatch` with `needs_adjudication`; `20260708-goalchainer-sidecar-offline-adjudicator` accepts that candidate for offline evidence only after 12/12 checks; `20260708-goalchainer-reviewer-policy-thresholds` adds a reusable offline reviewer policy/threshold fixture and passes 14/14 checks. `20260709-goalchainer-reviewer-policy-real-memory-replay` replays the same policy on the real `petta-memory` handoff replay candidate and passes 15/15 checks, preserving offline-only acceptance and no-live/no-write boundaries. Next small task: replay the policy on additional candidates when available, or ask Ben for explicit private Telegram opt-in approval with stop conditions before any live bridge/runtime behavior changes.

## Open decisions for Ben

- OmegaClaw↔ZeroBot/OpenClaw topology: Telegram group, local IPC/session bridge, raw-model route, or no direct live bridge yet.
- Whether the GGB capacity names in this file should be replaced with the exact curriculum labels from the original attachment if/when available.
