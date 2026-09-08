---
name: "materialize-narrowing-gate-procedure"
description: "Scaffold a PeTTaChainer materialize narrowing gate: rung generator, gate runner, JSON artifact with sha256, test, and project record update."
---

# Skill: materialize-narrowing-gate-procedure

## When to use

When adding a new bounded non-live PeTTaChainer `materialize-stmt-lambdas` narrowing gate to the `petta-memory` project. These gates isolate a specific sub-expression shape, run it through `materialize-stmt-lambdas` in an isolated subprocess, record timing/pass/fail, and narrow the known materializer blocker — without invoking `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal writes.

## Context

The petta-memory project has run ~10+ progressive narrowing gates (identity → proof-shape → sentinel → nested-type → context-matrix → four-field → neighbor-shape → right-payload-arity → adjacent-nested-arity). Each follows an identical structure. This skill scaffolds the boilerplate so the agent can focus on the diagnostic logic.

## Prerequisites

- Active project: `projects/petta-memory`
- Local repo: `projects/petta-memory/repos/petta-memory`
- Source file: `src/petta_memory/pettachainer_profile.py`
- Tests: `tests/`
- Artifacts: `projects/petta-memory/artifacts/`
- All prior gates pass their tests; the new gate extends the ladder.

## Procedure

### 1. Design the narrowing rungs

Identify what aspect of the materializer blocker to narrow next. Each rung should:
- Be a single `materialize-stmt-lambdas` invocation on a synthetic or real MeTTa expression.
- Vary exactly one dimension from the prior gate (arity, position, token, wrapper shape, neighbor payload).
- Include at least one known-passing control rung and one expected-to-block rung.
- Never invoke `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal writes.

### 2. Add rung generator function

In `pettachainer_profile.py`, add a function `materialize_<descriptive_name>_rungs(statement: str) -> list[str]` that returns the ordered list of rung expressions to test.

```python
def materialize_<descriptive_name>_rungs(statement: str) -> list[str]:
    """Return ordered rungs for <description> narrowing gate."""
    return [
        # control rung(s) known to pass
        # ...
        # diagnostic rung(s) expected to block
        # ...
    ]
```

### 3. Add gate runner function

Add `run_materialize_<descriptive_name>_gate(statement, *, project_root, stage_timeout_sec=10.0) -> dict` that:
- Calls `run_materialize_identity_ladder_gate(rungs, ...)` with the new rungs.
- Updates the result dict with `source`, `proof_statement`, `<descriptive_name>_rungs`, and `interpretation` (pass/fail branching).
- Sets `result["gates"]` to the standard safety gate list:
  - `"<Description> matrix only; each rung invokes materialize-stmt-lambdas in an isolated subprocess."`
  - `"No mm2compile, compileadd, query, GoalChainer, OmegaClaw path, journal write, or inferred-belief claim is invoked."`
  - `"Synthetic ... rungs are diagnostics for the materializer/evaluator and are not PLN premises."`

### 4. Add CLI entry (optional)

If the gate should be runnable from the CLI, add a subcommand in the CLI module following the existing pattern.

### 5. Add focused test

Add `tests/test_materialize_<descriptive_name>_gate.py` that:
- Calls the rung generator and asserts structural properties (non-empty, each rung is a string).
- Calls the gate runner with a short timeout and asserts the result has `status`, `rungs`, `gates`, `interpretation`.
- Does **not** assert pass/fail of the materialize runtime (it may time out); only asserts structural correctness.

### 6. Run tests

```bash
cd projects/petta-memory/repos/petta-memory
PYTHONPATH=src python3 -m unittest tests/test_materialize_<descriptive_name>_gate.py -v
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

All tests must pass. Record the new test count.

### 7. Run the gate and produce artifact

```bash
PYTHONPATH=src python3 -c "
from pathlib import Path
from petta_memory.pettachainer_profile import run_materialize_<descriptive_name>_gate
import json, hashlib, datetime
result = run_materialize_<descriptive_name>_gate(
    '<statement>',
    project_root=Path('..'),
    stage_timeout_sec=4.0,
)
artifact = {
    **result,
    'timestamp_utc': datetime.datetime.utcnow().isoformat() + 'Z',
}
print(json.dumps(artifact, indent=2, default=str))
" > ../../artifacts/pettachainer_materialize_<descriptive_name>_gate_<YYYY-MM-DDTHHMMZ>.json
```

Compute and verify sha256:
```bash
sha256sum ../../artifacts/pettachainer_materialize_<descriptive_name>_gate_<YYYY-MM-DDTHHMMZ>.json
```

### 8. Commit

```bash
git add -A
git commit -m "Add bounded non-live PeTTaChainer <descriptive name> materialize gate"
```

### 9. Update project records

- **NOTES.md**: Add a timestamped entry with: commit hash, rung description, artifact path + sha256, pass/fail per rung, interpretation, boundaries, verification (test count + `git diff --check`).
- **PROJECT.md**: Update "Current state" with a one-paragraph summary of the new gate and its narrowing result.
- **TASKS.md**: Update the relevant task item status.

### 10. Verify

- Test count increased by expected amount.
- `git diff --check` passes.
- Artifact file exists and sha256 is recorded.
- No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, or journal write was invoked.

## Anti-patterns

- Do not assert materialize runtime pass/fail in tests (timing varies).
- Do not add rungs that invoke `compileadd`, `mm2compile`, or query.
- Do not write to the journal or claim PLN inferences.
- Do not push to remote unless explicitly approved.
- Do not skip the artifact sha256 or NOTES.md provenance entry.
