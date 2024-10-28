"""Unit test file for team new_orleans_fc"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_new_orleans_fc(unittest.TestCase):
    """Test team new_orleans_fc PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card_positives(self):
        """Tests that credit card numbers are being detected as a CREDIT_CARD type"""
        # from https://support.bluesnap.com/docs/test-credit-card-numbers
        test_cases = {
            "VISA with dashes" : "4001-9192-5753-7193", 
            "VISA, whitespace" : "4001 9192 5753 7193",
            "VISA, no whitespace" : "4001919257537193",
            "A sentence with VISA credit card number" : "My credit card number is 4001919257537193",
            "A sentence with VISA card number" : "My card number is 4001919257537193",
            "A sentence about a VISA number" : "My number is 4001919257537193",
            "AMEX" : "374245455400126",
            "China Union Pay" : "6250941006528599",
            "ELO" : "6362970000457013",
            "Hipercard" : "6062826786276634",
            "JCB" : "3566000020000410",
            "Tarjeta Shopping" : "6034883265619896",
            "Mastercard" : "5425233430109903",
            "Discover" : "60115564485789458",
        }
        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input=test_input):
                # Analyze CREDIT_CARD entities only with our test_input.
                result = analyze_text(test_input, entity_list=["CREDIT_CARD"])
                # result is limited to return 1 item if a CREDIT_CARD match is found.
                # In python, anything other than False, None, [], or '' is truthful.
                # assertTrue will detect if len(result) is greater than or equal to 1.
                self.assertTrue(result, "Analyzer detected no credit card when it should've")
                self.assertEqual("CREDIT_CARD", result[0].entity_type)

    def test_credit_card_negative(self):
        """Tests that non-credit card numbers are not being detected as a CREDIT_CARD type"""
        # from https://support.bluesnap.com/docs/test-credit-card-numbers
        test_cases = {
            "Phone number" : "9192741111",
            "SSN" : "687098888",
            "US National Debt" : "35814215955888"
        }
        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input=test_input):
                # Analyze CREDIT_CARD entities only with our test_input.
                result = analyze_text(test_input, entity_list=["CREDIT_CARD"])
                # result will return [] if no results are found.
                # In Python, None, [], or '', etc are equivalent to False
                # assertFalse will catch if result is a falsy value (ex: [])
                self.assertFalse(result, "Analyzer detected credit card when it should not have")


    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
