'''question'''
'''Count minimum number of deletion to make string palindrome'''
'''approach: S: "aebcbda" solution == (total lenght of string) - (longestpalindromic subsequence) 
because if string is palindrome and its lenght is minimum then by default we have done less deletion so deletion is bydefault minimized
'''


def reverse(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r


def minimumNumberOfDeletions(s):
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
    length = t[m][n]
    result = m - length
    return result


s = "aebcbda"
print(minimumNumberOfDeletions(s))

