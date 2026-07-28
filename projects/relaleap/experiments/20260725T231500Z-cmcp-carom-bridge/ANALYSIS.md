# CMCP--CAROM bookkeeping convergence audit

## Evidence inspected

- CMCP bridge Steps 1--4 experiment records and raw JSON artifacts.
- RelaLeap CMCP typed accounting and Phase-7 assimilation/maintenance transport:
  `src/relaleap/hdpc/e4_cmcp_typed.py` and
  `src/relaleap/hdpc/e4_cmcp_phase7.py`.
- CAROM project/task records, E2/E3 specification, model fitness and
  direction-free channel penalties:
  `projects/carom/{PROJECT.md,TASKS.md}`,
  `projects/carom/docs/e2-e3-mode-fitness-channel-regularization-spec.md`, and
  `projects/carom/repos/carom/{model.py,run_carom_e2_e3.py}`.
- CAROM E2/E3 feasibility, GPU, and compiled-recurrence ledgers.

## Frozen-standard assessment

### 1. Explicit assimilation/maintenance or plasticity/replay split

**Partially satisfied, CMCP side only.** CMCP's typed protocol and Phase-7
transport explicitly keep assimilation and maintenance coordinates separate
until transport. The calibrated KD bridge in Steps 1--4 exercises assimilation
weights but does not implement a maintenance/replay arm. CAROM E2/E3 separates
mode-specific fitness from generic channel regularization; it does not expose
an assimilation-versus-replay ledger homologous to CMCP.

### 2. Allocation by measured marginal novelty/unclaimed frontier

**Satisfied for the calibrated CMCP selector; not satisfied for CAROM.**
Step 1 demonstrated why mass matching is necessary. Steps 2--3 then showed
response-conditional novelty credits complementary Teacher B and nearly
matches oracle Task-B loss on disjoint seeds. CAROM's E2 fitness uses workspace,
command, position, and interaction features, while E3 penalties regulate
overlap, directional movement, entropy, and activity mass without naming a
successor. None of the inspected CAROM code computes conditional marginal
novelty relative to already claimed workspace evidence. Its "workspace"
feature is state input to a fitness function, not an unclaimed-frontier mass
ledger.

### 3. Identifying outcome benefit

**Satisfied narrowly for CMCP; absent for the proposed bridge.** On disjoint
mass-normalized seeds, response CMCP improved mean Task-B loss over ordinary
by `0.00402349` and nearly matched oracle, but increased Task-A forgetting and
did not improve accuracy. CAROM's full E2/E3 scientific campaign is incomplete:
CPU feasibility projected about 86 hours; the first GPU attempt produced no
scientific result; the compiled campaign stopped at 16/25 arms under its bound.
Therefore there is no completed mass-matched or otherwise identifying CAROM
result to correlate with CMCP credit.

## Conclusion

The convergence hypothesis is **not supported yet** under the frozen standard.
There is a useful architectural analogy--separate plastic assimilation from
maintenance/replay and govern scarce update mass--but no shared empirical
bookkeeping principle has been demonstrated. Claiming convergence now would be
type alignment.

The evidence does support a precise future bridge test: add to CAROM an
explicit two-ledger controller in which (a) assimilation mass is conditional
response or settled-error novelty relative to previously credited workspace
directions, (b) maintenance mass is allocated to measured retention need, and
(c) total update mass is fixed across ordinary, naive, CMCP-style, and oracle
controllers. Compare plastic-task gain and retained-task loss jointly. This
should be attempted only after the existing E2/E3 campaign has a complete
scientific disposition or in a smaller equivalence-gated fixture.
