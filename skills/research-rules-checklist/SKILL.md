---
name: "research-rules-checklist"
description: "Apply Ben's cross-project research rules at project start/pivots."
---

# Research Rules Checklist

Use when starting a new research/engineering project, reviewing an active project, making a strategic pivot, or writing a progress report.

## Procedure

1. Read `catalog/RESEARCH_RULES.md` from the research-agent workspace.
2. Apply the rules fuzzily, not bureaucratically: identify which rules are relevant to the current project or pivot.
3. For project start or major pivot, record the project-specific implications in `PROJECT.md`, `TASKS.md`, `DECISIONS.md`, or `NOTES.md` as appropriate.
4. Before trusting any estimator/miner/detector, ask whether it has known-case validation; if not, add a test/benchmark task.
5. Before implementing nontrivial code, ensure there is a plain-language spec or design note with inputs, outputs, invariants, and acceptance tests.
6. Check whether a strong existing framework should be used instead of rebuilding.
7. For major strategic decisions, trigger concise multi-agent discussion where available.
8. For progress reports, include enough detail to replicate: repo/path/commit, commands, seeds/parameters, quantitative results, controls, failed checks, and limits.
9. For new conceptual methods, add a Hyperseed/formal-analysis subthread where relevant.
10. For software design, preserve modular interfaces so future implementations can swap algorithms or substrates.

## Update rule

When Ben identifies a new recurring pattern or antipattern, update `catalog/RESEARCH_RULES.md` and, if this skill is installed, revise this skill proposal/skill accordingly.
