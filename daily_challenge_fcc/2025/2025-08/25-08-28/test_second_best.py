from second_best import get_laptop_cost
import unittest


class TestSecondBest(unittest.TestCase):
    def test_get_laptop_cost(self):
        self.assertEqual(get_laptop_cost([1500, 2000, 1800, 1400], 1900), 1800)
        self.assertEqual(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900), 1800)
        self.assertEqual(get_laptop_cost([2099, 1599, 1899, 1499], 2200), 1899)
        self.assertEqual(get_laptop_cost([2099, 1599, 1899, 1499], 1000), 0)
        self.assertEqual(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450), 1400)
