# my-repo

A simple "Hello, World!" website served via Python's built-in HTTP server, with a scientific calculator module, CLI, and statistics module.

## Description

This project contains three main components:
1. **Hello World Website** — a minimal static website that displays a greeting, served via Python's built-in HTTP server.
2. **Scientific Calculator** — a Python package with basic arithmetic, scientific operations, and a command-line interface.
3. **Statistics Module** — a Python module for descriptive statistical operations on data sets.

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

## Statistics Module

The `Statistics` class provides descriptive statistical operations on data sets.

### Usage

```python
from src.stats import Statistics

stats = Statistics()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(stats.mean(data))              # 5.5
print(stats.median(data))            # 5.5
print(stats.mode(data))              # [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
print(stats.variance(data))          # 8.25 (population variance)
print(stats.standard_deviation(data)) # 2.872 (population std)
print(stats.min(data))               # 1.0
print(stats.max(data))               # 10.0
print(stats.range(data))             # 9.0
print(stats.quartiles(data))         # {'Q1': 3.0, 'Q2': 5.5, 'Q3': 8.0}
print(stats.iqr(data))               # 5.0

# Sample variance (ddof=1)
print(stats.variance(data, ddof=1))  # 9.166...
print(stats.standard_deviation(data, ddof=1))  # 3.027...
```

### Available Operations

| Operation            | Description                                  | Raises                                      |
|----------------------|----------------------------------------------|---------------------------------------------|
| `mean(data)`        | Arithmetic mean                              | `ValueError` if empty                       |
| `median(data)`      | Median value                                 | `ValueError` if empty                       |
| `mode(data)`        | Most frequent value(s) as sorted list        | `ValueError` if empty                       |
| `variance(data, ddof=0)` | Variance (0=population, 1=sample)       | `ValueError` if len(data) <= ddof           |
| `standard_deviation(data, ddof=0)` | Standard deviation (0=population, 1=sample) | `ValueError` if len(data) <= ddof |
| `min(data)`         | Minimum value                                | `ValueError` if empty                       |
| `max(data)`         | Maximum value                                | `ValueError` if empty                       |
| `range(data)`       | Range (max - min)                            | `ValueError` if empty                       |
| `quartiles(data)`   | Q1, Q2 (median), Q3 as dict                  | `ValueError` if len(data) < 2              |
| `iqr(data)`         | Interquartile range (Q3 - Q1)                | `ValueError` if len(data) < 2              |

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
│   ├── cli.py                 # Command-line interface
│   └── stats.py               # Statistics module
├── tests/
│   ├── __init__.py            # Tests package init
│   ├── test_calculator.py     # Calculator tests (basic + scientific + CLI)
│   └── test_stats.py          # Statistics tests
├── index.html                 # Main HTML page with greeting
├── run.sh                     # One-command launcher script
├── .gitignore                 # OS and Python ignores
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## License

MIT
