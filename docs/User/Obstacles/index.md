---
icon: material/sphere
---

# Obstacles & Contacts

Rigid obstacles interact with the material points through a [penalty contact law](contact_law.md). They are created
by the `obstacles` operator, one definition line per obstacle, with the syntax of mpmxdem's `Obstacle` and
`blender_Obstacle` commands:

```yaml linenums="1"
- obstacles:
    obstacles:
      - "Sphere 0 3.1 1.0 1.4 0.1 free 30000.0 2.0 0.1 0 0"
      - "Plane 1 0.0 0.5 0.0 8.0 0.5 0.0 8.0 0.5 4.0 0.0 0.5 4.0"
    blender_folder: "."      # folder of the Plane2 / Sphere2 files
    legacy_plane: false      # true: reproduce mpmxdem's plane bug
```

The second word of each line is the obstacle **group**, used by the contact laws.

<div class="center-table" markdown>

| Type | Line | Motion | Page |
| :--- | :--- | :--- | :--- |
| `Sphere` | `Sphere group xc yc zc R driveMode ...` | fixed, imposed velocity or free | [Sphere](sphere.md) |
| `Plane` | `Plane group x0 y0 z0 x1 y1 z1 x2 y2 z2 x3 y3 z3` | fixed | [Plane](plane.md) |
| `Cylinder` | `Cylinder group x y z R length dx dy dz` | fixed | [Cylinder](cylinder.md) |
| `LeftBiplanar` | `LeftBiplanar group x0 y0 z0 lengthz l1 l2 R angle` | fixed | [LeftBiplanar](left_biplanar.md) |
| `Plane2` | `Plane2 group file` | fixed | [Blender obstacles](blender_obstacles.md) |
| `Sphere2` | `Sphere2 group file driveMode ...` | as `Sphere` | [Blender obstacles](blender_obstacles.md) |

</div>

At most **9 obstacles** can be defined. As in mpmxdem, the Blender obstacles (`Plane2`, `Sphere2`) are put after
the others: obstacle indices (in the logs and outputs) follow this order. The obstacles are listed at startup:

```text
obstacle 0: Sphere group=0 free mass=1.2566370614e+02
obstacle 1: Plane group=1 driven mass=0.0000000000e+00
```

## Operators

<div class="center-table" markdown>

| Operator | Role |
| :--- | :--- |
| `obstacles` | creates the obstacles (setup) |
| `obstacles_delete_inside` | removes the material points overlapping a Cylinder (setup) |
| `contact_laws` | contact parameters per (MP group, obstacle group) (setup) |
| `obstacles_reset`, `obstacles_predict`, `obstacles_correct` | obstacle motion, in each step |
| `contact_forces` | material point-obstacle contact forces, in each step |
| `check_proximity` | periodic reset of the contact history (`mpm_prox_period`) |
| `print_obstacles` | log of the free obstacles |
| `paraview_obstacles` | VTK surfaces of the obstacles |

</div>
