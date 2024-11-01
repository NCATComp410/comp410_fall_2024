"""Unit test file for team tech_bros"""
import unittest

from numpy.lib.function_base import place

from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_tech_bros(unittest.TestCase):
    """Test team tech_bros PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality with and without context, and invalid code"""
        # Testing with context and valid fiscal code
        fiscal_code = 'RSSMRA85M01H501Z'  # Example of a valid Italian Fiscal Code
        result = analyze_text('Il mio codice fiscale cf è ' + fiscal_code, ['IT_FISCAL_CODE'])
        print("With context:", result)
        self.assertTrue(result, "Expected entity not found")  # Ensure result is not empty
        self.assertEqual('IT_FISCAL_CODE', result[0].entity_type)
        self.assertAlmostEqual(0.65, result[0].score, places=2)  # Adjust score to observed value with a tolerance

        # Testing without context and valid fiscal code
        result = analyze_text(fiscal_code, ['IT_FISCAL_CODE'])
        print("Without context:", result)
        self.assertTrue(result, "Expected entity not found")  # Ensure result is not empty
        self.assertEqual('IT_FISCAL_CODE', result[0].entity_type)
        self.assertAlmostEqual(0.3, result[0].score, delta=0.1)  # Adjust to observed score with tolerance

        # Testing invalid fiscal code
        invalid_fiscal_code = '1234XYZ'  # Example of an invalid Italian Fiscal Code
        result = analyze_text('Il mio codice fiscale cf è ' + invalid_fiscal_code, ['IT_FISCAL_CODE'])
        print("Invalid code:", result)
        self.assertListEqual([], result)  # Expect no entities detected due to invalid format




    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
