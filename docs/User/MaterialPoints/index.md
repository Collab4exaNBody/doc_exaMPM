---
icon: lucide/atom
---

# Material Points

Material points (MPs) are exaNBody particles of the exaMPM grid type (`grid_flavor_mpm`). Each one represents a
cube of material of side `size` and carries its mass, velocity, stress and history variables.

- [**Fields**](fields.md) — the per-material-point fields and their mpmxdem names
- [**Setters**](setters.md) — operators that create, move, regroup and initialize material points
- [**Blender files**](blender_files.md) — formats of the Blender coordinate and STL files

## Groups

The **group** of a material point (built-in field `type`, mpmxdem `groupNb`) selects:

- its constitutive model (slot `group` of `mohr_coulomb`, `hooke_elasticity`);
- its contact laws with each obstacle group (`contact_laws`).

Groups are integers from 0 to 255.
