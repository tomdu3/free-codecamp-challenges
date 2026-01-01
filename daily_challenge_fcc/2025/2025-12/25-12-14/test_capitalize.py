from capitalize import title_case
import unittest


class TestTitleCase(unittest.TestCase):
    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")
        self.assertEqual(title_case("JAVASCRIPT AND PYTHON"), "Javascript And Python")
        self.assertEqual(title_case("AvOcAdO tOAst fOr brEAkfAst"), "Avocado Toast For Breakfast")
        
if __name__ == "__main__":
    unittest.main()
