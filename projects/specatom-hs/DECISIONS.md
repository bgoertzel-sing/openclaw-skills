# Decision Log

## D-20260817-stage3-independent-validation-author: Separate plan authorship from implementation

- Date: `2026-08-17`
- Status: `accepted and implemented for Stage 3`
- Specification: revision 0.2, Stage 3

Validation-plan synthesis uses one provider-independent call whose canonical
request contains the exact reviewed source and strict contract/obligation
artifacts, never generated implementation bodies. Admission requires an exact
request hash, adapter provenance, reviewed-contract references, and immutable
Stage 2 ancestry. Review edits create new content-addressed plan bytes; review
records and approval decisions bind the exact resulting plan. Unresolved
critical meaning blocks approval, and upstream changes invalidate the complete
plan/review/approval chain.

This establishes role separation and reviewable plan provenance, not property
evidence. Stage 4 must implement the Hypothesis backend against approved plans.

## D-20260817-stage2-finite-contract-calculus: Execute only closed typed meaning

- Date: `2026-08-17`
- Status: `accepted and implemented for Stage 2`
- Specification: revision 0.2, Stage 2

Executable contract meaning is limited to
`plain2metta-contract-calculus/v1`: a finite typed JSON term language with
bounded quantifiers, explicit effects, trace/time semantics, approved
assumption references, and a declared execution-ownership locus. The
provider-free interpreter and canonical MeTTa projection first revalidate the
exact Stage 1 `SemanticContract` envelope and include its artifact ID and
content hash in their outputs. Free prose is never parsed as a predicate;
unknown meaning remains a typed hole and cannot execute or project.

This establishes deterministic reference semantics, not general semantic
equivalence. Stage 3 must synthesize and independently review strict validation
plans before Stage 4 generates property evidence or later formal-method stages
proceed.

## D-20260817-stage1-canonical-semantic-envelope: Bind semantic evidence to exact ancestry

- Date: `2026-08-17`
- Status: `accepted and implemented for Stage 1`
- Specification: revision 0.2, Stage 1

All Stage 1 semantic documents share the strict versioned envelope
`plain2metta-semantic-artifact/v1`. Their canonical identity covers the entire
document; provenance hashes must equal the exact ordered upstream references;
the current reviewed source is always the first reference; and project reload
revalidates document kind and ancestry against the immutable storage envelope.
Dedicated transition APIs, rather than generic artifact insertion, enforce
these rules. This preserves fail-closed migration behavior and makes upstream
byte changes transitively invalidate dependent semantic verdicts.

This decision does not claim general semantic equivalence. Stage 2 must still
define the finite typed calculus, reference interpreter, and canonical MeTTa
projection before higher validation stages may proceed.

## D-20260816-general-semantic-validation-r02: Implement the graded validation architecture

- Date: `2026-08-16`
- Status: `accepted as implementation direction; staged gates remain binding`
- Decision owner: Benjamin Goertzel
- Specification: `docs/plain2metta-general-semantic-validation-spec.tex`,
  revision 0.2

Ben directed the Plain2MeTTa coding agent to implement the revision 0.2
general semantic-validation architecture. The implementation uses Hypothesis
for generated properties and sequential state machines, TLA+/TLC initially for
concurrent and temporal models, Z3 through canonical SMT-LIB for bounded
logical obligations, Lean 4/Mathlib for the trusted semantic kernel and
selected durable proofs, and the existing Hyperon/Python runtimes for concrete
conformance evidence.

The coding-agent sequence and acceptance gates in the specification are
binding. Agents start at Stage 0 and may not skip prerequisite gates. This
decision authorizes task-branch implementation and draft-PR updates, not a
default-branch merge, release, public service exposure, system-wide dependency
changes, or paid compute.

## D-20260814-phase4-reviewed-inputs: Logical IR derives from reviewed snapshots

- Date: `2026-08-14`
- Status: `accepted; PDF-derived implementation invariant`
- Evidence: `experiments/20260814T130310Z-plain2metta-v2-phase4-reviewed-inputs/RUN.md`

Phase 4 logical-IR artifacts use the exact paired Phase 3 reviewed snapshot
refs as their direct upstream provenance. Approval records on Phase 2
elaborated/test artifacts are necessary to create those snapshots but are not
an alternative Phase 4 admission path. This preserves reviewer edits as the
actual logical-IR input and makes source/review invalidation transitively remove
the logical IR. Strict reload rejects artifacts rebound to the Phase 2 refs.

## D-20260814-plain2metta-v2-persistent-worker: Retarget worker to revised logical IR

- Date: `2026-08-14`
- Status: `accepted; Ben-directed correction`
- Decision owner: Benjamin Goertzel

