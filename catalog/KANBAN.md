# Cross-Project Kanban

Purpose: compact board for one-off and recurrent tasks spanning OpenClaw, Pop!_OS, MacBook, and project subagents. Project `TASKS.md` files remain authoritative; this file is an index and summary board.

Last updated: 2026-07-03

## Ready / Next

- **Chaos Language Algorithm / chaoslang first implementation** — project: `chaos-language-algorithm`; next: local pure-Python `chaoslang` repo with domain core, symbolic-string MVP, exact-reconstruction tests, then attractor benchmarks up to OmegaSim starter-vector dimensionality. Ben paused OmegaSim pending this detector. Source: Telegram msg 2325; `projects/chaos-language-algorithm/TASKS.md`.
- **petta-chem generated-unplanted exp02 sweep** — project: `petta-chem`; next: continue host-swept generated-unplanted controls unless PeTTa-side export hooks become cleaner. Source: `projects/petta-chem/TASKS.md`.
- **petta-memory PeTTaChainer add bottleneck** — project: `petta-memory`; next: instrument `compileadd` internals or find minimal/precompiled add path; current evidence says constructor is fast but size-1 add stages time out. Source: `projects/petta-memory/TASKS.md`.
- **ThreadKeeper hardening follow-up** — project: `omegaclaw`; next: continue safety/governance items after provider-fail-closed and transcript-index slices. Source: `projects/omegaclaw/TASKS.md`.
- **SpecAtom-HS / plain-to-MeTTa active compiler lane** — project: `specatom-hs`; next: keep validation/provenance tasks aligned with project `TASKS.md`. Source: `catalog/PROJECTS.md`, `projects/specatom-hs/TASKS.md`.
- **Hyperseed formalizations background lane** — project: `hyperseed-formalizations`; next: continue reverse-chronological Substack formalization and experiment annotations when not preempted. Source: `projects/hyperseed-formalizations/TASKS.md`.
- **RelaLeap SLT residual-layer pregate** — machine: MacBook/active RelaLeap subagent; next mandate: implement an SLT-informed seven-arm residual-factorization pregate (flat control, SVD/low-rank, orthogonal sparse diagnostic, non-orth dictionary, CE-gradient dictionary, Fisher/GN dictionary, rank-one atom columns) with LLC/additivity, Hessian/commutator, leakage, support-regret, and causal-fingerprint audits. Source: Telegram attachment `SLT and Residual Layers.pdf`; archived locally at `library/slt-residual-layers/SOURCE.md`.
- **Protomegabot SLT/Hyperseed synthesis** — project: `omegaclaw` / Protobots; next: ingest `library/slt-hyperseed-corpus/` slowly and produce a substantive Hyperseed-oriented perspective connecting SLT-guided residual learning, weakness/evidence, GoalChainer/MetaMo, SubRep, TransWeave, and PLN-style reasoning. Process constraint: no repeated generic boilerplate acknowledgements; only report substantive analysis/status changes. Source: Telegram msg 1937; `projects/omegaclaw/notes/2026-07-02-goalchainer-pointer.md`.

## In Progress / Running

- **CLA chaoslang implementation subagent** — project: `chaos-language-algorithm`; status: spawned 2026-07-03 to create local repo, implement tested domain core/symbolic-string/chunk-MDL slice, and record provenance. Source: subagent `cla_chaoslang_impl`.
- **OmegaClaw / ProtomegaTron supervised loop** — machine: Pop!_OS; status: running in Telegram private mode per latest summary, but summaries must distinguish MacBook-only from Pop!_OS/project subagents. Source: Telegram group msg 1843 and `projects/omegaclaw/TASKS.md`.
- **GGB capacity-gate fixture work** — project: `omegaclaw`; status: recurring local cron/project updates have been refreshing roadmap and `.metta` gate fixtures. Source: `projects/omegaclaw/TASKS.md`.

## Recurrent Pop!_OS Project Workers

These must be included in global subagent/workstream summaries even if `sessions_list` does not surface them.

- **ThreadKeeper hardening worker** — cron: `f0d70a09-ab9f-40b9-ae1c-dbe2c20c9b1c`, every 2h stagger; source: `projects/omegaclaw/`.
- **petta-chem dedicated progress worker** — cron: `c008e434-ea10-4d75-b13b-26b922d079ed`, every 2h stagger; source: `projects/petta-chem/`.
- **petta-memory progress worker** — cron: `4f4e146a-bdf9-4a6e-97da-6484cfe3f81f`, every 2h stagger; source: `projects/petta-memory/`.
- **plain-to-metta progress worker** — cron: `31e85b3b-784f-4b80-ab24-43e7167561b8`, every 2h stagger; source: `projects/specatom-hs/`.
- **Protobots GGB roadmap research worker** — cron: `15d5d56c-d393-4916-9908-ceaab07b6a2d`; include when relevant to the Protobots ecosystem.

## Blocked / Needs Ben

- **OmegaSim paused pending CLA** — project: `omegasim`; blocker/prerequisite: resume only after CLA or equivalent detector passes known-attractor grammar/compressibility benchmarks, including dimensions comparable to starter OmegaSim traces. Source: Telegram msg 2325; `projects/omegasim/TASKS.md`.
- **RelaLeap worktree cleanup** — machine: MacBook; blocker before new experiments: uncommitted `docs/relaleap_summary.{tex,pdf}` causes loop to skip new work. New SLT pregate direction is recorded under Ready / Next. Source: Telegram group msg 1843 plus 2026-07-02 SLT attachment.
- **OmegaClaw communication topology** — project: `omegaclaw`; blocker: decide real communication topology beyond private smoke. Source: `projects/omegaclaw/TASKS.md`.

## Waiting / Scheduled

- **Daily skill/tool reflection** — recurrence: daily 23:30 America/Vancouver; scheduler job: `1ad1f253-b010-4a1f-ba2f-40d0c90f4ac9`; action: review the day for repeated friction, missing skills/tools, recurring jobs, and board/source-of-truth cleanup. Source: OpenClaw cron.
- **Kanban task-board skill proposal** — status: pending Skill Workshop proposal `kanban-task-board-20260702-fce72386fe`; action: apply/install only if Ben explicitly approves the proposal. Source: Skill Workshop.
- **Cross-agent Kanban skill proposal** — status: duplicate pending Skill Workshop proposal `cross-agent-kanban-20260702-a14bb79a0a`; action: prefer consolidating with the existing Kanban proposal rather than applying both. Source: Skill Workshop.

## Done / Archived Recently

- **SWI-Prolog 9.3.36 + Janus + PeTTaChainer local runtime** — project: `petta-memory`; status: installed and smoke-verified; full upstream demos remain too verbose/long for a broad gate. Source: `projects/petta-memory/TASKS.md`.
- **Initial cross-project Kanban index** — created this file after Ben noted that a subagent summary missed Pop!_OS project subagents. Source: Telegram group msg 1845.

## Board hygiene rules

- State summary scope explicitly: all machines, Pop!_OS only, MacBook only, one project, etc.
- Before daily/global summaries, check project `TASKS.md` files, visible sessions/subagents, cron jobs, and relevant repo state.
- Keep detailed task history in project records; keep this board short and pointer-rich.
- Do not write credentials or private environment values here.
