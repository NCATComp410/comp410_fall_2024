"""Unit test file for team dreamteam"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_dreamteam(unittest.TestCase):
    """Test team dreamteam PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""

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
        pre = ['123']
        mid = ['456']
        suf = ['785']

        # positive test cases
        for p in pre:
            for m in mid:
                for s in suf:
                    # check context score
                    acn = '-'.join([p,m,s])
                    print(acn)
                    result = analyze_text('My ACN is ' + acn, ['AU_ACN'])
                    print(result)
                    self.assertEqual('AU_ACN', result)
                    self.assertEqual(0.1, result[0].score)

                    # checks no context
                    result = analyze_text('My ACN is ' + acn, ['AU_ACN'])
                    self.assertEqual('AU_ACN', result)
                    self.assertEqual(0.01, result[0].score)

        # negative test cases
        result_invalid = analyze_text('My ACN is 123-456-789', ['AU-ACN'])
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
