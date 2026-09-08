# The core motivation

Yes: **context management is the strongest first integration point for AtomSpaces**.

The precise motivation, though, should not be “give the agent a graph memory.” It should be:

> **Use an AtomSpace as the shared semantic control plane through which context, memory, inference, pattern mining, attention, and multiple agents can exchange structured evidence.**

In the Ben Goertzel sense, the important property is cognitive synergy: several cognitive processes operate over a common metagraph and can pass partially processed structures to one another. AtomSpace-style systems support variable-binding graph queries, substitution, and observable add/remove/replace events—not merely vector similarity over text chunks. ([GitHub][1])

The shortest test for whether AtomSpace is earning its complexity is:

> “What files were touched recently?” does not need an AtomSpace.
> “Which recently touched files define symbols implicated by an unresolved failure, are governed by a nested instruction, have changed since the agent read them, and support or contradict the current plan?” does.

That second question is a **relational join across time, code, instructions, observations, provenance, and goals**. It is exactly where pattern matching over an AtomSpace can outperform flat recency lists, keyword search, and vector retrieval.

The hard architectural judgment is equally important:

> **The AtomSpace should select and explain evidence. It should not become an oracle that chooses the agent’s next action.**

That preserves the LLM’s deliberative strength while giving it much better grounded context.

# What OpenCode and Codex currently do

## OpenCode

OpenCode’s current architecture already has an excellent insertion seam. It models privileged model context as independently refreshable typed sources. Each source has a stable key, codec, loader, baseline renderer, update renderer, and optional removal renderer. The admitted values are represented by durable snapshots, changes are reconciled at safe provider-turn boundaries, and compaction starts a new context epoch with a fresh baseline. Temporary source failure preserves the previously admitted value rather than silently erasing it. ([GitHub][2])

That is almost exactly the host interface required for an AtomSpace-derived semantic working set.

OpenCode’s older session path also tracks which instruction files have entered history and, when reading a file, walks upward to discover nearby `AGENTS.md`, `CLAUDE.md`, or related instructions that have not already been attached. The newer architecture describes durable nested instruction discovery as further work. Its compactor creates a structured continuation summary containing the objective, important details, completed/active/blocked work, next move, and relevant files, while retaining a recent raw tail under a token budget. ([GitHub][3])

In the OpenCode source I inspected, I did **not** find a model-visible semantic “recent files” selector. Its closest mechanisms are explicit file-read/tool history, path-local instruction discovery, and the `Relevant Files` field produced during compaction. That means its snapshot/diff infrastructure is sophisticated, but the content selected into those snapshots is not yet a relational working set.

## Codex

Codex has converged on a closely related architecture. Its `ContextManager` maintains versioned chronological history and baselines for model-visible world state. `WorldState` consists of typed sections with stable identifiers, typed snapshots, and section-specific diff renderers; persisted snapshots can be advanced with merge patches. Its existing sections cover such things as environments, permissions, model state, tools, applications, collaboration mode, personality, instructions, and realtime state. ([GitHub][4])

Codex discovers project instructions hierarchically from project root to current working directory, with nearer files supplementing or overriding broader project context. It also supports bounded loading and multiple selected environments. ([GitHub][5])

Codex’s newer startup-context mechanism is especially relevant. It creates bounded sections for:

* recent turns from the current thread;
* recent work grouped by repository or directory;
* recent first-user requests and branch/activity metadata;
* a shallow machine and workspace tree.

The implementation deliberately bounds thread count, group count, tree depth, entries per directory, and token allocation. This is useful recency-oriented context, but it is largely driven by timestamps, thread grouping, user-request text, and directory structure—not by semantic relationships among errors, symbols, tests, instructions, decisions, and file versions. ([GitHub][6])

Codex also now has a cross-thread memory pipeline when the feature is enabled. Phase 1 extracts structured memories from eligible recent rollouts; Phase 2 globally consolidates selected outputs into memory artifacts, using usage counts, recent use or generation time, workspace diffs, and a restricted consolidation agent.

Its memory read path tells the model to inspect an injected summary, keyword-search `MEMORY.md`, and then open one or two directly relevant rollout summaries or skills. That is disciplined and bounded, but still fundamentally **registry-and-file navigation**. An AtomSpace could make the retrieval relational while retaining Codex’s valuable freshness, evidence, bounded-search, and citation disciplines.

My synthesis is:

