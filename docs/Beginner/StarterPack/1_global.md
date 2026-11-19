---
icon: lucide/sliders-horizontal
---

# Global Control

The `global` operator, run by the hook `init_prolog`, creates the slots shared by the whole simulation. Its default
values are defined in `data/config/config_globals.msp`:

```yaml linenums="1"
--8<-- "docs/files/config_globals.msp"
```

??? note "Parameters' description"

    | Parameter | Description | Type | Default |
    | :--- | :--- | :---: | ---: |
    | `dt` | time step (s) | `float` | `1.0e-5` |
    | `timestep` | current time step | `int` | `0` |
    | `physical_time` | current time (s) | `float` | `0.0` |
    | `simulation_end_iteration` | last time step: the loop runs the steps `0 .. simulation_end_iteration` | `int` | `0` |
    | `compute_loop_continue` | loop condition, set to false by the loop itself | `bool` | `true` |
    | `mpm_vtk_period` | ParaView output period (steps) | `int` | `1000` |
    | `mpm_prox_period` | period of the proximity check of the contacts (steps) | `int` | `100` |
    | `mpm_log_period` | log line period (steps) | `int` | `1000` |

A deck overrides only what it needs:

```yaml linenums="1"
global:
  dt: 1.0e-5
  simulation_end_iteration: 49999   # 50000 steps = 0.5 s
```

!!! warning "Time step"

    MPM with explicit time integration is conditionally stable: `dt` must stay below the time for an elastic wave
    to cross one grid element, $\Delta t < h / c$ with $c = \sqrt{E/\rho}$ (times a safety factor).
