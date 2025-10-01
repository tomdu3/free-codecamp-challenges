import unittest
from second_largest import second_largest

class Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(second_largest([1, 2, 3, 4]), 3)

    def test_large_numbers(self):
        self.assertEqual(second_largest([20, 139, 94, 67, 31]), 94)

    def test_duplicates(self):
        self.assertEqual(second_largest([2, 3, 4, 6, 6]), 4)

    def test_negative_and_float(self):
        self.assertEqual(second_largest([10, -17, 55.5, 44, 91, 0]), 55.5)

    def test_many_duplicates(self):
        self.assertEqual(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]), 0)

    def test_two_elements(self):
        self.assertEqual(second_largest([5, 10]), 5)

    def test_all_same(self):
        with self.assertRaises(IndexError):
            second_largest([7, 7, 7, 7])

    def test_negative_numbers(self):
        self.assertEqual(second_largest([-10, -20, -30, -40]), -20)

    def test_floats(self):
        self.assertEqual(second_largest([1.1, 2.2, 3.3, 2.2]), 2.2)

    def test_mixed_types(self):
        self.assertEqual(second_largest([1, 2.5, 3, 2.5]), 2.5)

if __name__ == "__main__":
    unittest.main()