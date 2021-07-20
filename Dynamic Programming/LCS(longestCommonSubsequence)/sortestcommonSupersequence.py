def shortestCommonSupersequence( X, Y, m, n):
    t = [[0 for i in range(102)] for j in range(102)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    min_supersequence = (m + n) - t[m][n]
    return min_supersequence
X = "abcd"
Y = "xycd"
m =len(X)
n=len(Y)
print(shortestCommonSupersequence(X,Y,m,n))