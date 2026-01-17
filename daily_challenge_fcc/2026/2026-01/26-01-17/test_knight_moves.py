from knight_moves import knight_moves
import unittest


class TestKnightMoves(unittest.TestCase):
    def test_knight_moves(self):
        self.assertEqual(knight_moves("A1"), 2)
        self.assertEqual(knight_moves("D4"), 8)
        self.assertEqual(knight_moves("G6"), 6)
        self.assertEqual(knight_moves("B8"), 3)
        self.assertEqual(knight_moves("H3"), 4)

if __name__ == '__main__':
    unittest.main()
