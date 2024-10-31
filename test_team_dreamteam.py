"""Unit test file for team dreamteam"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_dreamteam(unittest.TestCase):
    """Test team dreamteam PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        pre = ['123']
        mid = ['456']
        suf = ['785']

        # positive test cases
        for p in pre:
            for m in mid:
                for s in suf:
                    # check context score
                    acn = '-'.join([p,m,s])
                    print(acn)
                    result = analyze_text('My ACN is ' + acn, ['AU_ACN'])
                    print(result)
                    self.assertEqual('AU_ACN', result)
                    self.assertEqual(0.1, result[0].score)

                    # checks no context
                    result = analyze_text('My ACN is ' + acn, ['AU_ACN'])
                    self.assertEqual('AU_ACN', result)
                    self.assertEqual(0.01, result[0].score)

        # negative test cases
        result_invalid = analyze_text('My ACN is 123-456-789', ['AU-ACN'])
        self.assertEqual([], result_invalid)

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
