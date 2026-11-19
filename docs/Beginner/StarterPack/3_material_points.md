---
icon: lucide/atom
---

# Material Points

## Gravity

The `parameters` operator sets the gravity and the mass tolerance used by the transfer operators:

```yaml linenums="1"
  - parameters:
      gravity: [ 0.0 , -9.81 , 0.0 ]   # y is the vertical axis in all examples
```

| Parameter | Description | Default |
| :--- | :--- | ---: |
| `gravity` | gravity acceleration (m/s²) | `[0, 0, 0]` |
| `tolmass` | nodes lighter than this are ignored in grid-to-particle transfers | `1e-6` |

## Creating material points

`set_mp_grid` fills a box with cubic material points of side `size`, at rest and stress free:

```yaml linenums="1"
  - set_mp_grid: { group: 0, density: 2000., lower: [ 3.5 , 0.5 , 0.3 ], upper: [ 3.9 , 1.0 , 2.7 ], size: 0.02 }
```

| Parameter | Description | Default |
| :--- | :--- | ---: |
| `group` | material point group, stored in the `type` field: selects the constitutive model and the contact laws | `0` |
| `density` | mass density (kg/m³) | required |
| `lower`, `upper` | corners of the box | required |
| `size` | side of the cubic material points: volume `size³`, mass `density × size³` | required |

Several setters can be chained to build more complex bodies: other boxes, Blender objects or STL meshes
(`blender_set_mp_grid`), rigid motions (`move_mp`), a new group in a region (`blender_modify_mp`), and an initial
geostatic stress (`set_k0_stress`). See [Material Points](../../User/MaterialPoints/setters.md).

!!! tip "Material point size"

    Use 2 to 3 material points per element and direction (here $h = 0.06$, `size` = 0.02: 27 MPs per element).
