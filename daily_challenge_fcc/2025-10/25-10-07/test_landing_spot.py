import unittest
from landing_spot import find_landing_spot

class TestLandingSpot(unittest.TestCase):

    def test_find_landing_spot_1(self):
        grid = [[1, 0], [2, 0]]
        self.assertEqual(find_landing_spot(grid), [0, 1])

    def test_find_landing_spot_2(self):
        grid = [[9, 0, 3], [7, 0, 4], [8, 0, 5]]
        self.assertEqual(find_landing_spot(grid), [1, 1])

    def test_find_landing_spot_3(self):
        grid = [[1, 2, 1], [0, 0, 2], [3, 0, 0]]
        self.assertEqual(find_landing_spot(grid), [2, 2])

    def test_find_landing_spot_4(self):
        grid = [[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]
        self.assertEqual(find_landing_spot(grid), [2, 1])

if __name__ == '__main__':
    unittest.main()
