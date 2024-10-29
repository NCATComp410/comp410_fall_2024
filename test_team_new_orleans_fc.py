"""Unit test file for team new_orleans_fc"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_new_orleans_fc(unittest.TestCase):
    """Test team new_orleans_fc PII functions"""
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
    def test_email_address_positives(self):
        test_cases = {
            "Standard email": "user@example.com",
            "Email with subdomain": "user@mail.example.com",
            "Email with numbers": "user123@example.com",
            "Email with plus sign": "user+extra@example.com",
            "Email with dash": "user-name@example.com",
        }
        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input=test_input):
                result = analyze_text(test_input, entity_list=["EMAIL_ADDRESS"])

                self.assertTrue(result, "Analyzer detected no email")
                self.assertEqual("EMAIL_ADDRESS", result[0].entity_type)

        def test_email_address_negatives(self):
            """Tests that are non-email strings are not detected as EMAIL_ADDRESS type"""

            test_cases = {
                "Phone number": "336-291-1191",
                "Random text": "Just some random text",
                "Date format": "10/28/2024",
                "Alphanumeric string": "ABCD1234XYZ",
            }

            for test_description, test_input in test_cases.items():
                with self.subTest(msg=test_description, test_input=test_input):
                    result = analyze_text(test_input, entity_list=["EMAIL_ADDRESS"])

                    self.assertFalse(result, "Analyzer incorrectly detected an email address")
    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
