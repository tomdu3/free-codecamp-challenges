import unittest
from string_count import count

class TestCountFunction(unittest.TestCase):
    def test_abcdefg_def(self):
        self.assertEqual(count('abcdefg', 'def'), 1)

    def test_hello_world(self):
        self.assertEqual(count('hello', 'world'), 0)

    def test_mississippi_iss(self):
        self.assertEqual(count('mississippi', 'iss'), 2)

    def test_she_sells_seashells_sh(self):
        self.assertEqual(count('she sells seashells by the seashore', 'sh'), 3)

    def test_101010101010101010101_101(self):
        self.assertEqual(count('101010101010101010101', '101'), 10)

    def test_empty_string(self):
        self.assertEqual(count('', 'a'), 0)

    def test_parameter_empty(self):
        self.assertEqual(count('abc', ''), 4)  # '' matches at every position + end

    def test_both_empty(self):
        self.assertEqual(count('', ''), 1)

    def test_no_occurrences(self):
        self.assertEqual(count('abcdef', 'xyz'), 0)

    def test_overlap(self):
        self.assertEqual(count('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()