Retire the completed Monday-playground milestone from the Plain2MeTTa worker's
active instructions. The worker must implement the revised logical-IR design
in `projects/omegaclaw/workspace/plain2metta-spec-v2-revised-logical-ir.pdf`
(SHA-256
`10969aabb39d4de057ca06cce151b780c07b381802a079f411814826665b2c4c`),
starting with the immutable project/artifact/version model, provenance hashes,
explicit approval state, and invalidation after upstream source changes.

Use a persistent named session with `openai/gpt-5.6-sol`/high and a five-minute
continuation cadence. Preserve the existing compiler and 144-commit-ahead
history, work on an isolated task branch/worktree, record reproducible evidence,
and do not push, merge, rewrite history, or use paid compute without explicit
authorization. Urgency means advancing multiple safe gates per turn, not
weakening tests, provenance, or branch isolation.


## D-20260726-no-whitespace-object-subtargets: Reject interior whitespace

- Date: `2026-07-26`
- Status: `accepted`
- Related task/run: `projects/specatom-hs/TASKS.md` 11:30 PDT entry

### Decision

Object-scoped validation subtargets reject all whitespace code points,
including interior ASCII and Unicode whitespace. Crisp validation, PeTTa
export, and diagnostics share this fail-closed rule; the compiler does not
normalize whitespace-bearing identities into different targets.

## D-20260725-unassigned-object-subtargets: Reject unassigned Unicode code points

- Date: `2026-07-25`
- Status: `accepted`
- Related task/run: `projects/specatom-hs/TASKS.md` 23:30 PDT entry

### Decision

Object-scoped validation subtargets reject Unicode general category `Cn`.
An unassigned code point can acquire semantics under a later Unicode database,
so accepting it would make stable validation identity dependent on runtime
Unicode version. Crisp validation, PeTTa export, and diagnostics share this
fail-closed rule.

## D-20260724-canonical-object-subtargets: Require unpadded object-scoped validation subtargets

- Date: `2026-07-24`
- Status: `accepted`
- Related task/run/commit: `projects/specatom-hs/TASKS.md` 21:30 PDT entry

### Decision

Treat leading or trailing whitespace in the suffix after a declared semantic
object ID and colon as an invalid object-scoped validation target. Reject it
in crisp validation and suppress the obligation and linked checks from PeTTa
export and diagnostics rather than silently normalizing or reifying an
ambiguous identity.

## D-20260629-separate-specatom-project: Track SpecAtom-HS compiler as its own software project

- Date: `2026-06-29`
- Status: `accepted`
- Decision owner: subagent implementation support, pending Benjamin review
- Related task/run/commit: `projects/specatom-hs/PROJECT.md`

### Context

The existing `hyperseed-formalizations` project contains design notes about Plain-to-MeTTa/PeTTa/Rholang and Hyperseed-compatible specification IRs. Benjamin uploaded a detailed revised SpecAtom-HS design paper and requested a subagent implementation lane. The work is now expected to become a compiler/prototype with tests, passes, target profiles, and validation checks, not only a LaTeX formalization note.

### Decision

Create a separate local project notebook `projects/specatom-hs/` for the Plain-to-MeTTa / SpecAtom-HS compiler implementation lane. Reuse `hyperseed-formalizations` as design context and provenance, but do not put software-project task tracking solely in that formalization notebook.

### Alternatives considered

- Continue tracking everything under `hyperseed-formalizations`.
- Create a remote GitHub repository immediately.
- Modify the existing untracked `papers/0005`/tracked `papers/0006` notes directly as the first implementation step.

### Rationale and evidence

The revised PDF includes coding-agent appendices, schema atoms, compiler passes, validation invariants, repository structure, JSON shape, bridge table, diagnostics, and implementation contracts. That is broader than a paper note and merits independent project state. The task constraints also forbid remote creation/push for this lane.

### Consequences

A local implementation repo can be created under `projects/specatom-hs/repos/` in a later step. Project records can track source summary, decisions, tasks, and validation experiments without cluttering the formalization-paper repo.

### Revisit trigger

Revisit if Benjamin prefers the implementation to live directly in `hyperseed-formalizations`, or if a different repository name/visibility is chosen.

### Supersedes or superseded by

Complements prior design notes 0005 and 0006 in `hyperseed-formalizations`.
Its local-only repository/name/visibility uncertainty was superseded by
`D-20260715-plain2metta-public-name`: the authoritative remote is public
`bgoertzel-sing/plain2metta`, while this separate project notebook and the
internal `specatom_hs` package/IR remain in force.

## D-20260629-python-stdlib-mvp: Start with source-preserving Python stdlib prototype

