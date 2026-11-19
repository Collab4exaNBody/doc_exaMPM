---
icon: material/timer-sand
---

# Numerical Scheme

One time step is the batch `mpm_modified_lagrangian`, mpmxdem's `ModifiedLagrangian::advanceOneStep` split into
operators. Notations: $p$ material points, $I$ nodes, $N_I = N_I(\mathbf{x}_p)$.

<div class="center-table" markdown>

| # | Operator | Computation |
| :---: | :--- | :--- |
| | `update_mp_cells` | list of the cells holding material points |
| A | `obstacles_reset` | obstacle force and moment set to 0, acceleration set to gravity |
| | `zero_particle_force` | material point contact forces set to 0 |
| | `reset_nodes` | all nodal values set to 0 |
| B | `obstacles_predict` | obstacle motion: position and first half velocity update (free), $\mathbf{x} \mathrel{+}= \mathbf{v}\Delta t$ (imposed velocity) |
| 0 | `update_mass` | $m_p = \rho_p V_p$ |
| 1 | `p2g_mass` | $m_I = \sum_p N_I\, m_p$ (aborts if a material point is outside the grid) |
| 2 | `p2g_internal_forces` | $\mathbf{f}_I = \sum_p \left(-V_p\,\sigma_p \nabla N_I + m_p\,\mathbf{g}\,N_I\right)$ |
| 2b | `contact_forces` | material point-obstacle contact forces ([contact law](../Obstacles/contact_law.md)) |
| C | `obstacles_correct` | second half velocity update of the free obstacles |
| | `p2g_contact_forces` | $\mathbf{f}^b_I = \sum_p N_I\,\mathbf{f}_p$ |
| 3 | `grid_momentum_rate` | $\dot{\mathbf{q}}_I = \mathbf{f}^b_I + \mathbf{f}_I$, $\mathbf{q}_I \mathrel{+}= \dot{\mathbf{q}}_I\,\Delta t$ |
| 3a | `g2p_velocity` | $\mathbf{v}_p \mathrel{+}= \Delta t \sum_I N_I\, \dot{\mathbf{q}}_I / m_I$ |
| 3b | `p2g_momentum` | $\mathbf{q}_I = \sum_p N_I\, m_p \mathbf{v}_p$ (nodal momentum recomputed from the updated velocities) |
| 4 | `mpm_constitutive_model` | strain increment and stress ([constitutive models](../ConstitutiveModels/index.md)) |
| 4a | `update_volume` | volume and density from `mp_delta_strain` |
| 5 | `g2p_position` | $\mathbf{x}_p^{prev} = \mathbf{x}_p$, $\mathbf{x}_p \mathrel{+}= \Delta t \sum_I N_I\, \mathbf{q}_I / m_I$ |

</div>

Sums over $I$ only use the nodes heavier than `tolmass`.

!!! info "Reproduced mpmxdem quirks"

    The scheme is reproduced as is, including:

    - the volume update uses only $\Delta\varepsilon_{xx} + \Delta\varepsilon_{yy}$ (2D formula) of
      `mp_delta_strain`, which neither `mohr_coulomb` nor `hooke_elasticity` fills (as in mpmxdem): the volume and
      the density of the material points stay constant;
    - the gravity only enters the first half velocity update of the free obstacles.

!!! note "Reproducibility"

    `p2g_*` and `contact_forces` sum with atomic additions: two identical multi-threaded or GPU runs differ by
    round-off (about $10^{-3}$ relative on the obstacle force after the impact of the sphere example).
