# Run 20260724T202651Z-e4-channel-diagnostic-seed-13121-v2: e4-channel-diagnostic-seed-13121-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:26:51Z`
- Finished: `2026-07-24T20:27:03Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On one corrected exploratory seed, how do factor completeness, constraint weight, and injection channel affect E4 recovery?

## Hypothesis or expected behavior

Holding per-factor weight constant should permit a clean full4-versus-cap comparison; stronger weights and a logit bypass diagnose penalty and channel bottlenecks.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command; this is one of three calibration seeds.
- Contract: `configs/e4_channel_diagnostic_v2.json`; 36 factorial conditions plus FF and diagnostic TC per split.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

All conditions completed with monotone guarded optimization and unchanged model weights. The three-seed aggregate finds nearly 2x completeness gain, strictly increasing recovery through 5x, and about 2.45x logit-over-hidden recovery. See `../20260724T202915Z-e4-channel-diagnostic-summary-v2/RUN.md`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use only the three-seed aggregate for the exploratory diagnostic read; do not revise the frozen E4 gate.
