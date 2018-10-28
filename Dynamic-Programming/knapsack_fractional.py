"""
Knapsack Problem.
Given a set of items, each with a weight and a value, determine a subset of items
to include in a collection so that the total weight is less than or equal to a
given limit and the total value is as large as possible.

Resource allocation along with some constraint, can be derived in a similar way
as the Knapsack Problem. Examples:
    (i). Finding the least wasteful way to cut raw materials
    (ii). Portfolio optimization
    (iii). Cutting stock problems

Knapsack problems are categorized as:
    a. Fractional knapsack
    b. Knapsack

A. Fractional Knapsack
Items can be broken into smaller pieces, hence the agent can select fractions of
items. 
• there are n items in the store
• weight of i'th item w_i > 0
• profit for i'th item p_i > 0 and
• capacity of the Knapsack is W

Linear Program
The agent may only take a fraction x_i of the i'th item
    0 <= x_i <= 1
Hence, the objective of this algorithm is to maximize
    Sum (from 1 to n):
        x_i * p_i
subject to the constraint
    Sum (from 1 to n):
        (x_i * w_i) <= W
An optimal solution can be obtained by:
    Sum (from 1 to n):
        (x_i * w_i) = W
"""
from itertools import accumulate
from bisect import bisect

def fracKnapsack(p_i, w_i, W, n):
    r = list(sorted(zip(p_i,w_i), key=lambda x:x[0]/x[1], reverse=True))
    p_i = [i[0] for i in r]
    w_i = [i[1] for i in r]
    acc = list(accumulate(w_i))
    k = bisect(acc, W)
    return 0 if k==0 else \
            sum(p_i[:k]) + (W - acc[k-1]) * (p_i[k]) / (w_i[k]) if k!=n else \
            sum(p_i[:k])

print("%.0f"%fracKnapsack([60,100,120],[10,20,30],50,3))
