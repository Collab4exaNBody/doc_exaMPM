---
icon: material/timer-sand
---

# Numerical Scheme

Two hooks of the default `simulation` block start the MPM computation:

```yaml linenums="1"
init_epilog: mpm_init            # allocates the MPM nodes, lists the cells holding MPs
compute_loop: mpm_compute_loop   # the time loop
```

`mpm_compute_loop` repeats, until `simulation_end_iteration`:

```yaml linenums="1"
mpm_compute_loop:
  loop: true
  condition: compute_loop_continue
  body:
    - mpm_begin_iteration       # outputs, log and proximity check at their periods
    - mpm_modified_lagrangian   # one MPM step
    - next_time_step            # timestep += 1, physical_time += dt
    - mpm_compute_loop_stop     # compute_loop_continue = timestep <= simulation_end_iteration
```

One step, `mpm_modified_lagrangian`, is mpmxdem's modified Lagrangian scheme split into operators:

```mermaid
flowchart TD
  A[obstacles_reset / reset_nodes / obstacles_predict] --> B[update_mass, p2g_mass]
  B --> C[p2g_internal_forces]
  C --> D[contact_forces, obstacles_correct, p2g_contact_forces]
  D --> E[grid_momentum_rate]
  E --> F[g2p_velocity, p2g_momentum]
  F --> G[mpm_constitutive_model]
  G --> H[update_volume, g2p_position]
```

You normally do not change it. See [Numerical Scheme](../../User/NumericalScheme/index.md) for the equations of each
operator.
