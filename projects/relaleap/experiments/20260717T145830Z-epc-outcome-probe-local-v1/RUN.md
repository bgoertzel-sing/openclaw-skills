# Run 20260717T145830Z-epc-outcome-probe-local-v1: epc-outcome-probe-local-v1

- Project: `relaleap`
- Started: `2026-07-17T14:58:30Z`
- Finished: `2026-07-17T14:58:34Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Do the frozen structural and common-rule adaptation probes execute
deterministically on matched small BP, KD, and ePC networks, and is a
chronological Tiny Shakespeare split informative enough for a later scientific
comparison?

## Hypothesis or expected behavior

Expected before outcome inspection: metric controls and repeated execution are
deterministic and finite. This two-seed run is an instrumentation/effect-size
pilot only. It cannot establish an ePC advantage. A useful domain shift should
produce positive domain-A forgetting after common domain-B adaptation; absence
of forgetting makes the plasticity endpoint uninformative.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Source commit: `e398876` on `agent/epc-outcome-probes`, clean at execution.
- Seeds: `113`, `271`.
- Corpus: canonical Tiny Shakespeare, SHA-256 recorded in `metrics.json`.
- Frozen config: `configs/epc_outcome_probe_local.json`, hash recorded in the
  artifact.
- Domain A/B: disjoint first/second halves of the training token stream.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Metrics: `artifacts/metrics.json`, SHA-256
  `416bc97590746ec7988f7b0ad8bcda4304924c3794490bcf18a95b83cac5ae90`.
- A second execution produced the exact same artifact hash.
- Mean domain-A forgetting (post minus pre loss): BP `-0.016205`, KD
  `-0.016195`, ePC `-0.016145`.
- Mean domain-B adaptation gain: BP `0.016584`, KD `0.016568`, ePC `0.016521`.
- Corresponding-layer linear CKA was approximately `0.99985` to `1.0`.
- Effective-rank, block-skip, and corruption summaries were nearly identical.

## Interpretation

**Observed:** the runner and metrics are finite and byte-deterministic. The
three arms are almost indistinguishable at this scale. Common domain-B
adaptation also improves domain-A loss, so the chronological halves do not
induce measurable forgetting. Ten-percent token corruption slightly improves
loss in all arms, another sign that these barely trained models are not a useful
robustness test.

**Interpretation:** the instrument gate passes, but the chosen local shift and
training budget are scientifically uninformative. This is neither evidence for
nor against an ePC plasticity advantage. Do not tune this tiny run after seeing
the outcome. Use it to harden the scalable runner, then freeze a genuinely
shifted domain and adequately trained checkpoint protocol.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Add checkpoint preservation and this probe battery to a fresh matched
GPT-2-small run. Freeze a real domain shift, three or more seeds, common
adaptation budget, and joint uncertainty analysis before requesting bounded
RunPod approval. The July 17 aborted artifacts remain ineligible.
