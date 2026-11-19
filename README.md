# intellectualSysLab2

A **genetic algorithm** that evolves random strings into a target word (Intelligent Systems
lab 2, 2020). The target is the Russian word `Мир`, built from the Cyrillic alphabet.

## Run

```sh
cd IS && python3 entrypoint.py
```

Python 3, standard library only. It prints the best string of every generation, then the number
of generations and the run time.

## How it works

- `IS/config.py`: `GOAL = "Мир"`, `GENES` = upper- and lower-case Cyrillic letters.
- `IS/src/genetic_code.py`: `GeneticCode`, one candidate string. Fitness (`measure`) is minus
  the number of wrong letters; `mutate` changes up to 5 wrong positions; `crossing_over` joins
  two parents at a random cut.
- `IS/src/pool.py`: `Pool` of 100 candidates. Each epoch mutates all, keeps the best 10%
  (`selection`) and refills the pool with children of random members (survivors first, then new children too); stops when the best
  matches the goal or after 1000 epochs.

Decisions: [docs/adr](docs/adr/README.md).
