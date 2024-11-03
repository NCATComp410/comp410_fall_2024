"""Unit test file for team dreamteam"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_dreamteam(unittest.TestCase):
    """Test team dreamteam PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number_positives(self):
        """Test ABA_Routing_Number positives functionality"""
        # Positive test case with valid ABA routing numbers
        valid_aba_routing_numbers = {
            "SECU" : "253177049",
            "Wells Fargo" : "053000219",
            "Truist" : "083974289",
            "Bank of America" : "053000196",
        }

        for test_description, test_input in valid_aba_routing_numbers.items():
            with self.subTest(msg=test_description, test_input=test_input):
                # Analyze ABA_Routing_Number entities with valid routing number
                result = analyze_text(test_input, entity_list=["ABA_ROUTING_NUMBER"])
                # Check that an ABA_Routing_Number entity was detected.
                self.assertTrue(result, "Analyzer detected no routing number when it should've")
                self.assertEqual("ABA_ROUTING_NUMBER", result[0].entity_type)

    def test_aba_routing_number_negatives(self):
        """Test ABA_Routing_Number negatives functionality"""
        # Negative test case with invalid ABA routing numbers
        invalid_aba_routing_numbers = {
            "Random Numbers" : "123456789",
            "Less than 9 digits" : "1456",
            "Invalid starting digits" : "991234567",
            "Random Numbers with text" : "12233W433",
        }

        for test_description, test_input in invalid_aba_routing_numbers.items():
            with self.subTest(msg=test_description, test_input=test_input):
                result = analyze_text(test_input, entity_list=["ABA_ROUTING_NUMBER"])
                print(result)
                self.assertFalse(result, "Analyzer incorrectly detected a routing number")

    def test_au_abn(self):
        """Test AU_ABN functionality"""

        # Positive test case with context and proper formatting
        result = analyze_text('Our company ABN is 51 824 753 556.', ['AU_ABN'])
        self.assertEqual('AU_ABN', result[0].entity_type)
        self.assertEqual(1.0, result[0].score)  # High confidence due to context and correct formatting

        # Negative test case with invalid ABN (checksum fails)
        result = analyze_text('My ABN is 51 824 753 557.', ['AU_ABN'])
        self.assertEqual([], result)  # Should not match due to invalid checksum

        # Note:
        # The confidence score for AU_ABN is binary:
        # - If the ABN passes checksum validation, the confidence score is set to 1.0.
        # - If the ABN fails validation, it is not detected at all.
        # This is because the Presidio Analyzer sets the confidence score to 1.0 when validation passes
        # and removes the entity when validation fails. For AU_ABN, checksum validation is crucial to
        # ensure that only valid ABNs are detected with high confidence.

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        # 005 499 981
        pre = ['005']
        mid = ['499']
        suf = ['981']

        # positive test cases
        for p in pre:
            for m in mid:
                for s in suf:
                    # check context score
                    acn = ' '.join([p, m, s])
                    text = 'My ACN is ' + acn
                    print(text)
                    result = analyze_text(text, ['AU_ACN'])
                    print(result)
                    self.assertEqual('AU_ACN', result[0].entity_type)
                    self.assertEqual(1.0, result[0].score)

                    # checks no context
                    result = analyze_text('My num is ' + acn, ['AU_ACN'])
                    self.assertEqual('AU_ACN', result[0].entity_type)
                    # Validation score is 1.0 even if there is no context for AU_ACN
                    self.assertEqual(1.0, result[0].score)

        # negative test cases
        result_invalid = analyze_text('My ACN is 123-456-789', ['AU_ACN'])
        self.assertEqual([], result_invalid)

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""
        #Positive test case
        result = analyze_text('My medicare number is 3854 72631 5', ['AU_MEDICARE'])
        print(result)
        
        #Negative test case
        invalid_result = analyze_text("My AU medical number is 1H34 56789 1", ['AU_MEDICARE'])
        print(invalid_result)
        self.assertEqual([], invalid_result)

    def test_au_tfn(self):
        """Test AU_TFN functionality"""
        # Positive test case
        result = analyze_text(' My TFN is 123 456 789', ['AU_TFN'])
        print(result)

        # Negative test case
        result_invalid = analyze_text('My TFM is 4321 8765', ['AU_TFN'])
        print(result_invalid)
        self.assertEqual(result_invalid, [])
    


if __name__ == '__main__':
    unittest.main()
