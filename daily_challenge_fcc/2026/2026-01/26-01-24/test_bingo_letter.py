from bingo_letter import get_bingo_letter
import unittest


class TestBingoLetter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_bingo_letter(75), "O")

    def test_2(self):
        self.assertEqual(get_bingo_letter(54), "G")

    def test_3(self):
        self.assertEqual(get_bingo_letter(25), "I")

    def test_4(self):
        self.assertEqual(get_bingo_letter(38), "N")

    def test_5(self):
        self.assertEqual(get_bingo_letter(11), "B")


if __name__ == "__main__":
    unittest.main()
