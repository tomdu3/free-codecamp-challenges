from par_hole import golf_score
import unittest


class TestGolfScore(unittest.TestCase):
    def test_par(self):
        self.assertEqual(golf_score(3, 3), "Par")

    def test_birdie(self):
        self.assertEqual(golf_score(4, 3), "Birdie")

    def test_hole(self):
        self.assertEqual(golf_score(3, 1), "Hole in one!")

    def test_double_bogey(self):
        self.assertEqual(golf_score(5, 7), "Double bogey")

    def test_bogey(self):
        self.assertEqual(golf_score(4, 5), "Bogey")

    def test_eagle(self):
        self.assertEqual(golf_score(5, 3), "Eagle")

if __name__ == '__main__':
    unittest.main()
