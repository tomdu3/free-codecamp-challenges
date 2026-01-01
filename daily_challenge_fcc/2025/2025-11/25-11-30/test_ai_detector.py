import unittest
from ai_detector import detect_ai

class TestAiDetector(unittest.TestCase):
    def test_detect_ai(self):
        self.assertEqual(detect_ai("The quick brown fox jumped over the lazy dog."), "Human")
        self.assertEqual(detect_ai("The hypersonic brown fox - jumped (over) the lazy dog."), "Human")
        self.assertEqual(detect_ai("Yes - you're right! I made a mistake there - let me try again."), "AI")
        self.assertEqual(detect_ai("The extraordinary students were studying vivaciously."), "AI")
        self.assertEqual(detect_ai("The (excited) student was (coding) in the library."), "AI")
