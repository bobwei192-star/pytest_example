import pytest
from calculator import add_numbers, divide_numbers, multiply_numbers


class TestCalculator:
    def test_add_numbers_correct(self):
        """Test that should pass but will fail due to the bug"""
        result = add_numbers(3, 5)
        assert result == 8, f"Expected 8, but got {result}"
    
    def test_add_numbers_with_negative(self):
        """Test addition with negative numbers - will fail due to the bug"""
        result = add_numbers(-3, -5)
        assert result == -8, f"Expected -8, but got {result}"
    
    def test_divide_numbers_normal(self):
        """Test normal division - should pass"""
        result = divide_numbers(10, 2)
        assert result == 5.0, f"Expected 5.0, but got {result}"
    
    def test_divide_numbers_by_zero(self):
        """Test division by zero - should fail due to missing error handling"""
        with pytest.raises(ZeroDivisionError):
            divide_numbers(10, 0)
    
    def test_multiply_numbers(self):
        """Test multiplication - should pass"""
        result = multiply_numbers(4, 7)
        assert result == 28, f"Expected 28, but got {result}"