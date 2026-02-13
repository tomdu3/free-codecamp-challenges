from luge import get_fastest_speed
import unittest


class TestLuge(unittest.TestCase):

    def test_get_fastest_speed(self):
        self.assertEqual(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]), "The luger's fastest speed was 35.07 m/s on segment 5.")
        self.assertEqual(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]), "The luger's fastest speed was 37.75 m/s on segment 2.")
        self.assertEqual(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]), "The luger's fastest speed was 38.49 m/s on segment 3.")
        self.assertEqual(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]), "The luger's fastest speed was 37.69 m/s on segment 1.")
        self.assertEqual(get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]), "The luger's fastest speed was 39.24 m/s on segment 4.")

if __name__ == '__main__':
    unittest.main()

