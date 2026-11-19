---
icon: lucide/grid-3x3
---

# Background Grid

## Nodes on exaNBody cells

The MPM background grid is a regular grid of cubic elements of size $h$. exaMPM stores it in exaNBody's
**grid cell values** with one node per cell: node $(i, j, k)$ is the centre of cell $(i, j, k)$, at
$\mathbf{x}_I = (i h, j h, k h)$ when the domain starts at $-h/2$ (see [Domain](../../Beginner/StarterPack/2_domain.md)).

`init_nodes` (in `mpm_init`) adds the nodal fields:

<div class="center-table" markdown>

| Field | Components | Meaning (mpmxdem name) |
| :--- | :---: | :--- |
| `mpm_mass` | 1 | nodal mass $m_I$ (`mass`) |
| `mpm_q` | 3 | nodal momentum $\mathbf{q}_I$ (`q`) |
| `mpm_qdot` | 3 | nodal momentum rate $\dot{\mathbf{q}}_I$ (`qdot`) |
| `mpm_f` | 3 | internal and gravity forces $\mathbf{f}_I$ (`f`) |
| `mpm_fb` | 3 | contact (boundary) forces $\mathbf{f}^b_I$ (`fb`) |

</div>

All the nodal values are reset at each step (`reset_nodes`).

## Shape functions

exaMPM uses mpmxdem's `RegularHexahedronLinear`: the 8 nodes of the element that contains the material point, with
trilinear shape functions

$$
N_I(\mathbf{x}_p) = \prod_{d \in \{x,y,z\}} \left(1 - \frac{|x_{p,d} - x_{I,d}|}{h}\right),
\qquad
\frac{\partial N_I}{\partial x} = -\frac{\operatorname{sign}(x_p - x_I)}{h}
\left(1 - \frac{|y_p - y_I|}{h}\right)\left(1 - \frac{|z_p - z_I|}{h}\right).
$$

Nodes lighter than `tolmass` (slot of `parameters`, default `1e-6`) are ignored in the grid-to-particle transfers.

## Cells holding material points

Most cells of an MPM grid hold no material point. `update_mp_cells` lists the cells that hold some (slot `mp_cells`)
at the beginning of each step, and every per-material-point kernel loops over these cells only.

!!! info "Material points are not re-binned"

    Material points stay in the cell where they were created; their nodes are always found from their position.
    This is why MPI is not supported yet.

!!! tip "Performance"

    The per-node operators (`reset_nodes`, `grid_momentum_rate`) loop over all the nodes. On large, mostly empty
    grids (e.g. config#A1: 2.2 million nodes for 8740 material points) they dominate the run time.
