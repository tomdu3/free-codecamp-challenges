import pytest
from pangram import is_pangram

def test_is_pangram_basic_true():
    assert is_pangram("hello", "helo") is True

def test_is_pangram_missing_letter():
    assert is_pangram("hello", "hel") is False

def test_is_pangram_extra_letter():
    assert is_pangram("hello", "helow") is False

def test_is_pangram_multiple_words_true():
    assert is_pangram("hello world", "helowrd") is True

def test_is_pangram_case_insensitive():
    assert is_pangram("Hello World!", "helowrd") is True

def test_is_pangram_extra_letter_false():
    assert is_pangram("Hello World!", "heliowrd") is False

def test_is_pangram_freecodecamp_false():
    assert is_pangram("freeCodeCamp", "frcdmp") is False

def test_is_pangram_full_alphabet_true():
    assert is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") is True

def test_is_pangram_empty_sentence():
    assert is_pangram("", "abc") is False

def test_is_pangram_empty_letters():
    assert is_pangram("hello", "") is False

def test_is_pangram_both_empty():
    assert is_pangram("", "") is True

def test_is_pangram_non_alpha_characters():
    assert is_pangram("h3ll0!", "helo") is False

def test_is_pangram_repeated_letters():
    assert is_pangram("aaaaa", "a") is True

def test_is_pangram_partial_alphabet_false():
    assert is_pangram("abcdefg", "abcdefgh") is False

def test_is_pangram_subset_true():
    assert is_pangram("abcdefg", "abcdefg") is True