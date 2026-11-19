---
icon: material/format-list-bulleted
---

# Exhaustive Operator List

Every operator of exaMPM, by plugin, with its slots (`exaMPM --help <operator>` prints the same information for
your build). Slots read from the global data graph (`dt`, `gravity`, `mp_cells`, `grid`, ...) are usually not set
in YAML. exaNBody and onika operators used by exaMPM (`domain`, `init_rcb_grid`, `write_paraview`, `global`,
`nop`, ...) are documented in the exaNBody documentation.

## exaMPMGrid

### `grid_flavor_mpm`

Selects the exaMPM grid type (MPMFieldSet). Must run before any other grid operator.

### `init_nodes`

Sizes grid_cell_values on the particle grid and adds the MPM nodal fields (mpm_mass, mpm_q, mpm_qdot, mpm_f, mpm_fb). The centre of each cell is one MPM node: the domain must start at -h/2, h being the cell size.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `grid_cell_values` | in/out | `GridCellValues` |  | MPM nodal values, one node per cell |

### `reset_nodes`

Sets every nodal value to 0 (discards the previous grid).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |

### `update_mp_cells`

Lists the cells that hold material points: the MP kernels only loop over these cells.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | out | `CellList` |  | cells holding MPs |

## exaMPMIO

### `blender_modify_mp`

Changes the group and density of the MPs inside the Blender objects (prisms along z), like mpmxdem's blender_modify_MP. As in mpmxdem, the MPs of the lowest and highest z layers are left unchanged. mpmxdem also changes the constitutive model: in exaMPM the model is chosen by group.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `group` | in | `long` | `required` | new MP group (selects the constitutive model and contact laws) |
| `density` | in | `double` | `required` | new mass density (the mass is updated) |
| `file` | in | `std::string` | `required` | 'Object n x y z ...' Blender coordinate file |

### `blender_set_mp_grid`

Fills a Blender object with cubic material points of side 'size' (MP centres on a lattice starting at the lower corner of the object bounding box + size/2), at rest and stress free.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `group` | in | `long` | `0` | MP group, stored in the 'type' field (mpmxdem: groupNb) |
| `density` | in | `double` | `required` | mass density |
| `file` | in | `std::string` | `required` | Blender geometry file |
| `format` | in | `std::string` | `"coords"` | 'coords': 'Object n x y z ...' file of the getCoord script (mpmxdem: blender_set_MP_grid),  each object being a prism along z; 'stl': ASCII STL closed mesh (blender_set_MP_grid2) |
| `size` | in | `double` | `required` | side of the cubic material points |

### `move_mp`

Rotates (Rz * Ry around 'origin') then translates all the MPs, like mpmxdem's move_MP command.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `origin` | in | `Vec3d` | `[0, 0, 0]` | centre of the rotations (x0, y0, z0) |
| `translation` | in | `Vec3d` | `[0, 0, 0]` | translation applied after the rotation (dx, dy, dz) |
| `theta_z` | in | `double` | `0.0` | rotation around the z axis (degrees, negative is clockwise) |
| `theta_y` | in | `double` | `0.0` | rotation around the y axis (degrees) |

### `parameters`

Global MPM parameters shared by the time scheme operators: gravity and mass tolerance.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `gravity` | in/out | `Vec3d` | `[0.0, 0.0, 0.0]` | gravity acceleration (mpmxdem: gravity) |
| `tolmass` | in/out | `double` | `1.e-6` | nodes lighter than this are ignored in grid-to-particle transfers (mpmxdem: tolmass) |

### `print_simulation_state`

Prints one log line per call, in the style of exaDEM's print_simulation_state: step, time, number of MPs, active nodes, active MP-obstacle contacts, total mass and volume, average kinetic energy per MP, maximum velocity, mean pressure and the throughput in MP updates per second (MPs x steps / wall-clock seconds since the previous line). The header is printed with the first line.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `timestep` | in | `long` | `required` | current time step |
| `physical_time` | in | `double` | `required` | current physical time |
| `mpm_simulation_state` | in | `MPMSimulationState` | `required` | reduced MPM quantities |
| `save_file` | in | `bool` | `true` | also append the log lines to log_file |
| `log_file` | in | `std::string` | `"ExaMPMOutputDir/log.txt"` | log file |

### `save_mp_pos`

Writes the MP positions in <directory>/mpPos<n>.txt, one line 'x y z' per MP sorted by id, like mpmxdem's MPMbox::save_MPpos (n = timestep / mpm_vtk_period). Single process only.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `timestep` | in | `long` | `required` | current time step |
| `mpm_vtk_period` | in | `long` | `1000` | output period, the file index is timestep / period |
| `directory` | in | `std::string` | `"mpm_mppos"` | output directory |

### `set_k0_stress`

