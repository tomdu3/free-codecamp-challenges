from missing_number import find_missing_numbers
import unittest

class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        self.assertEqual(find_missing_numbers([1, 3, 5]), [2, 4])
        self.assertEqual(find_missing_numbers([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_missing_numbers([1, 10]), [2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(find_missing_numbers([10, 1, 10, 1, 10, 1]), [2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(find_missing_numbers([3, 1, 4, 1, 5, 9]), [2, 6, 7, 8])
        self.assertEqual(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]), [11])

if __name__ == '__main__':
    unittest.main()
