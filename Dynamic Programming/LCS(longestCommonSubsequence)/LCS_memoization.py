
'''RECURSION + MEMOIZATION IS DP'''

def lcs(x,y,n,m):
    # Base Case
    if n==0 or m==0:
        return 0
    if t[m][n]!=-1:
        return t[m][n]
    if (x[n-1]==y[m-1]):
      t[m][n] = 1+lcs(x,y,n-1,m-1)
      return t[m][n]
    else:
        t[m][n]=max(lcs(x,y,n-1,m),lcs(x,y,n,m-1))
        return t[m][n]





x= "AGGTAB"
y= "GXTXAYB"
n=len(x)
m=len(y)
t=[[-1 for i in range(n+1)] for i in range(m+1)]
print(lcs(x,y,n,m))
