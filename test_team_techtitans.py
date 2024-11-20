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

    import unittest

def check_url(url):
    """Function to check if a URL contains potential PII, like a username or password."""
    # Define a simple check for common PII indicators in a URL
    pii_indicators = ["user=", "username=", "password="]
    return any(indicator in url for indicator in pii_indicators)

class TestURLFunctionality(unittest.TestCase):

    def test_url_with_pii(self):
        """Test case: URL containing PII parameters"""
        test_url = "http://www.test.com/pageName?user=RealName&Password=TheRealPassword123"
        expected = True
        actual = check_url(test_url)
        self.assertEqual(expected, actual, "Failed to detect PII in the URL")

    def test_url_without_pii(self):
        """Negative test case: URL without PII parameters"""
        negative_url = "http://www.testExample.com/page?param1=val1&param2=val2"
        expected = True
        actual = check_url(negative_url)
        self.assertNotEqual(expected, actual, "Incorrectly detected PII in a non-PII URL")

    def test_url_only_parameters(self):
        """Test case: URL without parameters that indicate PII"""
        parameter_test_url = "http://www.secret.com"
        expected = False
        actual = check_url(parameter_test_url)
        self.assertEqual(expected, actual, "Incorrectly detected PII in a URL with no parameters")

# Run the tests
if __name__ == "__main__":
    unittest.main()


    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality with various formats"""
        valid_itins = [
            "900-70-1234",
            "970-55-6789",
            "999-97-1111"]

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

        # Positive test case with a plain 9-digit passport number
        result = analyze_text("My passport is 140190332", ["US_PASSPORT"])
        print("Result for 'My passport is 140190332':", result)

        # Check that the result is not empty before accessing
        self.assertTrue(result, "Expected a US_PASSPORT entity but got no results.")
        if result:
            # Check entity type and confidence score for a weak pattern match
            self.assertEqual("US_PASSPORT", result[0].entity_type)
            self.assertEqual(0.4, result[0].score)  # Expected weak match score

        # Positive test case
        result = analyze_text("My is A12345678", ["US_PASSPORT"])
        print("Result for 'My is passport A12345678':", result)

        # Check that the result is not empty before accessing
        self.assertTrue(result, "Expected a US_PASSPORT entity but got no results.")
        if result:
            self.assertEqual("US_PASSPORT", result[0].entity_type)
            self.assertEqual(0.1, result[0].score)  # Expected next-gen weak match score

        # Negative test case
        result = analyze_text("My abc is 14019033", ["US_PASSPORT"])
        print("Result for 'My abc is 14019033':", result)

        self.assertFalse(result, "Expected no result for irrelevant context")


if __name__ == '__main__':
    unittest.main()
