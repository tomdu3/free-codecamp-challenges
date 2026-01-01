import unittest
from spacejam import space_jam


class TestSpaceJam(unittest.TestCase):
    def test_space_jam(self):
        self.assertEqual(space_jam("freeCodeCamp"), "F  R  E  E  C  O  D  E  C  A  M  P")
        self.assertEqual(space_jam("   free   Code   Camp   "), "F  R  E  E  C  O  D  E  C  A  M  P")
        self.assertEqual(space_jam("Hello World?!"), "H  E  L  L  O  W  O  R  L  D  ?  !")
        self.assertEqual(space_jam("C@t$ & D0g$"), "C  @  T  $  &  D  0  G  $")
        self.assertEqual(space_jam("allyourbase"), "A  L  L  Y  O  U  R  B  A  S  E")
