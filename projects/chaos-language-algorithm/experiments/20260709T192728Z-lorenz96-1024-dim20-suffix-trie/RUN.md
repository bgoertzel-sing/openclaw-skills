# Run 20260709T192728Z-lorenz96-1024-dim20-suffix-trie: Lorenz-96 1024-step × 20D suffix-trie CLA smoke

- Project: `chaos-language-algorithm`
- Started: `2026-07-09T19:27:28Z`
- Finished: `2026-07-09T19:27:32Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/chaos-language-algorithm/repos/chaoslang`

## Question

Can the local `chaoslang` prototype, after local-main suffix-trie miner integration, run the narrowest meaningful OmegaSim-scale dimensionality benchmark: a 1024-step, ~20D CLA stream using deterministic Lorenz-96 M1 symbols, JS category proposal path, and suffix-trie chunk miner?

## Hypothesis or expected behavior

Expected: the benchmark completes locally without remote/paid compute, preserves exact reconstruction, and reports basic compression/grammar metrics. This is a smoke/control run, not a validated OmegaSim detector calibration.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Repository commit: `b344aa3c1a4b5a5eeef93fc2ea239a7f75c97429`
- Dirty state: benchmark CLI modified to expose `--miner`, `--category-method`, `--js-threshold`, and fit wall time.
- System: Lorenz-96
- Dimension: 20
- Steps: 1024
- Discard: 256
- Bins: 4
- Iterations: 8
- Seed: 0
- Miner: `suffix_trie`
- Category method: `js`
- JS threshold: 0.1
- Lorenz-96 deterministic initial condition used by CLI: `[8.0] * 19 + [8.01]`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log` (empty)
- Machine status: `status.json`
- Artifacts: `artifacts/`

### Metrics from stdout

| Metric | Value |
|---|---:|
| exact_reconstruction | true |
| symbol_count | 1024 |
| unique_symbols | 510 |
| rules_learned | 8 |
| score_total | 1021.2 |
| fit_wall_time_seconds | 2.554301110096276 |
| history_length | 8 |

### Artifact hashes

```text
17d2a47476b6c18c719d359d3464aad6c89dccecc4a28204c8be1b33c1781526  stdout.log
7e77b80e2eccbd7328ea57f056e5e490ddbd91a0a67ddb3587343296a1f7341d  command.sh
```

## Interpretation

Direct observations:

- The local benchmark completed in about 4 seconds wall-clock including experiment harness overhead; model fit time reported by the CLI was ~2.55 seconds.
- Exact reconstruction held for the full 1024-symbol 20D stream.
- The stream was high-cardinality under M1 symbolization: 510 unique compound symbols out of 1024 positions.
- The greedy loop accepted 8 chunk rules. No explicit category edit was accepted in the history for this run.
- The final approximate MDL score was 1021.2, close to one score unit per input symbol, suggesting this M1 20D stream remains only weakly compressible by current chunk/category machinery at these settings.

Inference/limitations:

- This satisfies the first local OmegaSim-scale dimensionality smoke target (1024 × 20D) without needing a missing external JS/dimension-reduction path.
- It is still a Lorenz-96 control, not an OmegaSim trace, and uses direct 20D fixed-bin compound symbols rather than a learned dimension reduction or semantic state projection.
- The run does not compare old brute-force mining against suffix-trie mining because the local `NGramPatternMiner` on `main` has already been replaced internally by a bounded suffix-trie implementation; only the legacy wrapper `SuffixTrieMiner` remains selectable as a named path.
- The CLI now records fit wall time but not peak memory. A follow-up should add lightweight memory reporting or an external `/usr/bin/time -v` harness if memory is a key review metric.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

1. Add a dedicated benchmark command or script that compares the named miner paths on the same 1024 × 20D stream and captures peak RSS.
2. Preserve or reconstruct a true old brute-force miner fixture if reviewer comparison requires brute-force-vs-trie evidence.
3. Once an OmegaSim trace export or dimension-reduction symbolization path exists, rerun this same harness on real OmegaSim starter-vector traces.
