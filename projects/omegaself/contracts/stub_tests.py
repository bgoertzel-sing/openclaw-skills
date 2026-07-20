#!/usr/bin/env python3
"""Dependency-free canonical parser/validator and fixture tests for Track D."""
from __future__ import annotations

import datetime as dt
import math
import re
import unittest
from dataclasses import dataclass
from pathlib import Path


class ContractError(ValueError):
    pass


@dataclass(frozen=True)
class Atom:
    value: object
    quoted: bool = False


TOKEN = re.compile(r'\s*(?:(\()|(\))|("(?:\\["\\/bfnrt]|\\u[0-9a-fA-F]{4}|[^"\\])*")|([^\s()]+))')
HASH = re.compile(r"sha256:[0-9a-f]{64}\Z")
RFC3339 = re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ\Z")


def parse(text: str):
    pos, tokens = 0, []
    while pos < len(text):
        m = TOKEN.match(text, pos)
        if not m:
            if text[pos:].strip() == "":
                pos = len(text)
                break
            raise ContractError(f"invalid token at byte {pos}")
        pos = m.end()
        if m.group(1): tokens.append("(")
        elif m.group(2): tokens.append(")")
        elif m.group(3):
            import json
            tokens.append(Atom(json.loads(m.group(3)), True))
        else:
            raw = m.group(4)
            if raw == "true": value = True
            elif raw == "false": value = False
            elif raw == "null": value = None
            else:
                try: value = int(raw)
                except ValueError:
                    try: value = float(raw)
                    except ValueError: value = raw
            tokens.append(Atom(value))
    index = 0
    def one():
        nonlocal index
        if index >= len(tokens): raise ContractError("unexpected end")
        token = tokens[index]; index += 1
        if token == "(":
            out = []
            while index < len(tokens) and tokens[index] != ")": out.append(one())
            if index >= len(tokens): raise ContractError("unclosed list")
            index += 1
            return out
        if token == ")": raise ContractError("unexpected close")
        return token
    value = one()
    if index != len(tokens): raise ContractError("trailing input")
    return value


def render(value) -> str:
    import json
    if isinstance(value, list): return "(" + " ".join(render(v) for v in value) + ")"
    if value.quoted: return json.dumps(value.value, ensure_ascii=False, separators=(",", ":"))
    if value.value is True: return "true"
    if value.value is False: return "false"
    if value.value is None: return "null"
    return str(value.value)


def val(atom):
    if not isinstance(atom, Atom): raise ContractError("expected atom")
    return atom.value


def form(node, name, size=None):
    if not isinstance(node, list) or not node or val(node[0]) != name: raise ContractError(f"expected {name}")
    if size is not None and len(node) != size: raise ContractError(f"{name}: wrong arity")
    return node


def nonempty(atom, label):
    value = val(atom)
    if not isinstance(value, str) or not value: raise ContractError(f"{label}: non-empty string required")
    return value


def timestamp(atom, label):
    value = nonempty(atom, label)
    if not RFC3339.fullmatch(value): raise ContractError(f"{label}: UTC RFC3339 required")
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def common(root, tag, schema):
    form(root, tag)
    form(root[1], "schema", 3)
    if (val(root[1][1]), val(root[1][2])) != (schema, "1.0.0"): raise ContractError("unsupported schema/version")
    form(root[2], "id", 2); nonempty(root[2][1], "id")
    form(root[3], "closure", 2)
    if not HASH.fullmatch(nonempty(root[3][1], "closure")): raise ContractError("bad closure")
    clocks = form(root[4], "clocks", 4)
    for child, label in zip(clocks[1:], ("causal", "record", "adoption")):
        form(child, label, 2); nonempty(child[1], label)
    timestamp(clocks[2][1], "record clock")


