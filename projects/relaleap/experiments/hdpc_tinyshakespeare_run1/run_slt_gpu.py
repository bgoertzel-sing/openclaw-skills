#!/usr/bin/env python3
"""Run SLT estimator validation on Tiny Shakespeare using Runpod A100 GPU.

Usage: python3 run_slt_gpu.py [--device cuda] [--epochs 3] [--n-chains 4] [--n-samples 200]
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import torch
from relaleap.slt.tinyshakespeare import (
    run_tinyshakespeare_validation,
    run_known_singularity_calibration_check,
)


def main():
    parser = argparse.ArgumentParser(description="SLT Estimator Validation on Tiny Shakespeare")
    parser.add_argument("--device", default="cuda", help="torch device (default: cuda)")
    parser.add_argument("--epochs", type=int, default=3, help="transformer training epochs")
    parser.add_argument("--n-chains", type=int, default=4, help="SGLD chains per block")
    parser.add_argument("--n-samples", type=int, default=200, help="SGLD samples per chain")
    parser.add_argument("--seq-len", type=int, default=128, help="sequence length")
    parser.add_argument("--artifact-dir", default="results/slt_tinyshakespeare", help="output directory")
    args = parser.parse_args()

    print("=" * 60)
    print("SLT Estimator Validation on Tiny Shakespeare")
    print("=" * 60)
    print(f"Device: {args.device}")
    if args.device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    print(f"Config: epochs={args.epochs}, chains={args.n_chains}, samples={args.n_samples}, seq_len={args.seq_len}")
    print()

    # Run calibration check first
    print("--- Calibration Check (product_singularity_ab2) ---")
    cal = run_known_singularity_calibration_check(
        device=args.device,
        n_samples=min(args.n_samples, 200),
        n_chains=max(4, args.n_chains),
    )
    print(f"Lambda hat: {cal.lambda_hat:.4f} (SE: {cal.lambda_se:.4f})")
    print(f"Target lambda: {cal.diagnostics.get('target_lambda', '?')}")
    print(f"Passes loose calibration: {cal.diagnostics.get('passes_loose_calibration', '?')}")
    print(f"Status: {cal.status}")
    print()

    # Run full Tiny Shakespeare validation
    print("--- Tiny Shakespeare SLT Validation ---")
    report = run_tinyshakespeare_validation(
        device=args.device,
        epochs=args.epochs,
        n_chains=args.n_chains,
        n_samples=args.n_samples,
        seq_len=args.seq_len,
        artifact_dir=Path(args.artifact_dir),
    )

    print()
    print("=" * 60)
    print("Results Summary")
    print("=" * 60)
    print(f"Model parameters: {report['num_model_parameters']:,}")
    print(f"Parameter blocks: {report['num_parameter_blocks']}")
    print(f"Tokens for WBIC: {report['n_tokens_for_wbic']}")
    print(f"Elapsed: {report['elapsed_seconds']:.1f}s")
    print()
    print(f"Calibration: lambda={report['calibration']['lambda_hat']:.4f} "
          f"(target={report['calibration']['diagnostics'].get('target_lambda', '?')}, "
          f"pass={report['calibration']['diagnostics'].get('passes_loose_calibration', '?')})")
    print()
    print(f"Block WBIC estimates (top 10 by |lambda|):")
    blocks = sorted(report["blocks"], key=lambda b: abs(b["lambda_hat"]), reverse=True)
    for b in blocks[:10]:
        ess_str = ", ".join(f"{e:.1f}" for e in b.get("energy_ess_per_chain", []))
        print(f"  {b['block_name']:40s} lambda={b['lambda_hat']:+.4f} SE={b['lambda_se']:.4f} "
              f"n={b['n_parameters']:>6} status={b['status']} ESS=[{ess_str}]")

    print()
    print(f"Full report: {args.artifact_dir}/slt_tinyshakespeare_report.json")
    print("Done.")


if __name__ == "__main__":
    main()
