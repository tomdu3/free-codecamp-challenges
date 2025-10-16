import unittest
from email_validator import validate

class TestEmailValidator(unittest.TestCase):
    def test_valid_simple(self):
        self.assertTrue(validate("a@b.cd"))

    def test_valid_complex_local(self):
        self.assertTrue(validate("hell.-w.rld@example.com"))

    def test_invalid_local_starts_with_dot(self):
        self.assertFalse(validate(".b@sh.rc"))

    def test_invalid_tld_with_digit(self):
        self.assertFalse(validate("example@test.c0"))

    def test_missing_at_symbol(self):
        self.assertFalse(validate("freecodecamp.org"))

    def test_valid_special_local(self):
        self.assertTrue(validate("develop.ment_user@c0D!NG.R.CKS"))

    def test_invalid_local_ends_with_dot(self):
        self.assertFalse(validate("hello.@wo.rld"))

    def test_invalid_domain_double_dot(self):
        self.assertFalse(validate("hello@world..com"))

    def test_invalid_multiple_at(self):
        self.assertFalse(validate("git@commit@push.io"))

    # Additional tests
    def test_invalid_local_double_dot(self):
        self.assertFalse(validate("ab..cd@domain.com"))

    def test_invalid_domain_starts_with_dot(self):
        self.assertFalse(validate("abc@.domain.com"))

    def test_invalid_domain_ends_with_dot(self):
        self.assertFalse(validate("abc@domain.com."))

    def test_invalid_local_with_space(self):
        self.assertFalse(validate("ab c@domain.com"))

    def test_invalid_domain_with_space(self):
        self.assertFalse(validate("abc@dom ain.com"))

    def test_valid_long_local_and_domain(self):
        self.assertTrue(validate("a_b-c.d@sub.domain.co.uk"))

    def test_invalid_tld_too_short(self):
        self.assertFalse(validate("abc@domain.c"))

    def test_invalid_tld_with_special(self):
        self.assertFalse(validate("abc@domain.c!m"))

    def test_valid_local_with_underscore_and_hyphen(self):
        self.assertTrue(validate("a_b-c@domain.com"))

    def test_invalid_local_ends_with_hyphen(self):
        self.assertTrue(validate("abc-@domain.com"))  # Hyphen allowed at end

    def test_invalid_domain_double_dot_in_middle(self):
        self.assertFalse(validate("abc@do..main.com"))

if __name__ == "__main__":
    unittest.main()