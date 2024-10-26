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

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
