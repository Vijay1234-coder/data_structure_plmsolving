'''Find Min Insertion and Deletion to convert string A:"heap" to string B:"pea"   '''
'''note A: heap ,B:pea  in order to convert A to B  we need to remove h and p from A and Add P to A
 Basically here ea is lcs  firstly A is converted to ea then we add P to ea so in order to conver A to ea we need
 to remove 2 char from A i.e Len(A)-lcs and in order to convert ea to pea we need to add 1 char to B i.e
 len(B)-lcs'''

# 0<=m,n <=1000
def minInsertDel(a,b,m,n):
    t = [[0 for i in range(1002)]for j in range(1002)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif a[i-1]==b[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]= max(t[i-1][j],t[i][j-1])
    lcs = t[m][n]
    insertion = m-lcs
    deletion = n -lcs
    return insertion , deletion





a = "heap"
b= "pea"
m = len(a)
n= len(b)
print(minInsertDel(a,b,m,n))