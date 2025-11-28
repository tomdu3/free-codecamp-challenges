import unittest
from word_guesser import compare

class TestWordGuesser(unittest.TestCase):
    def test_compare_apple_poppa(self):
        self.assertEqual(compare("APPLE", "POPPA"), "10201")

    def test_compare_react_trace(self):
        self.assertEqual(compare("REACT", "TRACE"), "11221")

    def test_compare_debugs_python(self):
        self.assertEqual(compare("DEBUGS", "PYTHON"), "000000")

    def test_compare_javascript_typescript(self):
        self.assertEqual(compare("JAVASCRIPT", "TYPESCRIPT"), "0000222222")

    def test_compare_orange_rounds(self):
        self.assertEqual(compare("ORANGE", "ROUNDS"), "110200")

    def test_compare_wireless_ethernet(self):
        self.assertEqual(compare("WIRELESS", "ETHERNET"), "10021000")
