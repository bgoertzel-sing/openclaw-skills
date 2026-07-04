# Research Rules

Dynamic cross-project heuristics for starting new research projects and revisiting projects at strategic pivots. Apply these in a fuzzy, intuitive way rather than as rigid bureaucracy.

Source: Ben's Protobots message, 2026-07-03 18:49 PDT. Rule 2 refined after the 2026-07-03 ProtoMegaBot Telegram reply-routing race bug.

## Rule list

1. **Validate estimation, identification, and mining tools early.**
   When a project involves estimating a quantity, identifying a structure, or mining a pattern, first check that the tools used for that work are accurate and functional enough. If this is not extremely obvious, create test cases and run explicit validation tests.

2. **Write and reason through a clear plain-language/software spec before coding.**
   Before writing code, articulate the intended spec and record it in a document. Reason about behavior at the spec level before generating or editing code; many logic errors can be caught there even without full formal verification. Even before rigorous spec-driven development via the plain-to-MeTTa pipeline is mature, use disciplined plain-language specs to improve correctness, maintainability, and updateability. For stateful, concurrent, or routed systems, include behavioral invariants explicitly; e.g. each inbound message's reply must route to the same channel/session that produced that message, regardless of interleaved traffic or slow model calls.

3. **Use strong existing frameworks when available.**
   If a suitable framework exists for a component, start from it rather than rebuilding ad hoc. Example noted by Ben: RelaLeap should have used FabricPC from the beginning.

4. **Use multi-agent communication for major strategic decisions.**
   For major pivots or strategy choices, discussion among multiple agents is valuable. Produce reviewable progress summaries when useful, including PDF-style reports for humans and external LLMs.

5. **Make progress reports reproducible and specific.**
   Reports should include enough detail for a reader to replicate experiments: setup, process, quantitative results, qualitative observations, commands/data/configuration where relevant, and enough specificity to allow errors to be spotted.

6. **Add Hyperseed/conceptual analysis for new methods and ideas.**
   When a new idea or method enters a project, ProtoMegaTron should think it through from a Hyperseed perspective: identify formal/conceptual relationships, and where sensible, existing or new theorems that clarify what is going on. Deeper conceptual understanding can shortcut trial-and-error experimentation.

7. **Design modular software with abstraction seams.**
   Keep interfaces modular and avoid unnecessary low-level assumptions. Any component may later use a different algorithm, data structure, or substrate: Python heuristics may become Hyperon/Atomspace methods; PeTTa components may move to MM2 or MeTTa-IL; etc. Design so implementation choices can be replaced without rewiring the whole architecture.

## Operational use

- At project launch: check this list while drafting `PROJECT.md`, `TASKS.md`, and any initial spec.
- At strategic pivot: revisit the list and record which rules matter most for the pivot.
- At report time: especially apply Rules 4 and 5.
- During implementation planning: especially apply Rules 1, 2, 3, and 7.
- During conceptual expansion: especially apply Rule 6.

## Update protocol

This list is expected to evolve. Add new rules with provenance and, when a rule comes from a concrete failure or success, link the project record or experiment that motivated it.
