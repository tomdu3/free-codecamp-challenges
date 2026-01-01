from array_duplicates import find_duplicates
import unittest


class TestArrayDuplicates(unittest.TestCase):
    def test_find_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_duplicates([1, 2, 3, 4, 1, 2]), [1, 2])
        self.assertEqual(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]), [-6, 0, 2, 4, 5, 23])

if __name__ == '__main__':
    unittest.main()