| Need                   | OpenCode                                    | Codex                                              | AtomSpace contribution                                                       |
| ---------------------- | ------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------- |
| Durable chronology     | Session history                             | Versioned response history                         | Keep unchanged as source of truth                                            |
| Ambient changing state | Typed `SystemContext` sources               | Typed `WorldState` sections                        | Supply a semantic working-set section                                        |
| Instructions           | Path hierarchy and read-triggered discovery | Root-to-CWD hierarchy                              | Relate instructions to files, symbols, tasks, and inferred scope             |
| Recent work            | Explicit reads and recent tail              | Recent threads, requests, branches, workspace tree | Replace pure recency with task-relative graph patterns                       |
| Compaction             | Structured summary plus recent tail         | Replacement summary and context reinjection        | Preserve facts and provenance independently of prose summary                 |
| Cross-session memory   | Limited equivalent in inspected path        | Two-stage extracted/consolidated memory            | Query claims, episodes, evidence, contradictions, and supersessions directly |

# Recommended architecture

The AtomSpace should be a **materialized semantic view**, not the authoritative record.

```text
filesystem / git / LSP / tests / shell / tools / sessions / agents
                              │
                              ▼
                immutable append-only event journal
                    source of truth and audit
                              │
                        atomizer/indexer
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
      project AtomSpace                 session/branch overlay
      durable knowledge                 volatile working state
             └────────────────┬────────────────┘
                              │
        seeds: user request, active tasks, current diff,
        unresolved failures, recently touched symbols
                              │
             pattern queries + bounded graph expansion
             + optional lexical/vector candidate seeding
                              │
       hard filters: ACL, scope, freshness, existence,
       source validity, permission, privacy classification
                              │
       diversity-aware packing under a token budget
                              │
                    ContextBundle snapshot
           atoms + hashes + evidence + reasons + omissions
                              │
          OpenCode SystemContext / Codex WorldState
                              │
                              ▼
                             LLM
```

The event journal remains replayable and authoritative. Files remain files. Git remains the authority on versions. Test results remain test events. Conversation history remains chronological. The AtomSpace indexes and relates those sources so that context can be selected by patterns.

A project should have two principal spaces:

1. A **durable project space** containing files, symbols, instructions, commits, recurring decisions, established claims, capabilities, and cross-session episodes.
2. A **session or branch overlay** containing the present task, current reads, edits, failures, tentative hypotheses, tool calls, and temporary salience.

The overlay can be discarded, merged, or checkpointed. A context epoch or git commit can correspond to an AtomSpace frame or snapshot identifier.

# A minimal atom vocabulary

Do not start with a grand ontology. Approximately 12–16 node classes and 20–30 relations are enough.

Useful node classes are:

`Agent`, `Session`, `Turn`, `Task`, `Goal`, `File`, `Symbol`, `Commit`, `Instruction`, `ToolCall`, `Observation`, `Claim`, `Decision`, `Error`, `TestRun`, `Capability`, `ContextBundle`, and `Summary`.

Useful relations include:

`MentionedIn`, `ReadAt`, `EditedAt`, `ProducedBy`, `DerivedFrom`, `Defines`, `Calls`, `Imports`, `DependsOn`, `Blocks`, `Supports`, `Contradicts`, `Supersedes`, `VerifiedBy`, `GovernedBy`, `AppliesTo`, `RelevantTo`, `RequiredFor`, `RequiresCapability`, `AuthorizedBy`, `ActiveIn`, `Before`, `After`, and `PartOf`.

Each evidential atom should carry or reference:

* an immutable event identifier;
* path, commit, content hash, and line range where applicable;
* observed time and validity interval;
* source type;
* project/session scope;
* privacy classification;
* verification state;
* confidence, when probabilistic;
* token cost for rendering.

Crucially, use distinct claim states such as:

```text
SelfReported
Observed
Derived
ExternallyVerified
FormallyVerified
Superseded
```

A timestamp written by an agent must not be silently promoted into “verified.” Your transcript already caught this exact epistemic error: “most recently verified” was corrected to “last self-reported check.” 

# Context retrieval patterns

The most valuable first patterns are not exotic reasoning. They are the mundane joins coding agents repeatedly approximate badly.

The following is schematic MeTTa-like notation, not a promise of exact parser syntax.

## 1. File changed since the agent read it

```lisp
(, (ReadVersion $agent $file $oldHash $readTime)
   (CurrentVersion $file $newHash $now)
   (RelevantTo $file $activeTask)
   (!= $oldHash $newHash))
=>
(ContextWarning
  (StaleRead $file $oldHash $newHash)))
```

This is far better than merely showing “recently modified files.” It tells the model which of its own assumptions may now be stale.

## 2. Unresolved error to symbol to file

```lisp
(, (Produced $run $error)
   (Unresolved $error)
   (MentionsSymbol $error $symbol)
   (DefinedIn $symbol $file)
   (RelevantTo $run $activeTask))
=>
(ContextCandidate
  (FailureNeighborhood $error $symbol $file)))
```

Expansion can then find callers, affected tests, recent edits, and instructions governing the file.

## 3. Applicable nested instruction

```lisp
(, (Touches $task $file)
   (ScopedTo $instruction $directory)
   (AncestorOf $directory $file)
   (Active $task))
=>
(ContextCandidate
  (ApplicableInstruction $instruction $file)))
```

