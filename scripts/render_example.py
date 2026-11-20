# pvbatch render_example.py <run dir> <step> <out.png> <mp radius> <color: pressure|height|type> [azimuth elevation zoom pad]
import sys, glob, os
from paraview.simple import *

run, step, out, radius, color = sys.argv[1], int(sys.argv[2]), sys.argv[3], float(sys.argv[4]), sys.argv[5]
az = float(sys.argv[6]) if len(sys.argv) > 6 else 30.0
el = float(sys.argv[7]) if len(sys.argv) > 7 else 25.0
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
pad = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0  # camera framed on the MPs, bounds enlarged by pad (m)
pv = os.path.join(run, "mpm_paraview")

view = CreateView("RenderView")
view.ViewSize = [1600, 1000]
view.OrientationAxesVisibility = 0
view.Background = [1, 1, 1]
try:
    view.UseColorPaletteForBackground = 0
except Exception:
    pass

pvtp = os.path.join(pv, "mpm_%09d.pvtp" % step)
if not os.path.exists(pvtp):
    steps = sorted(int(f[4:13]) for f in os.listdir(pv) if f.endswith(".pvtp")) if os.path.isdir(pv) else []
    sys.exit("render_example: %s does not exist (run not finished, or wrong run dir?). Available steps: %s"
             % (pvtp, steps if steps else "none, no %s directory" % pv))
mps = XMLPartitionedPolydataReader(FileName=[pvtp])
mps.UpdatePipeline()
if mps.GetDataInformation().GetNumberOfPoints() == 0:
    sys.exit("render_example: %s holds no material point" % pvtp)
if color == "pressure":
    src = Calculator(Input=mps, ResultArrayName="p",
                     Function="-(mp_stress_0+mp_stress_4+mp_stress_8)/3")
    arr = "p"
elif color == "height":
    src = Calculator(Input=mps, ResultArrayName="height", Function="coordsY")
    arr = "height"
else:
    src, arr = mps, "type"
d = Show(src, view)
d.SetRepresentationType("Point Gaussian")
d.GaussianRadius = radius
d.ShaderPreset = "Sphere"
ColorBy(d, ("POINTS", arr))
lut = GetColorTransferFunction(arr)
if color == "pressure":
    lut.ApplyPreset("Viridis (matplotlib)", True)
    import numpy as np
    from vtk.numpy_interface import dataset_adapter as dsa
    data = servermanager.Fetch(MergeBlocks(Input=src))
    p = np.asarray(dsa.WrapDataObject(data).PointData["p"])
    lut.RescaleTransferFunction(0.0, float(np.percentile(p, 98)))  # a few contact MPs would squash the scale
    bar = GetScalarBar(lut, view)
    bar.Title = "mean stress (Pa)"
    bar.ComponentTitle = ""
    bar.TitleColor = bar.LabelColor = [0.1, 0.1, 0.1]
    bar.TitleFontSize = bar.LabelFontSize = 20
    d.SetScalarBarVisibility(view, True)
elif color == "height":
    lut.ApplyPreset("Viridis (matplotlib)", True)
    d.RescaleTransferFunctionToDataRange(False, True)
    bar = GetScalarBar(lut, view)
    bar.Title = "height (m)"
    bar.ComponentTitle = ""
    bar.TitleColor = bar.LabelColor = [0.1, 0.1, 0.1]
    bar.TitleFontSize = bar.LabelFontSize = 20
    d.SetScalarBarVisibility(view, True)
else:
    lut.InterpretValuesAsCategories = 1
    lut.Annotations = ["0", "group 0", "1", "group 1"]
    lut.IndexedColors = [0.80, 0.68, 0.48, 0.78, 0.20, 0.18]

obs = os.path.join(pv, "obstacles_%09d.vtk" % step)
if os.path.exists(obs):
    o = Show(LegacyVTKReader(FileNames=[obs]), view)
    ColorBy(o, None)
    o.DiffuseColor = o.AmbientColor = [0.62, 0.64, 0.68]
    o.Opacity = 0.35

b = list(src.GetDataInformation().GetBounds())
b = [b[i] - pad if i % 2 == 0 else b[i] + pad for i in range(6)]
view.ResetCamera(b)
cam = view.GetActiveCamera()
cam.SetViewUp(0, 1, 0)
cam.Azimuth(az)
cam.Elevation(el)
view.ResetCamera(b)
cam.Zoom(zoom)
SaveScreenshot(out, view, ImageResolution=[1600, 1000], TransparentBackground=0)
print("wrote", out)
