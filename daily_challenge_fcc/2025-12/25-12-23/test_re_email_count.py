from re_email_count import email_chain_count
import unittest

class TestEmailChainCount(unittest.TestCase):
    def test_1(self):
        self.assertEqual(email_chain_count("Re: Meeting Notes"), 1)

    def test_2(self):
        self.assertEqual(email_chain_count("Meeting Notes"), 0)

    def test_3(self):
        self.assertEqual(email_chain_count("Re: re: RE: rE: Meeting Notes"), 4)

    def test_4(self):
        self.assertEqual(email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes"), 5)

    def test_5(self):
        self.assertEqual(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"), 23)

