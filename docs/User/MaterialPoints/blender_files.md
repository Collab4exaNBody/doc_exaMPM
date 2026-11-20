---
icon: simple/blender
---

# Blender Geometry Files

Some mpmxdem examples describe their geometry with files exported from [Blender](https://www.blender.org/). exaMPM
reads the same files. All the files are text files, read from the run directory (`blender_folder` for the
obstacles).

!!! warning "Axes"

    Blender's vertical axis is z, exaMPM's is y. All the readers swap y and z: a Blender vertex `x y z` is the
    exaMPM point `(x, z, y)`.

## Coordinate files (`coordMP.txt`, `modifyMP.txt`)

Used by `blender_set_mp_grid` (`format: coords`) and `blender_modify_mp`. One block per object: the word `Object`, the
number of vertices, then the vertices (Blender axes).

```text
Object 8
1 1 0.5
9 1 0.5
9 1 3.5
5 1 3.5
1 5 0.5
9 5 0.5
9 5 3.5
5 5 3.5
```

Each object must be a **prism along exaMPM's z axis** (Blender's y): exaMPM takes the distinct (x, y) vertices,
sorts them by angle around their mean to get the cross-section polygon, and fills the bounding box of the object
with the material points inside this polygon.

## STL files

Used by `blender_set_mp_grid` with `format: stl`: an **ASCII** STL file of a closed mesh (Blender: File > Export >
STL, *ASCII* checked). A point is inside the mesh when a ray along +x crosses an odd number of triangles.

```text
solid slope
 facet normal 0 0 0
  outer loop
   vertex 1 1 0.5
   vertex 1 1 3
   vertex 1 5 3
  endloop
 endfacet
 ...
endsolid slope
```

## Plane files (`coordPlanes<i>.txt`)

Used by the `Plane2` obstacle: a name, the number of vertices (4) and the 4 vertices of a rectangle (Blender axes).
The coordinates are rounded to 0.01, as in mpmxdem.

```text
floor 4
0.75 0.75 0.5
9.5 0.75 0.5
0.75 5.25 0.5
9.5 5.25 0.5
```

The vertices are, in order: the origin, the end of the first edge, the end of the second edge and the opposite
corner. The normal of the plane is $-\mathbf{t}_1 \times \mathbf{t}_2$ with $\mathbf{t}_1$, $\mathbf{t}_2$ the two edges.

## Sphere files (`coordSpheres.txt`)

Used by the `Sphere2` obstacle: a name, the radius and the centre (Blender axes).

```text
ball 0.4 6.5 3 4
```

!!! note "Generating the files"

    In mpmxdem, these files are produced by a Blender Python script (`getCoord`) that is not distributed with
    mpmxdem. The example folders of exaMPM (`example/<name>/`) contain small hand-written files used by the tests.
