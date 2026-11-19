---
icon: material/sphere
---

# Obstacles and Contacts

Rigid obstacles are created by the `obstacles` operator from one line per obstacle, with the syntax of mpmxdem's
`Obstacle` command. The first word is the obstacle type, the second its **group**:

```yaml linenums="1"
  - obstacles:
      obstacles:
        # Sphere group xc yc zc R driveMode [density vx vy vz vrot]
        - "Sphere 0 3.1 1.0 1.4 0.1 free 30000.0 2.0 0.1 0 0"
        # Plane group x0 y0 z0  x1 y1 z1  x2 y2 z2  x3 y3 z3   (corners, clockwise)
        - "Plane 1 0.0 0.5 0.0 8.0 0.5 0.0 8.0 0.5 4.0 0.0 0.5 4.0"
```

Here a free sphere of radius 0.1 m and density 30000 kg/m³ is thrown at 2 m/s along x, and a horizontal plane at
y = 0.5 m holds the block.

## Contact laws

The contact between a material point and an obstacle is a penalty law with friction, whose parameters are given
per (material point group, obstacle group) with mpmxdem's `set` syntax `<param> groupMP groupObst value`:

```yaml linenums="1"
  - contact_laws:
      set: [ "mu 0 0 0.3", "kn 0 0 1.0e6", "en2 0 0 0.8", "kt 0 0 0.5e6",     # MPs of group 0 / sphere
             "mu 0 1 1.0", "kn 0 1 1.0e6", "en2 0 1 0.8", "kt 0 1 0.5e6" ]    # MPs of group 0 / plane
```

| Parameter | Description |
| :--- | :--- |
| `kn` | normal stiffness |
| `kt` | tangential stiffness |
| `en2` | unloading factor (square of the restitution coefficient): $f_n = -k_n\,e_n^2\,d_n$ when unloading |
| `mu` | friction coefficient |

!!! warning

    A missing (group, group) pair gives a zero law: the material points go through the obstacle.

See [Obstacles & Contacts](../../User/Obstacles/index.md) for all obstacle types and the contact law.
