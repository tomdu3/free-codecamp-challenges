from md_a_parser import parse_link
import unittest


class TestMdAParser(unittest.TestCase):
    def test_parse_link(self):
        self.assertEqual(parse_link("[freeCodeCamp](https://freecodecamp.org/)"), '<a href="https://freecodecamp.org/">freeCodeCamp</a>')
        self.assertEqual(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"), '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>')
        self.assertEqual(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"), '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>')

if __name__ == '__main__':
    unittest.main()
