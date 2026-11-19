# **Contact Law**

## **Description**

The force between a material point and an obstacle (mpmxdem: `MPMbox::boundaryConditions`) is computed by
`contact_forces` at each step, for every (material point, obstacle) pair in contact ($d_n < 0$), with the parameters
of the pair (MP group, obstacle group):

**Normal force** (incremental, with the previous distance $d_n^{old}$):

$$
f_n \leftarrow
\begin{cases}
-k_n\,e_n^2\,d_n & \text{unloading } (d_n > d_n^{old})\\
f_n - k_n\,(d_n - d_n^{old}) & \text{loading } (d_n < d_n^{old})\\
-k_n\,d_n & \text{otherwise}
\end{cases}
$$

**Friction** along each tangent $\mathbf{t}_k$, from the relative displacement over the step, with Coulomb's limit:

$$
f_{t,k} \leftarrow \operatorname{clamp}\left(f_{t,k} - k_t\left[(\mathbf{x}_p - \mathbf{x}_p^{prev}) - \Delta t\,\mathbf{v}_{obst}\right]\cdot\mathbf{t}_k,\; -\mu f_n,\; \mu f_n\right)
$$

The force $\mathbf{f} = f_n\mathbf{n} + f_{t,1}\mathbf{t}_1 + f_{t,2}\mathbf{t}_2$ is added to the material point
(`fx, fy, fz`, then to the nodes by `p2g_contact_forces`) and $-\mathbf{f}$ to the obstacle. The history
($d_n$, $f_n$, $f_{t,1}$, $f_{t,2}$) is stored per material point and obstacle, and reset when the contact is lost.

`check_proximity`, every `mpm_prox_period` steps, mimics mpmxdem's neighbor list rebuild: it resets $d_n$ and,
except for planes, $f_{t,2}$.

## **YAML syntax**

```yaml
- contact_laws:
    set: [ "<mu|kn|en2|kt> groupMP groupObst value", ... ]
```

<div class="center-table" markdown>

| Parameter | Description |
| :--- | :--- |
| `kn` | normal stiffness |
| `kt` | tangential stiffness |
| `en2` | unloading factor (square of the restitution coefficient) |
| `mu` | friction coefficient |

</div>

A (MP group, obstacle group) pair without a law has all parameters equal to 0: no contact force.

## **Usage example**

!!! example "Two obstacle groups"

    ```yaml
    - contact_laws:
        set: [ "mu 0 0 0.3", "kn 0 0 1.0e6", "en2 0 0 0.8", "kt 0 0 0.5e6",
               "mu 0 1 1.0", "kn 0 1 1.0e6", "en2 0 1 0.8", "kt 0 1 0.5e6" ]
    ```
