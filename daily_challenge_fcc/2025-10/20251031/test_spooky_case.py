import unittest
from spooky_case import spookify

class TestSpookyCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(spookify("hello_world"), "HeLlO~wOrLd")
        
    def test_spooky_case(self):
        self.assertEqual(spookify("Spooky_Case"), "SpOoKy~CaSe")
        
    def test_trick_or_treat(self):
        self.assertEqual(spookify("TRICK-or-TREAT"), "TrIcK~oR~tReAt")
        
    def test_candy_bowl(self):
        self.assertEqual(spookify("c_a-n_d-y_-b-o_w_l"), "C~a~N~d~Y~~b~O~w~L")
        
    def test_haunted_house(self):
        self.assertEqual(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"), 
                        "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS")
        
    def test_empty_string(self):
        self.assertEqual(spookify(""), "")
        
    def test_single_char(self):
        self.assertEqual(spookify("a"), "A")
        
    def test_multiple_delimiters(self):
        self.assertEqual(spookify("boo-_-boo"), "BoO~~~bOo")

if __name__ == '__main__':
    unittest.main()