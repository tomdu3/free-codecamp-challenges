from figure_scating import compute_score
import unittest


class TestFigureSkating(unittest.TestCase):
    def test_compute_score(self):
        self.assertEqual(compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1), 64)
        self.assertEqual(compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 80)
        self.assertEqual(compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1), 67)
        self.assertEqual(compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0), 67.5)
        self.assertEqual(compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5), 59)


if __name__ == '__main__':
    unittest.main()
