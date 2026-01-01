import unittest
from targeted_sum import find_target

class TestTargetedSum(unittest.TestCase):
    def test_find_target(self):
        self.assertEqual(find_target([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(find_target([3, 2, 4, 5], 6), [1, 2])
        self.assertEqual(find_target([1, 3, 5, 6, 7, 8], 15), [4, 5])
        self.assertEqual(find_target([1, 3, 5, 7], 14), 'Target not found')
