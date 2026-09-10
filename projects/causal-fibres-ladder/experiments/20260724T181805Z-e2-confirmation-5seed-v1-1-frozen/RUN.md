# Run 20260724T181805Z-e2-confirmation-5seed-v1-1-frozen: e2-confirmation-5seed-v1-1-frozen

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:18:05Z`
- Finished: `2026-07-24T18:19:16Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Under frozen criteria, do settled-error or adjoint fields qualify as E2-A,
E2-B, or E2-C, and does Prediction 2 co-location pass?

## Hypothesis or expected behavior

E2-A requires non-null M1/M2, at least two M3-aligned depth blocks, and
M4 diagonal dominance. E2-C applies if M5 is near zero; otherwise a
concentrated but structurally sub-threshold result is E2-B.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `6029, 7331, 8641, 9941, 11251`.
- Frozen criteria SHA-256:
  `d896798d73052fb327efadfe451c55bd3fe64e4a2f42259a7a3348bc8f1f9720`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Seed artifacts: `artifacts/campaign/`.
- Machine disposition: `artifacts/e2_disposition.json`, SHA-256
  `723674cfa4acd94fd985ae83afcd1d5ccf6d509b209cba63b5e0a564039d6972`.

## Interpretation

**Observed:** all five seeds completed and all 60 JBD fits converged. Settled
top-5% mass is entirely in block 6; adjoint mass is concentrated in blocks
1--2. M1 passes in settled blocks 3--6 and every adjoint block. Settled block
6 and every adjoint block pass M5 observability.

**Observed:** no block passes M2, reaches the M3 mean-MI floor `0.20`, or
reaches the M4 diagonal/off-diagonal ratio `2.0`. Settled M3/M4 peak at depth
blocks 3/6; adjoint M3/M4 peak at 4/5. M0 has zero equivalent blocks.

**Inferred:** both tracks and the joint read are E2-B, not E2-A or E2-C.
Prediction 2 fails. No recovered fibre may advance to E3.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Proceed to E3 only under programme branch 5.2, using supplied fibres clearly
labelled as imposed structure. See `../../docs/e2_disposition_memo.md`.
