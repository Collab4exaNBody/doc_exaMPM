---
icon: octicons/history-16
---

# A little background

**exaMPM** is a Material Point Method (MPM) code. It stands for **exa**scale **M**aterial **P**oint **M**ethod.

## What is exaMPM?

The Material Point Method describes a continuum by a set of *material points* (MPs) that carry the mass, velocity,
stress and history variables of the material, and a *background grid* on which the equations of motion are solved
at each time step. Because the grid is reset at every step and the material points move freely through it, MPM
handles very large deformations, free surfaces and contacts without mesh distortion: landslides, granular flows,
impacts, penetration and soil-structure interaction.

`exaMPM` is built on the same software stack as `exaStamp` (molecular dynamics) and `exaDEM` (discrete elements):

- **onika** provides the runtime: operators, the YAML simulation graph, OpenMP and CUDA parallelism, plugins.
- **exaNBody** provides the particle grid (particles sorted in cells, stored as structures of arrays), per-cell
  values, domain decomposition and IO.
- **mpmxdem** ([richefeu/mpmxdem](https://github.com/richefeu/mpmxdem)) is the reference MPM solver whose 3D part
  (`mpmbox3D`) exaMPM reproduces: shape functions, transfer scheme, constitutive models, obstacles and contact
  law, and the input commands of its `.sim` files.

## Physics and numerical methods

At each time step, `exaMPM` runs mpmxdem's *modified Lagrangian* (MUSL-like) algorithm:

1. particle-to-grid transfer (P2G) of the mass, the internal forces $-V_p\,\sigma_p\,\nabla N_I$, the gravity and the
   contact forces;
2. integration of the nodal momentum;
3. grid-to-particle transfer (G2P) of the velocity, then re-projection of the momentum on the grid;
4. strain increment and stress update by the constitutive model of each material point;
5. update of the volume and of the material point positions.

The background grid is a regular grid of hexahedra with trilinear shape functions. Rigid obstacles interact with the
material points through a penalty contact law with friction. See [Numerical Scheme](../User/NumericalScheme/index.md)
for the details.

## How MPM is mapped on exaNBody

- Material points are exaNBody **particles**, with MPM fields (`mp_mass`, `mp_vol`, `mp_stress`, ...).
- The MPM **nodes** are stored as exaNBody **grid cell values**, one node at the centre of each cell: the cell
  size is the MPM element size.
- Each step of the algorithm is a small **operator**; the time loop is composed in YAML from these operators, so a
  user can reorder, replace or extend it without recompiling.
- All per-MP and per-node kernels are written once as functors that run with OpenMP or on the GPU.

## Status

`exaMPM` is a prototype. The five 3D examples of mpmxdem that can be ported are ported and validated against mpmxdem
(see [Tutorials](../Tutorials/index.md)). MPI runs are not supported yet: material points are not re-binned into
cells when they move, and ghost exchanges of nodal values are not wired.
