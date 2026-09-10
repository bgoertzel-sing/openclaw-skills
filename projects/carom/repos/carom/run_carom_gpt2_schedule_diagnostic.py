#!/usr/bin/env python3
"""Bounded GPT-2 schedule diagnostic: low-LR warm start and fresh control."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

import exp2_compiled_channel as exp2
import harness_v2


def normalized_warmup_cosine(step, total_steps, warmup_fraction=0.05,
                             floor_fraction=0.10):
    warmup = max(1, round(total_steps * warmup_fraction))
    if step < warmup:
        return (step + 1) / warmup
    progress = min(1.0, (step - warmup) / max(1, total_steps - warmup - 1))
    return floor_fraction + (1 - floor_fraction) * 0.5 * (
        1 + math.cos(math.pi * progress)
    )


def checkpoint_payload(model, optimizer, scheduler, rng, update, config):
    return {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "scheduler": scheduler.state_dict(),
        "python_rng": rng.getstate(),
        "torch_rng": torch.random.get_rng_state(),
        "cuda_rng": torch.cuda.get_rng_state_all() if torch.cuda.is_available() else [],
        "update": update,
        "config": config,
    }


def file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def train_arm(*, arm, language_model, initial_state, rng_state, steps, peak_lr,
              batch_size, output_dir, corpora, seed=0, eval_interval=500):
    torch.manual_seed(seed)
    rng = random.Random(seed)
    if rng_state is not None:
        rng.setstate(rng_state)
    model = exp2.CompiledChannel(language_model.d).to(exp2.DEVICE)
    if initial_state is not None:
        model.load_state_dict(initial_state)
    optimizer = torch.optim.AdamW(model.parameters(), lr=peak_lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.LambdaLR(
        optimizer,
        lambda index: normalized_warmup_cosine(index, steps),
    )
    config = {
        "arm": arm, "steps": steps, "peak_lr": peak_lr,
        "schedule": "5% linear warmup then cosine decay to 0.1x peak",
        "batch_size": batch_size, "weight_decay": 1e-4, "gradient_clip": 1.0,
        "seed": seed, "optimizer_state_reset": True,
    }
    arm_dir = output_dir / arm
    arm_dir.mkdir(parents=True, exist_ok=True)
    rows, started = [], time.time()
    for update in range(steps + 1):
        if update % eval_interval == 0 or update == steps:
            checkpoint = arm_dir / f"step_{update:04d}.pt"
            torch.save(
                checkpoint_payload(model, optimizer, scheduler, rng, update, config),
                checkpoint,
            )
            row = {
                "arm": arm, "update": update,
                "effective_total_update": update + (3000 if arm == "warm_step3000" else 0),
                "lr": optimizer.param_groups[0]["lr"],
                "checkpoint": checkpoint.name,
                "checkpoint_sha256": file_sha256(checkpoint),
                "L24": harness_v2.eval_checkpoint(
                    model, language_model, corpora["val_L24"],
                    span_fn=exp2.span_reps_gpt2,
                ),
                "L5": harness_v2.eval_checkpoint(
                    model, language_model, corpora["val_L5"],
                    span_fn=exp2.span_reps_gpt2,
                ),
                "elapsed_seconds": time.time() - started,
            }
            rows.append(row)
            print(json.dumps(row), flush=True)
        if update == steps:
            break
        tokens, spans, x, y, edges, entries, orders, _ = exp2.make_batch(
            batch_size, rng
        )
        live = (orders >= 0).float()
        hidden = exp2.span_reps_gpt2(language_model, tokens, spans)
        output, edge_logits, _ = model(hidden, x, live)
        loss = F.cross_entropy(output.reshape(-1, exp2.V), y.reshape(-1))
        pair = (
            live[:, None, :] * live[:, :, None]
            * (1 - torch.eye(exp2.L_MAX, device=exp2.DEVICE)[None])
        )
        loss += F.binary_cross_entropy_with_logits(edge_logits, edges, weight=pair)
        entry_logits = model.entry(hidden).squeeze(-1) - 30 * (1 - live)
        loss += 0.2 * F.cross_entropy(entry_logits, entries.argmax(-1))
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()
        if not math.isfinite(float(loss)):
            raise RuntimeError(f"non-finite loss at update {update + 1}")
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--step3000", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--corpus", type=Path)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    language_model = exp2.GPT2Base(layer=-1).to(exp2.DEVICE)
    if args.corpus:
        corpora = harness_v2.load_corpora(args.corpus)
    else:
        corpora = harness_v2.build_corpora(
            seed=20260726, exp2_module=exp2,
            sizes={"val_L24": 16 if args.smoke else 256,
                   "val_L5": 8 if args.smoke else 128},
        )
        harness_v2.save_corpora(corpora, args.output_dir / "frozen_corpora.pt")
    original = torch.load(args.step3000, map_location="cpu", weights_only=False)
    steps = 2 if args.smoke else 3000
    fresh_steps = 2 if args.smoke else 6000
    warm = train_arm(
        arm="warm_step3000", language_model=language_model,
        initial_state=original["m"], rng_state=original.get("rng"),
        steps=steps, peak_lr=1e-4, batch_size=4 if args.smoke else 64,
        output_dir=args.output_dir, corpora=corpora,
        eval_interval=1 if args.smoke else 500,
    )
    fresh = train_arm(
        arm="fresh_low_peak", language_model=language_model,
        initial_state=None, rng_state=None, steps=fresh_steps, peak_lr=1e-4,
        batch_size=4 if args.smoke else 64, output_dir=args.output_dir,
        corpora=corpora, eval_interval=1 if args.smoke else 500,
    )
    with (args.output_dir / "summary.json").open("w") as handle:
        json.dump({"warm_step3000": warm, "fresh_low_peak": fresh}, handle, indent=2)


if __name__ == "__main__":
    main()
