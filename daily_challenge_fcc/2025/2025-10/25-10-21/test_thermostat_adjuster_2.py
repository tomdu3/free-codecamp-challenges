import pytest
from thermostat_adjuster_2 import adjust_thermostat

@pytest.mark.parametrize("current_f,target_c,expected", [
    (32, 0, "Hold"),
    (70, 25, "Heat: 7.0 degrees Fahrenheit"),
    (72, 18, "Cool: 7.6 degrees Fahrenheit"),
    (212, 100, "Hold"),
    (59, 22, "Heat: 12.6 degrees Fahrenheit"),
    (68.0, 20, "Hold"),  # 20°C == 68°F
    (32, -40, "Cool: 72.0 degrees Fahrenheit"),  # -40°C == -40°F -> large cooling
    (70.04, 21, "Cool: 0.2 degrees Fahrenheit"),  # small fractional cooling, rounds to 0.2
    (-40, -40, "Hold"),  # both equal at -40
    (0, 0, "Heat: 32.0 degrees Fahrenheit"),  # 0°C -> 32°F
])
def test_adjust_thermostat_various(current_f, target_c, expected):
    assert adjust_thermostat(current_f, target_c) == expected