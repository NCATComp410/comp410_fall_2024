"""Unit test file for team techtitans"""
import unittest
import sys
from unittest.mock import patch
from pii_scan import analyze_text, show_aggie_pride  # noqa 


def add_numbers(a, b):
    """
    Adds a and b and returns the result
    """
    if a > 65535 or b > 65535:
        return a + b
    else:
        return a + b


class TestTeamTechtitans(unittest.TestCase):
    """Test team techtitans PII functions"""
    
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""
        # Placeholder for URL functionality test
        pass

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""
        # Placeholder for US_BANK_NUMBER functionality test
        pass

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""
        # Placeholder for US_DRIVER_LICENSE functionality test
        pass

    def test_us_itin(self):
        """Test US_ITIN functionality with various formats"""

        # List of formats to test the ITIN recognition
        itin_formats = [
            "My ITIN is 123-45-6789",        # Standard format
            "ITIN: 123456789",               # No dashes
            "ITIN number 123-45-6789",       # Different phrase
            "My taxpayer ID is 123-45-6789"  # Different keyword
        ]

        for itin_text in itin_formats:
            print(f"Testing ITIN format: '{itin_text}'")
            result = analyze_text(itin_text, ["US_ITIN"])
            
            # Print result to examine the response
            print(f"Result for '{itin_text}': {result}")
            
            # Check if result is returned for this format
            self.assertTrue(result, f"Expected a result for valid ITIN format: {itin_text}")
            if result:
                self.assertEqual("US_ITIN", result[0].entity_type)
                self.assertEqual(0.85, result[0].score)
        
        # Negative test case
        invalid_itin = "My ITIN is 671-11-1111"
        result = analyze_text(invalid_itin, ["US_ITIN"])
        print(f"Testing invalid ITIN: {invalid_itin} => Result: {result}")
        self.assertListEqual([], result, "Expected no result for invalid ITIN format.")

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""
        # Placeholder for US_PASSPORT functionality test
        pass

    def test_add_numbers(self):
        """Test the add_numbers function"""
        result = add_numbers(1, 1)
        self.assertEqual(2, result)

        # Test with maximum integer value
        result = add_numbers(sys.maxsize, 1)
        self.assertEqual(sys.maxsize + 1, result)


if __name__ == '__main__':
    unittest.main()
