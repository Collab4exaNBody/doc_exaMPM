---
icon: material/baby-carriage
---

# Tutorials

The tutorials are the ports of the 3D examples of mpmxdem (`mpm/3D/Examples/*.sim`). Their decks are in the
`example/` directory of exaMPM, and short versions of all of them run in `ctest`.

<div class="center-table" markdown>

| Tutorial | mpmxdem example | Features |
| :--- | :--- | :--- |
| [Sphere impacting a structure](sphere_impacting_structure.md) | `sphereImpactingStructure.sim` | free sphere, plane, Mohr-Coulomb |
| [Block sliding on a slope](config_a1.md) | `config#A1.sim` | LeftBiplanar, `move_mp`, `set_k0_stress` |
| [Sphere on a slope](sphere_on_slope.md) | `sphereOnSlope.sim` | Blender slope, Plane2 box, Sphere2 |
| [Slope with two layers](slope_two_layers.md) | `slopeTwoLayers.sim` | `blender_modify_mp`, Hooke + Mohr-Coulomb |
| [Pile in a slope](piles_one.md) | `piles_one.sim` | STL slope, Cylinder, `obstacles_delete_inside` |

</div>

!!! note "Not ported"

    `slopeSoftLayer.sim` is not ported: its only obstacle line is invalid (mpmxdem ignores it) and the format of its
    `coordBoundaries.txt` file is not documented.

!!! info "Running the mpmxdem originals"

    The Blender examples use the `nstep` command, which mpmxdem 3D rejects at startup: they do not run as is in
    mpmxdem. exaMPM translates `nstep 300000` into `simulation_end_iteration: 299999`.
