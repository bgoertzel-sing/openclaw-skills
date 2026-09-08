# Frame-oracle v4 sealed-gate contract

- Contract: `frame-oracle-v4-gate-1`
- Frozen: `2026-08-02` America/Vancouver (`2026-08-03` UTC)
- Scope: local semantic oracle/readout lane only
- Prior exposed batteries: v1, v2, v3, and `offline_readout_corpus_v1`
- Status: gate prepared but unopened

## Scientific question

Can a versioned successor to the failed v3 proposal-plus-normalizer path
produce exact closed semantic frames across every declared predicate,
explicit polarity, possible modality, abstention, surface alternation, and
world-knowledge trap without changing the answer to match any exposed case?

The v3 offline label result (`22/24`) blocks readout training. V4 is not a
license to repair `test_dracula` or `test_window` directly. Those cases and all
earlier batteries remain failure evidence and may be used only for diagnosis,
never for a claimed fresh pass.

## Public counterexample and required repair boundary

V3 derives polarity with the regular expression `\b(?:no|not|never)\b` over
the whole sentence. Therefore `The No Name Cafe is located in Bristol.` is an
affirmed location claim that v3 deterministically changes to negated. This is
a code-derived counterexample, independent of the two opened v1 corpus
failures. Any v4 design must specify the grammatical scope from which
polarity and modality are derived; substring/whole-sentence cue ownership is
not admissible.

V4 must also preserve the distinction between `asserted` and `possible`.
The v3 normalizer unconditionally overwrites every non-unknown proposal with
`asserted`, although `possible` is part of the frozen schema. This is a
contract inconsistency visible from source inspection, not an empirical gate
outcome.

## Sealed battery

The durable bundle is `sealed/frame-oracle-v4/`:

- `gate_public.json`: 24 fresh case IDs, sentences, strata, and the SHA-256
  commitment of the answer file;
- `gate_answers.json`: exact semantic keys, process-sealed and not to be read
  or used during implementation;
- `validate_gate.py`: integrity, coverage, commitment, and exact-disjointness
  checks;
- `run_validation.sh`: integrity check, focused frame tests, full tests, and
  diff check. It does not invoke Ollama or open the scientific gate.

The gate covers all five predicates, three world-knowledge traps, five
explicit negations, five possible modalities, active/passive or inverted
surface forms, and four mandatory abstentions. No sentence exactly overlaps
the earlier v1--v3 or offline-readout-v1 batteries.

## Freeze-before-open procedure

1. Create a new isolated branch/worktree from commit `93383b2`.
2. Specify v4 prompt/schema/normalization behavior without consulting
   `gate_answers.json`. The implementation may use synthetic unit fixtures
   created independently of both prior and v4 batteries.
3. Pass focused unit tests and the full local suite. Record model ID/digest,
   prompt hash, schema hash, implementation commit, clean status, seed,
   deterministic decode settings, and exact paired-run command.
4. Commit the implementation and create the experiment `RUN.md` and
   `command.sh` before opening the answers or invoking the evaluator.
5. Run every public case twice with `qwen2.5:7b` ID `845dbda0ea48`. Only then
   may the evaluator read `gate_answers.json` and mark `gate_public.json` as
   consumed in the experiment record. Do not rewrite the frozen source bundle.
6. Pass only at 24/24 valid, 24/24 paired deterministic, and 24/24 exact
   semantic keys. Every predicate, negation, modality, world-knowledge, and
   abstention stratum must be perfect. Any error consumes and exposes the
   battery and blocks labels/readout.

## Readout boundary

Even a v4 oracle pass admits only a separately frozen offline-label run. The
oracle-admission cases may never become readout training examples. A readout
requires a new train/calibration/test corpus, exact split provenance, no
sentence overlap, deterministic feature extraction and replay, and a sealed
held-out conjunction over predicate, both slots, polarity, modality, and
abstention. No quantale, XM, or ePC semantic loss is admissible until the
readout and a later fresh substitution/gallery gate both pass.
