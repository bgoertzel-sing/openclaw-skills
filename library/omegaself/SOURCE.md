# OmegaSelf — Source Provenance

## Source

- Delivered by Ben Goertzel via Telegram direct message, 2026-07-15 15:54 PDT
- Original filename: `OmegaSelf.zip`
- Telegram file ID: `BQACAgUAAxkBAAIezmpYD7PR7vSgArdRioi5DUJGgltDAAKzHgACCSrAVlG6Mz3-ENrXPQQ`

## Local copies

| File | SHA-256 | Path |
|------|---------|------|
| OmegaSelf.zip | `4b2aca4cd246034042940435557163f947e313608074ce288afc3c8b8286bf88` | `library/omegaself/OmegaSelf.zip` |
| OmegaSelf_Architecture_and_Deployment_Guide.pdf | `d8f6da10781f00e843dad3cf564405672bda522715b71aa242364ea242b9cc13` | `library/omegaself/OmegaSelf_Architecture_and_Deployment_Guide.pdf` |
| OmegaSelf_Architecture_and_Deployment_Guide.tex | `ee90842dae56bbe028bde65f23eb6deb200c9d6ec77c3d27ec7bfc91646238e7` | `library/omegaself/OmegaSelf_Architecture_and_Deployment_Guide.tex` |
| omegaself-coding-agent-pack.zip (inner) | `560b4dfd376aabff2f43696a33c8b3e3ebc0b2bf931375da5b011ad9dfbba747` | inside OmegaSelf.zip |

## Summary

OmegaSelf is an evidence-grounded, continuously tested self-theory and governance layer for OmegaClaw systems using Hyperon, MeTTa/PeTTa, and PLN-style uncertain reasoning. First public edition, 2026-07-15.

### Package contents (138 files)

- **Architecture and Deployment Guide** (PDF + TeX)
- **Core requirements** — normative implementation boundaries
- **Concise design proposal**
- **Coding agent pack**:
  - Python package (`omegaself`): evidence ledger, applicability, context graph, continuity certificates/cache/verifier, reasoner SPI with Patham9 and OmegaPLN adapters, governance, attestation, policy, predictions, canonical types, CLI
  - MeTTa self-model (15 `.metta` files): types, beliefs, observations, predictions, governance, continuity, applicability, skills, loop_hooks, tripwires, reasoner_seam, policy_authority, continuity_certificates, module
  - OmegaClaw bridge: `omegaself_bridge.py` + 3 patch examples
  - 13 ADRs
  - 8 example scripts
  - Config templates
  - 44 Python unit tests, 21 JSON Schemas (Draft 2020-12)
  - SHA-256 manifest, smoke test script

### Core design principles

1. Evidence is append-only; staleness changes applicability, not history
2. `SelfReasoner` is substrate-neutral; Patham9/OmegaPLN are adapters behind it
3. Only externally-signed policy manifests can authorize actions
4. `SelfHereNow` from renewable live causal control, not copied history
5. High-impact mutations fail closed on cache miss
6. Forks create branching continuity, not identity equality

## Relationships

- **OmegaClaw/ProtoMegaBot**: direct integration target — slots between parse and eval in the OmegaClaw loop
- **petta-memory**: Patham9 PLN adapter connects to existing Patham9 PLN work
- **Machintel v2**: OmegaSelf governance layer addresses the continuation/protocol bug class observed on ProtoMegaBot
- **ProtoMegaBot2 canary**: testing target before live ProtoMegaBot deployment

## Extraction location

Unzipped to `scratch/omegaself-inspect/OmegaSelf/` for inspection.
