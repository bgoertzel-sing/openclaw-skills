# Decisions

## 2026-07-12 — Local-first, frontend-first vertical slice

Implement a deterministic parser/static-checker/reference semantics before coupling tightly to unstable MORK byte encoding. Keep the target as a versioned typed Morkql Core/Morkl AST, then connect it to the pinned runtime.

Rationale: the spec explicitly separates stable semantic requirements from implementation-dependent encoding and certificate serialization. This allows rapid tests while MORK/PathMap/Morkl provenance and toolchains are established.

## 2026-07-12 — No early petta-memory or petta-chem coupling

Preserve explicit seams but defer these integrations until the Base-profile compiler and differential tests work, per Ben's request.

## 2026-07-12 — No paid compute without a costed gate

Runpod CPU is an option if local build/test throughput is inadequate. Starting or retaining it requires provider/account/resource/cost/duration/cleanup approval.
