import unittest
from ball_trajectory import get_next_location


class TestBallTrajectory(unittest.TestCase):
    def test_get_next_location(self):
        self.assertEqual(get_next_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 2, 0], [0, 0, 0, 0]]), [2, 3])
        self.assertEqual(get_next_location([[0, 0, 0, 0], [0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 0, 0]]), [3, 0])
        self.assertEqual(get_next_location([[0, 2, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), [1, 2])
        self.assertEqual(get_next_location([[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 1, 0, 0]]), [1, 1])
        self.assertEqual(get_next_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 2]]), [2, 2])

