---
icon: lucide/blocks
---

# Building blocks

## Operators

An **operator** is a small C++ component that does one thing: create material points, transfer the mass to the
grid, compute contact forces, write a file... Each operator has typed **slots**: its inputs and outputs.

```console
$ exaMPM --help set_mp_grid
Operator    : set_mp_grid

Description : Fills a box with cubic material points of side 'size', at rest and stress free, like mpmxdem's
set_MP_grid command. Also sets the previous position to the current one (mpmxdem: MPMbox::init).
Slots       :
  density
    flow IN
    type double
    desc mass density (mpmxdem: mass_density)
  group
    flow IN
    type long
    desc MP group, stored in the 'type' field (mpmxdem: groupNb)
  lower
    flow IN
    type math::Vec3d
    desc lower corner of the box (x0, y0, z0)
  ...
```

Slots are connected **by name**: when `parameters` outputs `gravity`, every later operator with a `gravity`
input reads that value. You never wire operators by hand.

## Batches

A YAML list of operators is a **batch**: the operators run in order. A batch can be given a name and used as an
operator itself:

```yaml linenums="1"
mpm_init:          # a batch named mpm_init ...
  - init_nodes     # ... made of two operators
  - update_mp_cells

init_epilog: mpm_init   # ... used where the hook init_epilog is called
```

Batches can also loop (`loop: true` with a `condition` slot) or run conditionally (`condition:` with a boolean
slot). The MPM time loop `mpm_compute_loop` is such a batch.

## Setting slot values

A slot value is given in YAML under the operator name:

```yaml linenums="1"
- set_mp_grid: { group: 0, density: 2000., lower: [ 3.5, 0.5, 0.3 ], upper: [ 3.9, 1.0, 2.7 ], size: 0.02 }
```

Values not given keep the default of the operator (shown by `--help`). Slots marked `REQUIRED` must be set, or be
produced by an earlier operator.

!!! info "Units"

    exaMPM decks currently give **SI values without units** (m, kg, s, Pa). Angles of the constitutive models are
    in radians, rotation angles of `move_mp` and `LeftBiplanar` in degrees.
