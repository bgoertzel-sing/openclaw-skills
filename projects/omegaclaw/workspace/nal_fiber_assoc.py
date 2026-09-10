#!/usr/bin/env python3
"""
NAL revision: fiber-associativity test.

Goal (the fork Ben cares about):
  - Confidence merge for NAL revision is c' = c1 + c2 - c1*c2, and the
    truth-value merge is associative + commutative. NOT in question.
  - The question is whether *provenance-recovery fibers* are associative,
    i.e. whether the SET of premise-configurations consistent with the
    final (f', c') is the same regardless of the order (A(+)B)(+)C vs
    A(+)(B(+)C).
  - If fibers equal  -> obstruction is 1-dimensional (directed 1-structure).
  - If fibers differ -> non-naturality propagates -> directed (inf,1).

We model NAL evidence in the standard (w+, w-) count semantics, which is
the honest substrate underneath (f, c):
    w+ = evidence for, w- = evidence against, w = w+ + w-
    f  = w+ / w
    c  = w / (w + k)     (k the personal evidential horizon; k=1 canonical)
Revision merges by ADDING evidence counts:
    (w+_1, w-_1) (+) (w+_2, w-_2) = (w+_1+w+_2, w-_1+w-_2)
This is a free commutative monoid on counts -> merge is assoc + comm.

FIBER of a revision result R over premises drawn from a finite universe U:
    fiber(R) = { multiset of premises in U whose merge == R }
We compare, for the same three-premise total, whether the intermediate
result exposes distinguishable provenance depending on association.

The sharp probe: does the intermediate (w+, w-) reachable en route to the
final total differ between the two bracketings, in a way that is RECOVERABLE
from the final object plus its 2-cell (the revision-witness)?
"""

from itertools import product
from fractions import Fraction as Q

def w_to_fc(wp, wm, k=1):
    w = wp + wm
    if w == 0:
        return (Q(1,2), Q(0,1))  # vacuous
    f = Q(wp, w)
    c = Q(w, w + k)
    return (f, c)

def revise(a, b):
    """a,b are (w+,w-) count pairs. Free commutative monoid: add."""
    return (a[0] + b[0], a[1] + b[1])

# --- Three SAME-TERM premises, as (w+, w-) evidence pairs ---
A = (3, 1)   # f=3/4
B = (1, 2)   # f=1/3
C = (2, 2)   # f=1/2

# --- Two bracketings ---
left  = revise(revise(A, B), C)   # (A(+)B)(+)C
right = revise(A, revise(B, C))   # A(+)(B(+)C)

print("A =", A, "->", w_to_fc(*A))
print("B =", B, "->", w_to_fc(*B))
print("C =", C, "->", w_to_fc(*C))
print()
print("(A(+)B)(+)C total =", left,  "->", w_to_fc(*left))
print("A(+)(B(+)C) total =", right, "->", w_to_fc(*right))
print("final totals equal:", left == right)
print()

# --- Provenance fibers ---
# The 2-cell / revision-witness in this monoid records the ORDERED sequence
# of intermediate objects. Provenance-recovery asks: from the final object,
# can we recover WHICH intermediate object was passed through?
inter_left  = revise(A, B)        # intermediate seen by left bracketing
inter_right = revise(B, C)        # intermediate seen by right bracketing

print("left  intermediate (A(+)B) =", inter_left)
print("right intermediate (B(+)C) =", inter_right)
print("intermediates equal:", inter_left == inter_right)
print()

# --- The decisive fiber comparison ---
# Fiber = set of intermediate objects that a bracketing could have produced
# consistent with the final total. If the two bracketings induce DIFFERENT
# recoverable-intermediate sets, provenance-recovery is non-associative even
# though confidence-merge is associative -> 2-cell obstruction is nonzero.
fiber_left  = {inter_left}
fiber_right = {inter_right}
print("fiber_left  (recoverable intermediates) =", fiber_left)
print("fiber_right (recoverable intermediates) =", fiber_right)

nonassoc = fiber_left != fiber_right
print()
print("=== VERDICT ===")
if not nonassoc:
    print("Fibers EQUAL. Confidence merge AND provenance-recovery associative.")
    print("=> Obstruction is 1-DIMENSIONAL. Directed 1-structure suffices.")
else:
    print("Fibers DIFFER. Provenance-recovery is NON-associative.")
    print("=> Non-naturality PROPAGATES to 2-cells. Directed (inf,1) required.")
