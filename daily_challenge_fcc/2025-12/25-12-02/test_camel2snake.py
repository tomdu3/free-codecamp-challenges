import unittest
from camel2snake import to_snake
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

class TestCamel2Snake(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(to_snake("helloWorld"), "hello_world")
    def test_my_variable_name(self):
        self.assertEqual(to_snake("myVariableName"), "my_variable_name")
    def test_freecodecamp_daily_challenges(self):
        self.assertEqual(to_snake("freecodecampDailyChallenges"), "freecodecamp_daily_challenges")
    def test_hello_world_with_underscore(self):
        self.assertEqual(to_snake("hello_world"), "hello_world")
    def test_my_variable_name_with_underscore(self):
        self.assertEqual(to_snake("my_variable_name"), "my_variable_name")
    def test_freecodecamp_daily_challenges_with_underscore(self):
        self.assertEqual(to_snake("freecodecamp_daily_challenges"), "freecodecamp_daily_challenges")
