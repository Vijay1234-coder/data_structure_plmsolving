def longestCommonSubsequence(a, b):

    t = [[0 for j in range(105)] for i in range(105)]
    m = len(a)
    n = len(b)
    s = []

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max( t[i][j - 1], t[i - 1][j])

    i = m
    j = n
    while (i > 0 and j > 0):
        if a[i - 1] == b[j - 1]:
            s.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                j -= 1
            else:
                i -= 1
    return s

a = "thisisvijay"
b = "thisisvijay"
print(longestCommonSubsequence(a,b))