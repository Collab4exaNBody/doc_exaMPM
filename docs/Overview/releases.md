---
icon: octicons/versions-16
---

# Code evolution

## **Versioning**

`exaMPM` has no release yet: use the `main` branch. The version printed at startup comes from `project(exaMPM
VERSION ...)` in `CMakeLists.txt` (currently `0.1.0`).

## **Compatibility with onika, exaNBody & mpmxdem**

<div align="center" markdown="1">
  | exaMPM | exaNBody | onika | mpmxdem |
  |:------:|:--------:|:-----:|:-------:|
  | main   | main     | main  | branch `add_cmake` |
</div>

The continuous integration of exaMPM builds onika and exaNBody from their `main` branches and mpmxdem from its
`add_cmake` branch, so these are the combinations known to work.

## **Development notes**

??? note "Current development (main)"

    **✨ Features**

    - Port of the five portable 3D examples of mpmxdem: `sphereImpactingStructure`, `config#A1`, `sphereOnSlope`,
      `slopeTwoLayers`, `piles_one`.
    - Obstacles `Sphere`, `Plane`, `Cylinder`, `LeftBiplanar` and the Blender obstacles `Plane2`, `Sphere2`.
    - Material point setup: `set_mp_grid`, `blender_set_mp_grid` (coordinate files and STL), `blender_modify_mp`,
      `move_mp`, `set_k0_stress`.
    - Constitutive models `mohr_coulomb` and `hooke_elasticity`.
    - GPU port of every per-MP and per-node kernel.
    - exaDEM-like log line (`simulation_state`, `print_simulation_state`) and ParaView outputs of the obstacles.

    **🧪 Differences with mpmxdem**

    - `Plane` and `Plane2` tangent vectors are normalized (`obstacles: { legacy_plane: true }` restores mpmxdem's
      behaviour).
    - The constitutive model is chosen by material point group (see
      [Constitutive Models](../User/ConstitutiveModels/index.md)).
