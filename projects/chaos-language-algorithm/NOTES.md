# Notes

## 2026-07-03

Received and ingested Ben's `chaos_language_algorithm_ascii.pdf`. Core implementation risk is semantic conflation: chunks are sequential nonterminals; meta-symbols are context-substitution categories whose parse occurrences must retain chosen members for exact reconstruction.


## 2026-07-03 - CLA new project lane

Ben declared CLA a new project lane and paused OmegaSim until CLA is robust enough to detect grammatical strange-attractor structure in simulated OmegaHive traces. He supplied a second architecture document specifying a Hyperon-ready but pure-Python-first `chaoslang` library design.

## 2026-07-03 - GitHub repo created and first slice pushed

Ben confirmed CLA should be its own GitHub repo with the usual credentials. Local repo exists at `projects/chaos-language-algorithm/repos/chaoslang` with Git identity `Benjamin Goertzel <ben@singularitynet.io>`. Created GitHub remote `https://github.com/bgoertzel-sing/chaos-language-algorithm` and pushed the tested sprint-1 implementation to `main` at commit `4a7399c`.

Spawned subagent `cla_chaoslang_impl` to implement the first tested pure-Python symbolic-string MVP locally; the sprint completed with 19 passing tests.

## 2026-07-03 - Hyperseed / pattern calculus subthread

Ben suggested keeping a persistent subthread on CLA from a Hyperseed perspective. Core questions: what kind of language is induced from chaotic trajectories; how emergent pattern becomes grammar rather than merely compression; whether CLA edits/categories can be interpreted using McBride derivatives and pattern calculus; and how such an analysis can inform OmegaSim detector design. Ben pointed to Google Drive source `Weakness-Theory-10.pdf` (`https://drive.google.com/file/d/1PNg6ywTWPtSixm1yQ10z0TQXR8_bpgEh/view?usp=drive_link`), especially sections on emergent pattern and pattern calculus. Initial web fetch saw the Drive title but did not retrieve PDF contents.

## 2026-07-03 - chaoslang sprint 1 local implementation

Implemented and committed the first local `chaoslang` prototype at `projects/chaos-language-algorithm/repos/chaoslang`, commit `4a7399c`. Scope: pure-Python package with immutable-ish core dataclasses (`Token`, `Production`, `Category`, `Corpus`, `Grammar`, `Score`, `GrammarState`, `Edit`, `Proposal`), symbolic-string `CLA.simple().fit_symbols(...)`, n-gram chunk mining with non-overlap selection, exact chunk/category expansion, rule use counts and dead-rule pruning, a deterministic hard context category proposal seam, simple MDL-like greedy acceptance, `Fact`/`FactStore`/`MemoryFactStore` projection round-trip, and a logistic-map/equal-width symbolization smoke scaffold. Verification from repo root: `python3 -m unittest discover -s tests -v` passed 19 tests; `git diff --check` passed. Next: add fixed-partition trajectory symbolization and recorded attractor benchmark experiments before resuming OmegaSim detector calibration.

## 2026-07-04 - M1 controls slice

Implemented the next local `chaoslang` slice under `repos/chaoslang`: dependency-light deterministic Lorenz-63 and Rössler trajectory generators using fixed-step RK4; scalar/vector M1 fixed rectangular partition symbolization; a small JSON benchmark command (`python3 -m chaoslang.benchmarks.m1_controls`); and a Jensen-Shannon divergence clustering seam for future context/category clustering. Also fixed an n-gram chunk naming collision discovered by the Rössler M1 test: tie-breaking could accept `N2` before `N1`, then later reuse `N2` and overwrite the old rule, breaking exact reconstruction. Verification from repo root on 2026-07-04: `python3 -m unittest discover -s tests -v` passed 26 tests; `python3 -m chaoslang.benchmarks.m1_controls --system lorenz63 --steps 24 --discard 4 --bins 3 --iterations 3` emitted JSON with `exact_reconstruction: true`; `git diff --check` passed. Remaining next step: integrate JS-divergence context clustering into category proposal generation and record real attractor/control benchmark runs before attempting OmegaSim-level dimensionality.

## 2026-07-09 - suffix trie miner branch

Implemented a bounded suffix-trie chunk miner on branch `agent/suffix-trie-miner` in `projects/chaos-language-algorithm/repos/chaoslang`. The new `chaoslang.trie_miner.SuffixTrieMiner` builds suffix-prefix trie nodes keyed with `entry_key()` for `Token` and `CategoryOccurrence`, returns `ChunkProposal`s compatible with the existing n-gram miner, and can be selected via `CLA.simple(..., miner="suffix_trie")`. Added pytest coverage for smoke cases, equivalence with `NGramPatternMiner`, bounded O(N * max_ngram) node count, non-overlap behavior, and API switching. Verification: `PYTHONPATH=src python3 -m py_compile src/chaoslang/trie_miner.py`; `PYTHONPATH=src python3 -m pytest tests/ -v` passed 69 tests; `git diff --check` passed.

## 2026-07-09 - Suffix-trie n-gram miner for compound-symbol scaling

Ben approved replacing the brute-force `NGramPatternMiner` after OOM risk in high-cardinality compound-symbol CLA streams (e.g. 1024 steps × ~20D). Implemented a depth-bounded suffix-trie-backed miner in `repos/chaoslang/src/chaoslang/mining/ngram.py` on branch `agent/suffix-trie-miner`, preserving deterministic proposals and exact reconstruction. Added regression tests comparing trie output to a brute-force oracle for compound symbols and checking a high-cardinality repeated motif. Also added `docs/cla_expert_review_prompt.md` asking GPT-5.5-Pro/expert reviewers to explicitly audit algorithm/data-structure inefficiencies such as n-gram brute force, context histogram duplication, compound-symbol storage/copying, and repeated MDL re-encoding. Verification: focused chunk tests and full unittest suite passed; a 1024-step × 20D synthetic smoke completed locally with 1,710 proposals.
