"""Unit test file for team tech_baddies"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_tech_baddies(unittest.TestCase):
    """Test team tech_baddies PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

    def test_in_pan(self):
        """Test IN_PAN functionality"""
        #Positive test cases
        #check context
        result = analyze_text('My IN_PAN is AAAPZ1234C', ['IN_PAN'])
        print(result)
        self.assertEqual('IN_PAN', result[0].entity_type)
        self.assertEqual(1.0, result[0].score)

        #check no context
        result = analyze_text('My IN_PAN is 12APZ1234C', ['IN_PAN'])
        print(result)
        self.assertEqual('IN_PAN', result[0].entity_type)
        self.assertEqual(0.4, result[0].score)

        #Negative test cases
        result = analyze_text('My IN_PAN is 0000000000', ['IN_PAN'])
        
        self.assertListEqual([], result)
        

        

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
