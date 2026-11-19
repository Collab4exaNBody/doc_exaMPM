# **Mohr-Coulomb**

## **Description**

Elastic-perfectly plastic Mohr-Coulomb model with a non-associated flow rule, ported from mpmxdem's `MohrCoulomb`.

1. **Elastic predictor**, with the isotropic stiffness $D^e$ ($E$, $\nu$):
   $\sigma \leftarrow \sigma + D^e : \Delta\varepsilon$ (shear terms $G\,\Delta\varepsilon_{ij}$, as in mpmxdem, see [Hooke](hooke_elasticity.md)).
2. **Return mapping** in the principal stress space $\sigma_1 \ge \sigma_2 \ge \sigma_3$. For each pair of
   principal stresses $(a, b) \in \{(2,3), (1,3), (1,2)\}$, the yield function

    $$
    f_{ab} = \tfrac{1}{2}\left|\sigma_a - \sigma_b\right| + \tfrac{1}{2}(\sigma_a + \sigma_b)\sin\varphi - c\cos\varphi
    $$

    is brought back to 0 when positive, with the plastic potential $g$ of the same form using the dilatancy
    angle $\psi$ instead of $\varphi$. The correction is accumulated in `mp_plastic_stress`.
3. The stress is rotated back from the principal axes.

The three return-mapping cases are those of mpmxdem (yield functions of Ceccato's thesis), reproduced bitwise.

## **YAML syntax**

```yaml
mohr_coulomb:
  group: VALUE            # MP group, -1 for all
  young: VALUE            # Young modulus E (Pa)
  poisson: VALUE          # Poisson ratio nu
  friction_angle: VALUE   # phi (rad)
  cohesion: VALUE         # c (Pa)
  dilatancy_angle: VALUE  # psi (rad)
```

<div class="center-table" markdown>

| Parameter | Units | Default |
| :--- | :---: | ---: |
| `group` | — | `-1` |
| `young` | Pa | `200e6` |
| `poisson` | — | `0.2` |
| `friction_angle` | rad | `0.5` |
| `cohesion` | Pa | `0` |
| `dilatancy_angle` | rad | `0.3` |

</div>

## **Usage example**

!!! example "Cohesive soil block (sphere_impacting_structure)"

    ```yaml
    mpm_constitutive_model:
      - mohr_coulomb: { group: 0, young: 8.0e6, poisson: 0.42, friction_angle: 0.7, cohesion: 1e4, dilatancy_angle: 0.05 }
    ```

!!! warning "Angles in radians"

    mpmxdem's `.sim` files give the angles in radians: `friction_angle: 0.5` is 28.6°.
