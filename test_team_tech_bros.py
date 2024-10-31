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
        #testing with context
        dln = 'SS5196744P'
        result = analyze_text('Il mio numero di patente di guida è ' + dln, ['IT_DRIVER_LICENSE'])
        print(result)
        self.assertEqual('IT_DRIVER_LICENSE', result[0].entity_type)
        self.assertEqual(0.55, result[0].score)

        #testing without context
        result = analyze_text('Il mio numero è ' + dln, ['IT_DRIVER_LICENSE'])
        print(result)
        self.assertIn('IT_DRIVER_LICENSE', result[0].entity_type)
        self.assertEqual(0.2, result[0].score)

        #negative test case
        invalid_dln = 'SS238FN'
        result = analyze_text('Il mio numero di patente di guida è ' + invalid_dln, ['IT_DRIVER_LICENSE'])
        print(result)
        self.assertListEqual([], result)

        

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""
        # testing with context
        valid_vat = '74575451989'
        result = analyze_text('Il mio numero di partita iva è ' + valid_vat, ['IT_VAT_CODE'])
        print(result)
        self.assertEqual('IT_VAT_CODE', result[0].entity_type)
        self.assertEqual(1.0, result[0].score)

        # testing without context
        result = analyze_text('I miei valori sono ' + valid_vat, ['IT_VAT_CODE'])
        print(result)
        self.assertEqual('IT_VAT_CODE', result[0].entity_type)
        self.assertEqual(1.0, result[0].score)

        # negative test case
        invalid_vat = '12348945'
        result = analyze_text('Il mio numero di partita iva è ' + invalid_vat, ['IT_VAT_CODE'])
        print(result)
        self.assertListEqual([], result)


if __name__ == '__main__':
    unittest.main()
