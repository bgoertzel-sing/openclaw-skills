---
name: hyperon-workownerch
description: Clone, build, test, compare, and modify Hyperon-family systems including MeTTa, PeTTa, MORK, hyperon-experimental, and MeTTa-WAM. Use when work involves these repositories, their languages, runtimes, native dependencies, interoperability, or semantic experiments.
---

# Hyperon Workownerch

These repositories evolve rapidly. The checked-out repository at the pinned commit, its CI, and its dependency manifests outrank remembered commands.

## Discover and pin

1. Identify the canonical repository and relevant branch/tag.
2. Clone under the active project's `repos/` directory.
3. Record remote URL, exact commit, date, and dirty state in `PROJECT.md` or a run record.
4. Read README, linked wiki/docs, CI workflows, submodules, build scripts, manifests, and recent changes related to the task.

## Isolate environments

- Python: project virtual environment or repository-declared environment.
- Rust: repository-pinned toolchain; use `rustup` rather than replacing system Rust.
- SWI-Prolog: verify the actual version and Janus support before PeTTa work.
- Native build: record GCC/Clang, CMake, Conan, OpenSSL, zlib, and other relevant versions.
- Containers: pin image digest/tag and bind only required paths.

Do not globally upgrade or downgrade a toolchain merely to satisfy one experiment without approval and a rollback plan.

## Current orientation, to be revalidated

- PeTTa is a Prolog implementation of MeTTa and currently documents SWI-Prolog 9.3.x or newer plus Python/Janus. Optional build paths integrate MORK and FAISS.
- MORK currently documents a command-line build under `kernel/` using `cargo build --release` and a nightly Rust toolchain.
- `hyperon-experimental` offers released Python/Docker paths and a source build using Rust, Python development tooling, a C compiler, CMake, and repository-specific dependencies.
- MeTTa-WAM/MeTTaLog may offer Docker-based isolation.

Do not assume these details remain current; verify every time.

## Minimal-first workflow

1. Reproduce the smallest upstream smoke test unchanged.
2. Capture the exact command and output in an experiment record.
3. Add the smallest task-specific test or MeTTa/PeTTa program.
4. Compare semantics and performance only under documented equivalent conditions.
5. When modifying semantics, state the intended language-level implication, not only the code diff.
6. Preserve failing examples as regression tests when licensing permits.

## Report

Include repository/commit, toolchains, command, test result, semantic observations, performance conditions, documentation discrepancies, and exact reproduction steps.
