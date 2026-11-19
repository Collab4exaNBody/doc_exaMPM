# **LeftBiplanar**

## **Description**

A fixed slope made of a horizontal plane, a circular arc and an inclined plane, extruded along z (mpmxdem:
`LeftBiplanar`):

- the horizontal plane goes from $\mathbf{x}_0$ towards $-x$ over a length $l_1$;
- an arc of radius $R$ and angle $\alpha$ (degrees) connects it to
- an inclined plane of length $l_2$, at the angle $\alpha$ from the horizontal, going up towards $-x$;
- all three extend from $z_0$ to $z_0 + $ `lengthz`.

A material point touches the arc first, else the horizontal plane, else the inclined plane. The arc contact normal
points towards the arc centre, with $\mathbf{t}_2 = \mathbf{e}_z$.

## **YAML syntax**

```yaml
- obstacles:
    obstacles: [ "LeftBiplanar group x0 y0 z0 lengthz l1 l2 R angle" ]
```

## **Usage example**

!!! example "45° slope ending on a 6 m flat floor (config_a1)"

    ```yaml
    obstacles: [ "LeftBiplanar 0 9 0.5 0 2.5 6 4 0.3 45" ]
    ```
