'''IMPORTANT'''
import sys

'''https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/ 
Palindrome Partitioning using Recursion
Given a string, a partitioning of the string is a palindrome partitioning 
if every substring of the partition is a palindrome. 
if string itself a palindrome return 0
Example:
  “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.
  '''


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
        temp = partition(s,i,k)+ 1 + partition(s,k+1,j)
        Min =min(Min,temp)
    t[i][j]= Min
    return t[i][j]




s= "vijjjy"
n =len(s)
print(partition(s,0,n-1))