Geostatic initial stress, like mpmxdem's set_K0_stress command: with d the depth along the gravity below the highest MP, stress.yy = -d g rho0, stress.xx = K0 stress.yy, stress.xy = stress.yx = 0 (the other components are unchanged, as in mpmxdem).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `gravity` | in | `Vec3d` | `required` | gravity acceleration |
| `nu` | in | `double` | `required` | Poisson ratio used for K0 = nu / (1 - nu) |
| `density` | in | `double` | `required` | density of the overburden (mpmxdem: rho0) |

### `set_mp_grid`

Fills a box with cubic material points of side 'size', at rest and stress free, like mpmxdem's set_MP_grid command. Also sets the previous position to the current one (mpmxdem: MPMbox::init).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `group` | in | `long` | `0` | MP group, stored in the 'type' field (mpmxdem: groupNb) |
| `density` | in | `double` | `required` | mass density (mpmxdem: mass_density) |
| `lower` | in | `Vec3d` | `required` | lower corner of the box (x0, y0, z0) |
| `upper` | in | `Vec3d` | `required` | upper corner of the box (x1, y1, z1) |
| `size` | in | `double` | `required` | side of the cubic material points |

### `simulation_state`

Global MPM quantities for the log (MPs, active nodes, contacts, mass, volume, kinetic energy, max |v|, mean pressure).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in | `GridCellValues` | `optional` | MPM nodal values (active nodes count) |
| `tolmass` | in | `double` | `1.e-6` | a node is active if its mass is above tolmass |
| `mpm_obstacles` | in | `MPMObstacles` | `optional` | rigid obstacles (contact count) |
| `mpm_simulation_state` | out | `MPMSimulationState` |  | reduced MPM quantities |

## exaMPMConstitutiveModel

### `hooke_elasticity`

mpmxdem step 4 with the HookeElasticity model: strain increment from q_I/m_I, then linear elastic stress from the total strain.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in | `GridCellValues` | `required` | MPM nodes |
| `dt` | in | `double` | `required` | time step |
| `tolmass` | in | `double` | `required` | lighter nodes are ignored |
| `group` | in | `long` | `-1` | MP group using this model, -1 for all |
| `young` | in | `double` | `required` | Young modulus |
| `poisson` | in | `double` | `required` | Poisson ratio |

### `mohr_coulomb`

mpmxdem step 4 with the MohrCoulomb model: strain increment from q_I/m_I, elastic predictor and return mapping in the principal stress space.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in | `GridCellValues` | `required` | MPM nodes |
| `dt` | in | `double` | `required` | time step |
| `tolmass` | in | `double` | `required` | lighter nodes are ignored |
| `group` | in | `long` | `-1` | MP group using this model, -1 for all |
| `young` | in | `double` | `200.0e6` | Young modulus |
| `poisson` | in | `double` | `0.2` | Poisson ratio |
| `friction_angle` | in | `double` | `0.5` | friction angle (rad) |
| `cohesion` | in | `double` | `0.0` | cohesion |
| `dilatancy_angle` | in | `double` | `0.3` | dilatancy angle (rad) |

## exaMPMNumericalScheme

### `g2p_position`

mpmxdem step 5: x_p += dt N_I q_I / m_I (previous position kept in mp_prev_pos). MPs are not re-binned into cells: their nodes are found from their position.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in | `GridCellValues` | `required` | MPM nodes |
| `dt` | in | `double` | `required` | time step |
| `tolmass` | in | `double` | `required` | lighter nodes are ignored |

### `g2p_velocity`

mpmxdem step 3a: v_p += dt N_I qdot_I / m_I.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in | `GridCellValues` | `required` | MPM nodes |
| `dt` | in | `double` | `required` | time step |
| `tolmass` | in | `double` | `required` | lighter nodes are ignored |

### `grid_momentum_rate`

mpmxdem step 3: qdot_I = fb_I + f_I, q_I += qdot_I dt.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |
| `dt` | in | `double` | `required` | time step |

### `p2g_contact_forces`

mpmxdem: contact forces to the nodes, fb_I += N_I f_p.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |

### `p2g_internal_forces`

mpmxdem step 2: f_I += -V_p sigma_p gradN_I + m_p g N_I.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |
| `gravity` | in | `Vec3d` | `required` | gravity |

### `p2g_mass`

mpmxdem step 1: m_I += N_I m_p. Aborts if an MP is outside the grid, like mpmxdem.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |

### `p2g_momentum`

mpmxdem step 3b: q_I += N_I m_p v_p.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `grid_cell_values` | in/out | `GridCellValues` | `required` | MPM nodes |

### `update_mass`

mpmxdem step 0: m_p = rho_p V_p.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |

### `update_volume`

