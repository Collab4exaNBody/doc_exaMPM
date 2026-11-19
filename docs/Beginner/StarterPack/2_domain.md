---
icon: lucide/cuboid
---

# Domain and Background Grid

In exaMPM, the exaNBody **domain** is the MPM **background grid**: every exaNBody cell holds exactly one MPM node,
at its centre. The cell size is the MPM element size $h$.

To get nodes at $x = 0, h, 2h, \dots, n h$ (n elements), the domain has $n+1$ cells and starts at $-h/2$:

```yaml linenums="1"
input_data:
  # MPM grid of 100 x 40 x 55 elements of 0.06 m
  - domain:
      cell_size: 0.06
      grid_dims: [ 101 , 41 , 56 ]                                   # elements + 1
      bounds: [ [ -0.03 , -0.03 , -0.03 ] , [ 6.03 , 2.43 , 3.33 ] ]  # [-h/2, n h + h/2]
      periodic: [ false , false , false ]
      expandable: false
  - grid_flavor_mpm      # selects the exaMPM particle grid (must come before the MPs are created)
  - init_rcb_grid        # allocates the grid of cells
```

??? note "Parameters' description"

    | Property | Type | Description |
    | :--- | :---: | :--- |
    | `cell_size` | `float` | MPM element size $h$ |
    | `grid_dims` | `[int;3]` | number of cells = number of elements + 1 along each axis |
    | `bounds` | `AABB` | `[[xmin,ymin,zmin],[xmax,ymax,zmax]]`, from $-h/2$ to $n h + h/2$ |
    | `periodic` | `[bool;3]` | must be `false`: periodic MPM grids are not supported |
    | `expandable` | `bool` | must be `false`: the grid is fixed |

!!! info "mpmxdem equivalent"

    `new_set_grid nx ny nz h` in mpmxdem (n elements of size h along each axis) becomes `cell_size: h`,
    `grid_dims: [nx+1, ny+1, nz+1]` and `bounds: [[-h/2,-h/2,-h/2], [nx h + h/2, ny h + h/2, nz h + h/2]]`.

Material points must stay inside the grid: `p2g_mass` aborts the run when a material point leaves it, like mpmxdem.
See [Background Grid](../../User/Grid/index.md) for the shape functions and the nodal fields.
