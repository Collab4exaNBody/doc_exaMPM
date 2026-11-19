# **Linear Elasticity (Hooke)**

## **Description**

Isotropic linear elasticity, ported from mpmxdem's `HookeElasticity`. The stress is computed from the **total**
strain:

$$
\sigma_{ii} = \frac{E}{(1+\nu)(1-2\nu)}\left[(1-\nu)\,\varepsilon_{ii} + \nu \sum_{j \ne i} \varepsilon_{jj}\right],
\qquad
\sigma_{ij} = G\,\varepsilon_{ij} \;\; (i \ne j), \quad G = \frac{E}{2(1+\nu)} .
$$

!!! info "Shear terms"

    As in mpmxdem, the shear stress is $G\,\varepsilon_{ij}$ with the tensor strain $\varepsilon_{ij}$ (half the
    engineering shear strain), i.e. half the shear stress of the usual Hooke law. The Mohr-Coulomb elastic predictor
    uses the same convention.

Because the stress is recomputed from the total strain, an initial stress (e.g. `set_k0_stress`) is overwritten at
the first step, as in mpmxdem.

## **YAML syntax**

```yaml
hooke_elasticity:
  group: VALUE     # MP group, -1 for all
  young: VALUE     # Young modulus E (Pa)
  poisson: VALUE   # Poisson ratio nu
```

`young` and `poisson` are required.

## **Usage example**

!!! example "Stiff elastic slope with a weak Mohr-Coulomb layer (slope_two_layers)"

    ```yaml
    mpm_constitutive_model:
      - hooke_elasticity: { group: 0, young: 200.0e8, poisson: 0.42 }
      - mohr_coulomb: { group: 1, young: 70.0e6, poisson: 0.42, friction_angle: 0.5, cohesion: 5.0e1, dilatancy_angle: 0.05 }
    ```
