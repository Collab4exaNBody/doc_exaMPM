---
icon: material/eye-outline
---

# Visualization

## ParaView

The output files are made for [ParaView](https://www.paraview.org/) (`sudo apt install paraview`):

1. *File > Open* `mpm_paraview/mpm_..pvtp` (the time series is grouped) and `mpm_paraview/obstacles_..vtk`;
2. color the material points by `type`, `vx`, or a component of `mp_stress`;
3. to see the material points as cubes, apply a *Glyph* filter (*Box*, scale `mp_vol`^(1/3)) or render the
   points as *Point Gaussian*.

## Blender

Blender cannot read VTK files directly. Two ways to render a simulation in Blender:

- export the data from ParaView (*File > Save Data* as PLY for the material points, *File > Export Scene* as glTF
  for the obstacles) and import it in Blender, then use *Geometry Nodes* (*Instance on Points*) to draw the points;
- or read the `.vtp` files with a Python script inside Blender (e.g. with `meshio`) and update the positions at each
  frame.

!!! warning "Axes"

    exaMPM's vertical axis is y, Blender's is z: swap y and z when importing.
