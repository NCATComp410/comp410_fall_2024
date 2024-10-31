"""Unit test file for team tech_bros"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 



class TestTeam_tech_bros(unittest.TestCase):
    """Test team tech_bros PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

        #Step 1: Sample Text resembling Italian ID Information
        sample_text = "Mario Rossi, Carta d'identità: AY1234567, issued in Rome"

        #Step 2: Specify the Italian ID Entity Type
        entity_type = "IT_IDENTITY_CARD"

        #Step 3: Run the analysis
        results = analyze_text(sample_text, [entity_type])

        #Step 4: Check the results
        self.assertTrue(results[0].entity_type == entity_type, "Italian ID Card was not detected")

        # Check the score
        self.assertEqual(0.4, results[0].score)

        #Negative Test Case
        sample_text = "Mario Rossi, Codice Fiscale: CF1234A567B, issued in Rome"
        results = analyze_text(sample_text, [entity_type])
        self.assertFalse(any(result.entity_type == entity_type for result in results), "Italian ID Card was incorrectly detected")


    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
