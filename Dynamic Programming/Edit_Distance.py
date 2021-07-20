
''' q: u need to convert str1 to str2 u can perform 1.insert 2.delete 3.replace operation '''
'''return total number of operartion '''
def editDistance(a,b,m,n):
    t =[[0 for i in range(1002)] for j in range(1002)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                t[i][j] = j
            elif j==0:
                t[i][j]=i
            elif a[i-1]==b[j-1]:
                t[i][j] = t[i-1][j-1] # if equal char then do nothing return digonal value
            elif a[i-1]!=b[j-1]:
                t[i][j] = 1 + min(t[i-1][j-1],t[i-1][j],t[i][j-1]) # if not equal then taken min of diagonla,left,top elem then take min add 1

    return t[m][n]





str1 = "sunday"
str2 = "saturday"

m = len(str1)
n = len(str2)
print(editDistance(str1,str2,m,n))
