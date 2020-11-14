# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:44:00 2020

@author: Oladipo Bolaji
"""
"""





Write a function that converts a Roman numeral into an integer value.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
and M.

Their values are: I: 1 V: 5 X: 10 L: 50 C: 100 D: 500 M: 1000

Roman numerals are usually written largest to smallest from left to right.

For example:

3 is written as III
28 is written as XXVIII
However, there are some exceptions, to Roman numeral conversion: For example, 
the numeral for 4 is not IIII. Instead, the number four is written as IV
 (as the 1 is before the 5, it is subtracted making 1. The same principle 
  applies to the number 9, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Thus, given a roman numeral, convert it to an integer. You can assume
 that input is guaranteed to be within the range from 1 to 3999.
 """
 
 
 
 
 # gets the value if the digits and matches it with 
 # correspondent roman numerals
def int_to_roman(x):
    # Standard values that serve as the building blocks for roman numerals
    digits =[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    numerals = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    val = 12                # total numbers of the standard values
    roman_numerals = ' '    # creates an empty strings to store new values
    while x != 0:           # carries out the matching
        if digits[val] <= x:             # condition for conversion
              roman_numerals += numerals[val]
              x =x-digits[val]
        else:
            val  -= 1
    return roman_numerals
print(int_to_roman(999))