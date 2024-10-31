"""Unit test file for team 1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_1(unittest.TestCase):
    """Test team 1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        """Test ES_NIE functionality"""
        country_codes = ['X', 'Y', 'Z']  # Starting letters for NIEs
        digits = ['9613851', '8063915', '8078221']  # 7 digits for NIE
        control_letters = ['N', 'Z', 'M']  # Control letters

        nie_codes = []
        for i, country_code in enumerate(country_codes):
            nie = f"{country_code}{digits[i]}{control_letters[i]}"
            nie_codes.append(nie)

        for nie in nie_codes:
            result = analyze_text('NIE is ' + nie, ['ES_NIE'])
            self.assertEqual('ES_NIE', result[0].entity_type)
            print('\n' + nie)
            print(result)

        # Negative test case
        nie = 'W1234567X'  # Invalid NIE (wrong starting letter)
        result = analyze_text('NIE is ' + nie, ['ES_NIE'])
        self.assertListEqual([], result)
        print('\n', result)

    def test_es_nif(self):
        """Test ES_NIF functionality"""

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""
        birthdays, centuryMarkers, genderMarkers = ['190704', '260923', '051070'], ['A', 'Y'], ['293', '522', '435', '754']

        for date in birthdays:
            for marker in centuryMarkers:
                for num in genderMarkers:
                    checksum = int(date + num) % 31
                    checksum_chars = '0123456789ABCDEFHJKLMNPRSTUVWXY'
                    controlChar = checksum_chars[checksum]
                    hetu = ''.join([date, marker, num, controlChar])
                    result = analyze_text('My personal identity code is ' + hetu, ['FI_PERSONAL_IDENTITY_CODE'])
                    self.assertEqual('FI_PERSONAL_IDENTITY_CODE', result[0].entity_type)
                    print('\n' + hetu)
                    print(result)

        #negative test case
        incorrectHetu = '190704A293B' #Control character at the end is incorrect, should be C
        result = analyze_text('My hetu is ' + incorrectHetu, ['FI_PERSONAL_IDENTITY_CODE'])
        self.assertEqual([], result)
        
        print()
        print(result)

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

        #Positive test cases
        country_codes = ['DE', 'AT'] # Germany & Austria
        check_digits = ['29', '61']
        bank_iden = ['1001', '1904']
        bban = ['0010 0987 6543 21', '3002 3457 3201']

        iban_codes = []
        for i, country_code in enumerate(country_codes):
            iban = f"{country_code} {check_digits[i]} {bank_iden[i]} {bban[i]}"
            iban_codes.append(iban)

        for iban in iban_codes:
            result = analyze_text('IBAN is ' + iban, ['IBAN_CODE'])
            self.assertEqual('IBAN_CODE', result[0].entity_type)
            print('\n'+iban)
            print(result)


        #Negative test case
        iban = 'FI 21 1234 5600 0007 851' # Finland
        result = analyze_text('IBAN is ' + iban, ['IBAN_CODE'])
        self.assertListEqual([], result)
        print('\n',result)


    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
