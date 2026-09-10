# Run 20260724T202325Z-e4-channel-diagnostic-seed-13121-v1: e4-channel-diagnostic-seed-13121-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:23:25Z`
- Finished: `2026-07-24T20:23:35Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does one exploratory seed separate E4 information completeness, constraint weight, and injection channel?

## Hypothesis or expected behavior

The 36-condition factorial grid should reveal whether full information, stronger constraints, or a direct-logit bypass improves FF-to-TC headroom recovery.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command; the frozen 75-update student, ID/CS splits, and diagnostic TC anchor are unchanged.
- Contract: `configs/e4_channel_diagnostic_v1.json`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

All 38 conditions per split completed with frozen model weights. Post-run audit found that mean BCE diluted per-factor weight for full4 relative to two-factor caps; retain this run for channel and aggregate-weight provenance, but use corrected v2 for completeness conclusions.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Superseded for completeness by the corresponding v2 normalization-corrected seed run.
