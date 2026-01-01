from message_decoder import decode
import unittest

"""
1. decode("Xlmw mw e wigvix qiwweki.", 4) should return "This is a secret message."
2. decode("Byffi Qilfx!", 20) should return "Hello World!"
3. decode("Zqd xnt njzx?", -1) should return "Are you okay?"
4. decode("oannLxmnLjvy", 9) should return "freeCodeCamp"
"""

class TestMessageDecoder(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(decode("Xlmw mw e wigvix qiwweki.", 4), "This is a secret message.")
        self.assertEqual(decode("Byffi Qilfx!", 20), "Hello World!")
        self.assertEqual(decode("Zqd xnt njzx?", -1), "Are you okay?")
        self.assertEqual(decode("oannLxmnLjvy", 9), "freeCodeCamp")