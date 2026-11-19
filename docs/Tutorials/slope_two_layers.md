---
icon: material/numeric-4-circle
---

# Slope with two layers

An elastic slope with a weaker Mohr-Coulomb layer, in a box of 5 planes. Port of mpmxdem's `slopeTwoLayers.sim`.

## Deck

```yaml linenums="1"
--8<-- "docs/files/slope_two_layers.msp"
```

## Key points

- `blender_set_mp_grid` creates the slope (group 0, Hooke elasticity), then `blender_modify_mp` moves the material
  points inside the objects of `modifyMP.txt` to group 1 (Mohr-Coulomb).
- mpmxdem changes the constitutive model of these material points but keeps their group. In exaMPM the model is
  chosen by group, so the layer is a new group, and the contact laws of group 0 are duplicated for group 1.
- The floor (`coordPlanes0.txt`) is obstacle group 0, with friction; the walls are group 1, without friction.

## Input files

`coordMP.txt`, `modifyMP.txt` and `coordPlanes0..4.txt`, read from the run directory. Synthetic files are provided in
`example/blender/` (the layer is a 6 × 6 × 1.5 m block crossing the slope).

## Validation

With the files of `example/blender/`, exaMPM and mpmxdem create the same 36864 material points (8880 of them are
moved to the layer); their positions after 2000 steps differ by less than $6 \times 10^{-6}$ m.
