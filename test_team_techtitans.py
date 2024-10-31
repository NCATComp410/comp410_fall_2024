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
                test_url = "http://www.test.com/pageName?user=RealName&Password=TheRealPassword123"
        expected = True
        actual = check_url(test_url)
        self.assertEqual(expected, actual)

        #Negative test case, doesn't have PII in URL
        negative_url = "http://www.testExample.com/page?param1=val1&param2=val2"
        expected = True
        actual = check_url(negative_url)
        self.assertNotEqual(expected, actual)

        #Test Case to make sure only parameters are included
        parameter_test_url = "http://www.secret.com"
        expected = False
        actual= check_url (parameter_test_url)
        self.assertEqual(expected, actual)

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

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
