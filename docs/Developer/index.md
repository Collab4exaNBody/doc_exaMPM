---
icon: material/code-braces
---

# Developer Guide

`exaMPM` is an application on top of onika and exaNBody, organized like exaStamp and exaDEM: plugins of small
operators, composed in YAML.

```text
exaMPM/
├── CMakeLists.txt          # find_package(onika, exaNBody, mpmxdem), MPM field set, plugins
├── include/exaMPM/         # shared headers: fields, shape function, kernels, obstacles, setup helpers
├── src/                    # one plugin per directory, one operator per file
│   ├── grid/               #   exaMPMGrid: grid flavor, MPM nodes
│   ├── io/                 #   exaMPMIO: parameters, material point setup, log, outputs
│   ├── numericalscheme/    #   exaMPMNumericalScheme: P2G / grid update / G2P steps
│   ├── constitutivemodel/  #   exaMPMConstitutiveModel: mohr_coulomb, hooke_elasticity
│   ├── driver/             #   exaMPMDriver: obstacles and their motion, obstacle outputs
│   └── interaction/        #   exaMPMInteraction: contact laws and forces
├── data/config/            # main-config.msp, config_globals.msp
└── example/                # example decks (tests) and synthetic Blender files
```

- [**Adding an operator**](new_operator.md) — file, slots, registration, YAML wiring
- [**GPU kernels**](gpu_kernels.md) — writing a kernel once for OpenMP and CUDA
- [**Coding rules**](coding_rules.md) — naming, logging, style
- [**Tests**](tests.md) — example decks as tests, CI
