Suppose that x, y and z are strings. We say that z is a "shuffle" of 
x and y if z can be obtained by mixing the characters from x and y in a way
that preserves the left-to-right ordering of the characters from y.

For example, "OBesFUScCheATIwON" is a shuffle of "eschew" and "OBFUSCATION"

# Question
Given x,y and z, determine whether z is a shuffle of x and y.

## Approach
For this to be true, the last character of z must be equal either to the last
character of x or to the last character of z, and the remaining characters of
of z must be a shuffle of the remaining characters in x and y.

There are also base cases where x or y is empty. If x is the empty string,
then z must be equal to y; and vice versa.

Recursive algorithm:

``` bash
bool isShuffle(string x, string y, string z) {
    int n = x.length();
    int m = y.length();
    int r = z.length();
    if (n == 0)
        return y == z;
    if (m == 0)
        return x == z
```


