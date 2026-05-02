# Piscine_python

*This project has been created as part of the 42 curriculum by dosorio-*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A collection of Python exercises organized by modules/days (`py0` → `py10`). Each module contains multiple exercises (`ex0`, `ex1`, …) and small scripts meant to be executed directly with `python3`.

This repository is meant to be **practical and navigable**: you can quickly jump to a module, run an exercise, and review the concepts being practiced.

---

## Table of Contents

- [Structure](#structure)
- [Modules (py0 → py10)](#modules-py0--py10)
- [How to run](#how-to-run)
  - [Run a single script](#run-a-single-script)
  - [Virtual environment (recommended)](#virtual-environment-recommended)
  - [Extra dependencies (py8/ex1)](#extra-dependencies-py8ex1)
- [Notable exercises](#notable-exercises)
- [Author](#author)

---

## Structure

```
py0/
  ex0/
  ex1/
  ...
py1/
  ex0/
  ...
...
py10/
  ex0/
  ...
```

Some modules include additional folders or packaging/config examples (e.g. `py6/alchemy`, `py8/ex1/pyproject.toml`).

---

## Modules (py0 → py10)

> Note: Exercises are grouped in folders `ex0`, `ex1`, etc. The exact content is in the code.

### `py0` — Basic functions and first runnable scripts
Very first steps: defining simple functions and producing output.

Example:
- `py0/ex0/ft_hello_garden.py` — defines a function and prints a greeting.

### `py1` — Basic program structure + type hints + simple “report” output
Introduces a more “program-like” structure: a main guard, docstrings, and typed functions that print formatted information.

Example:
- `py1/ex0/ft_garden_intro.py` — prints a small “plant info” report and uses `if __name__ == "__main__":`.

### `py2` — Exception handling and error scenarios
Focused on understanding `try/except`, raising errors, and handling multiple exception types cleanly.

Examples:
- `py2/ex0/ft_first_exeption.py` — validates temperatures, raises `ValueError` for out-of-range values, and handles invalid literals.
- `py2/ex1/ft_different_erros.py` — demonstrates catching `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, and multi-exception handling.

### `py3` — CLI scripts and simple analytics
Exercises built to run from the terminal, reading arguments with `sys.argv` and producing computed results.

Example:
- `py3/ex1/ft_score_analytics.py` — computes total/avg/max/min/range from CLI scores and validates inputs.

### `py4` — File I/O (reading files) + graceful failure paths
Practices reading from files and handling missing files without crashing.

Example:
- `py4/ex0/ft_ancient_text.py` — opens and reads `ancient_fragment.txt` and handles `FileNotFoundError` with a clear message.

### `py5` — OOP foundations: abstract classes, validation, polymorphism
More advanced object-oriented exercises using `ABC`, `@abstractmethod`, validation methods, and polymorphic “processors/streams”.

Examples:
- `py5/ex0/stream_processor.py` — abstract `DataProcessor` with concrete `NumericProcessor`, `TextProcessor`, and `LogProcessor` implementations.
- `py5/ex1/data_stream.py` — expands the idea into a more complete “stream” architecture (`DataStream`, batch processing, filtering, stats).

### `py6` — Packages and modular design (`alchemy`) + relative imports
Focused on structuring code as a real package with subpackages and relative imports.

Highlights:
- `py6/alchemy/elements.py` — element factories (`create_fire`, `create_water`, `create_earth`, `create_air`).
- `py6/alchemy/potions.py` — composes elements to build potion messages.
- `py6/alchemy/grimoire/validator.py` — validates ingredient strings.
- `py6/alchemy/grimoire/spellbook.py` — records or rejects spells based on ingredient validation.

### `py7` — OOP design patterns: abstract base classes + enums + inheritance (card game model)
Builds a small class model showing inheritance, abstract methods, and enums.

Example:
- `py7/ex0/Card.py` defines an abstract `Card` and `Rarity` enum; `py7/ex0/main.py` demonstrates usage with a `CreatureCard`.

### `py8` — Virtual environments, dependencies, and tooling ("Matrix")
Hands-on work with virtual environments and third-party libs.

Highlights:
- `py8/ex0/construct.py` — detects if you’re inside a venv and prints instructions.
- `py8/ex1/loading.py` — checks dependencies via `importlib` and generates a plot (`matrix_analysis.png`).
- `py8/ex1/requirements.txt` and `py8/ex1/pyproject.toml` — dependency manifests for pip and Poetry.

### `py9` — Data validation with Pydantic (typed models + constraints)
Exercises around schema validation and typed data models with constraints and error reporting.

Example:
- `py9/ex0/space_station.py` — defines a `SpaceStation` model using `pydantic` and shows validation failures.

### `py10` — Functional programming tools (lambda, map/filter/sorted) + quick stats
Focused on functional-style patterns and data transformations.

Example:
- `py10/ex0/lambda_spells.py` — uses `sorted(key=lambda ...)`, `filter`, `map`, and computes min/max/avg from lists of dicts.

---

## How to run

### Run a single script
From the repository root:

```bash
python3 path/to/script.py
```

Example:

```bash
python3 py0/ex0/ft_hello_garden.py
python3 py3/ex1/ft_score_analytics.py 10 20 30
```

### Virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 --version
```

Exit:

```bash
deactivate
```

### Extra dependencies (py8/ex1)

Using **pip**:

```bash
python3 -m venv matrix_env
source matrix_env/bin/activate
pip install -r py8/ex1/requirements.txt
python3 py8/ex1/loading.py
```

Using **Poetry** (optional):

```bash
cd py8/ex1
poetry install
poetry run python loading.py
```

---

## Notable exercises

- `py0/ex0/ft_hello_garden.py` — very first steps (functions + print)
- `py2/ex0/ft_first_exeption.py` — temperature validation + raising/handling exceptions
- `py2/ex1/ft_different_erros.py` — multiple exception types demo
- `py3/ex1/ft_score_analytics.py` — CLI program using `sys.argv` + basic stats
- `py5/ex0/stream_processor.py` — abstract classes + validation + polymorphism
- `py6/alchemy/*` — package structure + relative imports + modular organization
- `py7/ex0/*` — card model with enums + abstract base classes
- `py8/ex0/construct.py` — venv detection
- `py8/ex1/loading.py` — dependency check + simple data analysis/plot
- `py9/ex0/space_station.py` — pydantic validation
- `py10/ex0/lambda_spells.py` — functional programming utilities

---

## Author

- GitHub: [Danilo-Ferreira37](https://github.com/Danilo-Ferreira37)
