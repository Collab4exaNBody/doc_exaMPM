# **Blender Obstacles**

`Plane2` and `Sphere2` are a [Plane](plane.md) and a [Sphere](sphere.md) whose geometry is read from a file
exported from Blender (mpmxdem: `blender_Obstacle`). The files are read from `blender_folder` (default: the run
directory); their formats are given in [Blender files](../MaterialPoints/blender_files.md).

## **YAML syntax**

```yaml
- obstacles:
    obstacles:
      - "Plane2 group file"                 # e.g. coordPlanes0.txt
      - "Sphere2 group file driveMode ..."  # e.g. coordSpheres.txt, same driveMode as Sphere
    blender_folder: "."
```

- `Plane2` vertices are rounded to 0.01, as in mpmxdem, and its vectors are normalized unless
  `legacy_plane: true`.
- Blender obstacles are placed after the other obstacles, whatever their order in the list.

## **Usage example**

!!! example "A box of 5 planes and a free sphere (sphere_on_slope)"

    ```yaml
    obstacles: [ "Plane2 0 coordPlanes0.txt", "Plane2 0 coordPlanes1.txt", "Plane2 0 coordPlanes2.txt",
                 "Plane2 0 coordPlanes3.txt", "Plane2 0 coordPlanes4.txt",
                 "Sphere2 1 coordSpheres.txt free 2700.0 0.0 0.0 0.0 0.0" ]
    ```
