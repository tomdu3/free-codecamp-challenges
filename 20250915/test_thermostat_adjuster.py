import pytest
from thermostat_adjuster import adjust_thermostat

def test_adjust_thermostat_heat():
    assert adjust_thermostat(68, 72) == "heat"
    assert adjust_thermostat(-20.5, -10.1) == "heat"
    assert adjust_thermostat(50, 55) == "heat"
    assert adjust_thermostat(0, 10) == "heat"

def test_adjust_thermostat_cool():
    assert adjust_thermostat(75, 72) == "cool"
    assert adjust_thermostat(100, 99.9) == "cool"
    assert adjust_thermostat(80, 70) == "cool"
    assert adjust_thermostat(10, 0) == "cool"

def test_adjust_thermostat_hold():
    assert adjust_thermostat(72, 72) == "hold"
    assert adjust_thermostat(0.0, 0.0) == "hold"
    assert adjust_thermostat(-5, -5) == "hold"
    assert adjust_thermostat(99.9, 99.9) == "hold"