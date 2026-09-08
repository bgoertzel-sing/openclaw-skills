# OmegaClaw clean-install pivot acceptance

Status: frozen before clean-install execution on 2026-08-13 22:46 PDT.

## Safety boundary

- Production supervisors, receivers, and Telegram identities remain stopped.
- The clean layout is outside `projects/omegaclaw/repos/PeTTa` and does not
  reuse its SWI-Prolog, environment, Git metadata, or mutable state.
- Every launch uses an allowlisted environment and fails before execution if
  any Telegram/token variable is present. Chroma and runtime paths are fresh,
  staging-only, identity-specific paths.
- No source production Chroma/state path is attached. Compatibility work uses
  ordinary recoverable copies, then disposable copies of those copies.
- The custom private-canary, deferred-job, synchronous file-bridge provider,
  phase5/phase6 case, acceptance-controller, and nested-supervisor stack is
  excluded.

## Repository and installation gate

- Fresh isolated PeTTa root; PeTTa is exactly `v1.0.4`, OmegaClaw-Core is
  exactly `2cdef059fe06d13e1fea7ea23b49825cb530c5b8`, and the exact resolved
  `petta_lib_chromadb` commit is recorded.
- README, CI, manifests, channel/loop, mock facilities, official asynchronous
  OpenClaw plugin, and Chroma code are read before changes.
- Because Docker is absent and sudo is not authorized, execute the documented
  non-Docker manual/mock path. Record this honestly as a deviation from the
  Docker smoke; do not claim Docker/CI equivalence.
- SWI-Prolog 10.x and Python dependencies are isolated under the fresh root.

## Ordinary-conversation gate

The provider and channel are deterministic local mocks. A run passes only if:

1. Three sequential messages in one session receive three correlated replies
   in order, and replies demonstrate retained turn context.
2. From an empty/idle queue, a newly injected message is acquired and replied
   to without a prior wake-up message.
3. An injected provider error and an injected provider stall each produce a
   correlated visible terminal error within the configured timeout plus two
   seconds; neither blocks the next ordinary message.
4. After controlled shutdown and restart, a new message succeeds and the
   intended persisted conversation state is retained.
5. At least eight messages split across two concurrent sessions all receive
   exactly one reply routed to the originating session, with no cross-session
   content leakage.
6. After every shutdown, within five seconds there are zero descendants or
   orphaned PeTTa/SWI/Python workers attributable to the run. A PID alone is
   never acceptance.

Raw ingress IDs, session IDs, provider/action records, replies, timestamps,
process trees, exit statuses, and exact commands are evidence. Any missing
correlation or silent timeout fails the gate.

## Three-configuration gate

Protomega, ProtoCosmo2, and Protomega2 use the same immutable code commit but
distinct config, state, Chroma, queue/cursor, session, log, attachment, and PID
roots. A preflight compares canonical paths and device/inode identities and
fails on overlap. Each configuration independently passes a two-turn local
mock exchange and clean shutdown. No Telegram configuration is present.

## Asset gates

- Protomega first: hash the source read-only, make a recoverable copy, verify
  the copy hash, and probe only a disposable derivative. Record schema,
  collection, dimension, embedding identity, counts, and exact known-query
  recall. If incompatible, specify a one-way source-copy-to-new-store migration
  with item/count/hash reconciliation and rollback before implementation.
- ProtoCosmo2 second: inventory each curated skill and classify KEEP,
  REIMPLEMENT, or DROP with dependency evidence. The excluded broken-runtime
  components default to DROP.
- Protomega2 last: rebuild cleanly with no assumption that legacy state is
  valuable.

## Completion boundary

After an autonomous soak and independent Fable end review, record rollback,
clean local commits, and a secret scan. Stop before production. Only Ben's
subsequent explicit cutover authorization permits deployment; fresh correlated
external-channel evidence is still required after an authorized cutover.
