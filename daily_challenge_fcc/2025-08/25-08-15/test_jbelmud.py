import unittest
from jbelmud import jbelmu

class TestJbelmu(unittest.TestCase):
    def test_jbelmu(self):
        self.assertEqual(jbelmu("hello world"), "hello wlord")
        self.assertEqual(jbelmu("i love jumbled text"), "i love jbelmud text")
        self.assertEqual(jbelmu("freecodecamp is my favorite place to learn to code"), "faccdeeemorp is my faiortve pacle to laern to cdoe")
        self.assertEqual(jbelmu("the quick brown fox jumps over the lazy dog"), "the qciuk borwn fox jmpus oevr the lazy dog")
