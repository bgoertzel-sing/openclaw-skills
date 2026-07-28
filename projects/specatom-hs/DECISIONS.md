# Decision Log

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
