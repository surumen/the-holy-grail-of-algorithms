"""
LIS Problem.
Given an unsorted array of integers, find the length of the longest increasing
subsequence.
For example, given [10,9,2,5,3,7,101,18], the longest increasing subsequence
is [2,3,7,101]. Therefore, the length is 4

Binary search can be one approach:
    for each num in nums
        if (list.size is 0)
            add num to list
        else if num > last element in list
            add num to list
        else
            replace the element in the list which is the smallest but bigger than num
"""
from __future__ import print_function

def LIS(X):
    m = len(X) # length of array
    # if array X contains only one element, we return it
    # base case for recursion
    if (m <= 1):
        return X
    pivot = X[0]
    isFound = False
    count = 1
    L = []

    while (not isFound and count < m):
        if (X[count] < pivot):
            isFound = True
            temp_X = [element for element in X[count:] if element >= X[count]]
            temp_X = LIS(temp_X)
            if (len(temp_X) > len(L)):
                L = temp_X
            else:
                count +=1

    temp_X = [element for element in X[1:] if element >= pivot]
    temp_X = [pivot] + LIS(temp_X)
    if (len(temp_X) > len(L)):
        return temp_X
    else:
        return L

# Test
# print(LIS([10,9,2,5,3,7,101,18]))
print(LIS([4,8,7,5,1,12,2,3,9]))
print(LIS([9,8,7,6,5,7]))


