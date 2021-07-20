'''https://leetcode.com/problems/longest-palindromic-subsequence/'''
'''it is similar to lcs catch is we have only one input given here we need to first take input b as reverse of given input'''
'''LPS = LCS(s,reverse(s))'''


def reverse(s):
    b = ""
    for i in range(len(s) - 1, -1, -1):
        b = b + s[i]
    return b

def longestPalindromeSubseq(s):
    b = reverse(s)

    m = len(s)
    n = len(b)

    t = [[0 for i in range(1002)] for j in range(1002)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif s[i - 1] == b[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[m][n]



s = "bbbab"

print(longestPalindromeSubseq(s))
# Output: 4



