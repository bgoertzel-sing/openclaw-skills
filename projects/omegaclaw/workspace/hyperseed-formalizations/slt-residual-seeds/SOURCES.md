# Source Manifest — SLT-Guided Residual Seeds

All citations in `outline.md` reference sources by short key.
This manifest maps each key to a canonical retrieval path that resolves from the **checked-out repository root**, not from an agent workspace.

---

## Citation keys

| Short key | Repo-relative path | SHA-256 (when committed) | Status | Description |
|---|---|---|---|---|
| Weakness-SL | `sources/Weakness-Singular-Learning.pdf` | `55703d39ce2651a6d9eab9f710bc199469661a91a4069ac69f0a480bc5760171` | ✅ committed | *Weakness as Local Evidence* (Ben Goertzel). LLC decomposition, evidence factorization, quantale message-passing, refinement DAGs. |
| SLT-ResLayers | `sources/SLT-and-Residual-Layers.pdf` | `bffc373dc65f02649269dde1d6cbe0ec0128d618e2cee9d2a021d17af82989c4` | ✅ committed | *SLT and Residual Layers*. Seven-term pregate formula, computable surrogates, mixed-Hessian / commutator diagnostics. |
| SLT-Accuracy | `sources/SLT-accuracy-weakness_v1.pdf` | `a55d4fd3ec6209be706ed43c6865c71363206687c49b61f676d16322f0f05949` | ✅ committed | *SLT-accuracy-weakness v1*. Evidence-ratio → soft-accuracy bridge, O(λ/n) correction. |
| SLT-SubRep | `sources/SLT-SubRep-v5.pdf` | `5f9b60ee0c10c734c4fa805b2a6083aa178b60e2024fa1e2bd312d33909c05f5` | ✅ committed | *SLT for SubRep v5*. I_λ > 0 / < 0 interpretation, interaction complexity. |
| SLT-Regime | `sources/SLT-for-regime-change-detection.pdf` | `a7d2d4d5d8670b1e54c472fd25e25b61b9ca098ee0a517d325eee86aa7c59e30` | ✅ committed | *SLT for regime-change detection*. Module-wise LLC signature shifts as refinement triggers. |
| SLT-GoalStab | `sources/SLT-Goal-Stability_v4.pdf` | `c66fed4198b7f181464f84c588d44a7cc5016f14fa5fa6d5f8b9d17b62f53a97` | ✅ committed | *SLT-Goal-Stability v4*. Semantic truth limits of SLT diagnostics. |
| SLT-Semantics | `sources/SLT-Semantics-v2.pdf` | `f2348c8c42faa5110cff78d56ccaabdab2e119c24a0010e05ce21bcf9a03762b` | ✅ committed | *SLT-Semantics v2*. Distinctions → partitions → symmetries → singularities. |
| SLT-Evolution | `sources/SLT-Evolution.pdf` | `84167b824e05a7e30cb3c14cb52d0fda748a6b1353ad14a288c3fe3abe5ed021` | ✅ committed | *SLT-Evolution*. Free-energy geodesics, EDA. |
| CausalFibres | `sources/causal-fibres-README.md` | `01fe8af0ff0bf88c06438f9bd3988bf25824addc95bb2cb42e2a00a1aa28fc19` | ✅ committed | *Causal Fibres 0.4.0 README*. H0–H6 hypothesis ladder, frozen interfaces, representation contests. |
| Note-0014 | `sources/note-0014.md` | `b9efcfd74f21d42d59446a41dd6c689c42f4735d4c03e79456182dd40c81d25a` | ✅ committed | *Note 0014: Emotion regime operators*. Regime-operator definitions referenced in Claim 5. |
| InitSynth | `sources/INITIAL_SYNTHESIS.md` | `c407540183bd230394528de471fc04df873f4cd82d91a68432d6ff31b9eec88e` | ✅ committed | *Initial synthesis*. Original hypothesis: "deviations from additivity signal geometric interactions between singular regions." |

## Resolution status

**Committed (11/11):** All source files present and hash-verified.

Sources were located in the research-agent library (`library/slt-hyperseed-synthesis/source/`, `library/slt-residual-layers/`) and copied to the canonical `sources/` directory on 2026-07-28.

## Clean-clone verification procedure

```bash
# From a fresh clone of this repository:
cd hyperseed-formalizations/slt-residual-seeds/

# 1. Check all source files exist
for f in $(awk -F'|' '/sources\//{gsub(/`/,"",$3); gsub(/^ +| +$/,"",$3); print $3}' SOURCES.md); do
  [ -f "$f" ] && echo "OK: $f" || echo "MISSING: $f"
done

# 2. Verify hashes for committed files
cd sources
sha256sum -c SHA256SUMS.txt

# 3. Check outline.md resolves all citation keys
grep -oP '\[([A-Za-z-]+)\]' ../outline.md | sort -u | while read key; do
  k=$(echo "$key" | tr -d '[]')
  grep -q "$k" ../SOURCES.md && echo "OK: $k" || echo "UNRESOLVED: $k"
done
```

**The clean-clone test passes only when step 1 reports no MISSING files and step 2 reports all OK.**

## Clean-clone verification result (2026-07-28 12:39 PDT)

```
=== STEP 1: Check all source files exist ===
OK: sources/Weakness-Singular-Learning.pdf
OK: sources/SLT-and-Residual-Layers.pdf
OK: sources/SLT-accuracy-weakness_v1.pdf
OK: sources/SLT-SubRep-v5.pdf
OK: sources/SLT-for-regime-change-detection.pdf
OK: sources/SLT-Goal-Stability_v4.pdf
OK: sources/SLT-Semantics-v2.pdf
OK: sources/SLT-Evolution.pdf
OK: sources/causal-fibres-README.md
OK: sources/note-0014.md
OK: sources/INITIAL_SYNTHESIS.md

=== STEP 2: Verify hashes ===
causal-fibres-README.md: OK
INITIAL_SYNTHESIS.md: OK
note-0014.md: OK
SLT-accuracy-weakness_v1.pdf: OK
SLT-and-Residual-Layers.pdf: OK
SLT-Evolution.pdf: OK
SLT-for-regime-change-detection.pdf: OK
SLT-Goal-Stability_v4.pdf: OK
SLT-Semantics-v2.pdf: OK
SLT-SubRep-v5.pdf: OK
Weakness-Singular-Learning.pdf: OK

=== STEP 3: Check outline.md resolves all citation keys ===
RESOLVED: CausalFibres
RESOLVED: InitSynth
RESOLVED: SLT-Accuracy
RESOLVED: SLT-Evolution
RESOLVED: SLT-GoalStab
RESOLVED: SLT-Regime
RESOLVED: SLT-ResLayers
RESOLVED: SLT-Semantics
RESOLVED: SLT-SubRep
RESOLVED: Weakness-SL
```

**Result: PASS.** All 11 files present, all hashes verified, all citation keys resolved.

## Provenance notes

Source PDFs/MDs originate from:
- `library/slt-hyperseed-synthesis/source/` — Weakness-SL, SLT-SubRep, SLT-Accuracy, SLT-GoalStab, SLT-Semantics, SLT-Evolution, SLT-Regime
- `library/slt-residual-layers/` — SLT-ResLayers
- `library/slt-hyperseed-synthesis/` — InitSynth

The canonical resolution path is `sources/` within this directory.
