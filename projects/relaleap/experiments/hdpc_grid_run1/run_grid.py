#!/usr/bin/env python3
"""Multi-seed HDPC/ePC controlled grid on Tiny Shakespeare.

Runs teacher-only, detached-crown, and coupled-crown conditions across
multiple seeds and lambda_kd values, collecting matched control deltas.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from dataclasses import asdict

sys.path.insert(0, str(Path(__file__).parent / "src"))

import torch
from relaleap.hdpc.tinyshakespeare import (
    HDPCTrainingConfig,
    HDPCTrainingResult,
    run_homotopy_kd_training,
    CausalCharTransformerLM,
    TinyCharTransformerConfig,
    TinyShakespeareTokenizer,
    prepare_tinyshakespeare_data,
    get_batch,
    cross_entropy_for_logits,
    count_parameters,
    estimate_perplexity,
)
from torch import nn
import torch.nn.functional as F


def run_teacher_only(config: HDPCTrainingConfig) -> dict:
    """Train a teacher-only model with same compute budget, no student/crown."""
    torch.manual_seed(config.seed)
    device = torch.device(config.device)
    dataset = prepare_tinyshakespeare_data(config.data_dir, download=config.download)
    model_config = TinyCharTransformerConfig(
        vocab_size=dataset.vocab_size,
        seq_len=config.seq_len,
        d_model=config.d_model,
        nhead=config.nhead,
        d_ff=config.d_ff,
        num_layers=config.num_layers,
    )
    model = CausalCharTransformerLM(model_config).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate)
    generator = torch.Generator().manual_seed(config.seed)

    for _ in range(config.epochs):
        for temperature in config.temperatures:
            for _ in range(config.steps_per_epoch):
                x, y = get_batch(dataset.train, batch_size=config.batch_size,
                                seq_len=config.seq_len, device=device, generator=generator)
                optimizer.zero_grad(set_to_none=True)
                loss = cross_entropy_for_logits(model(x), y)
                loss.backward()
                optimizer.step()

    ppl = estimate_perplexity(model, dataset.val, seq_len=config.seq_len,
                             batch_size=min(config.batch_size, 16), device=device,
                             steps=config.eval_batches)
    return {"teacher_perplexity": ppl, "parameters": count_parameters(model)}


def main():
    parser = argparse.ArgumentParser(description="HDPC/ePC Multi-Seed Grid")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--d-model", type=int, default=256)
    parser.add_argument("--nhead", type=int, default=4)
    parser.add_argument("--d-ff", type=int, default=1024)
    parser.add_argument("--num-layers", type=int, default=6)
    parser.add_argument("--seq-len", type=int, default=256)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--steps-per-epoch", type=int, default=200)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--learning-rate", type=float, default=3e-4)
    parser.add_argument("--artifact-dir", default="results/hdpc_grid")
    parser.add_argument("--data-dir", default="data/tinyshakespeare")
    args = parser.parse_args()

    artifact_dir = Path(args.artifact_dir)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    seeds = [42, 1234, 5678]
    lambdas = [0.01, 0.05, 0.10]
    temperatures = (1.0, 2.0, 4.0, 8.0)

    all_results = []
    start = time.time()

    print(f"=== HDPC/ePC Multi-Seed Grid ===")
    print(f"Seeds: {seeds}, Lambdas: {lambdas}, Epochs: {args.epochs}, Steps: {args.steps_per_epoch}")
    print(f"Model: d_model={args.d_model}, layers={args.num_layers}, batch={args.batch_size}, seq_len={args.seq_len}")
    print()

    for seed in seeds:
        # Teacher-only baseline
        cfg = HDPCTrainingConfig(
            device=args.device, epochs=args.epochs, steps_per_epoch=args.steps_per_epoch,
            batch_size=args.batch_size, seq_len=args.seq_len, d_model=args.d_model,
            nhead=args.nhead, d_ff=args.d_ff, num_layers=args.num_layers,
            learning_rate=args.learning_rate, seed=seed,
            artifact_dir=artifact_dir / f"seed{seed}_teacher",
            data_dir=Path(args.data_dir),
        )
        print(f"--- Seed {seed}: teacher-only ---")
        t0 = time.time()
        teacher_result = run_teacher_only(cfg)
        print(f"  Teacher perplexity: {teacher_result['teacher_perplexity']:.2f} ({time.time()-t0:.0f}s)")

        for lam in lambdas:
            cfg = HDPCTrainingConfig(
                device=args.device, epochs=args.epochs, steps_per_epoch=args.steps_per_epoch,
                batch_size=args.batch_size, seq_len=args.seq_len, d_model=args.d_model,
                nhead=args.nhead, d_ff=args.d_ff, num_layers=args.num_layers,
                learning_rate=args.learning_rate, lambda_kd=lam, seed=seed,
                artifact_dir=artifact_dir / f"seed{seed}_lam{lam}",
                data_dir=Path(args.data_dir),
            )
            print(f"--- Seed {seed}, lambda_kd={lam}: HDPC student (detached crown) ---")
            t0 = time.time()
            result = run_homotopy_kd_training(cfg)
            entry = {
                "seed": seed, "lambda_kd": lam,
                "teacher_perplexity": teacher_result["teacher_perplexity"],
                "student_perplexity": result.diagnostics.student_perplexity,
                "perplexity_delta": result.diagnostics.student_perplexity - teacher_result["teacher_perplexity"],
                "teacher_only_perplexity": teacher_result["teacher_perplexity"],
                "student_parameters": result.student_parameters,
                "energy_profile_length": len(result.diagnostics.energy_profile),
                "update_sparsity_histogram": list(result.diagnostics.update_sparsity_histogram),
                "gradient_cosines": [
                    {"name": g.name, "cosine": g.cosine, "bp_norm": g.bp_norm, "pc_norm": g.pc_norm}
                    for g in result.diagnostics.gradients
                ],
                "elapsed": time.time() - t0,
            }
            all_results.append(entry)
            print(f"  Student perplexity: {entry['student_perplexity']:.2f}, delta: {entry['perplexity_delta']:+.2f} ({entry['elapsed']:.0f}s)")

            cosines = [g["cosine"] for g in entry["gradient_cosines"] if g["cosine"] is not None]
            if cosines:
                print(f"  Cosine: min={min(cosines):.4f} max={max(cosines):.4f} mean={sum(cosines)/len(cosines):.4f}")

    elapsed = time.time() - start
    summary = {
        "config": vars(args),
        "seeds": seeds, "lambdas": lambdas, "temperatures": list(temperatures),
        "total_elapsed": elapsed,
        "results": all_results,
    }
    summary_path = artifact_dir / "grid_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))

    print(f"\n=== Grid Complete ({elapsed:.0f}s total) ===")
    print(f"Runs: {len(all_results)}")
    for r in all_results:
        print(f"  seed={r['seed']} lam={r['lambda_kd']}: student={r['student_perplexity']:.2f} teacher={r['teacher_perplexity']:.2f} delta={r['perplexity_delta']:+.2f}")
    print(f"\nSummary: {summary_path}")


if __name__ == "__main__":
    main()
