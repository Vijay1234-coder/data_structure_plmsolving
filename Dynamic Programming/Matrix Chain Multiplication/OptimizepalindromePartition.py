'''IMPORTANT'''
import sys

'''THIS IS OPTIMIZE Version of Palindrome partision'''

def is_palindrome(s, i, j):
    revString=""
    while i < j:
        if s[i]!=s[j]:
            return False
        i += 1
        j -= 1
    return True


t=[[-1 for i in range(102)]for j in range(102)]
def partition(s,i,j):
    Min = sys.maxsize
    if i>=j: # i==j there will be only 1 char iteself palindrome
        return 0
    if is_palindrome(s,i,j)==True:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    for k in range(i,j):
        if t[i][k]!=-1:
            left =t[i][k]
        else:
            left =partition(s,i,k)
            t[i][k] = left
        if t[k+1][j] != -1:
            right = t[k+1][j]

        else:
            right =partition(s,k+1,j)
            t[k+1][j]=right

        temp = left+ 1 + right
        Min =min(Min,temp)
    t[i][j]= Min
    return t[i][j]




s= "vijjjy"
n =len(s)
print(partition(s,0,n-1))








