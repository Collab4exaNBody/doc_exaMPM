---
icon: material/graph-outline
---

# Simulation Graph

The default configuration `data/config/main-config.msp` defines the `simulation` block, a fixed sequence of
**hooks**, and the **MPM building blocks** that MPM decks plug into these hooks.

## Hooks

<div class="center-table" markdown>

| Hook | Default | Typical MPM deck |
| :--- | :--- | :--- |
| `hw_device_init` | `mpi_comm_world`, `init_cuda` | — |
| `init_prolog` | `global` | — |
| `input_data` | `nop` | `parameters`, `domain`, `grid_flavor_mpm`, `init_rcb_grid`, MP setters, `obstacles`, `contact_laws` |
| `init_epilog` | `nop` | `mpm_init` |
| `first_iteration` | `nop` | — |
| `compute_loop` | `nop` | `mpm_compute_loop` |
| `simulation_epilog` | `nop` | — |
| `hw_device_finalize` | `finalize_cuda` | — |

</div>

Extend the application by overriding these hooks (in a deck), never by editing `simulation`.

## MPM blocks

```mermaid
flowchart TD
  loop[mpm_compute_loop] --> begin[mpm_begin_iteration]
  loop --> ml[mpm_modified_lagrangian]
  loop --> next[next_time_step]
  loop --> stop[mpm_compute_loop_stop]
  begin --> vtk[mpm_vtk_if: mpm_vtk_output]
  begin --> log[mpm_log_if: mpm_print_log]
  begin --> prox[mpm_prox_if: check_proximity]
  log --> extra[mpm_log_extra]
  ml --> cm[mpm_constitutive_model]
```

<div class="center-table" markdown>

| Block | Content | Override to... |
| :--- | :--- | :--- |
| `mpm_init` | `init_nodes`, `update_mp_cells` | — |
| `mpm_compute_loop` | the time loop, until `simulation_end_iteration` | — |
| `mpm_begin_iteration` | triggers and runs the periodic outputs, log and proximity check | — |
| `mpm_modified_lagrangian` | one MPM time step ([details](../NumericalScheme/index.md)) | change the scheme |
| `mpm_constitutive_model` | `nop` | **required**: the constitutive model(s) |
| `mpm_vtk_output` | `mpm_write_paraview` | add `save_mp_pos`, change the output |
| `mpm_write_paraview` | ParaView files of the MPs and obstacles | change the fields written |
| `mpm_print_log` | `simulation_state`, `print_simulation_state`, `mpm_log_extra` | — |
| `mpm_log_extra` | `nop` | e.g. `print_obstacles` |

</div>

The periods are the global values `mpm_vtk_period`, `mpm_log_period` and `mpm_prox_period`; each output also runs at
the first step. The full file is shown in [Default YAML](default_yaml.md).
