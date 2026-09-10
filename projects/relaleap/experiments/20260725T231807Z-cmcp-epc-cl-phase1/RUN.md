# CMCP-guided ePC continual-learning Phase 1

- Experiment ID: `20260725T231807Z-cmcp-epc-cl-phase1`
- Project: `relaleap`
- Status: `complete_negative`
- Frozen: `2026-07-25T23:18:07Z`
- Execution: local CPU only
- Repository: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`
- Source branch: `agent/cmcp-epc-cl-experiment`
- Parent commit: `12caf1b`
- Runner commit: `388d7d6`

## Scientific question

At normalized total KD mass 1.0 and identical student initialization, optimizer,
schedule, batch shapes, and update count, does response-novelty CMCP guidance
combined with two-step ePC improve continual learning and representation quality
relative to BP, ordinary KD, CMCP-KD without ePC, and ordinary ePC?

## Research-rule focus

Rules 1, 2, 3, 5, and 7 are primary: validate weighting and ePC invariants,
freeze a plain-language protocol first, reuse the existing transformer/ePC and
probe implementations, preserve exact evidence, and keep weighting, objectives,
and evaluation as separate seams.

## Frozen protocol

- Data A: canonical Tiny Shakespeare character corpus, deterministic 90/10
  split, local file SHA-256
  `86c4e6aa9db7c042ec79f339dcb96d42b0075e16b8fc2e86bf0ca57e2dc565ed`.
- Task B: deterministic modular arithmetic sequences with decreasing direction.
- Architecture: two-block `CausalCharTransformerLM`, vocabulary equal to the
  Tiny Shakespeare character vocabulary, sequence length 32, `d_model=32`,
  two heads, feed-forward width 64, dropout 0.
- Seeds: `1729, 3253, 6421`.
- Teacher A: BP/CE on Tiny Shakespeare for 2,000 updates.
- Complementary teacher: BP/CE on increasing modular arithmetic for 2,000
  updates. Both teachers are frozen before student training.
- Student training: 2,000 updates, batch 128, AdamW, identical per-seed initial
  state and frozen batch stream for every arm.
- Arms:
  1. `bp`: Task-A CE only.
  2. `kd`: Task-A CE plus ordinary KD from teacher A.
  3. `cmcp_kd`: Task-A CE plus response-novelty-weighted KD from both teachers.
  4. `epc`: Task-A CE plus two-step ePC from teacher A.
  5. `cmcp_epc`: Task-A CE plus response-novelty-weighted two-step ePC packets
     from both teachers.
- Every KD-bearing arm normalizes nonnegative packet weights to exactly 1.0 per
  update. `bp` has KD mass 0 by definition. The CE coefficient is 1.0 and the
  KD/ePC coefficient is 0.02, fixed across KD-bearing arms; temperature is 2.0.
- Compute matching: update count, batch shape, optimizer, schedule, teacher
  packet construction, and teacher-forward cache are matched. Actual wall time,
  ePC objective calls, and relaxation traces are reported; ePC's inherent extra
  relaxation work is not hidden. Scientific comparisons are update-matched,
  not falsely claimed wall-clock matched.
- Frozen evaluation batches are generated before training and reused across
  arms. Pre-adaptation evaluation includes Task-A loss/perplexity/accuracy,
  per-state CKA against teacher A (feature and Gram implementations must agree),
  centered entropy effective rank and participation ratio, block-skip loss, and
  token-corruption loss/accuracy at probabilities 0.1 and 0.3.
- Continual-learning evaluation applies the same 200-update Task-B CE adaptation
  stream and learning rate to every checkpoint. It records the Task-B loss
  curve and trapezoidal AUC, Task-A loss increase, and Task-A accuracy
  retention.
- Checkpoints and raw JSON are retained. Aggregate means, sample standard
  deviations, and paired arm differences are computed over the three seeds.

## Preregistered predictions

1. `cmcp_epc` will have lower Task-A forgetting than `epc`, because balanced
   evidence should reduce destructive specialization.
2. `cmcp_epc` will have higher centered effective rank and participation ratio
   than `kd`, with no representation-collapse signature.
3. A continual-learning advantage may trade off against worse immediate Task-A
   perplexity.

## Acceptance gate

The run is informative regardless of direction. Promotion to Phase 2 requires
`cmcp_epc` to beat `cmcp_kd` in at least one preregistered functional CL metric
(lower forgetting, higher accuracy retention, or lower Task-B adaptation AUC)
and at least one representation metric (higher mean hidden-state entropy rank or
participation ratio), without non-finite results or failed ePC monotonicity.
Otherwise the result is negative and Phase 2 is not triggered.

## Planned command and evidence

The exact executable command is frozen in `command.sh`. Standard output and
error go to `stdout.log` and `stderr.log`; exit status and timing go to
`status.json`; raw metrics go to `artifacts/results.json`.

## Results

### Direct observations

- Command exit status: 0. All 15 arm/seed records and 15 checkpoints were
  produced in 35:22 wall time. Maximum resident memory was 8,978,736 KiB.
- Every KD-bearing record had mean/min/max applied KD mass exactly 1.0.
  CMCP assigned the complementary packet mean weight 0.49994. All 18,000 ePC
  packet objectives had monotone two-state energy traces.
- Focused post-run regression suite:
  `test_cmcp_distillation.py`, `test_hdpc_tinyshakespeare.py`, and
  `test_outcome_probes.py`: 16 passed in 1.26 s.
- Complete repository suite from the nested repository root:
  `PYTHONPATH=src .../.venv/bin/python -m pytest tests -q`:
  420 passed, 1 skipped in 22.74 s. A preceding invocation from the outer
  workspace failed collection because the repository-local `scripts` namespace
  was not on the import path; rerunning from the correct recorded working
  directory resolved it without code changes.

Three-seed means (sample SD in parentheses):

| arm | A ppl | B adapt AUC | A forgetting | A acc retention | entropy rank | participation |
|---|---:|---:|---:|---:|---:|---:|
| BP | 8.065 (.163) | 2.231 (.025) | 3.410 (.098) | .110 (.005) | 12.278 (.536) | 7.525 (.532) |
| KD | 7.984 (.164) | 2.281 (.041) | 3.665 (.187) | .103 (.017) | 11.419 (.297) | 6.837 (.362) |
| CMCP-KD | 11.063 (.057) | 1.904 (.019) | 4.009 (.094) | .107 (.018) | 12.701 (.677) | 7.665 (.466) |
| ePC | 8.172 (.093) | 2.288 (.056) | 3.670 (.137) | .098 (.024) | 13.482 (.308) | 8.117 (.335) |
| CMCP-ePC | 9.970 (.119) | 1.994 (.018) | 4.868 (.127) | .104 (.016) | 12.234 (.368) | 8.095 (.330) |

Mean CKA versus teacher was BP .730, KD .747, CMCP-KD .719, ePC .705,
and CMCP-ePC .602. Mean corruption accuracies at p=.1/.3 were respectively:
BP .332/.247, KD .334/.248, CMCP-KD .293/.213, ePC .330/.246, and
CMCP-ePC .321/.240. Block-skip losses and all per-state metrics are preserved
in `artifacts/results.json`.

Mean student-training wall seconds were BP 41.9, KD 66.8, CMCP-KD 103.0, ePC
122.7, and CMCP-ePC 209.6. Thus the arms are update/batch/KD-mass matched but
not wall-clock matched; CMCP-ePC cost 1.71x ePC and 2.03x CMCP-KD.

### Prediction audit

1. **Contradicted:** CMCP-ePC forgetting was worse than ePC in every seed
   (means 4.868 versus 3.670), although accuracy retention was slightly higher
   on average (.104 versus .098).
2. **Partly supported:** CMCP-ePC exceeded ordinary KD in entropy rank
   (12.234 versus 11.419) and participation ratio (8.095 versus 6.837), but it
   did not exceed ePC and had the lowest teacher CKA.
3. **Supported:** the faster Task-B adaptation came with worse Task-A
   perplexity.

### Interpretation

Response-novelty weighting mostly split mass evenly between these two highly
different teachers. That produced a reproducible plasticity/retention tradeoff:
both CMCP arms adapted to arithmetic faster, but retained Shakespeare worse.
Two-step ePC did not repair this tradeoff. The increased rank relative to
ordinary KD is descriptive and is not evidence of better representation by
itself, especially given lower CKA, robustness, and functional retention.

An alternative explanation is fixture mismatch rather than a general failure
of CMCP: complementary arithmetic logits on Shakespeare inputs may be novel but
not conditionally useful for preserving Task A. This experiment identifies
response novelty as insufficient evidence of usefulness in this cross-domain
packet construction.

### Acceptance decision

`phase2_promotion_gate=false`. CMCP-ePC beat CMCP-KD on participation ratio
(8.095 versus 7.665) but on none of the required functional CL endpoints:
adaptation AUC 1.994 versus 1.904 (higher is worse), forgetting 4.868 versus
4.009 (higher is worse), and accuracy retention .104 versus .107. Phase 2
GPT-2 paid compute is not triggered and no resource was provisioned.

### Artifacts and hashes

- `artifacts/results.json`:
  `84724abe4a3c2e48112f1399a01f100a419ca2c2f0ec621e308cdf4beff744c4`
- `command.sh`:
  `230c743a4a2a3afae2b2eb5e2143b90daf3c483c9897be1a09a4e94bde0bb909`
- `stdout.log`:
  `ebde2f1e56fc2b40adcb4c8a20f59c008ed03cf33c71ddcd641305a7b83b1303`
- Checkpoint hash manifest: `checkpoint_hashes.sha256` (manifest SHA-256
  `43d03207f60f17a41ddd3ff0b5a38e181ffff5eca312c058e98a40c472b2a4ad`).

Reproduce by running `command.sh` from this directory with the recorded venv.
