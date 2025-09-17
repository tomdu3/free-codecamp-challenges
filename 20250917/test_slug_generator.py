import pytest
from slug_generator import generate_slug

def test_generate_slug_basic():
    assert generate_slug("helloWorld") == "helloworld"

def test_generate_slug_with_space_and_punctuation():
    assert generate_slug("hello world!") == "hello%20world"

def test_generate_slug_with_leading_trailing_spaces_and_dash():
    assert generate_slug(" hello-world ") == "helloworld"

def test_generate_slug_with_double_spaces():
    assert generate_slug("hello  world") == "hello%20world"

def test_generate_slug_with_special_characters():
    assert generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") == "h3110%20w0r1d"

def test_generate_slug_empty_string():
    assert generate_slug("") == ""

def test_generate_slug_only_special_characters():
    assert generate_slug("!@#$%^&*()") == ""

def test_generate_slug_only_spaces():
    assert generate_slug("     ") == ""

def test_generate_slug_mixed_case_and_numbers():
    assert generate_slug("AbC 123 XyZ") == "abc%20123%20xyz"

def test_generate_slug_multiple_spaces_and_specials():
    assert generate_slug("A   B!!  C") == "a%20b%20c"

def test_generate_slug_trailing_and_leading_specials():
    assert generate_slug("!A B C!") == "a%20b%20c"