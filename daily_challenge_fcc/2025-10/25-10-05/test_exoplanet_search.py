import pytest
from exoplanet_search import has_exoplanet

@pytest.mark.parametrize("reading,expected", [
    ("665544554", False),
    ("FGFFCFFGG", True),
    ("MONOPLONOMONPLNOMPNOMP", False),
    ("FREECODECAMP", True),
    ("9AB98AB9BC98A", False),
    ("ZXXWYZXYWYXZEGZXWYZXYGEE", True),
])
def test_has_exoplanet(reading, expected):
    assert has_exoplanet(reading) == expected