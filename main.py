#!/usr/bin/env python3
"""
Main entry point for the Python project.
"""

import sys
from src.calculator import Calculator
from src.utils import greet


def main():
    """Main function."""
    try:
        print(greet("User"))
        
        calc = Calculator()
        
        # Example calculations
        print("\n--- Calculator Examples ---")
        print(f"5 + 3 = {calc.add(5, 3)}")
        print(f"10 - 4 = {calc.subtract(10, 4)}")
        print(f"6 * 7 = {calc.multiply(6, 7)}")
        print(f"20 / 4 = {calc.divide(20, 4)}")
        
        print("\n--- Project running successfully! ---")
    except ValueError as ve:
        print(f"\n[Value Error] {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[Runtime Error] An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
