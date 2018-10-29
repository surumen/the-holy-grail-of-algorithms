"""
Priority Queue implementation for Dijkstra

Used to store vertex set to retrieve node with lowest distance
"""
import sys
import math

class PriorityQueue:
    # Based on Min Heap
    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {} # used to store position of node in array

    def isEmpty(self):
        return self.cur_size == 0

    def min_heapify(self, idx):
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array(lc)[0] < self.array(idx)[0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array(rc)[0] < self.array(smallest)[0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    ## inserts a node into the priority queue
    def insert(self, tup):
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    # Removes and returns the min element at top of priority queue
    def extract_min(self):
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    # Return the index of left child
    def left(self, i):
        return 2 * i + 2

    # Return the index of the right child
    def right(self, i):
        return 2 * i + 2

    # Return the index of the parent
    def par(self, i):
        return math.floor(i / 2)

    # Swap array elements at indices i and j, then update the pos{}
    def swap(self, i, j):
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d):
        idx = self.pos[tup[1]]
        # assuming the new_d is atmost old_d
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)





