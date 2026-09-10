# RelaLeap Reconciliation Artifact: SLT-v2 vs GPT-2 CPU Interface Gate

**Created:** 2026-07-16 14:06 PDT
**Status:** Draft — first two rows populated independently, overlap verdict derived mechanically
**Mac lane:** PAUSE-RECOVER (unchanged)
**GPU spend:** Blocked pending Ben's explicit approval

---

## Schema

| Column | Description |
|---|---|
| Claim ID | Stable handle |
| Metric + controls | What was measured, against which baselines |
| Hardware path | Concrete runtime the number came from |
| Overlap verdict | `shared-claim` / `interface-only` / `orthogonal` (derived, not asserted) |
| Production-only residue | What cannot be resolved without the GPU run |
| Provenance | Reproduction-grade: repo commit, harness commit, config hash, observed device, seed/determinism state, model identity iff model output is in the measured pipeline |

**`shared-claim` rule:** Identical metric, controls, dataset/seeds, and harness semantics; only the declared hardware/device path may differ. Otherwise `interface-only` or `orthogonal`.

---

## Row 1: SLT-v2 ePC Distillation Gate

| Field | Value |
|---|---|
| **Claim ID** | `SLT-v2-ePC-gate` |
| **Metric + controls** | Held-out matched-KD criterion: ePC at T=8, λ=0.05 vs BP (baseline), BP+KD (control), BP+CE (control). Primary endpoint: ePC improves over BP *and* matches or beats BP+KD on held-out matched-state evaluation. Secondary: earlier-block credit, training speed. |
| **Hardware path** | MacBook (RelaLeap Mac lane). Exact device unspecified in memory — CPU, local. |
| **Overlap verdict** | *(derived below)* |
| **Production-only residue** | *(filled after verdict)* |
| **Provenance** | Repo: RelaLeap Mac repo, branch `agent/slt-pregate-v2-cache`. Commits: `941b8b3` (ePC gate), `cbe4c08` (normalization fix), `65666f9` (preregistration). Seeds: three-seed local gate (exact seeds not recovered from memory — **GAP**). Harness: matched-state transformer ePC distillation gate v2. Model: GPT-2-small teacher (`607a30d`, safetensors SHA-256 `248dfc...a707`), six-layer GPT-2-width student. Dataset: WikiText-103, GPT-2 BPE. Determinism: fixed seeds, structured metrics, matched updates/time. |

### Row 1 result
**Observed:** Two three-seed local gates preserved invariants and exact T=1 KD equivalence, but **failed** the held-out matched-KD criterion. At T=8, λ=0.05, ePC improved over BP but remained worse and slower than ordinary KD. This is a **negative result**. The Mac lane entered PAUSE-RECOVER. Source: `memory/2026-07-15.md#L60`.

---

## Row 2: GPT-2 CPU Interface Gate

| Field | Value |
|---|---|
| **Claim ID** | `GPT2-CPU-interface` |
| **Metric + controls** | Interface determinism: two runs of frozen three seeds through a two-layer stub (BP+CE / BP+KD / ePC+KD arms). Nine structured records matched outside elapsed timing. Energy/credit diagnostics passed. Full suite 118/118. |
| **Hardware path** | Local CPU, commit `c310230` (unpushed). Two-layer stub, not production GPT-2 block-state runner. |
| **Overlap verdict** | *(derived below)* |
| **Production-only residue** | *(filled after verdict)* |
| **Provenance** | Repo: RelaLeap local repo. Commit: `c310230` (unpushed). Harness: two-layer stub interface gate. Seeds: frozen three seeds (exact values in commit). Metrics SHA-256: `004d42b2a9d7a5e8e451a1542ea398038801a226b179bb0703bb21982e60b447`. Dataset: WikiText-103, GPT-2 BPE (shared with Row 1). Model: GPT-2-small teacher (same revision `607a30d`). Determinism: two-run reproducibility check. |

### Row 2 result
**Observed:** Interface gate passed — deterministic reproduction across two runs, all structured metrics matched outside timing. Implementation evidence only: production runner, dependency lock, image digest, GPU smoke runtime, and Ben approval remain. Source: `memory/2026-07-16.md#L3`.

---

## Overlap verdict (derived mechanically)

| Axis | SLT-v2-ePC-gate | GPT-2-CPU-interface | Match? |
|---|---|---|---|
| **Metric** | Held-out matched-KD criterion (ePC vs BP, BP+KD, BP+CE) | Interface determinism (two-run structured-record match) | ❌ Different metrics |
| **Controls** | BP, BP+KD, BP+CE as matched controls | No scientific controls — internal reproducibility only | ❌ Different controls |
| **Dataset/seeds** | WikiText-103, GPT-2 BPE, three seeds | WikiText-103, GPT-2 BPE, frozen three seeds | ⚠️ Possibly same seeds (unconfirmed — seed values not recovered for Row 1) |
| **Harness semantics** | Matched-state transformer ePC distillation gate v2 (full evaluation pipeline) | Two-layer stub (interface check, not evaluation pipeline) | ❌ Different harness |
| **Device path** | MacBook CPU | Local CPU | ✅ Same (both CPU) |

**Verdict: `interface-only`**

The metrics differ (scientific evaluation vs interface determinism), the controls differ (matched KD/CE controls vs none), and the harness semantics differ (full ePC distillation gate vs two-layer stub). The CPU gate passing tells us the *interface plumbing* is deterministic, not that the *scientific claim* (ePC beats matched controls) survives. The device path is actually the same (both CPU), so there is no hardware-boundary question at all — the divergence is in what was measured, not where it ran.

---

## Production-only residue

Since the verdict is `interface-only`, the production-only residue column is not applicable for graduating the CPU result to confirmation of SLT-v2. The residue for SLT-v2 itself (if it were to be re-run on GPU) would include: GPT-2 block-state runner, GPU numerics/batching/kernel paths, production image/digest, and runtime behavior under GPU memory constraints. But none of these are licensed by the CPU interface gate.

---

## Conclusion

The GPT-2 CPU interface gate is **interface-only** evidence. It cannot graduate to confirmation of the SLT-v2 claim. The Mac lane's PAUSE-RECOVER state is correct and should not be rescued by the CPU gate's pass. The pivot candidate (CPU gate → production GPU run) is not valid without a `shared-claim` row.

**Next steps gated on Ben's direction:**
1. If the goal is to re-test SLT-v2 on GPU: design a preregistered production-runner gate with frozen pass/fail/stop thresholds, CPU dry-run of the exact production harness, and Ben's explicit cost approval.
2. If the goal is to test a different claim on GPU (e.g., interface validation under production load): frame it as a new claim, not a continuation of SLT-v2.
3. The negative SLT-v2 result stands as recorded.