- Date: `2026-06-29`
- Status: `accepted`
- Related repo: `projects/specatom-hs/repos/specatom-hs`

### Context

Appendices A-H and J-N require staged compilation, deterministic IDs, source provenance, exactly-one primary role, context/TV assertions for heuristic claims, questions for unknowns, and validation records before backend lowering.

### Decision

Implement the first MVP as a local-only Python standard-library package, emitting JSON and MeTTa-ish S-expressions. Do not generate executable code, lower to Rholang, or push/create a remote repository.

### Rationale

The stdlib implementation is inspectable, cheap to run, and adequate for parser/indexer/IR/validator progress. It keeps claims conservative and avoids premature dependency or target-runtime coupling.

### Consequences

The prototype is not a complete Plain grammar, not a full English semantics parser, and not a finalized PeTTa backend. It is a tested scaffold for source-preserving IR and validator work.

## D-20260702-freeze-v01-target-profile: Freeze v0.1 target profile

- Date: `2026-07-02`
- Status: `accepted`
- Related repo/docs: `projects/specatom-hs/repos/specatom-hs/docs/v01-profile.md`, `projects/specatom-hs/repos/specatom-hs/docs/validator-gap-audit.md`

### Context

The prototype now has a coherent v0.1 scaffold: source indexing with byte/line provenance and digests, concept extraction and occurrence spans, requirement/test coverage with document-scoped labels, structural validators, PeTTa reified profile filtering, and explicit Unknown/question behavior for unsupported profile gaps. Continuing to add schema surface before documenting the demo target risks endless growth and unclear success criteria.

### Decision

Freeze the v0.1 target profile as a conservative Plain-like input to SpecAtom-HS JSON plus PeTTa reified atoms and diagnostics. v0.1 supports source provenance, concepts, requirements/acceptance tests/coverage labels, current structural validation, PeTTa reified profile-filtered emission, validation rationales/evidence, and refusals for RawTextOnly, unsupported predicates, malformed arity, subject mismatches, and executable skeletons.

### Deferred beyond v0.1

Do not claim support for full Plain grammar, deep English semantics, executable code skeleton generation, SUMO/EXPO/Hyperseed bridge tables, PLN confidence propagation, Rholang profiles, MeTTa-IL, information-flow/temporal validation, Phase 2 objects (`Scope`, `EpistemicStatus`, `Evidence`, `Interpretation`, `Bridge`), or Phase 3 facets (witnesses/backend artifacts, process/resource placeholders, revisions).

### Rationale

Freezing v0.1 avoids endless schema growth and creates a coherent demo deliverable: given a Plain-like input with concepts, requirements, acceptance tests, and at least one intentional gap, the compiler should emit SpecAtom-HS JSON, PeTTa reified `.metta` atoms, and auditable Pass/Fail/Unknown diagnostics without hallucinated executable semantics.

### Consequences

v0.2 work should be chosen from the documented gap audit, with highest priority on methodology validation, information-flow/temporal availability checks, and security/privacy obligation scaffolding.

## D-20260707-proceed-to-phase2-semantic-objects: Pivot SpecAtom-HS next work to Phase 2 semantic objects

- Date: `2026-07-07`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run: `projects/specatom-hs/TASKS.md`; Telegram reply to daily reflection item 5

### Context

The v0.2 information-flow validation lane had been deepened through graph extraction, source/sink/reachability, cycles, redundant paths, temporal consistency, dependency depth, bottlenecks, graph summaries, and exact edge provenance. The daily reflection noted that recurring workers kept restating the fork between further information-flow validation and beginning Phase 2 semantic objects.

### Decision

Proceed to Phase 2 semantic objects next. Prioritize a small, tested first slice for `Scope`, `EpistemicStatus`, `Evidence`, `Interpretation`, and `Bridge` records, preserving the existing conservative behavior: no invented executable semantics, stable IDs, source provenance, validation obligations/checks, and profile-aware backend emission/refusal.

### Rationale

Ben explicitly chose the Phase 2 semantic-object direction on 2026-07-07. The information-flow validator is now broad enough to serve as a substrate; Phase 2 objects should make later methodology/security/information-flow checks less ad hoc by representing scope, evidence, interpretations, and bridge mappings directly.

### Consequences

Recurring SpecAtom-HS work should stop treating information-flow deepening vs Phase 2 as an open decision. Further information-flow checks are still allowed when needed, but the top priority is implementing semantic-object infrastructure and regression tests.

## D-20260715-plain2metta-public-name: Publish as Plain2Metta

- Date: `2026-07-15`
- Status: `accepted and implemented`
- Decision owner: Benjamin Goertzel
- Remote: `https://github.com/bgoertzel-sing/plain2metta`

