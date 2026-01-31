from valid_pawn_moves import find_pawn_moves
import unittest

"""
Tests
Waiting:1. find_pawn_moves("D4") should return ["D5"].
Waiting:2. find_pawn_moves("B2") should return ["B3", "B4"].
Waiting:3. find_pawn_moves("A7") should return ["A8"].
Waiting:4. find_pawn_moves("G2") should return ["G3", "G4"].
Waiting:5. find_pawn_moves("E3") should return ["E4"].
"""

class TestFindPawnMoves(unittest.TestCase):
    def test_find_pawn_moves(self):
        self.assertEqual(find_pawn_moves("D4"), ["D5"])
        self.assertEqual(find_pawn_moves("B2"), ["B3", "B4"])
        self.assertEqual(find_pawn_moves("A7"), ["A8"])
        self.assertEqual(find_pawn_moves("G2"), ["G3", "G4"])
        self.assertEqual(find_pawn_moves("E3"), ["E4"])


if __name__ == "__main__":
    unittest.main()