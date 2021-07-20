'''count all palindromic Subsequnce '''

t = [[-1 for i in range(1002) ]for j in range(1002)]
def palindromCount(s,i,j):
    # base case
    if(i>j):
        return 0
    if(i==j):
        return 1
    if t[i][j]!=-1:
        return t[i][j]
    if s[i]==s[j]:
        t[i][j] = palindromCount(s,i+1,j)+palindromCount(s,i,j-1)+ 1
        return t[i][j]
    else:
        t[i][j] = palindromCount(s,i+1,j)+palindromCount(s,i,j-1)-palindromCount(s,i+1,j-1)  #C(Mc2) +C(c1M)-C(M) M=middle c1=staring char c2 is endinf Char
        return t[i][j]







str1 = "aba"
n = len(str1)
print(palindromCount(str1,0,n-1))