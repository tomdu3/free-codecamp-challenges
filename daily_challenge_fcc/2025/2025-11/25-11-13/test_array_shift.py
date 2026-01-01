import unittest
from array_shift import shift_array

class TestShiftArray(unittest.TestCase):
    
    def test_shift_positive_integers(self):
        self.assertEqual(shift_array([1, 2, 3], 1), [2, 3, 1])
    
    def test_shift_negative_integers(self):
        self.assertEqual(shift_array([1, 2, 3], -1), [3, 1, 2])
    
    def test_shift_strings_positive(self):
        self.assertEqual(shift_array(["alpha", "bravo", "charlie"], 5), ["charlie", "alpha", "bravo"])
    
    def test_shift_strings_negative(self):
        self.assertEqual(shift_array(["alpha", "bravo", "charlie"], -11), ["bravo", "charlie", "alpha"])
    
    def test_shift_large_array(self):
        self.assertEqual(shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15), [5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
    
    def test_shift_zero(self):
        self.assertEqual(shift_array([1, 2, 3], 0), [1, 2, 3])
    
    def test_shift_empty_array(self):
        self.assertEqual(shift_array([], 5), [])
    
    def test_shift_single_element(self):
        self.assertEqual(shift_array([42], 10), [42])


if __name__ == '__main__':
    unittest.main()