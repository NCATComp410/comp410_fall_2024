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

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""
        # Positive test case
        result = analyze_text(' My TFN is 123 456 789', ['AU_TFN'])
        print(result)

        # Negative test case
        result_invalid = analyze_text('My TFM is 4321 8765', ['AU_TFN'])
        print(result_invalid)
        self.assertEqual(result_invalid, [])

if __name__ == '__main__':
    unittest.main()
