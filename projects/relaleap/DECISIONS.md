# Decision Log

## D-20260808-frame-oracle-v14-author-io-contract

- Date: `2026-08-08`
- Status: `adopted; interface only; Stage A remains blocked`
- Evidence:
  `experiments/20260808T232600Z-frame-oracle-v14-author-io-contract-r2/`

Require any future local Stage-A author attempt to use exactly one pre-hashed
request and one response, write the frozen bundle once with the manifest last,
and retire irreversibly on any interaction, schema, premise, provenance, or
mutation failure. The persistent worker may not supply prompt content or repair
the response. This contract does not prove model-load compatibility or author
eligibility and authorizes no inference. V14 remains sealed and unconsumed.

## D-20260808-frame-oracle-v14-combined-runtime-discovery

- Date: `2026-08-08`
- Status: `adopted; discovery only; Stage A remains blocked`
- Evidence:
  `experiments/20260808T212629Z-frame-oracle-v14-combined-runtime-discovery-r2/`

Accept the 22-entry combined closure and isolated runner device-discovery
receipt only as control/runner startup compatibility. Do not infer model-load
compatibility, noninteractive bundle compatibility, independent authorship, or
Stage-A eligibility. No request, model load, fixture input, sealed access, or
semantic evaluation occurred; v14 remains sealed, unopened, and unconsumed.

## D-20260808-frame-oracle-v14-runner-isolated-availability

- Date: `2026-08-08`
- Status: `adopted; availability only; Stage A remains blocked`
- Evidence:
  `experiments/20260808T192443Z-frame-oracle-v14-runner-isolated-availability-r2/`

Accept the hash-pinned runner's 14-entry direct dynamic closure and isolated
`--help` receipt as proof of executable availability only. Do not infer model
loadability, bundle compatibility, or author eligibility. Preserve r1's
origin-relative private-library counterexample. No request, model mount/load,
fixture, sealed access, or semantic evaluation occurred; v14 remains sealed,
unopened, and unconsumed.

## D-20260808-frame-oracle-v14-stage-a-isolation-primitive

- Date: `2026-08-08`
- Status: `BOUNDARY_VERIFIED; STAGE_A_NOT_EXECUTED`
- Evidence:
  `experiments/20260808T051702Z-frame-oracle-v14-stage-a-isolation-probe-r3/`

Use a fresh Bubblewrap-restricted process for Stage A: expose only the four
frozen allowlisted files read-only, verify their manifest, unshare networking,
and leave all project history, experiments, sealed paths, and candidate v14
code absent. The persistent worker may verify the wrapper and receipts but may
not author or suggest fixture content. This probe establishes mechanical
feasibility only; it created neither randomness nor fixtures and does not
authorize Stage B, runner work, inference, readout, or semantic loss.

## D-20260806-epc-c1-repeated-concurrent-provisioning-stop

- Date: `2026-08-06`
- Status: `BLOCKED_CONCURRENCY; second cleanup COMPLETE_VERIFIED`
- Evidence:
  `experiments/20260806T004532Z-epc-c1-second-concurrent-pod-audit/`,
  `experiments/20260806T004538Z-epc-c1-second-concurrent-pod-termination/`,
  `experiments/20260806T004552Z-epc-c1-post-second-concurrent-pod-provider-audit/`,
  and `experiments/20260806T004558Z-epc-c1-second-concurrent-pod-billing/`

Stop all C1 lifecycle activity for this activation. A competing writer recreated
an out-of-envelope pod immediately after the first containment, proving that
the provider lifecycle is not under single-writer control. The second pod was
also deleted before readiness and provider state is empty. No future
provisioning or science execution is admissible until the parent establishes
one lifecycle writer. Pending billing may be queried read-only later.

## D-20260806-epc-c1-concurrent-out-of-envelope-pod-containment

- Date: `2026-08-06`
- Status: `cleanup COMPLETE_VERIFIED; BLOCKED_CONCURRENCY; billing pending`
- Evidence:
  `experiments/20260806T004226Z-epc-c1-out-of-envelope-concurrent-pod-audit/`,
  `experiments/20260806T004237Z-epc-c1-out-of-envelope-concurrent-pod-termination/`,
  `experiments/20260806T004247Z-epc-c1-post-concurrent-pod-termination-provider-audit/`,
  and `experiments/20260806T004305Z-epc-c1-out-of-envelope-concurrent-pod-billing/`

Contain pod `dnwq8koj3rtu45` as out of the current frozen envelope. It was
created after this activation's clean provider audit by a concurrent writer,
named `relaleap-epc-c1-any-available-20260806`, and used a mutable Runpod image
tag rather than the approved digest. It had one GPU at `$0.44/hour`, a 50 GB
disposable disk, no network volume, and was not SSH-ready. Exact deletion
succeeded before any remote/science command; subsequent active pod and
serverless endpoint lists were empty. Itemized billing is pending; use the
approximately `$0.0177` elapsed-time estimate only as provisional.

Retain `BLOCKED_CONCURRENCY`. Exact US-West capacity also remains unavailable.
No future provisioning is admissible until one lifecycle writer is established,
even if provider inventory appears.

## D-20260806-epc-c1-current-us-west-scope-and-accounting

- Date: `2026-08-06`
- Status: `BLOCKED_ENVIRONMENT; exact approval unconsumed; Canada accounting resolved`
- Evidence:
  `experiments/20260806T003615Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r36/`,
  `experiments/20260806T003645Z-epc-remediation-c1-runpod-capacity-recheck-r35/`,
  `experiments/20260806T003725Z-epc-c1-unauthorized-canada-pod-billing-recheck-r2/`,
  and `experiments/20260806T003730Z-epc-c1-unauthorized-eu-pod-billing-recheck/`

For this worker, follow the current cron payload's exact US-West-only scope;
do not use earlier broader-region records to alter it. The exclusive writer
lock admitted this activation, all 14 original hashes passed, and no active
pod or serverless endpoint existed. A40 remained `$0.44/GPU-hour`, but none of
the six approved US-West centers exposed inventory. Therefore retain
`BLOCKED_ENVIRONMENT`, create no substitute resource, and leave Ben's exact
approval unconsumed. Preserve unowned commit `19bdbad` without adopting it;
the approved package remains bound to `6a08771`.

Replace the Canada pod's elapsed-time estimate with the provider's itemized
charge of `$0.032451326376758516` for `260776` billed milliseconds and 50 GB
billed disk. EU billing remains `PENDING_ACCOUNTING`; an empty itemization is
not evidence of zero cost, so retain the approximate `$0.104` estimate.

## D-20260806-epc-c1-eu-authority-incident-cleanup

- Date: `2026-08-06`
- Status: `resource terminated under current cron envelope; conflicting broader authority discovered; accounting pending`
- Evidence:
  `experiments/20260806T001936Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r35/`,
  `experiments/20260806T001954Z-epc-remediation-c1-runpod-capacity-recheck-r34/`,
  `experiments/20260806T002011Z-epc-c1-unauthorized-eu-pod-audit/`,
  `experiments/20260806T002022Z-epc-c1-unauthorized-eu-pod-termination/`,
  `experiments/20260806T002032Z-epc-c1-post-eu-termination-provider-audit/`,
  and `experiments/20260806T002117Z-epc-c1-unauthorized-eu-pod-billing/`

Under the current cron's explicit US-West-only envelope, EU pod
`codx4k4n26px4u` was out of scope. Its provider record showed creation at
`2026-08-06T00:06:11.887Z`,
one A40 at `$0.44/hour`, the pinned image, 50 GB disposable container disk, no
network volume, and `pod not ready`. Terminate it immediately to contain spend;
deletion returned `deleted:true`, and repeat queries showed zero active pods and
zero serverless endpoints. No remote connection or science input was opened.

Itemized accounting returned no record and remains pending. Creation-to-
deletion elapsed about 14.2 minutes, implying approximately `$0.104` compute at
the observed rate. A subsequent durable-memory check found a `17:05 PDT`
record of Ben broadening ePC authority to “any machine that works and is
available,” while this job's later `17:17 PDT` payload again binds execution to
US-West. Preserve both records without silently choosing one. Retain
`BLOCKED_AUTHORITY` plus `BLOCKED_CONCURRENCY`; no new provisioning is
admissible until the parent reconciles scope and confirms a single writer.

## D-20260805-epc-c1-canada-authority-incident-cleanup

- Date: `2026-08-05`
- Status: `out-of-envelope resource terminated; accounting pending; Canada amendment not adopted`
- Evidence:
  `experiments/20260805T233242Z-epc-c1-canada-amended-package/`,
  `experiments/20260805T235626Z-epc-c1-unauthorized-canada-pod-termination/`,
  `experiments/20260805T235720Z-epc-c1-post-termination-active-pod-audit/`,
  `experiments/20260805T235725Z-epc-c1-unauthorized-canada-pod-billing/`,
  `experiments/20260805T235835Z-epc-c1-post-amendment-frozen-envelope-audit/`,
  and
  `experiments/20260805T235900Z-epc-remediation-c1-runpod-capacity-recheck-r33/`

Reject the unowned Canada amendment as an authority record. The binding cron
payload at the amendment's purported approval time retained only one Secure
Cloud A40 in US-West; Git authorship and a source constant cannot broaden that
operator approval. Preserve clean unowned commit `19bdbad` without reverting,
merging, or executing it.

Terminate Canada pod `y77tenzngn59ga` to stop out-of-envelope spend. Deletion
succeeded before SSH readiness or any C1 bundle/model/data/CUDA/science action,
and repeat queries showed no active pods or serverless endpoints. The pod had
no network volume and its 50 GB disposable container disk is unrecoverable.
Itemized billing is pending; the elapsed-time estimate is about `$0.166`, but
pre-existing account storage spend prevents exact balance-delta attribution.

Continue only with the original 14-file US-West envelope, which still passes
every frozen hash and remains bound to approved commit `6a08771`. Exact
US-West A40 capacity remains unavailable, so retain `BLOCKED_ENVIRONMENT` and
leave Ben's exact approval unconsumed.

## D-20260805-epc-c1-exact-capacity-blocker

- Date: `2026-08-05`
- Status: `BLOCKED_ENVIRONMENT; standing approval unconsumed`
- Evidence:
  `experiments/20260805T232935Z-epc-remediation-c1-frozen-envelope-integrity-revalidation-r34/`
  and
  `experiments/20260805T232946Z-epc-remediation-c1-runpod-capacity-recheck-r32/`

Retain the exact frozen C1 lifecycle without substitution. All 14 bound hashes
passed immediately before the provider query, and Secure Cloud A40 pricing
remained exactly `$0.44/GPU-hour`; however, none of the six approved US-West
data centers exposed A40 inventory. Stock existed only outside the approved
region. The latest recheck at `2026-08-05T23:29Z` found stock only in
`CA-MTL-1` (`Low`) and `EU-SE-1` (`Medium`); all six approved US-West centers
remained empty. Therefore
provision nothing, open no science input or seed, and keep Ben's exact approval
unconsumed until the same resource appears within bounds.

## D-20260805-epc-c1-provider-free-end-to-end-cleanup-closure

- Date: `2026-08-05`
- Status: `adopted; provider-free lifecycle closure verified; C1 science blocked by activation scope`
- Evidence:
  `experiments/20260805T123833Z-epc-remediation-c1-cleanup-closure-spec-freeze/`,
  `experiments/20260805T124254Z-epc-remediation-c1-cleanup-closure-artifact-clean/`,
  `experiments/20260805T124322Z-epc-remediation-c1-cleanup-closure-cmp-clean/`,
  `experiments/20260805T124331Z-epc-remediation-c1-cleanup-closure-focused-clean/`,
  and
  `experiments/20260805T124343Z-epc-remediation-c1-cleanup-closure-full-suite/`
- Specification: commit `be63733`, SHA-256
  `70347f7dc77bdeb1c5628767fc4f7b49ca8dba636af13b15b986ea90bfc37c7c`
- Implementation: `agent/epc-remediation-a0` final clean commit `6a08771`

Adopt the deterministic local end-to-end closure. Only an intact successful
receipt bridge may advance; returned bytes are re-attested before the frozen
five-seed adjudicator runs, and cleanup is accepted only after exact termination
evidence, deleted container disk, zero remaining provider resources, monotone
timestamps/counters, and final cost within the hard cap. The three new events
bind artifact, adjudication, and cleanup attestation digests exactly.

Independent synthetic closures were byte-identical (SHA-256
`a248dc6840764470e51b3eb8bb5aa755101441a37613cbbbb94cdff488e2007b`).
A frozen statistical failure closes but does not admit transformer execution;
named corruptions fail closed. Fifteen focused/prior-seam and 287 full-suite
tests passed. This is synthetic local integration evidence only. No packaged
command, provider, science input/seed, CUDA query, GPU, or paid service ran.
Actual C1-A execution remains blocked whenever an activation explicitly
prohibits the otherwise approved paid/GPU envelope.

## D-20260805-epc-c1-provider-free-return-monitor-bridge

- Date: `2026-08-05`
- Status: `adopted; local return/monitor closure verified; provider/C1 science unrun`
- Evidence:
  `experiments/20260805T120950Z-epc-remediation-c1-return-bridge-spec-freeze/`,
  `experiments/20260805T121734Z-epc-remediation-c1-return-bridge-artifact-clean-r3/`,
  `experiments/20260805T121757Z-epc-remediation-c1-return-bridge-cmp/`,
  `experiments/20260805T121806Z-epc-remediation-c1-return-bridge-focused-clean/`,
  and
  `experiments/20260805T121818Z-epc-remediation-c1-return-bridge-full-suite/`
- Specification: commit `f6a7165`, SHA-256
  `7170ec61bcc8e0aad37a1b3b70f67058c321a53bc165035720351abd4c335c7e`
- Implementation: `agent/epc-remediation-a0` final clean commit `f4c7e6e`

Adopt the deterministic receipt-to-monitor bridge and returned-artifact
manifest builder. Every bridge first revalidates the exact command receipts and
evidence bytes, then applies only the existing state-machine transitions with
immutable resource identity, receipt digests, monotone counters, timezone-aware
ordering, and all five frozen seeds. Partial/bootstrap-failed, stopped, and
hard-cap streams remain cleanup-required and cannot become adjudicated science.

Return closure requires the canonical monitor record, all five lifecycle
categories, safe regular payload files, exact byte counts/hashes, deterministic
`RETURN.json`/`SHA256SUMS`, and immediate verification by the existing lifecycle
attestor. Independent bridge, return-manifest, and hash-manifest records were
byte-identical. Their SHA-256 values are respectively
`3a25581102daaa6f859733aacac437d16808becd9315991ae72f7a60411c0619`,
`226ba2f40679024959f4ef4e94d8558ae179e0f5e989c460c79fc34513adc7c6`,
and `5e7cf19f6db6284063a698728bf13952b43451431c3367db674b8a392b49c3e2`.
Thirteen focused/prior-seam and 285 full-suite tests passed. This is synthetic
local packaging evidence only; no packaged command, provider, science input,
seed, CUDA query, GPU, or paid service ran.

## D-20260805-epc-c1-provider-free-command-receipts

- Date: `2026-08-05`
- Status: `adopted; exact commands packaged but provider/resource/science unrun`
- Evidence:
  `experiments/20260805T114131Z-epc-remediation-c1-command-receipts-replay/`,
  `experiments/20260805T114142Z-epc-remediation-c1-command-receipts-cmp/`,
  `experiments/20260805T114152Z-epc-remediation-c1-command-receipts-focused-clean/`,
  and
  `experiments/20260805T114204Z-epc-remediation-c1-command-receipts-full-suite/`
- Implementation: `agent/epc-remediation-a0` commits `30fc690`, `58363e5`

Adopt one deterministic command envelope bound to the exact frozen lifecycle,
orchestration, handoff, and bootstrap. Only the provider resource ID may be
resolved at execution time. The embedded future reference script preserves
the existing five-seed authority, certificate, data-provenance, and CUDA gates.
Its presence is inert and grants no execution authority.

Accept monitor receipts only in command order with immutable resource identity,
exact argv, terminal nonzero-exit handling, hash-attested stdout/stderr and
evidence files, monotone usage/cost counters, and frozen science/hard-cap
classifications. Two 10,240-byte builds were byte-identical; archive SHA-256 is
`e4457addf095f285e45e75aaf91c3cddead4b3960b40fbf3bd4543f5c1bb811d`
and embedded manifest SHA-256 is
`e8a938fc3b29ef9bbb99bc68d9d8a33e3bbf574b7f75492c94ee1c23604484fb`.
Nine focused/prior-seam and 281 full tests passed. This is local packaging and
synthetic parser evidence only; no command, provider, resource, science input,
CUDA query, GPU, or paid service ran.

## D-20260805-epc-c1-provider-free-orchestration

- Date: `2026-08-05`
- Status: `adopted; orchestration packaged but provider/resource/science unrun`
- Evidence:
  `experiments/20260805T105859Z-epc-remediation-c1-orchestration-focused-r2/`,
  `experiments/20260805T105948Z-epc-remediation-c1-orchestration-artifact/`,
  `experiments/20260805T110016Z-epc-remediation-c1-orchestration-cmp/`, and
  `experiments/20260805T110031Z-epc-remediation-c1-orchestration-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `ac15e78`

Adopt an inert launch/monitor state machine bound to the frozen lifecycle and
unopened five-seed reference launch. Transition order, resource identity,
monotone elapsed/GPU-hour/cost counters, the `$0.44` rate, 20-hour/`$10.50`
science stops, and 24-hour/`$12.00` hard caps fail closed. Returned C1-A
metrics are accepted for local adjudication only after exact artifact hashes
and the returned launch copy bind to the local freeze; both pass and preserved
`FAILED_REFERENCE_REPRODUCTION` outcomes still require cleanup.

Two fresh 10,240-byte packages replayed byte-identically. Bundle SHA-256 is
`ec71f90e88b0e1360429dfda36a5fb96ae874307069b3cfb86f2a0d9fa3c6a07`;
manifest SHA-256 is
`94748261d1dd5e47dc51e97dc648d3f398c5c6639ed7b5e1f36f2632c2230746`.
Twenty-two focused/regression and 277 full-suite tests passed. This is local
packaging and synthetic control evidence only; no provider, resource, runtime,
science input, seed, CUDA, GPU, or paid service was accessed.

## D-20260805-epc-c1-provider-free-lifecycle

- Date: `2026-08-05`
- Status: `adopted; lifecycle packaged but provider/resource/science unrun`
- Evidence:
  `experiments/20260805T102951Z-epc-remediation-c1-lifecycle-focused-clean/`,
  `experiments/20260805T103008Z-epc-remediation-c1-lifecycle-artifact-clean/`,
  `experiments/20260805T103330Z-epc-remediation-c1-lifecycle-replay-clean/`,
  `experiments/20260805T103343Z-epc-remediation-c1-lifecycle-cmp-clean/`, and
  `experiments/20260805T103022Z-epc-remediation-c1-lifecycle-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `a91218e`

Adopt an inert provider/job lifecycle contract bound to the exact authority
proposal, handoff, bootstrap, image, wheelhouse, and source commit. Freeze the
approved Runpod A40 rate/time/cost envelope and require local SHA-256 artifact
return verification before accepting a cleanup record. Cleanup succeeds only
for `terminated` resources, deleted disposable storage, zero remaining pods,
volumes, endpoints, and snapshots, and final observed cost no greater than
`$12.00`; corrupt returns, stopped/nonzero resources, and cost overruns fail
closed.

Two fresh 20,480-byte lifecycle archives replayed byte-identically. Bundle
SHA-256 is
`847382c38535f1086e6ebd47c85480378a6625e0aab24b492081d1d78a254f01`;
manifest SHA-256 is
`bee91aa3c2209b1a555e9c2f862e9fa9682099c413844e9ddc7ea6cc2764b607`.
Two focused and 274 clean full-suite tests passed. This decision verifies local
packaging and synthetic fail-closed controls only: no provider, resource,
runtime, artifact return, cleanup, or C1 science was observed.

## D-20260805-epc-c1-provider-free-bootstrap

