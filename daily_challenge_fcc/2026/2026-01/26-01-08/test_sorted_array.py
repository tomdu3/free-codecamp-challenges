from sorted_array import is_sorted
import unittest



class TestSortedArray(unittest.TestCase):
    def test_is_sorted(self):
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), "Ascending")
        self.assertEqual(is_sorted([10, 8, 6, 4, 2]), "Descending")
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), "Not sorted")
        self.assertEqual(is_sorted([3.14, 2.71, 1.61, 0.57]), "Descending")
        self.assertEqual(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]), "Ascending")
        self.assertEqual(is_sorted([0.4, 0.5, 0.3]), "Not sorted")

if __name__ == '__main__':
    unittest.main()
