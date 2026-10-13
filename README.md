# OpenRocket Insight

Repository scope, evidence, and reuse boundaries are also available in the
[NED3 resource manifest](.ned3/resource-manifest-v0.1.json).

OpenRocket Insight is a small, open Python companion for turning exported OpenRocket simulation results into transparent, comparable engineering summaries.

## Status

**Pre-alpha / educational prototype.** Version 0.1 will support a documented normalized summary CSV format. It does not yet parse `.ork` files, run OpenRocket, or certify flight safety.

## Why this exists

OpenRocket provides detailed design and trajectory simulations. Comparing several designs and explaining the engineering consequences of changed conditions can still require repetitive export, spreadsheet work, and manual plotting. This project aims to make that *post-processing* workflow reproducible without replacing OpenRocket's simulation engine.

## First workflow

1. Export or transcribe selected results into the [normalized summary CSV](docs/data-contract.md).
2. Validate the input:

   ```powershell
   python -m openrocket_insight validate examples/sample_runs.csv
   ```

3. Create a compact comparison report:

   ```powershell
   python -m openrocket_insight summarize examples/sample_runs.csv
   ```

## Safety and scientific status

All results are derived from user-provided simulation output. They are **screening-level simulation results**, not measured flight performance, a design approval, or launch-safety advice. Users remain responsible for applicable safety codes, supervision, range procedures, hardware verification, and independent engineering judgment.

## Development

Requires Python 3.10 or later.

```powershell
python -m pip install -e ".[dev]"
python -m pytest
```

See the [project plan](docs/project-plan.md), [data contract](docs/data-contract.md), and [contributing guide](CONTRIBUTING.md).