- Date: `2026-08-05`
- Status: `adopted; bootstrap packaged but unexecuted; C1 science unrun`
- Evidence:
  `experiments/20260805T100610Z-epc-remediation-c1-bootstrap-artifact/`,
  `experiments/20260805T100639Z-epc-remediation-c1-bootstrap-replay/`,
  `experiments/20260805T100652Z-epc-remediation-c1-bootstrap-cmp/`, and
  `experiments/20260805T100712Z-epc-remediation-c1-bootstrap-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `21225bd`

Adopt a separate deterministic bootstrap package bound to the exact handoff,
handoff manifest, container digest, and wheelhouse manifest. Its future shell
path verifies both archive hash layers, performs only an offline `--no-deps`
install, and records Python/CUDA-build/Torch/direct-package versions without
calling `torch.cuda`; any script or handoff drift fails closed.

Two fresh 10,240-byte archives replayed byte-identically. Bundle SHA-256 is
`021d68fcdaa187ce90bef55d88c5f1d8392b1e1d3f600452f07de3c133179ed0`;
272 clean full-suite tests passed. This decision packages a future runtime
verification path only. It does not attest the container, install packages,
query a CUDA device, provision a resource, or authorize/execute C1 science.

## D-20260805-epc-c1-wheelhouse-bound-handoff

- Date: `2026-08-05`
- Status: `adopted; offline hand-off self-contained; runtime and C1 science unrun`
- Evidence:
  `experiments/20260805T094444Z-epc-remediation-c1-bound-handoff-focused/`,
  `experiments/20260805T094453Z-epc-remediation-c1-bound-handoff-c1-suite/`,
  `experiments/20260805T094723Z-epc-remediation-c1-bound-handoff-artifact/`,
  `experiments/20260805T094752Z-epc-remediation-c1-bound-handoff-replay/`,
  `experiments/20260805T094806Z-epc-remediation-c1-bound-handoff-cmp/`, and
  `experiments/20260805T094827Z-epc-remediation-c1-bound-handoff-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `11fd718`

Adopt hand-off schema v2, which embeds the exact 11-wheel direct-package
wheelhouse, its `SHA256SUMS`, and machine manifest alongside the previously
frozen source, reference, config, jobs, and MG certificates. Validate both the
outer archive and the inner wheelhouse semantically and byte-for-byte; reject
missing, extra, symlinked, hash-corrupt, activated, or environment-mismatched
package records.

Two fresh 46,264,320-byte bundles replayed byte-identically. Bundle SHA-256 is
`7951bb3e9cb5db736fcb390b37177f5196c8b8cab125f55487ecc50ed82fca9e`;
the bound wheelhouse manifest remains
`496fb73f6793792327b2faa1685da36fedf67b6232b932bba1581566eb38b5f1`.
Three focused, 21 C1/MG replay, and 271 full-suite tests passed. This admits an
offline transfer package only; it does not attest the base image/runtime or
authorize/execute C1 science.

## D-20260805-epc-c1-wheelhouse-runtime-verifier

- Date: `2026-08-05`
- Status: `adopted; direct wheels verified; remote runtime and C1 science unrun`
- Evidence:
  `experiments/20260805T092002Z-epc-remediation-c1-wheelhouse-download/`,
  `experiments/20260805T092051Z-epc-remediation-c1-wheelhouse-attestation/`,
  `experiments/20260805T092110Z-epc-remediation-c1-wheelhouse-replay/`,
  `experiments/20260805T092124Z-epc-remediation-c1-wheelhouse-cmp/`,
  `experiments/20260805T092136Z-epc-remediation-c1-wheelhouse-focused/`, and
  `experiments/20260805T092439Z-epc-remediation-c1-wheelhouse-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `017dbcf`

Adopt one exact direct-package wheel per frozen lock entry, downloaded for
CPython 3.11/manylinux x86-64 with binary-only `--no-deps`, and attest package
identity from wheel core metadata plus ordered SHA-256 hashes. Keep runtime
verification record-only: it compares a later captured container/runtime
record against the image digest, Python/CUDA/Torch versions, direct packages,
and wheelhouse digest without probing the current machine.

The 11 wheels total 43,559,835 bytes. Fresh manifests replayed byte-identically;
embedded SHA-256 is
`496fb73f6793792327b2faa1685da36fedf67b6232b932bba1581566eb38b5f1`.
Twenty-one focused and 271 clean full-suite tests passed. This does not attest
the pinned container's installed transitive closure or runtime and does not
execute C1-A. Bind the wheelhouse into the next clean offline hand-off; require
the actual runtime record before science.

## D-20260805-epc-c1-remote-handoff-preflight

- Date: `2026-08-05`
- Status: `adopted; provider-free hand-off verified; C1 science unrun`
- Evidence:
  `experiments/20260805T084839Z-epc-remediation-c1-remote-handoff-focused/`,
  `experiments/20260805T085134Z-epc-remediation-c1-remote-handoff-artifact/`,
  `experiments/20260805T085151Z-epc-remediation-c1-remote-handoff-replay/`,
  `experiments/20260805T085201Z-epc-remediation-c1-remote-handoff-cmp/`, and
  `experiments/20260805T085222Z-epc-remediation-c1-remote-handoff-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `aa62845`

Adopt a deterministic, inert remote hand-off that refuses dirty source,
attests the registry-resolved Runpod image digest, binds the exact direct lock,
archives only clean RelaLeap/official-reference commits plus the frozen C1
config, five unopened jobs, and MG-1/MG-3 certificates, and fails on missing,
unexpected, duplicated, reordered, or hash-corrupted members. Require a
SHA-256 wheelhouse, exact runtime/provider records, and explicit paid/GPU
activation permission before science; the hand-off itself never grants it.

Two fresh builds replayed byte-identically (bundle SHA-256
`35c6d73a7f67bc1cb6f7d5630a1bbcb39ba64be2a9da70e11bbc1a217fd8a84a`),
and 20 focused plus 270 clean full-suite tests passed. No dataset, seed, model,
CUDA query, GPU, pod, or paid resource was used. Materialize the exact
wheelhouse/runtime verifier next; this package is not C1-A reproduction
evidence.

## D-20260805-epc-c1-reference-seed-executor-package

- Date: `2026-08-05`
- Status: `adopted; provider-free seed executor verified; reference science unrun`
- Evidence:
  `experiments/20260805T082816Z-epc-remediation-c1-seed-executor-focused-r2/`,
  `experiments/20260805T082831Z-epc-remediation-c1-seed-executor-plan-r2/`,
  `experiments/20260805T082844Z-epc-remediation-c1-seed-executor-plan-replay/`,
  `experiments/20260805T082857Z-epc-remediation-c1-seed-executor-plan-cmp/`,
  and
  `experiments/20260805T082940Z-epc-remediation-c1-seed-executor-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `96b9741`

Adopt a lazy-import seed executor that refuses execution without an explicit
science-authority flag, exact fresh-process job replays, hash- and
content-attested MG-1/MG-3 certificates, the official `../data` root, exact
EMNIST-MNIST byte/split provenance, and CUDA. Hash compressed GZip members,
decoded IDX streams, and IDX payloads; require exact 60,000/10,000 shapes,
ten-class labels, and canonical hashes for all ascending split indices.

Synthetic/corruption controls passed, two fresh-process plans were
byte-identical (SHA-256 `4c527686...4501d53`), and 268 clean full-suite tests
passed. No dataset, official seed, CUDA device, GPU, pod, or paid resource was
opened. This is executable packaging, not C1-A reproduction evidence.

## D-20260805-epc-c1-reference-launch-adjudication

- Date: `2026-08-05`
- Status: `adopted; provider-free C1-A seam verified; reference science unrun`
- Evidence:
  `experiments/20260805T080410Z-epc-remediation-c1-reference-gate-focused/`,
  `experiments/20260805T080443Z-epc-remediation-c1-reference-launch-artifact-r2/`,
  `experiments/20260805T080456Z-epc-remediation-c1-reference-launch-replay/`,
  and
  `experiments/20260805T080759Z-epc-remediation-c1-reference-gate-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `5d47837`

Bind each of the five official C1-A seeds to an immutable source/config/
dataset-contract/MG-certificate input manifest before execution. Require two
fresh-process manifest digests per returned seed record, exactly one result
for each seed, finite percentage-scaled accuracy, valid MG-1/MG-3 certificates,
and a dataset-manifest digest. Apply the frozen five-seed mean interval and
sample-standard-deviation threshold without repair. A statistical miss is
preserved as `FAILED_REFERENCE_REPRODUCTION` and does not admit transformer
execution.

The provider-free controls and two fresh plan processes passed; serialized
plans were byte-identical and the clean suite passed 266 tests. This does not
constitute the official reproduction: no EMNIST bytes or reference seed were
opened and no GPU or paid resource was used. Package the gated seed executor
and dataset-byte/split manifest next, but do not execute it while an activation
prohibits GPU/paid use.

## D-20260805-epc-c1-provider-free-execution-package

- Date: `2026-08-05`
- Status: `adopted; provider-free packaging verified; C1 science unrun`
- Evidence:
  `experiments/20260805T074256Z-epc-remediation-c1-execution-dryrun-focused/`,
  `experiments/20260805T074435Z-epc-remediation-c1-execution-dryrun-artifact/`,
  and
  `experiments/20260805T074550Z-epc-remediation-c1-execution-dryrun-full-suite/`
- Implementation: `agent/epc-remediation-a0` commit `e8421ac`

Use one exact fail-closed JSON contract as the hand-off boundary for C1-A and
transformer execution. Any changed reference, model/corpus revision,
partition, metric, rung, optimizer, replay, or artifact value is a new contract
and may not pass this validator. The provider-free orchestrator may attest the
official source and emit phase/rung/stop plans, but it must explicitly record
no science execution, seed opening, model/data loading, GPU, or paid resource.

The dry-run manifest and focused/full regressions passed. This verifies only
packaging and prerequisite ordering; it does not reproduce the official result
or establish transformer identity, settlement, conditioning, quality,
departure, or an admissible lambda window. Implement C1-A execution and
adjudication next, but do not exercise it while the activation prohibits GPU
and paid-resource use.

## D-20260805-epc-c1-provider-free-graph-preflight

- Date: `2026-08-05`
- Status: `adopted; provider-free implementation unit verified; C1 science unrun`
- Evidence:
  `experiments/20260805T070453Z-epc-remediation-c1-reference-preflight-r2/`,
  `experiments/20260805T070503Z-epc-remediation-c1-provider-free-focused/`, and
  `experiments/20260805T070528Z-epc-remediation-c1-provider-free-full-suite/`,
  `experiments/20260805T071429Z-epc-remediation-c1-data-metric-focused/`, and
  `experiments/20260805T071606Z-epc-remediation-c1-data-metric-full-suite/`
- Implementation: `agent/epc-remediation-a0` commits `7142612`, `9bab1c9`

Use the exact pinned official checkout through a hash- and commit-attested
wrapper; do not copy or silently rewrite its PCE implementation. Use the new
shared FabricPC graph for C1 feedforward/rung-0 and EO reconstruction: each of
the 12 blocks contributes distinct attention and MLP residual edges, all
explicit errors follow that immutable order, and the tied embedding/head
storage and per-edge precision inputs fail closed. Construct the four token
partitions deterministically in source order, reject coordinate or exact-block
overlap, and fit every edge covariance in float64 with the frozen floor and
mean-one precision normalization.

The provider-free controls passed: six official source hashes matched, a real
Hugging Face GPT-2 fixture matched the zero-error graph byte-exactly, earliest
errors received output signal, and the partition/metric controls plus MG-7/
MG-8 replay passed. The final clean suite passed 262 tests. This
does not reproduce the published MNIST result or establish transformer
settlement, conditioning, quality, departure, or an admissible lambda window.
No C1 seed, model/data partition, GPU, pod, or paid resource was opened.

## D-20260805-epc-c1-homotopy-freeze

- Date: `2026-08-05`
- Status: `adopted; C1 frozen; BLOCKED_AUTHORITY for science execution`
- Evidence: `experiments/20260805T063722Z-epc-remediation-c1-spec-freeze/`
- Specification: `agent/epc-remediation-a0` commit `f8cfed4`, SHA-256
  `b5461260b9d27bb4354205707d83b8010b2bf20503fdceb216e6af596cb26891`
- Resource proposal: `docs/epc-c1-runpod-authority-proposal-20260805.md`,
  SHA-256
  `e743a8c4a54678dc66b11d8d1dca4fe260864394879401847321643cba4f9cb8`

Freeze C1 without opening seeds `820260819--820260821`. The official
five-seed MNIST ePC reproduction is a hard prerequisite to transformer
integration. The conversion then uses pinned GPT-2-small and WikiText-2
revisions, a single shared FabricPC graph with separate attention/MLP edges,
frozen diagonal precisions, exact rung-0 identity, ten fixed lambda rungs, and
predeclared settlement, conditioning, quality, departure, replay, and stop
rules. An empty admissible lambda window is a valid negative result.

Diagnosis CT-3 explicitly forbids laptop-CPU C1 science runs. The proposed
resource is one Runpod Secure Cloud A40 for expected 12 GPU-hours (`$5.28`)
with a 24-hour / `$12.00` hard cap and mandatory termination after verified
artifact return. No resource has been provisioned. Continue only provider-free
implementation and dry-run validation until Ben explicitly approves this exact
resource bound; C2 and C3 remain closed.

## D-20260805-epc-m0-deep-linear-adjudication

- Date: `2026-08-05`
- Status: `adopted; M0-R COMPLETE_VERIFIED; C1 specification admissible`
- Evidence: `experiments/20260805T062130Z-epc-remediation-m0-acceptance/`,
  `experiments/20260805T062537Z-epc-remediation-m0-focused-clean/`, and
  `experiments/20260805T062749Z-epc-remediation-m0-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `81ad6cd`

Accept the theorem-consistent M0-R result on its complete frozen float64 grid.
All 40 unique corrected EO points passed exact equilibrium, numerical/exact
local-gradient, convergence, fixed-point conditioning, and sign-aligned
adjoint-cosine controls. Both theorem decades passed at every layer with
median ratios `9.7205--9.9988` and minimum ratio `9.6811`; JSON, CSV, and both
SVG profiles replayed bit-exactly. Focused regressions passed 31 tests and the
complete suite passed 255 from the clean implementation commit.

Preserve the diagnosis finite-lambda equality claim as `FAILED_TEST`: its
maximum-layer BP differences span `0.002193--0.932356`, consistent with the
MG-2 counterexample rather than an EO fixed-point defect. Twelve legacy SO/sPC
points settled and matched the exact PC control; twelve remain explicit
partial settlements and support no equivalence claim. M0-R establishes only
the frozen deep-linear implementation/theorem identity. Freeze C1 separately;
do not infer transformer conversion, published-result reproduction, nonlinear
function preservation, or cap readiness.

## D-20260805-epc-mg8-determinism

- Date: `2026-08-05`
- Status: `adopted; MG-8 COMPLETE_VERIFIED; M0-R specification admitted`
- Evidence: `experiments/20260805T053817Z-epc-remediation-mg8-acceptance-r2/`,
  `experiments/20260805T053956Z-epc-remediation-mg8-focused-clean/`, and
  `experiments/20260805T054206Z-epc-remediation-mg8-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `27c5105`

Accept MG-8 on the recorded local CPU environment. Fresh subprocess runs under
`PYTHONHASHSEED=0` and `1` emitted byte-identical and SHA-256-identical
artifacts for MG-1, MG-2R, and MG-3--MG-7; every embedded spec digest matched
the frozen manifest. The byte-flip, missing artifact, false replay flag,
provenance mutation, duplicate manifest, and nonfinite JSON controls all failed
closed. Focused A0/MG tests passed 42 and the complete suite passed 252.
Artifact SHA-256:
`6d3f86d8fe369633aed5d6124c4a56b447609c38662acb85b66b5b6374bd8057`.

This establishes deterministic provenance-bound evidence production locally,
not cross-architecture identity or correctness of a repeated value. Preserve
MG-2 as `FAILED_TEST`. M0-R may proceed under its independently frozen
theorem-consistent adjudication contract at commit `5813c75`.

## D-20260805-epc-mg7-metric-neutrality

- Date: `2026-08-05`
- Status: `adopted; MG-7 COMPLETE_VERIFIED; MG-8 specification admitted`
- Evidence: `experiments/20260805T052237Z-epc-remediation-mg7-acceptance/`
- Implementation: `agent/epc-remediation-a0` commit `38f8efc`

Accept the frozen block-level diagonal inverse-variance metric certificate.
The exact perturb split contains disjoint complete 32-row fit and held-out
halves. On the held-out half, share-to-uniform ratios are
`1.0024781426298592` and `0.9975218573701409`; all six controls pass,
including the named raw late-block-domination regression (`256.0`). Artifact
replay is bit-exact; 34 focused and 249 complete-suite tests pass. Artifact
SHA-256: `3d3d3a908aa6e0fb3989c630a26f0966f87ae3f85d7e093e2dfe5b3888c4c555`.

This validates only the declared two-block local quadratic metric. It does not
certify a future attention/MLP graph, settlement, EO/BP equivalence,
learnability, or cap readiness. Freeze MG-8 independently before execution.

## D-20260804-epc-mg6-eval-train-correspondence

- Date: `2026-08-04`
- Status: `adopted; MG-6 COMPLETE_VERIFIED; MG-7 specification admitted`
- Evidence: `experiments/20260805T050415Z-epc-remediation-mg6-acceptance/`
  and `experiments/20260805T050443Z-epc-remediation-mg6-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `3f0d17e`

Accept MG-6. The immutable certificate uses the normative `_nll`, frozen
`1.4/2=0.7` threshold, exhaustive 64-row fixture, explicit pre/adapted oracle
models, retention view, and exact MG-5-certified trainer tensors. Explicit
oracle NLL was at most `2.3783352260358675e-09`; both trainer round trips were
`0.0`; uniform logits matched `ln(64)` exactly. The mismatch, wrong-position,
nonfinite, incomplete-batch, and historical reduction controls all failed
closed, replay was bit-exact, and the complete suite passed 247 tests.

Artifact SHA-256:
`2fc3641810f66c5b383e9a1e871642887947cff018e81c6efa9fa7574425d885`.
This establishes evaluator--teacher correspondence only, not learnability,
metric neutrality, or cap readiness. MG-7 may now be frozen independently.

## D-20260804-epc-mg5-teacher-write-integrity

- Date: `2026-08-04`
- Status: `adopted; MG-5 COMPLETE_VERIFIED; MG-6 specification admitted`
- Evidence: `experiments/20260805T035047Z-epc-remediation-mg5-acceptance/`
  and `experiments/20260805T035158Z-epc-remediation-mg5-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `5b9d272`

Accept the immutable teacher-write certificate and shared trainer-consumer
seam. Across both adaptation states, all 512 exhaustive scored positions have
exactly one planted winning candidate, the correct unique target sequence, and
finite strict margins. Minimum candidate-winning and within-candidate token
margins are `11.670098155736923` and `24`. The exact consumed tensor matches
the producer digest and object/storage identity attestations.

The historical advanced-indexing no-op, tied loser, wrong token, swapped
winner, and nonfinite loser all fail closed; ordinary KD and marginal targets
carry explicit non-applicable labels. Replay is bit-exact, the 12 focused and
historical regressions pass, and the complete suite passes 243 tests. Artifact
SHA-256: `19453717755a362df56acdb6db323e11d43b0b3d4f2e2af8f0f3d1ea147898ad`.

This certifies teacher construction and delivery only, not learnability or
evaluation correspondence. Freeze MG-6 independently before implementation.

## D-20260804-epc-mg4-fixed-point-conditioning

- Date: `2026-08-04`
- Status: `adopted; MG-4 COMPLETE_VERIFIED; MG-5 specification admitted`
- Evidence: `experiments/20260805T032454Z-epc-remediation-mg4-acceptance-r2/`
  and `experiments/20260805T032800Z-epc-remediation-mg4-full-suite-clean-r2/`
- Implementation: `agent/epc-remediation-a0` commit `9306d01`

Accept the immutable actual-variable conditioning certificate and frozen
20-iteration matrix-free HVP/power estimator. Exact stable, marginal,
unstable, flat, and equal-magnitude-mode controls match materialized Jacobians;
missing MG-3 evidence, partial settlement, nonfinite HVP, zero product, and
selected zero step all fail closed. All six core engines and 11 enumerated
downstream consumers propagate the complete certificate.

All 12 frozen MG-2R EO points retain residual `5.53e-9`--`8.14e-9`, replay
bit-exactly, and have finite stabilized `stable-conditioned` radius estimates
`0.4995`--`0.4999963102685592`. The focused 25-test gate and complete 238-test
suite passed from the clean commit. Artifact SHA-256:
`618eaecbf8e82fccf73d23dc9ef94464d3bb5c650aed460977c286cd02e978a1`.

