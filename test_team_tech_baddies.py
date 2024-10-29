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
        # postive test cases
        alpha, numeric = ['A','Z'], ['12345678','87654321']
        for letter in alpha:
            for num in numeric:
                passport = ''.join([letter,num])

                # check with context
                result = analyze_text('My passport number is ' + passport,['IN_PASSPORT'])
                print(result)
                self.assertEqual('IN_PASSPORT', result[0].entity_type)
                self.assertAlmostEqual(0.45, result[0].score, places=2)

                # check with no context
                result = analyze_text('My info is ' + passport,['IN_PASSPORT'])
                self.assertEqual('IN_PASSPORT', result[0].entity_type)
                self.assertEqual(0.1, result[0].score)

        # negative test case - no result found
        result = analyze_text('My passport number is A00000000',['IN_PASSPORT'])
        self.assertListEqual([], result)


    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""
        # Positive test case with context
        voters = ['AaB1234567','CkM9876543','HgN7654321']
        for voter in voters:
            result = analyze_text('My voter resgistration number is '+voter,['IN_VOTER'])
            print(result)
            self.assertEqual('IN_VOTER',result[0].entity_type)
            self.assertEqual(0.75,result[0].score)

        # Positive test case with no context
        result = analyze_text('My voter resgistration number is xyz9876543',['IN_VOTER'])
        print(result)
        self.assertEqual('IN_VOTER',result[0].entity_type)
        self.assertEqual(0.75,result[0].score)

        #negative test case
        result = analyze_text('My voter resgistration number is ABCD1234567',['IN_VOTER'])
        print(result)
        self.assertListEqual([],result)

        


if __name__ == '__main__':
    unittest.main()
