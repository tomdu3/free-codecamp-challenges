from snowboarding import get_landing_stance
import unittest


class TestSnowboarding(unittest.TestCase):
    def test_get_landing_stance(self):
        self.assertEqual(get_landing_stance("Regular", 90), "Regular")
        self.assertEqual(get_landing_stance("Regular", 180), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", -270), "Regular")
        self.assertEqual(get_landing_stance("Regular", 2340), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", 2160), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", -540), "Regular")

if __name__ == '__main__':
    unittest.main()
