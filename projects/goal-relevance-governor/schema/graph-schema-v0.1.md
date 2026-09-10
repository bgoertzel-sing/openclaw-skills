# Goal Relevance Governor - Minimal JSON Graph Schema v0.1

> Derived from `docs/goal_relevance_governor_design_2026-08-14.pdf`, sections 4-8.
> Implements Phase 0 of the staged implementation path (section 12).
> Satisfies the "Next" task in TASKS.md: "Specify a minimal JSON graph schema and read-only relevance verdict."

## Design principles

1. **Read-only evaluation.** The evaluator reads the graph and produces verdicts.
   It does not mutate state or retarget workers. Live enforcement is blocked
   pending replay/shadow validation and explicit Ben approval.
2. **Committed JSON.** Storage is a single JSON file committed to the project
   repo. No database dependency.
3. **Typed nodes and edges.** Every node has a `kind`; every edge has a
   `relation`. Unknown kinds/relations are ignored by the evaluator
   (forward-compatible).
4. **Evidence-bearing.** Every claim carries `source` and `as_of` so the
   evaluator can detect stale information.
5. **Stage-sensitive.** Every project node carries a `result_contract`
   (section 4.4 of the design) so the evaluator can detect premature
   hardening or displaced urgency.

## Top-level structure

```json
{
  "schema_version": "0.1",
  "as_of": "2026-09-08T01:31:00Z",
  "goals": [],
  "projects": [],
  "tasks": [],
  "resources": [],
  "results": [],
  "constraints": [],
  "edges": []
}
```

## Node types

### goal

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "goal" |
| `title` | string | yes | Human-readable summary |
| `level` | enum | yes | "top" or "intermediate" |
| `status` | enum | yes | "active", "achieved", "paused", "superseded", "cancelled" |
| `priority` | object | no | `{ rank: int, urgency: "low"|"medium"|"high"|"critical", notes: string }` |
| `time_horizon` | string | no | ISO date or human-readable deadline |
| `success_criteria` | string | no | What constitutes achievement |
| `authority` | string | no | Who authorized this goal |
| `source` | string | yes | Provenance (who/what set this status) |
| `as_of` | string | yes | ISO timestamp of last update |

### project

A project with a stage-sensitive result contract.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "project" |
| `title` | string | yes | Human-readable summary |
| `result_contract` | object | yes | See result_contract below |
| `source` | string | yes | Provenance |
| `as_of` | string | yes | ISO timestamp |

#### result_contract (section 4.4)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `project_kind` | enum | yes | "exploratory_research", "confirmatory_research", "production_engineering", "service_recovery", "infrastructure" |
| `maturity_stage` | enum | yes | "E0_exploration", "E1_signal_validation", "E2_replication_robustness", "E3_reusable_implementation", "E4_production_engineering" |
| `next_result` | string | yes | Next decision-relevant result needed |
| `trust_evidence` | string | yes | Evidence sufficient to trust that result |
| `mature_result` | string | yes | Intended final result |
| `known_shortcuts` | array | no | `[{ description: string, debt_estimate: string }]` |
| `hardening_trigger` | string | no | Conditions under which additional hardening becomes necessary |
| `non_goals` | array | no | `[string, ...]` - explicit non-goals for current stage |
| `owner` | string | yes | Project owner |
| `confidence` | enum | no | "low", "medium", "high" |
| `next_review_trigger` | string | no | Event or condition that should trigger next review |

### task

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "task" |
| `title` | string | yes | Human-readable summary |
| `status` | enum | yes | "active", "blocked", "completed", "paused", "cancelled" |
| `owner` | string | yes | Worker or person responsible |
| `expected_duration` | string | no | Estimated duration |
| `reversibility` | enum | no | "reversible", "checkpointable", "irreversible" |
| `acceptance_test` | string | no | How to verify completion |
| `evidence_path` | string | no | Path to evidence of progress |
| `source` | string | yes | Provenance |
| `as_of` | string | yes | ISO timestamp |

### resource

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "resource" |
| `title` | string | yes | Human-readable name |
| `resource_type` | enum | yes | "cpu", "gpu", "process", "repository", "identity", "credential", "database", "network", "human_attention" |
| `exclusive` | boolean | no | If true, only one task can hold it at a time (default: false) |
| `source` | string | yes | Provenance |
| `as_of` | string | yes | ISO timestamp |

### result

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "result" |
| `title` | string | yes | Human-readable summary |
| `outcome_type` | enum | yes | "success", "failure", "measurement", "artifact", "decision" |
| `source` | string | yes | Provenance |
| `as_of` | string | yes | ISO timestamp |

### constraint

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier |
| `kind` | string | yes | Always "constraint" |
| `title` | string | yes | Human-readable summary |
| `constraint_type` | enum | yes | "safety", "budget", "authorization", "deadline", "ordering", "privacy", "semantic", "lifecycle" |
| `enforced` | boolean | no | If true, violation is a hard block (default: false) |
| `source` | string | yes | Provenance |
| `as_of` | string | yes | ISO timestamp |

