from string_mirror import mirror
import unittest

class TestMirror(unittest.TestCase):
    def test1(self):
        self.assertEqual(mirror('freeCodeCamp'), 'freeCodeCamppmaCedoCeerf')
    def test2(self):
        self.assertEqual(mirror("RaceCar"), "RaceCarraCecaR")
    def test3(self):
        self.assertEqual(mirror("helloworld"), "helloworlddlrowolleh")
    def test4(self):
        self.assertEqual(mirror("The quick brown fox..."), "The quick brown fox......xof nworb kciuq ehT")


if __name__ == "__main__":
    unittest.main()
