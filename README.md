# CISC 217 Week 6 — Tested Utility Package

## Topic

Modules, public APIs, and unit testing.

## Goal

Complete a small Python package made of multiple modules.

You will practice:

- organizing related functions into modules,
- separating public functions from internal helpers,
- exposing a package-level public API through `__init__.py`,
- using `__all__`,
- writing code that satisfies an existing pytest suite,
- testing normal, boundary, invalid, and exception cases,
- using the `tmp_path` fixture for file tests.

## Repository Structure

```text
src/
└── cisc217_week6/
    ├── __init__.py
    ├── scores.py
    ├── text_tools.py
    └── file_tools.py

tests/
├── test_public_api.py
├── test_scores.py
├── test_text_tools.py
└── test_file_tools.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest -q
```

## Required Work

Complete the functions in:

- `src/cisc217_week6/scores.py`
- `src/cisc217_week6/text_tools.py`
- `src/cisc217_week6/file_tools.py`

Do not rename the required public functions.

## Public API

The package-level public API is already defined in `src/cisc217_week6/__init__.py`.

Other code should be able to use:

```python
from cisc217_week6 import (
    average_score,
    normalize_scores,
    clean_name,
    slugify,
    read_lines,
    write_lines,
)
```

## Internal Helpers

Functions beginning with `_` are internal helpers and are not part of the package public API.

## Important Rules

- Keep the required function names and parameters.
- Use UTF-8 for text-file operations.
- Use `pathlib.Path` for file paths.
- Raise `ValueError` for invalid scores and unusable names/slugs.
- Do not add internal helpers to `__all__`.
- Do not modify instructor tests merely to make code pass.
- Run the full test suite before pushing.

## Submit

1. Complete the package.
2. Run `python -m pytest -q`.
3. Commit your work.
4. Push to `main`.
5. Confirm the Classroom50 autograder passes.
6. Post your repository link and requested evidence in Canvas.
