# Piscine_python

Repository containing my solutions and exercises from a **Python Piscine** (organized by days/modules: `py0` → `py10`).

The goal of this repo is to keep a clean, browsable history of the learning path: from basic syntax and CLI programs to small packages/modules and simple data/plotting exercises.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [How to run](#how-to-run)
  - [1) Running a single exercise](#1-running-a-single-exercise)
  - [2) Virtual environment (recommended)](#2-virtual-environment-recommended)
  - [3) Extra dependencies (py8/ex1)](#3-extra-dependencies-py8ex1)
- [Highlights (examples)](#highlights-examples)
- [Conventions](#conventions)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

---

## Overview

This repository is organized by folders named `py0`, `py1`, ..., `py10`.

Inside each `pyN` folder there are multiple exercises `ex0`, `ex1`, ... (the exact set varies by module).

Most exercises are small, self-contained Python scripts meant to be run directly with `python3`.

---

## Repository Structure

High-level layout (simplified):

- `py0/` … `py10/` — modules/days
  - `ex0/`, `ex1/`, … — individual exercises

Example:

- `py0/ex0/ft_hello_garden.py`

Some modules may contain extra folders (packages) and config files. For example:

- `py6/alchemy/` — small Python package/module
- `py8/ex1/pyproject.toml` — Poetry configuration
- `py8/ex1/requirements.txt` — pip dependencies

---

## How to run

### 1) Running a single exercise

From the repository root:

```bash
python3 py0/ex0/ft_hello_garden.py
```

If the file is meant to be executed as a script, it usually includes an `if __name__ == "__main__":` section.

Some exercises accept CLI arguments. Example (`py3/ex1/ft_score_analytics.py`):

```bash
python3 py3/ex1/ft_score_analytics.py 10 20 30
```

---

### 2) Virtual environment (recommended)

For Python exercises that may require third-party packages, use a venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 --version
```

To exit:

```bash
deactivate
```

---

### 3) Extra dependencies (py8/ex1)

The folder `py8/ex1` contains an exercise that checks/install guides for dependencies such as:

- `requests`
- `pandas`
- `matplotlib`
- `numpy`

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

## Highlights (examples)

A few examples you can try quickly:

- **Hello exercise**
  - `py0/ex0/ft_hello_garden.py`

- **CLI analytics (scores)**
  - `py3/ex1/ft_score_analytics.py` (accepts numeric CLI args)

- **Virtualenv / dependency checks + plotting demo**
  - `py8/ex0/construct.py` (detects if you are inside a venv)
  - `py8/ex1/loading.py` (checks packages and generates a `matrix_analysis.png`)

---

## Conventions

- Folder naming: `pyN/exM/...`
- Most scripts are intended to be run with `python3`.
- When a script prints output, it usually goes to standard output.

---

## Troubleshooting

- **Permission denied**: run with `python3 file.py` (don’t rely on executable bit).
- **Module not found**: activate a virtual environment and install dependencies.
- **Wrong Python version**: try `python3 --version` and run with the same interpreter you used for installing packages.

---

## Author

- GitHub: [Danilo-Ferreira37](https://github.com/Danilo-Ferreira37)