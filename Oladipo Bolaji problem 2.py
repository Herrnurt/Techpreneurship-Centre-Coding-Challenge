# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 03:06:55 2020

@author: Oladipo Bolaji John
"""

"""
Given an array of integers, return how many elements of the array contain an 
even number of digits, and how many contain an uneven number of digits.

For example, for the array [555, 901, 482, 1771], the answer would be:

Even number: 1 element (482)
Odd numbers: 3 elements (555, 901, 1771)
"""
# This function searches though an array to check if its Even or Odd

def findNumbers(integers):
    
    # loopsthough the array, gets the length of the strings and
    # check if its divisible by 2 and prints if its even
        even_number = [i for i in integers if len(str(i)) % 2 == 0]
        print(f"Even numbers: {len(even_number)} elements {(even_number)}")
    
    # loopsthough the array, gets the length of the strings and
    # check if its divisible by 2 and prints if its odd.    
        
        odd_number = [i for i in integers if len(str(i)) % 2 != 0]
        print(f"Odd numbers: {len(odd_number)} elements {(odd_number)}")
findNumbers(integers =[555, 901, 482, 1771])