This decision certifies only local stability of the declared discrete maps at
tested fixed points. It does not establish global convergence, basin size,
transformer efficacy, legacy-state EO identity, metric neutrality, or cap
readiness. Freeze MG-5 independently before implementation.

## D-20260804-epc-mg3-convergence-certificate

- Date: `2026-08-04`
- Status: `adopted; MG-3 COMPLETE_VERIFIED; MG-4 specification admitted`
- Evidence: `experiments/20260805T023815Z-epc-remediation-mg3-acceptance/`
  and `experiments/20260805T023930Z-epc-remediation-mg3-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `030b679`

Accept the shared immutable active-variable residual certificate for MG-3.
The seed-free scalar regression has strictly decreasing energy but residual
`0.903687890625` after four updates and is correctly labeled partial. Direct
inclusive boundary, adjacent-float, degenerate-initial, nonfinite-final, and
feedforward endpoint controls pass. MLP state inference, transformer state
inference, GPT-2 state inference, `pc_step`, and MG-2/MG-2R error/state records
now propagate the same certificate. Eleven current downstream result builders
were enumerated and none can serialize or promote only energy monotonicity.
All 12 frozen MG-2R EO points retained residual at most `8.14e-9`, classify
settled, and enter the separate `1e-4` census. Artifact replay was bit-exact;
55 focused tests and the complete 233-test suite passed from the clean commit.

This decision validates convergence labeling, not fixed-point stability or
conditioning, EO identity for legacy state paths, metric neutrality, or
training efficacy. Freeze MG-4 independently before implementation.

## D-20260804-epc-mg2r-theorem-consistent-equivalence

- Date: `2026-08-04`
- Status: `adopted; MG-2R COMPLETE_VERIFIED; MG-3 specification admitted`
- Evidence: `experiments/20260805T015749Z-epc-remediation-mg2r-acceptance/`
  and `experiments/20260805T015835Z-epc-remediation-mg2r-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `aea2263`

Accept MG-2R as the bounded theorem-consistent replacement gate while retaining
the predecessor MG-2 result as `FAILED_TEST`. On fresh seed `820260813`, every
depth 2/6/12/24 and output weight `1e-3/1e-4/1e-5` EO point reached
`rho<=1e-8`; numerical errors and local PC gradients matched independently
solved exact controls within `8.14e-9`. Every layer's exact rescaled PC gradient
approached feedforward BP monotonically. Adjacent-decade median ratios were
`9.72--10.00`, with minimum individual ratio `9.68`, satisfying the frozen
first-order rate gate. Replay was bit-exact. The clean full suite passed 217
tests.

This validates exact finite-lambda PC settlement and its declared BP limit on
the linear fixtures. It does not establish finite-lambda PC/BP equality,
nonlinear or transformer correctness, conditioning, or training efficacy.
MG-3 may now be frozen independently; do not alter or reinterpret the MG-2
failure.

## D-20260804-epc-mg2-finite-lambda-contract-failed

- Date: `2026-08-04`
- Status: `MG-2 FAILED_TEST; MG-3 closed; bounded repair required`
- Evidence: `experiments/20260805T010748Z-epc-remediation-mg2-acceptance/`
  and `experiments/20260805T010832Z-epc-remediation-mg2-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `beb3fe0`

Preserve the frozen MG-2 result as a genuine failed gate. EO/ePC reached
`rho<1e-8` at every depth in 26--27 iterations, agreed with the independent
closed-form convex error equilibrium to about `1e-8`, and replayed bit-exactly.
Nevertheless, maximum per-layer rescaled fixed-point PC versus feedforward-BP
gradient errors grew from `0.0024427` at depth 2 to `0.0569152` at depth 24,
far above `1e-6`. The legacy path, when independently converged at depths 2/6,
reproduced the same non-BP profile.

Classify this as a contract/theorem mismatch rather than an EO implementation
failure. A seed-free scalar depth-2 unit chain analytically exceeds `1e-6` at
`lambda=1e-3`, and the primary paper's Appendix C.4 explicitly states that
finite-nudging PC gradients are generally distinct from BP. Do not weaken,
reinterpret, or tune the failed gate. MG-3 remains inadmissible. The only
admissible continuation is a separately frozen repair that compares numerical
EO against the exact analytic PC fixed point and tests the predeclared
lambda-to-zero approach toward BP; the opened MG-2 seed may not set its gates.

## D-20260804-epc-mg1-parameterization-identity

- Date: `2026-08-04`
- Status: `adopted; MG-1 COMPLETE_VERIFIED`
- Evidence: `experiments/20260805T004536Z-epc-remediation-mg1-acceptance/`,
  `experiments/20260805T004556Z-epc-remediation-mg1-artifact-acceptance/`, and
  `experiments/20260805T004613Z-epc-remediation-mg1-full-suite-clean/`
- Implementation: `agent/epc-remediation-a0` commit `d20e8c8`

Accept the bounded pinned-reference port for MG-1. Across float64 orthogonal
linear chains of depths 2/6/12/24, every first-step explicit-error SGD update
matched `-0.01` times its output-loss reverse-mode adjoint with measured
relative error zero. Every earliest hidden error received norm greater than 8,
and deterministic replay was bit-exact. The named legacy SO/sPC control moved
only its final hidden state on the first simultaneous step, reproducing the
expected wavefront limitation. The focused gate passed from a clean commit and
the complete suite passed 213 tests.

This decision establishes parameterization identity and immediate deep error
signal only. It does not establish convergence, equilibrium/BP equivalence,
fixed-point conditioning, transformer correctness, or training efficacy.
Freeze MG-2 separately before implementation.

## D-20260804-epc-a0-method-and-instrument-audit

- Date: `2026-08-04`
- Status: `adopted; A0 COMPLETE_VERIFIED`
- Evidence: `experiments/20260805T002848Z-epc-remediation-a0-acceptance-r2/`
- Implementation: `agent/epc-remediation-a0` commit `6bf9d01`

Pinned arXiv v5 and official reference code show that EO/ePC optimizes
independent error variables through a global recursive graph. RelaLeap instead
optimizes detached hidden states, so its legacy path is SO/sPC and its prior
finite-step outcomes must not be described as tests of the cited EO/ePC method.
The audit independently found that r5 selected the worst candidate because it
applied `min` before negating log-probability. Retain prior r5 as historical
instrument-failure evidence; do not reinterpret its arm comparisons.

The bounded repair now selects minimum NLL after tokenwise negation and passes
uniform `ln(64)`, untrained, planted-oracle, actual trainer-teacher round-trip,
teacher-argmax, and perturbation-independence controls. Proceed to MG-1--MG-8;
the external diagnosis thresholds remain prospective contracts until each gate
is frozen and tested.

## D-20260803-epc-diverse-frontier-negative: Do not build an MoE from the tested frontier

- Date: `2026-08-03`
- Status: `adopted; bounded negative result`
- Evidence: `experiments/20260804T055941Z-epc-diverse-pareto-frontier-v1/`
  and `experiments/20260804T060519Z-epc-diverse-pareto-frontier-v2/`
- Implementation: `agent/epc-diverse-pareto-frontier` commits `dd30b2d`,
  `5c956d0`

Ben proposed first checking whether the ePC Pareto frontier contains
"diversely good" models that could later serve as MoE experts. A 14-cell local
screen varied six controls. After an aggregate-frontier pilot exposed that
conditional specialists could be pruned, v2 retained each context-by-mode NLL
as a Pareto objective and used fresh exploration, selection, and confirmation
seeds. V2 retained two candidates in exploration, one in selection, and none
at the confirmation viability gate. All 62 v1/v2 records were deterministic
and energy-monotone, so the failure is behavioral rather than numerical.

Do not construct an MoE from this tested candidate pool. The observed
conditional variation is seed-sensitive and does not constitute stable expert
specialization. A successor must introduce a materially broader
mechanism/task-regime hypothesis, new unopened splits, and the same explicit
conditional-complementarity gate. This does not refute ePC generally.

## D-20260802-frame-oracle-v4-gate-frozen-unopened

- Date: `2026-08-02`
- Status: `contract frozen; scientific gate unopened`
- Evidence:
  `experiments/20260803T051233Z-frame-oracle-v4-sealed-contract-r2/`
- Contract: `docs/frame_oracle_v4_sealed_gate_contract_20260802.md`

Do not tune v3 against `test_dracula`, `test_window`, or any other exposed
battery. Source inspection independently shows that v3 derives polarity from
whole-sentence lexical cues and overwrites every non-unknown modality with
`asserted`; these are contract gaps, not permission to reopen old cases.
Freeze a v4 implementation, prompt/schema/model hashes, and paired command
before consuming the new 24-case gate. Until it passes 24/24 exact and paired
deterministic across every stratum, do not label, train a frame readout, or
integrate a semantic loss.

## D-20260801-offline-frame-labels-v1-failed-closed

- Date: `2026-08-01`
- Status: `do not train frame readout or semantic loss`
- Evidence: `experiments/20260801T161016Z-frame-oracle-offline-readout-v1/`

The normalized Qwen v3 oracle achieved 22/24 exact semantic labels on a
disjoint 12/12 train/test corpus, but failed its sealed-label conjunction on
`test_dracula` and `test_window`. Preserve raw proposals and normalized labels
as failure evidence. Do not train the frozen GPT-2 residual-to-frame readout
or use this channel in ePC/XM. A successor must be a versioned oracle/corpus
repair with fresh sealed cases.

## D-20260801-balanced-exploration-structural-pass-epc-gate-failed

- Date: `2026-08-01`
- Status: `admit balanced T=1 mechanism; do not admit current ePC T=4 config`
- Evidence: `experiments/20260801T154000Z-tiny-transformer-explorative-epc/`
  and `experiments/20260801T160000Z-tiny-transformer-balanced-exploration-v2/`

Pure WTA exploration improves transformer continuation coverage but does not
reliably preserve every mode conditionally. Equal-capacity WTA within context
repairs the structural failure on all fresh seeds without semantic labels.
Balanced T=1 passed the frozen coverage threshold on all seeds; balanced ePC
T=4 missed on one seed. Continue with balanced assignment as the semantic-free
baseline, while treating ePC settlement depth/optimization as unresolved.

## D-20260801-normalized-frame-oracle-v3-admitted-bounded

- Date: `2026-08-01`
- Status: `admit bounded offline-label stage only`
- Evidence: `experiments/20260801T154800Z-frame-oracle-v3/`

Use `qwen2.5:7b` only as a closed frame proposal generator; deterministic code
owns slot casing, explicit-negation polarity, state-value normalization, and
abstention canonicalization. V3 passed 8/8 valid, deterministic, exact frames
on a fresh battery. This does not establish unrestricted open-text reliability
or license direct integration into XM/ePC; the next gate is a larger frozen
offline label audit followed by held-out readout distillation.

## D-20260801-qwen-frame-oracle-v1-failed-closed

- Date: `2026-08-01`
- Status: `do not label or distill`
- Evidence: `experiments/20260801T145700Z-frame-oracle-schema-audit/`

Do not use the v1 `qwen2.5:7b` free-role frame extractor for offline corpus
labels or residual-to-frame distillation. Although all responses were valid
JSON, only 2/8 matched canonical known-answer frames and one paired response
was nondeterministic. A successor needs a closed predicate/role ontology or
separate normalization/validation stage and must use a fresh held-out battery.

## D-20260801-semantic-free-exploration-positive-control-passed

- Date: `2026-08-01`
- Status: `admit to transformer-language preflight only`
- Evidence: `experiments/20260801T151100Z-explorative-epc-baseline/`
- Implementation: `agent/explorative-epc-baseline` commit `ff4ec23`

Winner-assigned two-continuation training is a functioning semantic-free
exploration mechanism on the planted bimodal fixture, both at the ordinary
T=1 endpoint and with four-step ePC activity settlement. It recovered both
coherent modes on every seed while marginal controls learned the invalid mean.
This admits a separately specified language-scale preflight, not an ePC
advantage or language claim: T=1 and T=4 results were nearly identical.

Do not use assignment entropy alone as evidence of mode coverage. The marginal
controls had nearly two effective assignment modes despite negligible head
diversity and roughly unit prototype-coverage error. Future experiments must
report candidate diversity plus planted or independently judged continuation
coverage.

## D-20260801-gpt2-only-substitution-adapter-failed-closed

- Date: `2026-08-01`
- Status: `do not integrate`
- Evidence: `experiments/20260801T143000Z-gpt2-semantic-substitution-adapter/`

Do not insert the frozen GPT-2 hidden-state plus one-step predictive-agreement
adapter into an ePC/XM semantic-weakness loss. On its fixed natural-language
probe, every aggregate variant separated identity/paraphrase/unrelated but
scored the factual contradiction higher than the unrelated completion. This
shows the current teacher-only logit-divergence guard is not a sufficient
contradiction relation. A successor must introduce an independently frozen
semantic/NLI relation or a separately prespecified multi-step substitution
criterion and pass a fresh held-out calibration gate.

## D-20260728-v4-functional-result-accepted-for-v4-1

- Date: `2026-07-28`
- Status: `accepted for V4-1 substrate intake only`
- Decision owner: Benjamin Goertzel
- Evidence: `experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`
- Execution contract: `docs/v4-1_asset_intake_contract_20260728.md`

Ben explicitly accepts the nonlinear paired-rollout result as sufficient to
advance. The evidence is strong for the narrow operational claim that
`approximate_full_state_AD` predicts local paired `torch.optim.Adam` responses
on the tested nonlinear fixtures and is materially better than frozen-D under
high-LR stress.

The original V4-0 preregistration remains accurately recorded as
**inconclusive**: B2 and high-LR B1 missed the 5-sigma fixture-admission
precheck. This decision is an authorized progression choice, not a post-hoc
claim that that preregistered criterion passed. It opens V4-1 asset intake and
the `T=1` adapter-validation work only. It does not admit exact-D, JAX
reproduction, transformer or policy efficacy, V4-2, V4-3, or paid compute.

## D-20260727-commutator-critic-v4-preliminary

- Date: `2026-07-27`
- Status: `revision required before integration`
- Evidence:
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/`
- Source: `../../library/commutator-critic-v1-1/`

The V4 pivot is better identified than V1--V3: it measures the local
gradient/curvature/optimizer-state response and learns only a residual, while
recomputing positive-control truth per state and treating late-trajectory
signal loss explicitly. The supplied quadratic sandbox reproduced
byte-for-byte, so these fixture-level mechanisms merit continued local work.

Do not integrate or execute C2/policy stages yet. JAX-dependent nonlinear
claims remain unreproduced, and the supplied PyTorch backend failed all four of
its own bit-exact optimizer-replica admission tests on the target host. First
repair or explicitly version the functional optimizer equivalence, then
reproduce exact-D in an isolated reviewed JAX environment, then implement only
the minimal C0/C1 slice on a fresh branch. HDC footprints may propose sparse
pair edges, but measured commutator/cross-curvature terms must determine their
causal weights.

## D-20260728-v4-empirical-torch-admission

- Date: `2026-07-28`
- Status: `accepted for local validation`
- Decision owner: Benjamin Goertzel
- Evidence: `docs/causal_critic_v4_c4prime_execution_plan_20260727.md` V4-0

### Decision

Treat the failed Torch bit-exact functional-optimizer replicas as a
conformance diagnostic, not the primary scientific blocker. Admit a clearly
labeled `approximate_full_state_AD` backend only if it predicts direct paired
CRN counterfactual rollouts of the actual `torch.optim` nonlinear learner under
the frozen V4-0 empirical gate. It must beat or match frozen-D as specified.

### Consequences

A pass establishes local empirical usefulness of a full-state tangent on the
planted nonlinear fixture, not exact-D implementation equivalence, JAX
reproduction, transformer validity, C2 validity, routing-policy value, or C4′
readiness. A failure remains scientifically informative and blocks downstream
work.

## D-20260726-colearned-critic-v3-fixture-audit-failed

- Date: `2026-07-26`
- Status: `fail-closed before calibration/confirmation`
- Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T184000Z-colearned-causal-critic-v3-preconfirmation-audit/`
- Implementation: `agent/colearned-causal-critic-v1` commit `5eb57db`

The v3 trajectory audit retained the intended family ordering through 75% of
its 100-update trajectory, but every family violated it at the final
checkpoint. The null/harmful positive-utility proportion was 0%, satisfying
its one-class check, yet its intervention ordering also failed. Per the frozen
protocol, stop before calibration or confirmation; do not tune fixture
coefficients, re-anchoring, or thresholds against this audit. Any successor
requires a new protocol version, fresh audit seeds, and fresh confirmation
seeds.

## D-20260726-colearned-critic-v2-preregistered

- Date: `2026-07-26`
- Status: `accepted for local confirmation`
- Implementation branch: `agent/colearned-causal-critic-v1`
- Protocol: `docs/colearned_global_causal_critic_protocol_v2.md`

Replace the analytic response formula with a trainable planted modular learner
before another critic confirmation. Preserve randomized common-RNG paired
identification, logged propensities, replay boundaries, coverage gates, and
critic/learner gradient separation.

Use a two-part beneficial-sign/conditional-amount ensemble as the primary
uncertainty model, optionally isotonic-calibrated on calibration seeds only.
Apply AUROC only to two-class families and use false-beneficial rate for the
one-class null. Require critic MSE below constant and support-only baselines;
report local-linear but require dominance only on explicitly nonlinear
fixtures. Freeze confirmation choices before execution.

Observed v1 failures motivate these changes but do not constitute v2 evidence.
The implemented planted-fixture infrastructure passed the full local suite
(`459 passed, 1 skipped`); critic-v2 confirmation remains unrun.

## D-20260725-colearned-critic-phase0-failed: Block policy interpretation

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T063000Z-colearned-causal-critic-phase0/`
- Implementation branch: `agent/colearned-causal-critic-v1`

The global critic Phase-0 estimation conjunction failed on untouched analytic
confirmation seeds. Preserve the positive ordering, coverage, synergy
pair-error, and null false-benefit results, but do not interpret policy-arm
summaries or run Shakespeare. ECE failed in all four families; synergy sign
AUROC failed; and exact linear baselines correctly dominated the neural critic
in local/null. The null fixture contains no beneficial class, so its AUROC gate
is not identified, while the analytic fixture cannot emit the credit-wavefront
or entropy-rank policy diagnostics.

Any retry must be a versioned protocol repair with newly frozen confirmation
seeds. Prespecify a one-class null metric, nontrivial baseline fixtures,
calibration-only probability calibration, and a trainable planted learner for
trajectory-level policy and representation gates. Do not revise v1 thresholds
against the observed confirmation set.

## D-20260726-online-support-v3-confirmed-no-shakespeare-promotion

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T025745Z-online-causal-epc-v3/`
- Implementation: `agent/online-causal-epc-v3` commit `b490f52`

Use sign-insensitive squared Hutchinson overlap to gate nonzero curvature
interaction, retain signed trace only as cooperative/antagonistic
classification, and use the direct module-local vector
`H_B g_A - H_A g_B` for the theorem-relevant commutator condition. Judge
ablation load-bearing on each module's own task; report cross-task effects as
facilitative/suppressive without the old `.05` bound.

All revised planted gates passed on untouched seeds, confirming that v2's
failures were gate-specification errors. The contingent Shakespeare run failed
its separate promotion gate because full-causal forgetting and finite-update
commutator were worse than ordinary ePC. Do not scale or use paid compute.

## D-20260726-online-support-v2-failed: Stop before Shakespeare

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T023651Z-online-causal-epc-v2/`
- Implementation branch: `agent/online-causal-epc-v2`

The overlapping-vocabulary 90/10 teacher fixture repaired the exact-zero
interaction defect and made the dominant pathways reliably load-bearing.
Nevertheless, Phase 0 failed: signed `tr(H_A H_B)` was negative for some
modules/seeds, so the positive-baseline and shrinkage gates failed, and the
minority block's Task-A ablation effect exceeded the .05-nat cross-effect
limit. Do not run Shakespeare. Any third fixture must use untouched
confirmation seeds and justify whether signed curvature overlap or a
sign-insensitive quantity is the theorem-relevant diagnostic.

