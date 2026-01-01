from rps import rock_paper_scissors
import unittest

"""
Tests

Waiting: 1. rock_paper_scissors("Rock", "Rock") should return "Tie".
Waiting: 2. rock_paper_scissors("Rock", "Paper") should return "Player 2 wins".
Waiting: 3. rock_paper_scissors("Scissors", "Paper") should return "Player 1 wins".
Waiting: 4. rock_paper_scissors("Rock", "Scissors") should return "Player 1 wins".
Waiting: 5. rock_paper_scissors("Scissors", "Scissors") should return "Tie".
Waiting: 6. rock_paper_scissors("Scissors", "Rock") should return "Player 2 wins".
"""

class TestRockPaperScissors(unittest.TestCase):
    def test_rock_paper_scissors(self):
        self.assertEqual(rock_paper_scissors("Rock", "Rock"), "Tie")
        self.assertEqual(rock_paper_scissors("Rock", "Paper"), "Player 2 wins")
        self.assertEqual(rock_paper_scissors("Scissors", "Paper"), "Player 1 wins")
        self.assertEqual(rock_paper_scissors("Rock", "Scissors"), "Player 1 wins")
        self.assertEqual(rock_paper_scissors("Scissors", "Scissors"), "Tie")
        self.assertEqual(rock_paper_scissors("Scissors", "Rock"), "Player 2 wins")

if __name__ == '__main__':
    unittest.main()
