#!/usr/bin/env python 

from algorithm import binarysearch, result_binary


def binsearch():
    inputs = input("add the length of the array (1 - x); add the number you want to find").split()
    arr = [i for i in range(int(inputs[0]))]
    num = int(inputs[1])

    result_binary(arr, 0, len(arr)-1, num)


