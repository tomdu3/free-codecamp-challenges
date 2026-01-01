from reverse_sentence import reverse_sentence
import unittest

class TestReverseSentence(unittest.TestCase):
    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence("world hello"), "hello world")
        self.assertEqual(reverse_sentence("push commit git"), "git commit push")
        self.assertEqual(reverse_sentence("npm  install   apt    sudo"), "sudo apt install npm")
        self.assertEqual(reverse_sentence("import    default   function  export"), "export function default import")

if __name__ == "__main__":
    unittest.main()