"""Tests for the calculator module."""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-1, 1) == 0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 5) == 0
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(-2, 3) == -6
    
    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(20, 4) == 5
        assert self.calc.divide(10, 2) == 5
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
