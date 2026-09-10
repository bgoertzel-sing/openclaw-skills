# petta-memory coding-agent handoff

Prepared 2026-08-10 for ProtoCosmo2 or another coding agent taking over the work.

## Start here

The authoritative isolated takeover worktree is:

```text
/home/openclaw/research-agent/projects/petta-memory/worktrees/protocosmo2-handoff
```

Its frozen starting state is:

```text
branch: agent/protocosmo2-handoff
commit: 5b842f4d8e203d86c0d14f42eb91a03535376c0a
historical recorded full-suite result: 698 passed
```

Do not work in the older shared clone unless there is a specific reason:

```text
/home/openclaw/research-agent/projects/petta-memory/repos/petta-memory
```

That clone is useful for history/reference, but the isolated worktree prevents
collision with other agents. At handoff, the worktree is clean. Its configured
upstream is 352 commits behind the local head, so preserve the local Git history.

## Project notebook and evidence

The code repository is not the whole project record. Read these first:

```text
/home/openclaw/research-agent/projects/petta-memory/PROJECT.md
/home/openclaw/research-agent/projects/petta-memory/TASKS.md
/home/openclaw/research-agent/projects/petta-memory/DECISIONS.md
/home/openclaw/research-agent/projects/petta-memory/NOTES.md
/home/openclaw/research-agent/projects/petta-memory/experiments/
/home/openclaw/research-agent/projects/petta-memory/docs/
```

- `PROJECT.md`: purpose, scope, repository links, current-state narrative, and
  the adopted Atlas-indexed reversible pi-PLN roadmap.
- `TASKS.md`: open, blocked, and completed work. It is long and partly
  chronological; verify claims in code/tests.
- `DECISIONS.md`: durable boundary decisions and why they were made.
- `NOTES.md`: detailed chronological work log.
- `experiments/`: reproducible provider-free and shadow-consumer run records.
- `docs/`: architectural assessments and designs, including PeTTaChainer,
  patham9 pi-PLN, two-strata memory, and metta-attention integration.

The most relevant general research rules for takeover work are: write the
behavioral spec before nontrivial edits, preserve modular abstraction seams,
and make progress claims reproducible and specific.

## GitHub and publishing

Remote repository:

```text
https://github.com/bgoertzel-sing/petta-memory
origin https://github.com/bgoertzel-sing/petta-memory.git
```

The repository is public. Do not push directly to the default branch. The safe
publication target is the existing takeover branch:

```bash
cd /home/openclaw/research-agent/projects/petta-memory/worktrees/protocosmo2-handoff
git status --short --branch
git log -5 --oneline --decorate
git remote -v
git push -u origin agent/protocosmo2-handoff
```

Before the first push, inspect the 352 local commits, run the full tests, run
`git diff --check`, and scan tracked/untracked content for credentials and
accidental large files. A branch push is appropriate; merging, force-pushing,
or pushing the default branch requires Ben's explicit approval.

### GitHub authentication: do not pass credentials in chat

The Pop!_OS account already has GitHub CLI authentication configured for
`bgoertzel-sing`, and HTTPS Git operations are configured to use it. A coding
agent running as the same OS user should use the existing credential helper,
not receive or print a token:

```bash
gh auth status
git config --get credential.helper
```

If the agent runs under a different OS account/container and cannot access the
existing credential helper, Ben or an operator should authenticate that
environment interactively with `gh auth login` (browser/device flow) or install
a narrowly scoped token in the platform's secret store. Never paste a token into
Telegram, an agent prompt, a repository file, shell command arguments, logs, or
project memory. Never commit `~/.config/gh/hosts.yml` or copy its contents.

## Repository map

### Top-level

