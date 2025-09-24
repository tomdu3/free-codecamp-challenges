import pytest
from perfect_square import is_perfect_square

def test_is_perfect_square_true_cases():
    assert is_perfect_square(9) is True
    assert is_perfect_square(49) is True
    assert is_perfect_square(1) is True
    assert is_perfect_square(0) is True
    assert is_perfect_square(25281) is True

def test_is_perfect_square_false_cases():
    assert is_perfect_square(2) is False
    assert is_perfect_square(10) is False
    assert is_perfect_square(50) is False
    assert is_perfect_square(20) is False