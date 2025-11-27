"""python3 python_doc/calculator.py.

Public API:
- calculate(a: float, op: str, b: float) -> float
"""

__all__ = ["calculate"]

import operator


def calculate(a: float, op: str, b: float) -> float:
    """Return result of a (op) b. Raise ValueError for unknown operator."""

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return ops[op](a, b)


def cli():
    """Simple command-line calculator."""
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))
        result = calculate(a, op, b)
    except ValueError as e:
        print("Invalid number: ... ", e)
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    cli()
