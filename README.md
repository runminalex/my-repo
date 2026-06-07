# my-repo

A simple "Hello, World!" website served via Python's built-in HTTP server, with a scientific calculator module and CLI.

## Description

This project contains two main components:
1. **Hello World Website** — a minimal static website that displays a greeting, served via Python's built-in HTTP server.
2. **Scientific Calculator** — a Python package with basic arithmetic, scientific operations, and a command-line interface.

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

### Basic Operations (as a library)

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

### Scientific Operations (as a library)

```python
from src.calculator import Calculator
import math

calc = Calculator()
print(calc.sqrt(9))                 # 3.0
print(calc.factorial(5))            # 120
print(calc.sin(math.pi / 2))        # 1.0
print(calc.cos(0))                  # 1.0
print(calc.tan(0))                  # 0.0
print(calc.log10(100))              # 2.0
print(calc.ln(math.e))              # 1.0
```

### Command-Line Interface

The calculator can also be used from the command line:

```bash
# Basic arithmetic
python -m src.cli add 2 3          # 5
python -m src.cli subtract 5 2     # 3
python -m src.cli multiply 3 4     # 12
python -m src.cli divide 10 2      # 5.0
python -m src.cli power 2 3        # 8
python -m src.cli modulus 10 3     # 1

# Scientific operations
python -m src.cli sqrt 9           # 3
python -m src.cli factorial 5      # 120
python -m src.cli sin 0            # 0
python -m src.cli cos 0            # 1
python -m src.cli tan 0            # 0
python -m src.cli log 100          # 2.0
python -m src.cli ln 1             # 0
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
│   ├── calculator.py          # Calculator module (basic + scientific)
│   └── cli.py                 # Command-line interface
├── tests/
│   ├── __init__.py            # Tests package init
│   └── test_calculator.py     # Calculator tests (basic + scientific + CLI)
├── index.html                 # Main HTML page with greeting
├── run.sh                     # One-command launcher script
├── .gitignore                 # OS and Python ignores
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## License

MIT