## D-20260726-online-support-phase0-failed: Repair planted fixture

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T080000Z-online-causal-epc/`
- Implementation: `agent/online-causal-epc` commit `83abac8`

Do not run the Shakespeare phase. The estimator recovered architectural routing
(AUC 1.0) and gates acted correctly, but exact disjoint routing made the
protected mixed-Hessian baseline zero, precluding strict shrinkage. More
importantly, signed block-zero ablations were not reliably harmful on their own
tasks. A replacement positive control must jointly guarantee trained
load-bearing pathways and nonzero controlled cross-task curvature.

## D-20260726-causal-coding-epc-negative: Require planted support validation

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence:
  `experiments/20260726T003000Z-causal-coding-epc-5arm/`
- Implementation: `agent/cmcp-epc-kd-bridge` commit `4b0a425`

### Decision

Do not promote or scale the five-arm causal-coding ePC configuration. Before
another Tiny Shakespeare causal-routing run, construct a planted modular task
with known architectural `S_A/S_B`, validate support recovery and gate action,
and require the oracle-support arm to demonstrate a functional
retention/plasticity benefit.

### Evidence and rationale

The preregistered local CPU run completed all 15 records. The full causal stack
passed Task-B tolerance, finite-commutator reduction, rank, and credit-wavefront
checks, but worsened mean Task-A forgetting (4.9536 versus 4.8678) and did not
reduce pre-gate off-support leakage (.8572 versus .8551). Estimated supports
were seed-unstable and contained no A-only module in one seed. The true-label
intervention oracle reduced leakage and commutator but worsened forgetting, so
the fixture did not provide the intended positive control.

This does not reject the causal-continuous-learning theorem. It rejects the
claim that the current estimator, two-block fixture, and frozen regularizers
realize its useful modularity conditions.

## D-20260725-cmcp-epc-cl-negative: Do not promote CMCP-ePC to GPT-2

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence: experiment
  `20260725T231807Z-cmcp-epc-cl-phase1`

### Decision

Do not start the contingent GPT-2 CMCP-ePC experiment. In the frozen local
gate, CMCP-ePC failed to beat CMCP-KD on any functional continual-learning
endpoint and worsened forgetting relative to ordinary ePC in every seed.

### Interpretation and revisit trigger

Response novelty identified difference, not task-conditional usefulness: it
assigned about half the normalized mass to the arithmetic teacher and improved
plasticity at a large retention cost. Revisit only with a packet utility or
maintenance criterion validated on a fixture where teacher evidence is
conditionally useful on the actual student inputs; retain normalized mass and
explicit wall-time accounting.

## D-20260725-cmcp-selector-calibration: Use response novelty and direct KD in the fast calibration loop

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence: experiments `20260725T222650Z-cmcp-mass-normalized`
  through `20260725T231500Z-cmcp-carom-bridge`

### Decision

For this toy complementary-teacher selector calibration, normalize applied KD
mass, use response-space conditional novelty, and use direct KD for the fast
loop. Preserve ePC as a separate settled-error routing hypothesis rather than
claiming it has no value. Do not claim a CMCP--CAROM unification until CAROM
implements and identifies a comparable marginal-novelty/maintenance ledger.

### Rationale

Mass normalization collapsed the old fixture. The redesigned fixture gave
independent evidence positive value. Response novelty beat gradient novelty
under the frozen calibration rule and nearly matched oracle Task-B loss on
disjoint seeds, although it worsened retention. ePC improved plasticity but
worsened retention and cost about 2.17x runtime, failing the frozen joint gate.
CAROM E2/E3 currently lacks both the shared ledger and a completed scientific
outcome needed for convergence evidence.

## D-20260719-diagnostic-findings: ePC representation collapse and weight explosion

- Date: `2026-07-19`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (pending review)
- Related evidence: experiment `20260719T135900Z-gpt2-diagnostic-cpu-battery`;
  commit `ee77c3e`

### Findings

CPU diagnostic battery on the 9 saved Run-2 checkpoints revealed:
1. ePC hidden states collapse to effective rank ~1.0 in layers 1-5 (vs 1.5-4.5
   for BP controls).
2. ePC layer 5 spectral norms are 20-40x larger than BP controls, with
   condition numbers 10-40x worse.
3. ePC gradient flow is U-shaped (high L0 and L5, dip in middle) while BP
   shows monotonic decay.

### Interpretation

The ePC objective as configured (lambda_output=0.05, steps=4) creates a
credit-assignment pathology: the output KD term dominates, causing
representation collapse in middle layers and compensatory weight explosion
in the last layer. This supports hypotheses 2 (restrictive representation)
and 3 (credit-assignment mismatch) from the outcome report.

### Next step

Design a follow-up GPU experiment with revised ePC hyperparameters:
- Increase lambda_output (e.g., to 0.3-0.5) to strengthen local prediction
  errors relative to the output term.
- Or enable the hidden-state matching arm (already configured but disabled)
  to maintain representation diversity.
- Preregister the revised config, obtain explicit bounded approval, and run
  3-seed distillation + outcome battery on GPU.

## D-20260719-r5-negative-result: ePC_KD fails the GPT-2 six-layer distillation gate

- Date: `2026-07-19`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (pending review)
- Related evidence: experiment `r5-runpod-20260719`; commit `dc61f31`;
  summary.json with promotion eval

### Outcome

The r5 Runpod distillation stage (3 seeds, GPT-2 six-layer student,
WikiText-103) completed validly, but its separately requested Stage-2 outcome
battery did not execute. ePC_KD failed all four distillation-promotion criteria:

- Update-matched gain: −0.52 nats (ePC_KD worse than BP+KD at 1000 updates)
- Wall-clock-matched gain: −1.56 nats (ePC_KD worse — BP+KD does ~4× updates)
- Per-seed regression: up to 0.569 nats worse
- ePC_KD (6.49–6.54) also worse than plain BP+CE (5.25–5.30)

One positive signal: activity_energy_monotone=true for all ePC_KD runs.
kd_gap_nats very high (~880–893), suggesting poor teacher→student learning
under ePC at this scale.

### Decision

The twelve-layer confirmation run is **not authorized**. The distillation gate
is a scientifically valid negative result, while the independently completed
outcome battery is recorded at
`experiments/20260718T223300Z-epc-outcome-6layer-battery/`. Before any further ePC
GPU work, diagnose whether the failure is:
1. A fundamental ePC scaling issue (energy relaxation doesn't help at GPT-2 scale),
2. A credit-assignment configuration problem (kd_gap too high), or
3. A hyperparameter/learning-rate issue specific to the ePC arm.

The activity_energy_monotone signal suggests the ePC mechanism itself is
functioning, but not translating into student improvement.

## D-20260717-six-then-twelve-epc-depth: Gate twelve layers on six

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: commit `7d4d4dc`; experiment
  `20260717T154506Z-epc-outcome-6layer-preflight`

### Decision

Run the scalable six-layer GPT-2-width ePC/BP/KD outcome comparison first, then
move to a twelve-layer student after the six-layer gate completes validly. Keep
the source/target domains, seeds, common low-rank adaptation rule, metrics, and
decision thresholds fixed across depths; only depth and the separately
approved resource envelope may change.

### Consequences

- Six layers is the immediate paid-compute gate and requires explicit approval
  of its recorded USD 7 total cap before provisioning.
- Twelve layers is preregistered as a contingent confirmation, not authorized
  by approval of the six-layer job.
- Invalid provenance, incomplete checkpoints, or a failed six-layer systems
  gate blocks the twelve-layer run. A scientifically negative but valid
  six-layer outcome is still reported before deciding whether the confirmation
  remains informative.

## D-20260717-evaluate-epc-network-outcomes: Test structural and adaptation outcomes

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: `docs/epc_outcome_probe_protocol.md`; experiment
  `20260717T145830Z-epc-outcome-probe-local-v1`; implementation `e398876`

### Decision

Because BP, KD, and ePC produced nearly equal loss in the corrected local gate,
evaluate whether ePC produces a network with other advantages. Start with a
small local instrument/effect-size pilot, then move quickly to a more scalable
and informative RunPod test after freezing the domain shift, checkpoints,
metrics, controls, runtime, and cost.

The primary endpoint is the adaptation/forgetting tradeoff under an identical
post-training update rule. Structural similarity, spectral rank, block-skip
sensitivity, and corruption/OOD robustness are secondary diagnostics. A
structural difference without functional benefit is descriptive, not grounds
for promotion.

### Consequences

- The prior perplexity comparison remains valid but is no longer the sole
  scientific question.
- The aborted July 17 GPU artifacts remain provenance-ineligible and cannot be
  reused as the checkpoint trio.
- Paid execution requires a new remote job record and explicit bounded approval.
- The local v1 run validates instrumentation only; its weak chronological split
  cannot support an ePC plasticity conclusion.

## D-20260714-sgld-pilot-before-production: Gate the next SGLD production run on a step-size pilot

- Date: `2026-07-14`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/sgld_tuning_plan.md`; experiments `20260714T182809Z-sgld-step-size-sweep-targeted` and `20260714T182834Z-sgld-step-size-sweep-full-suite`

### Context

The prior A100 run had energy R-hat mean 2.0 and maximum 3.3 despite some ESS improvement, so increasing chain length without identifying a usable discretization regime would risk paying for autocorrelated or unstable samples.

### Decision

Before another production run, test about six step sizes with two 500-step chains. Reject divergence; require R-hat below 1.2 and mean ESS above 50 to proceed. If the best unpreconditioned candidate remains above R-hat 1.1, estimate a diagonal gradient-variance preconditioner and repeat the sweep.

### Consequences

- The approximately 6,000-step diagnostic is cheaper than another failed 8,000-step production configuration.
- A passing pilot permits a production attempt but does not replace full production convergence diagnostics.
- An all-high-R-hat sweep triggers preconditioning rather than a hopeful longer run.

### Revisit trigger

Revisit thresholds after empirical calibration against analytic benchmarks or if the short-chain R-hat estimate proves too noisy to rank candidates reliably.

## D-20260709-hdpc-before-slt-columnar-upgrades: Try HDPC/ePC Tiny Shakespeare first

- Date: `2026-07-09`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: HDPC working draft; Goemaere et al. 2026 ePC paper; planned branch `agent/tinyshakespeare-hdpc`

### Context

Ben supplied an HDPC working draft describing homotopy distillation from backprop-trained transformers into PC-consistent learners plus energy-coupled PC crowns, and the Goemaere et al. ePC paper as background. The prior RelaLeap sequence emphasized SLT estimator validation before SLT-guided residual-layer construction, while SLT measurement work is still running/concluding.

### Decision

Try the HDPC/ePC plan first on the Tiny Shakespeare corpus. Use a bounded Runpod GPU run only after explicit resource/time/cost approval and after local tests/smoke checks. Treat SLT inputs to the process and columnar residual-layer models as afterwards upgrades, not prerequisites for the first HDPC prototype.

### Consequences

- The immediate implementation target is technical viability of homotopy-distilled PC learners and identity-initialized PC crowns on Tiny Shakespeare.
- Initial tests must catch silent failure modes: ordinary-BP leakage from detach mistakes, dropout/KV-cache misuse, non-monotone relaxation, mixed-precision error decay, and loss of the pure-KD anchor.
- SLT/WBIC/LLC validation remains required before scientific promotion of causal residual columns or SLT-guided claims, but it no longer blocks the first HDPC/ePC engineering prototype.
- Runpod approval must specify provider/account context, GPU/resource/image/storage/region, current price source, expected duration, maximum cost/time, data upload scope, artifact retrieval, and termination/cleanup behavior.

### Revisit trigger

Revisit if the Tiny Shakespeare HDPC prototype fails the anchor/path/distinctness/crown-identity tests, if Runpod cost is unjustified after local smoke tests, or after baseline HDPC results are strong enough to justify adding SLT inputs and columnar residual structure.

## D-20260725-colearned-global-causal-critic-v1: Preregister an intervention-trained critic

- Date: `2026-07-25`
- Status: `protocol accepted for implementation; core implemented, experiment unrun`
- Decision owner: Benjamin Goertzel requested the concrete protocol
- Related task/run: `docs/colearned_global_causal_critic_protocol_v1.md`;
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`

### Context

The v3 estimator recovered planted support with AUC 1.0 and the planted oracle
improved retention, but estimated and oracle support routing both failed to
improve the Shakespeare retention/plasticity tradeoff. Support identifies
participation; it does not identify which update intervention is useful.

### Proposed decision

Test a co-learned critic as an action-relevant abstraction of the learner's
global causal dynamics. Train it online from logged randomized, paired
interventions over module gradient-protection actions. Require held-out
counterfactual calibration before allowing its conservative policy to control
routing.

The v1 critic is model-based/bandit-style with a hard gradient boundary.
Differentiating through the learner is deferred until intervention prediction
and policy value are established.

### Rationale

Randomized intervention assignments identify the critic's targets while
co-learning keeps its model adapted to the moving learner. Joint attention
over module tokens can represent downstream and synergistic effects that an
independent support gate cannot. Local analytic diagnostics remain informative
features, but forcing critic predictions to agree with them would circularly
reinstate the failed support-routing assumption.

### Consequences

- No Shakespeare or paid compute until all synthetic estimation and policy
  gates pass.
- “Global causal structure” means the intervention/outcome projection defined
  by the protocol, not recovery of a complete causal graph.
- Utility and causal prediction are tested separately: good task utility alone
  may be a heuristic, while good prediction alone may not improve routing.
- All actions, propensities, paired snapshots, outcomes, and uncertainty
  estimates must be preserved.

### Implementation status

Core implementation landed locally at commit `690c8f7` on
`agent/colearned-causal-critic-v1`. Sixteen focused tests and the full suite
(`448 passed, 1 skipped`) passed. This does not adopt or validate the critic's
scientific hypothesis; calibration and confirmation remain gated.

### Revisit trigger

Revisit if the critic cannot predict held-out intervention effects, if a global
critic does not beat an equal-capacity independent critic on downstream or
synergy fixtures, or if calibrated prediction fails to yield policy value.

## D-20260703-train-time-causal-factor-approach: Try train-time causal factor learning

- Date: `2026-07-03`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `projects/relaleap/docs/train_time_causal_factor_preregistration.md`

### Context

RelaLeap has passed through two inadequate phases:

1. `v0` seven-arm posthoc pregate: useful as a smoke scaffold, but fail-closed, with handcrafted LLC proxy and no arm beating required null controls.
2. `v2` parameterized arms fitted to cached residuals: deployable mechanisms failed winner recovery, lost to controls, and failed null specificity.

Both phases learned or selected residual bases after freezing residual caches. The SLT residual-layer direction instead treats residual columns as local charts on transformer failure modes and validates factorization by local evidence/free-energy additivity, causal audits, and LLC interaction information.

### Decision

Try a genuinely new **train-time causal factor learner** in which residual columns are discovered jointly during task training. The approach must be preregistered before implementation and must be evaluated first on synthetic ground-truth regimes with strict fail-closed controls.

### Alternatives considered

- Continue scaling v0 posthoc pregate: rejected because v0 was only a smoke harness and no arm beat nulls.
- Continue v2 cached-residual fitting: rejected as insufficient because deployable mechanisms failed controls/null specificity.
- Train a generic sparse dictionary end-to-end: insufficient unless causal audits, SLT additivity, split/merge/transfer rules, and matched null controls are built in.

### Rationale and evidence

The guiding SLT residual-layer source says residual columns should be validated by decomposition of local evidence/free energy and dominated interaction remainder, not raw reconstruction. The GPT-5.5 Pro v2 plan recommends fail-closed matched controls, synthetic ground-truth regimes, exact ablation calibration, commutator audits, and LLC interaction information.

### Consequences

- No GPU or paid compute is justified before synthetic gates pass.
- No implementation claim should be made from reconstruction quality alone.
- Promotion requires matched-control wins, dependency-aware null wins, calibrated causal audits, and interpretable sparse LLC interaction structure.
- `low_rank_trap` and `random_null` success means blocking the columnar claim, not forcing a positive result.

### Revisit trigger

Revisit if synthetic regimes show the train-time learner cannot separate exact factorized, shared-core, synergistic, low-rank, oblique, and null cases under matched controls, or if LLC/WBIC calibration fails.

### Supersedes or superseded by

Supersedes reliance on v0/v2 posthoc cached-residual basis fitting as the next scientific step.

## D-20260704-slt-estimator-validation-current-focus: Gate residual-layer work on Tiny Shakespeare estimator validation

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/relaleap_slt_estimator_validation_plan.pdf`; `docs/slt_estimator_validation_plan_summary.md`

### Context

Ben directed that the new SLT estimator validation plan should become the current focus for RelaLeap. The prior residual-layer idea remains important, but the weak link is whether WBIC/SGLD/LLC estimators are meaningful enough to guide residual-layer construction rather than repeating the earlier handcrafted-proxy failure mode.

### Decision

Make SLT estimator validation the active RelaLeap focus. Proceed to SLT-guided residual-layer construction on top of the transformer only after all relevant estimators pass calibration and validation on a Tiny Shakespeare level corpus.

### Consequences

- Wave 0 interface/report-schema freeze and estimator validation work outrank new residual-layer mechanism development.
- Tiny Shakespeare is the first real-text validation target after analytic/synthetic calibration.
- Residual-layer guidance should consume validated estimator outputs, not uncalibrated or clipped proxy numbers.
- Failures in calibration, sampler diagnostics, MAP/prior/gauge checks, sample-size sensitivity, or Tiny Shakespeare validation block scientific promotion and keep residual-layer use gated.

### Revisit trigger

Revisit if Tiny Shakespeare-level validation is too expensive or inconclusive after analytic benchmarks pass, or if a smaller real-text proxy is explicitly chosen as an equivalent validation gate.

### Supersedes or superseded by

Temporarily prioritizes estimator validation over the 2026-07-03 train-time residual-column implementation path; it does not reject that path.

## D-20260704-controlled-frontier-model-routing: Treat Fable/GPT-5.6 throttling as an empirical operations risk

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `MEMORY.md`; `projects/relaleap/PROJECT.md`

### Context

Ben noted that Claude Fable may throttle or degrade work on certain topics, including advanced neural-network AI development, and that similar strategies may be needed for other controlled frontier models such as GPT-5.6-class systems. RelaLeap may be more likely to trigger this than symbolic-AI-heavy projects such as `petta-memory` or `petta-chem`, although properly framed SLT estimator validation may be less likely to trigger throttling because the immediate focus is estimator calibration rather than frontier-model optimization.

### Decision

When using Fable or similar controlled frontier models for RelaLeap, treat model throttling, downgrade, rerouting, refusal, or invisible quality degradation as an empirical operations risk. Keep prompts factually accurate while deliberately framing work by the real immediate research subgoal and nearest truthful low-friction category, record observed behavior by task type, compare outputs against other models or local methods, and keep estimator/core code and tests model-portable. Treat frontier-dev safeguards as ethically contested: they may have a coherent safety rationale, but are structurally entangled with competitive moat protection unless classifier scope, vetting criteria, and appeals are externally auditable.

### Consequences

- Do not depend on a single proprietary model for critical RelaLeap estimator, architecture, or scientific decisions.
- Do not lie or misrepresent tasks. It is acceptable to work around overly broad/sloppy provider filters by using accurate phrasing and legitimate “spin,” such as analytic SLT calibration, WBIC/SGLD estimator validation, or Tiny Shakespeare-level validation when that is the actual work.
- Record signs of degradation or model switching when Fable/GPT-5.6-class systems become available; hidden degradation is especially harmful because it corrupts research evidence.
- Prefer local/open-model/decentralized verification paths where possible, especially if RelaLeap succeeds in making open LLMs more capable.

### Revisit trigger

Revisit after empirical Fable/GPT-5.6-class usage data exists across RelaLeap, `petta-memory`, `petta-chem`, and other projects, or if provider policies/tooling become clearer.

## D-20260703-meaningful-slt-estimation-contract: Require calibrated SLT evidence before promotion

