from consonant_case import to_consonant_case
import unittest

"""
Tests
Waiting:1. to_consonant_case("helloworld") should return "HeLLoWoRLD".
Waiting:2. to_consonant_case("HELLOWORLD") should return "HeLLoWoRLD".
Waiting:3. to_consonant_case("_hElLO-WOrlD-") should return "_HeLLo_WoRLD_".
Waiting:4. to_consonant_case("_~-generic_~-variable_~-name_~-here-~_") should return "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_".
"""


class TestToConsonantCase(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(to_consonant_case("helloworld"), "HeLLoWoRLD")
        self.assertEqual(to_consonant_case("HELLOWORLD"), "HeLLoWoRLD")
        self.assertEqual(to_consonant_case("_hElLO-WOrlD-"), "_HeLLo_WoRLD_")
        self.assertEqual(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"), "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_")


if __name__ == '__main__':
    unittest.main()
