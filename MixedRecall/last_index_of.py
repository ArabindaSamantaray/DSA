"""
Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
"""

def last_index(arr, target):
    map_number_index = {}
    for index, value in enumerate(arr):
        map_number_index[value]=index
    return map_number_index[target]

def last_index1(arr, target):
    for index in range(len(arr)-1, 0, -1):
        if arr[index]==target:
            return index

arr = [2, 4, 6, 8, 8, 8, 11, 13]
print(last_index(arr, 8))
print(last_index1(arr, 8))
