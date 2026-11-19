# **Sphere**

## **Description**

A rigid sphere of centre $\mathbf{x}_c$ and radius $R$. A material point of volume $V_p$ touches it when

$$
d_n = \|\mathbf{x}_p - \mathbf{x}_c\| - R - \tfrac{1}{2}V_p^{1/3} < 0 .
$$

The contact normal is $\mathbf{n} = (\mathbf{x}_p - \mathbf{x}_c)/\|\mathbf{x}_p - \mathbf{x}_c\|$, with the tangents
$\mathbf{t}_1 = (-n_y, n_x, 0)$ and $\mathbf{t}_2 = (0, n_z, -n_y)$ (as in mpmxdem; they are not normalized).

## **YAML syntax**

```yaml
- obstacles:
    obstacles: [ "Sphere group xc yc zc R driveMode ..." ]
```

| driveMode | Following values | Motion |
| :--- | :--- | :--- |
| `freeze` | — | fixed |
| `velocity` | `density vx vy vz` | imposed velocity (the density is read but unused) |
| `free` | `density vx vy vz vrot` | free rigid body: mass $\frac{4}{3}\pi R^3\rho$, inertia $\frac{2}{5} m R^2$, initial velocities |

A free sphere moves under gravity and the contact forces of the material points (velocity Verlet:
`obstacles_predict`, then `obstacles_correct` after `contact_forces`). As in mpmxdem, the gravity only contributes to
the first half velocity update.

## **Usage example**

!!! example "Free sphere thrown at 2 m/s (sphere_impacting_structure)"

    ```yaml
    obstacles: [ "Sphere 0 3.1 1.0 1.4 0.1 free 30000.0 2.0 0.1 0 0" ]
    ```
