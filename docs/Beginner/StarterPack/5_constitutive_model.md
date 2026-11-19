---
icon: material/function-variant
---

# Constitutive Model

The hook `mpm_constitutive_model` is called at each time step to compute the strain increment and update the stress
of the material points. It is a batch: list one model per material point group.

```yaml linenums="1"
mpm_constitutive_model:
  - mohr_coulomb: { group: 0, young: 8.0e6, poisson: 0.42, friction_angle: 0.7, cohesion: 1e4, dilatancy_angle: 0.05 }
```

| Parameter | Description | Default |
| :--- | :--- | ---: |
| `group` | material point group using this model, `-1` for all | `-1` |
| `young` | Young modulus (Pa) | `200e6` |
| `poisson` | Poisson ratio | `0.2` |
| `friction_angle` | friction angle (rad) | `0.5` |
| `cohesion` | cohesion (Pa) | `0` |
| `dilatancy_angle` | dilatancy angle (rad) | `0.3` |

Two models are available: `mohr_coulomb` and `hooke_elasticity` (linear elasticity). A two-material deck looks like:

```yaml linenums="1"
mpm_constitutive_model:
  - hooke_elasticity: { group: 0, young: 200.0e8, poisson: 0.42 }
  - mohr_coulomb: { group: 1, young: 70.0e6, poisson: 0.42, friction_angle: 0.5, cohesion: 50., dilatancy_angle: 0.05 }
```

See [Constitutive Models](../../User/ConstitutiveModels/index.md).
