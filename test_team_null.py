"""Unit test file for Team Teamnull"""
import unittest
from pii_scan import analyze_text, show_aggie_pride


class TestTeamnull(unittest.TestCase):
    """Test the Team Teamnull PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
