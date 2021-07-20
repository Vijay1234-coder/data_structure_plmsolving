'''Important'''
'''Scramble String using Recursion
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of A = “great”:
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node “gr” and swap its two children, it produces a scrambled string “rgeat”.

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that “rgeat” is a scrambled string of “great”.

Similarly, if we continue to swap the children of nodes “eat” and “at”, it produces a scrambled string “rgtae”.

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that “rgtae” is a scrambled string of “great”.
also "great" is also scramble string of "great" with 0 no. of swaps
'''
def solve(a,b):
    n =len(a)
    if a==b:
        return True
    if len(a)<=1:
        return False
    for i in range(1,n):
        if (solve(a[0:i],b[n-i:])==True and solve(a[i:],b[0:n-i])==True) or (solve(a[0:i],b[0:i])==True and solve(a[i:],b[i:])==True):
            return True
    return False










a = input("enter  sting a")
b = input("enter string b")


if (len(a)!=len(b)) or (len(a)==0 and len(b)==0):
    print(False)
else:
    print(solve(a,b))








