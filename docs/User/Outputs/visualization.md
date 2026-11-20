---
icon: material/eye-outline
---

# Visualization

## ParaView

The output files are made for [ParaView](https://www.paraview.org/) (`sudo apt install paraview`):

1. *File > Open* `mpm_paraview/mpm_..pvtp` (the time series is grouped) and `mpm_paraview/obstacles_..vtk`;
2. color the material points by `type`, `mp_mass`, `mp_vol`, or a component of `mp_stress` / `mp_strain` (the
   only fields written);
3. to see the material points as cubes, apply a *Glyph* filter (*Box*, scale `mp_vol`^(1/3)) or render the
   points as *Point Gaussian*.

## Example images

The pictures of the [tutorials](../../Tutorials/index.md) are rendered off screen with `pvbatch` (ParaView) and the
script `scripts/render_example.py` of this documentation repository:

```bash linenums="1"
pvbatch scripts/render_example.py <run dir> <step> <out.png> <MP radius> <color> [azimuth elevation zoom pad]
```

- `<run dir>` holds the `mpm_paraview/` folder of a run, `<step>` is a step with an output (a multiple of
  `mpm_vtk_period`). The script stops with the list of available steps when the file does not exist.
- `<MP radius>`: half the `size` of the material points of the deck.
- `<color>`: `pressure` (mean stress $-\operatorname{tr}\sigma/3$, scale clipped at the 98th percentile), `height` (y)
  or `type` (group 0 beige, group 1 red).
- The camera looks at the material points (bounds enlarged by `pad` metres), turned by `azimuth` and `elevation`
  degrees; obstacles are drawn semi-transparent.

The tutorial pictures come from longer runs than the tests, in the build tree:

```bash linenums="1"
cd build-exampm/example/piles_one
../exaMPM piles_one.msp --omp_num_threads 4 --set-global-simulation_end_iteration 29999 \
          --set-global-mpm_vtk_period 3000
pvbatch ${DOC_EXAMPM_DIR}/scripts/render_example.py . 27000 piles_one.png 0.07 height 35 25 1.0 0.3
```

<div class="center-table" markdown>

| Example | Steps run | Rendered step | MP radius | Color | Camera (az el zoom pad) |
| :--- | ---: | ---: | ---: | :--- | :--- |
| `sphere_impacting_structure` | 30000 | 24000 | 0.012 | `pressure` | 35 25 1.0 0.5 |
| `config_a1` | 10000 (full) | 9000 | 0.006 | `pressure` | 0 12 1.0 0.3 |
| `sphere_on_slope` | 30000 | 27000 | 0.07 | `height` | 35 25 1.0 0.3 |
| `slope_two_layers` | 30000 | 27000 | 0.07 | `type` | 35 25 1.0 0.3 |
| `piles_one` | 30000 | 27000 | 0.07 | `height` | 35 25 1.0 0.3 |

</div>

The images are stored as 1200 × 750 PNG in `example/<name>/<name>.png` (exaMPM) and `docs/images/examples/`
(this site).

## Blender

Blender cannot read VTK files directly. Two ways to render a simulation in Blender:

- export the data from ParaView (*File > Save Data* as PLY for the material points, *File > Export Scene* as glTF
  for the obstacles) and import it in Blender, then use *Geometry Nodes* (*Instance on Points*) to draw the points;
- or read the `.vtp` files with a Python script inside Blender (e.g. with `meshio`) and update the positions at each
  frame.

!!! warning "Axes"

    exaMPM's vertical axis is y, Blender's is z: swap y and z when importing.
