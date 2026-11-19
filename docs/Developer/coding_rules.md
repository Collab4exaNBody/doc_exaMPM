---
icon: material/format-list-checks
---

# Coding Rules

## Files and namespaces

- Headers are `.h` files under `include/exaMPM/`, with `#pragma once`.
- Host-only operators are `.cpp`; operators that launch a kernel are `.cu`.
- Code goes in `namespace exaMPM { using namespace exanb; ... }`. Fields are declared in `include/exaMPM/fields.h`
  with `XNB_DECLARE_FIELD`.

## Naming

- snake_case for operators, slots, YAML keys and functions; CamelCase for types; `m_` prefix for members.
- Operator names have no `mpm_` prefix; YAML blocks of `main-config.msp` keep it (`mpm_compute_loop`, ...) to avoid
  clashes with exaNBody and onika names.
- Grid-templated operators have a `...Tmpl` alias; `ONIKA_AUTORUN_INIT(<file basename>)`.

## Operators

- `inline void execute() override final`; every slot has a `DocString`; every operator implements
  `documentation()`.
- `REQUIRED`/`OPTIONAL` when there is no sane default; `PRIVATE` slots for persistent state.

## Logging and errors

- `lout` (output), `ldbg` (debug, enabled with `configuration: { debug: { filter: [ "regex" ] } }`), `lerr`;
  `fatal_error() << ...` to abort. Never `std::cout` or `printf`.

## Simplicity

- exaMPM is a prototype: no speculative abstraction.
- No new field set unless required: each one compiles every grid-templated operator once more.
- Never modify onika or exaNBody from exaMPM: report the need upstream and work around it locally.
