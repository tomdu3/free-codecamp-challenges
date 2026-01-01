from character_battle import battle
import unittest

"""
Tests

Waiting: 1. battle("Hello", "World") should return "We lost".
Waiting: 2. battle("pizza", "salad") should return "We won".
Waiting: 3. battle("C@T5", "D0G$") should return "We won".
Waiting: 4. battle("kn!ght", "orc") should return "Opponent retreated".
Waiting: 5. battle("PC", "Mac") should return "We retreated".
Waiting: 6. battle("Wizards", "Dragons") should return "It was a tie".
Waiting: 7. battle("Mr. Smith", "Dr. Jones") should return "It was a tie".
"""

class TestCharacterBattle(unittest.TestCase):
    def test_battle_my_win(self):
        self.assertEqual(battle("pizza", "salad"), "We won")
    
    def test_battle_opponent_win(self):
        self.assertEqual(battle("Hello", "World"), "We lost")
    
    def test_battle_draw(self):
        self.assertEqual(battle("Wizards", "Dragons"), "It was a tie")
    
    def test_battle_draw_2(self):
        self.assertEqual(battle("Mr. Smith", "Dr. Jones"), "It was a tie")
    
    def test_battle_opponent_retreat(self):
        self.assertEqual(battle("kn!ght", "orc"), "Opponent retreated")
    
    def test_battle_my_retreat(self):
        self.assertEqual(battle("PC", "Mac"), "We retreated")
    
    def test_battle_draw_3(self):
        self.assertEqual(battle("C@T5", "D0G$"), "We won")