mpmxdem step 4a: volume and density from mp_delta_strain (xx + yy). Mohr-Coulomb does not set it.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |

## exaMPMDriver

### `obstacles`

Creates the rigid obstacles from mpmxdem-style definition lines. As in mpmxdem, the Blender obstacles (Plane2, Sphere2) come after the others. A Cylinder removes the MPs it overlaps, see obstacles_delete_inside.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `obstacles` | in | `std::vector<std::string>` | `[]` | one obstacle per line, as mpmxdem's 'Obstacle' and 'blender_Obstacle' commands:  'Sphere group xc yc zc R driveMode ...', 'Plane group x0 y0 z0 x1 y1 z1 x2 y2 z2 x3 y3 z3',  'Cylinder group x y z R length dx dy dz', 'LeftBiplanar group x0 y0 z0 lengthz l1 l2 R angle',  'Plane2 group file' and 'Sphere2 group file driveMode ...' |
| `blender_folder` | in | `std::string` | `"."` | folder of the Plane2 / Sphere2 files (mpmxdem: result_folder) |
| `legacy_plane` | in | `bool` | `false` | reproduce mpmxdem's Plane / Plane2 bug (tangents and normal not normalized, plane acting on a  smaller rectangle). Only for comparisons with mpmxdem |
| `mpm_obstacles` | out | `MPMObstacles` |  | rigid obstacles |

### `obstacles_correct`

mpmxdem ModifiedLagrangian, part C: second half velocity update of the free obstacles from the contact force and moment computed by contact_forces.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in/out | `MPMObstacles` | `required` | rigid obstacles |
| `dt` | in | `double` | `required` | time step |

### `obstacles_delete_inside`

Removes the MPs overlapping a Cylinder, like mpmxdem's Cylinder::deleteIfInside (run after the MPs and the obstacles are created). As in mpmxdem the test ignores the cylinder length: the MPs closer than R + size/2 to the axis line are removed.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in | `MPMObstacles` | `required` | rigid obstacles |

### `obstacles_predict`

mpmxdem ModifiedLagrangian, part B: moves the obstacles according to their driving mode (velocity Verlet position update and first half velocity update for free obstacles, imposed velocity otherwise).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in/out | `MPMObstacles` | `required` | rigid obstacles |
| `dt` | in | `double` | `required` | time step |

### `obstacles_reset`

mpmxdem ModifiedLagrangian, part A: deletes the resultant force and moment of the obstacles and sets their acceleration to gravity.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in/out | `MPMObstacles` | `required` | rigid obstacles |
| `gravity` | in | `Vec3d` | `required` | gravity acceleration |

### `paraview_obstacles`

Writes the obstacle surfaces in a legacy VTK polydata file (one file per call), meshed with quads (spheres, cylinder side, LeftBiplanar arc) or one quad per plane. Cell data: obstacle index, group and velocity.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in | `MPMObstacles` | `required` | rigid obstacles |
| `timestep` | in | `long` | `required` | current time step |
| `obstacles_vtk_format` | in | `std::string` | `"mpm_paraview/obstacles_%09d.vtk"` | output file name, formatted with the time step |
| `sphere_resolution` | in | `long` | `24` | number of sectors used to mesh the curved surfaces |

### `print_obstacles`

Prints the position, velocity and contact force of the free obstacles.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mpm_obstacles` | in | `MPMObstacles` | `required` | rigid obstacles |
| `timestep` | in | `long` | `required` | current time step |
| `physical_time` | in | `double` | `required` | current physical time |

## exaMPMInteraction

### `check_proximity`

mpmxdem MPMbox::checkProximity: rebuilding the neighbor lists resets dn (and ft2, except for planes).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `mpm_obstacles` | in | `MPMObstacles` | `required` | rigid obstacles |

### `contact_forces`

mpmxdem MPMbox::boundaryConditions: MP-obstacle contact forces, added to the MP (fx, fy, fz) and, with the opposite sign, to the obstacle.

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `mp_cells` | in | `CellList` | `required` | cells holding MPs |
| `mpm_obstacles` | in/out | `MPMObstacles` | `required` | rigid obstacles |
| `mpm_contact_laws` | in | `MPMContactLaws` | `required` | MP-obstacle contact laws |
| `dt` | in | `double` | `required` | time step |

### `contact_laws`

Defines the MP-obstacle contact parameters per (MP group, obstacle group).

| Slot | Flow | Type | Default | Description |
| :--- | :---: | :--- | :--- | :--- |
| `set` | in | `std::vector<std::string>` | `[]` | one parameter per line, same syntax as mpmxdem's 'set' command: '<mu\|kn\|en2\|kt> groupMP groupObst value' |
| `mpm_contact_laws` | out | `MPMContactLaws` |  | MP-obstacle contact laws |