| Path | Role |
|---|---|
| `README.md` | Feature/boundary inventory and basic use. Long, but currently the best repository-level capability list. |
| `pyproject.toml` | Python package metadata and the `petta-memory` console entry point. No mandatory third-party runtime dependency for the core store. |
| `src/petta_memory/` | Python implementation. |
| `tests/` | Stdlib `unittest` suite; pytest can also collect most tests. |
| `fixtures/` | Small MeTTa journals and end-to-end/routing/GoalChainer fixtures. |
| `examples/` | Example fresh-message, idle, and group-memory episodes. |
| `artifacts/` | Checked-in bounded research evidence and frozen runtime records; do not overwrite create-once artifacts. |
| `docs/` | Repository-local implementation status, GoalChainer handoff, OmegaClaw migration, and PeTTaChainer repair plan. |
| `scripts/provider_free_usability_gate.sh` | End-to-end provider-free usability/evidence gate. |

### Python modules

| Module | Practical role |
|---|---|
| `store.py` | Core `MemoryCluster` parser/validator and `MediumMemoryStore`; append, locking, query, status, audit/index/prompt/PLN and handoff views. Start here for memory semantics. |
| `sexpr.py` | Small deterministic S-expression parser/serializer used at trust boundaries. |
| `cli.py` | Command-line parser and dispatch for the store, views, bridges, smoke tests, inference-control tools, and profiles. |
| `omegaclaw.py` | Feature-flagged OmegaClaw read bridge; autonomous writes intentionally raise `LiveWriteDisabled`. |
| `petta_runtime.py` | Optional PeTTa-backed parse checker; keeps the core package dependency-free unless explicitly enabled. |
| `goalchainer_smoke.py` | Bounded external GoalChainer smoke gates; validates decision payloads and does not claim tasks or write memory. |
| `live_bridge.py` | Read-only memory -> ranked pi-PLN/patham9 -> GoalChainer bridge plus strict copied-metadata validation. |
| `patham9_pln.py` | Patham9/PLN adapters, handoffs, semantic-output parsing, smoke/derivation gates, inference-control planning, and meta-learning benchmarks. Large module; edit cautiously. |
| `pipln_models.py` | Immutable evidence, snapshot, chart, compiler, capture, result, replay, artifact, and manifest types. Also contains bounded subprocess and persistence boundaries. Large module. |
| `pettachainer_profile.py` | PeTTaChainer workload generation, source-gated fan-out diagnosis, repaired compile/add/query/derivation probes, and typed capture helpers. Large and tied to pinned local runtime source. |
| `usability_bundle.py` | Fail-closed validation of provider-free evidence bundles and read-only shadow-consumer artifacts. |
| `__init__.py` | Small public package surface. |

### Tests

Tests mirror module names. At the frozen head, the largest areas are:

- `test_patham9_pln.py`: roughly 296 test methods;
- `test_pettachainer_profile.py`: roughly 154;
- `test_pipln_models.py`: roughly 111;
- `test_store.py`: roughly 45;
- `test_usability_bundle.py`: roughly 33;
- `test_live_bridge.py`: roughly 27.

Use a focused file first, then the full suite.

## Basic setup and verification

The core tests are designed to run from the repository without installation:

```bash
cd /home/openclaw/research-agent/projects/petta-memory/worktrees/protocosmo2-handoff
PYTHONPATH=src python3 -m unittest discover -s tests -v
git diff --check
```

Historical expected baseline: 698 passing tests at commit `5b842f4`. A fresh
run on 2026-08-10 collected 698 tests in 22.211 seconds but ended with one
failure, one error, and eight skips. `test_one_rule_truth_formula_path_matches_pinned_source`
looked for PeTTaChainer beneath the isolated worktree rather than the project
`repos/` directory; `test_new_output_directory_is_private_despite_permissive_caller_umask`
then received no semantic `Passed: #t` marker from the patham9 derivation gate.
Treat dependency-path normalization as a takeover prerequisite. Record the
exact Python version, elapsed time, exit status, and skips. Do not silently
weaken a failing test.

For one focused area:

```bash
PYTHONPATH=src python3 -m unittest tests.test_store -v
PYTHONPATH=src python3 -m unittest tests.test_pipln_models -v
```

CLI discovery:

```bash
PYTHONPATH=src python3 -m petta_memory.cli --help
```

Provider-free usability gate:

```bash
scripts/provider_free_usability_gate.sh --help
```

Read the script before running it, choose a new output directory, and record a
run under the project `experiments/` ledger. Several artifact writers are
create-once by design.

## External local repositories and runtimes

