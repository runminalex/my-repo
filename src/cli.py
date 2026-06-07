"""Command-line interface for the Calculator module.

Usage:
    python -m src.cli add 2 3
    python -m src.cli subtract 5 2
    python -m src.cli multiply 3 4
    python -m src.cli divide 10 2
    python -m src.cli power 2 3
    python -m src.cli modulus 10 3
    python -m src.cli sqrt 9
    python -m src.cli factorial 5
    python -m src.cli sin 0
    python -m src.cli cos 0
    python -m src.cli tan 0
    python -m src.cli log 100
    python -m src.cli ln 10
"""

import argparse
import sys
import math
from src.calculator import Calculator


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="Scientific Calculator CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")

    # Basic arithmetic operations
    for op in ["add", "subtract", "multiply", "divide", "power", "modulus"]:
        sub = subparsers.add_parser(op, help=f"{op.capitalize()} two numbers")
        sub.add_argument("a", type=float, help="First operand")
        sub.add_argument("b", type=float, help="Second operand")

    # Scientific operations
    sub = subparsers.add_parser("sqrt", help="Square root of a number")
    sub.add_argument("value", type=float, help="Number to compute square root of")

    sub = subparsers.add_parser("factorial", help="Factorial of a number")
    sub.add_argument("value", type=int, help="Non-negative integer for factorial")

    for op in ["sin", "cos", "tan"]:
        sub = subparsers.add_parser(op, help=f"{op.capitalize()} of an angle (in radians)")
        sub.add_argument("value", type=float, help="Angle in radians")

    sub = subparsers.add_parser("log", help="Logarithm (base 10) of a number")
    sub.add_argument("value", type=float, help="Positive number")

    sub = subparsers.add_parser("ln", help="Natural logarithm of a number")
    sub.add_argument("value", type=float, help="Positive number")

    return parser


def run(args: argparse.Namespace | None = None) -> str:
    """Run the calculator CLI with parsed arguments.

    Args:
        args: Parsed command-line arguments. If None, parses sys.argv.

    Returns:
        The result as a string.

    Raises:
        SystemExit: If the operation is unknown or arguments are invalid.
    """
    parser = create_parser()

    if args is None:
        parsed = parser.parse_args()
    else:
        parsed = args

    if not parsed.operation:
        parser.print_help()
        raise SystemExit(1)

    calc = Calculator()

    basic_ops = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide,
        "power": calc.power,
        "modulus": calc.modulus,
    }

    if parsed.operation in basic_ops:
        result = basic_ops[parsed.operation](parsed.a, parsed.b)
        return str(result)

    scientific_ops = {
        "sqrt": lambda v: math.sqrt(v),
        "factorial": lambda v: math.factorial(v),
        "sin": lambda v: math.sin(v),
        "cos": lambda v: math.cos(v),
        "tan": lambda v: math.tan(v),
        "log": lambda v: math.log10(v),
        "ln": lambda v: math.log(v),
    }

    if parsed.operation in scientific_ops:
        result = scientific_ops[parsed.operation](parsed.value)
        return str(result)

    parser.print_help()
    raise SystemExit(1)


def main() -> None:
    """Entry point for the CLI."""
    try:
        result = run()
        print(result)
    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except SystemExit:
        raise


if __name__ == "__main__":
    main()
