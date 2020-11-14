# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:15:50 2020

@author: Oladipo Bolaji John
"""


"""
Given a sorted array, remove the duplicates such that each element appear only
once and return the new length.
For example, for the array [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5], your function
should return length = 6, with the first five elements of being modified 
to 0, 1, 2, 3, 4, and 7, respectively.


"""

# This function removes duplicates from an array
def removeDuplicates(sorted_numbers= [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5]): 
    
    nums_len = len(sorted_numbers)    # gets the lenght of the array
    count = 0                         # initial value of the count
    
   #This loop checks theinidividual number in the array against the length 
   # of the array. it appends the the number of times each element of
   # the array appear"""
    
    for i in range(1, nums_len):
        if sorted_numbers[count] != sorted_numbers[i]: 
            count = count + 1
            sorted_numbers[count] = sorted_numbers[i] 
    print( count + 1)
removeDuplicates()