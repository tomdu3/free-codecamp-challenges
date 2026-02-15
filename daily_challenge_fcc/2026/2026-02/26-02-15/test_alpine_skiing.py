from alpine_skiing import get_hill_rating
import unittest


class TestHillRating(unittest.TestCase):

    def test_waiting_1(self):
        self.assertEqual(get_hill_rating(95, 900, "Slalom"), "Green")

    def test_waiting_2(self):
        self.assertEqual(get_hill_rating(620, 2800, "Downhill"), "Black")

    def test_waiting_3(self):
        self.assertEqual(get_hill_rating(420, 1680, "Giant Slalom"), "Blue")

    def test_waiting_4(self):
        self.assertEqual(get_hill_rating(250, 3000, "Downhill"), "Green")

    def test_waiting_5(self):
        self.assertEqual(get_hill_rating(110, 900, "Slalom"), "Blue")

    def test_waiting_6(self):
        self.assertEqual(get_hill_rating(380, 1500, "Giant Slalom"), "Black")


if __name__ == "__main__":
    unittest.main()
