# -*- coding: utf-8 -*-

import unittest
from roman_numerals import RomanNumerals


class TestClass(unittest.TestCase):
    def test_case_3(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman('3')
        self.assertEqual(roman_number, 'III')

    def test_case_4(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman('4')
        self.assertEqual(roman_number, 'IV')

    def test_case_5(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman('5')
        self.assertEqual(roman_number, 'V')

    def test_case_1999(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman('1999')
        self.assertEqual(roman_number, 'MCMXCIX')

    def test_case_unit_4(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman_factor('4', 0)
        self.assertEqual(roman_number, 'IV')

    def test_case_unit_7(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman_factor('7', 0)
        self.assertEqual(roman_number, 'VII')

    def test_case_tens_7(self):
        roman_numerals = RomanNumerals()
        roman_number = roman_numerals.to_roman_factor('7', 1)
        self.assertEqual(roman_number, 'LXX')

if __name__ == "__main__":
    unittest.main()
