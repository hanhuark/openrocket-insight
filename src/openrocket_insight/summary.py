"""Normalized simulation-summary CSV validation and comparison."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


REQUIRED_COLUMNS = (
    "run_id",
    "configuration",
    "apogee_m",
    "max_velocity_m_s",
    "max_acceleration_m_s2",
    "stability_calibers",
    "rail_exit_velocity_m_s",
)


@dataclass(frozen=True)
class SimulationRun:
    run_id: str
    configuration: str
    apogee_m: float
    max_velocity_m_s: float
    max_acceleration_m_s2: float
    stability_calibers: float
    rail_exit_velocity_m_s: float


def read_runs(path: str | Path) -> list[SimulationRun]:
    """Read the version-0 normalized summary contract.

    This intentionally does not claim to parse arbitrary OpenRocket exports.
    An export adapter will be introduced only after representative files are
    collected and tested.
    """
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        present = set(reader.fieldnames or [])
        missing = [column for column in REQUIRED_COLUMNS if column not in present]
        if missing:
            raise ValueError(f"Missing required column(s): {', '.join(missing)}")

        runs = []
        for line_number, row in enumerate(reader, start=2):
            try:
                runs.append(
                    SimulationRun(
                        run_id=_text(row, "run_id", line_number),
                        configuration=_text(row, "configuration", line_number),
                        apogee_m=_number(row, "apogee_m", line_number),
                        max_velocity_m_s=_number(row, "max_velocity_m_s", line_number),
                        max_acceleration_m_s2=_number(row, "max_acceleration_m_s2", line_number),
                        stability_calibers=_number(row, "stability_calibers", line_number),
                        rail_exit_velocity_m_s=_number(row, "rail_exit_velocity_m_s", line_number),
                    )
                )
            except KeyError as error:
                raise ValueError(f"Line {line_number}: missing value for {error.args[0]}") from error
    if not runs:
        raise ValueError("Input contains no simulation runs.")
    return runs


def format_summary(runs: list[SimulationRun]) -> str:
    """Return a compact, non-normative comparison summary."""
    apogees = [run.apogee_m for run in runs]
    return "\n".join(
        [
            f"Runs: {len(runs)}",
            f"Apogee range: {min(apogees):.1f} to {max(apogees):.1f} m",
            "Results are simulation-derived; verify inputs and do not use as flight approval.",
        ]
    )


def _text(row: dict[str, str | None], column: str, line_number: int) -> str:
    value = row.get(column)
    if value is None or not value.strip():
        raise ValueError(f"Line {line_number}: {column} must not be blank")
    return value.strip()


def _number(row: dict[str, str | None], column: str, line_number: int) -> float:
    value = _text(row, column, line_number)
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"Line {line_number}: {column} must be numeric, got {value!r}") from error
