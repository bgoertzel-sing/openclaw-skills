# Generalized category-slot seam v1

Status: implementation specification; synthetic validation only. This does not
revise the frozen Mackey--Glass/Lorenz--96 coding null and authorizes no new
attractor benchmark.

## Problem

`CategoryOccurrence("M", member)` must retain `member` for decoding, but chunk
mining currently includes that member in its identity key. Consequently the
blocks `a M[x] b` and `a M[y] b` cannot propose one generalized production.
Simply discarding the member would make reconstruction lossy.

## Types and invariants

- `CategorySlot("M")` is allowed only in a generalized production right-hand
  side. It matches category identity independently of the observed member.
- `GeneralizedChunkOccurrence(N, members)` is a top-level parse entry. Its
  ordered member tuple is the decoding side table for the `CategorySlot`s in
  production `N`.
- `GeneralizedChunkProposal(pattern, occurrences, name)` carries a pattern of
  ordinary entries and category slots. Every occurrence must match the whole
  pattern; each slot match must be a `CategoryOccurrence` of the same category.
- Applying a proposal replaces each non-overlapping matched block with one
  `GeneralizedChunkOccurrence`, preserving slot members in left-to-right order.
- Expansion substitutes those stored members into the production slots and
  must exactly reproduce the pre-edit expansion and original corpus.
- Mining identity and decoding identity are separate functions. Existing
  member-specific `entry_key` remains unchanged for persistence/accounting;
  the new miner uses a slot-pattern key only while proposing generalized chunks.

Malformed proposals fail closed: empty patterns, patterns without a category
slot, duplicate/overlapping/out-of-range occurrences, category mismatch, or a
slot/member arity mismatch raise `ValueError` before a state is returned.

## Modularity and scope

The new miner/applier path is additive and replaceable; existing ordinary chunk
and category behavior is unchanged. This first gate is domain/unit validation.
Persistence, fact projection, greedy joint search, and a decodable fair
model/member transmission code must explicitly support the new types before the
seam may be used in another measured attractor benchmark.

## Canonical transmission subgate

Before joint search is enabled, provide a versioned canonical state code with
two self-contained UTF-8 JSON documents:

- the model document transmits every category and production, including each
  `CategorySlot` identity;
- the data document transmits every top-level parse entry, including the full
  ordered member tuple of every `GeneralizedChunkOccurrence`.

The scorer charges exactly eight bits per emitted byte. Decoding the two
documents must reconstruct the grammar and parse without access to the stored
corpus, history, edit log, or score; the corpus is then defined by exact
expansion. Both documents carry schema/version/type tags and are framed by EOF
at this local subgate. Canonical re-encoding after decoding must be byte-stable.
This code is deliberately simple and conservative: it validates complete
transmission accounting, not optimal compression, and it is not the frozen
held-out predictive code.

## Joint proposal/search subgate

Joint discovery is an additive, replaceable seam. A joint proposal contains a
typed category proposal and a typed generalized-chunk proposal whose occurrence
indices are defined on the state after that category is applied. Applying the
joint proposal is exactly equivalent to applying those two component edits in
order; both ordinary edit-log records remain explicit for replay.

The first bounded miner uses the existing exact-context inducer with a
joint-only per-member occurrence threshold of one, applies each candidate to a
temporary state, and invokes the generalized slot miner on that state. It must
not mutate the input, inspect benchmark outcomes, or change the defaults of the
ordinary category inducer. Candidate ordering and naming must be deterministic.
Malformed or stale component proposals fail through the existing category and
generalized-chunk validators before a state is returned.

This subgate validates reachability and exact reconstruction only. It does not
authorize accepting a joint edit under the sprint-1 proxy, whose generalized
occurrence cost does not yet constitute a fair member code. A separately frozen
synthetic decision gate must use the canonical complete state code (or another
preregistered decodable code) before any measured claim or attractor run.

## Unit acceptance gate

On the already frozen 19-frame synthetic fixture, after manual application of
`M={m00,...,m18}`, the bounded generalized miner must propose
`N -> a CategorySlot(M) b` at all 19 frame starts. Applying it must
produce 19 generalized chunk occurrences with the exact ordered members and
expand byte-for-byte to the 76 original symbols. Results must be deterministic,
and existing member-specific mining behavior must remain available.

Relevant Research Rules: 1 (validate the detector/proposal tool), 2 (specify
before coding), 5 (record reproducible evidence), 6 (separate substitutability
from occurrence evidence), and 7 (keep mining, representation, decoding, and
future coding behind distinct seams).
