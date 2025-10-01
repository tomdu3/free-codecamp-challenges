import pytest
from fill_tank import cost_to_fill

def test_cost_to_fill_full_tank():
    assert cost_to_fill(20, 0, 4.00) == "$80.00"

def test_cost_to_fill_partial_tank():
    assert cost_to_fill(15, 10, 3.50) == "$17.50"

def test_cost_to_fill_half_tank():
    assert cost_to_fill(18, 9, 3.25) == "$29.25"

def test_cost_to_fill_no_fill_needed():
    assert cost_to_fill(12, 12, 4.99) == "$0.00"

def test_cost_to_fill_decimal_fuel_level():
    assert cost_to_fill(15, 9.5, 3.98) == "$21.89"