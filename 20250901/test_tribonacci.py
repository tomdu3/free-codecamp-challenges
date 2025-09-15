import pytest
from tribonacci import tribonacci_sequence

def test_tribonacci_sequence_length_20():
    assert tribonacci_sequence([0, 0, 1], 20) == [
        0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513
    ]

def test_tribonacci_sequence_length_1():
    assert tribonacci_sequence([21, 32, 43], 1) == [21]

def test_tribonacci_sequence_length_0():
    assert tribonacci_sequence([0, 0, 1], 0) == []

def test_tribonacci_sequence_length_2():
    assert tribonacci_sequence([10, 20, 30], 2) == [10, 20]

def test_tribonacci_sequence_length_3():
    assert tribonacci_sequence([10, 20, 30], 3) == [10, 20, 30]

def test_tribonacci_sequence_length_8():
    assert tribonacci_sequence([123, 456, 789], 8) == [123, 456, 789, 1368, 2613, 4770, 8751, 16134]