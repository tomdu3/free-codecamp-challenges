from checkerboard import create_board
import unittest


class TestCheckerboard(unittest.TestCase):

    def test_create_board_1(self):
        self.assertEqual(create_board([3, 3]), [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])

    def test_create_board_2(self):
        self.assertEqual(create_board([6, 1]), [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]])

    def test_create_board_3(self):
        self.assertEqual(create_board([2, 10]), [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]])

    def test_create_board_4(self):
        self.assertEqual(create_board([5, 4]), [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]])

if __name__ == "__main__":
    unittest.main()
