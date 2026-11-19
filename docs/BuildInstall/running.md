---
icon: material/run
---

# **Running your simulation**

`exaMPM` takes one input deck (a `.msp` YAML file). It first loads the default configuration
`data/config/main-config.msp`, then the deck, which overrides it key by key.

```bash linenums="1"
${EXAMPM_INSTALL_DIR}/bin/exaMPM mydeck.msp      # installed
build-exampm/exaMPM mydeck.msp                   # from the build tree
```

Input files read by the deck (Blender geometry files, ...) are searched in the current directory, and outputs are
written there (`mpm_paraview/`, `ExaMPMOutputDir/`).

## **Threads and GPU**

=== "OpenMP"

    ```bash linenums="1"
    exaMPM mydeck.msp --omp_num_threads 8
    ```

=== "GPU"

    The example decks set `configuration: { nogpu: true }`. Override it to run the kernels on the GPU:

    ```bash linenums="1"
    exaMPM mydeck.msp --nogpu false --profiling-summary true
    ```

    The profiling summary printed at the end shows the GPU time of each operator in parentheses.

!!! warning "MPI"

    `mpirun -n N exaMPM` starts, but MPM decks must run on **one** MPI process for now: material points are not
    migrated between processes.

## **Command-line options**

Any configuration key can be set from the command line: `--a-b value` sets `configuration: { a: { b: value } }`.
Global values and slots of the graph are set with `--set-<block>-<key> value`:

```bash linenums="1"
# short run with more frequent outputs
exaMPM sphere_impacting_structure.msp --set-global-simulation_end_iteration 199 \
                                      --set-global-mpm_vtk_period 100
```

## **Getting help**

```bash linenums="1"
exaMPM --help plugins            # every available operator, by plugin
exaMPM --help set_mp_grid        # description and slots of one operator
```

!!! tip "WSL"

    On WSL2, `init_cuda` may print `ERR: GPUs don't support unified memory, cannot continue` and then go on: it is not
    a failure. Using all logical cores collapses performance when another process is running: use fewer threads.
