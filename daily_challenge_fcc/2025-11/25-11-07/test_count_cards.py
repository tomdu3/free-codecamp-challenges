import unittest
from count_cards import combinations

"""
    1. combinations(52) should return 1.
Waiting:2. combinations(1) should return 52.
Waiting:3. combinations(2) should return 1326.
Waiting:4. combinations(5) should return 2598960.
Waiting:5. combinations(10) should return 15820024220.
Waiting:6. combinations(50) should return 1326.
"""


def test_combinations():
    assert combinations(52) == 1
    assert combinations(1) == 52
    assert combinations(2) == 1326
    assert combinations(5) == 2598960
    assert combinations(10) == 15820024220
    assert combinations(50) == 1326
