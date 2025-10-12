import unittest
from battle_words import battle

class TestBattle(unittest.TestCase):
    def test_hello_world_vs_hello_word(self):
        self.assertEqual(battle("hello world", "hello word"), "We win")

    def test_Hello_world_vs_hello_world(self):
        self.assertEqual(battle("Hello world", "hello world"), "We win")

    def test_lorem_ipsum_vs_kitty_ipsum(self):
        self.assertEqual(battle("lorem ipsum", "kitty ipsum"), "We lose")

    def test_hello_world_vs_world_hello(self):
        self.assertEqual(battle("hello world", "world hello"), "Draw")

    def test_git_checkout_vs_git_switch(self):
        self.assertEqual(battle("git checkout", "git switch"), "We win")

    def test_Cheeseburger_with_fries_vs_Cheeseburger_with_Fries(self):
        self.assertEqual(battle("Cheeseburger with fries", "Cheeseburger with Fries"), "We lose")

    def test_We_must_never_surrender_vs_Our_team_must_win(self):
        self.assertEqual(battle("We must never surrender", "Our team must win"), "Draw")

    # Additional tests
    def test_identical_strings(self):
        self.assertEqual(battle("abc", "abc"), "Draw")

    def test_empty_strings(self):
        self.assertEqual(battle("", ""), "Draw")

    
if __name__ == "__main__":
    unittest.main()