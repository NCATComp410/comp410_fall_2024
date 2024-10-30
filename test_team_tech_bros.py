"""Unit test file for team tech_bros"""
import unittest
import re
from pii_scan import analyze_text, show_aggie_pride  # noqa 
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, RecognizerRegistry, Pattern



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

        # Step 1: Define a custom recognizer for Italian ID pattern (e.g., `Carta d'identità: AY1234567`)
        pattern = Pattern(name="it_id_pattern", regex=r"\b[A-Z]{2}\d{7}\b", score=0.8)  # Example pattern for ID format
        italian_id_recognizer = PatternRecognizer(
            supported_entity="IT_IDENTITY_CARD",
            patterns=[pattern],
        )

        # Step 2: Create a RecognizerRegistry and add the custom recognizer
        registry = RecognizerRegistry()
        registry.add_recognizer(italian_id_recognizer)

         # Step 3: Initialize Presidio Analyzer with the custom registry
        analyzer = AnalyzerEngine(registry=registry)

        #Step 4: Sample Text resembling Italian ID Information
        sample_text = "Mario Rossi, Carta d'identità: AY1234567, issued in Rome"

        #Step 5: Specify the Italian ID Entity Type
        entity_type = "IT_IDENTITY_CARD"

        #Step 6: Run the analysis
        results = analyzer.analyze(
            text=sample_text,
            entities=[entity_type],
            language="en"
        )

        #Step 7: Check the results
        self.assertTrue(any(result.entity_type == entity_type for result in results), "Italian ID Card was not detected")

        #Negative Test Case
        sample_text = "Mario Rossi, Codice Fiscale: CF1234A567B, issued in Rome"
        results = analyzer.analyze(
            text=sample_text,
            entities=[entity_type],
            language="en"
        )
        self.assertFalse(any(result.entity_type == entity_type for result in results), "Italian ID Card was incorrectly detected")


    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