- Date: `2026-07-03`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/train_time_causal_factor_preregistration.md`; `repos/relaleap/src/relaleap/reporting.py`

### Context

Ben emphasized that RelaLeap should be very sure it is estimating SLT parameters meaningfully this time. Earlier work failed this standard: the main LLC term was a handcrafted complexity proxy, and WBIC/LLC was a tiny frozen-parameter diagnostic rather than an estimate over the learner's actual trainable singular structure.

### Decision

Scientific promotion now requires a mandatory SLT-estimation validity contract. WBIC/SGLD/LLC panels must be finite-sample proxies over actual trained parameter blocks, calibrated on known-SLT benchmarks, accompanied by sampler/temperature diagnostics and explicit input coverage/inference-budget accounting, and interpreted through module-vs-joint estimates with sample-size sensitivity and null-normalized uncertainty.

### Consequences

- Task loss, reconstruction, causal ablations, and null wins are still insufficient if the SLT evidence panel is uncalibrated.
- Reports must use finite-sample language and must not claim exact RLCT estimation.
- Reports must show enough input coverage to make the estimator meaningful: input counts, stratification/coverage, inference budget, and sensitivity as input count increases.
- Code-level reporting now rejects `scientific_status=pass` unless required calibrated SLT evidence fields are present.
- If calibration or uncertainty fails, the correct status is `scientific_status = fail_closed`.

### Revisit trigger

Revisit only after the known-SLT calibration suite demonstrates stable, null-normalized recovery of expected regular, singular, independent, redundant, and synergistic behavior across seeds, input-count sweeps, and WBIC/SGLD settings.
# D-20260715-epc-distillation-first

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel

Make effective ePC-based distillation of Tiny Shakespeare backprop transformers the immediate RelaLeap objective. Treat the columnar predictive-coding head with SLT guidance as the next stage, gated on a reproducible ePC distillation benefit. The first experiment must isolate relaxation depth from optimizer and stochastic-state drift, compare against matched BP and conventional KD, and fail closed unless a nontrivial `T>1` configuration improves held-out behavior across seeds while satisfying energy and gradient diagnostics.

## D-20260715-epc-gate-null: Do not promote the first block-state ePC objective

- Date: `2026-07-15`
- Status: `accepted result`
- Decision owner: Benjamin Goertzel's preregistered fail-closed gate
- Evidence: `experiments/20260715T153035Z-epc-distillation-gate-local-r2/RUN.md`; code commit `941b8b3`

The first matched-state three-seed diagnostic validated execution, exact
depth-one KD equivalence, monotone activity energy, and finite layerwise
gradients, but no genuine relaxation depth beat matched ordinary KD in every
seed. Do not scale this objective or begin columnar/crown/SLT-guided head work.
First determine whether output-KL/local-error scaling or layerwise credit
assignment explains the gap, and validate a revised mechanism on a synthetic
known-signal case under a newly frozen protocol.

### 2026-07-15 follow-up

The scaling defect was confirmed and corrected; synthetic local-credit tests
passed. A separately frozen v2 on untouched seeds materially increased deep
block credit but again failed to beat matched KD. This strengthens, rather than
relaxes, the decision: do not promote the current block-state objective. The
next run must test a distinct credit-assignment hypothesis, not another tuning
of lambda or relaxation depth.

## D-20260716-gpt2-small-pilot-protocol: Preregister the minimum GPT-2 pilot

- Date: `2026-07-16`
- Status: `proposed protocol; frozen before outcomes`
- Decision owner: Ben's GPT-2-small priority; numeric protocol drafted by the
  RelaLeap progress worker for Ben's review
- Contract: `worktrees/tinyshakespeare-hdpc/configs/gpt2_small_epc_pilot.json`

Do not iterate further on Tiny Shakespeare; it is below the scale needed to
resolve the hypothesis. Test a six-layer GPT-2-width student distilled from the
pinned 124M GPT-2 teacher on pinned WikiText-103. Keep hidden-state matching a
separate exploratory arm. Compare primary ePC against ordinary BP+KD under both
equal updates and equal elapsed time across three fixed seeds, and apply the
pre-run validation-loss/invariant criterion exactly. Passing promotes only a
larger confirmation. GPU execution remains separately gated on a successful
CPU dry-run and Ben's explicit bounded RunPod approval.
## D-20260727-c4prime-staged-execution: Admit the V4 bridge only through backend and substrate gates

- Date: `2026-07-27`
- Status: `accepted planning decision`
- Evidence: `docs/causal_critic_v4_c4prime_execution_plan_20260727.md`,
  `../../library/commutator-critic-c4prime-2026/SOURCE.md`, and
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/`.

The C4′ companion note gives the V4 critic a potentially valuable
function-pinned substrate, but it remains a proposed specification.  Sequence
the persistent work as V4-0 backend admission, V4-1 exact-asset/T=1 adapter
validation, V4-2 preregistration plus measured microprofile, and only then a
separately approved V4-3 deployment.

The Torch replica failures and absent JAX reproduction block exact-D admission.
Missing production checkpoints and settle code independently block substrate
validation.  Do not integrate the critic into RelaLeap, infer C2 validity,
open policy work, or spend on C4′ until the preceding gates pass.

Alternatives rejected: treating the quadratic sandbox as a transformer
validation; accepting a post-hoc tolerance as bit exactness; using reported
Mesto metrics without the pinned artifact bundle; and treating the proposed
45-A100-hour ceiling as authorization.
# 2026-07-28 — Label the GPU-ready transformer step as a clean-room hybrid

Decision: the locally validated GPT-2 PCStep seam is named
`clean_room_transformer_epc_v1`. It may support a bounded GPU engineering
smoke after separate costed approval, but it must not be described as Mesto
checkpoint-compatible or as a source-aligned transformer-local update.

Rationale: Mesto's public `metta-on-mork` `pcgraph` code fixes the
settle-then-update phase order and supplies checked XOR semantics, but it does
not specify attention, MLP, layer-normalization, tied-embedding, optimizer, or
transformer-local learning rules. The implemented seam therefore freezes
weights during block-state settlement and then uses explicit block gates with
ordinary autograd/AdamW. This is testable engineering progress while
preserving the production-asset boundary.

Evidence:
`experiments/20260728T184216Z-v4-1-gpt2-pcstep-preflight/` and
`experiments/20260728T184406Z-v4-1-gpt2-pcstep-full-suite/`.
# D-20260729-v4-1-independent-cleanroom-homotopy

- Date: `2026-07-29`
- Status: `accepted as local engineering substrate`
- Implementation: branch `agent/v4-1-cleanroom-homotopy-fable`, commit
  `3a38eb13c6d77eb3fb2fcd276dc25417b84ac394`
- Evidence:
  `experiments/20260729T084053Z-v4-1-cleanroom-homotopy-fable/`

Stop treating Mesto's unavailable production asset bundle as a prerequisite
for RelaLeap's clean-room engineering track. Maintain a strict provenance
boundary: independently specify and implement our own transformer homotopy/ePC
trainer, make no reproduction or compatibility claim, and retain the public
XOR seam only as a separately labelled phase-ordering reference.

V4-1 admits one explicitly named update mode,
`hybrid_settled_global_adamw`: local adjacent-block activity errors and a
teacher-output term determine settled activities, then ordinary global
autograd and gated AdamW update weights. This is deliberately not described as
a fully local predictive-coding weight rule.

The local implementation passes exact T=1 snapshot equivalence,
frozen-weight settlement, bounded multi-step scheduling, deterministic replay,
counter continuity, finite/monotone energy, and fail-closed configuration and
gate tests. These results admit the module as an engineering substrate only;
they do not establish efficacy, scaling, Mesto correspondence, or causal-critic
value.

## D-20260801-cleanroom-robustness-v1-primary-gate-failed

- Date: `2026-08-01`
- Status: `fail-closed; no promotion`
- Evidence: `experiments/20260801T063754Z-epc-robustness-reliability-run/`

The approved frozen reliability-first robustness evaluation did not support
promotion of the tested clean-room ePC configuration. On primary PTB OOD,
mean ePC-over-wall-clock-matched-KD gain was `-1.9135758082` nats with 1/3
positive fresh seeds. WikiText ID was likewise negative on average
(`-1.0506251653` nats; 1/3 positive). All three validators, exact
reaggregation, and 4/4 returned artifact hashes passed; the negative decision
is therefore scientific rather than an execution or evidence-integrity
failure. The pod was terminated and confirmed absent.

Do not retune or scale this frozen configuration on the observed seeds. Any
successor requires a versioned new protocol, fresh seeds, and a separately
approved compute envelope. This result is not a general refutation of ePC.

## D-20260803-frame-oracle-v4-admit-to-sealed-evaluation-only

- Date: `2026-08-03`
- Status: `implementation frozen; scientific gate unopened`
- Implementation: `agent/frame-oracle-v4` commit
  `1cbcf9e930a72d93ce388e549b86f97dc5e9185c`
- Evidence:
  `experiments/20260803T071411Z-frame-oracle-v4-freeze-before-open/`

Admit v4 only to the already committed one-use 24-case oracle gate. Its
deterministic layer now owns auxiliary-scoped negation and explicit possible
modality without treating a capitalized `No` inside a proper name as a free
negation cue. The prompt, schema, implementation, model ID, seed, paired
decode, and sealed-answer commitment are frozen; focused and full engineering
gates pass from a clean commit.

This is not semantic admission. The oracle was not invoked and the answers
were not opened. Labels, a frame readout, substitution scoring, and any
semantic loss remain blocked. The next scientific action must consume the
gate once from a fresh provenance-complete experiment and fail closed on any
invalid, nondeterministic, inexact, or imperfect-stratum result.

## D-20260803-frame-oracle-v4-import-provenance-blocks-opening

- Date: `2026-08-03`
- Status: `supersedes v4 execution admission; gate remains unopened`
- Evidence:
  `experiments/20260803T091034Z-frame-oracle-v4-exact-command-preflight/`

The exact frozen interpreter and runner cannot load the v4 dependency chain:
the virtual environment points `relaleap` at a separate causal-fibres source
tree and raises `ModuleNotFoundError` for `frame_oracle_v2` before argument
parsing. Therefore commit `1cbcf9e` is not admitted to scientific execution
despite its passing tests. Do not repair this implicitly at gate-opening time.

Require a clean descendant freeze with single-root module-path assertions,
interpreter/module provenance, and unchanged semantic hashes, followed by the
focused and full gates. Stop again before inference. Because the failure
occurred with `--help`, no public case, answer file, or Ollama call was made;
the existing sealed battery is not consumed and fresh cases are not yet
required. Labels, readout, substitution scoring, and semantic loss remain
blocked.

## D-20260803-frame-oracle-v4-import-provenance-repaired

- Date: `2026-08-03`
- Status: `implementation execution eligibility restored; gate unopened`
- Implementation: `agent/frame-oracle-v4` commit
  `acf3fbfecb1516069fb4f9c80006696e0c9c9081`
- Evidence:
  `experiments/20260803T111529Z-frame-oracle-v4-import-provenance-freeze/`

The bounded repair required by the prior provenance-block decision now passes
from a clean descendant without changing semantic sources. The frozen wrapper
sets exactly one v4-worktree source root; before CLI parsing, the runner records
interpreter metadata and verifies committed paths and hashes for `relaleap`
and frame-oracle v2/v3/v4, while rejecting all imported `relaleap` modules
outside that root. The exact interpreter now reaches `--help`, 7 focused and
14 exposed regression tests pass, and the full suite passes 182 tests with 5
skips.

Restore eligibility only for the exact one-use argv in the replacement freeze
manifest. This supersedes the execution suspension, not the semantic boundary:
the gate is still `opened=false`; no inference or answer evaluation occurred;
and labels, readout, substitution scoring, and semantic loss remain blocked.
Any later mismatch before decode leaves the gate unopened. Any failure after
the first public-case inference consumes the battery and fails closed.

## D-20260803-frame-oracle-v4-consumption-state-blocks-opening

- Date: `2026-08-03`
- Status: `supersedes one-use execution eligibility; real gate unopened`
- Evidence:
  `experiments/20260803T131110Z-frame-oracle-v4-consumption-counterexample/`
- Repair contract:
  `docs/frame_oracle_v4_consumption_state_repair_contract_20260803.md`

Do not execute the replacement manifest's one-use command. A mocked failure on
the second paired call, after one simulated public inference completed,
reproduced a persisted record with `gate_consumed=false` and
`completed_pairs=0`. This violates the already adopted rule that any
public-case inference consumes the battery and creates an unsafe reuse path.

Require a clean descendant whose runner atomically persists conservative
consumption before its first network request, checkpoints every completed call,
never reverts to unconsumed, and verifies the actual local model digest before
inference. Freeze it after independent failure-injection, focused, regression,
and full-suite tests; then stop again before scientific execution.

This decision is engineering fail-closure, not a semantic result. The audit
mocked the network function, used a synthetic fixture, and never touched
Ollama or sealed answers. The real gate remains `opened=false`; labels,
readout, substitution scoring, and semantic loss remain blocked.

## D-20260803-frame-oracle-v4-consumption-state-repaired-and-refrozen

- Date: `2026-08-03`
- Status: `supersedes consumption-state execution suspension; real gate unopened`
- Implementation: `agent/frame-oracle-v4-consumption-state` commit `53630b9`
- Evidence:
  `experiments/20260803T151446Z-frame-oracle-v4-consumption-state-repair-dev/`
  and
  `experiments/20260803T151801Z-frame-oracle-v4-consumption-state-freeze/`

Restore implementation-side eligibility only for the replacement manifest's
exact one-use argv. The clean descendant atomically persists
`consumed_pending` before inference, checkpoints each completed request,
forbids resumption, never reverts to unconsumed, and verifies the actual local
registry digest rather than copying the requested ID into metadata.

Independent synthetic failure injection passed 10/10; combined focused v4,
exposed regressions, and the full suite passed 17/17, 24/24, and 192 with 5
skips. The freeze contacted only `GET /api/tags`; no generation endpoint or
answer content was accessed. Prompt, schema, v2/v3/v4 semantics, model,
seed/decode, public battery, and commitment remain unchanged.

This decision restores engineering eligibility, not semantic admission. The
gate remains `opened=false` and `consumed=false`. Any failure after the durable
pending transition consumes it and blocks labels, readout, substitution
scoring, and semantic loss.

## D-20260803-frame-oracle-v4-failed-closed-v5-sealed

- Date: `2026-08-03`
- Status: `v4 consumed and failed; v5 fresh battery sealed unopened`
- V4 evidence:
  `experiments/20260803T171351Z-frame-oracle-v4-one-use-gate/`
- V5 integrity evidence:
  `experiments/20260803T172839Z-frame-oracle-v5-sealed-contract-r2/`
- V5 contract: `docs/frame_oracle_v5_fresh_gate_contract_20260803.md`

The exact frozen v4 one-use command completed all 48 calls under the repaired
state machine and terminally recorded `consumed_failed`. Schema validity was
24/24, but paired determinism and exact semantic keys were both 17/24, so the
preregistered conjunction failed. V4 admits no labels, frame readout,
substitution scorer, or semantic loss. Its opened cases and responses are
retired evidence and may not become repair fixtures or selection targets.

Preserve a fresh successor path rather than tuning: the contract-templated v5 bundle
contains 24 new cases with zero exact sentence overlap against v1--v4 and the
opened offline corpus. Its answer-file commitment is
`72097ca3560a8a14d3cd523a0b44d35fd02b084953983ac04526e3e3ed0ce51c`
and it remains `opened=false`. V5 execution is ineligible until a bounded
source-derived hypothesis, independent tests, clean isolated implementation,
and separate provenance-complete freeze all pass.

The v5 author knew the aggregate v4 verdict and per-stratum summary but did
not inspect raw proposals/rows. Therefore v5 is case-disjoint and
process-sealed, not strictly outcome-blind at the aggregate-stratum level. A
strict outcome-blind claim requires a separately authored battery.

## D-20260803-frame-oracle-v5-slot-masked-cue-hypothesis

- Date: `2026-08-03`
- Status: `behavior contract frozen; implementation not started`
- Evidence:
  `experiments/20260803T191310Z-frame-oracle-v5-source-behavior-audit/`
- Contract: `docs/frame_oracle_v5_behavior_spec_20260803.md`

Adopt one bounded, source-derived v5 hypothesis: mask the proposed entity spans
before deterministic polarity/modality cue recognition, and add common
contracted auxiliary negation plus `cannot` to the finite grammar. Four
independently authored counterexamples at clean v4 commit `53630b9` reproduce
the motivating defects without reading v4 raw outcomes, v5 public cases, or v5
answers.

Do not broaden this into a deterministic English parser or claim that it
repairs predicate/slot selection, abstention, or LLM proposal nondeterminism.
Implementation must use fresh independent fixtures on an isolated descendant,
preserve the atomic one-use runner and provenance checks, pass focused,
exposed-regression, and full tests, and stop at a new clean unopened freeze.
No label, readout, substitution scorer, or semantic loss is admitted.

## D-20260803-frame-oracle-v5-bounded-behavior-implemented

- Date: `2026-08-03`
- Status: `behavior implementation accepted; scientific gate unopened`
- Implementation: `agent/frame-oracle-v5` commit `f474d96`
- Evidence:
  `experiments/20260803T211703Z-frame-oracle-v5-behavior-implementation-clean/`
- Frozen parent contract: `docs/frame_oracle_v5_behavior_spec_20260803.md`

Accept the clean bounded implementation of the already frozen hypothesis. It
masks one case-insensitive, whitespace-normalized surface occurrence of each
proposed entity slot before finite polarity/modality cue recognition, adds
common straight/curly-apostrophe auxiliary contractions and `cannot`, and
leaves the closed proposal prompt unchanged. Ten independent fixtures, 34
exposed frame/atomic-runner regressions, and all 225 local tests passed.

This does not establish proposal correctness, slot correctness, abstention, or
determinism. It also does not yet satisfy the preopen provenance gate: a v5
one-use runner, import-hash registry, and clean freeze manifest remain absent.
Do not infer, inspect answers, or admit labels/readout/substitution scoring/a
semantic loss until a separate preopen freeze passes and the later one-use
scientific conjunction passes.

## D-20260803-frame-oracle-v5-preopen-freeze-passed

- Date: `2026-08-03`
- Status: `implementation eligible for one exact future use; gate unopened`
- Implementation: `agent/frame-oracle-v5-freeze` commit `a90298b`
- Evidence:
  `experiments/20260803T231206Z-frame-oracle-v5-runner-provenance-freeze/`

Accept the v5 implementation-side preopen gate. The versioned runner preserves
the conservative atomic consumption state machine, uses the v5 normalizer,
reads committed answers only after all paired calls, and verifies the exact
local model digest before transition. A pinned wrapper and import attestor
verify one source root and exact v2--v5 source hashes before argument parsing.

The clean freeze passed 20 focused v5/state-machine tests, 44 exposed frame
regressions, 212 pinned-interpreter tests with 5 skips, and 235 broader
host-interpreter tests. The public contract was mechanically validated; the
answer file was not read. Only `GET /api/tags` and a no-inference `--help`
preflight ran. Therefore restore eligibility only for the manifest's exact
one-use argv in a fresh experiment. V5 remains `opened=false`,
`consumed=false`; no oracle outcome, label, readout, substitution score, or
semantic loss is admitted.

## D-20260803-frame-oracle-v5-failed-closed-v6-sealed

- Date: `2026-08-03`
- Status: `v5 consumed and failed; v6 process-sealed unopened`
- V5 evidence:
  `experiments/20260804T011531Z-frame-oracle-v5-one-use-gate/`
- V6 evidence:
  `experiments/20260804T013026Z-frame-oracle-v6-sealed-contract/`
- V6 contract: `docs/frame_oracle_v6_fresh_gate_contract_20260803.md`

The exact frozen v5 one-use command completed all 48 calls under clean commit
`a90298b` and terminally recorded `consumed_failed`. All 24 rows were
schema-valid; only 18/24 were paired-deterministic and 18/24 exact. The
preregistered perfect conjunction therefore failed. Permanently retire v5 and
admit no labels, readout, substitution evaluation, or semantic loss. Its
opened cases, proposals, normalized rows, and answers may not become fixtures
or tuning targets.

Preserve a successor path without tuning: the v6 bundle contains 24 new
sentences and committed exact frames, covers the existing closed ontology and
required strata, has zero exact overlap with v1--v5 and offline-readout-v1,
and remains `opened=false`. The author knew v5's aggregate/per-stratum
terminal report and failure identifiers but did not use proposal or
normalized-row contents. Accordingly, v6 is exact-case-disjoint and
process-sealed, not strictly outcome-blind.

V6 execution is ineligible until a new bounded source-derived hypothesis,
independent fixtures, isolated implementation, focused/exposed/full
engineering tests, atomic one-use runner, exact import/model/source provenance,
and a separate clean unopened freeze all pass.

## D-20260803-frame-oracle-v6-mask-all-exact-slot-occurrences

- Date: `2026-08-03`
- Status: `bounded source behavior frozen; implementation absent`
- Evidence:
  `experiments/20260804T031820Z-frame-oracle-v6-source-behavior-audit-r2/`
- Contract: `docs/frame_oracle_v6_behavior_spec_20260803.md`

