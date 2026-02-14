from skeleton import get_difficulty
import unittest


class TestGetDifficulty(unittest.TestCase):
    def test_difficulty(self):
        self.assertEqual(get_difficulty("SLSLLSRRLSRLRL"), "Easy")
        self.assertEqual(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"), "Hard")
        self.assertEqual(get_difficulty("SRRRRLSLLRLRSSRLSRL"), "Medium")
        self.assertEqual(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"), "Hard")
        self.assertEqual(get_difficulty("SLLSSLRLSLSLRSLSSLRL"), "Medium")
        self.assertEqual(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"), "Easy")


if __name__ == "__main__":
    unittest.main()
