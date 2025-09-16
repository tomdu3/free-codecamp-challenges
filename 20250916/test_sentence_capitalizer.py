import pytest
from sentence_capitalizer import capitalize

def test_simple_sentence():
    assert capitalize("this is a simple sentence.") == "This is a simple sentence."

def test_multiple_sentences():
    assert capitalize("hello world. how are you?") == "Hello world. How are you?"

def test_ellipsis_and_exclamations():
    assert capitalize("i did today's coding challenge... it was fun!!") == "I did today's coding challenge... It was fun!!"

def test_multiple_punctuations():
    assert capitalize("crazy!!!strange???unconventional...sentences.") == "Crazy!!!Strange???Unconventional...Sentences."

def test_space_before_period():
    assert capitalize("there's a space before this period . why is there a space before that period ?") == "There's a space before this period . Why is there a space before that period ?"

def test_empty_string():
    assert capitalize("") == ""

def test_no_punctuation():
    assert capitalize("this is not punctuated") == "This is not punctuated"

def test_all_uppercase():
    assert capitalize("HELLO. WORLD!") == "HELLO. WORLD!"

def test_leading_spaces():
    assert capitalize("   leading spaces. next sentence.") == "   Leading spaces. Next sentence."

def test_numbers_and_symbols():
    assert capitalize("123abc. $money?") == "123Abc. $Money?"

def test_newlines():
    assert capitalize("first line.\nsecond line?") == "First line.\nSecond line?"

def test_mixed_case():
    assert capitalize("tHiS iS a TeSt. aNoThEr oNe!") == "THiS iS a TeSt. ANoThEr oNe!"