---
icon: material/test-tube
---

# Tests

Every example deck is a test, registered in `example/CMakeLists.txt`:

```cmake
add_omp_mpi_test(empty empty.msp)          # 1 thread, 2 threads (_omp), mpirun -n 2 (_mpi)
add_omp_test(config_a1 config_a1.msp       # 1 thread, 2 threads (_omp); extra arguments are passed to exaMPM
             --set-global-simulation_end_iteration 99 --set-global-mpm_vtk_period 50)
```

MPM decks use `add_omp_test` (no MPI support yet) with a reduced number of steps, so that the whole suite runs in about a
minute. The Blender decks run in a copy of `example/blender/` in the build tree (their working
directory), so that their outputs stay out of the sources.

```bash
ctest --test-dir build-exampm --output-on-failure
ctest --test-dir build-exampm -R Example_ExaMPM_config_a1
```

## Continuous integration

`.github/workflows/install.yml` (Ubuntu 24.04, mpich), on every push and pull request:

1. builds onika and exaNBody from their `main` branches (cached by commit);
2. builds and installs mpmxdem (branch `add_cmake`, without the 2D part);
3. builds exaMPM, runs `ctest` and `cmake --install`;
4. checks the installed files and runs the installed `exaMPM` on `example/empty.msp`.

## Comparing with mpmxdem

The CMake target of mpmxdem gives the path of its `mpmbox3D` solver (`MPMXDEM_MPMBOX3D`). To compare a port:

- use `obstacles: { legacy_plane: true }` and `mpm_vtk_output: [ mpm_write_paraview, save_mp_pos ]`;
- run both codes for the same number of steps on one thread;
- compare `mpm_mppos/mpPos<n>.txt` with mpmxdem's `mpPos<n>.txt` (6 significant digits).
