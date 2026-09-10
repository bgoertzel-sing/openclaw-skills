# Decisions

## 2026-07-09 — Local-first, approval-gated Runpod pilot

**Decision:** Do not start Runpod resources until a concrete bounded pilot spec is approved. First build the local repository scaffold and smoke tests, then request approval for a small Runpod run.

**Rationale:** Runpod is paid remote compute; autonomous spend budget is USD 0. The HDPC paper's implementation section identifies likely silent-corruption bugs (detach discipline, `use_cache=False`, dropout off, fp32 errors), so cheap local tests should precede GPU spend.

**Initial recommended pilot:** single 24–48GB GPU, LoRA, Tiny Shakespeare, homotopy stages `T={1,2}`, with hard wall-clock and cost cap to be filled in after current Runpod pricing is checked.
