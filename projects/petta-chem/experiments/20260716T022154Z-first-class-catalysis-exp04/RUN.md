# Run 20260716T022154Z-first-class-catalysis-exp04: first-class-catalysis-exp04

- Project: `petta-chem`
- Started: `2026-07-16T02:21:54Z`
- Finished: `2026-07-16T02:21:55Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/petta-chem/repos/petta-chem`

## Question

Can exp04 materialize catalysis as a first-class binary PeTTa relation and make
the existing maximal-RAF reference consume that relation without changing the
seeded positive or no-catalysis results?

## Hypothesis or expected behavior

Expected: PeTTa exposes 18 `(catalyzes Molecule RuleId)` edges; PeTTa smoke
tests query those edges and show the shared positive/ablated RA interface;
the reference detector reproduces maximal RAF 15, greedy core 2
(`lCD`, `lBCD2`), core RAF true, and empty-relation ablation 0.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Source fixture: exp04 20-rule rich chemistry in `src/chem_exp04.metta`.
- Catalysis representation: binary, 18 materialized PeTTa edges.
- Runtime: repository-pinned `scripts/run_exp04.sh` PeTTa/SWI configuration.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Reference gate: 18 edges, maximal RAF 15, core 2, ablation 0.
- PeTTa smoke: 79 assertions passed.
- Python compilation and `git diff --check`: passed.

## Interpretation

**Observed:** The first-class PeTTa relation contains 18 explicit
molecule-to-rule edges. PeTTa queries and the relation-parameterized ablation
check passed. The host reference loaded those PeTTa facts instead of calling
the structural template matcher and reproduced maximal RAF size 15, greedy
core `lCD`/`lBCD2`, core RAF true, 56 events, and empty-relation RAF size 0.

**Interpretation:** The catalysis interface is now first-class and the seeded
RAF reference is faithful across the port. Structural template matching remains
only as provenance for how the initial relation was materialized and for the
older reduction sweep; it is no longer the exp04 reference detector interface.

**Boundary:** This validates a seeded positive and its causal catalysis
ablation. It is not evidence of unseeded ACS emergence.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use the first-class relation in the exp07 native/weak-guidance/shuffled-control
ensemble and compute RAF incidence/persistence without terminal forcing.
