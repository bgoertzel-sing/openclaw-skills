#!/usr/bin/env python3
"""CAROM GPT-2 piecewise schedule: high-LR phase then low-LR anneal.

Phase 1: peak LR 2e-3, 5% warmup, cosine decay over 3000 steps (fast learning).
Phase 2: peak LR 1e-4, 5% warmup, cosine decay to 1e-5 over remaining steps
(stable anneal). Tests whether combining the proven fast-learning phase with
the proven stable phase avoids collapse and reaches higher final accuracy.
"""
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


def piecewise_lr(step, phase1_steps, phase2_steps,
                 phase1_peak=2e-3, phase2_peak=1e-4,
                 warmup_fraction=0.05, floor_fraction=0.10):
    """Piecewise schedule: high-LR cosine for phase 1, low-LR cosine for phase 2.

    Phase 1: 5% linear warmup to phase1_peak, then cosine decay to phase2_peak.
    Phase 2: no warmup (model is already trained), cosine decay from phase2_peak
    to floor_fraction * phase2_peak.
    """
    warmup1 = max(1, round(phase1_steps * warmup_fraction))
    if step < phase1_steps:
        if step < warmup1:
            return phase1_peak * (step + 1) / warmup1
        progress = min(1.0, (step - warmup1) / max(1, phase1_steps - warmup1 - 1))
        # Phase 1 decays from phase1_peak down to phase2_peak
        return phase2_peak + (phase1_peak - phase2_peak) * 0.5 * (1 + math.cos(math.pi * progress))
    else:
        # Phase 2: no warmup, direct cosine decay from phase2_peak to floor
        step2 = step - phase1_steps
        total2 = max(1, phase2_steps - 1)
        progress2 = min(1.0, step2 / total2)
        return phase2_peak * (floor_fraction + (1 - floor_fraction) * 0.5 * (1 + math.cos(math.pi * progress2)))


def original_onecycle_lr(step, total_steps, peak_lr=2e-3,
                         warmup_fraction=0.05, floor_fraction=0.10):
    """Replicate the original OneCycleLR for the control arm."""
    warmup = max(1, round(total_steps * warmup_fraction))
    if step < warmup:
        return peak_lr * (step + 1) / warmup
    progress = min(1.0, (step - warmup) / max(1, total_steps - warmup - 1))
    return peak_lr * (floor_fraction + (1 - floor_fraction) * 0.5 * (1 + math.cos(math.pi * progress)))


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


def train_arm(*, arm, language_model, initial_state, rng_state, steps,
              phase1_steps, phase2_steps, schedule_type, batch_size,
              output_dir, corpora, seed=0, eval_interval=500):
    torch.manual_seed(seed)
    rng = random.Random(seed)
    if rng_state is not None:
        rng.set_state(rng_state)
    model = exp2.CompiledChannel(language_model.d).to(exp2.DEVICE)
    if initial_state is not None:
        model.load_state_dict(initial_state)
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)

    if schedule_type == "piecewise":
        lr_fn = lambda s: piecewise_lr(s, phase1_steps, phase2_steps)
    elif schedule_type == "onecycle":
        lr_fn = lambda s: original_onecycle_lr(s, steps)
    else:
        raise ValueError(f"unknown schedule {schedule_type}")

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_fn)

    config = {
        "arm": arm, "steps": steps, "schedule": schedule_type,
        "phase1_steps": phase1_steps, "phase2_steps": phase2_steps,
        "phase1_peak_lr": 2e-3, "phase2_peak_lr": 1e-4,
        "batch_size": batch_size, "weight_decay": 1e-4, "gradient_clip": 1.0,
        "seed": seed,
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

    total_steps = 4 if args.smoke else 12000
    phase1_steps = 2 if args.smoke else 3000
    phase2_steps = total_steps - phase1_steps
    eval_interval = 1 if args.smoke else 500
    batch_size = 4 if args.smoke else 64

    # Piecewise arm: high LR for 3000 steps, then low LR for 9000 steps
    piecewise = train_arm(
        arm="piecewise", language_model=language_model,
        initial_state=None, rng_state=None, steps=total_steps,
        phase1_steps=phase1_steps, phase2_steps=phase2_steps,
        schedule_type="piecewise", batch_size=batch_size,
        output_dir=args.output_dir, corpora=corpora,
        eval_interval=eval_interval,
    )

    # Control arm: original OneCycleLR (peak 2e-3, 12000 steps)
    onecycle = train_arm(
        arm="onecycle_control", language_model=language_model,
        initial_state=None, rng_state=None, steps=total_steps,
        phase1_steps=phase1_steps, phase2_steps=phase2_steps,
        schedule_type="onecycle", batch_size=batch_size,
        output_dir=args.output_dir, corpora=corpora,
        eval_interval=eval_interval,
    )

    with (args.output_dir / "summary.json").open("w") as handle:
        json.dump({"piecewise": piecewise, "onecycle_control": onecycle}, handle, indent=2)


if __name__ == "__main__":
    main()
