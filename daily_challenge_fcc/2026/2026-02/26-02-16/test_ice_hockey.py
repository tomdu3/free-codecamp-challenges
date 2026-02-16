from ice_hockey import get_semifinal_matchups
import unittest


class TestGetSemiFinalMatchups(unittest.TestCase):
    def test_get_semifinal_matchups(self):
        self.assertEqual(
            get_semifinal_matchups(
                [
                    "CAN: 2-2-0-1",
                    "FIN: 2-2-1-0",
                    "GER: 1-0-1-3",
                    "SUI: 0-1-3-1",
                    "SWE: 1-1-2-1",
                    "USA: 2-1-0-2",
                ]
            ),
            "The semi-final games will be FIN vs SWE and CAN vs USA.",
        )
        self.assertEqual(
            get_semifinal_matchups(
                [
                    "CAN: 2-1-1-1",
                    "CZE: 1-1-1-2",
                    "FIN: 1-2-1-1",
                    "NOR: 0-1-1-3",
                    "SLO: 1-0-1-3",
                    "USA: 5-0-0-0",
                ]
            ),
            "The semi-final games will be USA vs CZE and CAN vs FIN.",
        )
        self.assertEqual(
            get_semifinal_matchups(
                [
                    "CAN: 3-2-0-0",
                    "CZE: 2-1-2-0",
                    "LAT: 0-0-1-4",
                    "ITA: 1-1-1-2",
                    "DEN: 1-0-0-4",
                    "USA: 3-1-1-0",
                ]
            ),
            "The semi-final games will be CAN vs ITA and USA vs CZE.",
        )
        self.assertEqual(
            get_semifinal_matchups(
                [
                    "AUT: 2-2-1-0",
                    "DEN: 1-0-0-4",
                    "ITA: 1-1-1-2",
                    "JPN: 3-2-0-0",
                    "KOR: 2-1-2-0",
                    "LAT: 0-0-1-4",
                ]
            ),
            "The semi-final games will be JPN vs ITA and AUT vs KOR.",
        )


if __name__ == "__main__":
    unittest.main()
