"""
Inplace merge sort of array iterative.
"""
import random

def mergeSort(xs):
    unit = 1
    while unit <= len(xs):
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit

            p, q = l, mid
            while p < mid and q < r:
                if xs[p] < xs[q] : p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
        unit *= 2
    return xs

def test():
    assert mergeSort([4,3,2,1]) == [1,2,3,4]
    assert mergeSort([4,2,3,1]) == [1,2,3,4]
    assert mergeSort([4,5,3,2,1]) == [1,2,3,4,5]

    for _ in range(100):
        tmp = range(100)
        random.shuffle(list(tmp))
        assert mergeSort(tmp) == range(100)

    return "All tests passed!"

