"""Unit test file for team new_orleans_fc"""
import unittest
# Assuming the recognizer is in the correct relative path as a module
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
                    self.assertEqual(0.4, result[0].score)
                    # check context should be 1.0
                    result = analyze_text('My DEA is ' + mln, ['MEDICAL_LICENSE'])
                    self.assertEqual('MEDICAL_LICENSE', result[0].entity_type)
                    self.assertEqual(1.0, result[0].score)

        #result = analyze_text("My USA DEA Certificate Number number is Tx4327537",['MEDICAL_LICENSE'])
        #print(result)
        #self.assertEqual('MEDICAL_LICENSE', result[0].entity_type)
        #self.assertEqual(1.0, result[0].score)

if __name__ == '__main__':
    unittest.main()
