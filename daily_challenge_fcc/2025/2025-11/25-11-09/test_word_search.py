import unittest
from word_search import find_word

class TestFindWord(unittest.TestCase):
    def test_find_word_cat(self):
        board = [
            ["a", "c", "t"],
            ["t", "a", "t"],
            ["c", "t", "c"],
        ]
        self.assertEqual(find_word(board, "cat"), [[0, 1], [2, 1]])

    def test_find_word_dog(self):
        board = [
            ["d", "o", "g"],
            ["o", "g", "d"],
            ["d", "g", "o"],
        ]
        self.assertEqual(find_word(board, "dog"), [[0, 0], [0, 2]])

    def test_find_word_fish(self):
        board = [
            ["h", "i", "s", "h"],
            ["i", "s", "f", "s"],
            ["f", "s", "i", "i"],
            ["s", "h", "i", "f"],
        ]
        self.assertEqual(find_word(board, "fish"), [[3, 3], [0, 3]])

    def test_find_word_fox(self):
        board = [
            ["f", "x", "o", "x"],
            ["o", "x", "o", "f"],
            ["f", "o", "f", "x"],
            ["f", "x", "x", "o"],
        ]
        self.assertEqual(find_word(board, "fox"), [[1, 3], [1, 1]])


if __name__ == "__main__":
    unittest.main()