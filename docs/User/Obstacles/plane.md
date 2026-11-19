# **Plane**

## **Description**

A rigid rectangle given by its 4 corners $\mathbf{p}_0 \dots \mathbf{p}_3$ (clockwise). Its tangents are
$\mathbf{t}_1 = \mathbf{p}_1 - \mathbf{p}_0$ and $\mathbf{t}_2 = \mathbf{p}_3 - \mathbf{p}_0$, its normal
$\mathbf{n} = -\mathbf{t}_1 \times \mathbf{t}_2$ (all three normalized). A material point touches the plane when its
projection lies inside the rectangle and

$$
d_n = (\mathbf{x}_p - \mathbf{p}_0)\cdot\mathbf{n} - \tfrac{1}{2}V_p^{1/3} < 0 .
$$

The plane acts on one side only: choose the order of the corners so that $\mathbf{n}$ points towards the material.

## **YAML syntax**

```yaml
- obstacles:
    obstacles: [ "Plane group x0 y0 z0 x1 y1 z1 x2 y2 z2 x3 y3 z3" ]
    legacy_plane: false
```

!!! warning "`legacy_plane`"

    mpmxdem calls `vec3r::normalized()`, which returns a normalized copy and leaves the vectors unchanged: its plane
    vectors are **not** normalized, so the plane only acts on a smaller rectangle. exaMPM normalizes them;
    `legacy_plane: true` reproduces mpmxdem (for comparisons only). It also applies to `Plane2`.

The tangential contact history of a plane is kept by `check_proximity` (mpmxdem behaviour).

## **Usage example**

!!! example "Horizontal floor at y = 0.5 m, normal +y"

    ```yaml
    obstacles: [ "Plane 1 0.0 0.5 0.0 8.0 0.5 0.0 8.0 0.5 4.0 0.0 0.5 4.0" ]
    ```
