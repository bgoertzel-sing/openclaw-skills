# RUN: CAROM Experiment 3 — Teach Loop

- Experiment ID: `20260720T134700Z-exp3-teach-loop`
- Status: completed; one seed, TinyLM mechanism screen
- Source: Ben supplied PDF report + `exp3_teach.py` via Telegram 2026-07-20 13:45 PDT
- Report PDF SHA-256: `b29d26ebdaefa334a5e103d63a03911ded9cc662cd92cdabdc02ca165d59dbf6`
- Script SHA-256: `e8babc238d6835256aa224e381285485d9146d984e6ae660e76ccb849918a6ff`
- Preserved at: `projects/carom/docs/teach-loop/`

## Question

Can a frozen base LM's representations anchor the routing of newly taught
neural operators, trained purely on teacher-generated input/output pairs with
the existing operator library frozen? (The "teaching channel" for CAROM.)

## Setup (from sandbox report)

- 9 primitives over Z8 on 6 slots; 7 old (cap-trained), 2 held-out (shl, sq)
- Base LM: 3-layer d=96 causal transformer (~0.4M params), pretrained on all 9
- Cap: hypernetwork routing over K=8 operators, scheduled execution
- Teach: fresh operator slot trained on N=1024 teacher pairs, library frozen
- Anchor: frozen-LM representation of taught name; routing via s·cos(h,anchor)+b
- 4 measurements: M1 acquisition, M2 interference, M3 sample efficiency, M4 novelty

## Observed run results (seed 0)

All stages completed. Raw logs were retrieved 2026-07-21 from RunPod pod
`sgmngeyziytvbv` and are preserved in `artifacts/`.

| Measurement | Result |
|---|---|
| M1 taught-name invocation | shl 0.632; sq 0.632 |
| M1 unseen-paraphrase invocation | shl 0.410; sq 0.275 |
| baseline old-only accuracy | 0.659 |
| M2 old-program accuracy | 0.702 before registration; 0.627 after |
| M4 maximum frozen routing probability | old 0.942; held-out 0.835 |
| M4 routing entropy | old 0.224; held-out 0.438 |

The two new operator parameters fitted their synthetic teacher-pair losses to
near zero. This establishes direct operator acquisition, not reliable composition
or description transfer.

### Interpretation

- **Observed:** independently sampled old-program accuracy was 0.702 before and
  0.627 after adding slots. These are *not paired evaluations* (the RNG advances
  between calls), so the 7.5-point difference is suggestive of routing-mediated
  interference, not a causal estimate. A fixed paired set is required.
- **Observed:** both held-out operators worked under their taught names, but unseen-paraphrase routing was weak and asymmetric (`sq` 0.275).
- **Observed:** held-out commands had lower maximum old-library routing confidence and higher entropy, providing an imperfect novelty signal.
- **Not established:** an LLM teaching channel. The teacher was synthetic, the base a 0.4M TinyLM pretrained on all nine descriptions, and there was one seed with no M3 N/noise sweep, GPT-2, or prompted-teacher result.

## Sandbox results (from supplied PDF, single seed)

- M1 taught-name: shl 0.601, sq 0.584 (baseline 0.691, chance 0.125)
- M1 unseen paraphrases: shl 0.408, sq 0.438 (genuine invoke-by-description transfer)
- M2: zero weight interference (frozen library); routing interference 0.772→0.562, recovered to 0.650
- M4: novelty signal exists (held-out max routing 0.766 vs 0.862; entropy 0.822 vs 0.554)
- Key findings: (1) routing calibration — anchor gate must train against full routing distribution;
  (2) routing interference ≠ weight interference — "frozen weights ≠ frozen behavior when action space grows"

## Original run plan

Ran on spare CPU while the approved GPU pod was otherwise idle:
1. `--stage lm --steps 800` (LM pretraining)
2. `--stage cap --steps 800` (cap training on 7 old primitives)
3. `--stage teach --n_ex 1024 --eps 0.0` (teach shl + sq)
4. `--stage eval` (measure M1–M4)

The cap stage reported 263 seconds; all stages completed.
Cost: $0 (using spare CPU on already-approved E0/E1 pod).

## GPU upgrade path (not in this run)

- GPT-2 base swap (stub in script)
- Prompted teacher generation
- KL no-regression penalty at registration
- Sequential multi-skill acquisition
- ≥3 seeds

## Evidence

- `artifacts/exp3_lm.log` SHA-256 `58340b51d48c4810692956464ba3a07eb9ce6fa448d338a81adae0fe4aa9af9a`
- `artifacts/exp3_cap.log` SHA-256 `9806614fdfd8c0c8646a1390348feeffb1849c3a104c26e10472ecfe4f656a63`
- `artifacts/exp3_teach.log` SHA-256 `041b1edab7043ab5b15c0343087723fe04e1065ebe52db7cb0a08e3f26b0e96c`
- `artifacts/exp3_eval.log` SHA-256 `68c429668730a3a430eedeac89c6602bf6b0e62587b206688ea8a6293d521f26`
