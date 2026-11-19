---
icon: material/book-open-variant
---

# References

## Citing exaMPM

There is no reference paper for `exaMPM` yet. Please cite the software, together with exaNBody and mpmxdem:

```{ .bibtex .copy }
@software{exampm,
  title   = {exaMPM: a Material Point Method application on top of onika and exaNBody},
  year    = {2026},
  version = {0.1.0},
  url     = {https://github.com/Collab4exaNBody/exaMPM},
  license = {GPL-3.0}
}
```

## exaNBody

Thierry Carrard, Raphaël Prat, Guillaume Latu, Killian Babilotte, Paul Lafourcade, Lhassan Amarsid, and Laurent
Soulard. *ExaNBody: a HPC framework for N-body applications.* In Euro-Par 2023: Parallel Processing Workshops,
342–354. Springer Nature Switzerland, 2024.
[doi:10.1007/978-3-031-50684-0_27](https://link.springer.com/chapter/10.1007/978-3-031-50684-0_27)

## mpmxdem

The physics of exaMPM (shape functions, modified Lagrangian scheme, Mohr-Coulomb model, obstacles and contact law)
is ported from [mpmxdem](https://github.com/richefeu/mpmxdem), an MPM code that can also embed periodic DEM
simulations at the material points to build a numerically homogenized constitutive law.

## Related codes

- [exaStamp](https://github.com/Collab4exaNBody/exaStamp) — molecular dynamics on exaNBody
  ([documentation](https://collab4exanbody.github.io/doc_exaStamp/))
- [exaDEM](https://github.com/Collab4exaNBody/exaDEM) — discrete element method on exaNBody
- [onika](https://github.com/Collab4exaNBody/onika), [exaNBody](https://github.com/Collab4exaNBody/exaNBody) —
  the underlying frameworks
