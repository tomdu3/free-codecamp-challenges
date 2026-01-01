import pytest
from yoda_talk import wise_speak

def test_wise_speak_basic():
    assert wise_speak("You must speak wisely.") == "Speak wisely, you must."
    
def test_wise_speak_exclamation():
    assert wise_speak("You can do it!") == "Do it, you can!"

def test_wise_speak_question():
    assert wise_speak("Do you think you will complete this?") == "Complete this, do you think you will?"

def test_wise_speak_base():
    assert wise_speak("All your base are belong to us.") == "Belong to us, all your base are."
    
def test_wise_speak_learn():
    assert wise_speak("You have much to learn.") == "Much to learn, you have."

def test_wise_speak_no_trigger_words():
    assert wise_speak("The sky is blue.") == "The sky is blue."
