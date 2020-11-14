# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 08:53:06 2020

@author: Oladipo  Bolaji
"""


"""
Given a collection of intervals, merge all overlapping intervals.

For example: For the input intervals of [[1,3], [2,6], [8,10], [15,18]], 
the output would be [[1,6], [8,10], [15,18]]. 
Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].


"""

"""
Overlaping means for example when you plot the intervalson a  graph,the 
the range covers by an interval cut across the range cover by another interval,
there is an overlapping""" 


def merge_overlapping(intervals):
# The array is sorted and the first number of the fisrt array is stored in start
    start = sorted([x[0] for x in intervals])

# The array is sorted and the second number of the fisrt array  is stored in end
    end = sorted([x[1] for x in intervals])     # the  start/end lists
    Overlap_interval = []           # creates an empty list to store the result                                                               
    j = 0                       # initial value for end value of the second array
    new_start = 0


# loopthat check for value of each number in each array and checkif there is 
# an overlap with the end value of the second array
    for i in range(len(start)):
        if start[i]<end[j]:
            continue
        else:
            j = j + 1
            Overlap_interval.append([start[new_start], end[j]])
            new_start = i
    print(Overlap_interval) #[[1,3], [2,6], [8,10], [15,18]]
merge_overlapping(intervals = [[1,3], [2,6], [8,10], [15,18]])