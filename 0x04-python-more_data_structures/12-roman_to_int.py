#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    last = 0
    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if roman[roman_string[c]] >= last:
                number += roman[roman_string[c]]
            else:
                number -= roman[roman_string[c]]
            last = roman[roman_string[c]]
    return number
