from acronym_builder import build_acronym
import unittest

class TestBuildAcronym(unittest.TestCase):
    def test_build_acronym(self):
        self.assertEqual(build_acronym("Search Engine Optimization"), "SEO")
        self.assertEqual(build_acronym("Frequently Asked Questions"), "FAQ")
        self.assertEqual(build_acronym("National Aeronautics and Space Administration"), "NASA")
        self.assertEqual(build_acronym("Federal Bureau of Investigation"), "FBI")
        self.assertEqual(build_acronym("For your information"), "FYI")
        self.assertEqual(build_acronym("By the way"), "BTW")

if __name__ == '__main__':
    unittest.main()