This generalizes path-local `AGENTS.md` discovery. An instruction may also apply because it governs a symbol class, language, proof directory, generated code, or security-sensitive operation—not only because it sits in an ancestor directory.

## 4. A summary contradicted by newer evidence

```lisp
(, (Claims $summary $proposition)
   (Contradicts $observation $proposition)
   (After $observation $summary))
=>
(ContextUpdate
  (SupersedeClaim $proposition $observation)))
```

The agent receives an explicit correction instead of carrying a stale prose summary through subsequent compactions.

## 5. Impact context around an edit

```lisp
(, (Editing $task $symbol)
   (Calls $caller $symbol)
   (DefinedIn $caller $callerFile)
   (CoveredBy $test $caller))
=>
(ContextCandidate
  (ImpactPath $symbol $caller $callerFile $test)))
```

## 6. Cross-agent collision

```lisp
(, (WorkingOn $agent1 $task1)
   (WorkingOn $agent2 $task2)
   (Touches $task1 $file)
   (Touches $task2 $file)
   (!= $agent1 $agent2))
=>
(CoordinationWarning
  (ConcurrentFileInterest $file $agent1 $agent2)))
```

This need not lock the file automatically. It can tell each agent what the other is doing and suggest a lease, worktree split, or explicit synchronization point.

# “Recent files” should become “the current semantic working set”

A good working set should include files because one or more explicit reasons apply:

1. The user named the file, symbol, module, or concept.
2. The agent read or edited it during the current task.
3. It changed since the last read.
4. A current error, stack trace, theorem failure, or test mentions it.
5. It defines, calls, imports, or tests a symbol currently under consideration.
6. A relevant instruction applies to it.
7. It supports or contradicts an active decision or hypothesis.
8. It changed on the current branch since the context epoch began.
9. Another agent is modifying a dependency or overlapping region.
10. The user pinned it.

Modification time can be one feature, but not the organizing principle.

Candidate retrieval should combine three mechanisms:

* exact retrieval from paths, symbols, hashes, error text, and identifiers;
* AtomSpace pattern matching and one-to-three-hop relational expansion;
* embeddings as a **candidate generator**, not the final authority.

The resulting candidates should pass hard scope, freshness, permission, and privacy filters. Then they can be packed under the token budget using relevance, unresolvedness, evidential reliability, recency, novelty, user pins, dependency position, and token cost. A diversity constraint should prevent twelve near-duplicate facts from consuming the budget.

Every rendered item should include a compact explanation:

```text
Included:
src/goals.py:203–250

Why:
- implements active goal ranking;
- changed after last model read;
- implicated by attention-collapse observation;
- supports unresolved invariant obligation.

Evidence:
event 01K...; commit abc123; content hash sha256:...
```

The retrieval itself becomes auditable. A `ContextBundle` atom records the seeds, query version, selected atoms, score components, source hashes, omissions, and token budget.

# Do not repeat the STI failure

The existing attention mechanism gives a strong negative specification for the AtomSpace design.

The source review found that STI normalization only scales values downward when the total exceeds the budget. It never restores a depleted total, so the “budget” is merely a ceiling and the economy can collapse toward zero. LTI only rises, while culling requires low STI **and** low LTI, meaning sufficiently old goals can become irrelevant to ranking yet permanently immune to culling. 

You also correctly rejected computing a privileged “Next Move” from that collapsed ranking: it manufactures authority the signal has not earned. 

This aligns with a broader warning. The classic ECAN implementation is now unmaintained, and current AtomSpace commentary explicitly questions the micromanagement implied by assigning attention to every individual atom, suggesting hierarchical or block-level attention instead. ([OpenCog Wiki][7])

For the agent integration, attention should therefore operate primarily on:

* task clusters;
* failure neighborhoods;
* context bundles;
* episodes;
* computational processes;
* coherent subgraphs.

It should obey these invariants:

1. **Named stimulus:** every positive activation has a source such as user mention, edit, test failure, contradiction, tool result, dependency activation, deadline, or explicit pin.
2. **Explicit budget semantics:** either activation mass is genuinely conserved, or unused capacity is explicitly represented as idle capacity. No accidental one-sided normalization.
3. **No decay-only terminal dynamics:** a system whose only persistent operation is decay must not be called an economy.
4. **No floor tie wall:** rounding or clamping must not turn most candidates into an arbitrary equal-valued mass.
5. **Retention must be reversible:** long-term importance must decay, be challenged, or be separately garbage-collected; it must not permanently defeat culling.
6. **Multiple dimensions remain visible:** relevance, freshness, reliability, unresolvedness, novelty, and token cost should not be prematurely collapsed into one mysterious scalar.
7. **Attention allocates context and computation, not action authority:** it proposes what the LLM or GoalEvaluator should inspect.
8. **Exploration is reserved:** a small fraction of retrieval or compute should go to diverse, weakly activated candidates so established salience cannot form a closed loop.