## Edge types

Edges are directed (`from` -> `to`) with a typed `relation`.

| Relation | Description |
|----------|-------------|
| `contributes_to` | Task/goal contributes to a parent goal |
| `necessary_for` | Source is necessary for target |
| `sufficient_for` | Source is sufficient for target |
| `depends_on` | Source depends on target |
| `blocks` | Source blocks target |
| `conflicts_with` | Source conflicts with target |
| `competes_for` | Source competes with target (a resource) |
| `achieves` | Source achieves target (a goal) |
| `invalidates` | Source invalidates target |
| `supersedes` | Source supersedes target |
| `provides_evidence_for` | Source (a result) provides evidence for target |
| `alternative_to` | Source is an alternative to target |
| `refines` | Source refines target |
| `part_of` | Source is part of target |
| `authorized_by` | Source authorized by target |
| `proposed_by` | Source proposed by target |
| `reviewed_by` | Source reviewed by target |
| `occupies` | Source (a task) occupies target (a resource) |

### Edge metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `from` | string | yes | Source node ID |
| `to` | string | yes | Target node ID |
| `relation` | enum | yes | One of the relations above |
| `confidence` | enum | no | "low", "medium", "high" (default: "medium") |
| `provenance` | string | no | How this edge was established |
| `assumptions` | string | no | Key assumptions |
| `last_review` | string | no | ISO timestamp of last review |
| `revisit_criterion` | string | no | When to revisit this edge |

## Verdict types (section 5.4)

| Verdict | Description |
|---------|-------------|
| `CONTINUE` | Current plan remains proportionate and relevant |
| `ACCELERATE` | Reduce cadence/governance overhead or allocate more resources |
| `PAUSE_RECOVERABLY` | Preserve state and release a resource |
| `STOP_STALE` | Parent goal is achieved, superseded, or absent |
| `REPLAN` | A better path or invalidated assumption changes the decomposition |
| `DEFER` | The task may matter later but is not necessary for the next result |
| `ESCALATE` | Human or multi-seat judgment is required |
| `BLOCKED` | No safe authorized step is available; name the blocker |

### Verdict structure

```json
{
  "task_id": "task-001",
  "verdict": "STOP_STALE",
  "reasons": ["Sole parent goal g-initial-demo is achieved"],
  "evidence": ["goal g-initial-demo status=achieved as of 2026-08-10"],
  "alternatives": ["Link task to revised goal g-v2-ir-translation"],
  "authority": "read_only_shadow",
  "expiry": "2026-09-15T00:00:00Z",
  "review_time": "2026-verdict_expires": "2026-09-15T00:00:00Z",
  "generated_at": "2026-09-08T01:31:00Z"
}
```

## Authority levels (section 8.3)

The evaluator operates at `read_only_shadow` authority. It may only emit
verdicts and record counterfactual recommendations. It must not silently edit
human priorities. It may propose changes with confidence and provenance.

| Authority | Description |
|-----------|-------------|
| `read_only_shadow` | Record what would have been recommended |
| `advisory` | Notify the operator of stale or conflicting work |
| `scheduling_gate` | Prevent a worker with no active goal path from starting |
| `low_risk_autonomy` | Pause checkpointable work or retarget obviously stale workers |
| `strategic_autonomy` | Major goal and priority changes (defer until extensive validation) |

## Review triggers (section 6)

Reviews should be triggered by semantic events, not arbitrary time slices:

- Before a worker starts or resumes
- After a meaningful success, failure, or acceptance result
- When a goal is created, achieved, paused, superseded, or reprioritized
- When the next result, project kind, or maturity stage changes
- When expected duration, cost, or risk changes materially
- When a new resource conflict or blocking relation appears
- After repeated activity with no recorded parent-goal delta
- At a bounded periodic cadence as a backstop

The cadence should be adaptive: stable low-risk tasks need fewer reviews than
incident response with rapidly changing state.

## Maturity ladder (section 4.3)

| Stage | Description |
|-------|-------------|
| `E0_exploration` | Run the smallest trustworthy experiment that can falsify or support the core idea |
| `E1_signal_validation` | Calibrate the estimator, add decisive controls, establish one credible result |
| `E2_replication_robustness` | Test seeds, datasets, baselines, ablations, perturbations, uncertainty |
| `E3_reusable_implementation` | Add cleanup, documentation, interfaces, tests for repeated scientific use |
| `E4_production_engineering` | Add security, fault tolerance, deployment, monitoring, performance, edge cases |

## Minimum-sufficient-hardening test (section 4.5)

Proposed hardening should be checked against:

1. Does the current maturity stage require it?
2. Does the result contract's `hardening_trigger` fire?
3. Is the hardening proportionate to the evidence and risk?
4. Does a simpler alternative achieve the same safety property?

If not, the evaluator should flag `DEFER` or `ESCALATE`.
