---
icon: simple/yaml
---

# YAML basics

`.msp` files are YAML. The constructs used in exaMPM decks are:

```yaml linenums="1"
# a comment
global:                        # a map (block)
  dt: 1.0e-5                   # scalar
  simulation_end_iteration: 49999

input_data:                    # a list (batch of operators)
  - grid_flavor_mpm            # operator without parameters
  - parameters:                # operator with parameters, block style
      gravity: [ 0.0 , -9.81 , 0.0 ]   # a vector
  - set_mp_grid: { group: 0, density: 2000., size: 0.02,      # flow style
                   lower: [ 3.5, 0.5, 0.3 ], upper: [ 3.9, 1.0, 2.7 ] }
  - obstacles:
      obstacles:               # a list of strings
        - "Sphere 0 3.1 1.0 1.4 0.1 free 30000.0 2.0 0.1 0 0"
```

## onika extensions

<div class="center-table" markdown>

| Syntax | Meaning |
|---|---|
| `includes: [ file.msp ]` | read other configuration files first (searched in `ONIKA_CONFIG_PATH`) |
| `+key: [ ... ]` | append to the batch `key` instead of replacing it |
| `name: other_block` | the hook `name` runs the batch `other_block` |
| `rebind: { slot: other }` | inside a batch, read/write the slot `slot` under the name `other` |
| `loop: true`, `condition: slot` | repeat the batch while the boolean slot is true |
| `condition: slot` (without loop) | run the batch only if the slot is true |
| `configuration:` | runtime options (threads, GPU, logging, profiling, debug) |

</div>

!!! tip "Debugging a deck"

    `--debug-graph true` prints the operator graph actually executed, and `--debug-config true` the final merged
    configuration.
