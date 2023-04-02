"""
This module performs bubble sort on the data.
"""
import sys 
import os
sys.path.append(os.path.abspath("/Users/so43cs/Developer/PRO-Development/python-playground/python-playground/sandbox/algorithms"))
from getData import fetchUnsortedIntList

input = fetchUnsortedIntList()

def bubbleSort(input):
    """ 
    Method perfoming bubble sort, 
    Argument: List of integers
    Returns: Sorted list of integers 
    """
    data = list(input)
    itemCount = len(data)

    for i in range(itemCount): # range(), just create a range for iteration or index
        
        for j in range(0, itemCount - i - 1):

            if data[j] > data[j + 1]:

                data[j], data[j + 1] = data[j + 1], data [j]
    return data

    