A scalar may eventually be used for token-budget packing, but the component vector and derivation should remain inspectable.

# Exact OpenCode integration

Add a source analogous to:

```ts
type SemanticWorkingSetSnapshot = {
  frameID: string
  queryVersion: string
  seedAtomIDs: string[]
  selected: Array<{
    atomID: string
    contentHash: string
    reasonHash: string
    sourceEventIDs: string[]
  }>
  tokenBudget: number
}
```

Register it as something like:

```text
agent/semantic-working-set
```

Its loader performs the bounded AtomSpace query. Its baseline renderer emits the full current bundle. Its update renderer emits additions, removals, changed evidence, stale-read warnings, and supersessions. Its removal renderer states that the semantic working set no longer applies.

Most importantly, AtomSpace unavailability should map to OpenCode’s **unavailable** state, preserving the previously admitted snapshot. It must not be interpreted as “all previous semantic context has ceased to be true.”

At compaction or another context-epoch transition, recompute a full bundle from the current graph and make it part of the fresh baseline. Ordinary changes should be admitted as chronological deltas only at safe provider-turn boundaries.

Before automatic injection, expose the same machinery as read-only tools:

```text
context.query
context.explain
context.diff
context.pin
context.unpin
```

That allows shadow evaluation without modifying model behavior.

# Exact Codex integration

Codex can receive the same snapshot as an extension world-state section:

```text
semantic_working_set
```

The section’s `snapshot()` returns the selected atom identifiers, hashes, query version, frame, and budget. Its `render_diff()` returns a compact model-visible fragment describing additions, removals, changed evidence, and corrections.

This naturally plugs into Codex’s existing world-state baseline and merge-patch behavior. Rollback or compaction should clear or replace the semantic baseline in the same situations where Codex already forces a full world-state reinjection.

The realtime startup context should become one set of **seeds**, not the final context:

* recent thread requests seed task and concept atoms;
* current branch and repository seed project atoms;
* workspace trees seed file and directory atoms;
* current-thread turns seed active claims, decisions, and unresolved questions.

The AtomSpace then asks which portions of that recent activity are actually connected to the present request.

Similarly, Codex’s consolidated memory files can become cached human-readable projections of a structured space. A memory lookup would become:

1. Seed from the current task.
2. Query relevant claims, decisions, commands, failures, and episodes.
3. Expand to supporting or contradictory evidence.
4. Open only the one or two source rollouts needed for exact verification.
5. Record which atoms and episodes were useful.

This preserves Codex’s bounded evidence lookup while replacing brittle keyword navigation with structured retrieval.

# Implementation in the PeTTaClaw stack

Given the existing stack, the fastest credible implementation is:

```text
Python event adapters
    ↓
PeTTa project/session spaces
    ↓
MORK-backed exact/pattern storage where useful
FAISS-backed embedding space for candidate seeding
    ↓
MeTTa/Prolog relational queries
    ↓
Python ContextBundle renderer
    ↓
agent prompt/context adapter
```

PeTTa already advertises Python interoperability through Janus and optional MORK-backed AtomSpaces and FAISS-backed atom-vector spaces, so the hybrid exact-pattern-plus-vector architecture does not require inventing an entirely separate retrieval stack.  ([GitHub][8])

A minimal broker API would be:

```text
observe(event) -> EventID
assert(atom, provenance, scope) -> AtomID
supersede(oldAtom, newAtom, reason) -> AtomID
query(pattern, seeds, asOf, budget, acl) -> Candidate[]
bundle(candidates, tokenBudget, diversityPolicy) -> ContextBundle
explain(atomOrBundle) -> ProvenancePath[]
snapshot() -> FrameID
diff(frameA, frameB) -> ChangeSet
pin(atom, scope)
unpin(atom, scope)
```

The LLM should not receive arbitrary executable access to the whole AtomSpace. It receives bounded, permission-checked query and explanation capabilities.

# Compaction becomes safer

Today, prose compaction can accidentally become the only surviving representation of an earlier fact. AtomSpace allows a better division:

1. Before compaction, atomize durable claims, decisions, errors, obligations, relevant files, and evidence links.
2. Generate the prose summary as a projection of those atoms plus recent conversation.
3. Link every summary claim to source event atoms.
4. Retain a recent raw conversation tail.
5. After compaction, regenerate the semantic working set from the graph rather than trusting the summary as an unexamined truth source.
6. When new evidence contradicts a summary claim, emit a supersession delta.

This does not require storing every token forever in prompt context. The raw event journal remains outside the prompt; only provenance identifiers and selected evidence enter the bundle.

# Later integration: goals and capabilities

Once context retrieval is demonstrably useful, the same substrate can support two further agent functions.

First, the goal evaluator can ask relational questions:

```text
Which active obligations lack evidence?
Which goal depends on an unresolved blocker?
Which claimed completion has no verifier event?
Which tasks share a file or capability?
Which goal assumptions were superseded?
```

It should return an **obligation view**, not an unearned next-action ranking.

Second, a typed capability broker can relate:

```text
Task
RequiresCapability
Capability
AuthorizedBy
Permission
AvailableInEnvironment
```

A tool can be offered or called only when the relevant pattern succeeds. The AtomSpace provides relational policy state; the ordinary permission system remains the enforcement boundary.

# What Lean should certify

Lean should not attempt to prove that the AtomSpace “understands” the project. It should certify the runtime bridge properties that matter.

Good initial theorems are:

```text
bundle_sound:
  every rendered context item has an admitted provenance event

acl_sound:
  every rendered item is permitted in the current agent/project scope

verification_sound:
  a self-report cannot become Verified without a verifier event

stale_read_sound:
  every emitted stale-read warning corresponds to unequal source hashes

budget_sound:
  rendered token cost does not exceed the declared bundle budget

summary_traceable:
  every durable summary claim retains at least one source reference

delta_replay:
  applying all admitted semantic deltas reproduces the current snapshot

capability_sound:
  an authorized action has a corresponding current authorization derivation
```

For attention, formalize nondegeneracy, actual budget semantics, absence of absorbing floor walls, and culling liveness.

This directly addresses the review bundle’s strongest skeptical question: the current Lean work formalizes important abstract relations, but nothing yet guarantees that failure of those relations changes what the running agent does. An extraction-and-rendering refinement theorem would make the formal layer operationally load-bearing rather than decorative. 

# Evaluation-first rollout

The rollout should be conservative.

**Phase 0 — shadow graph.** Ingest session, file, git, tool, test, LSP, instruction, and agent events. Run queries but expose nothing to the model. Measure latency and compare retrieved candidates against what the agent actually needed.

**Phase 1 — explicit query tool.** Add `context.query` and `context.explain`. Start with only three patterns: changed-since-read, unresolved-failure neighborhood, and applicable instruction. Keep all results read-only and provenance-backed.

**Phase 2 — automatic working-set context.** Inject a bounded bundle through OpenCode’s typed context source or Codex’s world-state section. Admit changes only at safe turn boundaries.

**Phase 3 — compaction anchoring.** Atomize durable claims and evidence before compaction and regenerate working sets afterward.

**Phase 4 — obligation and capability patterns.** Add goal-evidence gaps, cross-agent collisions, and authorization queries. Still do not let graph activation choose actions directly.

**Phase 5 — adaptive attention and pattern mining.** Learn retrieval weights and mine recurrent useful subgraphs only after the static system demonstrates measurable value.

Run paired replays over actual PeTTaClaw histories with four ablations:

```text
recency only
vector only
graph patterns only
hybrid graph + vector
```

The main metrics should be successful-task rate, tokens per verified result, repeated file reads, repeated searches, stale-read incidents, missed applicable instructions, unresolved-error recovery, compaction continuation accuracy, time to resume after restart, contradiction rate, retrieval precision, latency, and privacy or ACL violations.

# The smallest correct first build

The first implementation should contain:

```text
1. An append-only event journal.
2. A project AtomSpace plus session overlay.
3. Atomizers for file reads, edits, git state, tests, errors,
   instructions, tasks, claims, and tool calls.
4. context.query and context.explain.
5. Three patterns:
   - changed since last read;
   - unresolved failure → symbol → file/test;
   - applicable instruction.
6. A ContextBundle with provenance and explicit inclusion reasons.
7. Shadow-mode replay evaluation.
```

Do **not** initially connect it to `Next Move`, goal priority, autonomous action selection, or self-modification.

That is the smallest integration that is genuinely AtomSpace-shaped rather than “a graph database bolted onto an LLM.” It exploits the characteristic strength of AtomSpaces—typed relational pattern matching shared across cognitive processes—while using the mature snapshot, diff, compaction, and permission machinery that OpenCode and Codex have already developed.

[1]: https://github.com/opencog/atomspace "https://github.com/opencog/atomspace"
[2]: https://raw.githubusercontent.com/anomalyco/opencode/dev/CONTEXT.md "https://raw.githubusercontent.com/anomalyco/opencode/dev/CONTEXT.md"
[3]: https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/session/instruction.ts "https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/session/instruction.ts"
[4]: https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/context/world_state/mod.rs "https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/context/world_state/mod.rs"
[5]: https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/agents_md.rs "https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/agents_md.rs"
[6]: https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/realtime_context.rs "https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/realtime_context.rs"
[7]: https://wiki.opencog.org/w/OpenCogPrime%3AEconomicAttentionAllocation "https://wiki.opencog.org/w/OpenCogPrime%3AEconomicAttentionAllocation"
[8]: https://github.com/trueagi-io/MORK "https://github.com/trueagi-io/MORK"
## Core distinction

