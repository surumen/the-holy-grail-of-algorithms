from itertools import islice

def window(seq, n=3):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        if result[0] < result[2] < result[1]:
            print(result)
            return True
    for elem in it:
        result = result[1:] + (elem,)
        if result[0] < result[2] < result[1]:
            print(result)
            return True
    return False


