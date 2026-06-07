"""Tests for the calculator module."""
import pytest
from calculator import add, subtract, multiply, divide


class TestCalculator:
    """Test suite for calculator operations."""

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 2) == 5.0

    def test_divide(self):
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
        assert divide(0, 5) == 0.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