I am using **Iter** to mean the live PeTTaClaw-derived agent reviewed on August 19, 2026, rather than merely the abstract GOLEM-Iter specification. The public `godelclaw/pettaclaw` repository is the closest inspectable proxy, but the live Iter implementation is ahead of it: the review bundle described 109 files from the live Iter-style agent, including the recent context upgrade. 

The architectures can be summarized as:

```text
Original MeTTaClaw
  = reconstructed text prompt
  + recent raw history tail
  + recent tool-result tail
  + always-present promoted memories
  + explicit vector-memory queries

Current Iter / PeTTaClaw
  = reconstructed text prompt
  + persistent present-moment state
  + recent activity/actions
  + goals/work state
  + pins
  + recent history and tool results
  + explicit long-term-memory retrieval

Current OpenCode / Codex
  = versioned conversational history
  + independently typed context sources/sections
  + durable snapshots and chronological deltas
  + bounded recent context
  + structured compaction
  + fresh state reinjection after context replacement
```

So Iter has become substantially better at **maintaining a continuous working self**, but Codex and OpenCode are developing a more principled **context operating system**.

## Original MeTTaClaw

Upstream MeTTaClaw constructs one large text string on each agent cycle. Its `getContext` concatenates:

* the identity/system prompt;
* the complete skill catalog;
* output-format instructions;
* the tail of the previous tool results;
* the history tail;
* the most promoted memories;
* the current time.

The newly received message is appended afterward, and the resulting string is sent to the model.

Its short-term conversation management is especially simple:

```metta
(= (getHistory)
   (let $ret (read-file ...history.metta)
        (last_chars $ret (maxHistory))))
```

The defaults are approximately:

```text
history tail             30,000 characters
last tool-result tail    50,000 characters
automatic promoted LTM   10 memories
embedding recall         10 promoted + 10 similar items
episode recall           20 history lines
```

There is no semantic compaction, turn-aware truncation, message-role preservation, contradiction handling, or source versioning. It retains the last characters of a growing file—even potentially cutting through a semantic unit.

### Long-term memory

MeTTaClaw has a genuine persistent-memory subsystem, but it is mostly **agent-directed retrieval**, not automatic context selection.

The agent can:

```text
remember "..."
query "..."
episodes "timestamp"
promote "timestamp"
demote "timestamp"
```

`query` embeds the search phrase, finds nearest memories, combines similarity with manually accumulated promotion, and returns a bounded selection. Promotion decays over time. The ten most promoted memories are inserted automatically into every prompt, whether or not they are relevant to the current task.

The policy prompt tells the agent always to query memory, use pins for task state, and use ordinary memories for information valuable in the future. But this is an instruction to the LLM, not an enforced retrieval planner.

Upstream’s baseline `pin` implementation merely returns `PIN-SUCCESS`; it does not maintain a separate structured pin store. Its usefulness is largely indirect because the command appears in recent history. Iter’s later pin system is a real extension over this.

Thus:

> **MeTTaClaw stores memories in an AtomSpace-compatible representation, but its LLM context is not selected by AtomSpace pattern matching.**

The AtomSpace is a memory/tool substrate. The actual context manager is a text concatenator.

## Current public PeTTaClaw and live Iter

PeTTaClaw added considerably richer ongoing state. Its public documentation describes:

* batch consumption of pending messages into a chronological activity block;
* a persisted “present moment” across process restarts;
* persistent pins;
* an autonomic goal stack;
* embedding-based long-term memory;
* heartbeat-driven autonomous wake cycles;
* persistence of current pacing, results, and in-flight intention.

A restart is intentionally treated as sleep rather than a new identity.

The public loop restores state at boot and snapshots it at each turn boundary. Its prompt assembly places static content first to improve provider prefix-cache reuse, then appends dynamic fields:

```text
LOOPS_LEFT
SLEEP_INTERVAL_SECONDS
ACTIVE_MODEL
RECENT_ACTIVITY
GOAL_STACK
ATTENTION_RANKING
PINNED
HISTORY
LAST_SKILL_USE_RESULTS
TIME
```

That static-prefix arrangement is a good optimization. It increases cache stability. But semantically, it is still the same broad architecture: **render every selected subsystem as text and concatenate the blocks every cycle**.

### The private/live Iter upgrade

The August 19 review indicates that the live agent had advanced beyond the public version:

* a `WORK_STATE` context block had been added;
* a `RECENT_ACTIONS` block had been added, though its first post-restart population still needed live confirmation;
* long-term memory and promoted memories remained;
* the old attention view was considered dead code and marked for deletion;
* Telegram state was still structurally duplicated;
* the context upgrade was shipped but pending restart verification. 

