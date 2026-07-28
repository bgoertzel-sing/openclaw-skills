# Run 20260716T152520Z-exp07-detector-invariance: exp07-detector-invariance

- Project: `petta-chem`
- Started: `2026-07-16T15:25:20Z`
- Finished: `2026-07-16T15:25:20Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/petta-chem/repos/petta-chem`

## Question

Does the canonical exp04 RAF detector return identical outputs for identical
rule-pool, food-set, and catalysis inputs regardless of intervening calls or
tick-history metadata, while retaining single-result committed PeTTa clauses?

## Hypothesis or expected behavior

Expected: positive A -> no-catalysis B -> positive A reproduces identical A
metrics; direct and advanced seed-31 histories that project to identical
detector inputs reproduce identical metrics; committed PeTTa detector heads,
catalysis dispatches, and 18 ground edges remain unique and mutation-free.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Fixture: `exp07-seeded-dynamic-positive-control-seed-31`.
- Canonical detector: `experiments/exp04/run_rich_raf.py`.
- Canonical facts: `src/chem_exp04.metta` (18 ground catalysis edges).
- Scope: seeded positive control only; no exp07 experimental arm was loaded.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifact: `artifacts/detector-invariance.json`.
- Artifact SHA-256: `b64204bac415521dff4c80d41b324e3344b5bc6f0b3ac00b4de4ec8d3d357c61`.
- Call-order invariance: passed; positive A remained RAF 15 around the
  no-catalysis B call (RAF 0).
- Tick/path invariance: passed; direct tick-22 and advanced ticks 3--22
  histories both returned RAF 15 and core `{lCD, lBCD2}`.
- Single-result/uniqueness guard: passed; top-level RAF, RA, and FG heads each
  occur once; specific/ablated catalysis dispatches each occur once; all 18
  catalysis edges are unique; no guarded mutable PeTTa form was found.

## Interpretation

**Observed:** All three checks returned true with exit status 0. The detector
reproduced maximal RAF 15, minimal core size 2 (`lCD`, `lBCD2`), and
`minimal_core_is_raf=true` for both histories. The intervening no-catalysis
call returned RAF 0 without changing the repeated positive output.

**Interpretation:** The current canonical detector behaves as a pure function
of its detector inputs across calls and path metadata. Static guards make a
future duplicate equation, mutable PeTTa detector form, host decorator, or
host `global`/`nonlocal` dependency fail loudly.

**Boundary:** The two histories deliberately project to identical detector
inputs; this tests detector statelessness, not chemistry-path equivalence. It
does not inspect the registered exp07 arms, amend N=20, or support an emergence
claim.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

To preserve the machine-readable metrics explicitly:

```bash
scripts/run_exp07_detector_invariance.sh artifacts/detector-invariance.json
```

## Follow-up

Keep this guard in the pre-N=20 validation suite. Implement the registered
20-tick trajectories separately, with replenishment at ticks 8/13/18.
