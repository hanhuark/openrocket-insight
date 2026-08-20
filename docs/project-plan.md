# Project plan: OpenRocket Insight v0.1

## Purpose

Build a transparent post-processing companion for OpenRocket users who want to compare simulated configurations without ad hoc spreadsheet work. The tool augments—not replaces—OpenRocket's simulation engine.

## Version-0 question

Given several exported simulation results, can a user obtain a reproducible comparison of performance quantities and a clear record of assumptions, units, and provenance?

## Scope

**In scope**

- Version-controlled normalized summary data in SI units
- CSV validation and compact command-line comparison
- Representative example cases, automated tests, and plain-language documentation
- A design brief for future OpenRocket-export adapters

**Out of scope for v0.1**

- Parsing `.ork` files or controlling OpenRocket
- A Java plug-in, automated flight-control logic, or hardware interfaces
- Claims that a design is safe, certifiable, or experimentally validated
- Replacing applicable launch codes, adult supervision, or range procedures

## Eight-week student pathway

| Week | Milestone | Evidence of completion |
| --- | --- | --- |
| 1 | Define three target user tasks and examine OpenRocket exports | Short requirements note and de-identified sample files |
| 2 | Confirm schema, units, and provenance fields | Reviewed data contract |
| 3 | Implement CSV validation | Tests for valid, missing, and malformed values |
| 4 | Add multi-run comparison summaries | Tested command-line output |
| 5 | Prototype plots or HTML report | Screenshot generated from example data |
| 6 | Build an export-adapter design from real files | Mapping table; no unsupported compatibility claim |
| 7 | Usability pass with clearly labeled feedback | Issue list and revised README |
| 8 | Release candidate | Tagged repository, test record, limitations note |

## Quality gates

- Every quantity has an explicit unit and simulation provenance.
- Raw OpenRocket exports and normalized derivatives remain linked by stable identifiers.
- Tests run from the repository root.
- Documentation distinguishes simulated, measured, and assumed quantities.
- Any user feedback is treated as formative product feedback; do not make generalizable human-subject research claims without University review.

## Future directions

1. An adapter for documented, versioned OpenRocket CSV exports.
2. Side-by-side configuration plots and a static HTML report.
3. A user-defined uncertainty study planner that records parameter ranges and aggregates exported runs.

The project will not automate simulation or parse `.ork` files until the compatibility and verification burden is justified by representative examples.
