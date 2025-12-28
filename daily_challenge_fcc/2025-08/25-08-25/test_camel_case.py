from camel_case import to_camel_case 
import unittest

"""
Tests

Waiting: 1. to_camel_case("hello world") should return "helloWorld".
Waiting: 2. to_camel_case("HELLO WORLD") should return "helloWorld".
Waiting: 3. to_camel_case("secret agent-X") should return "secretAgentX".
Waiting: 4. to_camel_case("FREE cODE cAMP") should return "freeCodeCamp".
Waiting: 5. to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") should return "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk".
"""

class TestCamelCase(unittest.TestCase):
    def test_camel_case(self):
        self.assertEqual(to_camel_case("hello world"), "helloWorld")
        self.assertEqual(to_camel_case("HELLO WORLD"), "helloWorld")
        self.assertEqual(to_camel_case("secret agent-X"), "secretAgentX")
        self.assertEqual(to_camel_case("FREE cODE cAMP"), "freeCodeCamp")
        self.assertEqual(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"), "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk")