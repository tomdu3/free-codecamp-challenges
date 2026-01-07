from md_ul_parser import parse_unordered_list
import unittest



class TestMdUlParser(unittest.TestCase):
    def test_parse_unordered_list(self):
        self.assertEqual(parse_unordered_list("- Item A\n- Item B"), "<ul><li>Item A</li><li>Item B</li></ul>")
        self.assertEqual(parse_unordered_list("-  JavaScript\n-  Python"), "<ul><li>JavaScript</li><li>Python</li></ul>")
        self.assertEqual(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"), "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>")
        self.assertEqual(parse_unordered_list("- A-1\n- A-2\n- B-1"), "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>")

if __name__ == '__main__':
    unittest.main()
