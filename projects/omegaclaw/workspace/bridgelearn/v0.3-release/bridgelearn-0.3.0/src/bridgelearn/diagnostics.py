"""Tracing, calibration, and export utilities."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from .types import ControlCommand


@dataclass(frozen=True, slots=True)
class CalibrationReport:
    """One-step predicted-versus-realized variance calibration summary."""

    count: int
    blocks: int
    bias: list[float]
    mae: list[float]
    rmse: list[float]
    correlation: list[float]
    interval_coverage: list[float] | None
    nominal_coverage: float | None
    residual_quantiles: dict[str, list[float]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "count": self.count,
            "blocks": self.blocks,
            "bias": self.bias,
            "mae": self.mae,
            "rmse": self.rmse,
            "correlation": self.correlation,
            "interval_coverage": self.interval_coverage,
            "nominal_coverage": self.nominal_coverage,
            "residual_quantiles": self.residual_quantiles,
        }

    def to_json(self, path: str | Path) -> Path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
        return output


@dataclass(slots=True)
class BridgeTrace:
    """Append-only controller trace suitable for plots and regression tests."""

    records: list[dict[str, Any]] = field(default_factory=list)

    def append(
        self,
        command: ControlCommand,
        *,
        observed_variance: Any | None = None,
        observed_variance_std: Any | None = None,
        extra: Mapping[str, Any] | None = None,
    ) -> None:
        target = np.asarray(command.target_variance, dtype=np.float64)
        predicted = np.asarray(command.predicted_variance, dtype=np.float64)
        record: dict[str, Any] = {
            "channel": command.channel,
            "step": command.next_step,
            "requested_progress": command.requested_progress,
            "accepted_progress": command.accepted_progress,
            "feasible": command.feasible,
            "target_variance": target.tolist(),
            "predicted_variance": predicted.tolist(),
            "controls": _jsonable(command.controls),
            "diagnostics": _jsonable(command.diagnostics),
        }
        if observed_variance is not None:
            observed = np.asarray(observed_variance, dtype=np.float64).reshape(-1)
            if observed.size != target.size:
                raise ValueError("observed_variance block count does not match command.")
            record["observed_variance"] = observed.tolist()
        if observed_variance_std is not None:
            standard = np.asarray(observed_variance_std, dtype=np.float64).reshape(-1)
            if standard.size != target.size or np.any(standard < 0.0):
                raise ValueError("observed_variance_std must match blocks and be non-negative.")
            record["observed_variance_std"] = standard.tolist()
        if extra:
            record["extra"] = _jsonable(extra)
        self.records.append(record)

    def calibration_report(
        self,
        *,
        z_score: float = 1.6448536269514722,
        nominal_coverage: float = 0.90,
    ) -> CalibrationReport:
        usable = [record for record in self.records if "observed_variance" in record]
        if not usable:
            raise ValueError("no records contain observed_variance.")
        predicted = np.asarray([record["predicted_variance"] for record in usable])
        observed = np.asarray([record["observed_variance"] for record in usable])
        if predicted.shape != observed.shape:
            raise ValueError("predicted and observed calibration arrays differ in shape.")
        residual = observed - predicted
        bias = np.mean(residual, axis=0)
        mae = np.mean(np.abs(residual), axis=0)
        rmse = np.sqrt(np.mean(residual**2, axis=0))
        correlations = []
        for index in range(predicted.shape[1]):
            if np.std(predicted[:, index]) <= 1e-15 or np.std(observed[:, index]) <= 1e-15:
                correlations.append(float("nan"))
            else:
                correlations.append(float(np.corrcoef(predicted[:, index], observed[:, index])[0, 1]))
        std_records = [record.get("observed_variance_std") for record in usable]
        coverage: list[float] | None = None
        nominal: float | None = None
        if all(value is not None for value in std_records):
            standard = np.asarray(std_records, dtype=np.float64)
            coverage = np.mean(np.abs(residual) <= z_score * standard, axis=0).tolist()
            nominal = nominal_coverage
        quantiles = {
            "q05": np.quantile(residual, 0.05, axis=0).tolist(),
            "q50": np.quantile(residual, 0.50, axis=0).tolist(),
            "q95": np.quantile(residual, 0.95, axis=0).tolist(),
        }
        return CalibrationReport(
            count=int(predicted.shape[0]),
            blocks=int(predicted.shape[1]),
            bias=bias.tolist(),
            mae=mae.tolist(),
            rmse=rmse.tolist(),
            correlation=correlations,
            interval_coverage=coverage,
            nominal_coverage=nominal,
            residual_quantiles=quantiles,
        )

    def control_effort(self) -> dict[str, float]:
        compute = 0.0
        innovation = 0.0
        progress = 0.0
        for record in self.records:
            diagnostics = record.get("diagnostics", {})
            compute += float(diagnostics.get("compute_units", 1.0))
            progress += float(diagnostics.get("progress_delta", 0.0))
            predicted = np.asarray(record["predicted_variance"], dtype=np.float64)
            target = np.asarray(record["target_variance"], dtype=np.float64)
            innovation += float(np.sum(np.maximum(predicted - target, 0.0)))
        return {
            "compute_units": compute,
            "accepted_progress": progress,
            "progress_per_compute": progress / max(compute, 1e-12),
            "positive_variance_excess": innovation,
        }

    def to_json(self, path: str | Path) -> Path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(self.records, indent=2), encoding="utf-8")
        return output

    def to_csv(self, path: str | Path) -> Path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "channel",
            "step",
            "block",
            "requested_progress",
            "accepted_progress",
            "feasible",
            "target_variance",
            "predicted_variance",
            "observed_variance",
            "compute_units",
            "progress_per_compute",
        ]
        with output.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.records:
                target = record["target_variance"]
                predicted = record["predicted_variance"]
                observed = record.get("observed_variance", [None] * len(target))
                diagnostics = record.get("diagnostics", {})
                for index, target_value in enumerate(target):
                    writer.writerow(
                        {
                            "channel": record["channel"],
                            "step": record["step"],
                            "block": index,
                            "requested_progress": record["requested_progress"],
                            "accepted_progress": record["accepted_progress"],
                            "feasible": record["feasible"],
                            "target_variance": target_value,
                            "predicted_variance": predicted[index],
                            "observed_variance": observed[index],
                            "compute_units": diagnostics.get("compute_units"),
                            "progress_per_compute": diagnostics.get("progress_per_compute"),
                        }
                    )
        return output


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    return value
