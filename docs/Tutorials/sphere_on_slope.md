---
icon: material/numeric-3-circle
---

# Sphere on a slope

A free sphere falls on a Mohr-Coulomb slope standing in a box of 5 planes. The slope, the planes and the sphere are
read from Blender files. Port of mpmxdem's `sphereOnSlope.sim`.

## Deck

```yaml linenums="1"
--8<-- "docs/files/sphere_on_slope.msp"
```

## Input files

The deck reads `coordMP.txt` (slope, see [coordinate files](../User/MaterialPoints/blender_files.md)),
`coordPlanes0..4.txt` (box) and `coordSpheres.txt` (sphere) from the run directory.

The Blender files of the original example are not distributed with mpmxdem. The exaMPM repository provides small
hand-written files in `example/blender/` (a 8 × 4 × 3 m slope, a box and a sphere of radius 0.4 m), used by the
test:

```bash linenums="1"
mkdir run && cp ${EXAMPM_SRC_DIR}/example/blender/* run/ && cd run
exaMPM ${EXAMPM_SRC_DIR}/example/sphere_on_slope.msp --set-global-simulation_end_iteration 1999
```

## Validation

With the files of `example/blender/` and `legacy_plane: true`, exaMPM and mpmxdem create the same 36864 material
points; after 2000 steps their positions differ by less than $6 \times 10^{-6}$ m and the sphere trajectories by
about $10^{-6}$ m.
