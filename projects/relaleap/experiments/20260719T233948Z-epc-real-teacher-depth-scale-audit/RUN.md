# Run 20260719T233948Z-epc-real-teacher-depth-scale-audit: epc-real-teacher-depth-scale-audit

- Project: `relaleap`
- Started: `2026-07-19T23:39:48Z`
- Finished: `2026-07-19T23:40:31Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

On one frozen real WikiText batch and the preregistered seed-3253 historical
ePC checkpoint, how do objective scales, credit propagation, and gradient
alignment vary across lambda `{0.005,0.05,0.5,5,50}` and activity-state count
`{4,8,12}` without optimizer updates?

## Hypothesis or expected behavior

The historical four-state setting may starve early blocks because prediction
error propagates backward only through a finite relaxation wavefront. Larger
lambda may amplify credit but need not improve direction or stationarity.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Checkpoint: `seed3253_epc_kd` from the preserved Run-2 checkpoint set.
- Teacher: `openai-community/gpt2` revision
  `607a30d783dfa663caf39e06633721c8d4cfcd7e`.
- Data: first 32 frozen tokens from the hashed WikiText dataset-server response;
  exact response/token hashes are in the primary artifact.
- Optimizer updates: zero.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Primary artifact: `artifacts/scale_audit.json`, SHA-256
  `7c0605d5f1f6295a985fecff19affa937b889195bdfb5356044be0c8706806ad`.

## Interpretation

**Observed:** Ordinary-KD parameter-gradient norm was `444.38`. At historical
`T=4, lambda=0.05`, ePC norm was `4.81`, cosine `0.460`, blocks 0-3 had exactly
zero parameter gradient, and only blocks 4-5 received credit. At `T=8`, the
same lambda reached blocks 2-5 but block-2 norm was only `0.00035`; at `T=12`
all blocks were technically nonzero, but block-0 norm was `4.85e-7` versus
ordinary KD `266.3`. Raising lambda to 5 or 50 made all blocks nonzero at
T>=8, but produced large nonstationarity and poor/negative alignment (overall
cosine about `-0.16` for lambda 5); it is not a clean repair. Weighted KD
dominated the raw post-relaxation local energy throughout this fixed-batch
audit.

**Inference:** Four activity states create a finite credit-propagation
wavefront that starves the early half of a six-layer student. Increasing lambda
mostly amplifies late/blockwise gradients and can rotate them away from
ordinary KD. Neither `lambda=5` nor `50` is justified for training. A deeper
inference arm and an explicitly normalized objective are more informative GPU
screen candidates than a naive high-lambda arm.

**Limitations:** One checkpoint and one short real batch; endpoint checkpoint
rather than initialization/training trajectory; Adam/clipping effects absent;
the result diagnoses mechanism scale but does not establish a training repair.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze a 200-update seed-3253 GPU screen with common initialization/batches:
BP+KD, historical T4/lambda.05 ePC, deeper current-semantics ePC, and a
normalized-energy ePC. Instrument pre/post-clip norms and Adam moments and save
checkpoints at 0/10/50/100/200.
