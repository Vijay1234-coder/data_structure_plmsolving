'''quse'''
'''Sequence Pattern Matching 
a: "AXY"
b: "ABGXJDGY"

Q: if a is subsequnce of b return True else return False
'''
''' Aproach would be first find LCS of a and b then if lcs == len(a) then True '''


def lcs(x,y,n,m):
    t = [[-1 for j in range(n + 1)] for i in range(m + 1)]
    # Base Case

    for i in range(0,m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif (x[j - 1] == y[i - 1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j]= max(t[i-1][j],t[i][j-1])

    if t[m][n] == min(len(x),len(y)):
        return True
    else:
        return False








x= "AXY"
y= "ABGXJDGY"
n=len(x)
m=len(y)

print(lcs(x,y,n,m))