Some integration code assumes sibling/local research trees. Resolve and record
their actual commits before making runtime claims. Expected references include:

```text
/home/openclaw/research-agent/projects/petta-memory/repos/patham9-pln
/home/openclaw/research-agent/projects/petta-memory/repos/PeTTa
/home/openclaw/research-agent/projects/petta-memory/repos/PeTTaChainer
/home/openclaw/research-agent/projects/omegaclaw/repos/OmegaClaw-GoalChainer
/home/openclaw/research-agent/projects/petta-memory/toolchains/local/swi-prolog-9.3.36/bin/swipl
```

Do not assume these paths or revisions are still correct merely because a
default constant names them. Inspect the filesystem and Git state. Historical
claims referenced patham9 revision `55f1751` and PeTTaChainer revision
`e4db5ca`, but current runtime work must re-pin what is actually used.

## Semantic and safety boundaries

These are core project requirements, not optional conservatism:

- Raw utterances and unpromoted quoted claims are not factual PLN premises.
- Derived STVs are not empirical evidence; explicit evidence bases/counts must
  remain distinguishable.
- Runtime success, shell exit 0, or a content hash alone does not establish a
  valid inference result.
- Promotion into canonical memory is separate from inference/result admission.
- OmegaClaw autonomous writes and GoalChainer task/directive claims remain
  disabled/rejected.
- Bounded runtime experiments must pin source/profile, inputs, budgets, output
  identities, and provenance.
- Existing checked-in artifacts may be immutable/create-once. Never overwrite
  them to make a test pass.

## What is implemented versus still open

Implemented and tested locally:

- append-only clustered memory, deterministic queries, and multiple bounded
  views;
- explicit promotion gate for PLN-safe exports;
- immutable evidence/snapshot/chart/compiler/capture/manifest substrate;
- patham9 program assembly, bounded capture, result admission, persistence,
  reload, and exact replay;
- PeTTaChainer fan-out diagnosis and a narrowly repaired exact-fact/one-rule
  path with typed non-promoting evidence;
- read-only GoalChainer/live-bridge and provider-free bundle validation.

Still open or deliberately closed:

- production ProtoCosmo2/OmegaClaw deployment;
- general autonomous journal writes;
- inferred-belief promotion from runtime results;
- general PeTTaChainer repair/upstream adoption;
- arbitrary proof/rule trace attribution;
- broad semantic corpus validation and production performance characterization;
- remote publication of the 352 local commits.

## Recommended first task for a takeover agent

1. Verify the worktree commit and clean state.
2. Normalize/configure dependency paths for the isolated worktree without
   copying or modifying the pinned dependency repositories.
3. Rerun the full 698-test suite and save exact output in a new experiment record.
4. Run the provider-free usability canary in a new output directory.
5. Audit the 352-commit remote gap and prepare a non-default branch push.
6. Report observed results before changing semantics.

After that canary, select one bounded frontier and write its acceptance test
before coding. A sensible first implementation task is a read-only production
retrieval canary for ProtoCosmo2, retaining a single writer and no promotion.

## Change workflow

- Work only in the isolated worktree/branch.
- Inspect `PROJECT.md`, `TASKS.md`, and `DECISIONS.md` for the affected boundary.
- Add a test demonstrating the intended behavior.
- Run the narrow test, then the full suite.
- Record dependency commits, commands, environment, exit status, and evidence.
- Update project records without duplicating long prose.
- Scan for secrets and accidental generated files.
- Make a focused local commit; push only the task branch.

If code contradicts project prose, preserve the contradiction, inspect Git and
tests, and update the prose only when the evidence resolves it.

## Handoff checklist

- [ ] `git rev-parse HEAD` is `5b842f4d8e203d86c0d14f42eb91a03535376c0a`.
- [ ] `git status --short --branch` is understood and user work is preserved.
- [ ] Full tests pass or every failure is recorded precisely.
- [ ] External dependency paths and commits are pinned for runtime work.
- [ ] No credentials appear in source, artifacts, logs, or prompts.
- [ ] The non-default publication branch and remote are explicit.
- [ ] The next task has a written acceptance test and evidence path.
