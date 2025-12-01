import unittest
from email_sorter import sort

class TestEmailSorter(unittest.TestCase):
    def test_basic_sort(self):
        emails = ["jill@mail.com", "john@example.com", "jane@example.com"]
        expected = ["jane@example.com", "john@example.com", "jill@mail.com"]
        self.assertEqual(sort(emails), expected)
        
    def test_sort_different_domains(self):
        emails = ["bob@mail.com", "alice@zoo.com", "carol@mail.com"]
        expected = ["bob@mail.com", "carol@mail.com", "alice@zoo.com"]
        self.assertEqual(sort(emails), expected)
        
    def test_sort_same_user(self):
        emails = ["user@z.com", "user@y.com", "user@x.com"]
        expected = ["user@x.com", "user@y.com", "user@z.com"]
        self.assertEqual(sort(emails), expected)
        
    def test_sort_case_insensitive(self):
        emails = ["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]
        expected = ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"]
        self.assertEqual(sort(emails), expected)
        
    def test_sort_complex_case(self):
        emails = ["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", 
                 "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]
        expected = ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com",
                   "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"]
        self.assertEqual(sort(emails), expected)

if __name__ == '__main__':
    unittest.main()