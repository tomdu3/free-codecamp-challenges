import unittest
from signature_validaton import verify

class TestSignatureValidation(unittest.TestCase):

    def test_verify_foo_bar_57_returns_true(self):
        self.assertTrue(verify("foo", "bar", 57))

    def test_verify_foo_bar_54_returns_false(self):
        self.assertFalse(verify("foo", "bar", 54))

    def test_verify_freeCodeCamp_Rocks_238_returns_true(self):
        self.assertTrue(verify("freeCodeCamp", "Rocks", 238))

    def test_verify_is_this_valid_no_210_returns_false(self):
        self.assertFalse(verify("Is this valid?", "No", 210))

    def test_verify_is_this_valid_yes_233_returns_true(self):
        self.assertTrue(verify("Is this valid?", "Yes", 233))

    def test_verify_podcast_in_mobile_app_514_returns_true(self):
        self.assertTrue(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514))

if __name__ == '__main__':
    unittest.main()
