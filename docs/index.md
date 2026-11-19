---
icon: lucide/mountain
---

# Welcome to the exaMPM online documentation! { style="color: var(--md-primary-fg-color);" }

<div style="background: color-mix(in srgb, var(--md-primary-fg-color) 8%, var(--md-default-bg-color)); border-radius: 12px; padding: 1.5rem 2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
  <div style="font-size: 1.4rem; font-weight: 700; line-height: 1.3;">
    <span style="color: var(--md-primary-fg-color);">exa</span>scale
    <span style="color: var(--md-primary-fg-color);">M</span>aterial
    <span style="color: var(--md-primary-fg-color);">P</span>oint
    <span style="color: var(--md-primary-fg-color);">M</span>ethod
  </div>
  <div style="margin-top: .5rem;">
    Large-deformation continuum mechanics (landslides, impacts, soil-structure interaction) with the
    Material Point Method, written as an application of the onika + exaNBody HPC frameworks.
  </div>
</div>

!!! warning "Prototype"

    exaMPM is a young prototype. It reproduces the 3D MPM solver of
    [mpmxdem](https://github.com/richefeu/mpmxdem) on exaNBody data structures, runs on CPU (OpenMP) and GPU (CUDA),
    and does not support MPI runs yet. Interfaces and YAML keys may still change.

<div class="grid cards" markdown>

-   :material-feature-search-outline:{ .lg .middle } __Features__

    ---

    - Material Point Method, modified Lagrangian scheme
    - Mohr-Coulomb and Hooke constitutive models
    - Rigid obstacles: spheres, planes, cylinders, biplanar slopes
    - Geometry from Blender (coordinate files, STL)
    - OpenMP and GPU (CUDA) kernels from one source

    [:octicons-arrow-right-24: All features](Overview/features.md)

-   :octicons-mark-github-16:{ .lg .middle } __Access to the code__

    ---

    - [:material-code-braces: GitHub repository](https://github.com/Collab4exaNBody/exaMPM) to access the code and fork it.
    - [:octicons-issue-opened-16: Open an issue](https://github.com/Collab4exaNBody/exaMPM/issues) to report bugs.
    - [:octicons-git-pull-request-16: Create a pull request](https://github.com/Collab4exaNBody/exaMPM/pulls) to propose developments.

-   :material-rocket-launch-outline:{ .lg .middle } __Get started__

    ---

    - [Build & Install](BuildInstall/index.md) onika, exaNBody, mpmxdem and exaMPM
    - Write a first input deck with the [Beginner Guide](Beginner/index.md)
    - Run the ported mpmxdem [Tutorials](Tutorials/index.md)

-   :material-scale-balance:{ .lg .middle } __Open Source, GPL v3__

    ---

    exaMPM links the mpmxdem library, distributed under the GNU GPL v3: an exaMPM build is therefore GPL v3.

    [:octicons-arrow-right-24: License](About/index.md#license)

-   :fontawesome-solid-people-carry:{ .lg .middle } __Team__

    ---

    exaMPM is developed within the [Collab4exaNBody](https://github.com/Collab4exaNBody) collaboration, with
    the physics of mpmxdem.

    [:octicons-arrow-right-24: Contributors](About/index.md#contributors)

-   :fontawesome-solid-contact-book:{ .lg .middle } __Contact__

    ---

    Use the [:octicons-issue-opened-16: GitHub issues](https://github.com/Collab4exaNBody/exaMPM/issues) for bugs,
    questions and feature requests.

    See the [About](About/index.md) page for contact and license information.

</div>
