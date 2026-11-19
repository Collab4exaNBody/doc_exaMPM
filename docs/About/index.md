---
icon: octicons/info-16
---

# About exaMPM

## Project summary

**exaMPM** (**exa**scale **M**aterial **P**oint **M**ethod) is a prototype of Material Point Method code built on
the onika and exaNBody HPC frameworks, in the [Collab4exaNBody](https://github.com/Collab4exaNBody) collaboration,
alongside exaStamp and exaDEM. It reproduces the 3D MPM solver of mpmxdem on exaNBody data structures, with
kernels that run with OpenMP and on GPUs.

## Contributors

<div class="grid cards" markdown>

-   :material-developer-board:{ .lg } __Development team__

    ---
    - [:octicons-mark-github-16:](https://github.com/rprat-pro) Raphaël Prat

-   :material-lightbulb-on:{ .lg } __mpmxdem__

    ---
    - [:octicons-mark-github-16:](https://github.com/richefeu) Vincent Richefeu and the mpmxdem contributors,
      authors of the reference MPM solver

</div>

## License

exaMPM links the mpmxdem library, which is distributed under the **GNU General Public License v3**: an exaMPM build
is therefore distributed under the GPL v3.

## Contact

Please open an [issue on GitHub](https://github.com/Collab4exaNBody/exaMPM/issues) to report a bug, ask a question
or suggest a feature.
