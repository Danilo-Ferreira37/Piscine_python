# Piscine_python

*This project has been created as part of the 42 curriculum by dosorio-*

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

Below is a high-level description of what you can expect from each module in this repo.

> Note: Exercises are grouped in folders `ex0`, `ex1`, etc. The exact content is in the code.

### `py0` — First steps & basic functions
Introductory exercises focused on getting comfortable with:
- writing functions and printing output
- running simple scripts

Example:
- `py0/ex0/ft_hello_garden.py` — defines `ft_hello_garden()` and prints a greeting.

### `py1` — Basic scripting and progression
Exercises continuing the fundamentals and reinforcing:
- basic Python control flow and functions
- small self-contained scripts per exercise

### `py2` — Building confidence with small programs
A set of intermediate beginner exercises (still script-based) typically practicing:
- manipulating values and lists
- writing reusable helpers
- simple error handling patterns

### `py3` — CLI programs and analytics-style scripts
Focuses more on programs that are executed from the terminal with arguments.

Example:
- `py3/ex1/ft_score_analytics.py` — reads numeric scores from `sys.argv` and prints total, average, max/min, and range, with validation.

### `py4` — Continued practice (more structure)
A continuation module that usually increases complexity and encourages writing cleaner, more structured code across exercises.

### `py5` — More patterns & problem solving
Exercises that typically require combining multiple ideas and building slightly larger scripts.

### `py6` — Imports, packages, and modular code (`alchemy`)
This module includes a small package-style structure and multiple scripts.

Highlights:
- `py6/alchemy/` — a Python package example:
  - `elements.py` — simple element factories (`create_fire`, `create_water`, `create_earth`, `create_air`).
  - `potions.py` — composes elements to build potion messages.
  - `grimoire/validator.py` — validates ingredient strings.
  - `grimoire/spellbook.py` — records or rejects spells based on ingredient validation.

This module is good for understanding:
- relative imports (`from .elements import ...`)
- package layout (`__init__.py`, subpackages)
- splitting responsibilities into modules.

### `py7` — Advanced progression
A later module continuing the piscine progression. Content is organized by exercises in `py7/ex*`.

### `py8` — Virtual environments, dependencies, and tooling ("Matrix")
This module contains exercises around environments and third‑party libraries.

Highlights:
- `py8/ex0/construct.py` — detects if you're inside a venv and prints guidance.
- `py8/ex1/loading.py` — checks dependencies via `importlib`, suggests installation steps, and generates a histogram plot (`matrix_analysis.png`).
- `py8/ex1/requirements.txt` — pip dependencies.
- `py8/ex1/pyproject.toml` — Poetry configuration (`matrix-loader`).

### `py9` — Late-stage exercises
Another advanced module with exercises in `py9/ex*`.

### `py10` — Final module / consolidation
Final set of exercises (`py10/ex0` → `py10/ex4`) aimed at consolidating everything learned.

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
- `py3/ex1/ft_score_analytics.py` — CLI program using `sys.argv` + basic stats
- `py6/alchemy/*` — package structure + relative imports + modular organization
- `py8/ex0/construct.py` — venv detection
- `py8/ex1/loading.py` — dependency check + simple data analysis/plot

---

## Author

- GitHub: [Danilo-Ferreira37](https://github.com/Danilo-Ferreira37)