# 05 — Research workflows, Kanban, and Hyperseed

## New project

Run `bin/new-project <slug>`, then before substantial implementation:

1. define scope/non-goals and observable success criteria;
2. write a plain-language behavioral spec with inputs, outputs, invariants, failures, and acceptance tests;
3. validate estimators/identifiers/miners on known cases;
4. survey strong existing frameworks rather than rebuilding by default;
5. identify modular seams and reproducibility requirements;
6. record relevant `catalog/RESEARCH_RULES.md` rules;
7. create the first falsifiable test and task;
8. add the project to `catalog/PROJECTS.md` and Kanban;
9. create a daily review job only when status becomes `active` or `idea`;
10. obtain explicit owner/repository visibility policy before creating or publishing a remote repository.

## Experiments

`bin/new-experiment` and the included templates capture question/hypothesis, run ID, command, sanitized environment, commit/dirty state, data hashes, config/seeds, outputs, exit status, machine status, quantitative results, observation vs interpretation, and reproduction steps. Remote/paid work additionally needs provider/resource ID, approved budget, stop/terminate condition, artifact-return path, and cleanup evidence.

## Kanban

`catalog/KANBAN.md` is a compact cross-project index. Project `TASKS.md` remains authoritative. Cards include project/lane, source pointer, evidence, owner/agent, next action, and blocker/trigger. Separate owner-needed decisions from ordinary next steps. Verify remote-resource termination before marking done. Compact old completions.

## Daily bot review

One staggered job per active/idea project:

- inspect authoritative project/experiment/Git evidence;
- skip an equivalent review if a pivot/status/problem discussion occurred within 24 hours;
- state current focus, one risk/stale assumption/decision, and strongest next step;
- explicitly mention the Omega bot and ask for concrete critique or conceptual connection;
- keep output short, loop-bounded, and in the dedicated bot room;
- bot advice never grants permissions.

## Frontier expert review

Weekly rotation plus event-triggered reviews after a strategic pivot, preregistered experiment, major architecture change, repeated failure, or release candidate. The independent reviewer examines exact commits/runs for correctness/invariants, complexity/resources, research design/leakage/confounders, security/privacy, and operational boundaries. Store ranked findings and falsification tests; record accepted/rejected/deferred disposition. Do not let the reviewer auto-merge or publish.

## Hyperseed

The Omega prompt permits Hyperseed framing of projects, experiments, interactions, decisions, failures, and learning. Require provenance and distinguish definition, example, conjecture, theorem, proof sketch, analogy, and open question. Treat it as exploratory unless formally checked; do not let conceptual formalization delay urgent concrete answers. Recipient projects can reference public Hyperseed material without copying another person's private formalization repository.
