#!/usr/bin/env python

'''
This is the section responsible for being able to run a binarysearch for a given array.
'''
def binarysearch(arr, left, right, num):
        
    if not right >= left:
        return -1
    else:
        mid = left + (right-left) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binarysearch(arr, mid+1, right, num)
        elif arr[mid] > num:
            return binarysearch(arr, left, mid-1, num)
    

def result_binary():
    result = binarysearch(arr, 0, len(arr)-1, num)
    
    if result != -1:
        print(f"The number is present at index {result}")
    else:
        print("The number is not pressent in the array.")