The problematic part was that `WORK_STATE` initially included a **Next Move** derived from the top goal under STI ranking. Since STI had collapsed toward a near-uniform floor, that rendered recommendation manufactured authority from an unreliable signal. You rejected it, and it was removed. 

This episode reveals the present Iter architecture quite well:

> The context blocks are bespoke projections of subsystems, and some projections can quietly become load-bearing policy.

They do not yet share a uniform contract for:

* source identity;
* typed state;
* freshness;
* provenance;
* exact previous value;
* delta rendering;
* temporary unavailability;
* removal;
* contradiction or supersession.

The STI incident is therefore not just an attention problem. It is also a context-governance problem: `WORK_STATE` had no principled distinction between **observed state**, **ranked candidate**, and **recommended action**.

### Operational consequence

In an earlier July 22 snapshot, one agent call carried roughly 54 KB—approximately 14,000 input tokens—because every turn included the complete system prompt, goal stack, history block, and skill catalog. The analysis correctly identified context size as the major cost multiplier and proposed transmitting only hot goals and relevant history. That predates the newest Iter context upgrade, so it should not be treated as Iter’s exact current token count, but it shows the architectural pressure that motivated the upgrade. 

## What OpenCode changes

OpenCode now represents ambient system context as a collection of independently refreshable, typed sources. Each source specifies:

```ts
key
codec
load
baseline(current)
update(previous, current)
removed(previous)   // optional
```

It stores a structured snapshot of the value that was actually admitted to the model. On the next safe context reconciliation:

* unchanged values emit nothing;
* changed values emit an update;
* newly appearing sources emit a baseline;
* removed sources emit a removal message;
* incompatible snapshot formats trigger complete replacement;
* temporarily unavailable sources retain their previously admitted state instead of being interpreted as deleted.

Duplicate source keys are rejected.

That last distinction is particularly important:

```text
failed to load pins
    ≠
there are now no pins
```

Iter’s current string-projection approach does not naturally encode that distinction.

### OpenCode compaction

When history becomes too large, OpenCode retains a bounded recent tail and summarizes the older head into a fixed structure:

```text
Objective
Important Details
Work State
  Completed
  Active
  Blocked
Next Move
Relevant Files
```

It carries the previous summary into the next compaction and explicitly instructs the model to preserve older unfinished objectives and decisions unless newer conversation supersedes them.

This is still lossy model-generated prose. It is not perfect epistemology. Its `Next Move` may still be mistaken. But it differs from Iter’s removed version:

* Iter’s was mechanically selected from a broken scalar ranking.
* OpenCode’s is a summarizing model’s continuation hypothesis derived from conversation.
* Neither should be treated as verified authority.
* OpenCode at least keeps it inside an explicitly identified summary artifact rather than silently presenting a scalar winner as fact.

## What Codex changes

Codex’s corresponding abstraction is `WorldState`. It consists of independently typed sections with:

* stable IDs;
* serializable typed snapshots;
* section-specific diff renderers;
* full rendering when no baseline exists;
* exact rendering against a known snapshot;
* fallback inspection of retained history;
* persisted fingerprints;
* RFC 7386-style merge patches;
* extension-defined sections.

Current sections include environment, model, permissions, tools, instructions, collaboration state, personality, applications, realtime state, and other operational facts.

So instead of every turn saying:

```text
Here is the environment again.
Here are all permissions again.
Here are all tools again.
Here are all instructions again.
```

Codex can preserve a known baseline and tell the model only what has changed.

### Bounded recent context

Codex also builds bounded startup context with separate budgets for:

```text
Current Thread            1,200 tokens
Recent Work               2,200 tokens
Machine / Workspace Map   1,600 tokens
Notes                       300 tokens
```

It examines recent threads, groups work by repository, prioritizes the current repository, retains bounded pieces of recent turns, and performs only a shallow workspace scan. It explicitly labels this context as potentially incomplete or stale.

That is already considerably safer than injecting an unlabelled mass of historical text. But it remains mostly:

* recency;
* repository grouping;
* directory structure;
* bounded text selection.

It is not yet an AtomSpace-like relational working set connecting failures, symbols, files, tests, decisions, and instructions.

### Cross-session memory

When enabled, Codex has a two-stage memory pipeline:

1. Recent eligible rollouts are filtered and converted into structured per-thread memories and summaries.
2. A globally serialized consolidation phase selects memories using usage and freshness, updates stable memory artifacts, computes a workspace diff, prunes stale material, and invokes a restricted consolidation agent only when something changed.

This is much more managed than MeTTaClaw’s manually written embedding memories: it has leases, retry backoff, selection watermarks, secret redaction, usage telemetry, pruning, and explicit consolidation boundaries.

Conversely, MeTTaClaw/Iter gives the agent more direct authorship over what it remembers. That may be cognitively valuable. Codex’s pipeline is more operationally disciplined but more externally administered.

## Direct comparison

