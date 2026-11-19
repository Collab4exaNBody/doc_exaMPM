---
icon: material/file-document-check-outline
---

# Working Example

The complete deck gathers all the blocks of the previous pages. It is `example/sphere_impacting_structure.msp`, the
port of mpmxdem's `sphereImpactingStructure.sim`: a rigid sphere hits a Mohr-Coulomb block lying on a plane.

```yaml linenums="1"
--8<-- "docs/files/sphere_impacting_structure.msp"
```

Run it with:

```bash linenums="1"
exaMPM sphere_impacting_structure.msp --omp_num_threads 8
# or a short test run
exaMPM sphere_impacting_structure.msp --set-global-simulation_end_iteration 199 --set-global-mpm_vtk_period 100
```

Then open `mpm_paraview/mpm_*.pvtp` and `mpm_paraview/obstacles_*.vtk` in ParaView. The
[tutorial](../../Tutorials/sphere_impacting_structure.md) discusses the results.
