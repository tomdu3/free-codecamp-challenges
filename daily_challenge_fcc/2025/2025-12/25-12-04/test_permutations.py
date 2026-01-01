from permutations import count_permutations
import unittest

class TestPermutations(unittest.TestCase):
    def test_count_permutations_abb(self):
        self.assertEqual(count_permutations("abb"), 3)

    def test_count_permutations_abc(self):
        self.assertEqual(count_permutations("abc"), 6)

    def test_count_permutations_racecar(self):
        self.assertEqual(count_permutations("racecar"), 630)

    def test_count_permutations_freecodecamp(self):
        self.assertEqual(count_permutations("freecodecamp"), 39916800)
