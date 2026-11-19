---
icon: simple/cmake
---

# **Installation with CMake**

The required minimal `CMake` version is `3.26`. The commands below use these environment variables (choose your own
paths):

<div class="center-table" markdown>

| Variable | Meaning |
|---|---|
| `ONIKA_SRC_DIR` / `ONIKA_INSTALL_DIR` | onika source tree / install prefix |
| `XNB_SRC_DIR` / `XNB_INSTALL_DIR` | exaNBody source tree / install prefix |
| `MPMXDEM_SRC_DIR` / `MPMXDEM_INSTALL_DIR` | mpmxdem source tree (branch `add_cmake`) / install prefix |
| `EXAMPM_SRC_DIR` / `EXAMPM_INSTALL_DIR` | exaMPM source tree / install prefix |

</div>

## **Requirements**

- CMake ≥ 3.26, a C++20 compiler with OpenMP, MPI and `yaml-cpp`;
- git and network access when configuring mpmxdem (it fetches [toofus](https://github.com/richefeu/toofus));
- optional: CUDA, to run the kernels on NVIDIA GPUs.

=== "Ubuntu / Debian"

    ```bash linenums="1"
    sudo apt install cmake g++ libyaml-cpp-dev mpich libmpich-dev
    ```

=== "yaml-cpp from sources"

    See the [exaStamp documentation](https://collab4exanbody.github.io/doc_exaStamp/BuildInstall/cmake_installation.html)
    for a `yaml-cpp` build with CMake, then add `-DCMAKE_PREFIX_PATH=${YAML_CPP_INSTALL_DIR}` to the onika command.

## **Onika**

`onika` is the component-based HPC platform under exaNBody: operators, YAML, OpenMP, CUDA/HIP.

=== "`Linux x GCC`"

    ```bash linenums="1"
    git clone https://github.com/Collab4exaNBody/onika.git ${ONIKA_SRC_DIR}
    cmake -S ${ONIKA_SRC_DIR} -B build-onika -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=${ONIKA_INSTALL_DIR} \
          -DONIKA_BUILD_CUDA=OFF
    cmake --build build-onika --target install -j10
    ```

=== "`Linux x GCC x CUDA`"

    ```bash linenums="1"
    git clone https://github.com/Collab4exaNBody/onika.git ${ONIKA_SRC_DIR}
    cmake -S ${ONIKA_SRC_DIR} -B build-onika -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=${ONIKA_INSTALL_DIR} \
          -DONIKA_BUILD_CUDA=ON \
          -DCMAKE_CUDA_COMPILER=$(which nvcc) \
          -DCMAKE_CUDA_ARCHITECTURES=${ARCH}
    cmake --build build-onika --target install -j10
    ```

    `${ARCH}` is the GPU architecture, e.g. `80` for an A100, `89` for an RTX 40xx.

## **exaNBody**

```bash linenums="1"
git clone https://github.com/Collab4exaNBody/exaNBody.git ${XNB_SRC_DIR}
source ${ONIKA_INSTALL_DIR}/bin/setup-env.sh
cmake -S ${XNB_SRC_DIR} -B build-exanb -DCMAKE_BUILD_TYPE=Release \
      -Donika_DIR=${ONIKA_INSTALL_DIR} \
      -DCMAKE_INSTALL_PREFIX=${XNB_INSTALL_DIR}
cmake --build build-exanb --target install -j10
```

## **mpmxdem**

exaMPM uses an installed mpmxdem (headers of toofus, `PBC3D` library, and the reference solver `mpmbox3D`). Only the
3D part is needed, so the 2D part (which needs OpenGL/GLUT) is disabled:

```bash linenums="1"
git clone --branch add_cmake https://github.com/richefeu/mpmxdem.git ${MPMXDEM_SRC_DIR}
cmake -S ${MPMXDEM_SRC_DIR} -B build-mpmxdem -DCMAKE_BUILD_TYPE=Release \
      -DMPMXDEM_BUILD_2D=OFF \
      -DCMAKE_INSTALL_PREFIX=${MPMXDEM_INSTALL_DIR}
cmake --build build-mpmxdem --target install -j10
```

!!! tip

    Add `-DFETCHCONTENT_SOURCE_DIR_TOOFUS=<path>` to use a local copy of toofus instead of downloading it.

## **exaMPM installation**

```bash linenums="1"
git clone https://github.com/Collab4exaNBody/exaMPM.git ${EXAMPM_SRC_DIR}
source ${XNB_INSTALL_DIR}/bin/setup-env.sh   # also sources onika's environment
cmake -S ${EXAMPM_SRC_DIR} -B build-exampm -DCMAKE_BUILD_TYPE=Release \
      -Donika_DIR=${ONIKA_INSTALL_DIR} \
      -DexaNBody_DIR=${XNB_INSTALL_DIR} \
      -Dmpmxdem_DIR=${MPMXDEM_INSTALL_DIR} \
      -DCMAKE_INSTALL_PREFIX=${EXAMPM_INSTALL_DIR}
cmake --build build-exampm -j10
ctest --test-dir build-exampm --output-on-failure
cmake --install build-exampm
```

`ctest` runs short versions of all the example decks (see [Tests](../Developer/tests.md)).

!!! note "GPU support"

    exaMPM has no GPU option of its own: it is GPU-enabled when onika is built with `ONIKA_BUILD_CUDA=ON`. Sourcing
    exaNBody's `setup-env.sh` before configuring sets the right compilers.

## **Installed layout**

```text
${EXAMPM_INSTALL_DIR}/
├── bin/
│   ├── exaMPM          # execution wrapper (sources setup-env.sh, then runs onika-exec)
│   └── setup-env.sh    # LD_LIBRARY_PATH, ONIKA_CONFIG_PATH, ONIKA_PLUGIN_PATH, ONIKA_DATA_PATH
├── lib/                # exaMPM plugins and exaNBody plugins rebuilt for the exaMPM grid
└── data/config/
    ├── main-config.msp     # default simulation graph, loaded by every run
    └── config_globals.msp  # default global values
```
