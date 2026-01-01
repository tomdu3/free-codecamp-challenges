from resolution_streak import resolution_streak
import unittest


class TestResolutionStreak(unittest.TestCase):
    def test_resolution_streak(self):
        self.assertEqual(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]), "Resolution on track: 3 day streak.")
        self.assertEqual(resolution_streak([[10000, 120, 5], [10950, 121, 11]]), "Resolution failed on day 2: 1 day streak.")
        self.assertEqual(resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]), "Resolution failed on day 3: 2 day streak.")
        self.assertEqual(resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]), "Resolution failed on day 4: 3 day streak.")
        self.assertEqual(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]), "Resolution on track: 10 day streak.")


if __name__ == '__main__':
    unittest.main()
