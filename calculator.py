"""Calculator module for basic arithmetic operations.

This module provides simple calculator functions.
"""

def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers."""
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