def validate_evidence(root):
    if len(root) != 11: raise ContractError("EvidenceRecord: wrong field count")
    common(root, "EvidenceRecord", "omegaself.evidence_record")
    form(root[5], "event-version", 2)
    if not isinstance(val(root[5][1]), int) or val(root[5][1]) < 1: raise ContractError("bad event version")
    form(root[6], "kind", 2); nonempty(root[6][1], "kind")
    form(root[7], "payload-hash", 2)
    if not HASH.fullmatch(nonempty(root[7][1], "payload hash")): raise ContractError("bad payload hash")
    p = form(root[8], "provenance", 4)
    form(p[1], "source", 2); nonempty(p[1][1], "source")
    form(p[2], "method", 2); nonempty(p[2][1], "method")
    parents = form(p[3], "parents")
    for x in parents[1:]: nonempty(x, "parent")
    times = form(root[9], "timestamps", 4)
    ts = []
    for child, label in zip(times[1:], ("observed", "recorded", "adopted")):
        form(child, label, 2); ts.append(timestamp(child[1], label))
    if ts != sorted(ts): raise ContractError("timestamps out of order")
    replay = form(root[10], "replay", 5)
    for child, label in zip(replay[1:3], ("adapter", "input-hash")): form(child, label, 2)
    nonempty(replay[1][1], "adapter")
    if not HASH.fullmatch(nonempty(replay[2][1], "input hash")): raise ContractError("bad replay input hash")
    form(replay[3], "command", 2); nonempty(replay[3][1], "command")
    form(replay[4], "deterministic", 2)
    if not isinstance(val(replay[4][1]), bool): raise ContractError("deterministic must be boolean")


def validate_prediction(root):
    if len(root) != 11: raise ContractError("PreActionPrediction: wrong field count")
    common(root, "PreActionPrediction", "omegaself.pre_action_prediction")
    target = form(root[5], "target", 3)
    for child, label in zip(target[1:], ("proposal", "action-class")): form(child, label, 2); nonempty(child[1], label)
    dist = form(root[6], "distribution")
    if len(dist) < 3: raise ContractError("at least two outcomes required")
    labels, probs = [], []
    for item in dist[1:]:
        form(item, "outcome", 3); labels.append(nonempty(item[1], "outcome")); probs.append(val(item[2]))
    if len(labels) != len(set(labels)): raise ContractError("duplicate outcome")
    if any(not isinstance(p, (int, float)) or isinstance(p, bool) or not math.isfinite(p) or p < 0 or p > 1 for p in probs) or abs(sum(probs)-1) > 1e-9: raise ContractError("invalid distribution")
    needs = form(root[7], "affected-needs")
    names = []
    for item in needs[1:]:
        form(item, "need", 3); names.append(nonempty(item[1], "need")); delta = val(item[2])
        if not isinstance(delta, (int,float)) or isinstance(delta,bool) or not -1 <= delta <= 1: raise ContractError("invalid need delta")
    if len(names) != len(set(names)): raise ContractError("duplicate need")
    form(root[8], "confidence", 2); confidence = val(root[8][1])
    if not isinstance(confidence,(int,float)) or isinstance(confidence,bool) or not 0 <= confidence <= 1: raise ContractError("invalid confidence")
    form(root[9], "rubric", 2); nonempty(root[9][1], "rubric")
    ordering = form(root[10], "ordering", 4)
    values = []
    for child, label in zip(ordering[1:], ("proposal-created", "prediction-committed", "action-authorized")):
        form(child, label, 2); values.append(val(child[1]))
    if not all(isinstance(v,int) and not isinstance(v,bool) and v > 0 for v in values[:2]) or values[0] >= values[1]: raise ContractError("prediction not committed after proposal")
    if values[2] is not None and (not isinstance(values[2],int) or isinstance(values[2],bool) or values[1] >= values[2]): raise ContractError("prediction not committed before authorization")
    # status follows ordering in canonical v1
    # This explicit lookup also rejects reordered/extra fields.
    # len check above is adjusted by accepting status as final field below.


