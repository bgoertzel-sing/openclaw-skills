# CLA expert-review prompt

Use this prompt when asking GPT-5.5-Pro or another expert reviewer to audit the Chaos Language Algorithm prototype.

```text
You are reviewing the pure-Python Chaos Language Algorithm prototype (`chaoslang`) and its current project notes. Please give a technically critical review focused on correctness, scalability, and research validity.

Context:
- CLA learns exact-reconstructing symbolic grammars from chaotic trajectory symbol streams.
- It proposes chunk rules from repeated n-grams, category rules from context similarity / JS divergence, and accepts edits through an MDL-like greedy loop.
- High-dimensional fixed-partition symbolization can create high-cardinality compound symbols, e.g. 1024-step × ~20D streams where each stream token encodes many per-dimension bins.

Please explicitly identify algorithmic or data-structure inefficiencies, not just conceptual issues. In particular, look for:
1. n-gram mining approaches that brute-force materialize all windows/counts and can blow up on high-cardinality compound-symbol streams;
2. avoidable duplication in context histograms or JS-divergence category induction;
3. wasteful compound-symbol storage, copying, hashing, or stringification;
4. proposal-ranking or MDL-evaluation loops that repeatedly re-encode full grammar/parse state unnecessarily;
5. opportunities for suffix tries, suffix automata, rolling hashes, inverted indexes, sparse histograms, interning, streaming counters, or bounded/top-k candidate filters.

For each issue, report:
- observed or likely complexity/memory behavior;
- concrete failure mode or misleading scientific consequence;
- a minimal implementation recommendation compatible with exact reconstruction;
- tests or benchmarks that would catch regressions.

Also flag any assumptions about trajectory length, bin count, dimensionality, or symbol-cardinality that make current benchmark conclusions fragile.
```
