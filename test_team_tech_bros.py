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

        # Valid examples
        p_num = "JF3349917"
        invalid_p = "12ABC5678"
        
        # Test valid passport with context
        result = analyze_text(f"My italiano passaporto number is {p_num}", ['IT_PASSPORT'])
        print(result)
        self.assertEqual('IT_PASSPORT', result[0].entity_type)
        self.assertAlmostEqual(0.4, result[0].score, places=2)

        # Test valid passport without context
        result = analyze_text(f"My number is {p_num}", ['IT_PASSPORT'])
        print(result)
        self.assertEqual('IT_PASSPORT', result[0].entity_type)
        self.assertAlmostEqual(0.01, result[0].score, places=2)

        # Test invalid passports
        result = analyze_text(f"My passaporto number is {invalid_p}", ['IT_PASSPORT'])
        print(result)
        self.assertListEqual([], result)

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""
        # testing with context
        valid_vat = '74575451989'
        result = analyze_text('Il mio numero di partita iva è ' + valid_vat, ['IT_VAT_CODE'])
        print(result)
        self.assertEqual('IT_VAT_CODE', result[0].entity_type)
        self.assertEqual(1.0, result[0].score)

        # testing without context
        result = analyze_text(valid_vat, ['IT_VAT_CODE'])
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
