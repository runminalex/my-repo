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
from src.calculator import Calculator


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="Scientific Calculator CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")

    # Basic arithmetic operations (two operands)
    for op in ["add", "subtract", "multiply", "divide", "power", "modulus"]:
        sub = subparsers.add_parser(op, help=f"{op.capitalize()} two numbers")
        sub.add_argument("a", type=float, help="First operand")
        sub.add_argument("b", type=float, help="Second operand")

    # Scientific operations (single operand)
    for op in ["sqrt", "factorial", "sin", "cos", "tan", "log", "ln"]:
        sub = subparsers.add_parser(op, help=f"{op.capitalize()} of a number")
        sub.add_argument("value", type=float, help="Input value")

    return parser


def run(parsed: argparse.Namespace | None = None) -> str:
    """Run the calculator CLI with parsed arguments.

    Args:
        parsed: Parsed command-line arguments. If None, parses sys.argv.

    Returns:
        The result as a string.

    Raises:
        SystemExit: If the operation is unknown or arguments are invalid.
    """
    parser = create_parser()

    if parsed is None:
        parsed = parser.parse_args()

    if not parsed.operation:
        parser.print_help()
        raise SystemExit(1)

    calc = Calculator()

    # Map operations to Calculator methods
    op_map: dict[str, tuple] = {
        "add": (calc.add, ["a", "b"]),
        "subtract": (calc.subtract, ["a", "b"]),
        "multiply": (calc.multiply, ["a", "b"]),
        "divide": (calc.divide, ["a", "b"]),
        "power": (calc.power, ["a", "b"]),
        "modulus": (calc.modulus, ["a", "b"]),
        "sqrt": (calc.sqrt, ["value"]),
        "factorial": (calc.factorial, ["value"]),
        "sin": (calc.sin, ["value"]),
        "cos": (calc.cos, ["value"]),
        "tan": (calc.tan, ["value"]),
        "log": (calc.log10, ["value"]),
        "ln": (calc.ln, ["value"]),
    }

    if parsed.operation not in op_map:
        parser.print_help()
        raise SystemExit(1)

    func, param_names = op_map[parsed.operation]

    if len(param_names) == 2:
        args_list = [getattr(parsed, param_names[0]), getattr(parsed, param_names[1])]
    else:
        args_list = [getattr(parsed, param_names[0])]

    result = func(*args_list)

    # Format result — int if no fractional part
    if isinstance(result, float) and result == int(result):
        return str(int(result))
    return str(result)


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
