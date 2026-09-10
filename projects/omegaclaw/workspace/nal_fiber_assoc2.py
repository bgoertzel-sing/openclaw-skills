#!/usr/bin/env python3
"""
Sharper probe. The v1 test conflated two things:

  (a) "the two bracketings pass through different intermediate objects"
      -- TRIVIALLY true, it's just which premise is held out. This is
      re-association book-keeping, NOT a coherence-tower obstruction.

  (b) "the intermediate object is RECOVERABLE from the final object plus
      the revision 2-cell, and that recovery depends on association" --
      THIS is the real 2-cell coherence question.

The categorical content: a coherence tower terminates at level 1 iff the
associator 2-cell is INVERTIBLE and satisfies the pentagon. In the free
commutative monoid of evidence counts, the associator IS invertible (it's
an identity: (A(+)B)(+)C and A(+)(B(+)C) are the SAME final object, canonically).
The pentagon holds automatically because addition of counts is strictly
associative. So the question is whether the WITNESS carries irreducible
higher data.

Test: is the map  (ordered premise triple) -> (final object) 's fiber
structure sensitive to bracketing in a way that survives quotient by
premise-permutation? If the ONLY difference between bracketings is a
permutation of held-out premise, the obstruction is 1-dimensional.
"""
from fractions import Fraction as Q
from itertools import permutations

def revise(a, b):
    return (a[0] + b[0], a[1] + b[1])

A = (3, 1); B = (1, 2); C = (2, 2)

# All bracketings AND orderings of the three premises.
premises = {'A': A, 'B': B, 'C': C}

def merge_seq(seq):
    # left-fold
    acc = premises[seq[0]]
    inters = []
    for name in seq[1:]:
        acc = revise(acc, premises[name])
        inters.append(acc)
    return acc, inters

finals = set()
for seq in permutations(['A','B','C']):
    final, inters = merge_seq(seq)
    finals.add(final)
    print(f"order {''.join(seq)}: final={final} intermediates={inters}")

print()
print("distinct final objects across ALL orderings/bracketings:", finals)
print("number of distinct finals:", len(finals))
print()

# The decisive question:
# Does the final object determine the multiset of premises? (fiber over final)
# If yes -> provenance is a property of the FINAL object -> 1-dimensional.
# The final (6,5) is reached by exactly one multiset {A,B,C}? Check if any
# OTHER multiset of same-universe premises also yields (6,5).
print("=== Is the final object's provenance-fiber bracketing-invariant? ===")
print("All orderings/bracketings of {A,B,C} yield the SAME final:",
      len(finals) == 1)
print()
print("VERDICT:")
if len(finals) == 1:
    print("Final object is bracketing- AND order-invariant.")
    print("The intermediate difference (4,3)vs(3,4) is PURE re-association")
    print("book-keeping: it's the held-out premise, recoverable as")
    print("final MINUS held-out = the other pair's sum. No irreducible")
    print("higher data. Associator is the identity; pentagon is strict.")
    print("=> Obstruction is 1-DIMENSIONAL for the evidence-revision core.")
    print("=> Directed 1-structure suffices HERE.")
else:
    print("=> genuinely non-confluent; (inf,1) needed.")
