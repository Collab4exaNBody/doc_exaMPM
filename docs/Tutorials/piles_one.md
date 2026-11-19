---
icon: material/numeric-5-circle
---

# Pile in a slope

A fixed vertical pile (Cylinder) through a Mohr-Coulomb slope read from an STL file, in a box of 5 planes. Port of
mpmxdem's `piles_one.sim`.

## Deck

```yaml linenums="1"
--8<-- "docs/files/piles_one.msp"
```

## Key points

- `blender_set_mp_grid` with `format: stl` fills a closed mesh with material points.
- `obstacles_delete_inside` removes the material points inside the pile. As in mpmxdem, it ignores the length of the
  cylinder (see [Cylinder](../User/Obstacles/cylinder.md)).
- The material/pile contact has no friction (mpmxdem's Cylinder has no tangents), whatever `mu`.

## Input files

`slope.stl` and `coordPlanes0..4.txt`, read from the run directory. Synthetic files are provided in
`example/blender/` (a box-shaped slope).

## Validation

With the files of `example/blender/`, exaMPM and mpmxdem create the same 40960 material points and both remove 880
of them inside the pile; positions after 2000 steps differ by less than $6 \times 10^{-6}$ m.
