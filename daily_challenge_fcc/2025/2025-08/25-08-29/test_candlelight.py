from candlelight import burn_candles
import unittest

"""
Waiting: 1. burn_candles(7, 2) should return 13
Waiting: 2. burn_candles(10, 5) should return 12
Waiting: 3. burn_candles(20, 3) should return 29
Waiting: 4. burn_candles(17, 4) should return 22
Waiting: 5. burn_candles(2345, 3) should return 3517
"""

class TestCandlelight(unittest.TestCase):
    def test_burn_candles(self):
        self.assertEqual(burn_candles(7, 2), 13)
        self.assertEqual(burn_candles(10, 5), 12)
        self.assertEqual(burn_candles(20, 3), 29)
        self.assertEqual(burn_candles(17, 4), 22)
        self.assertEqual(burn_candles(2345, 3), 3517)

if __name__ == '__main__':
    unittest.main()
