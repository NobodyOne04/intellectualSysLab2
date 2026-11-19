# intellectualSysLab2

A 2020 university lab: genetic algorithm that evolves strings toward `GOAL`.

## Commands
- `cd IS && python3 entrypoint.py` (imports are relative to `IS/`). Standard library only. No tests.

## Layout
- `IS/config.py`: `GOAL`, `GENES`.
- `IS/entrypoint.py`: builds a pool of 100, runs `evolution()`, prints steps and time.
- `IS/src/genetic_code.py`: one candidate (fitness, mutation, crossover).
- `IS/src/pool.py`: population, selection, evolution loop.
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- `GOAL` may only use characters from `GENES`, or it can never be reached.
- Archived lab: docs or small fixes only unless asked.
