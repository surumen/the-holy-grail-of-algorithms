"""
Given a string, find the longest substring which is a palindrome.

Solution:
Generate all even length and odd length palindromes and keep track of
the longest palindrome seen so far.

Step to generate odd length palindrome:
Fix a center and expand in both directions for longer palindromes

Step to generate even length palindrom:
Fix two centers (low and high) and expand in both directions for longer
palindromes.
"""""
def longestSubstring(s):
    start = 0
    length = len(s)
    low = 0
    high = 0

    max_length = 1

    # consider every character as center point of even and odd pals
    for i in range(1, length):
        # find longest even length palindrom with center points
        # as i-1 and i
        low = i-1
        high = i
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # find longest odd length palindrome with center as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    # to return the actual palindrome return s[start:start+max_length]
    return max_length


