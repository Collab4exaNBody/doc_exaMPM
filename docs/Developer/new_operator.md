---
icon: material/plus-box-outline
---

# Adding an operator

## 1. Look for an existing one

Before writing an operator, check that exaNBody or onika does not already provide it:

```bash
exaMPM --help plugins
grep -rn 'register_factory( *"<keyword>' ${XNB_SRC_DIR}/src ${ONIKA_SRC_DIR}/src
```

## 2. Create the file

One operator per file, named after the operator, in the plugin directory that fits (`src/<module>/<name>.cpp`).
Use `.cu` when the operator launches a kernel (`compute_mps`, `parallel_for`): it is compiled by `nvcc` when CUDA is
enabled and as C++ otherwise. A plugin directory with only `.cu` files also needs a `<module>_link_helper.cpp`.

## 3. Write it

A complete example, `update_mass` ($m_p = \rho_p V_p$):

```cpp linenums="1"
#include <exaMPM/mpm_gpu.h>
#include <exaMPM/mpm_operator.h>

namespace exaMPM
{
  struct UpdateMass   // the kernel: a POD functor, called for each material point
  {
    ONIKA_HOST_DEVICE_FUNC void operator()(double& mass, double density, double vol) const { mass = density * vol; }
  };
}  // namespace exaMPM
EXAMPM_GPU_PARTICLE_FUNCTOR(UpdateMass)   // may run on the GPU

namespace exaMPM
{
  template <class GridT, class = AssertGridHasFields<GridT, field::_mp_mass, field::_mp_density, field::_mp_vol>>
  struct UpdateMassNode : public OperatorNode
  {
    ADD_SLOT(GridT, grid, INPUT_OUTPUT, REQUIRED, DocString{"material points"});
    ADD_SLOT(CellList, mp_cells, INPUT, REQUIRED, DocString{"cells holding MPs"});

    inline std::string documentation() const override final { return "mpmxdem step 0: m_p = rho_p V_p."; }

    inline void execute() override final
    {
      compute_mps(*grid, *mp_cells, UpdateMass{}, parallel_execution_context(), field::mp_mass, field::mp_density,
                  field::mp_vol);
    }
  };

  template <class GridT> using UpdateMassTmpl = UpdateMassNode<GridT>;

  ONIKA_AUTORUN_INIT(update_mass)
  {
    OperatorNodeFactory::instance()->register_factory("update_mass", make_grid_variant_operator<UpdateMassTmpl>);
  }
}  // namespace exaMPM
```

- **Slots** are declared with `ADD_SLOT(type, name, flow, default, DocString{...})`. `flow` is `INPUT`, `OUTPUT`,
  `INPUT_OUTPUT` or `PRIVATE` (persistent state of the operator); `default` is a value, `REQUIRED` or `OPTIONAL`.
- **Registration**: `make_grid_variant_operator<Tmpl>` for an operator templated on the grid,
  `make_simple_operator<T>` otherwise.
- The new file is picked up by the plugin's `CMakeLists.txt` (`exampm_add_plugin`), after re-running CMake.

## 4. Wire it in YAML

Put the operator in a hook of `main-config.msp` (application default) or of a deck. Never edit the `simulation`
batch:

```yaml
+mpm_log_extra:
  - my_operator: { my_slot: 1.0 }
```

## 5. Test and document it

Check `exaMPM --help my_operator`, add an example folder `example/<name>/` (deck `<name>.msp` and the files it reads) and a test to `example/CMakeLists.txt` (see
[Tests](tests.md)), and document the operator in this site.
