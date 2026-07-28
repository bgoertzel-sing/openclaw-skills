# Run 20260719T233244Z-epc-correctness-audit-v2: epc-correctness-audit-v2

- Project: `relaleap`
- Started: `2026-07-19T23:32:44Z`
- Finished: `2026-07-19T23:33:14Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Do the representation-rank and CKA observations survive a correctness audit
using standard centered linear CKA and identical real WikiText/TinyStories
samples for every one of the nine preserved checkpoints?

## Hypothesis or expected behavior

Standard CKA must be symmetric and agree between feature-space and centered-
Gram formulations. Real-data centered effective rank may remain lower for ePC,
but the prior random-token CKA values are not assumed valid.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Checkpoints: preserved Run-2 3 seeds x 3 arms at
  `20260718T073312Z-epc-outcome-6layer-run2`.
- Probe shape: 4 segments x 64 tokens for WikiText validation, TinyStories
  validation, and seed-42 random-token OOD control.
- Exact token and dataset-server response hashes are embedded in
  `artifacts/representation_audit.json`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Primary artifact: `artifacts/representation_audit.json`, SHA-256
  `7ffa94aa519cfe53a93e623863260752c22e5d88c8040d545b6afabd3681da72`.

## Interpretation

**Observed:** The audit passed with maximum CKA symmetry error `4.44e-16`
and maximum feature-vs-Gram formulation error `2.34e-12`. BP within-arm
mean CKA is high on real data (roughly 0.84-0.93), contradicting the prior
CPU battery's 0.003-0.007 claim. ePC centered entropy effective rank remains
much lower in middle/final layers: roughly 2.7-3.8 versus 23-42 for BP
controls. ePC seeds 1729 and 6421 are similar in later layers (WikiText CKA
about 0.91), while seed 3253 differs sharply from both (about 0.03).

**Inference:** Real-data low rank is robust descriptive evidence. The old D3
CKA implementation and its interpretation are rejected. Low rank is not yet a
demonstrated cause of poor adaptation or a demonstrated credit-assignment
failure.

**Limitation:** Public real-data rows were retrieved through the Hugging Face
dataset-server API; response and token hashes freeze the actual inputs, but the
API response was not revision-addressed. Random tokens are OOD control only.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the no-update real-teacher component/gradient scale audit before selecting
any repaired-ePC training coefficient.
