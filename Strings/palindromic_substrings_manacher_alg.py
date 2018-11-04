"""
Given a string, your task is to count how many palindromic substrings
there are in the string.
The substrings with different start indices or end indices are counted as
different substrings even if they consist of the same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c"

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"

Constraints:
The input string length won't exceed 1000
"""
def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    # Pre-processed for Manacher's Algorithm
    s = '#' + '#'.join(s) + '#'

    # Initialization
    m = [0] * len(s)
    maxRight = 0 # The most-right position ever touched by sub-strings
    pos      = 0 # The center for the sub-string touching the maxRight
    maxLen   = 0

    for idx in range(len(s)):
        # check for idx
        if idx < maxRight:
            m[idx] = min(m[2*pos - idx], maxRight - idx) # symmetric to pos
        else:
            m[idx] = 1 # previous sub-strings haven't gone this far

        # expand with taking idx as center
        # pay attention to the boundary
        while (idx-m[idx]) >= 0 and (idx+m[idx]) < len(s) and s[idx-m[idx]] == s[idx+m[idx]]:
            m[idx] += 1

        # update maxRight and pos if needed
        if (m[idx]+idx - 1) > maxRight:
            maxRight = m[idx] + idx - 1
            pos = idx

        # update maxLen
        maxLen = max(maxLen, m[idx])

    # maxLen-1 represents the real length in original string without '#'
    m = [x-1 for x in m]
    return sum([(1+x) // 2 for x in m])
