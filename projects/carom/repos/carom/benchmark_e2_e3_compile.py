#!/usr/bin/env python3
"""Measure compile overhead and steady-state CAROM recurrence throughput."""
import argparse
import copy
import json
from pathlib import Path
import time

import torch
import torch.nn.functional as F

from model import Itinerant
from run_carom_e2_e3 import make_activity_noise


def synchronize(device):
    if device.type == "cuda":
        torch.cuda.synchronize(device)


def one_step(model, optimizer, C, X, Y, initial, activity_noise):
    optimizer.zero_grad(set_to_none=True)
    logits, activity = model(
        C, X, return_traj=True,
        initial_activity_noise=initial,
        activity_noise=activity_noise,
    )
    loss = F.cross_entropy(logits.flatten(0, 1), Y.flatten())
    loss.backward()
    optimizer.step()
    return float(loss.detach()), logits.detach(), activity.detach()


def maximum_tensor_error(left, right):
    return float((left - right).detach().abs().max())


def maximum_parameter_error(left_model, right_model, *, gradients=False):
    errors = []
    for left, right in zip(left_model.parameters(), right_model.parameters()):
        left_value = left.grad if gradients else left
        right_value = right.grad if gradients else right
        if left_value is None or right_value is None:
            if left_value is not None or right_value is not None:
                return float("inf")
            continue
        errors.append(maximum_tensor_error(left_value, right_value))
    return max(errors, default=0.0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--d", type=int, default=8)
    parser.add_argument("--K", type=int, default=4)
    parser.add_argument("--controller-steps", type=int, default=3)
    parser.add_argument("--timed-steps", type=int, default=2)
    parser.add_argument("--backend", default="inductor")
    parser.add_argument("--mode", default="reduce-overhead")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")

    torch.manual_seed(404)
    reference = Itinerant(
        d=args.d, K=args.K, steps=args.controller_steps, noise=0.02,
        mode_specific_fitness=True,
    ).to(device).train()
    candidate = copy.deepcopy(reference).train()
    candidate.enable_compiled_recurrence(
        backend=args.backend, mode=args.mode, fullgraph=True,
    )
    C = torch.randint(0, 7, (args.batch_size, 5), device=device)
    X = torch.randint(0, 9, (args.batch_size, 6), device=device)
    Y = torch.randint(0, 8, (args.batch_size, 6), device=device)
    noises = [
        make_activity_noise(reference, args.batch_size, device)
        for _ in range(args.timed_steps + 1)
    ]

    opt_reference = torch.optim.AdamW(reference.parameters(), lr=1e-3)
    opt_candidate = torch.optim.AdamW(candidate.parameters(), lr=1e-3)
    synchronize(device)
    start = time.perf_counter()
    compiled_first = one_step(candidate, opt_candidate, C, X, Y, *noises[0])
    synchronize(device)
    compile_first_step_s = time.perf_counter() - start
    reference_first = one_step(
        reference, opt_reference, C, X, Y, *noises[0]
    )
    equivalence = {
        "loss_abs_error": abs(compiled_first[0] - reference_first[0]),
        "logit_max_abs_error": maximum_tensor_error(
            compiled_first[1], reference_first[1]
        ),
        "activity_max_abs_error": maximum_tensor_error(
            compiled_first[2], reference_first[2]
        ),
        "gradient_max_abs_error": maximum_parameter_error(
            candidate, reference, gradients=True
        ),
        "parameter_max_abs_error_after_step": maximum_parameter_error(
            candidate, reference
        ),
    }

    compiled_times = []
    for index in range(args.timed_steps):
        synchronize(device)
        start = time.perf_counter()
        one_step(candidate, opt_candidate, C, X, Y, *noises[index + 1])
        synchronize(device)
        compiled_times.append(time.perf_counter() - start)

    eager_times = []
    for index in range(args.timed_steps):
        synchronize(device)
        start = time.perf_counter()
        one_step(reference, opt_reference, C, X, Y, *noises[index + 1])
        synchronize(device)
        eager_times.append(time.perf_counter() - start)

    eager_mean = sum(eager_times) / len(eager_times)
    compiled_mean = sum(compiled_times) / len(compiled_times)
    payload = {
        "device": str(device),
        "torch_version": torch.__version__,
        "backend": args.backend,
        "mode": args.mode,
        "batch_size": args.batch_size,
        "d": args.d,
        "K": args.K,
        "controller_steps": args.controller_steps,
        "compile_first_step_s": compile_first_step_s,
        "eager_step_s": eager_times,
        "compiled_step_s": compiled_times,
        "eager_mean_step_s": eager_mean,
        "compiled_mean_step_s": compiled_mean,
        "steady_state_speedup": eager_mean / compiled_mean,
        "equivalence": equivalence,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
