from vowel_case import vowel_case
import unittest


class TestVowelCase(unittest.TestCase):
    def test_vowel_case(self):
        self.assertEqual(vowel_case("vowelcase"), "vOwElcAsE")
        self.assertEqual(vowel_case("coding is fun"), "cOdIng Is fUn")
        self.assertEqual(vowel_case("HELLO, world!"), "hEllO, wOrld!")
        self.assertEqual(vowel_case("git cherry-pick"), "gIt chErry-pIck")
        self.assertEqual(vowel_case("HEAD~1"), "hEAd~1")

if __name__ == '__main__':
    unittest.main()
