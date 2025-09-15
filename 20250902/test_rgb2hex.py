import pytest
from rgb2hex import rgb_to_hex

def test_rgb_to_hex_white():
    assert rgb_to_hex("rgb(255, 255, 255)") == "#ffffff"

def test_rgb_to_hex_varied_digits():
    assert rgb_to_hex("rgb(1, 11, 111)") == "#010b6f"

def test_rgb_to_hex_light_blue():
    assert rgb_to_hex("rgb(173, 216, 230)") == "#add8e6"

def test_rgb_to_hex_blue_shade():
    assert rgb_to_hex("rgb(79, 123, 201)") == "#4f7bc9"