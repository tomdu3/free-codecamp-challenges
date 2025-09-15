import pytest
from vowel_repeater import repeat_vowels

def test_repeat_vowels_hello_world():
    assert repeat_vowels("hello world") == "helloo wooorld"

def test_repeat_vowels_freeCodeCamp():
    assert repeat_vowels("freeCodeCamp") == "freeeCooodeeeeCaaaaamp"

def test_repeat_vowels_AEIOU():
    assert repeat_vowels("AEIOU") == "AEeIiiOoooUuuuu"

def test_repeat_vowels_long_sentence():
    assert repeat_vowels("I like eating ice cream in Iceland") == (
        "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam "
        "iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"
    )