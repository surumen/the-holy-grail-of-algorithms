
"""
Example:
Input: "abcabcabcabc"
Output: "True"
Explanation: The substring 'abc' is repeated four times.
"""
def repeatedSubstring(s):
    i = (s+s).find(s, 1, -1)
    if i == -1:
        return False
    else:
        return True
