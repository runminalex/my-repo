"""Simple calculator module with basic and scientific arithmetic operations."""

import math


class Calculator:
    """A simple calculator with basic and scientific arithmetic operations."""

    # ── Basic Operations ──────────────────────────────────────────

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Return base raised to the power of exponent."""
        return base ** exponent

    def modulus(self, a: float, b: float) -> float:
        """Return the remainder of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot compute modulus with divisor zero")
        return a % b

    # ── Scientific Operations ─────────────────────────────────────

    def sqrt(self, value: float) -> float:
        """Return the square root of value.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(value)

    def factorial(self, value: int) -> int:
        """Return the factorial of value.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("Cannot compute factorial of a negative number")
        return math.factorial(value)

    def sin(self, value: float) -> float:
        """Return the sine of value (in radians)."""
        return math.sin(value)

    def cos(self, value: float) -> float:
        """Return the cosine of value (in radians)."""
        return math.cos(value)

    def tan(self, value: float) -> float:
        """Return the tangent of value (in radians)."""
        return math.tan(value)

    def log10(self, value: float) -> float:
        """Return the base-10 logarithm of value.

        Raises:
            ValueError: If value is zero or negative.
        """
        if value <= 0:
            raise ValueError("Cannot compute logarithm of zero or a negative number")
        return math.log10(value)

    def ln(self, value: float) -> float:
        """Return the natural logarithm of value.

        Raises:
            ValueError: If value is zero or negative.
        """
        if value <= 0:
            raise ValueError("Cannot compute natural logarithm of zero or a negative number")
        return math.log(value)
