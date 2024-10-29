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
        prefix = ['2345'] 
        mid = ['6789']
        suffix = ['1234']

        # Positive test cases
        for p in prefix:
            for m in mid:
                for s in suffix:
                    aadhaar = ''.join([p, m, s])
                    
                    # Check with context score 
                    result = analyze_text('My Aadhaar is ' + aadhaar, ['IN_AADHAAR'])
                    print("Result with context:", result)
                    
                    if result:
                        self.assertEqual('IN_AADHAAR', result[0].entity_type)
                        self.assertEqual(0.85, result[0].score)
                    else:
                        print("No Aadhaar detected with context for:", aadhaar)

                    # Check without context
                    result = analyze_text('My abc is ' + aadhaar, ['IN_AADHAAR'])
                    print("Result without context:", result)

                    if result:
                        self.assertEqual('IN_AADHAAR', result[0].entity_type)
                        self.assertEqual(0.5, result[0].score)
                    else:
                        print("No Aadhaar detected without context for:", aadhaar)

        # Negative test case (invalid Aadhaar number)
        result = analyze_text('My Aadhaar is 000000000000', ['IN_AADHAAR'])
        print("Negative test result:", result)
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


if __name__ == '__main__':
    unittest.main()
