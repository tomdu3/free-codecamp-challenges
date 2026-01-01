from md_img_parser import parse_image
import unittest
"""
Waiting: 1. parse_image("![Cute cat](cat.png)") should return '<img src="cat.png" alt="Cute cat">'.
Waiting: 2. parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)") should return '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">'.
Waiting: 3. parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)") should return '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">'.
"""

class TestMdImgParser(unittest.TestCase):
    def test_parse_image(self):
        self.assertEqual(parse_image("![Cute cat](cat.png)"), '<img src="cat.png" alt="Cute cat">')
        self.assertEqual(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)"), '<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">')
        self.assertEqual(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)"), '<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">')

if __name__ == '__main__':
    unittest.main()
