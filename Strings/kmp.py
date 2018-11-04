"""
KMP Algorithm for pattern searching
"""
def kmpSearch(s, pattern):
    """
    KMP search main algorithm: String -> String -> [Int]
    Return all the matching position of pattern string P in S
    """
    def partial(pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
    ## main function
    partial, ret, j = partial(pattern), [], 0

    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = partial[j - 1]
        if s[i] == pattern[j]: j += 1
        if j == len(pattern):
            ret.append(i - (j - 1))
            j = 0
    return ret
