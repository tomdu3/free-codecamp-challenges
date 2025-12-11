from md_bold2 import parse_bold
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(parse_bold("**This is bold**"), "<b>This is bold</b>")
    
    def test_2(self):
        self.assertEqual(parse_bold("__This is also bold__"), "<b>This is also bold</b>")
    
    def test_3(self):
        self.assertEqual(parse_bold("**This is not bold **"), "**This is not bold **")
    
    def test_4(self):
        self.assertEqual(parse_bold("__ This is also not bold__"), "__ This is also not bold__")
    
    def test_5(self):
        self.assertEqual(
            parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."),
            "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog."
            )

if __name__ == "__main__":
    unittest.main()
