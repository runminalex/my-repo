"""Tests for the Calculator module."""

import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


class TestCalculator:
    """Test suite for the Calculator class."""

    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
        assert calc.add(1.5, 2.5) == 4.0

    def test_subtract(self, calc):
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(1, 1) == 0
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(1.5, 0.5) == 1.0

    def test_multiply(self, calc):
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(1.5, 2) == 3.0

    def test_divide(self, calc):
        assert calc.divide(6, 3) == 2
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(0, 5) == 0
        assert calc.divide(-6, 3) == -2

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(5, 0)

    def test_power(self, calc):
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(2, -1) == 0.5
        assert calc.power(9, 0.5) == 3.0

    def test_modulus(self, calc):
        assert calc.modulus(10, 3) == 1
        assert calc.modulus(10, 5) == 0
        assert calc.modulus(-10, 3) == 2  # Python's modulo behavior

    def test_modulus_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="Cannot compute modulus with divisor zero"):
            calc.modulus(5, 0)
