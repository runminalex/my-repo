# my-repo

A simple "Hello, World!" website served via Python's built-in HTTP server, with a calculator module.

## Description

This project contains two main components:
1. **Hello World Website** — a minimal static website that displays a greeting, served via Python's built-in HTTP server.
2. **Calculator Module** — a Python package with basic arithmetic operations and comprehensive tests.

It serves as the starting point for the multi-agent GitOps pipeline.

## Prerequisites

- **Python 3.11+** (stdlib only for the website — pytest required for tests)

## Quick Start (Website)

```bash
chmod +x run.sh
./run.sh
```

Then open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

## Calculator Module

The calculator supports basic arithmetic operations:

```python
from src.calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.subtract(5, 2))  # 3
print(calc.multiply(3, 4))  # 12
print(calc.divide(10, 2))   # 5.0
print(calc.power(2, 3))     # 8
print(calc.modulus(10, 3))  # 1
```

### Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

## Project Structure

```
my-repo/
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI workflow
├── docs/
│   └── prds/
│       └── PRD-001-hello-world-website.md
├── src/
│   ├── __init__.py            # Calculator package init
│   └── calculator.py          # Calculator module
├── tests/
│   ├── __init__.py            # Tests package init
│   └── test_calculator.py     # Calculator tests
├── index.html                 # Main HTML page with greeting
├── run.sh                     # One-command launcher script
├── .gitignore                 # OS and Python ignores
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## License

Not yet licensed.