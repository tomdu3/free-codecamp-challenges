from game_of_life import game_of_life
import unittest

class TestGameOfLife(unittest.TestCase):
    def test_game_of_life(self):
        self.assertEqual(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]), [[0, 1, 1], [0, 0, 1], [1, 1, 1]])
        self.assertEqual(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]), [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]])
        self.assertEqual(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]), [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]])


if __name__ == "__main__":
    unittest.main()