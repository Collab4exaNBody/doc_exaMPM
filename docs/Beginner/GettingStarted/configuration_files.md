---
icon: lucide/files
---

# Configuration files

Every run reads, in this order:

1. `data/config/main-config.msp` — the default simulation graph, installed with exaMPM;
2. the files listed under its `includes:` key, here `config_globals.msp` (default `global` values);
3. your deck, given on the command line.

A later file **overrides** earlier definitions key by key. The default `simulation` block runs a fixed sequence of
**hooks**:

```yaml linenums="1"
simulation:
  name: sim
  body:
    - print_logo_banner
    - hw_device_init      # MPI and GPU initialization
    - init_prolog         # default: global
    - input_data          # nop: domain, material points, obstacles...
    - init_epilog         # nop: MPM decks use mpm_init
    - first_iteration     # nop
    - compute_loop        # nop: MPM decks use mpm_compute_loop
    - simulation_epilog   # nop
    - hw_device_finalize
```

A deck never edits `simulation`: it fills the hooks. An MPM deck typically defines `input_data` and sets

```yaml linenums="1"
init_epilog: mpm_init
compute_loop: mpm_compute_loop
mpm_constitutive_model:
  - mohr_coulomb: { ... }
```

The complete default configuration is shown in [Default YAML](../../User/SimulationGraph/default_yaml.md).

## Overriding and appending

- `key: value` replaces the whole block `key`;
- inside a map, only the keys you give are replaced (e.g. `global: { dt: 1.0e-6 }` keeps the other globals);
- `+key: [ ... ]` appends operators to the batch `key` instead of replacing it:

```yaml linenums="1"
+mpm_log_extra:
  - print_obstacles
```
