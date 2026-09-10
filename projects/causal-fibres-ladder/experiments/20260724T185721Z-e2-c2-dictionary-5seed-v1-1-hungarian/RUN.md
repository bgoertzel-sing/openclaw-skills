# Run 20260724T185721Z-e2-c2-dictionary-5seed-v1-1-hungarian: e2-c2-dictionary-5seed-v1-1-hungarian

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:57:21Z`
- Finished: `2026-07-24T19:03:27Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the mandatory C2 sparse-autoencoder baseline recover factor-aligned,
intervention-selective structure from the identical frozen E2 confirmation
fields where JBD failed?

## Hypothesis or expected behavior

If estimator choice binds, dictionary codes may pass frozen M3/M4 on
M5-observable blocks even though JBD did not. This does not retrospectively
authorize C2 atoms as E3 fibres.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `6029, 7331, 8641, 9941, 11251`.
- Source fields: exact hash-verified artifacts from confirmation run
  `20260724T181805Z-e2-confirmation-5seed-v1-1-frozen`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Dictionaries/codes/results: `artifacts/campaign/`.
- Machine disposition: `artifacts/c2_disposition.json`, SHA-256
  `380244b7052fd7a4f22c00a2a6c6b780dd763c032266ca0a8d49c0d03bcaf2cc`.

## Interpretation

**Observed:** all five seeds and 60 SAE fits completed. C2 passes frozen
M3/M4 on M5-observable settled block 6 and adjoint blocks 1--6. Eligible M3/M4
peaks co-locate with the frozen home blocks on both tracks. JBD passed no
block under the same confirmation set.

**Inferred:** estimator choice, rather than absence of all factor structure,
binds the JBD-negative E2 result. The operational branch remains E2-B because
E2-A preregistered JBD recovery and C2 was not an alternative fibre selector.
The broad phrase “structure sits at null” is superseded by “no
JBD-recoverable structure; C2 dictionary structure is positive.”

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Proceed to branch-5.2 E3 with supplied fibres only. Do not retrospectively
select C2 atoms without a separate preregistered selector/transport gate.
