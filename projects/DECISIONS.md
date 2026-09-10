
## 2026-07-12: EvidenceSnapshot fingerprints bind evidence content, not only packet IDs

**Decision:** A typed piPLN evidence snapshot accepts only ACTIVE packets sharing its context and assumption/ontology versions, and its deterministic fingerprint covers packet statement, evidence deltas, token provenance, reliability/relevance metadata, origin, parents, and packet schema version.

**Rationale:** Packet IDs and token digests alone do not prove that the selected evidence weights or semantic payload are unchanged. Snapshot identity is a replay/audit boundary and must change when evidential content changes.

**Consequences:** Snapshot creation remains an immutable in-memory Phase-1 operation. Persistence, migration, runtime compilation, inference, and promotion remain separately deferred/gated.
