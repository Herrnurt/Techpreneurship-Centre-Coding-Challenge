# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:44:44 2020

@author: USER
"""


"""
Question 6
Given an array of integers nums and an integer k, determine whether there are
two distinct indices i and j in the array where nums[i] = nums[j] and the
absolute difference between i and j is less than or equal to k.

Example: For nums = [0,1,2,3,5,2] and k=3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions
is exactly 3.

For nums = [0,1,2,3,5,2] and k=2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is
more than k.
# A simple program to count pairs with difference k
"""

# loops to get the difference between the absolute values of the integer
def absoluteDifference(integers,nums,k):
    count = 0
     
    # Picks all elements one by one
    for i in range(0, nums):
         
        # See if there is a pair of this picked element
        for j in range(i+1,nums):
            if integers[i] -integers[j] == k or integers [j] - integers[i] == k:
                count += 1
                 
    return count
 
# Driver program
integers = [0,1,2,3,5,2]
nums = len (integers)
k = 3
print("Count of pairs with given diff is ",absoluteDifference
      ( integers = [0,1,2,3,5,2],nums = len (integers),k = 3))
