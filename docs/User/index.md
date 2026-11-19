---
icon: fontawesome/solid/chalkboard-teacher
---

# User guide to exaMPM

This is the reference section of the documentation: the default simulation graph, the background grid, the
material points and how to create them, the constitutive models, the obstacles and their contact law, the time
scheme and the outputs.

For a guided introduction, see the **Beginner Guide** tab.

- [**Simulation Graph**](SimulationGraph/index.md) — the default configuration, its hooks and MPM blocks
- [**Background Grid**](Grid/index.md) — MPM nodes on the exaNBody cells, shape functions
- [**Material Points**](MaterialPoints/index.md) — fields, setup operators and Blender geometry files
- [**Constitutive Models**](ConstitutiveModels/index.md) — Mohr-Coulomb and Hooke elasticity
- [**Obstacles & Contacts**](Obstacles/index.md) — rigid obstacles and the material point-obstacle contact law
- [**Numerical Scheme**](NumericalScheme/index.md) — the modified Lagrangian time step, operator by operator
- [**Outputs**](Outputs/index.md) — log, ParaView files, visualization
- [**Exhaustive Operator List**](Operators/index.md) — every exaMPM operator and its slots

!!! note

    The list of operators available in your build, with their slots, is printed by `exaMPM --help plugins` and
    `exaMPM --help <operator_name>`.
