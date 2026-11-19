# **Simulation Starter Pack**

A minimal MPM deck defines, on top of the default configuration:

```yaml
global:                  # time step, number of steps, output periods
input_data:              # gravity, domain (= background grid), material points, obstacles, contact laws
init_epilog: mpm_init    # initialize the MPM nodes
compute_loop: mpm_compute_loop      # the MPM time loop
mpm_constitutive_model:  # the constitutive model of each group of material points
```

The time scheme (`mpm_modified_lagrangian`) and the outputs already have working defaults, but they are covered too.

The following pages build, block by block, the deck of the
[sphere impacting a structure](../../Tutorials/sphere_impacting_structure.md) tutorial:

- [**Global control**](1_global.md) — time step, end of the run, output periods through `global`
- [**Domain and background grid**](2_domain.md) — the MPM grid through `domain`
- [**Material points**](3_material_points.md) — gravity and material points through `parameters` and `set_mp_grid`
- [**Obstacles and contacts**](4_obstacles.md) — rigid bodies through `obstacles` and `contact_laws`
- [**Constitutive model**](5_constitutive_model.md) — the material behaviour through `mpm_constitutive_model`
- [**Numerical scheme**](6_numerical_scheme.md) — the time loop `mpm_compute_loop`
- [**Output data**](7_output.md) — log, ParaView files
- [**Working example**](8_example.md) — the complete deck