Rename the existing `bgoertzel-sing/specatom-hs` remote to the public-facing
repository name `plain2metta` and make it public. Preserve the technical
`specatom_hs` package and intermediate-representation name; do not create a
duplicate repository or perform a package-wide semantic rename. Update public
branding through a task branch/draft PR rather than pushing directly to the
default branch.

## D-20260817-stage4-hypothesis-evidence: Admit bounded property evidence

- Status: accepted and implemented
- Decision: Hypothesis results are admissible only from canonical modules
  bound to an exactly approved plan and complete source/contract/obligation/
  review ancestry. Passing exit status cannot conceal mismatched observations;
  failures persist immutable replayable counterexamples rather than partial
  state. The evidence is bounded, not a proof of unrestricted semantics.

## D-20260817-stage5-tlc-evidence: Admit bounded finite-state evidence

- Status: accepted and implemented
- Decision: TLC evidence is admissible only from canonical TLA+ bundles bound
  to an exactly approved validation plan and its complete reviewed ancestry.
  Release/engine/JRE/JAR and module/config/source-map hashes, finite scope,
  workers, state-space metrics, fairness, symmetry, liveness mode, deadlock
  policy, bounds, and replay command are mandatory. Tool errors never become
  counterexamples, and a successful exit cannot override contradictory data.
  This is bounded evidence, not a proof beyond the recorded model.

## D-20260817-stage6-smt-evidence: Admit exact canonical solver evidence

- Status: accepted and implemented
- Decision: Z3 evidence is admissible only from canonical SMT-LIB formulas
  lowered from an exactly approved plan and complete reviewed ancestry. Exact
  formula, declaration/source map, logic, options, bounds, executable/version
  hashes, replay command, and a matching model or unsat core are mandatory;
  requested supported proofs are mandatory. Unknown, timeout, exhaustion,
  unsupported meaning, or any provenance/hash mismatch fails closed. Results
  establish only the recorded bounded formula, not unrestricted semantics.

## D-20260817-stage11-release-acceptance: Accept bounded revision-0.2 implementation

- Status: accepted and implemented
- Decision: mark the implementation objective complete only after the focused
  threat matrix, full baseline, pinned backends, clean-checkout replay,
  browser/API authorization, immutable downloads, live examples, mutation
  corpus, trace reconstruction, and repository audits pass.
- Boundary: acceptance covers exact-ancestry G0--G6 behavior under recorded
  bounds; it does not authorize merge/release or claim arbitrary correctness.

## D-20260817-stage7-lean-kernel: Admit kernel-checked Lean evidence

- Status: accepted and implemented
- Decision: admit Lean evidence only when the fixed semantic-kernel package,
  theorem/source map, exact approved ancestry, Lean/Lake hashes, Mathlib
  revision, imports, bounds, build command, and kernel result match. `sorry`,
  new axioms, unsafe/native trust, unresolved meaning, and forged or stale
  results fail closed. TLC/Z3 evidence is never relabeled as a Lean proof.
# 2026-08-16 — Evaluation before documentation

**Decision:** prioritize the extended v2 web UI and actual executable
MeTTa/Python examples through the logical IR before preparing a design PDF.

**Sequence:** working UI and end-to-end examples; Ben's hands-on inspection and
iteration; stabilized PDF; frontier-model review and incorporation; then human
MeTTa-developer feedback.

**Rationale:** documentation and external review should describe observed,
usable behavior rather than prematurely freeze an interface or architecture.
## 2026-08-17 — Stage 8 verdicts compose evidence conservatively

Approved exact-ancestry validation plans are the sole source of dual-runtime cases and independent expected observations. Runtime evidence is append-only across independent tools but remains transitively invalidated by upstream changes. Per-obligation G0--G6 vectors require all declared evidence; divergence, wrong output, inconclusive execution, missing proof, and unresolved meaning map fail-closed to Fail, Unknown, or Blocked.

## 2026-08-17 — Stage 9 API authority remains narrow

Semantic metadata reads expose exact identities and ancestry, while commands
and immutable artifact bodies require an injected authorization policy. JSON
commands are bounded and duplicate-rejecting. Provider and executor authority
is injected; the browser cannot supply credentials or arbitrary commands.
G0--G6 remain distinct evidence grades and unsupported input is never promoted.

## 2026-08-17 — Stage 10 mutation confidence is scoped

Mutation score is evidence only about the categorized corpus: all eight
relevant semantic mutants must be killed, while cosmetic survivors require
explicit review. It is not a general correctness probability. Policy-dependent
input remains Blocked, and examples retain source, contract, validation, and
obligation data rather than exact-source code branches.
