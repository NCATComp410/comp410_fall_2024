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

    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
