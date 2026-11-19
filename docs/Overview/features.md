---
icon: material/feature-search
---

# **Main Features**

<div class="grid cards" markdown>

-   :simple-yaml:{ .lg .middle } __YAML-based input__

    ---

    The whole simulation — setup, time loop, outputs — is a graph of operators described in YAML (`.msp`
    files). A user deck only overrides the blocks it needs from the default configuration.

    [:octicons-arrow-right-24: YAML basics](../Beginner/GettingStarted/yaml_basics.md)

-   :fontawesome-solid-microchip:{ .lg .middle } __OpenMP x GPU__

    ---

    All per-material-point and per-node kernels are written once and run with OpenMP or on NVIDIA GPUs (CUDA),
    selected at run time with `--nogpu`. MPI is not supported yet.

    [:octicons-arrow-right-24: Running](../BuildInstall/running.md)

-   :lucide-grid-3x3:{ .lg .middle } __Background grid__

    ---

    Regular grid of hexahedral elements with trilinear shape functions (`RegularHexahedronLinear`), one MPM node
    per exaNBody cell.

    [:octicons-arrow-right-24: Background Grid](../User/Grid/index.md)

-   :lucide-atom:{ .lg .middle } __Material points__

    ---

    Cubic material points created in boxes, in Blender objects (prisms) or in closed STL meshes; moved, rotated,
    regrouped, and initialized with a geostatic K0 stress.

    [:octicons-arrow-right-24: Material Points](../User/MaterialPoints/index.md)

-   :material-function-variant:{ .lg .middle } __Constitutive models__

    ---

    - Mohr-Coulomb elasto-plasticity with return mapping in the principal stress space
    - Linear (Hooke) elasticity
    - One model per material point group

    [:octicons-arrow-right-24: Constitutive Models](../User/ConstitutiveModels/index.md)

-   :material-sphere:{ .lg .middle } __Rigid obstacles__

    ---

    Spheres (fixed, driven or free), planes, cylinders and biplanar slopes, also read from Blender files; up to
    9 obstacles. Penalty contact with friction per (material point group, obstacle group).

    [:octicons-arrow-right-24: Obstacles & Contacts](../User/Obstacles/index.md)

-   :material-chart-line:{ .lg .middle } __Outputs__

    ---

    ParaView files of the material points and obstacle surfaces, a log line with global quantities and
    throughput, obstacle trajectories, and mpmxdem-compatible position files.

    [:octicons-arrow-right-24: Outputs](../User/Outputs/index.md)

-   :material-check-decagram:{ .lg .middle } __Validated against mpmxdem__

    ---

    Each ported example is compared to mpmxdem: same material point count and positions within the output
    precision of mpmxdem.

    [:octicons-arrow-right-24: Tutorials](../Tutorials/index.md)

</div>
