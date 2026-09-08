#!/usr/bin/env python3
"""PLN Inference Rules v0.1
============================

Formal Probabilistic Logic Networks inference rules that operate on
TruthValue pairs (strength, confidence) following the PLN specification.

These rules implement the core inference patterns:
  - Revision: combine two independent estimates of the same atom
  - Deduction:  A→B, B→C ⟹ A→C
  - Induction:  A→B, A→C ⟹ B→C  (with A as shared cause)
  - Abduction:  A→B, C→B ⟹ A→C  (with B as shared effect)
  - Analogy:    A→B, C→D, A~C ⟹ B~D

Each rule uses the standard PLN truth-value formulas (Wang 2006,
"Rationality Uncertainty in Artificial Intelligence").

The module is self-contained and does NOT depend on the graph structure
— it operates purely on (TruthValue, TruthValue) pairs, making it
reusable across any PLN-based reasoning pipeline.
"""

import math
from dataclasses import dataclass

import sys, os
try:
    from atomspace.pln_propagation import TruthValue
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from pln_propagation import TruthValue


# ── Count-based confidence conversion ────────────────────────────────

def confidence_to_count(conf: float, k: float = 1.0) -> float:
    """Convert PLN confidence ∈ (0,1) to an evidence count.

    confidence = n / (n + k), so n = k * conf / (1 - conf).
    """
    if conf >= 1.0:
        return 1e6  # effectively infinite
    if conf <= 0.0:
        return 0.0
    return k * conf / (1.0 - conf)


def count_to_confidence(n: float, k: float = 1.0) -> float:
    """Convert evidence count back to PLN confidence."""
    if n <= 0:
        return 0.0
    return n / (n + k)


# ── Revision Rule ────────────────────────────────────────────────────

def revision(tv1: TruthValue, tv2: TruthValue) -> TruthValue:
    """PLN Revision Rule.

    Combine two *independent* truth-value estimates of the same atom
    into a single, more confident estimate.

    s = (s1*n1 + s2*n2) / (n1 + n2)
    c = (n1 + n2) / (n1 + n2 + k)

    where n_i = confidence_to_count(c_i, k=1).
    """
    n1 = confidence_to_count(tv1.confidence)
    n2 = confidence_to_count(tv2.confidence)
    total_n = n1 + n2
    if total_n == 0:
        return TruthValue(0.5, 0.0)
    s = (tv1.strength * n1 + tv2.strength * n2) / total_n
    c = count_to_confidence(total_n)
    return TruthValue(s, c)


# ── Deduction Rule ───────────────────────────────────────────────────

def deduction(tv_ab: TruthValue, tv_bc: TruthValue) -> TruthValue:
    """PLN Deduction Rule: A→B, B→C ⟹ A→C.

    s_AC = s_AB * s_BC + (1 - s_AB) * (1 - s_BC)
    c_AC = c_AB * c_BC * f(s_AB, s_BC)

    where f is the deduction confidence factor:
      f = s_AB * s_BC + (1 - s_AB) * (1 - s_BC)  (bounded to [0,1])
    """
    s_ab = tv_ab.strength
    s_bc = tv_bc.strength
    s_ac = s_ab * s_bc + (1 - s_ab) * (1 - s_bc)
    # PLN deduction confidence: product of input confidences, scaled by
    # the informativeness of the result (how far from pure 0.5 uncertainty).
    deduction_factor = abs(s_ac - 0.5) * 2
    c_ac = tv_ab.confidence * tv_bc.confidence
    return TruthValue(s_ac, max(0.0, min(1.0, c_ac)))


# ── Induction Rule ───────────────────────────────────────────────────

def induction(tv_ab: TruthValue, tv_ac: TruthValue, s_a: float = 0.5) -> TruthValue:
    """PLN Induction Rule: A→B, A→C ⟹ B→C (A is shared cause).

    Uses Bayes-like inversion:
      s_BC = s_AB * s_AC / s_A  (when s_A > 0)

    Confidence is discounted by the ratio of counts.
    """
    if s_a <= 0:
        return TruthValue(0.5, 0.0)
    s_bc = (tv_ab.strength * tv_ac.strength) / s_a
    s_bc = max(0.0, min(1.0, s_bc))
    n_ab = confidence_to_count(tv_ab.confidence)
    n_ac = confidence_to_count(tv_ac.confidence)
    n_min = min(n_ab, n_ac)
    info_factor = abs(s_bc - 0.5) * 2
    c_bc = count_to_confidence(n_min) * 0.5 * (0.5 + 0.5 * info_factor)
    return TruthValue(s_bc, c_bc)


