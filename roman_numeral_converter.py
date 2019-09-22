"""Roman numerals consist of seven different symbols:
 I, V, X, L, C, D and M, with the following values 
for each symbol:

Symbol Value

I 1

V 5

X 10

L 50

C 100

D 500

M 1000

The roman numerals are written next to each other and are added, if they are equal or greater in value reading from left to right, to get their Arabic numeral equivalent. For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X II. The number twenty seven is written as XXVII, which is XX V II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Create a function called romanNumeral, that takes as input an integer and returns it's roman numeral. Input is guaranteed to be within the range from 1 to 3000."""


class Converter:
    def int_to_Roman(self, digit: str)-> int:

        arabic = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]

        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

        roman_numeral = ''

        i = 0
        while digit > 0:
            for _ in range(digit // arabic[i]):
                roman_numeral += roman[i]
                digit -= arabic[i]
            i += 1
        return roman_numeral


print(Converter().int_to_Roman(2940))
print(Converter().int_to_Roman(409))