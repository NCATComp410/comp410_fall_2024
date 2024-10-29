"""Unit test file for team tech_bros"""
import re
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_tech_bros(unittest.TestCase):
    """Test team tech_bros PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""
        # Valid examples
        valid_passports = ["JF3349917", "AB1234567", "ea1213002"]
        
        # Invalid examples
        invalid_passports = ["J3349917", "JF334991", "J#3349917", "JF 3349917", "ABC1234567", "12AB3456789", "99ABCDEFG", "12ABC5678"]
        
        # Test valid passports
        for passport in valid_passports:
            with self.subTest(passport=passport):
                # Use Italian for passport to increase the score
                result = analyze_text(f"My passaporto number is {passport}", ['IT_PASSPORT'])
                print(result)
                self.assertEqual('IT_PASSPORT', result[0].entity_type)
                self.assertAlmostEqual(0.4, result[0].score, places=2)

        # Test invalid passports
        for passport in invalid_passports:
            with self.subTest(passport=passport):
                result = analyze_text(f"My passaporto number is {passport}", ['IT_PASSPORT'])
                self.assertListEqual([], result)

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
