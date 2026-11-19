---
icon: material/cube-outline
---

# Material Point Setters

These operators run once, in `input_data`, after `grid_flavor_mpm` and `init_rcb_grid`. They can be chained: each
`set_*` operator adds material points to those already created, and the other operators act on all the existing
material points.

## `set_mp_grid`

Fills a box with cubic material points of side `size`, at rest and stress free (mpmxdem: `set_MP_grid`).

```yaml
- set_mp_grid: { group: 0, density: 2000., lower: [ 3.5 , 0.5 , 0.3 ], upper: [ 3.9 , 1.0 , 2.7 ], size: 0.02 }
```

| Slot | Description | Default |
| :--- | :--- | ---: |
| `group` | material point group | `0` |
| `density` | mass density | required |
| `lower`, `upper` | corners of the box | required |
| `size` | side of the material points | required |

## `blender_set_mp_grid`

Fills a Blender object with material points of side `size`. The material point centres are on a lattice that starts
at the lower corner of the bounding box of the object + `size/2` (mpmxdem: `blender_set_MP_grid` and
`blender_set_MP_grid2`).

```yaml
- blender_set_mp_grid: { group: 0, density: 2000., file: coordMP.txt, size: 0.125 }            # prisms
- blender_set_mp_grid: { group: 0, density: 2000., file: slope.stl, format: stl, size: 0.125 }  # closed mesh
```

| Slot | Description | Default |
| :--- | :--- | ---: |
| `group` | material point group | `0` |
| `density` | mass density | required |
| `file` | geometry file (read from the run directory) | required |
| `format` | `coords`: `Object n x y z ...` file, each object being a prism along z; `stl`: ASCII STL closed mesh | `coords` |
| `size` | side of the material points | required |

The run aborts if the cell size is more than 3 times `size` (same check as mpmxdem). File formats:
[Blender files](blender_files.md).

## `blender_modify_mp`

Gives a new group and density to the material points inside the objects of a Blender coordinate file (mpmxdem:
`blender_modify_MP`). The mass is updated. As in mpmxdem, the material points of the lowest and highest z layers
are left unchanged.

```yaml
- blender_modify_mp: { group: 1, density: 2000., file: modifyMP.txt }
```

| Slot | Description |
| :--- | :--- |
| `group` | new group (selects the constitutive model and contact laws) |
| `density` | new mass density |
| `file` | `Object n x y z ...` Blender coordinate file |

!!! info "Difference with mpmxdem"

    mpmxdem's `blender_modify_MP` changes the constitutive model of the material points but keeps their group. In
    exaMPM the model is chosen by group, so the modified material points get a new group, and the deck must define
    the contact laws of this group too (see [slope_two_layers](../../Tutorials/slope_two_layers.md)).

## `move_mp`

Rotates all the material points around `origin` (rotation $R = R_z(\theta_z)\,R_y(\theta_y)$), then translates them
(mpmxdem: `move_MP`). The previous position is moved too.

```yaml
- move_mp: { origin: [ 2.87573593 , 0.5 , 1.25 ], translation: [ -0.4 , 0.4 , 0.0 ], theta_z: 45.0 }
```

| Slot | Description | Default |
| :--- | :--- | ---: |
| `origin` | centre of the rotations | `[0, 0, 0]` |
| `translation` | translation applied after the rotation | `[0, 0, 0]` |
| `theta_z` | rotation around z (degrees, negative is clockwise) | `0` |
| `theta_y` | rotation around y (degrees) | `0` |

## `set_k0_stress`

Geostatic initial stress (mpmxdem: `set_K0_stress`). With $d$ the depth along the gravity below the highest
material point:

$$
\sigma_{yy} = -d\,g\,\rho_0, \qquad \sigma_{xx} = K_0\,\sigma_{yy}, \qquad \sigma_{xy} = \sigma_{yx} = 0,
\qquad K_0 = \frac{\nu}{1-\nu}.
$$

The other components are left unchanged, as in mpmxdem.

```yaml
- set_k0_stress: { nu: 0.42, density: 2000. }
```

| Slot | Description |
| :--- | :--- |
| `gravity` | gravity (taken from `parameters` by default) |
| `nu` | Poisson ratio used for $K_0$ |
| `density` | density of the overburden $\rho_0$ |
