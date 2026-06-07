"""Tests for the Calculator scientific operations and CLI module."""

import pytest
from src.calculator import Calculator
from src.cli import create_parser, run


@pytest.fixture
def calc():
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


# ── Scientific Operation Tests ─────────────────────────────────────

class TestCalculatorScientific:
    """Test suite for scientific operations on the Calculator class."""

    def test_sqrt(self, calc):
        assert calc.sqrt(9) == 3.0
        assert calc.sqrt(0) == 0.0
        assert calc.sqrt(2) == pytest.approx(1.414213562, rel=1e-9)
        assert calc.sqrt(0.25) == 0.5

    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
            calc.sqrt(-1)

    def test_factorial(self, calc):
        assert calc.factorial(0) == 1
        assert calc.factorial(1) == 1
        assert calc.factorial(5) == 120
        assert calc.factorial(10) == 3628800

    def test_factorial_negative(self, calc):
        with pytest.raises(ValueError, match="Cannot compute factorial of a negative number"):
            calc.factorial(-1)

    def test_sin(self, calc):
        assert calc.sin(0) == 0.0
        assert calc.sin(math.pi / 2) == pytest.approx(1.0, rel=1e-9)
        assert calc.sin(math.pi) == pytest.approx(0.0, abs=1e-15)

    def test_cos(self, calc):
        assert calc.cos(0) == 1.0
        assert calc.cos(math.pi / 2) == pytest.approx(0.0, abs=1e-15)
        assert calc.cos(math.pi) == pytest.approx(-1.0, rel=1e-9)

    def test_tan(self, calc):
        assert calc.tan(0) == 0.0
        assert calc.tan(math.pi / 4) == pytest.approx(1.0, rel=1e-9)

    def test_log10(self, calc):
        assert calc.log10(1) == 0.0
        assert calc.log10(10) == 1.0
        assert calc.log10(100) == 2.0
        assert calc.log10(1000) == 3.0

    def test_log10_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot compute logarithm of zero or a negative number"):
            calc.log10(0)

    def test_log10_negative(self, calc):
        with pytest.raises(ValueError, match="Cannot compute logarithm of zero or a negative number"):
            calc.log10(-5)

    def test_ln(self, calc):
        assert calc.ln(1) == 0.0
        assert calc.ln(math.e) == pytest.approx(1.0, rel=1e-9)
        assert calc.ln(math.e ** 2) == pytest.approx(2.0, rel=1e-9)

    def test_ln_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot compute natural logarithm of zero or a negative number"):
            calc.ln(0)

    def test_ln_negative(self, calc):
        with pytest.raises(ValueError, match="Cannot compute natural logarithm of zero or a negative number"):
            calc.ln(-5)

    def test_chained_operations(self, calc):
        """Test that basic and scientific operations compose correctly."""
        result = calc.sin(calc.sqrt(calc.power(calc.pi / 2, 2)))
        assert result == pytest.approx(1.0, rel=1e-9)


# ── CLI Tests ──────────────────────────────────────────────────────

class TestCalculatorCLI:
    """Test suite for the Calculator CLI."""

    def test_create_parser(self):
        """Parser should be created without errors."""
        parser = create_parser()
        assert parser is not None

    def test_cli_add(self):
        result = run(_parse("add", ["2", "3"]))
        assert result == "5"

    def test_cli_subtract(self):
        result = run(_parse("subtract", ["5", "2"]))
        assert result == "3"

    def test_cli_multiply(self):
        result = run(_parse("multiply", ["3", "4"]))
        assert result == "12"

    def test_cli_divide(self):
        result = run(_parse("divide", ["10", "2"]))
        assert result == "5.0"

    def test_cli_power(self):
        result = run(_parse("power", ["2", "3"]))
        assert result == "8"

    def test_cli_modulus(self):
        result = run(_parse("modulus", ["10", "3"]))
        assert result == "1"

    def test_cli_sqrt(self):
        result = run(_parse("sqrt", ["9"]))
        assert result == "3"

    def test_cli_factorial(self):
        result = run(_parse("factorial", ["5"]))
        assert result == "120"

    def test_cli_sin(self):
        result = run(_parse("sin", ["0"]))
        assert result == "0"

    def test_cli_cos(self):
        result = run(_parse("cos", ["0"]))
        assert result == "1"

    def test_cli_tan(self):
        result = run(_parse("tan", ["0"]))
        assert result == "0"

    def test_cli_log(self):
        result = run(_parse("log", ["100"]))
        assert result == "2.0"

    def test_cli_ln(self):
        result = run(_parse("ln", ["1"]))
        assert result == "0"

    def test_cli_divide_by_zero(self):
        """CLI should propagate ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            run(_parse("divide", ["5", "0"]))

    def test_cli_sqrt_negative(self):
        """CLI should propagate ValueError for sqrt of negative."""
        with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
            run(_parse("sqrt", ["-1"]))

    def test_cli_no_operation(self):
        """CLI should exit with code 1 when no operation given."""
        with pytest.raises(SystemExit):
            run(_parse(None, []))


def _parse(operation: str | None, args: list[str]) -> argparse.Namespace:
    """Helper to simulate command-line argument parsing."""
    parser = create_parser()
    if operation is None:
        return parser.parse_args([])
    return parser.parse_args([operation] + args)
