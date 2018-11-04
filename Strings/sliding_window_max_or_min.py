"""
Suppose you have an array A containing n numbers and want to compute the minimum
or maximum of each possible consecutive k elements. Perhaps we want to apply
a maximum filter to an image, or examine how many substrings' maxima meet a certain
criterion.
The naive approach is to write two nested for-loops, running in 0(nk) time.

Deque-based algorithm.
The best approach uses a double-ended queue in a clever way, and runs in
0(n) time using 0(k) space. This example is maximization, but same idea applies
to minimization.
1. The deque shall always represent some kind of processing on a particular
   range of consecutive array elements, e.g. A[i : j]
2. When we increment the array range's right endpoint j to add a new element,
   we manipulate the tail of the deque. Suppose the new element's value is x.
   Looping while the deque is non-empty and its tail element is less than x,
   we remove the tail element. This is because x will be removed later than
   those elements and x is strictly larger, so those other elements will never
   be a range maximum from now on. Finally, add x to the tail of the deque
3. When we increment the array range's left endpoint i to remove a previously
   added element, we manipulate the head of the deque. Suppose the just-removed
   element's value is x. If the deque's head element equals x, then remove the
   head element. This is because x is no longer in the array range, so it cannot
   be in the deque either. Otherwise the deque's head element must be greater
   than x, which means the value x was already removed from the deque at some
   point in the past. The head of the deque cannot possibly be less than x.
"""
import collections, numbers


# ---- Function for one-shot computation ----

def compute(array, window, maximize):
    if not isinstance(window, numbers.Integral):
        raise TypeError()
    if not isinstance(maximize, bool):
	raise TypeError()
    if window <= 0:
	raise ValueError("Window size must be positive")
    result = []
    deque = collections.deque()
    for (i, val) in enumerate(array):
	val = array[i]
	while len(deque) > 0 and ((not maximize and val < deque[-1]) or (maximize and val > deque[-1])):
	    deque.pop()
	    deque.append(val)
	    j = i + 1 - window
	    if j >= 0:
	        result.append(deque[0])
		if array[j] == deque[0]:
		    deque.popleft()
    return result

# ---- Stateful instance for incremental computation ----
class SlidingWindowMinMax(object):

    def __init__(self):
	self.mindeque = collections.deque()
	self.maxdeque = collections.deque()
    def get_minimum(self):
	return self.mindeque[0]

    def get_maximum(self):
    	return self.maxdeque[0]

    def add_tail(self, val):
	while len(self.mindeque) > 0 and val < self.mindeque[-1]:
	    self.mindeque.pop()
	self.mindeque.append(val)
    	while len(self.maxdeque) > 0 and val > self.maxdeque[-1]:
    	    self.maxdeque.pop()
	self.maxdeque.append(val)
    def remove_head(self, val):
	if val < self.mindeque[0]:
	    raise ValueError("Wrong value")
	elif val == self.mindeque[0]:
	    self.mindeque.popleft()
	if val > self.maxdeque[0]:
	    raise ValueError("Wrong value")
	elif val == self.maxdeque[0]:
	    self.maxdeque.popleft()

