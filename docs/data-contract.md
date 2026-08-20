# Version-0 data contract

The initial prototype accepts a **normalized simulation-summary CSV**, not arbitrary OpenRocket exports. This keeps the evidence path explicit while representative export files and an adapter are evaluated.

Each row represents one simulation run. Header names and SI units are fixed.

| Column | Unit | Meaning |
| --- | --- | --- |
| `run_id` | — | Unique, stable identifier |
| `configuration` | — | Human-readable design and condition label |
| `apogee_m` | m | Maximum altitude above launch point from the simulation |
| `max_velocity_m_s` | m/s | Maximum simulated speed |
| `max_acceleration_m_s2` | m/s² | Maximum simulated acceleration |
| `stability_calibers` | body diameters | Reported static stability margin; a reported simulation quantity, not an independent safety criterion |
| `rail_exit_velocity_m_s` | m/s | Simulated speed at rail exit |

## Provenance requirements

Retain the source `.ork` file, OpenRocket version, motor data source, launch conditions, output-export settings, and any manually transcribed values alongside each dataset. A future adapter must preserve these fields rather than silently assume them.
