from biathlon import calculate_penalty_distance
import unittest


class TestBiathlon(unittest.TestCase):
    def test_calculate_penalty_distance(self):
        self.assertEqual(calculate_penalty_distance([4, 4]), 300)
        self.assertEqual(calculate_penalty_distance([5, 5]), 0)
        self.assertEqual(calculate_penalty_distance([4, 5, 3, 5]), 450)
        self.assertEqual(calculate_penalty_distance([5, 4, 5, 5]), 150)
        self.assertEqual(calculate_penalty_distance([4, 3, 0, 3]), 1500)


if __name__ == "__main__":
    unittest.main()
