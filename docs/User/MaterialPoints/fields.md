---
icon: material/table
---

# Material Point Fields

All the material points share one field set, `MPMFieldSet` (declared in `include/exaMPM/fields.h`):

<div class="center-table" markdown>

| Field | Type | Meaning | mpmxdem (`MaterialPoint`) |
| :--- | :---: | :--- | :--- |
| `rx`, `ry`, `rz` | `double` | position | `pos` |
| `vx`, `vy`, `vz` | `double` | velocity | `vel` |
| `fx`, `fy`, `fz` | `double` | contact force from the obstacles | `f` |
| `id` | `uint64` | identifier | index in `MP` |
| `type` | `uint8` | group | `groupNb` |
| `mp_mass` | `double` | mass | `mass` |
| `mp_vol` | `double` | volume | `vol` |
| `mp_density` | `double` | mass density | `density` |
| `mp_stress` | `Mat3d` | total stress $\sigma$ | `stress` |
| `mp_strain` | `Mat3d` | total strain $\varepsilon$ | `strain` |
| `mp_plastic_stress` | `Mat3d` | cumulated plastic stress correction | `plasticStress` |
| `mp_delta_strain` | `Mat3d` | strain increment of the step, used for the volume update | `deltaStrain` |
| `mp_prev_pos` | `Vec3d` | position at the previous step (friction) | `prev_pos` |
| `mp_contact_dn`, `_fn`, `_ft1`, `_ft2` | `Mat3d` | contact history with each obstacle | `Neighbor::dn, fn, ft` |

</div>

The contact history fields hold one value per obstacle: component `o` (`m11, m12, ..., m33`) is the history for
obstacle `o`, hence at most **9 obstacles**.

The ParaView output writes `id`, `type`, `vx`, `vy`, `vz`, `mp_mass`, `mp_vol`, `mp_stress` and `mp_strain` by
default (see [Outputs](../Outputs/index.md)).
