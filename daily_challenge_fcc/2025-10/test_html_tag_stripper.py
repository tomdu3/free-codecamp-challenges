import unittest
from html_tag_stripper import strip_tags

class TestStripTags(unittest.TestCase):
    def test_anchor(self):
        self.assertEqual(strip_tags('<a href="#">Click here</a>'), "Click here")

    def test_paragraph_and_bold(self):
        self.assertEqual(strip_tags('<p class="center">Hello <b>World</b>!</p>'), "Hello World!")

    def test_img_tag(self):
        self.assertEqual(strip_tags('<img src="cat.jpg" alt="Cat">'), "")

    def test_nested_sections(self):
        self.assertEqual(
            strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'),
            "sectionsection"
        )

    def test_empty_string(self):
        self.assertEqual(strip_tags(''), "")

    def test_no_tags(self):
        self.assertEqual(strip_tags('Just text'), "Just text")

    def test_self_closing_br(self):
        self.assertEqual(strip_tags('Hello<br>World'), "HelloWorld")

    def test_multiple_tags(self):
        self.assertEqual(strip_tags('<div><span>Test</span></div>'), "Test")

    def test_comment(self):
        self.assertEqual(strip_tags('<!-- comment -->Visible'), "Visible")

if __name__ == '__main__':
    unittest.main()