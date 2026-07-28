# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-23 - H0 launch

Relevant research rules are 1 (validate the estimator), 2 (write the metric and
interface spec first), 3 (use the released `FrozenReadProbe` rather than
rebuilding every arm), 5 (full reproducibility), and 7 (keep model, interface,
probe, and metrics modular). The local CPU run is explicitly a smoke
instantiation of H0; it does not substitute for the specified GPT-2-small
replication.

## 2026-07-23 - H0 CPU smoke outcome

The immutable first pilot overtrained the student, making both task gap
denominators nonpositive; it is retained at
`experiments/20260723T181307Z-h0-frozen-interface-cpu/`. Calibration selected
30 student updates before the final run.

The final run evaluated linear, low-rank ranks 4/8/16/32, MLP, and
LoRA-labeled equivalent low-rank arms across blocks 0, 2, 4, 5, and their
concatenation. At an additive final-logit write, the LoRA and unscaled low-rank
residual parameterizations are algebraically equivalent; they are labeled
honestly and not treated as independent mechanism evidence.

The combined-layer MLP won. Raw held-out base/residual/teacher losses were
`0.967670 / 0.081691 / 0.074032`; accuracies were
`0.927734 / 1.0 / 1.0`. `Gamma_L=0.991430` with 95% paired-bootstrap CI
`[0.990696,0.992202]`; `Gamma_A=1.0`, CI `[1,1]`. Factor Γ values were subject
`0.848056`, object `0.836857`, tense `0.826813`, negation `0.861884`, and
agreement `0.819706`; corresponding off-factor score spill was
`0.124350`--`0.142183`. This passes H0 only for the toy smoke interface.

Stage 0B was prepared at `configs/h1_stage0b_toy_prepared.json` but not run.
The target GPT-2-small replication remains open and no paid compute was used.

## 2026-07-23 - Revised E1--E5 strategic pivot

Ben supplied `Revised ePC Experimental Programme: Homotopy Absorption, Fibre
Emergence, and the Deployment Settle`, preserved at
`../../library/revised-epc-experimental-programme-2026/`.

Research Rules 1, 2, 3, 5, 6, and 7 govern the pivot. Validate frontier/JBD
estimators on constructed cases; freeze the spec and machine-readable gates
before implementation; reuse causal-fibres 0.4.0 and the archived R8/R9 branch;
record exact provenance and artifacts; retain the H0--H6 conceptual
distinctions; and keep PyTorch/MORK plus dense/top-k/fibre paths modular.

The archived R8 command names source commit `9ccb151`, while the final RUN.md
names `ecf2f79`; both exist in the RelaLeap repository on
`agent/epc-outcome-probes`. Inspection resolves the code relation:
`ecf2f79` is the direct child of `9ccb151` and adds the four-line batch-dimension
fix in `scripts/run_gpt2_pilot_gpu.py` that allowed the final campaign to
complete. E1's pathology control therefore binds to `ecf2f79`; `9ccb151` is
the preregistered pre-fix design ancestor.

The actual R8 campaign trained random six-layer GPT-2-config students against
the frozen 12-layer GPT-2 124M teacher on WikiText-103. The four-factor
synthetic grammar (`subj_num`, `obj_num`, `tense`, `negation`) entered in R9
as a posthoc representation/intervention probe, not as R8's training data.
The revised programme instead says all E1--E4 training runs use the synthetic
grammar rig. That is a deliberate new protocol, not a literal R8 rerun:
preserve an `R8-WikiText` reproduction control and separately define the
`E1-synthetic-grammar` homotopy test. Factor count and names must come from
the frozen protocol and mismatches must fail closed.

The plan's replicate-envelope rule is amended to use disjoint calibration and
confirmation sets. This is necessary because the same outcomes cannot both set
and independently pass their acceptance envelope. Provisional structural bars
also require positive/pathology/null calibration.
