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
        """Test US_ITIN functionality with various formats"""

        valid_itins = [
           "900-70-1234",
           "970-45-6789",
           "999-97-1111"
    ]

    # Positive test cases
        for itin in valid_itins:
            print(f"Testing valid ITIN format: '{itin}'")

            # Test the valid ITIN format
            result = analyze_text(f'My ITIN is {itin}', ['US_ITIN'])
            print(f"Result for 'My ITIN is {itin}': {result}")

               # Test the valid ITIN format
        result = analyze_text(f'My ITIN is {itin}', ['US_ITIN'])
        print(f"Result for 'My ITIN is {itin}': {result}")

        # Ensure result is not empty before accessing
        self.assertTrue(result, f"Expected a result for valid ITIN: {itin}")
        if result:
            self.assertEqual('US_ITIN', result[0].entity_type)
            

        # Test with a different phrase
        result = analyze_text(f'My abc is {itin}', ['US_ITIN'])
        print(f"Result for 'My abc is {itin}': {result}")

        # Ensure result is not empty before accessing
        self.assertTrue(result, f"Expected a result for valid ITIN: {itin} with different phrase")
        if result:
            self.assertEqual('US_ITIN', result[0].entity_type)
            

    # Negative test case
        invalid_input = '617-32-2222'
        result = analyze_text(invalid_input, ['US_ITIN'])
        print(f"Result for invalid ITIN '{invalid_input}': {result}")
        self.assertListEqual([], result, "Expected no result for invalid ITIN format.")
        
    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
