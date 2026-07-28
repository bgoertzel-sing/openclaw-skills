# Run 20260715T153035Z-epc-distillation-gate-local-r2: epc-distillation-gate-local-r2

- Project: `relaleap`
- Started: `2026-07-15T15:30:35Z`
- Finished: `2026-07-15T15:30:42Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Does the committed block-state ePC objective beat matched BP and ordinary KD on
fixed Tiny Shakespeare minibatches while preserving endpoint, energy, and
gradient invariants?

## Hypothesis or expected behavior

Expected behavior: `T=1` reproduces ordinary KD; all `T>1` energy traces are
monotone; promotion occurs only if one nontrivial depth beats BP and matched KD
in all three seeds.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds: `11,29,47`; corpus SHA-256 recorded in the JSON artifact.
- Grid: `lambda={0,.001,.01,.05}`, ePC inference depth `T={1,2,4,8}`;
  distillation temperature fixed separately at 2.0.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: all ePC energy and finite-gradient invariants passed, and the `T=1`
endpoint matched ordinary KD to floating-point precision. The promotion gate
failed for every genuine `T>1` candidate. Mean held-out perplexity was 76.2118
for BP; matched KD means were 76.2093, 76.1900, and 76.1809 as lambda increased.
The corresponding best nontrivial-depth ePC means were 76.2101, 76.1978, and
76.1906, respectively: close, but consistently worse than matched KD. Mean wall
time increased from about 0.025 s for KD to 0.074/0.107/0.175 s for ePC depths
2/4/8 at lambda 0.001, with similar scaling elsewhere.

Decision: fail closed. This diagnostic-scale run validates execution and core
invariants but gives no evidence for an ePC perplexity benefit. Do not proceed
to longer training or a columnar/crown head on this result. The next change must
be mechanistically motivated and preregistered rather than selected on these
held-out rows.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it. Raw JSON is
also preserved at `artifacts/epc_distillation_gate_local_20260715.json`.

## Follow-up

Inspect why relaxed local KD gradients lag ordinary KD despite monotone energy,
especially layerwise norm ratios and whether the output KL/local-error scaling
is comparable across depths. Add a synthetic teacher/student case with a known
useful local-credit signal before another Tiny Shakespeare outcome run.
