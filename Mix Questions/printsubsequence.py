
t = [[-1 for i in range(1002)]for j in range(1002)]
def find(a,b,m,n):
    if (m==0 and n==0) or n==0:
        return 1
    if m==0:
        return 0
    if t[m][n]!=-1:
        return t[m][n]
    elif a[m-1]==b[n-1]:
        t[m][n]= find(a,b,m-1,n-1)+find(a,b,m-1,n)
        return t[m][n]
    else:
        t[m][n]=find(a,b,m-1,n)
        return t[m][n]




a ="geeks"
b= "gee"
m=len(a)
n =len(b)
print(find(a,b,m,n))