---
icon: material/content-save-outline
---

# Output Data

By default, `mpm_begin_iteration` writes, at the first step and then periodically:

<div class="center-table" markdown>

| Output | Period | Files |
| :--- | :--- | :--- |
| log line (screen and file) | `mpm_log_period` | `ExaMPMOutputDir/log.txt` |
| material points (ParaView) | `mpm_vtk_period` | `mpm_paraview/mpm_<step>.pvtp` |
| obstacle surfaces (ParaView) | `mpm_vtk_period` | `mpm_paraview/obstacles_<step>.vtk` |

</div>

The log line looks like:

```text
     Step     Time               MPs  Act. nodes   Contacts       Mass     Volume    avg. Ec    max |v|    avg. p  Throughput (MP/s)
        0  0.000000e+00         57000           0          0  9.120e+02  4.560e-01  0.000e+00  0.000e+00  0.000e+00  0.0000e+00
      100  1.000000e-03         57000        3280       2280  9.120e+02  4.560e-01  6.427e-07  9.810e-03  1.438e+02  4.0420e+06
      200  2.000000e-03         57000        3280       2280  9.120e+02  4.560e-01  2.231e-06  1.962e-02  5.369e+02  4.0033e+06
```

(`sphere_impacting_structure.msp` with `--set-global-mpm_log_period 100`, 4 threads.) The columns are: number of
material points, active nodes (mass above `tolmass`), active material point-obstacle contacts, total mass and volume,
average kinetic energy per material point, maximum velocity, mean pressure $-\mathrm{tr}(\sigma)/3$, and material
point updates per second since the previous line.

Extra outputs are added through hooks:

```yaml linenums="1"
# also print the position, velocity and force of the free obstacles at each log line
mpm_log_extra: print_obstacles

# also write the MP positions in mpmxdem's mpPos<n>.txt format
mpm_vtk_output: [ mpm_write_paraview, save_mp_pos ]
```

See [Outputs](../../User/Outputs/index.md) for the fields written and [Visualization](../../User/Outputs/visualization.md)
to open them in ParaView.