At clean consumed-v5 commit `a90298b`, the deterministic surface layer masks
only one non-overlapping occurrence of each proposed entity slot. Independent
synthetic appositive/byline fixtures reproduce three contradictions: a repeated
title leaks `could` into possible modality, a repeated author name leaks both
`May` and `not`, and a repeated located-entity name leaks lower-case `no` into
negated polarity. A single-mention control behaves correctly. The preserved
engineering suites pass 20 focused, 44 exposed regressions, and 235 full tests.

Therefore freeze v6 to the smallest repair: mark the union of every exact
case-insensitive, whitespace-normalized surface match of both proposed slots
before running the unchanged v5 cue recognizers. Do not add fuzzy matching,
change the prompt/schema/cue vocabularies, or claim improvements to proposal
selection, abstention, or nondeterminism. A later isolated implementation and
separate atomic runner/provenance freeze are still required before opening.

No v5 gate row/proposal/normalized output, v6 case/answer, oracle inference,
readout, substitution evaluation, or semantic loss was used or admitted.

## D-20260803-frame-oracle-v6-bounded-implementation-passed

- Date: `2026-08-03`
- Status: `behavior implementation passed; runner/provenance freeze absent`
- Implementation: `agent/frame-oracle-v6` commit `df62566`
- Evidence:
  `experiments/20260804T051741Z-frame-oracle-v6-behavior-implementation-clean/`

Accept the bounded v6 engineering implementation. It imports and therefore
mechanically preserves the v5 prompt, closed schema helpers, canonicalization,
and finite polarity/modality recognizers while replacing only the slot mask
with the union of every exact case-insensitive whitespace-normalized match.
Independent repeated-title, repeated-name, single-mention, overlapping-slot,
identical-slot, unmasked-cue, and canonical-unknown fixtures passed 8/8. The
complete exposed frame/atomic-runner battery passed 52/52 and the full suite
passed 243/243 from clean commit `df62566`.

This decision does not open or admit v6 scientifically. A separate conservative
atomic runner, single-root import/source/model provenance contract, and clean
unopened freeze must pass before any one-use execution. No sealed v6 case or
answer, v5 opened outcome, oracle inference, readout, substitution evaluation,
semantic loss, remote compute, push, or publication was used.

## D-20260804-frame-oracle-v6-preopen-freeze-passed

- Date: `2026-08-04`
- Status: `implementation eligible for one exact future use; gate unopened`
- Implementation: `agent/frame-oracle-v6-freeze` commit `56b9eb9`
- Evidence:
  `experiments/20260804T072033Z-frame-oracle-v6-runner-provenance-freeze/`

Accept the v6 implementation-side preopen gate. The versioned runner preserves
the conservative atomic consumption state machine, uses the bounded v6
all-occurrence normalizer, reads committed answers only after all paired calls,
and verifies the exact local model digest before transition. A pinned wrapper
and import attestor verify one source root and exact v2--v6 source hashes
before argument parsing.

The clean freeze passed 18 focused v6/state-machine tests, 62 exposed frame and
runner regressions, 230 pinned-interpreter tests with 5 skips, and 253 broader
host-interpreter tests. The public contract was mechanically validated; the
answer file was not read. Only `GET /api/tags` and a no-inference `--help`
preflight ran. Therefore restore eligibility only for the manifest's exact
one-use argv in a fresh experiment. V6 remains `opened=false`,
`consumed=false`; no oracle outcome, label, readout, substitution score, or
semantic loss is admitted.

## D-20260804-frame-oracle-v6-protocol-failed-v7-sealed

- Date: `2026-08-04`
- Status: `v6 consumed protocol failure; v7 process-sealed unopened`
- V6 evidence:
  `experiments/20260804T091501Z-frame-oracle-v6-one-use-gate/`
- V7 evidence:
  `experiments/20260804T092458Z-frame-oracle-v7-sealed-contract-r2/`
- V7 contract: `docs/frame_oracle_v7_fresh_gate_contract_20260804.md`

The exact frozen v6 one-use command passed all provenance and engineering
checks, then checkpointed 45/48 local calls before `ClosedFrame` rejected a
schema-shaped proposal whose predicate and `abstain` flag were inconsistent.
The atomic exception handler terminally recorded `consumed_failed`. Paired
decoding never completed, so the committed answers were never read and no
accuracy or per-stratum metrics exist. Permanently retire v6 and admit no
labels, readout, substitution evaluation, or semantic loss. Do not inspect or
tune against its opened cases, raw proposals, normalized rows, or answers.

Preserve a successor path without tuning: the v7 bundle contains 24 new
sentences and committed exact frames, covers the existing closed ontology and
required strata, has zero exact overlap with v1--v6 and offline-readout-v1,
and remains `opened=false`. The initial candidate was rejected by its
integrity validator for a negation coverage miscount; r2 corrected only that
unopened authoring error. The author knew the v6 terminal exception class and
call count but did not inspect the failing case, proposal, response,
normalized row, or answers. Accordingly, v7 is exact-case-disjoint and
process-sealed, not strictly outcome-blind.

V7 execution is ineligible until a bounded source-derived hypothesis,
independent fixtures, isolated implementation, focused/exposed/full
engineering tests, atomic one-use runner, exact import/model/source provenance,
and a separate clean unopened freeze all pass.

## D-20260804-frame-oracle-v7-fail-closed-proposal-ingestion

- Date: `2026-08-04`
- Status: `bounded behavior implementation accepted; execution ineligible`
- Evidence:
  `experiments/20260804T111528Z-frame-oracle-v7-source-contract-audit-r3/`
- Implementation evidence:
  `experiments/20260804T131754Z-frame-oracle-v7-behavior-implementation-clean-r2/`
- Implementation: `agent/frame-oracle-v7` commit `f096252`
- Contract: `docs/frame_oracle_v7_behavior_spec_20260804.md`

At clean v6 commit `56b9eb9`, four independent source-only fixtures show that
the generation schema's explicit constraints accept both non-unknown/abstain
and unknown/non-abstain combinations. Strict `ClosedFrame.from_json` rejects
both before `normalize_proposal_v6` reaches its intended union-to-unknown
branch. Canonical unknown and non-unknown controls continue to pass. The
unchanged baseline passed 10 focused tests and 230 full pinned-interpreter
tests with 5 skips.

Freeze the smallest fail-closed repair at proposal ingestion only: validate
the existing field envelope without weakening `ClosedFrame`, then canonicalize
to unknown whenever either `predicate == "unknown"` or `abstain=true`.
Otherwise continue through unchanged v6 behavior. Preserve prompt, schema,
ontology, cue recognition, slot masking, strict committed-answer validation,
and runner state semantics.

Accept the bounded implementation at clean commit `f096252`. Its independent
fixtures cover both mismatch directions, canonical controls, malformed fields,
confidence bounds, and preservation of direct strict-`ClosedFrame` rejection.
Validation passed 17 focused tests, 77 exposed frame/atomic-runner regressions,
and the full 247-test suite with 5 skips.

No opened v6 content, v7 case/answer, oracle inference, readout, substitution
evaluation, semantic loss, remote compute, push, or publication was used or
admitted. A separate atomic runner/provenance implementation and clean
unopened freeze remain required before v7 may be opened.

## D-20260804-frame-oracle-v7-preopen-freeze

- Date: `2026-08-04`
- Status: `implementation-side preopen eligibility passed; gate unopened`
- Implementation: `agent/frame-oracle-v7` commit `61776ef`
- Evidence:
  `experiments/20260804T152139Z-frame-oracle-v7-runner-provenance-freeze/`

Accept the v7 implementation-side freeze only. The exact clean descendant
preserves v6's conservative atomic one-use state machine, replaces only the
versioned normalizer/prompt aliases with v7, and attests one pinned source root
and exact v2--v7 hashes before argument parsing. Its independent mismatch
fixture confirms that the runner applies the frozen union-to-unknown behavior.

The clean freeze passed 28 focused v7/state-machine tests, 90 exposed frame and
runner regressions, 258 pinned-interpreter tests with 5 skips, and 281 broader
host-interpreter tests. The public contract was mechanically hash/metadata
validated. The answer file was not read; only `GET /api/tags` and a
no-inference `--help` preflight ran, with zero `/api/generate` requests.

V7 is eligible only for the exact manifest argv in a later fresh experiment.
It remains `opened=false`, `consumed=false`, and admits no label corpus,
readout, substitution evaluation, or semantic loss. Any failure after the
pending-state checkpoint is terminal consumption and must fail closed.

## D-20260804-frame-oracle-v7-failed-v8-sealed

- Date: `2026-08-04`
- Status: `v7 scientific gate failed closed; v8 process-sealed unopened`
- V7 evidence:
  `experiments/20260804T171432Z-frame-oracle-v7-one-use-gate/`
- V8 evidence:
  `experiments/20260804T172300Z-frame-oracle-v8-sealed-contract/`
- V8 contract: `docs/frame_oracle_v8_fresh_gate_contract_20260804.md`

The exact frozen v7 command reverified commit `61776ef`, all commitments and
source hashes, the local model digest, 28 focused tests, 90 exposed
regressions, and 258 pinned tests with 5 skips. It then completed all 48 calls
and durably terminated in `consumed_failed`. Although all 24 rows were
schema-valid, paired determinism was 19/24 and exact semantic keys were 3/24;
no required stratum was perfect.

Retire v7 permanently. Its raw cases, proposals, responses, normalized rows,
and answers are failure evidence only and may not be tuning data. Admit no
label corpus, readout, substitution evaluation, or semantic loss.

Preserve a successor path without tuning: v8 contains 24 new sentences with
committed exact frames, all five predicates and inherited coverage counts,
zero exact overlap with v1--v7 plus offline-readout-v1, and `opened=false`.
Its author knew the v7 aggregate counts and per-stratum imperfection but did
not inspect raw v7 content. V8 is exact-case-disjoint and process-sealed, not
strictly outcome-blind. It remains ineligible until a bounded source-derived
hypothesis, independent fixtures, isolated implementation, atomic runner,
exact provenance, and separate clean unopened freeze all pass.

## D-20260804-frame-oracle-v8-empty-canonical-slots-fail-closed

- Date: `2026-08-04`
- Status: `bounded source behavior frozen; implementation absent; v8 unopened`
- Evidence:
  `experiments/20260804T192000Z-frame-oracle-v8-source-behavior-audit-r4/`
- Contract: `docs/frame_oracle_v8_behavior_spec_20260804.md`

At clean v7 commit `61776ef`, the proposal envelope accepts whitespace-only
entity strings for a non-unknown predicate. The existing v6 canonicalizer then
produces valid non-unknown frames with an empty first slot, empty second slot,
or both. Three independent synthetic fixtures reproduced these outcomes; a
non-empty control, 17 focused v7 tests, and 258 full tests with 5 skips passed.

Freeze a bounded v8 occupancy rule. After the existing v7 envelope and
predicate/abstention union checks, canonicalize both entity slots. If either is
empty for an otherwise non-unknown proposal, return canonical unknown with
confidence preserved. Otherwise preserve v7 behavior unchanged. This rule
must not infer, repair, or judge the correctness of a non-empty entity.

No v7 opened material or v8 case/answer was inspected. At this decision point,
v8 remained unopened and unimplemented. The implementation obligation below
supersedes that open loop without changing this source-derived rule.

## D-20260804-frame-oracle-v8-bounded-behavior-implemented

- Date: `2026-08-04`
- Status: `bounded behavior implemented and validated; v8 unopened`
- Evidence:
  `experiments/20260804T212000Z-frame-oracle-v8-behavior-implementation-clean/`
- Commit: `dee262f5f41fd29a3787b3ba1ddbd064c72f15d7`

Accept only the frozen occupancy behavior implementation. After v7 envelope
validation and predicate/abstention union handling, either empty canonical
entity slot maps an otherwise non-unknown proposal to canonical unknown with
confidence preserved. Occupied proposals delegate unchanged to v7; no entity
is inferred, repaired, or judged.

The exact clean commit passed 20 focused v8 tests, 108 exposed frame/runner
regressions, and 278 full tests with 5 skips, plus compilation, diff, hash, and
pre/post clean-state checks. V8 remains unopened. Atomic-runner adaptation,
exact source/import/model provenance, and a separate unopened freeze remain
mandatory before any one-use execution.

No sealed v8 artifact, opened v7 material, model endpoint, inference, label
corpus, readout, substitution evaluation, semantic loss, remote compute, push,
or publication was used.

## D-20260804-frame-oracle-v8-runner-provenance-frozen

- Date: `2026-08-04`
- Status: `implementation-side eligible for one exact future use; v8 unopened`
- Evidence:
  `experiments/20260804T232548Z-frame-oracle-v8-runner-provenance-freeze/`
- Commit: `b54fdcc1c391bff49fcf1c7dce8b394355a287e4`

Freeze only the exact one-use argv in the manifest. The v8 runner preserves
the v7 resumeless atomic consumption contract, substitutes only the accepted
v8 empty-slot normalizer, and attests a single hashed import root through v8
plus the exact local model digest. Independent validation passed 32 focused
v8/state-machine tests, 94 exposed regressions, 290 pinned tests with 5 skips,
and 313 host tests from the clean commit.

This is implementation-side eligibility, not semantic admission. The public
contract was mechanically validated, the answer file was not read, and the
only Ollama contact was `GET /api/tags`; `--help` made no inference request.
V8 remains `opened=false`, `consumed=false`. A fresh successor turn may
execute the manifest argv once after exact reverification and must fail closed
on any post-transition error.

## D-20260805-frame-oracle-v8-executable-provenance-failed-closed

- Date: `2026-08-05`
- Status: `current manifest revoked; v8 unopened and scientifically unconsumed`
- Evidence:
  `experiments/20260805T013037Z-frame-oracle-v8-one-use-gate/`
- Repair contract:
  `docs/frame_oracle_v8_execution_permission_repair_contract_20260805.md`

The exact manifest argv failed before runner entry because the pinned wrapper
was committed with Git mode `100644` but invoked directly. Exit 126 occurred
before provenance attestation, atomic consumption, answer access, or model
generation. No gate or provenance artifact exists; the public contract retains
its frozen hash and `opened=false`.

Revoke the `b54fdcc` manifest's one-use eligibility and do not retry or chmod
it in place. This supersedes only the prior execution-eligibility decision,
not the accepted bounded v8 semantic behavior or unopened battery. A clean
isolated repair may change only the wrapper Git mode to `100755`, add direct
executable-boundary tests and mode attestation, and produce a replacement
unopened freeze. A later separate turn is required for scientific execution.

## D-20260805-frame-oracle-v8-executable-provenance-repaired-unopened

- Date: `2026-08-05`
- Status: `replacement manifest frozen; v8 unopened and unconsumed`
- Evidence:
  `experiments/20260805T042743Z-frame-oracle-v8-execution-permission-repair-freeze/`
- Commit: `96460e99fd3ae76e242ca82cabdc499da2570266`
- Replacement manifest SHA-256:
  `b750eb181c1639112e0f9fea2bc3ae2fcc51bc9122e061ba88f500ccc19d11fe`

Accept the contract-bounded execution-provenance repair only. The pinned
wrapper's bytes remain SHA-256 `543e0a...be713f`; its Git/filesystem modes are
now attested as `100755`/`0755`. One new regression proves that the wrapper can
be executed as the argv program through `/usr/bin/env`, reaches `--help`, and
writes single-root import provenance without public/answer/model arguments.

The clean commit passed 33 focused, 95 exposed, 291 pinned tests with 5 skips,
and 314 host tests. Public and semantic commitments are unchanged, the answer
file was not read, and only local `GET /api/tags` plus no-inference `--help`
ran. V8 remains `opened=false`, `consumed=false`; no downstream semantic stage
is admitted.

The prior `b54fdcc` manifest remains revoked and may never be retried. Freeze
the replacement manifest's exact argv for at most one later use from a fresh
turn after full reverification. Any deviation or post-transition failure must
fail closed.

## D-20260805-frame-oracle-v8-failed-v9-sealed

- Date: `2026-08-05`
- Status: `v8 scientific gate failed closed; v9 process-sealed unopened`
- V8 evidence:
  `experiments/20260805T064745Z-frame-oracle-v8-one-use-gate-r2/`
- V9 evidence:
  `experiments/20260805T070000Z-frame-oracle-v9-sealed-contract/`
- V9 contract: `docs/frame_oracle_v9_fresh_gate_contract_20260805.md`

The replacement v8 manifest passed clean provenance and engineering
reverification, then its exact one-use command completed all 48 requests and
atomically terminated `consumed_failed`. Aggregate results were 24 valid, 21
paired-deterministic, and 15 exact, with imperfect required strata. Preserve
v8 as negative evidence only: never retry, resume, train on, or tune against
its opened cases, responses, normalized rows, expected frames, or failure
identifiers. Admit no label corpus, readout, substitution evaluation, or
semantic loss.

Preserve a successor path without tuning: v9 contains 24 new sentences with
the same closed ontology and frozen coverage counts, a committed answer file,
`opened=false`, and zero exact sentence overlap against v1--v8 plus the failed
offline readout corpus. V9 is process-sealed and exact-case-disjoint, not
strictly outcome-blind. The next admissible step is one bounded source-derived
behavior audit using independent fixtures; no v9 inference is yet eligible.

## D-20260805-frame-oracle-v9-surface-grounding-frozen

- Date: `2026-08-05`
- Status: `source behavior frozen; v9 unopened and unimplemented`
- Evidence:
  `experiments/20260805T090359Z-frame-oracle-v9-source-behavior-audit/`
- Contract: `docs/frame_oracle_v9_behavior_spec_20260805.md`

At clean v8 commit `96460e9`, three independent synthetic fixtures show that
the v8 normalizer emits non-unknown semantic keys when proposed `entity_a`,
`entity_b`, or both have no exact boundary-delimited surface occurrence in the
sentence. A both-present control remained unchanged. The baseline passed 20
focused v8 tests and 291 full pinned-interpreter tests with 5 skips.

Freeze one bounded v9 rule only: after all inherited v8 checks, require each
canonical non-unknown slot to have at least one exact case-insensitive
boundary-delimited match in the whitespace-normalized sentence. If either is
absent, return canonical unknown with confidence preserved. Do not infer,
repair, lemmatize, translate, or synonym-expand slots; preserve the v8 prompt.

No v8 opened outcome or v9 case/answer was read. No inference, readout,
substitution evaluation, semantic loss, remote compute, push, or publication
occurred. V9 remains `opened=false`. The next admissible step is an isolated
behavior implementation followed by focused, exposed, and full tests; runner
adaptation and provenance remain separate.

## D-20260805-frame-oracle-v9-behavior-accepted-unopened

- Date: `2026-08-05`
- Status: `behavior accepted; v9 unopened; runner/provenance absent`
- Commit: `9b10fdc916a68a099b27cd3e040c0f9ce09a694b`
- Evidence:
  `experiments/20260805T111902Z-frame-oracle-v9-behavior-acceptance-r2/`
- Contract: `docs/frame_oracle_v9_behavior_spec_20260805.md`

Accept only the frozen surface-grounding normalizer. After inherited v8
validation and non-empty checks, each canonical non-unknown slot must have an
exact case-insensitive `_slot_pattern` match in the whitespace-normalized
sentence. Either absence returns canonical unknown with proposal confidence
preserved; equal slots may share one occurrence. Do not infer, repair,
lemmatize, translate, synonym-expand, or use substring-only matching.

The exact clean commit passed 25 focused v9 tests, 146 exposed v2--v9
oracle/runner tests, and 316 full tests with 5 skips. V9 remains
`opened=false`. This behavior result does not admit inference, labels,
readout, substitution evaluation, or semantic loss. The next admissible step
is a separate conservative atomic-runner and exact source/import/model
provenance implementation and clean unopened freeze; gate execution must wait
for a later turn.

## D-20260805-frame-oracle-v9-runner-provenance-frozen

- Date: `2026-08-05`
- Status: `implementation-side eligible for one exact future use; v9 unopened`
- Commit: `8edead5b3977b9ce15761df3ae33dbd1b4e2639c`
- Evidence:
  `experiments/20260805T132357Z-frame-oracle-v9-runner-provenance-freeze/`
- Canonical manifest SHA-256:
  `ef78d00c813dc727b4bd1f148d358124f65fd37e160f3c5017df6f6e9a92c805`

