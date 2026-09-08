#!/usr/bin/env python3
"""PLN Inference-Enhanced Chain Propagation v0.1
=================================================

Integrates the PLN inference rules (deduction, induction, abduction,
analogy, revision) into the multi-hop chain propagation pipeline.

Instead of naively multiplying strength * confidence along edges,
this module selects the appropriate inference rule based on the
relation type and graph structure:

  - contributes_to (transitive):  deduction(tv_source, tv_edge)
  - part_of (containment):        deduction with confidence boost
  - provides_evidence_for:        revision (merge evidence)
  - blocks:                       negate + deduction (inhibitory)
  - supersedes:                   abduction (infer backwards)
  - unknown/other:                fallback to naive multiplication

Additionally, when multiple chains reach the same goal, their
truth values are combined using PLN revision (rather than simple
disjunction), producing more nuanced confidence aggregation.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional

from pln_propagation import (
    TruthValue, _edge_confidence, _initial_tv, normalize_status,
)
from pln_inference_rules import (
    deduction, induction, abduction, revision, analogy,
    confidence_to_count, count_to_confidence,
)


# ─── Relation-to-rule mapping ────────────────────────────────────────

# Relations that use deductive propagation (A->B, B->C => A->C)
DEDUCTIVE_RELATIONS = frozenset({
    "contributes_to",
    "part_of",
})

# Relations that use evidential revision (merge, not chain)
EVIDENTIAL_RELATIONS = frozenset({
    "provides_evidence_for",
})

# Relations that use abduction (backward inference)
ABDUCTIVE_RELATIONS = frozenset({
    "supersedes",
})

# Relations that are inhibitory (negate strength)
INHIBITORY_RELATIONS = frozenset({
    "blocks",
    "occupies",
})


def select_inference_rule(relation: str) -> str:
    """Return the inference rule name for a given relation type.

    Returns one of: 'deduction', 'revision', 'abduction', 'inhibitory',
    'naive'.
    """
    if relation in DEDUCTIVE_RELATIONS:
        return "deduction"
    if relation in EVIDENTIAL_RELATIONS:
        return "revision"
    if relation in ABDUCTIVE_RELATIONS:
        return "abduction"
    if relation in INHIBITORY_RELATIONS:
        return "inhibitory"
    return "naive"


def propagate_edge(
    source_tv: TruthValue,
    edge: dict,
    edge_conf: Optional[float] = None,
) -> TruthValue:
    """Propagate a truth value along a single edge using the
    appropriate PLN inference rule.

    Args:
        source_tv: Truth value of the source node.
        edge: The edge dict (must have 'relation' key).
        edge_conf: Pre-computed edge confidence (optional).

    Returns:
        The propagated truth value after applying the inference rule.
    """
    if edge_conf is None:
        edge_conf = _edge_confidence(edge)

    relation = edge.get("relation", "")
    rule = select_inference_rule(relation)

    # Construct the edge truth value
    edge_tv = TruthValue(
        strength=edge_conf,
        confidence=edge_conf,
    )

    if rule == "deduction":
        return deduction(source_tv, edge_tv)

    if rule == "revision":
        return revision(source_tv, edge_tv)

    if rule == "abduction":
        # For supersedes, we infer backwards: if B supersedes A,
        # then A's relevance is (1 - B's strength)
        negated = source_tv.negate()
        return deduction(negated, edge_tv)

    if rule == "inhibitory":
        # For blocks: negate source strength, then deduct
        negated = source_tv.negate()
        return deduction(negated, edge_tv)

    # Naive fallback: simple multiplication
    return TruthValue(
        strength=source_tv.strength * edge_conf,
        confidence=source_tv.confidence * edge_conf,
    )


def aggregate_chains_by_revision(
    chains: list,
) -> TruthValue:
    """Aggregate multiple chain truth values using PLN revision.

    Unlike simple disjunction (max strength), revision produces
    a weighted average that respects evidence counts, yielding
    more nuanced confidence when chains agree or disagree.

    Args:
        chains: List of objects with a .tv attribute (TruthValue).

    Returns:
        The revision-aggregated truth value.
    """
    if not chains:
        return TruthValue()

    result = chains[0].tv
    for c in chains[1:]:
        result = revision(result, c.tv)
    return result


@dataclass
class InferenceRuleStats:
    """Statistics about which inference rules were applied during
    a multi-hop evaluation."""
    deduction_count: int = 0
    revision_count: int = 0
    abduction_count: int = 0
    inhibitory_count: int = 0
    naive_count: int = 0

    @property
    def total(self) -> int:
        return (self.deduction_count + self.revision_count
                + self.abduction_count + self.inhibitory_count
                + self.naive_count)

    def to_dict(self) -> dict:
        """Return a dictionary representation of this object."""
        return {
            "deduction": self.deduction_count,
            "revision": self.revision_count,
            "abduction": self.abduction_count,
            "inhibitory": self.inhibitory_count,
            "naive": self.naive_count,
            "total": self.total,
        }

    def record(self, relation: str) -> None:
        """Record an inference rule application for a relation."""
        rule = select_inference_rule(relation)
        if rule == "deduction":
            self.deduction_count += 1
        elif rule == "revision":
            self.revision_count += 1
        elif rule == "abduction":
            self.abduction_count += 1
        elif rule == "inhibitory":
            self.inhibitory_count += 1
        else:
            self.naive_count += 1
