"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 
import sys


def add_numbers(a, b):
    """
    Adds a and b and returns the result
    """
    if a or b > 65535:
        # return coprocessor result
        return a+b
    else:
        return a+b

class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        prefix = ['123', '456']
        mid = ['12']
        suffix = ['1234']

        # positive test cases
        for p in prefix:
            for m in mid:
                for s in suffix:
                    ssn = '-'.join([p,m,s])
                    # check context score should be 0.85
                    result = analyze_text('My SSN is ' + ssn, ['US_SSN'])
                    print(result)
                    self.assertEqual('US_SSN', result[0].entity_type)
                    self.assertEqual(0.85, result[0].score)
                    # check no context
                    result = analyze_text('My abc is ' + ssn, ['US_SSN'])
                    self.assertEqual('US_SSN', result[0].entity_type)
                    self.assertEqual(0.5, result[0].score)

        # negative test case
        result = analyze_text('My SSN is 123-45-6789', ['US_SSN'])
        self.assertListEqual([], result)


    def test_add_numbers(self):
        """Test the add_numbers function"""
        result = add_numbers(1, 1)
        self.assertEqual(2, result)

        # test maxint
        result = add_numbers(sys.maxsize, 1)
        self.assertEqual(sys.maxsize+1, result)


if __name__ == '__main__':
    unittest.main()
