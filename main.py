#!/usr/bin/env python3
"""
Main entry point for the Python project.
"""

from src.calculator import Calculator
from src.utils import greet


def main():
    """Main function."""
    print(greet("User"))
    
    calc = Calculator()
    
    # Example calculations
    print("\n--- Calculator Examples ---")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    
    print("\n--- Project running successfully! ---")


if __name__ == "__main__":
    main()
