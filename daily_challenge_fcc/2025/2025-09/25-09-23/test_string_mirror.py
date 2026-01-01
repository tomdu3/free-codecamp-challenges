import unittest
from string_mirror import is_mirror

class TestIsMirror(unittest.TestCase):
    def test_not_mirror_same(self):
        self.assertFalse(is_mirror("helloworld", "helloworld"))

    def test_mirror_with_spaces(self):
        self.assertTrue(is_mirror("Hello World", "dlroW olleH"))

    def test_mirror_case_sensitive(self):
        self.assertTrue(is_mirror("RaceCar", "raCecaR"))

    def test_not_mirror_same_case(self):
        self.assertFalse(is_mirror("RaceCar", "RaceCar"))

    def test_not_mirror(self):
        self.assertFalse(is_mirror("Mirror", "rorrim"))

    def test_mirror_with_dash(self):
        self.assertTrue(is_mirror("Hello World", "dlroW-olleH"))

    def test_mirror_with_exclamation(self):
        self.assertTrue(is_mirror("Hello World", "!dlroW !olleH"))

if __name__ == "__main__":
    unittest.main()