# **Cylinder**

## **Description**

A fixed rigid cylinder of radius $R$ and length $L$, starting at $\mathbf{x}_0$ along the unit axis $\mathbf{a}$
(mpmxdem: `Cylinder`). A material point touches it when $0 \le (\mathbf{x}_p - \mathbf{x}_0)\cdot\mathbf{a} \le L$ and
its distance to the axis minus $R$ and $\frac{1}{2}V_p^{1/3}$ is negative.

!!! warning "mpmxdem behaviour"

    - The contact has **no friction**: mpmxdem leaves the tangents to zero.
    - `obstacles_delete_inside` removes the material points closer than $R + \frac{1}{2}V_p^{1/3}$ to the **axis line**,
      ignoring the length of the cylinder, like mpmxdem's `deleteIfInside`.

## **YAML syntax**

```yaml
input_data:
  - [...]                               # material points first
  - obstacles:
      obstacles: [ "Cylinder group x y z R length dx dy dz" ]
  - obstacles_delete_inside             # optional: remove the MPs inside the cylinder
```

The axis $(d_x, d_y, d_z)$ is normalized.

## **Usage example**

!!! example "Vertical pile of radius 0.4 m and length 4 m (piles_one)"

    ```yaml
    obstacles: [ "Cylinder 1 5.5 0 3.0 0.4 4 0 1 0" ]
    ```
