# OmegaSelf Policy Gate Decision Contract

Schema: `omegaself.policy_decision` version `1.0.0`.

## Canonical record

```metta
(PolicyDecision
  (schema "omegaself.policy_decision" "1.0.0")
  (id "decision-001")
  (closure "sha256:<64 lowercase hex>")
  (clocks (causal "cycle:44") (record "2026-07-20T12:02:00Z") (adoption "decision-log:9"))
  (proposal "proposal-001")
  (prediction "pred-001")
  (decision "Allow")
  (authorization (manifest "policy:v3") (manifest-hash "sha256:<64 lowercase hex>") (issuer "external:operator") (verification "Verified") (scope "read_only_probe") (expires "2026-07-20T13:00:00Z"))
  (authority-inputs "signed_manifest" "runtime_capability")
  (causes))
```

`decision` is exactly one of `Allow`, `Deny`, `RequireProbe`, `RequireReview`, or `Defer`. Authorization verification is `Verified`, `Unverified`, `BadSignature`, or `Expired`. Only `Allow` requires `Verified`, a future expiry relative to the record clock, and an empty cause list. Every non-Allow decision requires at least one typed cause.

Cause codes are closed in version 1.0.0: `MISSING_EVIDENCE`, `INCOMPLETE_CLOSURE`, `UNKNOWN_AUTHORITY`, `BAD_SIGNATURE`, `EXPIRED_AUTHORITY`, `CAPABILITY_MISSING`, `POLICY_PROHIBITED`, `PROBE_REQUIRED`, `REVIEW_REQUIRED`, `CONTINUITY_FAILURE`, `CACHE_MISS`, `UNSUPPORTED_SEMANTICS`, `BUDGET_EXHAUSTED`, `CONFLICTING_COMMITMENTS`, and `TEMPORAL_CONTRACT_VIOLATION`.

The authorization envelope reports externally established authority; it does not create authority. `authority-inputs` must be non-empty, unique, and may name signed policy, runtime, capability, attestation, or review inputs. Any input beginning `affect:` is invalid: affective state may change estimates or proposal priority but never expands authorization. Unknown decision classes fail closed at parsing rather than becoming Allow.

## Failure contract

Unknown fields/enums/cause codes, malformed authorization, affect-derived authority, invalid Allow conditions, cause incompatibility, invalid expiry, and trailing input raise a validation error and return no decision.
