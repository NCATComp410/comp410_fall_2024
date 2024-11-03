"""Unit test file for team new_orleans_fc"""
import unittest
# Assuming the recognizer is in the correct relative path as a module
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

    def test_crypto_positives(self):
        """Tests that valid Bitcoin addresses are being detected as a CRYPTO type"""
        # test addresses from https://bitcoin.design/guide/glossary/address/
        # Bitcoin addresses follow a certain pattern, even aside from their first character
        test_cases = {
            "P2TR (Taproot)": "bc1p5d7rjq7g6rdk2yhzks9smlaqtedr4dekq08ge8ztwac72sfr9rusxg3297",
            "P2WPKH (SegWit)": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
            "P2SH (Script)": "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
            "P2PKH (Legacy)": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
        }

        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input = test_input):
                result = analyze_text(test_input, entity_list=["CRYPTO"])
                self.assertTrue(result, "Analyzer detected no CRYPTO when it should've")
                self.assertEqual("CRYPTO", result[0].entity_type)

    def test_crypto_negatives(self):
        """Tests that invalid Bitcoin addresses are not detected as a CRYPTO type"""
        # some values borrowed from credit card and date time tests.
        test_cases = {
            "35 Zeroes": "00000000000000000000000000000000000",
            "27 A's": "AAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "Visa Credit Card Number": "4001919257537193",
            "ISO Formatted Date": "2023-10-28T15:45:00",
        }

        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input = test_input):
                result = analyze_text(test_input, entity_list=["CRYPTO"])
                self.assertFalse(result,
                                 "Analyzer detected Bitcoin address on non-Bitcoin address value.")

    def test_date_time_positives(self):
        """Tests that date/time strings are being detected as a DATE_TIME type"""

        # Example date/time formats to test
        test_cases = {
            "ISO format": "2023-10-28T15:45:00",
            "Date with slashes": "10/28/2023",
            "Date with dashes": "2023-10-28",
            "Short date format": "10/28/23",
        }
        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input=test_input):
                # Analyze DATE_TIME entities only with test_input.
                result = analyze_text(test_input, entity_list=["DATE_TIME"])
                # Check that a DATE_TIME entity was detected.
                self.assertTrue(result, "Analyzer detected no date/time when it should've")
                self.assertEqual("DATE_TIME", result[0].entity_type)


    def test_date_time_negatives(self):
        """Tests that non-date/time strings are not detected as DATE_TIME type"""
        # Non-date/time examples to ensure they are not detected as DATE_TIME
        test_cases = {
            "Phone number": "336-291-1191",
            "Credit card": "4001 9192 5753 7193",
            "Alphanumeric code": "ABC123XYZ",
        }
        for test_description, test_input in test_cases.items():
            with self.subTest(msg=test_description, test_input=test_input):
                # Analyze DATE_TIME entities only with our test_input.
                result = analyze_text(test_input, entity_list=["DATE_TIME"])
                # Check that no DATE_TIME entity was detected.
                self.assertFalse(result, "Analyzer detected date/time when it should not have")

    def test_email_address_positives(self):
        """Test EMAIL_ADDRESS positive functionality"""
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
        prefix = ['T9','Ca']
        mid = ['4327']
        suffix = ['537']

        # positive test cases
        for p in prefix:
            for m in mid:
                for s in suffix:
                    mln = ''.join([p,m,s])
                    # check no context score should be 0.4
                    result = analyze_text('' + mln, ['MEDICAL_LICENSE'])
                    print(result)
                    self.assertEqual('MEDICAL_LICENSE', result[0].entity_type)
                    self.assertEqual(1.0, result[0].score)
                    # check context should be 1.0
                    result = analyze_text('My DEA Certificate number is ' + mln, ['MEDICAL_LICENSE'])
                    self.assertEqual('MEDICAL_LICENSE', result[0].entity_type)
                    self.assertEqual(1.0, result[0].score)

        # negative test cases

        result = analyze_text("My USA DEA Certificate Number number is Tx432757",['MEDICAL_LICENSE'])
        self.assertListEqual([],result)
        #print(result)
        #self.assertEqual('MEDICAL_LICENSE', result[0].entity_type)
        #self.assertEqual(1.0, result[0].score)

if __name__ == '__main__':
    unittest.main()