CAUSES = {"MISSING_EVIDENCE","INCOMPLETE_CLOSURE","UNKNOWN_AUTHORITY","BAD_SIGNATURE","EXPIRED_AUTHORITY","CAPABILITY_MISSING","POLICY_PROHIBITED","PROBE_REQUIRED","REVIEW_REQUIRED","CONTINUITY_FAILURE","CACHE_MISS","UNSUPPORTED_SEMANTICS","BUDGET_EXHAUSTED","CONFLICTING_COMMITMENTS","TEMPORAL_CONTRACT_VIOLATION"}


def validate_policy(root):
    if len(root) != 11: raise ContractError("PolicyDecision: wrong field count")
    common(root, "PolicyDecision", "omegaself.policy_decision")
    form(root[5], "proposal", 2); nonempty(root[5][1], "proposal")
    form(root[6], "prediction", 2); nonempty(root[6][1], "prediction")
    form(root[7], "decision", 2); decision = val(root[7][1])
    if decision not in {"Allow","Deny","RequireProbe","RequireReview","Defer"}: raise ContractError("unknown decision")
    auth = form(root[8], "authorization", 7)
    expected = ("manifest","manifest-hash","issuer","verification","scope","expires")
    values = {}
    for child, label in zip(auth[1:], expected): form(child, label, 2); values[label] = nonempty(child[1], label)
    if not HASH.fullmatch(values["manifest-hash"]): raise ContractError("bad manifest hash")
    if values["verification"] not in {"Verified","Unverified","BadSignature","Expired"}: raise ContractError("bad verification")
    expires = timestamp(auth[6][1], "expires")
    inputs = form(root[9], "authority-inputs")
    inputs_v = [nonempty(x, "authority input") for x in inputs[1:]]
    if not inputs_v or len(inputs_v) != len(set(inputs_v)): raise ContractError("authority inputs must be non-empty and unique")
    if any(x.startswith("affect:") for x in inputs_v): raise ContractError("affective state cannot confer authority")
    causes = form(root[10], "causes"); cause_v = [val(x) for x in causes[1:]]
    if len(cause_v) != len(set(cause_v)) or any(x not in CAUSES for x in cause_v): raise ContractError("unknown/duplicate cause")
    record_time = timestamp(root[4][2][1], "record clock")
    if decision == "Allow":
        if values["verification"] != "Verified" or expires <= record_time or cause_v: raise ContractError("Allow lacks valid external authority")
    elif not cause_v: raise ContractError("non-Allow requires cause")


def validate(root):
    if not isinstance(root, list) or not root: raise ContractError("record list required")
    tag = val(root[0])
    if tag == "EvidenceRecord": validate_evidence(root)
    elif tag == "PreActionPrediction":
        # prediction has status as the eleventh field after ordering
        if len(root) != 12: raise ContractError("PreActionPrediction: wrong field count")
        status = root.pop()
        try:
            validate_prediction(root)
            form(status, "status", 2)
            if val(status[1]) != "committed": raise ContractError("prediction status must be committed")
        finally: root.append(status)
    elif tag == "PolicyDecision": validate_policy(root)
    else: raise ContractError("unknown record type")
    return root


FIXTURES = Path(__file__).with_name("fixtures")


class FixtureTests(unittest.TestCase):
    def test_valid_and_edge_round_trip_byte_identical(self):
        for path in sorted(FIXTURES.glob("*.metta")):
            if "malformed" in path.name: continue
            with self.subTest(path=path.name):
                raw = path.read_text(encoding="utf-8")
                tree = validate(parse(raw))
                self.assertEqual(render(tree) + "\n", raw)

    def test_malformed_fail_cleanly(self):
        for path in sorted(FIXTURES.glob("*malformed*.metta")):
            with self.subTest(path=path.name):
                with self.assertRaises(ContractError): validate(parse(path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