| Property          | MeTTaClaw                                     | Iter / PeTTaClaw                                              | OpenCode / Codex                                       |
| ----------------- | --------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| Immediate history | Last character tail                           | History plus recent activity/actions                          | Versioned turns plus bounded recent selection          |
| Working memory    | Nominal `pin`; largely history-based upstream | Persistent pins, goals, work state, present moment            | Typed state sources/sections                           |
| Restart behavior  | Reload files and persistent memory            | Explicitly preserves the working self                         | Restores durable history and state baselines           |
| Context update    | Rebuild and resend blocks                     | Rebuild and resend richer blocks                              | Compare snapshots and emit deltas                      |
| Long-term memory  | Explicit vector query and manual promotion    | Extended LTM plus agent-owned goals/pins                      | Extracted, consolidated, usage-ranked memories         |
| Compaction        | Character truncation                          | Newer work-state projection, but no general compactor visible | Structured summary plus recent raw tail                |
| Retrieval         | Similarity plus promotion                     | Similarity, promotion, goals, recent actions                  | Recency, fuzzy search, structured memory lookup        |
| Source identity   | Mostly labels in a prompt string              | Named blocks, bespoke schemas                                 | Stable machine-readable source IDs                     |
| Failure semantics | Empty or missing text can look like absence   | Better loud failures, but no uniform context protocol         | Unavailable, absent, changed, removed, incompatible    |
| Provenance        | Timestamped memories; limited claim typing    | Some goal metadata, but self-report confusion occurred        | Versioned snapshots, source sections, history metadata |
| Action authority  | LLM chooses after retrieval                   | LLM plus attempted goal ranking; bad ranking removed          | Generally LLM chooses; context supplies evidence       |
| Main strength     | Tiny, transparent, agent-controlled           | Continuous embodied self and autonomous life rhythm           | Integrity, boundedness, rollback, diffing, compaction  |

## The important non-dominance

Codex/OpenCode are not simply “better agents.”

Iter is stronger in several ways:

* It has a persistent, agent-visible present moment.
* It treats process restart as bodily sleep rather than conversational replacement.
* It owns goals, pins, pacing, energy, and memory operations.
* Its long-term memories can coexist with other MeTTa/Hyperon cognitive processes.
* Its continual loop supports autonomous thought between human messages.
* It can intentionally remember, promote, demote, or reorganize its own knowledge.

Codex and OpenCode are stronger at a different layer:

* knowing exactly which context state the model has seen;
* updating only changed state;
* distinguishing unavailability from removal;
* handling rollback and compaction;
* bounding recent work;
* avoiding accidental duplication;
* preserving source identity and compatibility;
* controlling context-window consumption.

The ideal is not to replace Iter’s cognition with Codex’s session machinery. It is:

> **Keep Iter’s living self, but give it OpenCode/Codex-grade context plumbing.**

## The exact synthesis I would implement

Turn the current context blocks into typed sources:

```text
iter/identity
iter/capabilities
iter/present-moment
iter/recent-activity
iter/recent-actions
iter/work-state
iter/goals
iter/pins
iter/tool-results
iter/environment
iter/memory-recall
iter/semantic-working-set
```

Each should implement approximately:

```text
key
schema/version
observe()
snapshot()
renderBaseline()
renderDelta(previous)
renderRemoval()
unavailablePolicy
provenance
tokenCost
```

Then:

1. **Preserve the baseline across ordinary process restarts.** For Iter, restart is sleep, so it should not automatically create a new context generation.

2. **Keep raw history as an append-only event source outside the prompt.** Prompt context should contain a structured continuation summary, a bounded recent tail, and exact references back to the event log.

3. **Make `WORK_STATE` descriptive.** It may state active goals, blockers, obligations, and evidence. It should not declare the next action.

4. **Make `RECENT_ACTIONS` event-derived.** Include action ID, time, tool, result status, affected resources, and relation to current work—not merely the latest text lines.

5. **Use AtomSpace behind `semantic-working-set`.** Seed it from the current message, goals, pins, failures, changed files, and recent actions. Pattern-match for relevant facts and render only the selected bundle.

6. **Keep Iter’s static-prefix optimization.** Typed sources should render in deterministic canonical order so provider caching still works.

7. **Do not allow STI alone to select context or action.** After its economy is repaired, it can be one retrieval feature alongside relevance, freshness, unresolvedness, evidence quality, user pins, and token cost.

The most accurate verdict is:

> **MeTTaClaw has an AtomSpace memory but a text-tail context manager. Iter has evolved into a persistent working-self context manager, but it still projects bespoke blocks into a monolithic prompt. Codex and OpenCode are evolving typed, versioned, delta-aware context runtimes—but their selection remains mostly recency, summaries, and heuristics rather than relational cognition.**

That makes the AtomSpace integration unusually well motivated: not as another store, but as the missing **task-relative selector behind Iter’s typed context sources**.
