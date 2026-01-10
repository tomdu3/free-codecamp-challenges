from tic_tac_toe import tic_tac_toe
import unittest


class TestTicTacToe(unittest.TestCase):
    def test_tic_tac_toe(self):
        self.assertEqual(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]), "X wins")
        self.assertEqual(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]), "O wins")
        self.assertEqual(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]), "Draw")
        self.assertEqual(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]), "O wins")
        self.assertEqual(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]), "X wins")
        self.assertEqual(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]), "Draw")

if __name__ == "__main__":
    unittest.main()