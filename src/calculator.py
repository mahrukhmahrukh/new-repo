"""Calculator utilities."""

from typing import Union

Number = Union[int, float]


class Calculator:
    """Simple calculator class with basic operations."""
    
    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Subtract two numbers."""
        return a - b
    
    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: Number, b: Number) -> Number:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
