class RomanNumerals:
    def __init__(self):
        self.romanOrder = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.romanValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_roman_factor(self, factor, n):
        """
        Converts a decimal digit to its corresponding roman representation according to its position within the decimal
        number
        :param factor: must be a decimal number 0-9 in string format
        :param n: indicates the decimal position for the input digit within the number it belongs to:
                    3 for thousands,
                    2 for hundreds,
                    1 for tens,
                    0 for units
        :return: a string with the roman numeral representation for the input digit according to its decimal position
        """
        if factor == '0':
            # an input number equal to zero outputs an empty string (no roman symbol for zero quantity)
            return ''

        factor_value = int(factor)
        distance = abs(5 - factor_value)

        # select the three possible necessary roman symbols to further convert
        # the current digit according to its decimal position
        index_first = min(2 * n, len(self.romanOrder))
        index_second = min(2 * n + 3, len(self.romanOrder))
        roman_letters = self.romanOrder[index_first:index_second]

        # special case: thousands (only the case up to three thousands is taken into account)
        if len(roman_letters) == 1:
            return roman_letters[0] * factor_value

        # compose a string of roman symbols for the current digit
        if factor_value < 5:
            # if input decimal digit is less than 5
            return roman_letters[0] * factor_value if distance > 1 else roman_letters[0] + roman_letters[1]
        else:
            return roman_letters[1] + roman_letters[0] * distance if distance < 4 \
                else roman_letters[0] + roman_letters[2]

    def to_roman(self, number):
        """
        Convert a decimal number to roman number
        :param number: must be a decimal number (no greater than 3999) in string representation
        :return: the roman symbolic representation for the input number in string format
        """
        # check if input decimal number maps directly to a roman number
        for key, value in self.romanValue.items():
            if value == int(number):
                return key
        # fill number with leading zeros up to four digits: thousand, hundred, ten and unit digits
        number = number.zfill(4)
        roman_string = ''
        for n, factor in enumerate(number):
            # loop through each of four decimal digits, convert them to roman numbers, and compose the output string
            roman_string += self.to_roman_factor(factor, len(number) - n - 1)
        return roman_string