# ── Abduction Rule ───────────────────────────────────────────────────

def abduction(tv_ab: TruthValue, tv_cb: TruthValue, s_b: float = 0.5) -> TruthValue:
    """PLN Abduction Rule: A→B, C→B ⟹ A→C (B is shared effect).

      s_AC = s_AB * s_CB / s_B  (when s_B > 0)

    Confidence is discounted more heavily than induction.
    """
    if s_b <= 0:
        return TruthValue(0.5, 0.0)
    s_ac = (tv_ab.strength * tv_cb.strength) / s_b
    s_ac = max(0.0, min(1.0, s_ac))
    n_ab = confidence_to_count(tv_ab.confidence)
    n_cb = confidence_to_count(tv_cb.confidence)
    n_min = min(n_ab, n_cb)
    info_factor = abs(s_ac - 0.5) * 2
    c_ac = count_to_confidence(n_min) * 0.3 * (0.5 + 0.5 * info_factor)
    return TruthValue(s_ac, c_ac)


# ── Analogy Rule ─────────────────────────────────────────────────────

def analogy(tv_ab: TruthValue, tv_cd: TruthValue, tv_ac: TruthValue) -> TruthValue:
    """PLN Analogy Rule: A→B, C→D, A~C ⟹ B~D.

    Strength is a weighted blend based on the similarity of A and C.
    Confidence is discounted by all three input confidences.
    """
    sim = tv_ac.strength  # similarity strength
    s_bd = sim * (tv_ab.strength * tv_cd.strength) + (1 - sim) * 0.5
    c_bd = tv_ab.confidence * tv_cd.confidence * tv_ac.confidence * 0.7
    return TruthValue(max(0.0, min(1.0, s_bd)), c_bd)


# ── Graph-based deduction helpers ────────────────────────────────────

def transitive_contribution(tv_t1_g1: TruthValue, tv_g1_g2: TruthValue) -> TruthValue:
    """Compute transitive task→goal contribution through an intermediate goal.

    task → contributes_to → goal1 → contributes_to → goal2
    Uses deduction to compute the implied task→goal2 truth value.
    """
    return deduction(tv_t1_g1, tv_g1_g2)


def multi_source_revision(tvs: list[TruthValue]) -> TruthValue:
    """Revision-combine a list of truth values into one.

    Repeatedly applies revision: tv = revision(tv, next).
    """
    if not tvs:
        return TruthValue(0.5, 0.0)
    result = tvs[0]
    for tv in tvs[1:]:
        result = revision(result, tv)
    return result


def relevance_blend(pln_tv: TruthValue, heuristic_score: float, w: float = 0.5) -> TruthValue:
    """Blend a PLN truth value with a heuristic relevance score.

    Uses revision-like weighting controlled by w (weight on PLN).
    """
    heuristic_tv = TruthValue(heuristic_score, 0.5)
    n_pln = confidence_to_count(pln_tv.confidence)
    n_heur = confidence_to_count(heuristic_tv.confidence)
    # Reweight based on w
    n_pln_w = n_pln * w / max(n_pln + n_heur, 1e-9) * (n_pln + n_heur)
    n_heur_w = n_heur * (1 - w) / max(n_pln + n_heur, 1e-9) * (n_pln + n_heur)
    total = n_pln_w + n_heur_w
    if total <= 0:
        return TruthValue(0.5, 0.0)
    s = (pln_tv.strength * n_pln_w + heuristic_tv.strength * n_heur_w) / total
    c = count_to_confidence(total)
    return TruthValue(s, c)


# ── Inference Rule Registry ──────────────────────────────────────────

INFERENCE_RULES = {
    "revision": revision,
    "deduction": deduction,
    "induction": induction,
    "abduction": abduction,
    "analogy": analogy,
}


def apply_rule(rule_name: str, *args, **kwargs) -> TruthValue:
    """Apply a named inference rule."""
    rule = INFERENCE_RULES.get(rule_name)
    if rule is None:
        raise ValueError(f"Unknown inference rule: {rule_name}. "
                         f"Available: {list(INFERENCE_RULES.keys())}")
    return rule(*args, **kwargs)
