from pathlib import Path
import subprocess
import sys

import pytest

from openrocket_insight.summary import format_summary, read_runs


SAMPLE = Path(__file__).parents[1] / "examples" / "sample_runs.csv"


def test_reads_documented_contract() -> None:
    runs = read_runs(SAMPLE)
    assert len(runs) == 3
    assert runs[0].apogee_m == 224.1


def test_summary_reports_apogee_range() -> None:
    summary = format_summary(read_runs(SAMPLE))
    assert "Apogee range: 213.5 to 231.8 m" in summary


def test_missing_required_column_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "invalid.csv"
    source.write_text("run_id,configuration\n1,baseline\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Missing required column"):
        read_runs(source)


def test_module_cli_validates_example() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "openrocket_insight", "validate", str(SAMPLE)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Valid normalized summary CSV: 3 run(s)." in result.stdout