Freeze only the exact one-use argv in the canonical manifest. The v9 runner
preserves the v8 resumeless atomic consumption contract, substitutes only the
accepted v9 surface-grounding normalizer, and attests one hashed source root
through v9 plus the exact local model digest. Corrected clean validation passed
39 focused v9/state-machine tests, 162 exposed v1--v9 frame/runner regressions,
330 pinned full tests with 5 skips, and 353 host tests.

The earlier successful command at
`experiments/20260805T132226Z-frame-oracle-v9-runner-provenance-freeze/`
generated a manifest with a wrong host-test count and is superseded; it is not
canonical freeze evidence.

This is implementation-side eligibility, not semantic admission. Neither
sealed v9 file was accessed; only local `GET /api/tags` and no-inference
`--help` ran. V9 remains unopened and unconsumed. A fresh successor turn must
reverify the canonical manifest, clean commit, prior seal identifiers, local
model digest, and preopen tests before executing the exact argv at most once.
Any deviation or post-transition failure must fail closed.

## D-20260805-frame-oracle-v9-failed-closed

- Date: `2026-08-05`
- Status: `v9 scientific gate failed closed; permanently consumed`
- Evidence:
  `experiments/20260805T152703Z-frame-oracle-v9-one-use-gate-r3/`
- Gate artifact SHA-256:
  `13ad454aee6b665bb4669e469bbcf43731861788764b9cff405c1d3c03525d54`

The fresh-turn preflight reverified the canonical manifest and exact argv,
clean commit `8edead5`, every frozen source/import/model identifier, prior seal
identifiers, 39 focused tests, 162 exposed regressions, 330 pinned tests with
5 skips, and 353 host tests. The exact argv then ran once, completed 48/48
calls, and durably terminated in `consumed_failed`. All 24 rows were
schema-valid, 18/24 were paired-deterministic, and 0/24 semantic keys were
exact; every required stratum had zero exact rows.

Retire v9 permanently. Its opened cases, proposals, responses, normalized
rows, expected frames, failure identifiers, and raw artifact are failure
evidence only and may not be used for tuning. Admit no label corpus, readout,
substitution evaluation, or semantic loss. Do not infer a causal diagnosis
from the aggregate result.

Two earlier local records are preserved as unopened engineering failures: the
first transcribed the model digest incorrectly; the second had an ambiguous
shell-continuation argv verifier. Neither reached pinned-wrapper entry, sealed
file access, tests, or inference. The next admissible step is a fresh v10
process-sealed battery constructed without consulting v9 opened content.

## D-20260805-frame-oracle-v10-process-sealed-unopened

- Date: `2026-08-05`
- Status: `v10 process-sealed, exact-case-disjoint, and unopened`
- Evidence:
  `experiments/20260805T172833Z-frame-oracle-v10-sealed-contract-r3/`
- Contract: `docs/frame_oracle_v10_fresh_gate_contract_20260805.md`
- Public SHA-256:
  `9a0a963f3def7c94421c6e393a82ef8e989ad922c965b3fe48c43f3023b2e3cb`
- Answer commitment SHA-256:
  `a59c056c24abbfbf3a535c047b2e4cb045e3e4d882f58700d8e6d2694d99a9af`

Preserve v9 as permanently consumed negative evidence. V10 contains 24 new
committed cases and passes all inherited ontology/coverage checks,
`opened=false`, and zero exact sentence overlap against v1--v9 plus
offline-readout-v1. The author knew only v9 aggregate and per-stratum counts;
the automated comparison emitted no prior sentence or identifier. V10 is
therefore process-sealed and exact-case-disjoint, not strictly outcome-blind.

The first integrity attempt reported one unnamed overlap. Repair was blind to
the collision: apply the same semantic-neutral dossier prefix to every v10
sentence, alter no expected frame, and rerun the whole contract. Final
integrity passed. The unchanged clean v9 source separately passed 162 exposed
and 330 full tests with 5 skips.

No v10 implementation or inference is admitted, nor any label corpus,
readout, substitution evaluation, or semantic loss. A fresh successor turn
may perform at most one bounded source-derived behavior audit with independent
synthetic fixtures and without accessing v10 answers.

## D-20260805-frame-oracle-v10-overt-template-consistency

- Date: `2026-08-05`
- Status: `behavior implemented and verified; v10 unopened`
- Evidence:
  `experiments/20260805T192502Z-frame-oracle-v10-source-behavior-audit/`
- Contract: `docs/frame_oracle_v10_behavior_spec_20260805.md`

Clean v9 source checks that both canonical slots have boundary-delimited
surface occurrences but does not bind those occurrences to the proposed
predicate or directed roles. Four independent probes reproduced non-unknown
wrong-predicate or reversed-role frames; four matching controls were
unchanged. Focused, exposed, and full host suites passed 25, 162, and 353
tests. This result is a source capability counterexample, not a causal
diagnosis of v9's failed gate.

Freeze a finite negative consistency guard over five overt template families:
capital-of, located-in, active authored-by, passive authored-by, and simple
copular state, with specific-before-generic precedence. A recognized template
whose predicate or directed slots disagree with the proposal must become
canonical unknown with confidence preserved; exact matches and unrecognized
sentences delegate to v9. Do not infer aliases, synonyms, facts, or implicit
relations, and preserve the prompt. Implement and test this behavior only in a
separate turn; runner/provenance adaptation and inference remain forbidden.

Implementation is now verified at clean commit `82f3ecc`. Independent
fixtures cover all five templates, wrong predicates, reversed directed roles,
exact controls, inherited abstention/occupancy/surface failure classes,
whitespace/case/punctuation normalization, unrecognized paraphrases,
specific-before-generic precedence, invalid envelopes, confidence
preservation, and prompt identity. Clean focused/exposed/full suites passed
38/200/391. The first development run exposed a fixture-classification error:
`A is B` had been called an unmatched paraphrase even though it is the frozen
generic copular template. Only that invented fixture was replaced; the
implementation did not change.

This admits runner/provenance adaptation as the next separate unopened step,
not inference. V10 remains unopened and unconsumed; no semantic downstream
stage or loss is admitted. Evidence:
`experiments/20260805T212936Z-frame-oracle-v10-behavior-acceptance/`.

## D-20260805-frame-oracle-v10-runner-provenance-frozen

- Date: `2026-08-05`
- Status: `implementation-side eligible for one exact future use; v10 unopened`
- Commit: `ad7fe09291f2808bc1b5bc6df23a71279a397916`
- Evidence:
  `experiments/20260805T234401Z-frame-oracle-v10-runner-provenance-freeze/`
- Canonical manifest SHA-256:
  `78df4abc53834f201a9e6945a82374c8a5473cb3799fc835dd0b9176ec5d4e04`

Freeze only the exact future argv in the canonical manifest. The v10 runner
uses the accepted overt-template consistency normalizer and preserves the
resumeless atomic consumption contract, answer-after-paired-decode ordering,
exact model-digest rejection, and one-root source/import attestation through
v10. Clean validation passed 53 focused, 215 exposed, 383 pinned full tests
with 5 skips, and 406 host tests.

Draft audit found and corrected missing v9 import/test coverage, an incorrect
v10 source hash, and one invalid invented copular fixture before the clean
commit and canonical freeze. No sealed input informed any correction.

This is implementation-side eligibility only. Neither sealed v10 file was
accessed; only local `GET /api/tags` and no-inference `--help` ran. V10 remains
unopened and unconsumed. A fresh successor turn must reverify every canonical
identifier and preopen gate before executing the exact argv at most once. Any
deviation or post-transition failure must fail closed.

## D-20260805-frame-oracle-v10-failed-closed-consumed

- Date: `2026-08-05`
- Status: `v10 permanently consumed negative evidence`
- Evidence:
  `experiments/20260806T030955Z-frame-oracle-v10-one-use-gate/`

Fresh preflight reproduced every frozen implementation/provenance gate: exact
manifest and argv, clean `ad7fe09`, source hashes, sealed identifiers, local
model digest, pinned one-root imports, 53 focused tests, 215 exposed tests, 383
pinned tests with 5 skips, and 406 host tests. The exact argv then ran once,
completed 48/48 calls, and terminally recorded `consumed_failed`: 24/24
schema-valid, 17/24 paired-deterministic, and 12/24 exact. Required strata
were imperfect (abstention 4/4, direct 1/4, explicit negation 2/6, paraphrase
1/1, possible 3/5, world-knowledge trap 1/4).

Retire v10. Admit no label corpus, readout, substitution evaluation, or
semantic loss. Opened rows, proposals, responses, answers, and failure
identifiers are not a tuning source. The aggregate result rejects only the
frozen v10 normalizer/local-model configuration and does not establish a
causal diagnosis. A successor may process-seal v11 from the pre-existing
ontology/coverage contract without consulting v10 opened content.

## D-20260805-frame-oracle-v11-process-sealed

- Date: `2026-08-05` (local; `2026-08-06` UTC)
- Status: `v11 process-sealed, unopened, and unconsumed`
- Evidence:
  `experiments/20260806T051159Z-frame-oracle-v11-sealed-contract/`
- Public SHA-256:
  `49fb93d12beb68c15eb834a51a35eb03abf284d8c074058a551e1becd8e86cae`
- Answer commitment SHA-256:
  `7f97f0a7933f0cdf23611e3cb497273d1bc52014989e105bf790be9a250b4d19`

Author v11 only from the inherited closed ontology and frozen coverage counts.
The accepted battery contains 24 aligned unique cases: four direct, six
explicit-negation, five possible, one paraphrase, four abstention, and four
world-knowledge-trap cases, with all five predicates and five `located_in`
frames. Integrity confirmed the answer commitment, `opened=false`, and zero
exact sentence overlap against v1--v10 plus offline-readout-v1. Comparison
against v10 loaded only public sentences inside a non-identifying set check;
no sentence or collision identifier was emitted.

The unchanged clean v10 implementation at `ad7fe09` passed 215 exposed tests
and 383 full tests with 5 skips. No opened v10 row, proposal, response, answer,
or failure identifier informed v11; no v11 oracle/model call, implementation,
label corpus, readout, substitution evaluation, or semantic loss occurred.

Preserve v10 as consumed negative evidence and v11 as unopened. A fresh
successor may perform at most one bounded source-derived behavior audit using
independent synthetic fixtures, then stop before implementation or inference.

## D-20260806-frame-oracle-v11-terminal-question-contract

- Date: `2026-08-06`
- Status: `source behavior frozen; v11 unopened and unimplemented`
- Evidence:
  `experiments/20260806T071142Z-frame-oracle-v11-source-behavior-audit/`
- Contract: `docs/frame_oracle_v11_behavior_spec_20260806.md`
- Contract SHA-256:
  `f16345eb6b0fc6e4f0e566871ec9a6e8d2fcac59d286e7e74416fb0812a8d62f`

Clean v10 has no deterministic interrogative guard despite the inherited
prompt requiring questions to become canonical unknown. Four independent
terminal-question probes spanning every non-unknown predicate remained
non-unknown; four matched declarative controls were unchanged. Clean focused,
exposed, and full suites passed 38, 215, and 406 tests.

Freeze only this finite negative rule: after valid proposal ingestion,
canonicalize a non-unknown proposal to unknown with confidence preserved when
the trimmed sentence ends in ASCII `?`; otherwise delegate exactly to v10.
Do not infer interrogative force from other syntax or punctuation and do not
alter the prompt. This source counterexample neither diagnoses v10's gate nor
reveals anything about v11 cases.

V11 remains unopened and unconsumed. A separate successor may implement the
frozen rule with independent fixtures, then stop before runner/provenance work
or inference. No downstream semantic stage or loss is admitted.

## D-20260806-frame-oracle-v11-bounded-behavior-implemented

- Date: `2026-08-06`
- Status: `behavior implemented and verified; v11 unopened`
- Evidence:
  `experiments/20260806T091116Z-frame-oracle-v11-behavior-acceptance/`
- Clean commit: `b76d9579a583586d47e258fcf84e57e866c40f6f`

Accept only the frozen finite terminal-question guard. After strict proposal
envelope validation, inherited v10 handling remains authoritative for raw
`predicate=unknown` or `abstain=true`. A valid non-unknown proposal becomes
canonical unknown with validated confidence only when `sentence.rstrip()`
ends in ASCII `?`; otherwise normalization delegates unchanged to v10. The v11
prompt is the identical v10 object.

Independent fixtures cover all four non-unknown predicates, matched
declarative controls, trailing whitespace, internal and fullwidth question
marks, inherited unknown/abstain cases, invalid envelopes, confidence, and
prompt identity. Clean acceptance passed 30 focused, 245 exposed, and 436 full
tests plus compilation, diff, and clean-state checks. The first development
wrapper invocation failed before collection due to a missing worktree `cd`;
only that wrapper was repaired.

V11 remains unopened and unconsumed. This admits runner/provenance adaptation
as the next separate unopened step, not inference. No label corpus, readout,
substitution evaluation, semantic loss, remote compute, push, or publication
is admitted.

## D-20260806-frame-oracle-v11-runner-provenance-frozen

- Date: `2026-08-06`
- Status: `implementation-side eligible for one exact future use; v11 unopened`
- Clean commit: `46c16f0742d8a87ac5755fc35f6981b8245080cb`
- Evidence:
  `experiments/20260806T111606Z-frame-oracle-v11-runner-provenance-freeze/`
- Canonical manifest SHA-256:
  `9745561dd25220d35e047fa4930714a118c85d0fc5ac8eef954edb0296625738`

Freeze only the exact future argv recorded in the canonical manifest. The v11
runner uses the accepted terminal-question normalizer while preserving durable
pre-request consumption, resumeless atomic checkpoints, answer-after-paired-
decode ordering, exact model-digest rejection, and one-root source/import
attestation through v11. Clean validation passed 46 focused, 261 exposed, 452
host, and 429 pinned-interpreter tests with 5 skips.

Neither sealed v11 file was read; only local `GET /api/tags` and no-inference
wrapper `--help` ran. V11 remains unopened and unconsumed. A fresh successor
must reverify every canonical identifier and preopen gate before executing the
frozen argv at most once. No label corpus, readout, substitution evaluation,
semantic loss, remote compute, push, or publication is admitted.

## D-20260806-frame-oracle-v11-gate-failed-closed

- Date: `2026-08-06`
- Status: `v11 permanently consumed and retired; downstream gate closed`
- Evidence:
  `experiments/20260806T131410Z-frame-oracle-v11-one-use-gate/`

Retire v11 after the single exact frozen argv passed every preregistered
engineering/provenance check but terminally recorded `consumed_failed` with
24/24 schema-valid, 21/24 paired-deterministic, and 0/24 exact rows. Every
required stratum had zero exact rows. Preserve this only as aggregate negative
evidence for the frozen v11 normalizer and local `qwen2.5:7b` configuration;
it does not establish a causal diagnosis.

Do not inspect or tune against opened v11 rows, proposals, responses, answers,
or failure identifiers. Admit no label corpus, readout, substitution
evaluation, or semantic loss. A successor may process-seal v12 only from the
pre-existing ontology and coverage contract, without consulting v11 opened
content. No remote compute, push, or publication is authorized by this result.

## D-20260806-frame-oracle-v12-process-sealed

- Date: `2026-08-06`
- Status: `v12 process-sealed, exact-case-disjoint, unopened, and unconsumed`
- Evidence:
  `experiments/20260806T151513Z-frame-oracle-v12-sealed-contract/`
- Contract: `docs/frame_oracle_v12_fresh_gate_contract_20260806.md`
- Public SHA-256:
  `a6f6e12ec083497515358fb31051ff5d34fe84cf361d042d7bd751469324cc91`
- Answer commitment SHA-256:
  `ac7d0438e6a1d648ff4ebd898f0a3218f435068532cfe82b6aff5b4bfcb85fdf`

Preserve v11 as consumed negative evidence and admit v12 only as an unopened
successor. V12 has 24 aligned unique cases, the inherited closed categorical
schema and 4/6/5/1/4/4 stratum counts, exactly five `located_in` frames, and
zero exact sentence overlap against v1--v11 plus offline-readout-v1. Automated
comparison against v11 emitted only a zero overlap count, no sentence or case
identifier. The author knew v11 aggregate and per-stratum counts but inspected
no opened v11 content; v12 is therefore process-sealed and exact-case-disjoint,
not strictly outcome-blind.

V12 remains ineligible for inference until a fresh bounded source-derived
hypothesis, independent fixtures, isolated implementation, atomic runner,
exact provenance, and separate clean unopened freeze pass. No label corpus,
readout, substitution evaluation, semantic loss, remote compute, push, or
publication is admitted.

## D-20260806-frame-oracle-v12-finite-coordination-contract

- Date: `2026-08-06`
- Status: `source counterexample reproduced; finite behavior contract frozen`
- Evidence:
  `experiments/20260806T171519Z-frame-oracle-v12-source-behavior-audit/`
- Contract: `docs/frame_oracle_v12_behavior_spec_20260806.md`
- Contract SHA-256:
  `6dad6fc6ab014a564ce05bc3f6225f8581444ce4eead5e82cc54372f6dd71619`

Clean v11 source accepted four independently invented comma-`and`
two-proposition sentences as the same non-unknown frames as matched
single-proposition controls. Freeze only a case-insensitive ASCII
`,\s+and\b` recognizer after inherited normalization and exact masking of all
surface occurrences of both proposed slots. A match in the masked remainder
returns canonical unknown with validated confidence; otherwise delegate to
v11. Do not generalize to bare `and`, other coordinators, dependency parsing,
or delimiters inside a fully masked slot.

This is bounded source evidence only. It neither reveals v12 contents nor
diagnoses any earlier gate. V12 remains unopened and unconsumed. Implement the
finite rule with independent fixtures in a separate clean isolated turn, then
stop before runner/provenance adaptation or inference. No downstream semantic
stage is admitted.

## D-20260806-frame-oracle-v12-bounded-behavior-implemented

- Date: `2026-08-06`
- Status: `behavior implemented and verified; v12 unopened`
- Evidence:
  `experiments/20260806T191425Z-frame-oracle-v12-behavior-implementation/`
- Clean commit: `9bab920284e1d61fd95239b4094f1aeb2c3ddf11`

Accept only the frozen finite coordination guard. After strict proposal
envelope validation, inherited v11 handling remains authoritative for raw
`predicate=unknown` or `abstain=true`. For a valid non-unknown proposal, apply
inherited canonical slot normalization and all-occurrence case-insensitive
surface masking, then map to canonical unknown with validated confidence only
when ASCII `,\s+and\b` occurs in the masked remainder. Otherwise delegate
unchanged to v11. The v12 prompt is the identical v11 object.

Independent fixtures cover every non-unknown predicate, matched
single-proposition controls, a delimiter wholly inside each proposed slot
position, excluded coordinator/punctuation surfaces, unmatched grounding,
inherited question and unknown/abstain behavior, invalid envelopes,
confidence, and prompt identity. A first focused run found two fixture-only
leading-article assumptions; the implementation did not change. Clean
acceptance passed 33 focused, 294 exposed, 462 pinned tests with 5 skips, and
485 host tests, plus compilation, diff, hash, and clean-state checks.

V12 remains unopened and unconsumed. This admits a separately frozen
runner/provenance adaptation as the next step, not inference. No label corpus,
readout, substitution evaluation, semantic loss, remote compute, push, or
publication is admitted.

## D-20260806-frame-oracle-v12-runner-provenance-frozen

- Date: `2026-08-06`
- Status: `atomic runner frozen; v12 unopened and unconsumed`
- Evidence:
  `experiments/20260806T211608Z-frame-oracle-v12-runner-provenance-freeze/`
- Clean commit: `228ff13c99a7e6c5fedc34886ff6d00734925eed`
- Manifest SHA-256:
  `8f7099a100389e82b700c542f16081427ebb3b706a083e34b21f30af8aa462f6`

Admit only the exact manifest-bound v12 runner. It must durably persist
`consumed_pending` before the first request, checkpoint each response,
forbid resume/replacement, defer answer access until all paired decodes,
normalize with v12, and verify the pinned interpreter, model digest, one source
root, and exact modules through v12.

The clean isolated acceptance passed 50 focused, 311 exposed, 502 host, and
479 pinned tests with 5 skips. Preserve the disclosed automation-cell overlap:
two noncanonical invocations shared a captured log tail, but no sealed access
or inference occurred; a final isolated unchanged invocation passed and
reproduced the artifact hashes.

V12 remains `opened=false` and `consumed=false`. Any execution belongs to a
fresh turn, must fully revalidate the frozen manifest and argv, and may occur
at most once. No labels, readout, substitution evaluation, semantic loss,
remote compute, push, or publication is admitted.

