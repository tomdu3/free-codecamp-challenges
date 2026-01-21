from md_inline_code import parse_inline_code
import unittest


class TestMdInlineCode(unittest.TestCase):

    def test_parse_inline_code(self):
        self.assertEqual(parse_inline_code("Use `let` to declare the variable."), "Use <code>let</code> to declare the variable.")
        self.assertEqual(parse_inline_code("Use `let` or `const` to declare a variable."), "Use <code>let</code> or <code>const</code> to declare a variable.")
        self.assertEqual(parse_inline_code("Run `npm install` then `npm start`."), "Run <code>npm install</code> then <code>npm start</code>.")

if __name__ == '__main__':
    unittest.main()

