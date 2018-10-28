"""
A subsequence is a sequence that can be derived from another sequence by
deleting some elements without changing the order of the remaining elements.
Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length,
which is common to both the sequences.

Given two sequence of integers, A = [a1...aN] and B=[b1...bM], find any one longest
common subsequence.

In case multiple solutions exist, print any of them.
It is guaranteed that at least one non-empty common subsequence will exist.

Input Format.
First line contains two space separated integers, n and m, where n is the size of
sequence A, while m is the size of sequence B.
In next line there are n space separated integers representing sequence A, and in
third line there are m space separated integers representing sequence B.

n m
A1 A2 ... AN
B1 B2 ... BM

Output Format.
Print the longest common subsequence and each element should be separated by
at least one white-space.
In case of multiple answers, print any one of them.
"""""
n, m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


#create a DP table
# L = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
L = [[0 for j in range(m+1)] for i in range(n+1)] # zero indexed cols and rows so len(B)+1 & A too
seq = [] # to store max sequence

for i, a_i in enumerate(A):
    for j, b_j in enumerate(B):
        if a_i == b_j:
            L[i+1][j+1] = L[i][j] + 1
        else:
            L[i+1][j+1] = max(L[i+1][j], L[i][j+1])

# read the substring out from the matrix
while n != 0 and m != 0:
    if L[n][m] == L[n-1][m]:
        n -= 1
    elif L[n][m] == L[n][m-1]:
        m -= 1
    else:
        assert A[n-1] == B[m-1]
        seq = [A[n - 1]] + seq
        n -= 1
        m -= 1
print(*seq)


