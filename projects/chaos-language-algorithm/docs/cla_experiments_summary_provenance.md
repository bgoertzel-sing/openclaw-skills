# CLA experiments summary provenance

This note records evidence inspected for `cla_experiments_summary.tex` on 2026-07-09. The LaTeX paper is ASCII-only; this provenance note is also written with ASCII punctuation.

## Project records inspected

- `projects/chaos-language-algorithm/PROJECT.md`
- `projects/chaos-language-algorithm/TASKS.md`
- `projects/chaos-language-algorithm/DECISIONS.md`
- `projects/chaos-language-algorithm/NOTES.md`
- `projects/chaos-language-algorithm/docs/cla_expert_review_prompt.md`
- `projects/chaos-language-algorithm/docs/cla_five_attractor_systems_summary.tex`
- `projects/chaos-language-algorithm/docs/cla_standard_attractor_summary.tex`

The two earlier summaries were treated as orientation only. Claims in the new paper were checked against experiment records, source, tests, or Git history. Their stronger statements about entropy, monotonic scaling, OmegaSim field counts, and calibrated bits were not adopted where primary evidence was missing or conflicting.

## Project-level experiment record inspected

All files in `projects/chaos-language-algorithm/experiments/20260709T192728Z-lorenz96-1024-dim20-suffix-trie/` were inspected:

- `RUN.md`
- `command.sh`
- `env.txt`
- `git.txt`
- `status.json`
- `stdout.log`
- `stderr.log`
- `artifacts/` (empty)

## Repository records inspected

Repository root: `projects/chaos-language-algorithm/repos/chaoslang`

- `README.md`
- `pyproject.toml`
- `AUTOMATION_STATUS.md`
- Git status, local and remote branches, remotes, recent graph/log, branch containment, and the dirty diff for `src/chaoslang/benchmarks/m1_controls.py`
- Git history and stats for commits `0152027`, `1501346`, `97cfb4f`, and `b344aa3`
- Historical pre-trie `src/chaoslang/mining/ngram.py` from `b344aa3^`
- `src/chaoslang/api.py`
- `src/chaoslang/benchmarks/attractors.py`
- `src/chaoslang/benchmarks/m1_controls.py`
- `src/chaoslang/core/edits.py`
- `src/chaoslang/categorization/context.py`
- `src/chaoslang/categorization/js_inducer.py`
- `src/chaoslang/mining/ngram.py`
- `src/chaoslang/trie_miner.py`
- `src/chaoslang/scoring.py`
- `src/chaoslang/scoring/mdl.py`
- `tests/test_trie_miner.py`
- `tests/test_m1_controls.py`
- `tests/test_mackey_glass_lorenz96.py`
- `tests/test_js_integration.py`
- `tests/test_persistence.py`
- Test and source directory listings, including all other test filenames

No `scripts/` directory exists in the repository. The repository README filename is `README.md`, not `README`.

## Repository experiment records inspected

- `repos/chaoslang/experiments/logistic-m1-baseline/RUN.md`
- `repos/chaoslang/experiments/lorenz63-m1-baseline/RUN.md`
- `repos/chaoslang/experiments/rossler-m1-baseline/RUN.md`
- `repos/chaoslang/experiments/mackey-glass-m1-baseline/RUN.md`
- `repos/chaoslang/experiments/lorenz96-m1-baseline/RUN.md`
- `repos/chaoslang/experiments/lorenz96-dim8/RUN.md`
- `repos/chaoslang/experiments/lorenz96-dim12/RUN.md`
- `repos/chaoslang/experiments/lorenz96-dim16/RUN.md`
- `repos/chaoslang/experiments/lorenz96-dim20/RUN.md`
- `repos/chaoslang/experiments/lorenz96-dim24/RUN.md`

## Evidence gaps and cautions

1. The 256-symbol repository records contain summary `RUN.md` files only. They do not include raw stdout/stderr, environment captures, artifact hashes, timing, memory, or a commit identifier in each run record.
2. The baseline records call the approximate score "bits." The source describes it as a token-count proxy with fixed costs, not a complete calibrated code. The paper therefore uses "score units."
3. No matched old brute-force versus bounded suffix-trie benchmark exists. The old implementation is recoverable from Git history, but the 1024 by 20D run executed only the new code path. No speedup or memory reduction is evidenced.
4. Peak memory was not recorded for any run.
5. The 1024 by 20D experiment used commit `b344aa3c1a4b5a5eeef93fc2ea239a7f75c97429` plus an uncommitted CLI modification. The record captures its diff summary and the current working tree still contains that modification, but no committed tree uniquely identifies the full run source.
6. The 1024 by 20D run selected JS categories at threshold 0.1, but its history contains only eight chunk edits. It gives no evidence that a category edit improved the grammar.
7. No actual OmegaSim trace was run. "OmegaSim-scale" refers only to the selected stream length and approximately 20-dimensional control.
8. No labeled chaos-detection task, non-chaotic controls, shuffled surrogates, held-out trajectories, repeated seeds, confidence intervals, or perturbation sweep is recorded.
9. Numerical generators were not independently checked against reference integrators in the inspected evidence. The finite samples were not supplied with Lyapunov exponents or other independent chaos diagnostics.
10. M1 bounds are usually inferred from the entire trajectory. This is deterministic but uses global sample information and is not a held-out evaluation protocol.
11. The source declares Python `>=3.10`, while older experiment commands used `/usr/local/bin/python3.9`. A compatibility commit is present in history and project notes report Python 3.9 runs, but packaging metadata and historical commands are inconsistent.
12. At inspection, both local branches `main` and `agent/suffix-trie-miner` pointed to `b344aa3`; `b344aa3` was already an ancestor of local `main`. There is no distinct merge commit for the suffix-trie work. Local `main` was two commits ahead of `origin/main`.
13. Project task text says a "true brute-force comparison fixture" remains needed; this agrees with the experiment record and source history.
14. The `artifacts/` directory in the 1024 by 20D record is empty. Fitted grammar/state JSON and replay output were not preserved with the run.
15. Existing project summaries contain conflicting or unsupported OmegaSim dimension statements (approximately 16, 17, 20, or 20-30 fields). The new paper does not choose among them and limits its claim to the recorded 20D control target.
