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
        net1s = ['168', '192', '255'] #First part of the IP Address
        net2 = ['243', '542', '495']  #Second part of the IP Address
        net3 = ['1']  #Third part of the IP Address
        hostID = ['1', '32', '170'] #Last part of IP and the host ID
        
        IP61 = ['2001:0db8:85a3:','09C0:876A:130B:'] #First part of the IP
        IP62 = ['8a2e:0370:7334','2001:0db8:85a3'] # Second part of the IP
        
        IPAddres = []
        IP6 = []
        for n1 in net1s:
            for n2 in net2:
                for n3 in net3:
                    for h in hostID:
                        IPAddres = '.'.join([n1,n2,n3,h])
                        result = analyze_text('IP_ADDRESS is ' + IPAddres, ['IP_ADDRESS']) #One with Context words
                        result2 = analyze_text('my Address is ' + IPAddres, ['IP_ADDRESS'])#One without context words
                        print('\n',IPAddres)
                        print(result, '\n')
                        print(result2)
                        break
        for IP1 in IP61:
            for IP2 in IP62:
                IP6 = ':'.join([IP1,IP2])
                result = analyze_text('IP_ADDRESS is ' + IP6, ['IP_ADDRESS'])#One with Context words
                result2 = analyze_text('my Road is ' + IP6, ['IP_ADDRESS'])#One without context words
                print('\n',IP6)
                print(result, '\n')
                print(result2)

        #Negative test case
        IPAddres = '192.158. 1' #fake address
        result = analyze_text('IP Address is ' + IPAddres, ['IP_ADDRESS'])
        self.assertListEqual([], result)
        print('\n',result)



if __name__ == '__main__':
    unittest.main()
