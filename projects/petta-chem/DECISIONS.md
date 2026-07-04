# Decision Log

## D-20260626-petta-native-kernel: Build the chemistry kernel in PeTTa from the start

- Date: `2026-06-26`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: Telegram clarification on 2026-06-26; `projects/petta-chem/TASKS.md`

### Context

ZeroBot suggested a hybrid implementation path in which Python host code would implement the first chemistry kernel while emitting PeTTa/MeTTa-style atoms. Benjamin rejected that interpretation and clarified that the algorithmic chemistry system itself should be built in PeTTa from the start.

### Decision

Implement the algorithmic chemistry kernel in PeTTa from the beginning. Python may be used for experimental wrapping only: running batches, loading configuration files, saving data, plotting, filesystem logistics, or other harness duties.

### Alternatives considered

- Python-first kernel with PeTTa/MeTTa-shaped atom protocol.
- Mixed host-kernel implementation where core matching/scoring/firing lives outside PeTTa.

### Rationale and evidence

Benjamin's explicit clarification: “build the algorithmic chemistry system in PeTTa right from the start -- NOT in python. You can use python for some experimental wrapping -- as a harness for running experiments, saving data, loading configuration files or whatever.” He added that implementing the chemistry in Python would make a mess that is cumbersome to check for errors and would still require a PeTTa port later.

### Consequences

- exp00 must be designed around PeTTa-native chemistry behavior, not a Python simulation that merely exports atoms.
- Harness code is acceptable but should remain thin and replaceable.
- Repository inspection should focus on the practical PeTTa runtime path and test strategy.

### Revisit trigger

Revisit only if PeTTa runtime limitations make the specified exp00 impossible or scientifically misleading; prefer narrowing exp00 rather than moving the chemistry kernel to Python.

### Supersedes or superseded by

Supersedes the tentative Python-kernel/hybrid recommendation made in chat before Benjamin's clarification.

## D-20260626-runtime-swi-petta: Use PeTTa on SWI-Prolog 9.3.x for version 0.1

- Date: `2026-06-26`
- Status: `accepted`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Related task/run/commit: `projects/petta-chem/repos/petta-chem/docs/runtime.md`; exp00 smoke runner

### Context

The project needs a PeTTa-native kernel from the start. During OmegaClaw setup, the local workstation obtained a working PeTTa runtime with SWI-Prolog 9.3.36. PeTTa's upstream `examples/fib.metta` smoke test passed, and OmegaClaw initialized and ran its mock loop on the same stack.

### Decision

Use the locally validated PeTTa implementation running on SWI-Prolog 9.3.x as the version-0.1 runtime for `petta-chem`. Keep the chemistry kernel in PeTTa `.metta` files. Use Python only as optional thin harness/glue for configs, batch execution, storage, plotting, or filesystem logistics.

### Alternatives considered

- Python-first chemistry kernel emitting PeTTa-shaped atoms.
- Waiting for another Hyperon-family runtime before beginning exp00.
- Starting with Docker-only runtime wiring.

### Rationale and evidence

The local PeTTa/SWI stack is already installed and tested. This makes it the lowest-friction path that satisfies Benjamin's PeTTa-first constraint while preserving future seams for MORK or other acceleration.

### Consequences

- exp00 starts as executable PeTTa tests, not a Python simulation.
- Every consequential run should record the PeTTa commit, SWI version, command, and output.
- Runtime docs live in the implementation repo at `docs/runtime.md`.

### Revisit trigger

Revisit if PeTTa/SWI cannot express or test deterministic replay and ACS detection without misleading semantics or unacceptable fragility.

### Supersedes or superseded by

Complements `D-20260626-petta-native-kernel`.

## D-20260626-abstract-first: Start with abstract PeTTa chemistry before semantic/music/MORK integration

- Date: `2026-06-26`
- Status: `proposed`
- Decision owner: Benjamin Goertzel / ZeroBot implementation support
- Related task/run/commit: `library/petta-abstract-algorithmic-chemistry/SOURCE.md`

### Context

Benjamin provided a June 2026 design PDF for initial abstract algorithmic chemistry experiments in PeTTa. The document argues for proving replayable, causally testable ACS dynamics in a bounded symbolic chemistry before adding semantic graph chemistry, music molecules, MORK execution, PLN, MOSES, or other larger subsystems.

### Decision

Use the PDF as the seed specification for `projects/petta-chem`. Treat version 0.1 as an abstract PeTTa/Atomspace-shaped chemistry focused on deterministic replay, planted ACS recovery, random polymer ACS emergence tests, and intervention/ablation evidence.

### Alternatives considered

- Begin directly with semantic graph chemistry.
- Begin directly with music chemistry.
- Couple the prototype tightly to MORK from the start.
- Build a large open-ended chemistry system before validating replay and ACS detection.

### Rationale and evidence

The PDF's rationale is that abstract molecules and catalytic rewrite rules allow fast, interpretable experiments and reduce confounds from graph normalization, truth propagation, language realization, or musical scoring. It also emphasizes that MORK seams should be preserved as interfaces rather than blocking the first implementation.

### Consequences

- Version 0.1 must prioritize event logs, seed discipline, snapshot/replay, conservative ACS detection, and controls.
- MORK/semantic/music code is postponed until the abstract substrate yields validated evidence.
- Implementation tasks should be milestone-sized and test-gated.

### Revisit trigger

Revisit if exp01 cannot recover planted ACSs, exp02 only yields trivial/hand-coded ACSs, deterministic replay remains unreliable, or PeTTa integration constraints make the abstract-first design impractical.

### Supersedes or superseded by

None.
