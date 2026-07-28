#!/usr/bin/env python3
"""Large SLT estimator validation on Tiny Shakespeare with sample-size sweeps.

Runs calibration suite, full block-WBIC with higher SGLD budget,
and sample-size sensitivity sweeps with slope fitting.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from dataclasses import asdict

sys.path.insert(0, str(Path(__file__).parent / "src"))

import torch
from relaleap.slt.tinyshakespeare import (
    run_tinyshakespeare_validation,
    run_known_singularity_calibration_check,
    run_transformer_block_wbic,
    extract_tinyshakespeare_parameter_blocks,
    train_tiny_char_transformer,
    download_tiny_shakespeare,
    load_char_dataset,
    make_evaluation_windows,
    count_parameters,
)
from relaleap.slt.wbic import TemperatureConvention
from relaleap.slt.sgld import SGLDConfig, run_sgld_chains
from relaleap.slt.energy import GaussianPrior
from relaleap.slt.diagnostics import effective_sample_size_1d


def run_sample_size_sweep(model, blocks, eval_x, eval_y, *, device, artifact_dir):
    """Run WBIC at multiple input sizes to fit slope of Delta E_n."""
    results = []
    n_values = [256, 512, 1024, 2048, 4096, 8192]

    # Pick a representative block (largest |lambda| from prior run or just use output_projection)
    target_block = None
    for b in blocks:
        if "output_projection" in b.block.name:
            target_block = b
            break
    if target_block is None:
        target_block = blocks[0]

    print(f"\n--- Sample-size sweep on block: {target_block.block.name} ---")

    for n in n_values:
        if n > int(eval_y.numel()):
            print(f"  n={n}: skipping (exceeds eval tokens {eval_y.numel()})")
            continue

        sub_x = eval_x[:n]
        sub_y = eval_y[:n]

        from relaleap.slt.tinyshakespeare import TransformerBlockEnergyModel

        energy_model = TransformerBlockEnergyModel(model, target_block, sub_x, sub_y)
        convention = TemperatureConvention.wbic_total_energy(n)

        cfg = SGLDConfig(
            num_steps=max(2000, n * 2),
            step_size=1e-5,
            burn_in=max(500, n // 2),
            thin=10,
            seed=42 + n,
            init_noise=1e-4,
            eval_interval=100,
        )

        prior = GaussianPrior(prior_scale=10.0)
        t0 = time.time()
        chains = run_sgld_chains(
            energy_model,
            energy_model.theta_hat().to(device),
            beta_total_energy=convention.beta_total_energy,
            prior=prior,
            config=cfg,
            num_chains=8,
        )

        from relaleap.slt.wbic import estimate_wbic_from_chains
        wbic = estimate_wbic_from_chains(energy_model, chains, convention=convention, prior=prior)

        ess = [effective_sample_size_1d(c.energy_trace) for c in chains]
        elapsed = time.time() - t0

        entry = {
            "n": n,
            "lambda_hat": wbic.lambda_hat,
            "lambda_se": wbic.lambda_se,
            "energy_ess": ess,
            "mean_ess": sum(ess) / len(ess) if ess else 0,
            "beta_total_energy": convention.beta_total_energy,
            "num_chains": 8,
            "num_steps": cfg.num_steps,
            "elapsed": elapsed,
        }
        results.append(entry)
        print(f"  n={n}: lambda={entry['lambda_hat']:.4f} SE={entry['lambda_se']:.4f} "
              f"meanESS={entry['mean_ess']:.1f} ({elapsed:.0f}s)")

    # Slope fitting: Delta E_n = a * log(n) + b * log(log(n)) + c
    if len(results) >= 3:
        import math
        ns = [r["n"] for r in results]
        log_n = [math.log(n) for n in ns]
        log_log_n = [math.log(math.log(n)) if n > 1 else 0 for n in ns]
        energies = [r["lambda_hat"] * r["n"] for r in results]  # Delta E_n approx

        # Simple least squares: [log_n, log_log_n, 1] -> lambda_hat
        X = [[ln, lln, 1.0] for ln, lln in zip(log_n, log_log_n)]
        XtX = [[sum(X[i][j] * X[i][k] for i in range(len(X))) for k in range(3)] for j in range(3)]
        Xty = [sum(X[i][j] * results[i]["lambda_hat"] for i in range(len(X))) for j in range(3)]

        # Solve 3x3 system
        import copy
        A = [row[:] for row in XtX]
        b = Xty[:]
        for i in range(3):
            pivot = A[i][i]
            if abs(pivot) < 1e-12:
                continue
            for j in range(3):
                A[i][j] /= pivot
            b[i] /= pivot
            for k in range(3):
                if k != i:
                    factor = A[k][i]
                    for j in range(3):
                        A[k][j] -= factor * A[i][j]
                    b[k] -= factor * b[i]

        slope_fit = {"a_log_n": b[0], "b_log_log_n": b[1], "c_intercept": b[2]}
        print(f"\n  Slope fit: a={b[0]:.4f}, b={b[1]:.4f}, c={b[2]:.4f}")
    else:
        slope_fit = None

    return {"sweep": results, "slope_fit": slope_fit}


def main():
    parser = argparse.ArgumentParser(description="Large SLT Validation on Tiny Shakespeare")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--n-chains", type=int, default=8)
    parser.add_argument("--n-samples", type=int, default=1000)
    parser.add_argument("--seq-len", type=int, default=128)
    parser.add_argument("--artifact-dir", default="results/slt_large")
    parser.add_argument("--data-dir", default="data/tinyshakespeare")
    args = parser.parse_args()

    artifact_dir = Path(args.artifact_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Large SLT Estimator Validation on Tiny Shakespeare")
    print("=" * 60)
    print(f"Device: {args.device}")
    if args.device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    print(f"Epochs: {args.epochs}, Chains: {args.n_chains}, Samples: {args.n_samples}")
    print()

    # Phase 1: Calibration check
    print("--- Phase 1: Calibration Check ---")
    cal = run_known_singularity_calibration_check(
        device=args.device, n_samples=500, n_chains=8, seed=42
    )
    print(f"Lambda hat: {cal.lambda_hat:.4f} (SE: {cal.lambda_se:.4f})")
    print(f"Target: {cal.diagnostics.get('target_lambda', '?')}")
    print(f"Passes: {cal.diagnostics.get('passes_loose_calibration', '?')}")
    print()

    # Phase 2: Train transformer and run full block-WBIC
    print("--- Phase 2: Train Transformer + Block WBIC ---")
    report = run_tinyshakespeare_validation(
        device=args.device,
        epochs=args.epochs,
        n_chains=args.n_chains,
        n_samples=args.n_samples,
        seq_len=args.seq_len,
        artifact_dir=artifact_dir,
    )

    print(f"\nModel parameters: {report['num_model_parameters']:,}")
    print(f"Parameter blocks: {report['num_parameter_blocks']}")
    print(f"Block WBIC elapsed: {report['elapsed_seconds']:.0f}s")

    # Show top blocks
    blocks_sorted = sorted(report["blocks"], key=lambda b: abs(b["lambda_hat"]), reverse=True)
    print(f"\nTop 10 blocks by |lambda|:")
    for b in blocks_sorted[:10]:
        print(f"  {b['block_name']:40s} lambda={b['lambda_hat']:+.4f} SE={b['lambda_se']:.4f} "
              f"n={b['n_parameters']:>6}")

    # Phase 3: Sample-size sweep
    print("\n--- Phase 3: Sample-Size Sweep ---")
    # Reconstruct model from checkpoint
    ckpt = torch.load(artifact_dir / "slt_tinyshakespeare" / "tiny_char_transformer.pt",
                      map_location=args.device, weights_only=False)
    from relaleap.slt.tinyshakespeare import TinyCharTransformer, TinyShakespeareConfig
    cfg_dict = ckpt["config"]
    model_cfg = TinyShakespeareConfig(**cfg_dict)
    model = TinyCharTransformer(model_cfg).to(args.device)
    model.load_state_dict(ckpt["model_state_dict"])

    blocks = extract_tinyshakespeare_parameter_blocks(model)
    data_path = download_tiny_shakespeare(artifact_dir / "slt_tinyshakespeare" / "tinyshakespeare.txt")
    dataset = load_char_dataset(data_path)
    eval_x, eval_y = make_evaluation_windows(
        dataset.tokens[int(0.9 * dataset.tokens.numel()):],
        seq_len=args.seq_len, max_sequences=128
    )

    sweep_result = run_sample_size_sweep(
        model, blocks, eval_x, eval_y,
        device=args.device, artifact_dir=artifact_dir
    )

    # Save full report
    full_report = {
        "calibration": {
            "lambda_hat": cal.lambda_hat,
            "lambda_se": cal.lambda_se,
            "status": cal.status,
            "diagnostics": cal.diagnostics,
        },
        "block_wbic": report,
        "sample_size_sweep": sweep_result,
    }
    full_path = artifact_dir / "slt_large_report.json"
    full_path.write_text(json.dumps(full_report, indent=2, default=str))

    print(f"\n=== Complete ===")
    print(f"Full report: {full_path}")
    if sweep_result.get("slope_fit"):
        sf = sweep_result["slope_fit"]
        print(f"Slope fit: a={sf['a_log_n']:.4f}, b={sf['b_log_log_n']:.4f}, c={sf['c_intercept']:.4f}")


if __name__ == "__main__":
    main()
