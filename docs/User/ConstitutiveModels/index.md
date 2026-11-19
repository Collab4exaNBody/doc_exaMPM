---
icon: material/function-variant
---

# Constitutive Models

The constitutive models update the strain and the stress of the material points at step 4 of the
[time scheme](../NumericalScheme/index.md). They are listed in the hook `mpm_constitutive_model`, one operator per
group of material points:

```yaml linenums="1"
mpm_constitutive_model:
  - hooke_elasticity: { group: 0, young: 200.0e8, poisson: 0.42 }
  - mohr_coulomb: { group: 1, young: 70.0e6, poisson: 0.42, friction_angle: 0.5, cohesion: 50., dilatancy_angle: 0.05 }
```

`group: -1` (the default) applies the model to all the material points. A group with no model keeps its stress.

## Strain increment

All models start from the same strain increment, computed from the nodal velocities $\mathbf{v}_I = \mathbf{q}_I / m_I$
of the nodes heavier than `tolmass`:

$$
\Delta\varepsilon_p = \frac{\Delta t}{2} \sum_I \left(\mathbf{v}_I \otimes \nabla N_I(\mathbf{x}_p)
+ \nabla N_I(\mathbf{x}_p) \otimes \mathbf{v}_I\right),
\qquad \varepsilon_p \leftarrow \varepsilon_p + \Delta\varepsilon_p .
$$

<div class="center-table" markdown>

| Model | Operator | mpmxdem |
| :--- | :--- | :--- |
| [Mohr-Coulomb](mohr_coulomb.md) | `mohr_coulomb` | `MohrCoulomb` |
| [Linear elasticity](hooke_elasticity.md) | `hooke_elasticity` | `HookeElasticity` |

</div>

Both models run on the GPU.
