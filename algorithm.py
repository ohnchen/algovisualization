#/usr/bin/env python

'''
This is the section responsible for being able to run a binarysearch for a given array.
'''
def binarysearch(arr, left, right, num):
    '''
    Search for a number in a sorted array via Binary Search.
    '''
    if not right >= left:
        return -1
    else:
        mid = left + (right-left) // 2  # Split the array in half
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binarysearch(arr, mid+1, right, num) # Pass in new array with half the elements
        elif arr[mid] > num:
            return binarysearch(arr, left, mid-1, num) # ''
    

def result_binary(arr, left, right, num):
    '''
    Give the result of the Binary Search.
    '''
    result = binarysearch(arr, 0, len(arr)-1, num)
    
    if result != -1:
        print(f"The number is present at index {result}")
    else:
        print("The number is not pressent in the array.")



def mergesort(arr):
    '''
    Split array of length n into n subarrays. Mergee the n subarrays in sorted order.
    ''' 
     

def quicksort(arr):
    pass

def insertionsort(arr):
    pass


