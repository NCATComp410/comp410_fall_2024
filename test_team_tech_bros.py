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
        # Testing with context and valid fiscal code
        fiscal_code = 'RSSMRA85M01H501Z'  # Example of a valid Italian Fiscal Code
        result = analyze_text('Il mio codice fiscale è ' + fiscal_code, ['IT_FISCAL_CODE'])
        print(result)
        self.assertEqual('IT_FISCAL_CODE', result[0].entity_type)
        self.assertEqual(0.80, result[0].score)  # Adjust score as expected based on analyze_text behavior

        # Testing without context and an invalid fiscal code
        invalid_fiscal_code = '1234XYZ'
        result = analyze_text('Il mio codice è ' + invalid_fiscal_code, ['IT_FISCAL_CODE'])
        print(result)
        self.assertListEqual([], result)  # Expect no entities detected due to invalid format


    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
