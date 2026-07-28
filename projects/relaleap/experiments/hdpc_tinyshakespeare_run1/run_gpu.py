#!/usr/bin/env python3
"""Run HDPC/ePC Tiny Shakespeare training on Runpod GPU.

Usage: python3 run_gpu.py [--device cuda] [--epochs 2] [--steps-per-epoch 50]
"""

import argparse
import json
import sys
from pathlib import Path

# Ensure src is on path
sys.path.insert(0, str(Path(__file__).parent / "src"))

import torch
from relaleap.hdpc.tinyshakespeare import (
    HDPCTrainingConfig,
    HDPCTrainingResult,
    run_homotopy_kd_training,
)


def main():
    parser = argparse.ArgumentParser(description="HDPC/ePC Tiny Shakespeare GPU run")
    parser.add_argument("--device", default="cuda", help="torch device (default: cuda)")
    parser.add_argument("--epochs", type=int, default=2, help="training epochs")
    parser.add_argument("--steps-per-epoch", type=int, default=50, help="steps per epoch per temperature")
    parser.add_argument("--batch-size", type=int, default=64, help="batch size")
    parser.add_argument("--seq-len", type=int, default=128, help="sequence length")
    parser.add_argument("--d-model", type=int, default=128, help="model dimension")
    parser.add_argument("--nhead", type=int, default=4, help="attention heads")
    parser.add_argument("--d-ff", type=int, default=512, help="feedforward dimension")
    parser.add_argument("--num-layers", type=int, default=4, help="transformer layers")
    parser.add_argument("--learning-rate", type=float, default=3e-4, help="learning rate")
    parser.add_argument("--lambda-kd", type=float, default=0.05, help="KD loss weight")
    parser.add_argument("--seed", type=int, default=1234, help="random seed")
    parser.add_argument("--artifact-dir", default="results/hdpc_tinyshakespeare", help="output directory")
    parser.add_argument("--data-dir", default="data/tinyshakespeare", help="data directory")
    args = parser.parse_args()

    print(f"=== HDPC/ePC Tiny Shakespeare GPU Run ===")
    print(f"Device: {args.device}")
    if args.device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    print(f"Config: epochs={args.epochs}, steps={args.steps_per_epoch}, batch={args.batch_size}, "
          f"d_model={args.d_model}, layers={args.num_layers}, seq_len={args.seq_len}")
    print()

    config = HDPCTrainingConfig(
        device=args.device,
        epochs=args.epochs,
        steps_per_epoch=args.steps_per_epoch,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        d_model=args.d_model,
        nhead=args.nhead,
        d_ff=args.d_ff,
        num_layers=args.num_layers,
        learning_rate=args.learning_rate,
        lambda_kd=args.lambda_kd,
        seed=args.seed,
        artifact_dir=Path(args.artifact_dir),
        data_dir=Path(args.data_dir),
        download=True,
    )

    result = run_homotopy_kd_training(config)

    print(f"\n=== Results ===")
    print(f"Teacher parameters: {result.teacher_parameters:,}")
    print(f"Student parameters: {result.student_parameters:,}")
    print(f"Teacher perplexity: {result.diagnostics.teacher_perplexity:.2f}")
    print(f"Student perplexity: {result.diagnostics.student_perplexity:.2f}")
    print(f"Perplexity delta: {result.diagnostics.perplexity_delta:+.2f}")
    print(f"Energy profile length: {len(result.diagnostics.energy_profile)}")
    print(f"Update sparsity histogram (zero/tiny/small/large): "
          f"{result.diagnostics.update_sparsity_histogram}")
    print(f"Artifact saved: {result.artifact_path}")

    # Gradient diagnostics summary
    print(f"\n=== Gradient Diagnostics ===")
    for g in result.diagnostics.gradients:
        cos_str = f"{g.cosine:.4f}" if g.cosine is not None else "N/A"
        print(f"  {g.name:50s} bp_norm={g.bp_norm:.6f} pc_norm={g.pc_norm:.6f} cos={cos_str}")

    # Save summary JSON
    summary = {
        "config": {
            "device": args.device,
            "epochs": args.epochs,
            "steps_per_epoch": args.steps_per_epoch,
            "batch_size": args.batch_size,
            "seq_len": args.seq_len,
            "d_model": args.d_model,
            "nhead": args.nhead,
            "d_ff": args.d_ff,
            "num_layers": args.num_layers,
            "learning_rate": args.learning_rate,
            "lambda_kd": args.lambda_kd,
            "seed": args.seed,
        },
        "teacher_parameters": result.teacher_parameters,
        "student_parameters": result.student_parameters,
        "teacher_perplexity": result.diagnostics.teacher_perplexity,
        "student_perplexity": result.diagnostics.student_perplexity,
        "perplexity_delta": result.diagnostics.perplexity_delta,
        "energy_profile_length": len(result.diagnostics.energy_profile),
        "update_sparsity_histogram": list(result.diagnostics.update_sparsity_histogram),
        "gradient_diagnostics": [
            {
                "name": g.name,
                "bp_norm": g.bp_norm,
                "pc_norm": g.pc_norm,
                "cosine": g.cosine,
                "shape": list(g.shape),
            }
            for g in result.diagnostics.gradients
        ],
        "energy_profile_first_20": list(result.diagnostics.energy_profile[:20]),
        "energy_profile_last_20": list(result.diagnostics.energy_profile[-20:]),
        "artifact_path": str(result.artifact_path),
        "source_path": str(result.source_path),
    }
    summary_path = Path(args.artifact_dir) / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"\nSummary JSON: {summary_path}")
    print("Done.")


if __name__ == "__main__":
    main()
