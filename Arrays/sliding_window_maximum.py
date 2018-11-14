"""
Given an array and an integer k, find the maximum for each and every
contiguous subarray of size k.

Example1:
Input: [1,2,3,1,4,5,2,3,6]  k=3
Output: 3 3 4 5 5 5 6

Example2:
Input: [8,5,10,7,9,4,15,12,90,13]  k=4
Output: 10 10 10 15 15 90 90

Solution: Approach 1
Run two loops. In the outer loop, take all subarrays of size k.
In the inner loop, get the maximum of the current subarray.
Time complexity: 0(nk)

Approach 2: Use self-balancing BST
• Pick first k elements and create a self-balancing binary search tree
  of size k
• Run a loop for i=0 to n - k
    - get the maximum element from the BST, and print it
    - search for arr[i] in the BST and delete it from the BST
    - insert arr[i+k] into the BST
Time Complexity: step 1 is 0(klogk). steps 2abc is 0(logk).
Total time complexity is 0(nlogk)

Approach 3: Use Deque (most efficient)
Create a deque of capacity k, that stores only useful elements of current
window of k elements. An element is useful if it is in current window
and is greater than all other elements on left side of it in current window.
We process all array elements one by one and maintain Q to contain useful
elements of current window and these useful elements are maintained in
sorted order. The element at from of the Q is the largest and element at
rear of Q is the smallest of current window.
Time Complexity: 0(n)
"""
from collections import deque

def printMax(arr, n, k):
    # Double ended queue will store indexes of useful elements
    # in every window and it will maintain decreasing order of values
    # from front to rear in Q i.e. arr[Q.front()] to arr[Q.rear()] are
    # sorted in decreasing order
    Q = deque()

    # process first k (or first window)
    # elements of array
    for i in range(k):
        # for every element, the previous smaller elements are useless
        # so remove them from Q
        while Q and arr[i] >= arr[Q[-1]] :
            Q.pop()

        # add new element at rear of queue
        Q.append(i)

    # process rest of the elements i.e. from arr[k] to arr[n-1]
    for i in range(k, n):
        # the element at the front of the queue is the largest
        # element of previous window, so print it
        print(str(arr[Q[0]]) + " ", end = "")

        # remove the elements which are out of window
        while Q and Q[0] <= (i-k):
            # remove from front of deque
            Q.popleft()

        # remove all elements smaller than the currently being added
        # element (remove useless elements)
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()

        # add current element at the rear of Q
        Q.append(i)

    # print the maximum element of last window
    print(str(arr[Q[0]]))








