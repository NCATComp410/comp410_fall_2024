"""Unit test file for Team Teamtech_baddies"""
import unittest
from pii_scan import analyze_text, show_aggie_pride


class TestTeamtech_baddies(unittest.TestCase):
    """Test the Team Teamtech_baddies PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

    def test_in_pan(self):
        """Test IN_PAN functionality"""

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""
