def lcs(x,y,n,m):
    t = [[-1 for i in range(n + 1)] for i in range(m + 1)]
    # Base Case
    for i in range(0,m+1):
        t[i][0]=0
    for j in range(1,n+1):
        t[0][j]=0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if (x[j - 1] == y[i - 1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j]= max(t[i-1][j],t[i][j-1])
    return t[m][n]








x= "AGGTAB"
y= "GXTXAYB"
n=len(x)
m=len(y)

print(lcs(x,y,n,m))