## D-20260806-frame-oracle-v12-consumed-failed

- Date: `2026-08-06`
- Status: `failed closed; permanently consumed`
- Evidence:
  `experiments/20260806T231440Z-frame-oracle-v12-one-use-gate/`
- Gate artifact SHA-256:
  `51ab831ea9afc31fda335cecf1fd3cb961f67feb60278e6e5346dc532d9257ef`

Retire v12 after its single exact frozen argv passed every preregistered
engineering/provenance check but failed the scientific gate. The terminal
aggregate is 24/24 schema-valid, 18/24 paired-deterministic, and 4/24 exact;
no required stratum was perfect. This is negative evidence only for the frozen
v12 normalizer and local `qwen2.5:7b` proposal configuration and is not a
causal diagnosis.

The aggregate stdout unexpectedly emitted case-level failure identifiers,
which were surfaced during post-run aggregate review. Preserve the disclosure,
but do not inspect or tune against those identifiers or any opened row,
proposal, response, or answer. Admit no label corpus, readout, substitution
evaluation, or semantic loss. A future v13 may be process-sealed only from the
pre-existing ontology and coverage contract, without consulting v12 opened
content or surfaced identifiers. No remote compute, push, or publication is
authorized by this result.

## D-20260806-frame-oracle-v13-process-sealed

- Date: `2026-08-06` (local; `2026-08-07T01:33:29Z` completion)
- Status: `sealed; integrity passed; unopened and unconsumed`
- Evidence:
  `experiments/20260807T012715Z-frame-oracle-v13-sealed-contract/`
- Public SHA-256:
  `8674b1d9fb372ed116ac8033f099f6ec0c672d2e1971bfcb098d7111c583e1e3`
- Answer commitment:
  `c1aa66a7e8e2bc06d8589ba4b3dfc190939743f389f3de510649e65481d5a5b5`

Preserve v12 as consumed negative evidence and v13 as its fresh exact-case-
disjoint successor. The v13 battery satisfies the inherited 24-case closed
schema, exact 4/6/5/1/4/4 strata, all five predicates, exactly five
`located_in` frames, and zero exact sentence overlap against v1--v12 plus
offline-readout-v1. Clean `228ff13` passed 311 exposed tests and 479 pinned
tests with 5 skips.

The automated comparator was permitted to read prior public strings only to
emit a non-identifying overlap count. No v12 opened row, proposal, response,
answer, or surfaced failure identifier informed v13. Keep `opened=false` and
do not access `gate_answers.json` during the next audit. A later fresh turn may
perform at most one bounded source-derived behavior audit with independent
fixtures and no inference. No labels, readout, substitution evaluation,
semantic loss, remote compute, push, or publication is admitted.

## D-20260806-frame-oracle-v13-semicolon-hypothesis-rejected

- Date: `2026-08-06` (local; `2026-08-07T03:31:58Z` completion)
- Status: `source hypothesis falsified; implementation rejected`
- Evidence:
  `experiments/20260807T032523Z-frame-oracle-v13-source-behavior-audit/`

Reject the conditional masked-remainder `;\s+and\b` v13 rule. The
preregistered audit expected four exact-template semicolon-`and` sentences to
survive v12 normalization, but all four already became canonical unknown via
the inherited v10 whole-sentence template consistency guard. Do not adapt the
opened independent fixtures to manufacture a passing counterexample and do
not implement the rejected rule.

The unchanged clean source passed 50 focused, 311 exposed, 479 pinned tests
with 5 skips, and 502 host tests. V13 remains unopened and unconsumed. A later
source audit, if any, requires a fresh preregistration and independent fixtures;
it may not inspect v13 answers or infer from sealed content. No inference,
labels, readout, substitution evaluation, semantic loss, remote compute, push,
publication, or semantic-free work is admitted.

## D-20260806-frame-oracle-v13-slot-only-fragment-contract

- Date: `2026-08-06` (local; `2026-08-07T05:31:56Z` completion)
- Status: `source counterexample reproduced; finite rule frozen; unimplemented`
- Evidence:
  `experiments/20260807T052500Z-frame-oracle-v13-fragment-source-audit/`
- Contract:
  `docs/frame_oracle_v13_fragment_behavior_spec_20260807.md`
- Contract SHA-256:
  `483248d04bb96cc0831c9bac6a5c5cab7f913c6cf3799d648c608858726d003d`

Accept the bounded source counterexample: clean v12 preserves all four
independent punctuation-separated slot-only fragments as non-unknown, with
the same semantic key as matched one-proposition controls and preserved
confidence. After inherited union masking, every fragment remainder contains
no ASCII letter while every control remainder does.

Freeze only the finite `[A-Za-z]`-absence guard in the cited contract. A
separate clean successor may implement it with fresh independent fixtures and
must stop before runner/provenance adaptation or inference. The unchanged
source passed 50 focused, 311 exposed, 479 pinned tests with 5 skips, and 502
host tests. V13 remains unopened and unconsumed. No sealed v13 path or answer,
v12 opened content or identifier, inference, labels, readout, substitution
evaluation, semantic loss, remote compute, push, publication, or semantic-free
work was used or admitted.

## D-20260807-frame-oracle-v13-fragment-guard-implemented

- Date: `2026-08-07` (local; `2026-08-07T07:33:06Z` completion)
- Status: `complete verified; runner not adapted; unopened and unconsumed`
- Implementation commit: `47d4eeeff4e27746f27bfa257c68a6352262504e`
- Evidence:
  `experiments/20260807T072744Z-frame-oracle-v13-fragment-implementation/`

Accept the clean bounded implementation of the frozen v13 finite fragment
contract. For validated non-unknown proposals, it union-masks every inherited
exact occurrence of both canonical slots and canonicalizes to unknown only
when the remainder has no ASCII `[A-Za-z]` letter; every other case delegates
to v12. Prompt identity and validated confidence are preserved.

The exact clean run passed 30 focused, 341 exposed, 509 pinned tests with 5
skips, and 532 host tests. Stop before runner/provenance adaptation or
inference. V13 remains unopened and unconsumed; no labels, readout,
substitution evaluation, semantic loss, remote compute, push, publication, or
semantic-free work is admitted.

## D-20260807-frame-oracle-v13-runner-provenance-frozen

- Date: `2026-08-07` (local; `2026-08-07T09:36:08Z` completion)
- Status: `atomic runner frozen; v13 unopened and unconsumed`
- Clean commit: `8108d986e95d66e74cdb222695b9c94f81350c26`
- Evidence:
  `experiments/20260807T092902Z-frame-oracle-v13-runner-provenance-freeze/`
- Canonical manifest SHA-256:
  `7f12401d1bcd8ac1ff9c0427f9af45246ffcaa3e109b16c9fb67fe788f40e325`

Admit only the exact manifest-bound v13 runner. It uses the accepted v13
normalizer and preserves durable pre-request consumption, per-call atomic
checkpoints, forbidden resume, answer-after-decode ordering, exact local model
digest verification, and one-root v2--v13 source/import attestation.

The clean freeze passed 48 focused, 359 exposed, 527 pinned tests with 5 skips,
and 550 host tests. Only `GET /api/tags` and pinned-wrapper `--help` ran;
neither sealed file nor `/api/generate` was accessed. V13 remains unopened and
unconsumed. Any execution requires a fresh-turn revalidation of every frozen
identifier, seal, model/source provenance, and test battery before at most one
exact argv. No labels, readout, substitution evaluation, semantic loss, remote
compute, push, or publication is admitted.
## D-20260807-frame-oracle-v13-terminal-retirement

- Date: `2026-08-07`
- Status: `adopted; v13 consumed_failed; downstream semantic stages blocked`
- Evidence: `experiments/20260807T132600Z-frame-oracle-v13-one-use-gate/`

Retire v13 permanently after its exact one-use gate completed 48/48 calls but
reached only 24/24 schema-valid, 20/24 paired-deterministic, and 15/24 exact.
Admit no labels, readout, substitution evaluation, or semantic loss. Preserve
opened material as terminal evidence only. Any successor battery must be v14,
freshly process-sealed from the inherited ontology and coverage contract
without using v13 rows, responses, answers, or surfaced failure identifiers.

## D-20260807-frame-oracle-v14-process-sealed

- Date: `2026-08-07`
- Status: `v14 sealed, exact-case-disjoint, unopened, and unconsumed`
- Evidence:
  `experiments/20260807T151100Z-frame-oracle-v14-sealed-contract-r2/`
- Public SHA-256:
  `db5a60a5781c543cb766ef3a3c276dfa49e8c71da1b3a35add00398c8fe93da2`
- Answer commitment:
  `c66446c05fff38cbb60bea118eb5437c70172d24eef841b114929145b2b658ff`

Preserve v13 as permanently consumed negative evidence. V14 was authored only
from the inherited closed ontology and coverage contract, without inspecting
v13 opened cases, responses, answers, artifacts, or surfaced identifiers. The
non-identifying comparator found zero exact sentence overlap against exposed
batteries through v13 plus offline-readout-v1. Integrity accepted 24 aligned
unique cases, exact frozen strata, all five predicates, exactly five
`located_in` frames, and `opened=false`; 225 focused and 527 pinned tests with
5 skips passed.

V14 is process-sealed and exact-case-disjoint, not strictly outcome-blind. It
remains unopened and unconsumed. A fresh successor may conduct at most one
bounded source-derived behavior audit using independent fixtures and without
accessing v14 answers. No oracle inference, labels, readout, substitution
evaluation, semantic loss, remote compute, push, publication, or semantic-free
work is admitted.
## D-20260807-frame-oracle-v14-relation-bearing-contract-required

- Date: `2026-08-07`
- Status: `adopted; source counterexample reproduced; v14 remains unopened`
- Evidence:
  `experiments/20260807T171100Z-frame-oracle-v14-source-behavior-audit/`

Do not execute v14 under the current v13 normalizer. An independent audit
reproduced that unrelated ASCII residue `x` is sufficient for v13 to accept
relationless grounded fragments across all four non-unknown predicates. Freeze
a finite predicate-specific relation-bearing remainder contract with fresh
fixtures before implementation. Preserve the audit fixtures as exposed
regressions and do not tune against v14 or inspect its answers. No oracle
inference, labels, readout, substitution evaluation, or semantic loss is
admitted.

## D-20260807-frame-oracle-v14-relation-bearing-contract-frozen

- Date: `2026-08-07`
- Status: `adopted; implementation pending; v14 remains unopened`
- Evidence:
  `experiments/20260807T191100Z-frame-oracle-v14-relation-bearing-contract/`

After v13 returns a non-unknown result, require exact equality between the
proposal's predicate/canonical slots and the inherited v10 whole-sentence
`_overt_template` result. Otherwise return canonical unknown with preserved
validated confidence. This is the finite predicate-specific relation-bearing
contract; do not extend it with synonyms, parsers, or sealed-case-dependent
exceptions. Implementation must use fresh preregistered fixtures in a clean
isolated worktree. Runner adaptation and inference remain separate future
turns. V14 stays sealed, unopened, and unconsumed.
## D-20260807-frame-oracle-v14-first-implementation-fixtures-failed

- Date: `2026-08-07`
- Status: `failed closed; candidate implementation unadmitted`
- Evidence:
  `experiments/20260807T211100Z-frame-oracle-v14-relation-bearing-implementation/`

Preserve the 11/13 focused result as a failed preregistered fixture gate. Two
fresh cases assumed to survive v13 were already unknown under v13, so the run
stopped before exposed or pinned suites. Do not modify or replace these opened
fixtures within the run, and do not admit or commit the candidate normalizer.
The frozen finite relation-bearing contract itself is unchanged. A successor
may freeze an independent acceptance set in a separate run. V14 remains
sealed, unopened, and unconsumed; runner adaptation and inference remain
blocked.

## D-20260808-frame-oracle-v14-fixture-provenance-protocol

- Date: `2026-08-08`
- Status: `adopted; process only; no fixture admitted`
- Evidence:
  `experiments/20260808T011300Z-frame-oracle-v14-fixture-provenance-protocol/`

Independent v14 acceptance fixtures require two stages. Stage A may read only
the frozen finite contract, clean v13 normalizer/test at `8108d98`, the frozen
protocol, and a post-boundary OS-random receipt; it must record a file-read
ledger and freeze fixture hashes before any candidate visibility. Stage B is a
later clean turn. Any unexpected input, prior visibility, hash discrepancy,
premise mismatch, or test failure retires the fixture set. This decision
admits no fixture or code and leaves v14 sealed, unopened, and unconsumed.
## D-20260808-frame-oracle-v14-stage-a-requires-context-isolation

- Date: `2026-08-08`
- Status: `adopted; no fixture admitted; v14 remains unopened`
- Evidence:
  `experiments/20260808T031441Z-frame-oracle-v14-stage-a-contamination-audit/`

Do not execute Stage A inside the persistent semantics worker: its mandatory
project-history audit reveals details of retired fixture attempts and violates
the frozen no-prior-visibility requirement. Stage A requires a fresh process
with a mechanically enforced readable-input allowlist, denial receipts for all
other project inputs, and immutable artifact hashes before Stage B. The
persistent worker may verify receipts but must not author or preview fixtures.
No implementation, runner work, inference, labels, readout, substitution
evaluation, or semantic loss is admitted.
# 2026-08-08 — Process isolation does not substitute for independent authorship

**Decision:** Do not generate v14 Stage-A fixtures using derivation logic
supplied by the persistent semantics worker, even inside the verified
Bubblewrap boundary. Require an independently initialized author whose only
inputs are the frozen four-file allowlist and post-boundary randomness.

**Rationale:** The worker has necessarily read retired fixture details. A
child shell can satisfy filesystem denial checks while inheriting contaminated
fixture choices through worker-authored code, making the required
no-prior-visibility attestation false. V14 remains sealed and Stage B remains
blocked.
# 2026-08-08 — Freeze non-disclosing Stage-A bundle schema

**Decision:** Any future independent-author Stage-A output must satisfy
`docs/frame_oracle_v14_stage_a_bundle_schema_20260808.md`. Verify exact file
membership, hashes, provenance and denial receipts, executable identity,
predicate coverage, and premise results without printing fixture text. Any
discrepancy retires the entire bundle; repair in place is forbidden. This does
not substitute for an independent author and does not authorize Stage B.

**Evidence:**
`experiments/20260808T091730Z-frame-oracle-v14-stage-a-bundle-schema-r3/`.
# 2026-08-08 — Stage-A author eligibility is a pre-launch outer decision

- An author's own claim of freshness is insufficient. Before launch, a trusted
  outer process must establish immutable executable/runtime identity, absence
  of inherited context, general-purpose independent provenance, the exact
  four-input boundary, and complete launch receipts.
- Mutable aliases, opaque provider context, inherited sessions, or fixture
  logic supplied by this history-exposed worker are ineligible. A passing
  preflight is necessary but not sufficient; bundle verification and later
  Stage B remain separate gates.
- Evidence: `experiments/20260808T112000Z-frame-oracle-v14-author-eligibility-contract/`.

# 2026-08-08 — Treat local Qwen only as a Stage-A artifact candidate

**Decision:** The SHA-256-verified local Ollama 0.31.1 plus `qwen2.5:7b`
closure is eligible for the next no-inference runtime preflight, but is not yet
an eligible author. Require exact isolated runtime-closure receipts,
fresh-context proof, and noninteractive bundle compatibility before any Stage-A
launch. Artifact identity alone does not authorize inference or fixture work.

**Evidence:**
`experiments/20260808T132900Z-frame-oracle-v14-local-author-preflight-r2/`.
# 2026-08-08 — Control-server launch is not inference-runner eligibility

**Decision:** Accept the hash-pinned, network-unshared Ollama control-server
startup receipt as a bounded runtime result, but do not treat it as Stage-A
author eligibility. The receipt explicitly showed that `llama-server` was not
mounted. Require a separate no-inference hash/provenance freeze and isolated
availability receipt for the exact runner closure before any author launch.
No request, model load, fixture, or sealed access occurred; v14 remains sealed.

**Evidence:**
`experiments/20260808T152658Z-frame-oracle-v14-runtime-closure-launch-receipt-r3/`.

# 2026-08-08 — Local runner identity does not establish runner closure

**Decision:** Treat the host runner at
`/home/openclaw/.local/lib/ollama/llama-server` with SHA-256
`dbfeea380cdc1de9bbfe32399befbcd8381a3c5ac83e573d79d0fa41bdc40037`
as the exact candidate for a later no-inference dependency-closure probe. Do
not infer isolated availability from file presence, and do not authorize Stage
A until its required libraries are frozen and an isolated availability receipt
passes. V14 remains sealed, unopened, and unconsumed.

**Evidence:**
`experiments/20260808T172358Z-frame-oracle-v14-runner-closure-probe/`.

# 2026-08-09 — Separate model readiness from Stage-A authoring

**Decision:** A successor may run at most one separately preregistered,
model-neutral ASCII-sentinel probe under
`docs/frame_oracle_v14_stage_a_model_readiness_gate_20260809.md`. The probe
must receive no Stage-A inputs or fixture material and must satisfy exact
model-load identity, one-request/one-response, isolation, receipt, and teardown
predicates. Its response is never fixture evidence. Even a `READY` result does
not establish independent authorship or authorize Stage A. Any discrepancy is
`NOT_READY` and cannot be repaired in place.

**Evidence:**
`experiments/20260809T012300Z-frame-oracle-v14-model-readiness-contract/`.

# 2026-08-09 — Freeze readiness request before any model invocation

**Decision:** The sole readiness probe permitted by the parent gate is the
exact 133-byte request with SHA-256
`60b30c2d270ec9093379f7ae0a507e31353d496b6db191c45d6787d602abf950`
and normalized sentinel `READY7K2`, under the immutable endpoint, timeout,
isolation, denial, loaded-model receipt, and teardown predicates in
`docs/frame_oracle_v14_model_readiness_probe_20260809.md`. Do not adapt or
retry it after output. Its response is transport evidence only. Even `READY`
does not authorize Stage A; any discrepancy consumes the probe as `NOT_READY`.

**Evidence:**
`experiments/20260809T032700Z-frame-oracle-v14-readiness-probe-preregistration-r2/`.

# 2026-08-09 — Retire the sole readiness probe on namespace failure

**Decision:** Adjudicate the exact preregistered probe `NOT_READY` and consume
it without repair or retry. The frozen unprivileged network namespace could
not raise loopback, and the failure preceded server launch, model load, HTTP
request, and response. Do not infer anything about generation readiness from
this environmental failure. Any later attempt requires a fresh preregistration
with transport feasibility handled before the one-use request. Stage A remains
blocked and v14 remains sealed.

**Evidence:**
`experiments/20260809T052300Z-frame-oracle-v14-readiness-probe-execution/`.

# 2026-08-09 — Require model-free transport feasibility before readiness

**Decision:** Do not spend another one-use model-readiness probe on an
unverified namespace topology. First require the identical intended topology
to pass a separately frozen, model-free inert HTTP exchange with complete
loopback, denial, request-count, response-hash, process, and teardown receipts.
Transport output cannot select or repair the topology and does not authorize
inference or Stage A. A changed topology requires a new contract.

**Evidence:**
`experiments/20260809T072900Z-frame-oracle-v14-transport-feasibility-contract-r2/`.

# 2026-08-09 — Reject the intended local readiness topology

**Decision:** Adjudicate the frozen model-free preflight
`TRANSPORT_INFEASIBLE`. The exact unprivileged network-unshared Bubblewrap
topology cannot raise loopback on this host, and failure preceded all server,
client, bind, request, and response activity. Do not repair or substitute a
topology based on this output, and do not preregister another model probe
against it. This is transport evidence only; Stage A remains blocked and v14
remains sealed.

**Evidence:**
`experiments/20260809T093000Z-frame-oracle-v14-transport-feasibility-execution/`.

# 2026-08-09 — Freeze exhaustive Stage-A unblock events

**Decision:** Stage A remains blocked unless one of exactly three independently
originating events occurs: an external conforming independent-author bundle, a
fresh result-independent topology proposal that first passes a model-free
preflight, or an explicit Ben-approved protocol revision. Do not tune, repair,
privilege, or substitute transport based on the observed loopback failure.
Finding another mechanism alone is not an unblock event. No event itself admits
Stage B, readout, substitution evaluation, or semantic loss.

**Evidence:**
`experiments/20260809T113028Z-frame-oracle-v14-stage-a-unblock-contract-r3/`.
