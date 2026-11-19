---
icon: fontawesome/solid/microchip
---

# GPU Kernels

Kernels are written once, as functors, and run with OpenMP on the CPU or with CUDA on the GPU. The choice is made at
run time (`--nogpu false` enables the GPU).

## Per-material-point kernels

`compute_mps(grid, mp_cells, func, pec, field::a, field::b, ...)` (in `include/exaMPM/mpm_gpu.h`) calls
`func(a, b, ...)` for every material point of the cells listed in `mp_cells`. Arguments are references for the fields
the kernel writes. `EXAMPM_GPU_PARTICLE_FUNCTOR(F)` declares the functor GPU compatible.

## Per-node kernels

Node loops use onika's `parallel_for` over the cells; `mpm_nodes(grid_cell_values)` gives raw pointers to the nodal
fields. `EXAMPM_GPU_FOR_FUNCTOR(F)` declares the functor GPU compatible:

```cpp linenums="1"
struct GridMomentumRate
{
  MPMNodes nodes;
  double dt;
  ONIKA_HOST_DEVICE_FUNC void operator()(size_t c) const
  {
    const size_t i = c * nodes.stride;
    for (int d = 0; d < 3; d++)
    {
      nodes.qdot[i + d] = nodes.fb[i + d] + nodes.f[i + d];
      nodes.q[i + d] += nodes.qdot[i + d] * dt;
    }
  }
};
EXAMPM_GPU_FOR_FUNCTOR(GridMomentumRate)

// in execute():
onika::parallel::parallel_for(grid_cell_values->number_of_cells(),
                              GridMomentumRate{mpm_nodes(*grid_cell_values), *dt}, parallel_execution_context());
```

## Rules inside a kernel

- The functor is trivially copyable: values and raw pointers only, and a `const` call operator marked
  `ONIKA_HOST_DEVICE_FUNC`.
- No virtual calls, STL containers, allocations, exceptions or logging.
- Scatter to the nodes (P2G) with `ONIKA_CU_ATOMIC_ADD`.
- Arrays read by a kernel (e.g. the obstacles, the contact laws) are copied to `onika::memory::CudaMMVector`
  (`PRIVATE` slots of the operator).
- Small linear algebra: `Vec3d`, `Mat3d` and their functions (`dot`, `cross`, `norm`, `transpose`, ...) from
  onika, and `include/exaMPM/mat9.h` (port of toofus `mat9`, with the symmetric eigen decomposition used by
  Mohr-Coulomb).

!!! tip "Checking that a kernel runs on the GPU"

    Run with `--nogpu false --profiling-summary true`: the GPU time of each operator is printed in parentheses.
