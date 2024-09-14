"""Unit test file for Team Teamnew_orleans_fc"""
import unittest
from pii_scan import analyze_text, show_aggie_pride


class TestTeamnew_orleans_fc(unittest.TestCase):
    """Test the Team Teamnew_orleans_fc PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""
