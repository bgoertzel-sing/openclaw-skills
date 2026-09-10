# Decision Log

## D-20260814-complementary-rooms: Keep goal relevance distinct from deliberation transport

- Date: `2026-08-14`
- Status: `proposed`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md`; `library/omegahive-deliberation-rooms/SOURCE.md`

### Context

Deliberation Rooms specify how bounded seats and humans discuss a question and
commit a conclusion. They explicitly are not a task queue or knowledge store.
The observed failures require persistent means--ends and resource-conflict
state plus relevance review.

### Decision

Use a committed typed goal/task/resource graph as control state. Use cheap
event-triggered or periodic workers for ordinary relevance checks, and open a
Deliberation Room only for ambiguous, novel, conflicting, or high-impact
verdicts.

### Alternatives considered

- Make every relevance check a room: rejected as excessive coordination cost.
- Treat rooms as the goal store: rejected because conversation is explicitly
  non-authoritative until committed.

### Rationale and evidence

This preserves the Deliberation Rooms doctrine while adding the missing
selection, priority, opportunity-cost, and stale-task mechanisms. Relevant
research rules: 1, 2, 3, 4, 5, 6, and 7, with Rules 2, 3, and 7 most central.

### Consequences

The evaluator, graph store, and deliberation adapter must be modular. Initial
deployment is read-only recommendation and retrospective replay.

### Revisit trigger

Replay shows the graph adds no detection value beyond ordinary project files,
or rooms evolve to include an authoritative goal/task projection.

### Supersedes or superseded by

None.

## D-20260814-stage-result-contracts: Make useful results stage-sensitive

- Date: `2026-08-14`
- Status: `proposed`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/goal_relevance_governor_design_2026-08-14.pdf`

### Context

Top-level goals such as fast first results, simple execution, and fast mature
results can still rationalize premature hardening unless the project kind,
current stage, and meaning of a useful result are explicit.

### Decision

Add a result contract to the goal graph: project kind, maturity stage, next
decision-relevant result, sufficient trust evidence, mature result, shortcut
debt, hardening triggers, and current non-goals. Treat minimum-sufficient rigor
as mandatory and production polish as deferred until its trigger fires.

### Alternatives considered

- Use priority weights alone: rejected because they do not define progress.
- Always optimize the first result: rejected because invalid evidence and
  excessive rework can delay the mature result.
- Harden broadly in anticipation: rejected because many exploratory ideas will
  be abandoned before the infrastructure has value.

### Rationale and evidence

The rule would have challenged both extended research-infrastructure hardening
before scientific signal and the generalized privileged-inspector path before
an unchanged OmegaClaw upstream baseline was tested.

### Consequences

Replay evaluation must score project-kind/stage inference and distinguish
validity-critical guards from premature polish.

### Revisit trigger

Historical replay shows that result contracts add little beyond ordinary goal
links, or project-stage inference proves too unstable to guide recommendations.

### Supersedes or superseded by

None.

## D-20260908-pln-integration: Layered PLN evaluation with blended scoring

- Date: `2026-09-08`
- Status: `accepted`
- Decision owner: autonomous session
- Related task/run/commit: `9821a23` (blended relevance), `4ff837b` (PLN inference rules)

### Context

The pure-Python evaluator handles the 6 replay episodes correctly but uses
simple priority/status heuristics. PLN evidence propagation and inference
rules can provide deeper relevance signals (multi-hop goal chains, truth-value
combination) but add complexity and potential false signals.

### Decision

Implement PLN as a *layered enhancement* on top of the base evaluator, not a
replacement. Blend 60% naive relevance with 40% enhanced PLN relevance for
nuanced task differentiation. The base evaluator verdict remains authoritative;
PLN signals inform the relevance score that feeds into the verdict rules.

### Alternatives considered

- Replace base evaluator with PLN-only: rejected as too brittle for simple cases.
- Run PLN purely as shadow with no blending: rejected as providing no practical differentiation.
- 50/50 blend: rejected as giving PLN too much weight before cross-validation maturity.

### Rationale and evidence

5/5 replay episodes cross-validate between PLN and pure-Python evaluator.
The 60/40 blend provides differentiation on episode_06 (conflict) where naive
scoring gives both tasks equal relevance but PLN correctly down-weights the
weaker task.

### Consequences

The blended score feeds into relevance_evaluator.py's verdict rules.
Future tuning of the blend ratio may be needed as more episodes are added.
PLN inference rules (deduction, induction, abduction) are available but
not yet wired into the live evaluator chain.

### Revisit trigger

New replay episodes show PLN signals degrading verdict accuracy, or
cross-validation drops below 5/6 agreement.

### Supersedes or superseded by

None.
