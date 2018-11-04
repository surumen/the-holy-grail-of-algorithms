"""
Binary search
"""

def binarySearch(xs, item):
    """
    type: Listof[Val] * Val -> Int
    input: xs :: Sorted list
           item :: Search item
    rtype: the index of the element in the list, -1
           if the element is not in the list
    """
    l, r = 0, len(xs) - 1
    while l <= r:
        mid = (l + r) // 2
        if xs[mid] == item:
            return mid
        elif xs[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


