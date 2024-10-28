"""Unit test file for team techtitans"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_techtitans(unittest.TestCase):
    """Test team techtitans PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""
        prefix = ['123', '456']
        mid = ['12']
        suffix = ['1234']

        result = analyze_text('My passport is 123456789', ['US_PASSPORT'])
        print(result)
        self.assertEqual('US_PASSPORT', result[0].entity_type)
        self.assertEqual(0.4, result[0].score)


if __name__ == '__main__':
    unittest.main()
