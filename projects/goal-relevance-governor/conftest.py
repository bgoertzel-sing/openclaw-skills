#!/usr/bin/env python3
"""Root conftest.py — makes atomspace/ and evaluator/ importable from any test location."""
import os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
for sub in ("atomspace", "evaluator"):
    p = os.path.join(ROOT, sub)
    if os.path.isdir(p) and p not in sys.path:
        sys.path.insert(0, p)
