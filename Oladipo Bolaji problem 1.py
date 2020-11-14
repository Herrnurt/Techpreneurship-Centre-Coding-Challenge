# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:43:56 2020

@author: Oladipo Bolaji John
"""

"""
Write a function that computes the list of the first 100 Fibonacci numbers.

By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
 and each subsequent number is the sum of the previous two.

As an example, the first 10 Fibonacci numbers are:
    0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Please start your timer before you attempt this challenge.

"""


def Fibonacci(n):           # function to print the fibonacci numbers
    firstNumber = 0 
    secondNumber = 1
    for number in range(n):       # loops through the given number of series 
        print(firstNumber)        # declares the initial number of the series
        series = firstNumber      # stores the initial number
        firstNumber = secondNumber # second number is stored as first number
        secondNumber = series + secondNumber   # does the increment


def seriesLength():     # function to get the number of series to printed
   print( n = int(input("Enter the number of series you want to be printe :")))

Fibonacci(100)          #list first 100 Fibonacci numbers
