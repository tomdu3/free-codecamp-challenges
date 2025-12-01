import pytest
from tip_calculator import calculate_tips

@pytest.mark.parametrize("meal, custom, expected", [
    ("$10.00", "25%", ["$1.50", "$2.00", "$2.50"]),
    ("$89.67", "26%", ["$13.45", "$17.93", "$23.31"]),
    ("$19.85", "9%",  ["$2.98", "$3.97", "$1.79"]),
])
def test_calculate_tips_examples(meal, custom, expected):
    assert calculate_tips(meal, custom) == expected