# Run 20260726T185730Z-v01-three-spec-install-report: v01-three-spec-install-report

- Project: `specatom-hs`
- Started: `2026-07-26T18:57:30Z`
- Finished: `2026-07-26T18:59:28Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/specatom-hs/repos/specatom-hs`

## Question

Can a clean local installation of the frozen Plain2Metta v0.1 profile carry
three representative specs from input to JSON, reified MeTTa, and diagnostics?

## Hypothesis or expected behavior

The package installs without application dependencies and each example exits
zero while emitting three nonempty report artifacts.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.
- Inputs: bundled `examples/auth_service.plain`, `task_manager.plain`, and
  `ml_timeseries.plain`; no random seeds or remote inputs.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Artifact summary: `artifacts/summary.json` (SHA-256
  `263d78ea3d43fdaa8d015932723bc4ac66bfa69f9cfbfb8926faeedd842238e1`).
- The complete temporary output set was 452 MiB because source-provenance-rich
  JSON/MeTTa is large; the summary preserves all source/output digests rather
  than duplicating that generated bulk in the notebook.

## Interpretation

**Observed:** all three installed CLI invocations exited zero. The output
summary records 95/30/36 semantic objects and 165,592/54,432/56,952 checks for
auth-service/task-manager/ML-time-series respectively.

**Inferred:** the stated narrow internal-alpha usability claim is now supported
by an install-to-report run, although this is not a claim of arbitrary English
understanding or executable generation.

## Reproduction

Run `command.sh`; it invokes `scripts/usability-gate.sh` in the exact recorded
repository state. Use a new output path because the gate refuses overwrite.

## Follow-up

Keep generated artifacts compressed or externally archived if a human wants to
inspect full 452 MiB outputs; product work should address output size/ergonomics.
