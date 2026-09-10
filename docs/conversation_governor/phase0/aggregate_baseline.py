#!/usr/bin/env python3
"""Aggregate Phase 0 run-level JSONL into baseline metrics.

Reads run records (one JSON per line) on stdin, writes a JSON summary to
stdout. No-op classes (terminal text, whitespace-normalized, case-folded):
  ""           — empty reply
  "no_reply"   — suppression directive leaked or intended-silent
  "heartbeat_ok" — heartbeat idle reply
Duplicates: consecutive runs in the same file with identical non-noop text.
"""
import json
import sys
from collections import Counter, defaultdict

NOOP = {"", "no_reply", "heartbeat_ok"}

runs = []
for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            runs.append(json.loads(line))
        except json.JSONDecodeError:
            pass

by_file = defaultdict(list)
for r in runs:
    by_file[r["file"]].append(r)

total_runs = total_calls = 0
total_cost = total_tok = 0.0
noop_runs = noop_cost = noop_tok = 0.0
noop_calls = 0
hb_runs = hb_noop = 0
dup_runs = dup_cost = 0
noop_kind = Counter()
dup_texts = Counter()

for f, fruns in by_file.items():
    fruns.sort(key=lambda r: r.get("ts") or "")
    prev_text = None
    for r in fruns:
        total_runs += 1
        total_calls += r["calls"]
        total_cost += r["cost"]
        total_tok += r["tok"]
        norm = " ".join(r["text"].split()).strip().lower()
        if r.get("trig_hb"):
            hb_runs += 1
        if norm in NOOP:
            noop_runs += 1
            noop_calls += r["calls"]
            noop_cost += r["cost"]
            noop_tok += r["tok"]
            noop_kind[norm or "<empty>"] += 1
            if r.get("trig_hb"):
                hb_noop += 1
        elif norm and norm == prev_text:
            dup_runs += 1
            dup_cost += r["cost"]
            dup_texts[r["text"][:80]] += 1
        prev_text = norm

pct = lambda a, b: round(100.0 * a / b, 2) if b else 0.0
summary = {
    "runs": total_runs,
    "llm_calls": total_calls,
    "cost_usd": round(total_cost, 2),
    "tokens": int(total_tok),
    "noop_runs": noop_runs,
    "noop_run_pct": pct(noop_runs, total_runs),
    "noop_llm_calls": noop_calls,
    "noop_call_pct": pct(noop_calls, total_calls),
    "noop_cost_usd": round(noop_cost, 2),
    "noop_cost_pct": pct(noop_cost, total_cost),
    "noop_token_pct": pct(noop_tok, total_tok),
    "noop_kinds": dict(noop_kind.most_common()),
    "heartbeat_runs": hb_runs,
    "heartbeat_noop_pct": pct(hb_noop, hb_runs),
    "dup_runs": dup_runs,
    "dup_run_pct": pct(dup_runs, total_runs),
    "dup_cost_usd": round(dup_cost, 2),
    "top_dups": dup_texts.most_common(5),
}
json.dump(summary, sys.stdout, indent=2)
print()
