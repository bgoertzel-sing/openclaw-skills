# CAROM `harness_v3_probes.py` audit

Date: 2026-07-21

## Provenance

Ben supplied `harness_v3_probes.py` through Telegram. The received file is at
`media/inbound/openclaw-staged-7c5d8beb-f419-415c-93c2-b270ab21f3e1/`
`harness_v3_probes---f3a5380c-fdc0-4b17-8d30-a41ec0a9357a.py` with SHA-256
`3f245aef9c419498a07eb9761e25f838619f83a81d64c7354c37b2019b085f5f`.
It passes `python3 -m py_compile`.

## Useful additions

- `swap_discrepancy` directly measures nonlinear phase-order sensitivity.
- `commutator_energy` estimates a local linearized interference diagnostic by
  JVP rather than inferring it from passive logs.
- The checkpoint sweep joins itinerary, intervention, nonlinear swap, and
  local-Jacobian evidence in a scientifically useful panel.
- Switching stress, cross-slot perturbation, and routing/control entropy are
  appropriate exploratory diagnostics when reported without theorem-strength
  promotion language.

## Blocking compatibility and correctness issues

1. **GPT-2 span extraction is not supported.** Every public probe calls
   `exp2.span_reps`. In the active repository, GPT-2 requires
   `span_reps_gpt2`; `GPT2Base.hidden` returns a tuple that `span_reps` cannot
   consume. Accept a `span_fn` argument everywhere and freeze its tokenizer,
   layer, and offset-mapping contract.

2. **Torch randomness is not seeded locally.** `commutator_energy` and
   `schedule_stability_probe` use `torch.randn_like`, but their `seed` controls
   only Python's `random.Random`. `cross_slot_coupling_probe` mutates the
   process-global Torch RNG. Use local `torch.Generator` instances and record
   probe seeds.

3. **The schedule-stability verdict is not licensed.** A p90 random-product
   growth estimate below one cannot establish joint spectral radius below one;
   rare unstable switching words can be missed. Report a descriptive sampled
   growth distribution. Values above one can provide an instability witness
   after numerical validation, but values below one are not a stability proof.

4. **The promised natural-trajectory comparator is absent.** The adversarial
   alternation probe reports only final norm divided by initial norm. It does
   not compute the natural trajectory's matched-horizon growth, so the
   docstring's “versus natural” interpretation is currently unsupported.

5. **Cross-slot coupling has a GPU device bug and an undefined zero case.**
   `C` is allocated on CPU while the assigned effects are CUDA tensors in GPU
   runs. `C / C.sum()` becomes non-finite when perturbations have zero effect.
   Allocate on the model device, preserve an unnormalized effect matrix, and
   explicitly handle a zero denominator.

6. **The typed-slot decision threshold is arbitrary.** `offdiag_mass > 0.5`
   is not derived from the named theorem, has no null or uncertainty estimate,
   and depends on global normalization. It can be a descriptive coupling
   statistic, not a “license” for per-slot or joint interpretation. Use
   multiple perturbation directions, matched diagonal/off-diagonal nulls, and
   paired confidence intervals.

7. **Control entropy includes padded modes.** `decisiveness_report` normalizes
   the complete trajectory vector without masking `ORD < 0`; the model clamps
   padded activities to a nonzero floor. Mask live modes before normalization
   and report normalized entropy plus dominance margin/classified fraction.

8. **Checkpoint loading is not portable.** `torch.load` lacks `map_location`.
   The sweep also assumes a harness whose `eval_checkpoint` and intervention
   functions are compatible with the selected span adapter.

## Interpretation constraints

- Small nonlinear swap discrepancy establishes approximate commutation only on
  sampled states, commands, amplitudes, and horizons.
- Small Jacobian commutator energy is a local linear statement at sampled base
  states, not global nonlinear commutation.
- The three proposed explanations—metric artifact, mechanistic drift, and
  learned commutation—are not mutually exclusive. Treat the sweep as a panel
  of evidence, not a classifier, unless thresholds and positive/negative
  controls are preregistered.
- The Oruzi theorem identifiers are not defined in the delivered file. Their
  assumptions must be linked to a preserved source before theorem-level claims
  are made.

## Decision

Do not deploy this file unchanged or use its categorical verdict strings in a
report. Preserve the six probe families, repair the eight issues above, and
run constructed controls before applying the probes read-only to the saved
TinyLM and GPT-2 checkpoints. Active training need not be interrupted.

