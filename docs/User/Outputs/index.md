---
icon: material/content-save-outline
---

# Outputs

All the outputs are written by `mpm_begin_iteration`, before the step, at the first step and then periodically.

## Log line

`mpm_print_log` (every `mpm_log_period` steps) runs `simulation_state` (global reductions) and
`print_simulation_state`, which prints one line on screen and appends it to `ExaMPMOutputDir/log.txt`:

```text
     Step     Time               MPs  Act. nodes   Contacts       Mass     Volume    avg. Ec    max |v|    avg. p  Throughput (MP/s)
      100  1.000000e-03         57000        3280       2280  9.120e+02  4.560e-01  6.427e-07  9.810e-03  1.438e+02  4.0420e+06
```

<div class="center-table" markdown>

| Column | Meaning |
| :--- | :--- |
| `MPs` | number of material points |
| `Act. nodes` | nodes heavier than `tolmass` |
| `Contacts` | material point-obstacle pairs in contact |
| `Mass`, `Volume` | total mass and volume of the material points |
| `avg. Ec` | average kinetic energy per material point |
| `max \|v\|` | maximum material point velocity |
| `avg. p` | mean pressure $-\mathrm{tr}(\sigma)/3$ |
| `Throughput` | material point updates per second since the previous line |

</div>

| `print_simulation_state` slot | Description | Default |
| :--- | :--- | ---: |
| `save_file` | also write the lines to `log_file` | `true` |
| `log_file` | log file | `ExaMPMOutputDir/log.txt` |

The hook `mpm_log_extra` runs after the log line. `print_obstacles` prints the position, velocity and force of each
free obstacle:

```yaml
mpm_log_extra: print_obstacles
```

```text
obstacle 0 step      100 t 1.000000e-03 pos  3.102000000e+00  1.000097523e+00  1.400000000e+00 vel  2.000000000e+00  9.509500000e-02  0.000000000e+00 force  0.000000000e+00  0.000000000e+00  0.000000000e+00
```

## ParaView files

`mpm_vtk_output` (every `mpm_vtk_period` steps) runs `mpm_write_paraview` by default:

```yaml linenums="1"
mpm_write_paraview:
  - timestep_file: "mpm_paraview/mpm_%09d"
  - write_paraview:
      binary_mode: true
      write_ghost: false
      write_box: true
      fields: [ "id", "type", "vx", "vy", "vz", "mp_mass", "mp_vol", "mp_stress", "mp_strain" ]
  - paraview_obstacles: { obstacles_vtk_format: "mpm_paraview/obstacles_%09d.vtk" }
```

- `mpm_paraview/mpm_<step>.pvtp`: the material points (VTK XML polydata, compressed binary), with the listed fields,
  and the domain box;
- `mpm_paraview/obstacles_<step>.vtk`: the obstacle surfaces (legacy VTK, ASCII), meshed with quads (spheres,
  cylinder side and LeftBiplanar arc with `sphere_resolution` sectors, default 24). Cell data: obstacle index,
  group and velocity.

To write other fields, override the block, e.g. add `"mp_density"` or `"fx"` to `fields`.

## mpmxdem position files

`save_mp_pos` writes `<directory>/mpPos<n>.txt` (default `mpm_mppos/`), one line `x y z` per material point sorted
by id, with `n = timestep / mpm_vtk_period`, like mpmxdem's `save_MPpos`. Useful to compare with mpmxdem:

```yaml
mpm_vtk_output: [ mpm_write_paraview, save_mp_pos ]
```
